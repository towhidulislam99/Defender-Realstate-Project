/**
* Template Name: EstateAgency
* Template URL: https://bootstrapmade.com/real-estate-agency-bootstrap-template/
* Updated: Mar 17 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Toggle .navbar-reduce
   */
  let selectHNavbar = select('.navbar-default')
  if (selectHNavbar) {
    onscroll(document, () => {
      if (window.scrollY > 100) {
        selectHNavbar.classList.add('navbar-reduce')
        selectHNavbar.classList.remove('navbar-trans')
      } else {
        selectHNavbar.classList.remove('navbar-reduce')
        selectHNavbar.classList.add('navbar-trans')
      }
    })
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Search window open/close
   */
  let body = select('body');
  on('click', '.navbar-toggle-box', function(e) {
    e.preventDefault()
    body.classList.add('box-collapse-open')
    body.classList.remove('box-collapse-closed')
  })

  on('click', '.close-box-collapse', function(e) {
    e.preventDefault()
    body.classList.remove('box-collapse-open')
    body.classList.add('box-collapse-closed')
  })

  /**
   * Intro Carousel
   */
  new Swiper('.intro-carousel', {
    speed: 800,
    loop: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Property carousel
   */
  new Swiper('#property-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.propery-carousel-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * News carousel
   */
  new Swiper('#news-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.news-carousel-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * Testimonial carousel
   */
  new Swiper('#testimonial-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.testimonial-carousel-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Property Single carousel
   */
  new Swiper('#property-single-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.property-single-carousel-pagination',
      type: 'bullets',
      clickable: true
    }
  });

})()



$(document).ready(function() {

  // Animation black layer
 {
  let options = {
    root: null, // Use the viewport as the root
    rootMargin: '0px',
    threshold: 0.1 // Trigger the callback when 10% of the section is visible
};

let observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Element is in view, hide the overlay after 1 second
            setTimeout(() => {
                $(entry.target).find('.black_layer').css('opacity', 0);
            }, 250); // 1 second delay before hiding the overlay
        } else {
            // Element is out of view, ensure the overlay is visible again
            $(entry.target).find('.black_layer').css('opacity', 1);
        }
    });
}, options);

