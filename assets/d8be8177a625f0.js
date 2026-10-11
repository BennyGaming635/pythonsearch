(function ($) {
	jQuery(document).ready(function () {
		console.log("theme custom.js is running");

		//add class on scroll
		$(window).bind("scroll", function () {
			if ($(window).scrollTop() > 10) {
				$("body").addClass("scrolled");
			} else {
				$("body").removeClass("scrolled");
			}
		});

		$(function () {
			$(".mega-desktop-menu-toggle > a").click(function () {
				$(this).text(function (i, text) {
					return text === "Menu" ? "Close" : "Menu";
				});
			});
		});

		//search button toggle
		$(".bn-search-toggle").click(function () {
			$("#searchform-header").slideToggle();
			$(".searchinput").focus();
			$(this).toggleClass("active");
		});
		$(".close-search").click(function () {
			$("#searchform-header").slideUp();
		});

		//show/hide mobile menu
		$(".bn-mainmenu-toggle").click(function () {
			$(".bn-megamenu-wrap").slideToggle();
			$("#socials-container").slideToggle(); // Add this line
			$(this).toggleClass("active");
			$("body").toggleClass("mainmenu-active");
		});

	}); // end doc ready
})(jQuery); //end compatibility

//lazy loading animation
const elements = document.querySelectorAll("#content .wp-block-column:not(.wp-block-group):not(.wp-block-lazyblock-henley-separator-left):not(.henley-separator):not(.wp-block-lazyblock-staff-page):not(.wp-block-lazyblock-staff-page > *)");
const options = {
		root: null,
		rootMargin: "200px",
		threshold: 0,
	};
	const callbacks = (entries) => {
		entries.forEach((entry) => {
			if (entry.isIntersecting) {
				entry.target.classList.add("revealed");
			}
		});
	};
	let bn_observer = new IntersectionObserver(callbacks, options);
	elements.forEach((element) => {
		bn_observer.observe(element);
	});