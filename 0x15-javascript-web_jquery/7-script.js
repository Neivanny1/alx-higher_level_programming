// fetches and replaces the name of the URL
$.get('http://swapi.co/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});