// Observe each .fade-in-section
$('.fade-in-section').each(function() {
    observer.observe(this);
});
 }

  // Animation tab pills
  $('.tabPills_btn').on('click', function(){
    $('.right_to_left').each(function() {
      var section = $(this);
      var windowHeight = $(window).height();
      var scrollTop = $(window).scrollTop();
      var sectionOffset = section.offset().top;
      var sectionHeight = section.height();
      
      // Check if the section is within the viewport and the top of the section is 20px above the bottom of the viewport
      if (scrollTop + windowHeight - 20 > sectionOffset && scrollTop < sectionOffset + sectionHeight) {
        section.css({transform: "translateX(0)", opacity: "1", transition: "1s"});
      } else {
        section.css({transform: "translateX(100%)", opcity: ".2", transition: "1s"});
      }
  });
  });


  // Animation left to right
  setTimeout(() => {
    function checkVisibility() {
      $('.left_to_right').each(function() {
          var section = $(this);
          var windowHeight = $(window).height();
          var scrollTop = $(window).scrollTop();
          var sectionOffset = section.offset().top;
          var sectionHeight = section.height();
          
          // Check if the section is within the viewport and the top of the section is 20px above the bottom of the viewport
          if (scrollTop + windowHeight - 20 > sectionOffset && scrollTop < sectionOffset + sectionHeight) {
            section.css({transform: "translateX(0)", opacity: "1", transition: "1s"});
          } else {
            section.css({transform: "translateX(-100%)", opacity: ".2", transition: "1s"});
          }
      });
    }
  
    // Check visibility on scroll
    $(window).on('scroll', checkVisibility);
  
    // Initial check in case the sections are already in view on page load
    checkVisibility();
  }, 1000);

  // Animation right to left
  setTimeout(() => {
    function checkVisibility() {
      $('.right_to_left').each(function() {
          var section = $(this);
          var windowHeight = $(window).height();
          var scrollTop = $(window).scrollTop();
          var sectionOffset = section.offset().top;
          var sectionHeight = section.height();
          
          // Check if the section is within the viewport and the top of the section is 20px above the bottom of the viewport
          if (scrollTop + windowHeight - 20 > sectionOffset && scrollTop < sectionOffset + sectionHeight) {
            section.css({transform: "translateX(0)", opacity: "1", transition: "1s"});
          } else {
            section.css({transform: "translateX(100%)", opcity: ".2", transition: "1s"});
          }
      });
    }
  
    // Check visibility on scroll
    $(window).on('scroll', checkVisibility);
  
    // Initial check in case the sections are already in view on page load
    checkVisibility();
  }, 1000);
  

   // Animation bottom to top
   setTimeout(() => {
    function checkVisibility() {
      $('.bottom_to_top').each(function() {
          var section = $(this);
          var windowHeight = $(window).height();
          var scrollTop = $(window).scrollTop();
          var sectionOffset = section.offset().top;
          var sectionHeight = section.height();
          
          // Check if the section is within the viewport and the top of the section is 20px above the bottom of the viewport
          if (scrollTop + windowHeight - 20 > sectionOffset && scrollTop < sectionOffset + sectionHeight) {
            section.css({transform: "translateY(0)", opacity: "1", transition: "1s"});
          } else {
            section.css({transform: "translateY(100%)", opcity: ".2", transition: "1s"});
          }
      });
    }
  
    // Check visibility on scroll
    $(window).on('scroll', checkVisibility);
  
    // Initial check in case the sections are already in view on page load
    checkVisibility();
  }, 1000);

  // Animation top to bottom
  setTimeout(() => {
    function checkVisibility() {
      $('.top_to_bottom').each(function() {
          var section = $(this);
          var windowHeight = $(window).height();
          var scrollTop = $(window).scrollTop();
          var sectionOffset = section.offset().top;
          var sectionHeight = section.height();
          
          // Check if the section is within the viewport and the top of the section is 20px above the bottom of the viewport
          if (scrollTop + windowHeight - 20 > sectionOffset && scrollTop < sectionOffset + sectionHeight) {
            section.css({transform: "translateY(0)", opacity: "1", transition: "1s"});
          } else {
            section.css({transform: "translateY(-100%)", opcity: ".2", transition: "1s"});
          }
      });
    }
  
    // Check visibility on scroll
    $(window).on('scroll', checkVisibility);
  
    // Initial check in case the sections are already in view on page load
    checkVisibility();
  }, 1000);
 

  // Golden Card Modal
  let goldenModal = $(".golden_card_modal");
  $("#golden_btn").click(function(e){
    e.preventDefault();
    goldenModal.css({transform: "scale(1)", transition: ".5s"});
  });
  $(".golden_modal_close").click(function(){
    goldenModal.css({transform: "scale(0)", transition: ".5s"});
  });

  // black Card Modal
  let blackModal = $(".black_card_modal");
  $("#black_btn").click(function(e){
    e.preventDefault();
    blackModal.css({transform: "scale(1)", transition: ".5s"});
  });
  $(".black_modal_close").click(function(){
    blackModal.css({transform: "scale(0)", transition: ".5s"});
  });
});

//=========================================================================
//Towhid Modification Code Start Here
// Function to toggle dropdown menu
// scripts.js
document.addEventListener('DOMContentLoaded', function () {
  var navbarToggler = document.getElementById('navbar-toggler');
  var navbarCollapse = document.getElementById('navbarDefault');

  navbarToggler.addEventListener('click', function () {
    if (navbarCollapse.classList.contains('show')) {
      navbarCollapse.classList.remove('show');
    } else {
      navbarCollapse.classList.add('show');
    }
  });
});