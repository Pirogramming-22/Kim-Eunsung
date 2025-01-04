import { setButtonClickEvents, stopStopWatch } from "./stopwatch.js";
import { setTimerButtonClickEvents, stopTimer } from "./timer.js";

const updateDisplaybyMode = () => {
    const btnModeStopwatch = document.getElementById("btn-mode-stopwatch");
    const btnModeTimer = document.getElementById("btn-mode-timer");
    const titleH1 = document.getElementById("title");
    const record = document.getElementsByClassName("record")[0];
    const timerSetting = document.getElementsByClassName("timer-setting")[0];

    switch (mode) {
        case 0:
            // 스톱워치
            btnModeStopwatch.classList.add("option-selected");
            btnModeTimer.classList.remove("option-selected");
            titleH1.innerText = "피로그래밍 스톱워치";
            timerSetting.classList.add("no-display");
            record.classList.remove("no-display");

            setButtonClickEvents();
            break;
            
        case 1:
            // 타이머
            btnModeTimer.classList.add("option-selected");
            btnModeStopwatch.classList.remove("option-selected");
            titleH1.innerText = "피로그래밍 타이머";
            record.classList.add("no-display");
            timerSetting.classList.remove("no-display");

            setTimerButtonClickEvents()
            break;
        default:
            mode=0;
            break;
    }
    stopTimer();
    stopStopWatch();
}

const switchToStopwatch = () => {
    mode = 0;
    updateDisplaybyMode();
}
const switchToTimer = () => {
    mode = 1;
    updateDisplaybyMode();
}

function setModeButtonClickEvents() {
    const btnModeStopwatch = document.getElementById("btn-mode-stopwatch");
    const btnModeTimer = document.getElementById("btn-mode-timer");

    btnModeStopwatch.addEventListener("click", switchToStopwatch);
    btnModeTimer.addEventListener("click", switchToTimer);
}


// Main

// MODE 저장하는 변수
let mode = 0;

setModeButtonClickEvents();
setButtonClickEvents();

const checkAll = document.getElementById("check-all")
checkAll.addEventListener("change", () => {
    if (checkAll.checked) {
        const allCheckbox = document.getElementsByClassName("checkbox-individual");
        for (let i = 0; i < allCheckbox.length; i++) {
            allCheckbox[i].checked = true;
        }
    } else {
        const allCheckbox = document.getElementsByClassName("checkbox-individual");
        for (let i = 0; i < allCheckbox.length; i++) {
            allCheckbox[i].checked = false;
        }
    }
})
