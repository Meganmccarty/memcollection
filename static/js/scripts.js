// Table for specimen records
var specimenTable = new List('specimen-table', {
    valueNames: [ 'usi', 'order', 'family', 'species', 'country', 'state', 'county', 'locality', 'date', 'collector', 'method' ],
    page: 100,
    pagination: true,
    innerWindow: 2,
    outerWindow: 1
});
// "Table" for images
var imageTable = new List('image-table', {
    valueNames: [ 'name' ],
    page: 100,
    pagination: true,
    innerWindow: 2,
    outerWindow: 1
});

// Table for collecting trips
var collectingTripTable = new List('collecting-trip-table', {
    valueNames: [ 'trip-name', 'start-date', 'end-date' ]
});

// Table for species pages (as well as options)
var optionsSpeciesPages = {
    valueNames: [ 'species-page', 'authority', 'common-name', 'mona', 'p3' ]
};

var eudaminaePageTable = new List('eudaminae-page-table', optionsSpeciesPages);
var pyrginaePageTable = new List('pyrginae-page-table', optionsSpeciesPages);
var heteropterinaePageTable = new List('heteropterinae-page-table', optionsSpeciesPages);
var hesperiinaePageTable = new List('hesperiinae-page-table', optionsSpeciesPages);
var parnassiinaePageTable = new List('parnassiinae-page-table', optionsSpeciesPages);
var papilioninaePageTable = new List('papilioninae-page-table', optionsSpeciesPages);
var coliadinaePageTable = new List('coliadinae-page-table', optionsSpeciesPages);
var pierinaePageTable = new List('pierinae-page-table', optionsSpeciesPages);
var miletinaePageTable = new List('miletinae-page-table', optionsSpeciesPages);
var lycaeninaePageTable = new List('lycaeninae-page-table', optionsSpeciesPages);
var theclinaePageTable = new List('theclinae-page-table', optionsSpeciesPages);
var polyommatinaePageTable = new List('polyommatinae-page-table', optionsSpeciesPages);
var riodininaePageTable = new List('riodininae-page-table', optionsSpeciesPages);
var libytheinaePageTable = new List('libytheinae-page-table', optionsSpeciesPages);
var danainaePageTable = new List('danainae-page-table', optionsSpeciesPages);
var heliconiinaePageTable = new List('heliconiinae-page-table', optionsSpeciesPages);
var limenitidinaePageTable = new List('limenitidinae-page-table', optionsSpeciesPages);
var apaturinaePageTable = new List('apaturinae-page-table', optionsSpeciesPages);
var nymphalinaePageTable = new List('nymphalinae-page-table', optionsSpeciesPages);
var charaxinaePageTable = new List('charaxinae-page-table', optionsSpeciesPages);
var satyrinaePageTable = new List('satyrinae-page-table', optionsSpeciesPages);

// Pagination buttons for all tables
 $('.next').on('click' , function(){
      $('.pagination').find('.active').next().trigger( "click" );
 });

 $('.previous').on('click' , function(){
       $('.pagination').find('.active').prev().trigger( "click" );
 });

