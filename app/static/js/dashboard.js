// TOGGLING THE SIDEBAR ON MOBILE VERSION
const sideMenu = document.querySelector("aside");
const menuBtn = document.getElementById("menu-btn");
const closeBtn = document.getElementById("close-btn");

menuBtn.addEventListener("click", () => {
    sideMenu.style.display = "block";
});

closeBtn.addEventListener("click", () => {
    sideMenu.style.display = "none";
});



// DARK MODE
const darkMode = document.querySelector(".dark-mode");

darkMode.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode-variables");
    darkMode.querySelector("span:nth-child(1)").classList.toggle("active");
    darkMode.querySelector("span:nth-child(2)").classList.toggle("active");
});



// APPLY HOVERING FOR ALL LINKS
const sidebarLinks = document.querySelectorAll('.sidebar a');

sidebarLinks.forEach(link => {
    link.addEventListener('click', function () {
        sidebarLinks.forEach(link => {
            link.classList.remove('active');
        });
        this.classList.add('active');
    });
});



/* Sidebar LINKS */
const dashboardBtn = document.querySelector(".dashboard");
const ticketsBtn = document.querySelector(".tickets");
const reportBtn = document.querySelector(".report");
const settingsBtn = document.querySelector(".settings");
const addBtn = document.querySelector(".add");


// Helper function to update headers
function updateHeaders(recentOrdersText, mainTitleText) {
    recentOrdersTitle.textContent = recentOrdersText;
    mainTitle.textContent = mainTitleText;
}

// Helper function to toggle visibility
function toggleVisibility(elements, visibility) {
    elements.forEach(element => {
        if (visibility) {
            element.classList.remove('hidden');
        } else {
            element.classList.add('hidden');
        }
    });
}

// DISPLAY BOOKING DETAILS
const bookingsBtn = document.querySelector(".bookings");
const rightSection = document.querySelector(".right-section");
const recentOrdersTitle = document.querySelector(".recent-orders h2");
const mainTitle = document.querySelector('main .main-title');
const recentOrders = document.querySelector(".recent-orders");
const newUsers = document.querySelector(".new-users");
const container = document.querySelector(".container"); // Assuming container class exists

bookingsBtn.addEventListener("click", function (event) {
    event.preventDefault();
    toggleVisibility([rightSection, newUsers], false);
    analyzeSection.style.display = '';
    updateHeaders('All bookings in details', 'Bookings');
    container.style.gridTemplateColumns = "12rem auto auto";
});

// DISPLAY ANALYTIC SECTION
const analyzeSection = document.querySelector(".analyse");
const analyticsBtn = document.querySelector(".analytics");

analyticsBtn.addEventListener('click', () => {
    toggleVisibility([rightSection, newUsers], true);
    analyzeSection.style.display = '';
    updateHeaders('Recent bookings', 'Analytics');
});

// DISPLAY ALL USERS IN DETAIL
const usersBtn = document.querySelector(".users");

usersBtn.addEventListener('click', (event) => {
    event.preventDefault();
    analyzeSection.style.display = 'none';
    toggleVisibility([rightSection, analyzeSection], false);
    toggleVisibility([newUsers], true);
    updateHeaders('All users', 'Users');
});
/* END OF SIDEBAR LINKS */


// BOOKING STATUS
const statusButtons = document.querySelectorAll('.status-btn');

statusButtons.forEach(button => {
    button.addEventListener('click', function () {
        const statusCell = this.closest('tr').querySelector('.task-status');
        const idCell = this.closest('tr').querySelector('.book-id');

        // Cycle through statuses (for example: Pending -> In Progress -> Completed)
        if (statusCell.textContent === 'Pending') {
            statusCell.textContent = 'Progressing';
        } else if (statusCell.textContent === 'Progressing') {
            statusCell.textContent = 'Completed';
        } else {
            statusCell.textContent = 'Pending';
        }

        // Optionally, add styles based on status
        statusCell.classList.remove('pending', 'progressing', 'completed');
        if (statusCell.textContent === 'Pending') {
            statusCell.classList.add('pending');
        } else if (statusCell.textContent === 'Progressing') {
            statusCell.classList.add('progressing');
        } else {
            statusCell.classList.add('completed');
        }

        const status = statusCell.textContent;
        const id = idCell.textContent; // Extract the id value from the cell
        updateStatus(status, id);
    });
});



