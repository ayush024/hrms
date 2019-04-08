//start of scroll
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("headerDesktop").style.top = "0";
  } else {
    document.getElementById("headerDesktop").style.top = "-90px";
  }
  prevScrollpos = currentScrollPos;
}
//end of desktop nav menu
//mobile menu toggler
$(document).ready(function(){
	$('#menu-toggler').click(function(){
	$('.mobile-menu').toggle('active');
	})
})
function submitFunction(){
	var name = document.forms["contact-form"]["name"].value;
	var email = document.forms["contact-form"]["email"].value;
	var number = document.forms["contact-form"]["number"].value;
	var subject = document.forms["contact-form"]["subject"].value;
	var message = document.forms["contact-form"]["message"].value;
	if(name==null||name==""||email==null||email==""||message==null||message==""){
		alert("Text fields cannot be empty");
		}
	else{
		alert("form submitted")
		window.open('mailto:shirishmaharjan71@gmail.com');
		}
	
	}
//end of menu toggler
//get screen size

//end screen size


//slider

//end of slider