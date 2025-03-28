// window.onload = function () {
//     window.focus(); // Ensure the window is focused
//     document.body.scrollTop = 0; // Reset the scroll position to the top
//     document.documentElement.scrollTop = 0;
// };



document.addEventListener("DOMContentLoaded", eventFunction);

function createNewImageDiv(idNo, array, index, mobile) {




    if (mobile) {


        const imageSection = document.querySelector('.image-section-mobile');
        const newDiv = document.createElement('img');
        newDiv.className = 'image-box-mobile';

        newDiv.id = `box-mobile${idNo}`;

        newDiv.style.height = '100%'
        newDiv.style.width = '0'
        newDiv.src = `${array[index]}`
        newDiv.style.objectFit = 'cover'
        newDiv.style.objectPosition = 'center'

        imageSection.appendChild(newDiv);

    } else {

        const imageSection = document.querySelector('.image-section');
        const newDiv = document.createElement('img');
        newDiv.className = 'image-box';
        newDiv.id = `box${idNo}`;
        newDiv.style.height = '100%'
        newDiv.style.width = '0'
        newDiv.src = `${array[index]}`
        newDiv.style.objectFit = 'cover'
        newDiv.style.objectPosition = 'center'
        // newDiv.style.backgroundRepeat = 'no-repeat'

        imageSection.appendChild(newDiv);

    }


}

function eventFunction() {

    let imageCount = 0
    let imageIndex = 0



    if (window.screen.width < 1336) {

        setInterval(
            () => {

                const images = [
                    "static/img/10p.jpg",
                    "static/img/11p.jpg",
                    "static/img/9p.jpg",
                ];

                const imageArray = document.querySelectorAll('.image-box-mobile')


                imageArray[imageCount].style.width = 0
                imageArray[imageCount].style.marginLeft = 0
                imageArray[imageCount + 1].style.width = '15.5rem'
                imageArray[imageCount + 1].style.marginLeft = '5px'
                imageArray[imageCount + 2].style.width = '5.5rem'
                imageArray[imageCount + 3].style.width = '2.375rem'
                createNewImageDiv(imageCount + 4, images, imageIndex, true)

                imageCount++

                if (imageIndex == 2) {
                    imageIndex = 0
                } else {
                    imageIndex++
                }

            },
            2000);
    } else {
        setInterval(
            () => {

                const images = [
                    "static/img/10p.jpg",
                    "static/img/11p.jpg",
                    "static/img/9p.jpg",
                ];

                const imageArray = document.querySelectorAll('.image-box')


                imageArray[imageCount].style.width = 0
                imageArray[imageCount].style.marginLeft = 0
                imageArray[imageCount + 1].style.width = '22.5rem'
                imageArray[imageCount + 2].style.width = '12.5rem'
                imageArray[imageCount + 3].style.width = '9.375rem'
                createNewImageDiv(imageCount + 4, images, imageIndex, false)

                imageCount++

                if (imageIndex == 2) {
                    imageIndex = 0
                } else {
                    imageIndex++
                }

            },
            2000);
    }





}




// Cache elements to avoid repeated DOM queries
const buttons = document.querySelectorAll('.filter-btn');
const cards = document.querySelectorAll('.card');
const noPropMessage = document.getElementById('no-property-message');

function filterProperties(category) {
    // --- Instantly Update Active State of Filter Buttons ---
    buttons.forEach(button => {
        button.classList.remove('active');
    });

    // Get the clicked button and activate it immediately
    const activeButton = document.querySelector(`.filter-btn[data-category="${category}"]`);
    if (activeButton) {
        activeButton.classList.add('active');

        // ✅ Force the browser to apply the style update immediately
        activeButton.offsetHeight; // Triggers a reflow

        // ✅ Prevent hover from overriding active state
        activeButton.classList.add('clicked');
    }

    // --- Use requestAnimationFrame to Optimize Filtering ---
    requestAnimationFrame(() => {
        let visibleCount = 0;

        cards.forEach(card => {
            let isVisible = category === 'all' || card.getAttribute('data-category') === category;

            // ✅ Ensure cards update smoothly
            card.style.opacity = isVisible ? '1' : '0';
            card.style.visibility = isVisible ? 'visible' : 'hidden';
            card.style.position = isVisible ? 'relative' : 'absolute';

            if (isVisible) visibleCount++;
        });

        // --- Show/Hide "No Properties Found" Message ---
        noPropMessage.style.display = visibleCount === 0 ? 'block' : 'none';
    });
}



// document.getElementById('navbar-toggle').addEventListener('click', function () {
//     var navOptions = document.getElementById('nav-options');
//     navOptions.classList.toggle('active');
//   });



let isNavOpened = false

function handleToggle() {
    console.log('haaaaaahaaa');

    var navOptions = document.getElementById('mobile-navbar');
    const bar1 = document.getElementById('bar1')
    const bar2 = document.getElementById('bar2')
    const bar3 = document.getElementById('bar3')


    if (isNavOpened) {
        navOptions.style.marginTop = '-100vh'
        isNavOpened = false
        bar1.style.transform = "rotate(0deg)";
        bar2.style.transform = "rotate(0deg)";
        bar3.style.display = "block";
        bar1.style.marginBottom = "4px";





    } else {

        navOptions.style.marginTop = '0'
        isNavOpened = true
        bar1.style.transform = "rotate(45deg)";
        bar2.style.transform = "rotate(-45deg)";
        bar3.style.display = "none"; 
        bar1.style.marginBottom = "-4px";



    }

}


function handleImage(media,url){

    console.log(url,'urlll');
    
    
    const shareUrl = url;
    const message = "Keep in touch for your needs!";

    if(media=='whatsapp'){
        const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(message + " " + shareUrl)}`;
        window.open(whatsappUrl, "_blank");

    }else if(media == 'fb'){

        const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl)}`;
        window.open(facebookUrl, "_blank");

    }else if(media == 'x'){

        const twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(shareUrl)}&text=${encodeURIComponent(message)}`;
    window.open(twitterUrl, "_blank");

        
    }else if(media == 'linkedin'){

        const linkedinUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(shareUrl)}&title=${encodeURIComponent(message)}`;
    window.open(linkedinUrl, "_blank");
    }else{
        const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(shareUrl)}&text=${encodeURIComponent(message)}`;
        window.open(telegramUrl, "_blank");
    }
        
        
    
       
    }



   