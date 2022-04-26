function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
      document.getElementsByClassName("header")[0].className = "header header-fixed";
    } else {
      document.getElementsByClassName("header")[0].className = "header";
    }
}
window.onscroll = function() {scrollFunction()};