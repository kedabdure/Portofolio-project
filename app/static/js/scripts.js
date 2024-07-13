document.querySelector('.all-services a').addEventListener('click', function() {
    // Show all cards
    document.querySelectorAll('.service-container ul li').forEach(function(card) {
        card.style.display = 'block';
    });
    // Hide the "Show All Services" button
    this.style.display = 'none';
});


// POPUP Massage
// Function to show the pop-up
function showBookingPopup() {
    document.getElementById('booking-popup').style.display = 'block';
}

// Function to hide the pop-up
function hideBookingPopup() {
    document.getElementById('booking-popup').style.display = 'none';
}

// Event listener for the close button
document.querySelector('.close-btn').addEventListener('click', hideBookingPopup);

// Event listener for the OK button
document.querySelector('.ok-btn').addEventListener('click', hideBookingPopup);

// Check if the booking was successful
const urlParams = new URLSearchParams(window.location.search);
const success = urlParams.get('success');
if (success === 'true') {
    showBookingPopup();
}
