$(document).ready(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (content) => {
    $('#hello').text(content.hello);
  });
});
