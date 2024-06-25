MAPPY
This project demonstrates an extended Leaflet map application integrated with various features such as tile layers, marker clustering, GeoJSON data handling, drawing tools, geocoding, and fullscreen mode.

Features
Map Layers:

OpenStreetMap as the default base layer.
Additional tile layers from Google Maps (Streets, Satellite, Terrain, Hybrid) for varied map views.
Marker Clustering:

Utilizes Leaflet.markercluster plugin to cluster markers for improved performance and visualization.
GeoJSON Data:

Loads GeoJSON data (indiadata and choice_location) to display points on the map with interactive popups showing location details.
Drawing Tools:

Leaflet.draw plugin integrated for drawing and editing features such as polyline, polygon, circle, rectangle, and marker.
Geocoding:

Mapbox Geocoding API used to fetch and display detailed place information when clicking on the map.
Fullscreen Mode:

Includes a fullscreen control (L.Control.Fullscreen) allowing users to view the map in fullscreen mode.
Event Handling:

Handles events like drawing creation, editing, deletion, and map clicks with debouncing to optimize performance.
Usage
Setup:

Clone the repository or download the HTML file (index.html) and associated JavaScript files (indiadata.js, choice_location.js).
Open in Browser:

Open index.html in a web browser that supports JavaScript.
Explore the Map:

Navigate the map using zoom controls and layer selection in the top-right corner.
Use drawing tools to create and edit features on the map.
Click on markers or draw on the map to view popup details and geocoded information.
Fullscreen Mode:

Click on the fullscreen button (top-left corner) to expand the map to fullscreen mode.
Exit fullscreen mode using the provided control.
Credits
Leaflet: Open-source JavaScript library for mobile-friendly interactive maps.
Leaflet.markercluster: Plugin for clustering markers on the map.
Leaflet.draw: Plugin for drawing and editing features on the map.
Control.Geocoder: Plugin for geocoding and displaying location information.
Mapbox: Provides geocoding API used in this project.
Google Maps: Provides additional tile layers for different map views.
License
This project is licensed under the MIT License - see the LICENSE file for details.

