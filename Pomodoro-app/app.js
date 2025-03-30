const bells = new Audio('./sounds/bell.wav'); 
const startBtn = document.querySelector('.btn-start'); 
const session = document.querySelector('.minutes'); 
const secondDiv = document.querySelector('.seconds');

let myInterval; 
let totalSeconds;
let state = true; 

const appTimer = () => {
    const sessionAmount = Number.parseInt(session.textContent);
  
    if (state) {
        state = false;
        totalSeconds = sessionAmount * 60;
        
        myInterval = setInterval(updateSeconds, 1000);
    } else {
        alert('Session has already started.');
    }
};

const updateSeconds = () => {
    let minutesLeft = Math.floor(totalSeconds / 60);
    let secondsLeft = totalSeconds % 60;

    session.textContent = `${minutesLeft}`;
    secondDiv.textContent = secondsLeft < 10 ? `0${secondsLeft}` : secondsLeft;

    if (minutesLeft === 0 && secondsLeft === 0) {
        bells.play();
        clearInterval(myInterval);
        state = true; // Reset state for a new session
    }

    totalSeconds--;
};

// Attach event listener to the start button
startBtn.addEventListener('click', appTimer);
