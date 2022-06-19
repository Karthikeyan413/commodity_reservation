function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
      document.getElementsByClassName("header")[0].className = "header header-fixed";
    } else {
      document.getElementsByClassName("header")[0].className = "header";
    }
}
window.onscroll = function() {scrollFunction()};

function cancel(block) {
  ticket_num = block.getAttribute('id')
  if (confirm('Do you want to cancel you ticket!')){
    document.getElementById(ticket_num).className = "none"
    document.getElementsByClassName(ticket_num).className = "block";
  }
  else{
    event.stopPropagation();
    event.preventDefault();
  }
}
blocks = document.getElementsByClassName('block');
for (let index = 0; index < blocks.length; index++) {
  console.log(blocks[index]);
  
}
// blocks.forEach(cancel);