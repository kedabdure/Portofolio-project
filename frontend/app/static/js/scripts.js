// SHOW ALL CARDS
document.querySelector('.all-services a').addEventListener('click', function() {
    document.querySelectorAll('.service-container ul li').forEach(function(card) {
        card.style.display = 'block';
    });
    this.style.display = 'none';
});



// POPUP Massage
function showBookingPopup() {
    document.getElementById('booking-popup').style.display = 'block';
}
function hideBookingPopup() {
    document.getElementById('booking-popup').style.display = 'none';
}
document.querySelector('.close-btn').addEventListener('click', hideBookingPopup);
document.querySelector('.ok-btn').addEventListener('click', hideBookingPopup);

// Check if the booking was successful
const urlParams = new URLSearchParams(window.location.search);
const success = urlParams.get('success');
if (success === 'true') {
    showBookingPopup();
}



// UPDATE THE FOOTER DATE
function updateDateTime() {
    const dateTimeElement = document.getElementById("footer-datetime");
    const now = new Date();

    const options = { 
        year: 'numeric',
    };
    
    const formattedDateTime = now.toLocaleDateString(undefined, options);
    dateTimeElement.textContent = formattedDateTime;
}
updateDateTime();
// Update the date and time every second
setInterval(updateDateTime, 1000);
