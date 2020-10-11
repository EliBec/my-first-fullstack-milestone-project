toTopButton = document.getElementById("return-to-top-btn");

    window.onscroll = function() {scrollFunction()};

    // Show the button after scrolling 20px down the screen.
    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            toTopButton.classList.add("setBackTop");
        } 
        else {
            toTopButton.classList.add("setHiddenTop");
            toTopButton.classList.remove("setBackTop");
        }
    }

    function topFunction() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    }


