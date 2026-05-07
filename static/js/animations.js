// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    // Register the ScrollTrigger plugin
    gsap.registerPlugin(ScrollTrigger);

     // Animate the background color of the navigation bar on scroll
     const nav = document.querySelector(".transparent-nav");
     
    ScrollTrigger.create({
        start: "top top", // Trigger when the top of the page is at the top of the viewport
        end: "bottom top", // Optional: Define when the effect ends
        onUpdate: (self) => {
            if (self.direction === 1) {
                // Scrolling down
                // nav.style.backgroundColor = "rgba(0, 0, 0, 0.9)"; // Black background
                // nav.style.boxShadow = "-1px 37px 17px -12px rgba(0,0,0,0.32) inset;"; // Add shadow
                nav.style.boxShadow = "rgba(0, 0, 0, 0.95) 0px 70px 200px 0px inset";
            } else if (self.direction === -1 && self.progress === 0) {
                // Scrolling up and back to the top
                // nav.style.backgroundColor = "transparent"; // Transparent background
                nav.style.boxShadow = "rgba(0, 0, 0, 0.25) 0px 70px 20px 0px inset"; // Subtle shadow
            }
        },
    });

    // Home hero intro sequence and scroll-driven photo reveal
    const hero = document.querySelector("#home_header.home-hero");

    if (hero) {
        const heroMedia = hero.querySelector(".home-hero__media");
        const heroOverlay = hero.querySelector(".home-hero__overlay");
        const heroWords = hero.querySelectorAll(".hero-word");
        const heroSegments = hero.querySelectorAll(".hero-build__segment");
        const heroSlogan = hero.querySelector(".home-hero__slogan");
        const heroExtras = hero.querySelectorAll(".hero-cta, .home-hero__mark, .home-hero__scroll-indicator");
        const heroInner = hero.querySelector(".home-hero__inner");
        const heroMark = hero.querySelector(".home-hero__mark");

        gsap.set([heroWords, heroSegments, heroSlogan, heroExtras], { autoAlpha: 0 });

        const heroTimeline = gsap.timeline({ defaults: { ease: "power3.out" } });

        heroTimeline
            .fromTo(heroMedia, { scale: 1.08 }, { scale: 1, duration: 1.4 }, 0)
            .fromTo(heroWords, { y: 28, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.6, stagger: 0.14 }, 0.1)
            .fromTo(heroSegments, { y: 20, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.45, stagger: 0.16 }, 0.75)
            .to(heroSegments, { y: -12, autoAlpha: 0, duration: 0.35, stagger: 0.08 }, "+=1.0")
            .fromTo(heroSlogan, { y: 18, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.65 }, "-=0.05")
            .fromTo(heroExtras, { y: 18, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.55, stagger: 0.08 }, "-=0.25");

        gsap.to(heroOverlay, {
            opacity: 0.35,
            scrollTrigger: {
                trigger: hero,
                start: "top top",
                end: "bottom top",
                scrub: true,
            },
        });

        gsap.to(heroMedia, {
            scale: 1.08,
            yPercent: 4,
            scrollTrigger: {
                trigger: hero,
                start: "top top",
                end: "bottom top",
                scrub: true,
            },
        });

        gsap.to(heroInner, {
            y: 45,
            autoAlpha: 0.15,
            scrollTrigger: {
                trigger: hero,
                start: "top top",
                end: "bottom top",
                scrub: true,
            },
        });

        if (heroMark) {
            gsap.to(heroMark, {
                y: 30,
                autoAlpha: 0.05,
                scrollTrigger: {
                    trigger: hero,
                    start: "top top",
                    end: "bottom top",
                    scrub: true,
                },
            });
        }
    }

    // Fade in elements with the class "fade-in" on page load
    gsap.from(".fade-in", {
        opacity: 0,
        y: 50,
        duration: 1,
        stagger: 0.3, // Adds a delay between animations for multiple elements
    });

    // Slide up the footer on page load
    gsap.from("footer", {
        y: 100,
        opacity: 0,
        duration: 1,
        ease: "power2.out",
    });

    // Scroll-triggered animations
    // Example 1: Fade in elements when they scroll into view and fade out when scrolling back up
    gsap.fromTo(
        ".scroll-fade-in",
        { opacity: 0, y: 50 }, // Initial state
        {
            opacity: 1,
            y: 0,
            duration: 1,
            scrollTrigger: {
                trigger: ".scroll-fade-in",
                start: "top 80%",
                end: "bottom 20%",
                toggleActions: "play reverse play reverse", // Play forward and reverse on scroll
            },
        }
    );

    // Example 2: Slide in from the left and slide out to the left when scrolling back up
    gsap.fromTo(
        ".scroll-slide-left",
        { opacity: 0, x: -100 }, // Initial state
        {
            opacity: 1,
            x: 0,
            duration: 1,
            scrollTrigger: {
                trigger: ".scroll-slide-left",
                start: "top 90%",
                end: "bottom 20%",
                toggleActions: "play reverse play reverse", // Play forward and reverse on scroll
            },
        }
    );

    // Example 3: Slide in from the right and slide out to the right when scrolling back up
    gsap.fromTo(
        ".scroll-slide-right",
        { opacity: 0, x: 100 }, // Initial state
        {
            opacity: 1,
            x: 0,
            duration: 1,
            scrollTrigger: {
                trigger: ".scroll-slide-right",
                start: "top 90%",
                end: "bottom 20%",
                toggleActions: "play reverse play reverse", // Play forward and reverse on scroll
            },
        }
    );

    // Example 4: Scale up elements when they scroll into view and scale down when scrolling back up
    gsap.fromTo(
        ".scroll-scale-up",
        { opacity: 0, scale: 0.8 }, // Initial state
        {
            opacity: 1,
            scale: 1,
            duration: 1,
            scrollTrigger: {
                trigger: ".scroll-scale-up",
                start: "top 80%",
                end: "bottom 20%",
                toggleActions: "play reverse play reverse", // Play forward and reverse on scroll
            },
        }
    );

    // Example 5: Rotate elements when they scroll into view and rotate back when scrolling back up
    gsap.fromTo(
        ".scroll-rotate",
        { opacity: 0, rotation: 180 }, // Initial state
        {
            opacity: 1,
            rotation: 0,
            duration: 1,
            scrollTrigger: {
                trigger: ".scroll-rotate",
                start: "top 80%",
                end: "bottom 20%",
                toggleActions: "play reverse play reverse", // Play forward and reverse on scroll
            },
        }
    );
});