// Use the jQuery document ready function to ensure the document is fully loaded
$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
