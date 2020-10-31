// BackToTop button functionality
var toTopButtonElem = document.getElementById('return-to-top-btn');
if (toTopButtonElem != null) { 
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
    
}

// sorting functionality 
var sortingElem = document.getElementById('sort-option'); 
if (sortingElem != null) { 

    $('#sort-option').change(function() {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if(selectedVal != "reset"){
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    })
}

