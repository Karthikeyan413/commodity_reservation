# Generated by Django 4.0.4 on 2022-05-17 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('type', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_name', models.CharField(max_length=30)),
                ('train_id', models.IntegerField(primary_key=True, serialize=False)),
                ('no_of_block', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserCredientials',
            fields=[
                ('phone_no', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('dept_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('train_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservationapp.train')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_num', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('block_no', models.IntegerField()),
                ('train_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservationapp.train')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservationapp.commodity')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('train_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservationapp.train')),
            ],
        ),
    ]
