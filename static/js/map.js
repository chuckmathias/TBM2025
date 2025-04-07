document.addEventListener("DOMContentLoaded", () => {
    const mapElement = document.getElementById("map");

    if (mapElement) {
        const latitude = parseFloat(mapElement.dataset.latitude);
        const longitude = parseFloat(mapElement.dataset.longitude);

        if (!isNaN(latitude) && !isNaN(longitude)) {
            // Initialize the MapTalks map
            const map = new maptalks.Map("map", {
                center: [longitude, latitude], // MapTalks uses [lng, lat] format
                zoom: 7,
                baseLayer: new maptalks.TileLayer("base", {
                    urlTemplate: "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png",
                    subdomains: ["a", "b", "c"],
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/">CARTO</a>',
                }),
            });

            // Configure map interactions
            map.config({
                scrollWheelZoom: false, // Disable scroll zooming
                draggable: true, // Enable dragging
                doubleClickZoom: true, // Enable zooming on double-click
                touchZoom: true, // Enable touch-based zooming
            });

            // Add zoom controls
            map.addControl(new maptalks.control.Zoom({
                position: 'top-right', // Position of the zoom control
            }));

            // Add scale control
            map.addControl(new maptalks.control.Scale({
                position: 'bottom-left', // Position of the scale control
            }));

            // Add a custom image marker for the missionary's location
            new maptalks.Marker([longitude, latitude], {
                symbol: {
                    markerFile: "/static/images/tbm-marker.png", // Path to your custom marker image
                    markerWidth: 60, // Width of the marker
                    markerHeight: 40, // Height of the marker
                },
            }).addTo(new maptalks.VectorLayer("vector").addTo(map));
        } else {
            console.error("Invalid latitude or longitude provided for the map.");
        }
    }
});