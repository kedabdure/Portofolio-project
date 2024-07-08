const sideMenu = document.querySelector("aside");
const menuBtn = document.getElementById("menu-btn");
const closeBtn = document.getElementById("close-btn");

const darkMode = document.querySelector(".dark-mode");


// TOGGLING THE SIDEBAR
menuBtn.addEventListener("click", () => {
    sideMenu.style.display = "block";
});

closeBtn.addEventListener("click", () => {
    sideMenu.style.display = "none";
});


// DARK MODE
darkMode.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode-variables");
    darkMode.querySelector("span:nth-child(1)").classList.toggle("active");
    darkMode.querySelector("span:nth-child(2)").classList.toggle("active");
});


// HOVER FOR LINKS
const sidebarLinks = document.querySelectorAll('.sidebar a');

sidebarLinks.forEach(link => {
    link.addEventListener('click', function () {
        // Prevent the default link behavior

        // Remove 'active' class from all links
        sidebarLinks.forEach(link => {
            link.classList.remove('active');
        });

        // Add 'active' class to the clicked link
        this.classList.add('active');
    });
});




// Sidebar LINKS
const dashboardBtn = document.querySelector(".dashboard");
const usersBtn = document.querySelector(".users");
const bookingsBtn = document.querySelector(".bookings");
const analyticsBtn = document.querySelector(".analytics");
const ticketsBtn = document.querySelector(".tickets");
const reportBtn = document.querySelector(".report");
const settingsBtn = document.querySelector(".settings");
const addBtn = document.querySelector(".add");


// CONTAINER COMPONENTS
const container = document.querySelector(".container");
// Main Section Contents
const mainSection = document.querySelectorAll("main");
const analyzeSection = document.querySelector(".analyse");
const newUsers = document.querySelector(".new-users");
const recentOrders = document.querySelector(".recent-orders");
// Right Section Content
const rightSection = document.querySelector(".right-section");

console.log("rightSection:", rightSection);
console.log("bookingsLink:", bookingsBtn);

// Add event listener to the button
bookingsBtn.addEventListener("click", function (event) {
    // Add the 'hidden' class to the right section to hide it
    event.preventDefault();
    rightSection.classList.add("hidden");
    newUsers.classList.add("hidden");

    // Adjust the container grid template columns
    container.style.gridTemplateColumns = "12rem auto 1rem";
});


// BOOKING STATUS
const statusButtons = document.querySelectorAll('.status-btn');

    statusButtons.forEach(button => {
        button.addEventListener('click', function() {
            const statusCell = this.closest('tr').querySelector('.task-status');
            console.log('Button clicked');
            console.log('Status cell:', statusCell);

            // Cycle through statuses (for example: Pending -> In Progress -> Completed)
            if (statusCell.textContent === 'Pending') {
                statusCell.textContent = 'In Progress';
            } else if (statusCell.textContent === 'In Progress') {
                statusCell.textContent = 'Completed';
            } else {
                statusCell.textContent = 'Pending';
            }

            // Optionally, add styles based on status
            statusCell.classList.remove('pending', 'in-progress', 'completed');
            if (statusCell.textContent === 'Pending') {
                statusCell.classList.add('pending');
            } else if (statusCell.textContent === 'In Progress') {
                statusCell.classList.add('in-progress');
            } else {
                statusCell.classList.add('completed');
            }
        });
});