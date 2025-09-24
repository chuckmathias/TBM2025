document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('missionary-slider');
    if (!slider) return;

    const track = slider.querySelector('.slider-track');
    const slides = track.querySelectorAll('.slider-slide');
    const prevBtn = slider.querySelector('.slider-arrow-left');
    const nextBtn = slider.querySelector('.slider-arrow-right');
    const visibleCount = 4;
    let current = 0;

    function updateSlider() {
        const slideWidth = slides[0].offsetWidth;
        track.style.transform = `translateX(-${current * slideWidth}px)`;
    }

    function prevSlide() {
        current = Math.max(0, current - visibleCount);
        updateSlider();
    }

    function nextSlide() {
        if (current + visibleCount < slides.length) {
            current += visibleCount;
        }
        updateSlider();
    }

    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);

    // Responsive: recalculate on window resize
    window.addEventListener('resize', updateSlider);

    // Initialize
    updateSlider();
});