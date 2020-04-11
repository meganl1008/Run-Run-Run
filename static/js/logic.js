// Create a map object
var myMap = L.map("map", {
  center: [42.3601, -71.0589],
  zoom: 2
});

// Add a tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// An array containing each city's name, location, and population
var cities = [{
  location: [45.5051, -122.6750],
  name: "Portland",
  runner: "Rupp, Galen"
},
{
  location: [0.4261, 35.6902],
  name: "Keringet",
  runner: "Kirui, Geoffrey"
},
{
  location: [35.5467, 139.4386],
  name: "Machida-City",
  runner: "Osako, Suguru"
},
{
  location: [37.6485, -118.9721],
  name: "Mammoth Lakes",
  runner: "Biwott, Shadrack"
},
{
  location: [1.0498, 35.4782],
  name: "Marakwet",
  runner: "Chebet, Wilson"
},
{
  location: [38.8339, -104.8214],
  name: "Colorado Springs",
  runner: "Maiyo, Augustus K."
},
{
  location: [42.3601, -71.0589],
  name: "Boston",
  runner: "Ashe, Eric"
},
{
  location: [30.0799, -95.4172],
  name: "Spring",
  runner: "Varela, Jonnathan"
},
{
  location: [41.9848, -88.0798],
  name: "Roselle",
  runner: "Flanagan, Lindsey"
},
{
  location: [51.5074, -0.1278],
  name: "London",
  runner: "Hall, Matt"
},
{
  location: [38.9072, -77.0369],
  name: "Washington D.C.",
  runner: "Tateishi, Caitlyn Claire"
},
{
  location: [53.5461, -113.4938],
  name: "Edmonton",
  runner: "Stewart, Simon"
},
{
  location: [31.2304, 121.4737],
  name: "Shanghai",
  runner: "Qin, Zhenning"
},
{
  location: [24.8347, 120.9934],
  name: "Zhubei City",
  runner: "Yu, Michael"
},
{
  location: [41.4721, 2.0865],
  name: "Sant Cugat Del Valles",
  runner: "Bel Franquesa, Laura"
},
{
  location: [48.8476, 2.2081],
  name: "Saint Cloud",
  runner: "Petitjean, Damien"
}
];

// Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
for (var i = 0; i < cities.length; i++) {
  var city = cities[i];
  L.marker(city.location)
    .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Runner's Name: " + city.runner + "</h3>")
    .addTo(myMap);
}
