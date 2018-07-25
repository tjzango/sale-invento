$(function () {
  var bgs = ['banner.jpg', 'cat-fish.jpg', 'chicken.jpg'];

  
  $(window).scroll(function () {

    var level = $(window).scrollTop();
    if (level < 255) {
      $('.header-top').css('background', 'rgb(0, 0, 0, .41)' ).removeClass('invert')
    } else  {
      level /= 2
      var opacity = level / 255;
      opacity = opacity < .5 ? .5 : opacity
      $('.header-top').css('background', 'rgb(' + level + ', ' + level + ', ' + level + ', ' + opacity + ')' )
      if (opacity < .7) {
        $('.header-top').removeClass('invert')
      } else {
        $('.header-top').addClass('invert')
      }
    }
  })
  changeBg(0)
})