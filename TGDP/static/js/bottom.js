
    //Get the button
    var mybutton = document.getElementById("myBtn");
    
    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};
    
    function scrollFunction() {
      // if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "inline-block";
      // } else {
        // mybutton.style.display = "none";
      // }
    }
    
    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
   
    



// down button

    
    
    var downbutton = document.getElementById("downBtn");
    
   
    window.onscroll = function() {scrolldownFunction()};
    
    function scrolldownFunction() {
        downbutton.style.display = "inline-block";
      
    }
    
    
    function downFunction() {
      window.scrollTo(0, 20000);
    }
   
