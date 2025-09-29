document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('missionary-slider');
    if (!slider) return;

    const clickableRegions = document.querySelectorAll('.map-region.clickable');
    const track = slider.querySelector('.slider-track');
    const allSlides = Array.from(track.querySelectorAll('.slider-slide'));
    const prevBtn = slider.querySelector('.slider-arrow-left');
    const nextBtn = slider.querySelector('.slider-arrow-right');
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
        // Optionally, keep your transform for animation
        track.style.transform = `translateX(-${current * allSlides[0].offsetWidth}px)`;
        renderPagination();
    }

    function prevSlide() {
        current = Math.max(0, current - visibleCount);
        updateSlider();
    }

    function nextSlide() {
        if (current + visibleCount < allSlides.length) {
            current += visibleCount;
        }
        updateSlider();
    }

    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);

    window.addEventListener('resize', updateSlider);

    // Region jump with animation
    clickableRegions.forEach(region => {
        region.addEventListener('click', function() {
            const regionKey = this.getAttribute('data-region');
            const targetIdx = allSlides.findIndex(slide => slide.getAttribute('data-region') === regionKey);
            if (targetIdx >= 0) {
                current = targetIdx;
                updateSlider();
            }
        });
    });

    const pagination = document.getElementById('slider-pagination');

    function renderPagination() {
        const groupCount = Math.ceil(allSlides.length / visibleCount);
        pagination.innerHTML = '';
        for (let i = 0; i < groupCount; i++) {
            const bullet = document.createElement('button');
            bullet.className = 'slider-bullet';
            if (i === Math.floor(current / visibleCount)) bullet.classList.add('active');
            bullet.setAttribute('data-group', i);
            bullet.innerHTML = (i + 1);
            bullet.addEventListener('click', function() {
                current = i * visibleCount;
                updateSlider();
            });
            pagination.appendChild(bullet);
        }
    }

    updateSlider();
});