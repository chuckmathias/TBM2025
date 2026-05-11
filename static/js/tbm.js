document.addEventListener('DOMContentLoaded', function() {
    // Select all region toggle buttons and map regions
    const toggleBtns = document.querySelectorAll('.toggle-btn');
    const mapRegions = document.querySelectorAll('.map-region.clickable');
    const sliderTrack = document.querySelector('.slider-track');
    const allSlides = Array.from(sliderTrack.querySelectorAll('.slider-slide'));
    const visibleCount = 4;
    let current = 0;

    function updateSlider() {
        allSlides.forEach((slide, idx) => {
            if (idx >= current && idx < current + visibleCount) {
                slide.classList.add('visible');
            } else {
                slide.classList.remove('visible');
            }
        });
        // Calculate the offset accounting for the gap (1rem = 16px)
        const slideWidth = allSlides[0].offsetWidth;
        const gapWidth = 16; // 1rem in pixels
        const totalSlideSpace = slideWidth + gapWidth;
        sliderTrack.style.transform = `translateX(-${current * totalSlideSpace}px)`;
        renderPagination();
    }

    function renderPagination() {
        const pagination = document.getElementById('slider-page-indicator');
        const groupCount = Math.ceil(allSlides.length / visibleCount);
        const currentPage = Math.floor(current / visibleCount);

        pagination.innerHTML = '';
        for (let i = 0; i < groupCount; i++) {
            const bullet = document.createElement('button');
            bullet.className = 'slider-bullet';
            if (i === currentPage) bullet.classList.add('active');
            bullet.setAttribute('data-group', i);
            bullet.innerHTML = (i + 1);
            bullet.addEventListener('click', function() {
                current = i * visibleCount;
                updateSlider();
            });
            pagination.appendChild(bullet);
        }
    }

    // Helper: activate region everywhere and jump slider
    function activateRegion(regionKey) {
        // Highlight map region
        mapRegions.forEach(r => r.classList.remove('active'));
        const svgRegion = document.querySelector('.map-region.clickable[data-region="' + regionKey + '"]');
        if (svgRegion) svgRegion.classList.add('active');

        // Highlight toggle button
        toggleBtns.forEach(b => b.classList.remove('active'));
        const btn = document.querySelector('.toggle-btn[data-region="' + regionKey + '"]');
        if (btn) btn.classList.add('active');

        // Jump slider to region
        const targetIdx = allSlides.findIndex(slide => slide.getAttribute('data-region') === regionKey);
        if (targetIdx >= 0) {
            current = targetIdx;
            updateSlider();
        }
    }

    function prevSlide() {
        const groupCount = Math.ceil(allSlides.length / visibleCount);
        if (current - visibleCount < 0) {
            // Go to last page (wrap around)
            current = (groupCount - 1) * visibleCount;
        } else {
            current -= visibleCount;
        }
        updateSlider();
    }

    function nextSlide() {
        const groupCount = Math.ceil(allSlides.length / visibleCount);
        if (current + visibleCount >= allSlides.length) {
            // Go to first page (wrap around)
            current = 0;
        } else {
            current += visibleCount;
        }
        updateSlider();
    }

    // Toggle button click
    toggleBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const regionKey = btn.getAttribute('data-region');
            activateRegion(regionKey);
        });
    });

    // Map region click
    mapRegions.forEach(region => {
        region.addEventListener('click', function(e) {
            e.preventDefault();
            const regionKey = region.getAttribute('data-region');
            activateRegion(regionKey);
        });
    });

    document.querySelector('.slider-arrow-left').addEventListener('click', prevSlide);
    document.querySelector('.slider-arrow-right').addEventListener('click', nextSlide);

    // Initial slider setup
    updateSlider();

    // Testimonial carousel setup
    const testimonialCarousel = document.getElementById('envision-testimonial-carousel');
    if (testimonialCarousel) {
        const testimonialCards = Array.from(testimonialCarousel.querySelectorAll('.envision-testimonial-card'));
        let currentTestimonial = 0;

        if (testimonialCards.length > 0) {
            // Set first testimonial as active
            testimonialCards[0].classList.add('active');

            // Cycle through testimonials every 8 seconds (if more than one exists)
            if (testimonialCards.length > 1) {
                setInterval(() => {
                    testimonialCards[currentTestimonial].classList.remove('active');
                    currentTestimonial = (currentTestimonial + 1) % testimonialCards.length;
                    testimonialCards[currentTestimonial].classList.add('active');
                }, 8000);
            }
        }
    }
});