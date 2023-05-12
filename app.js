// This function retrieves the value of the selected bathroom count from the UI
function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

// This function retrieves the value of the selected BHK count from the UI
function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

// This function is called when the "Estimate Price" button is clicked and makes an HTTP POST request to a Flask server using jQuery
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  // Construct the URL for making the HTTP POST request
  var url = "http://127.0.0.1:5000/predict_home_price"; 

  // Make the HTTP POST request using jQuery
  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value
  },function(data, status) {
      console.log(data.estimated_price);

      // Update the UI with the estimated price returned by the server
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

// This function is called when the page loads and retrieves the list of locations from the Flask server using jQuery
function onPageLoad() {
  console.log( "document loaded" );
  // Construct the URL for making the HTTP GET request
  var url = "http://127.0.0.1:5000/get_location_names";

  // Make the HTTP GET request using jQuery
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          // Clear the options in the location dropdown and add the new options from the server
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

// This function is set as the handler for the window's onload event and is called when the page finishes loading
window.onload = onPageLoad;
