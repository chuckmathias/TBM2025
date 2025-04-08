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