// adds an LI element to a list when the user clicks on DIV#add_item
const item = "<li>Item</li>"
$('#add_item').click(function () {
  $('.my_list').append(item);
});
