from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect

from reservationapp.forms import RegisterForm,RegisterNoForm
from reservationapp.models import Route, Train, Time, Ticket, Commodity

import random
# Create your views here.

@csrf_protect
def register_user(request):
    if(request.user.is_authenticated):
        logout(request)
    registered = False
    if request.method == 'POST':
        form_register = RegisterForm(data=request.POST)

        if form_register.is_valid() :
            user = form_register.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            return render(request, 'login/registration.html', { 
                'form_register' : form_register,
                })
    else:
        form_register = RegisterForm()
    if(registered):
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'login/registration.html', {
                                                'form_register': form_register,
                                                 })

@csrf_protect
def user_login(request):
    if(request.user.is_authenticated):
        logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        user = authenticate(username=username, password=password)

        if user:
            if(user.is_active):
                login(request, user)
                return HttpResponseRedirect('/')

            else:
                return HttpResponse("Account Not Active")
        else:
            # print("u={}p={}".format(username, password))
            return render(request, 'login/login.html', {'invaliduser': True})
    else:
        return render(request, 'login/login.html', {})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def availability(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        source = request.POST.get('source')
        type = request.POST.get('type')
        request.session['selected_type'] = type

        routes = Route.objects.all()
        ltrain_ids=[]
        for route in routes:
            if(route.source == source and route.destination == destination):
                ltrain_ids.append(route.train_id_id)
        
        trains = Train.objects.all()
        ltrains=[]
        for train in trains:
            if(train.train_id in ltrain_ids):
                ltrains.append(train)
        
        time = Time.objects.all()
        
        ltime=[]
        for t in time:
            if(t.train_id_id in ltrain_ids):
                ltime.append(t)

        ldetails=[]
        for i in range(len(ltrain_ids)):
            ldetails.append(tuple((ltrains[i],ltime[i])))

        return render(request, 'availability.html', {'ldetails': ldetails})

    
    else:
        return render(request, 'reservation.html')

@login_required(login_url='/login')
def reservation(request,reservation_id):

    train = Train.objects.get(train_id=reservation_id)
    ticket = Ticket()

    ticket.ticket_num = random.randint(1, 100)
    request.session['ticket_num'] = ticket.ticket_num
    ticket.user = request.user
    ticket.train_id = train
    ticket.type = Commodity.objects.get(type = request.session.get('selected_type'))
    ticket.block_no = random.randint(1,int(train.no_of_block))
    ticket.save()

    return HttpResponseRedirect('/tickets')
    
    
    # return render(request, 'reservation.html')
@login_required(login_url='/login')
def ticket(request):
    ticket = Ticket.objects.get(ticket_num = request.session.get('ticket_num'))
    return render(request, 'ticket.html', {'ticket' : ticket})

@login_required(login_url='/login')
def profile(request):
    if(request.method == 'POST'):
        if request.user.is_superuser:
            print("Not permitted")
            return HttpResponse("Superuser can not be deleted")
        try:
            user = User.objects.get(username=request.user.username)
            user.delete()
            return HttpResponseRedirect('/login')
        except:
            return HttpResponse("Some other error")
            
    else:
        profile_info = User.objects.get(username = request.user)
        tickets = Ticket.objects.filter(user = request.user)
        return render(request, 'profile.html', {'profile_info' : profile_info, 'tickets' : tickets} )