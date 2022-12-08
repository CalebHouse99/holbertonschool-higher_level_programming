const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, (data) => {
  const name = data.name;
  $('DIV#character').text(name);
});