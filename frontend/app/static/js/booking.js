// BOOKING CUSTOM JS

const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.querySelector(".progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

let formStepsNum = 0;

/* Event Listener for Next Button. */
nextBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        formStepsNum++;
        updateFormSteps();
        updateProgressbar();
    });
});

/* Event Listener for Back Button. */
prevBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        formStepsNum--;
        updateFormSteps();
        updateProgressbar();
    });
});

/* Updates Form Items */
function updateFormSteps() {
    formSteps.forEach((formStep) => {
        formStep.classList.contains("form-step-active") &&
        formStep.classList.remove("form-step-active")
    })
    formSteps[formStepsNum].classList.add("form-step-active");
}

/* Updates Progress Bar */
function updateProgressbar() {
    progressSteps.forEach((progressStep, index) => {
        if ( index < formStepsNum + 1 ) {
            progressStep.classList.add('progress-step-active')
            
            
        } else {
            progressStep.classList.remove('progress-step-active')
        }
    })
    progress.style.width = ((formStepsNum) / (progressSteps.length - 1)) * 100 + "%";
    
}


// BOOKING CONFIRMATION POP UP
const popUpBox = document.querySelector('.popup-overlay')
const closeIcon = document.querySelector('.close-btn')

closeIcon.addEventListener('click', () => {
    popUpBox.style.display = 'none'
})

okBtn.addEventListener('click', () => {
    popUpBox.style.display = 'none'
})


function showPopUp() {
    popUpBox.style.display = 'block'
}

// CHECK IF THE BOOKING WAS SUCCESSFUL
const urlParams = new URLSearchParams(window.location.search);
const success = urlParams.get('success')
if (success === 'true') {
    showPopUp()
}


