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
    let filteredSlides = allSlides; // Start with all slides

    function updateSlider() {
        // Hide all slides
        allSlides.forEach(slide => slide.style.display = 'none');
        // Show only the filtered slides for the current region, in groups of visibleCount
        filteredSlides.forEach((slide, idx) => {
            if (idx >= current && idx < current + visibleCount) {
                slide.style.display = 'block';
            }
        });
    }

    function prevSlide() {
        current = Math.max(0, current - visibleCount);
        updateSlider();
    }

    function nextSlide() {
        if (current + visibleCount < filteredSlides.length) {
            current += visibleCount;
        }
        updateSlider();
    }

    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);

    // Responsive: recalculate on window resize
    window.addEventListener('resize', updateSlider);

    // Region filtering
    clickableRegions.forEach(region => {
        region.addEventListener('click', function() {
            const regionKey = this.getAttribute('data-region');
            filteredSlides = allSlides.filter(slide => slide.getAttribute('data-region') === regionKey);
            current = 0; // Reset to first slide of the region
            updateSlider();
        });
    });

    const pagination = document.getElementById('slider-pagination');

    function renderPagination() {
        // Calculate number of groups
        const groupCount = Math.ceil(filteredSlides.length / visibleCount);
        pagination.innerHTML = '';
        for (let i = 0; i < groupCount; i++) {
            const bullet = document.createElement('button');
            bullet.className = 'slider-bullet';
            if (i === Math.floor(current / visibleCount)) bullet.classList.add('active');
            bullet.setAttribute('data-group', i);
            bullet.innerHTML = (i + 1); // Or use • for dots
            bullet.addEventListener('click', function() {
                current = i * visibleCount;
                updateSlider();
                renderPagination();
            });
            pagination.appendChild(bullet);
        }
    }

    // Update updateSlider to call renderPagination
    function updateSlider() {
        allSlides.forEach(slide => slide.style.display = 'none');
        filteredSlides.forEach((slide, idx) => {
            if (idx >= current && idx < current + visibleCount) {
                slide.style.display = 'block';
            }
        });
        renderPagination();
    }
    // Initialize
    updateSlider();
});