// ANIMATE COUNT UP
const countUp = (element, endValue, duration) => {
    let startValue = 0;
    const increment = endValue / (duration / 10); // Adjust the increment based on the duration
    const counter = setInterval(() => {
        startValue += increment;
        element.textContent = Math.floor(startValue).toLocaleString(); // Format the number with commas

        if (startValue >= endValue) {
            clearInterval(counter);
            element.textContent = endValue.toLocaleString(); // Ensure the final value is set correctly
        }
    }, 10); // Adjust the interval for smoother animation
};



// UPDATE THE STATUS OF THE BOOKING
function updateStatus(status, id) {
    fetch(`http://127.0.0.1:5000/api/v1/booking/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json' // Add correct headers
        },
        body: JSON.stringify({
            "status": status
        })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Status updated successfully:', data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}



// FUNCTION TO COUNT EACH TASK STATUS AND DISPLAY WITH ANIMATION
function updateAnalytics() {
    fetch('http://127.0.0.1:5000/api/v1/task_counts')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Select the elements where the task counts will be displayed
            const completedTasksElement = document.querySelector('.sales .info h1');
            const pendingTasksElement = document.querySelector('.visits .info h1');
            const inProgressTasksElement = document.querySelector('.searches .info h1');

            // Start the count up animations
            countUp(completedTasksElement, data.completed, 1000); // 2000ms = 2 seconds
            countUp(pendingTasksElement, data.pending, 1000);
            countUp(inProgressTasksElement, data.in_progress, 1000);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}



// SHOW ALL TABLE CONTENTS
const initialDisplayCount = 3;
let currentDisplayCount = initialDisplayCount;

// Get DOM elements
const allBookingsTable = document.getElementById('all-bookings');
const showMoreBtn = document.getElementById('show-more-btn');
const rows = allBookingsTable.querySelectorAll('tbody tr');

// Function to render rows
function renderRows() {
    // Hide all rows initially
    rows.forEach(row => row.classList.add('hidden'));

    // Display rows up to the current count
    for (let i = 0; i < currentDisplayCount && i < rows.length; i++) {
        rows[i].classList.remove('hidden');
    }

    // Hide the button if all rows are displayed
    if (currentDisplayCount >= rows.length) {
        showMoreBtn.style.display = 'none';
    }
}

// Event listener for the "Show More" button
showMoreBtn.addEventListener('click', (event) => {
    event.preventDefault();
    currentDisplayCount += initialDisplayCount;
    renderRows();
});

// Initial render
renderRows();


// FUNCTION TO GENERATE RANDOM COLOR
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}


// FUNCTION TO FETCH AND DISPLAY LAST 5 NEW USERS
function showNewUsers() {
    fetch('http://127.0.0.1:5000/api/v1/users')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            return response.json();
        })
        .then(data => {
            console.log(data);

            const lastFiveUsers = data.slice(-5);
            console.log(lastFiveUsers[0].first_name);
            
            // Select the user list container
            const userList = document.querySelector('.user-list');
            userList.innerHTML = ''; // Clear any existing content

            // Iterate over the last 5 users
            lastFiveUsers.forEach(user => {
                // Create user container div
                const userDiv = document.createElement('div');
                userDiv.classList.add('user');

                // Create nickname paragraph element
                const nicknamePara = document.createElement('p');
                nicknamePara.classList.add('nickname');
                nicknamePara.textContent = user.first_name.charAt(0).toUpperCase();
                nicknamePara.style.color = getRandomColor();
                userDiv.appendChild(nicknamePara);

                // Create h2 element for first name
                const firstNameHeading = document.createElement('h2');
                firstNameHeading.classList.add('first-name');
                firstNameHeading.textContent = user.first_name;
                userDiv.appendChild(firstNameHeading);

                // Create paragraph element for phone number
                const phonePara = document.createElement('p');
                phonePara.classList.add('phone-no');
                phonePara.textContent = user.phone;
                userDiv.appendChild(phonePara);

                // Append userDiv to user list
                userList.appendChild(userDiv);
            });
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

// Call the function to fetch and display new users
showNewUsers();



// Call the function to update analytics on page load
document.addEventListener('DOMContentLoaded', updateAnalytics);
