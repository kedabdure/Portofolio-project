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
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default link behavior

        // Remove 'active' class from all links
        sidebarLinks.forEach(link => {
            link.classList.remove('active');
        });

        // Add 'active' class to the clicked link
        this.classList.add('active');
    });
});


// BOOKING STATUS
Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
        <td>${order.productName}</td>
        <td>${order.productNumber}</td>
        <td>${order.paymentStatus}</td>
        <td class="${order.status === 'Declined' ? 'danger' : order.status === 'Pending' ? 'warning' : 'primary'}">${order.status}</td>
        <td class="primary">Details</td>
    `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
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
const logoutBtn = document.querySelector(".logout");

// CONTAINER COMPONENTS
const container = document.querySelector(".container");

// CONTAINER COMPONENTS

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


