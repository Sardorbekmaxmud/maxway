const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const closeBtn = document.getElementById('close');
const thumbnails = document.querySelectorAll('.thumbnail');

// Rasm bosilganda lightbox ochish
thumbnails.forEach(thumbnail => {
    thumbnail.addEventListener('click', () => {
        lightbox.style.display = 'flex';
        lightboxImg.src = thumbnail.src;
    });
});

// Lightboxni yopish
closeBtn.addEventListener('click', () => {
    lightbox.style.display = 'none';
});

