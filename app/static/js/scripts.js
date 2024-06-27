document.querySelector('.all-services a').addEventListener('click', function() {
    // Show all cards
    document.querySelectorAll('.service-container ul li').forEach(function(card) {
        card.style.display = 'block';
    });
    // Hide the "Show All Services" button
    this.style.display = 'none';
});