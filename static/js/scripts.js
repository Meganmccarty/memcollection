var specimenTable = new List('specimen-table', {
    valueNames: [ 'usi', 'order', 'family', 'species', 'country', 'state', 'county', 'locality', 'date', 'collector', 'method' ],
    page: 100,
    pagination: true,
    innerWindow: 2,
    outerWindow: 1
});

var imageTable = new List('image-table', {
    valueNames: [ 'name' ],
    page: 100,
    pagination: true,
    innerWindow: 2,
    outerWindow: 1
});

var collectingTripTable = new List('collecting-trip-table', {
    valueNames: [ 'trip-name', 'start-date', 'end-date' ]
});

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

 $('.next').on('click' , function(){
      $('.pagination').find('.active').next().trigger( "click" );
 });

 $('.previous').on('click' , function(){
       $('.pagination').find('.active').prev().trigger( "click" );
 });

