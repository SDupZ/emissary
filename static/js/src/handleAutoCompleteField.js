// This example displays an address form, using the autocomplete feature
// of the Google Places API to help users fill in the information.

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

var placeSearch, autocomplete;
var addresstypes = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  country: 'long_name',
  postal_code: 'short_name'
};

var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  country: 'long_name',
  postal_code: 'short_name'
};

function initAutocomplete() {
  // Create the autocomplete object, restricting the search to geographical
  // location types.
  autocomplete_origin = new google.maps.places.Autocomplete(
      /** @type {!HTMLInputElement} */(document.getElementById('autocomplete_origin')),
      {types: ['geocode']});

  autocomplete_destination = new google.maps.places.Autocomplete(
      /** @type {!HTMLInputElement} */(document.getElementById('autocomplete_destination')),
      {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocomplete_origin.addListener('place_changed', updateOriginAddress);
  autocomplete_destination.addListener('place_changed', updateDestinationAddress);
}

function updateAddressArray(place) {
    // Get each component of the address from the place details
    // and fill the corresponding field on the form.
    for (var i = 0; i < place.address_components.length; i++) {
      var addressType = place.address_components[i].types[0];
      if (addresstypes[addressType]) {
          var val = place.address_components[i][addresstypes[addressType]];
          componentForm[addressType] = val;
      }
    }
}
function updateOriginAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete_origin.getPlace();

  updateAddressArray(place);

  document.getElementById('origin_street_number').value = Object.values(componentForm)[0]
  document.getElementById('origin_street_name').value = Object.values(componentForm)[1]
  document.getElementById('origin_city').value = Object.values(componentForm)[2]
  document.getElementById('origin_country').value = Object.values(componentForm)[3]
  document.getElementById('origin_post_code').value = Object.values(componentForm)[4]
}


function updateDestinationAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete_destination.getPlace();

  updateAddressArray(place);

  document.getElementById('destination_street_number').value = Object.values(componentForm)[0]
  document.getElementById('destination_street_name').value = Object.values(componentForm)[1]
  document.getElementById('destination_city').value = Object.values(componentForm)[2]
  document.getElementById('destination_country').value = Object.values(componentForm)[3]
  document.getElementById('destination_post_code').value = Object.values(componentForm)[4]
}
