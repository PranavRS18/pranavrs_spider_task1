// Get the HTML Elements
const scoreboard = document.querySelector("#score h2");
const hammer = document.querySelector("#hammer");
const smash = document.querySelector("#smash");
const mode = document.querySelector("#mode");
const result = document.querySelector(".result");

// Declare the Variables

// Score
let score = 0;
let curr_score = 0;
let score_speed = 25;
let player_1_score = 0;
let player_2_score = 0;

// Hammer
let angle = 0;
let initial_speed = 1;
let direction = "forward";

// Two Player Mode
let display = "";
result.textContent = display;
mode.disabled = true;

// Animate Hammer
function animate_hammer() {

    // Player has hit SMASH
    if(direction === "stop") {
        if (smash.textContent === "SMASH") {
            smash.textContent = "TRY AGAIN";
            return;
        }

        else if(smash.textContent === "PLAYER 1 SMASH") {
            smash.textContent = "PLAYER 2 START";
            return;
        }

        else if(smash.textContent === "PLAYER 2 SMASH") {
            smash.textContent = "NEXT GAME";
            return;
        }
    }

    // Initialise the Variables
    let speed = initial_speed;
    let rad = angle * Math.PI / 180;
    let translateX = -190 * Math.cos(rad) + 190;
    let translateY = -250 * Math.sin(rad);

    // Rotate the Hammer and Translate
    hammer.style.transform = `scaleX(-1) rotateZ(-${angle}deg) translateX(${translateX}px) translateY(${translateY}px)`;

    // Change the Angle
    if(angle < 180 && direction === "forward") {
       angle++;
    }
    else if (angle > 0 && direction === "backward") {
        angle--;
    }
    else if (angle === 180 && direction === "forward") {
        direction = "backward";
    }
    else if (angle === 0 && direction === "backward") {
        direction = "forward";
    }

    // Variable Speed
    speed = initial_speed / 20 + initial_speed * 39 / 20 * Math.abs(Math.cos(rad));

    setTimeout(animate_hammer, speed);

}

function add_scoring() {
    if(curr_score > score - 1){
        scoreboard.textContent = `${score}`;

        //Single Player
        if(smash.textContent === "TRY AGAIN"){
            mode.disabled = false;
        }

        // Between Player 1 and Player 2
        else if(smash.textContent === "PLAYER 2 START") {
            player_1_score = parseFloat(score);
        }

        // Two Players
        else if(smash.textContent === "NEXT GAME") {
            player_2_score = parseFloat(score);
            //Display
            if(player_1_score > player_2_score) {
                display = "PLAYER 1 WINS";
            }

            else if(player_2_score > player_1_score) {
                display = "PLAYER 2 WINS";
            }
            else{
                display = "DRAW";
            }

            result.textContent = display;
            mode.disabled = false;
        }

        // Enabling Buttons
        smash.disabled = false;

    }

    // Scoring Animation
    else {
        curr_score++;
        scoreboard.textContent = `${curr_score} `;
        score_speed = Math.max(25, 25 + (curr_score - score / 2) * 2);
        setTimeout(add_scoring, score_speed);
    }
}

// The Game
animate_hammer()

// Listen for Smash Button Click
smash.addEventListener("click", () => {

    // Get Score and Stop Hammer
    if(smash.textContent === "SMASH" || smash.textContent === "PLAYER 1 SMASH" || smash.textContent === "PLAYER 2 SMASH") {

        let smash_rad = angle * Math.PI / 180
        score = 100 * Math.sin(smash_rad) ** 3;
        score = score.toFixed(1);
        direction = "stop";

        // Disable Buttons
        smash.disabled = true;

        setTimeout(() => {
            curr_score = 0;
            add_scoring();
        }, 10);
    }

    // Player 2
    else if (smash.textContent === "PLAYER 2 START") {
        direction = "forward";
        angle = 0;
        smash.textContent = "PLAYER 2 SMASH";
        scoreboard.textContent = "0";
        animate_hammer();
    }

    // New Game Call
    else if(smash.textContent === "TRY AGAIN" || smash.textContent === "NEXT GAME") {

        // Single Player
        if(mode.textContent === "SINGLE PLAYER"){
            direction = "forward";
            angle = 0;
            smash.textContent = "SMASH";
            scoreboard.textContent = "0";
            result.textContent = "";

            mode.disabled = true;

            animate_hammer();
        }

        // Two Player
        else{
            direction = "forward";
            angle = 0;
            smash.textContent = "PLAYER 1 SMASH";
            scoreboard.textContent = "0";
            result.textContent = "";

            mode.disabled = true;

            animate_hammer();
        }
    }
});

// Listen for Mode change clicks
mode.addEventListener("click", function () {
    if(mode.textContent === "SINGLE PLAYER") {
        mode.textContent = "TWO PLAYERS";
    }

    else {
        mode.textContent = "SINGLE PLAYER";
    }
})