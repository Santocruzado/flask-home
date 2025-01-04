/**
 * This script is used to animate the images on the home page.
 */
fetch('/meme-images')
    .then(response => response.json())
    .then(data => {
        const images = data.images;
        let currentIndex = 0;
        const animatedImage = document.getElementById('animatedImage');

        function changeImage() {
            currentIndex = (currentIndex + 1) % images.length;
            animatedImage.src = `/static/${images[currentIndex]}`;
            animatedImage.classList.remove('animate-drop');
            void animatedImage.offsetWidth; // Trigger reflow to restart animation
            animatedImage.classList.add('animate-drop');
        }

        let interval = setInterval(changeImage, 5000);

        animatedImage.addEventListener('mouseenter', () => clearInterval(interval));
        animatedImage.addEventListener('mouseleave', () => interval = setInterval(changeImage, 3000));
    })
    .catch(error => {
        console.error('Error fetching images:', error);
    });


