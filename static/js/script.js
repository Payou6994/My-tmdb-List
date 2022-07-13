$(function () {
  var didScroll;
  var lastScrollTop = 0;
  var delta = 10;
  var navbarHeight = $('#navbar').outerHeight();

  $(window).scroll(function (event) {
    didScroll = true;
    console.log('scroll');
  });

  setInterval(function () {
    if (didScroll) {
      hasScrolled();
      didScroll = false;
    }
  }, 250);

  function hasScrolled() {
    var st = $(this).scrollTop();

    if (Math.abs(lastScrollTop - st) <= delta)
      return;

    if (st > lastScrollTop && st > navbarHeight) {
      $('#navbar').removeClass('nav-down').addClass('nav-up');
      console.log('affiche nav bar');
    } else {
      if (st + $(window).height() < $(document).height()) {
        $('#navbar').removeClass('nav-up').addClass('nav-down');
        console.log('masque nav bar');
      }
    }

    lastScrollTop = st;
  }
});