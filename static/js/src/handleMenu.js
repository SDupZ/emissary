(function() {
    var active = false;
    var menuIcon = $('.menu-icon');
    var body = $('body');

    var toggleMenu = function() {
      if (!active) {
          active = true;
          openMenu();
      } else {
          active = false;
          closeMenu();
      }
  };

    var click = 'click';
    if( 'ontouchstart' in window ){
        click = 'touchstart';
    }

    menuIcon.on(click, toggleMenu);

    // $('div.menu ul li a').on(click, function(e){
    //     e.preventDefault();
    //     closeMenu();
    // });


    function openMenu(){
        //Show Menu
        menuIcon.addClass("is-active");
        // body.addClass("noscroll");

        $('div.menu-bg').addClass('animate');
        $('.menu li').addClass('animate');
    }

    function closeMenu(){

        //Hide Menu
        menuIcon.removeClass("is-active");
        // body.removeClass("noscroll");

        $('.menu li').removeClass('animate');
        setTimeout(function(){
            $('div.menu-bg').removeClass('animate');
        }, 100);

    }
}());
