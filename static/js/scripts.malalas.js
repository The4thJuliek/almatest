/*
 * scrollt zwischen Anker und Link in Edition
 * beruht darauf, dass derartige Link-IDs mit '#K' beginnen
*/
$(document).ready(function(){
  $('a[href^="#K"]').on('click',function (e) {
    e.preventDefault();
    var target = this.hash;
    var $target = $(target);
    $('html, body').stop().animate({
      'scrollTop': $target.offset().top
      }, 900, 'swing', function () {
        window.location.hash = target;
      });
  });
  $("#book, #chapter").change(function () {
        var book = document.getElementById("book").value;
        var chapter = document.getElementById("chapter").value;
        target_url = "/kommentar/" + book + "/" + chapter
        window.open(target_url, "_self")
    });
});











