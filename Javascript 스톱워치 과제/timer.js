import { startStopWatch, stopStopWatch, resetStopWatch } from "./stopwatch.js";

const timeOver = () => {
    // TODO: 타이머 종료 시 실행할 것들
    console.log("종료!");

    stopTimer();
}

const updateDisplayDown = () => {
    const timeDisplay = document.getElementById("display-time");

    const temp = timeDisplay.innerText.split(":");
    let sec = Number(temp[0]);
    let ms = Number(temp[1]);

    ms--;
    if (ms === -1) {
        ms = 99;
        sec--;

        if (sec === -1) {
            timeOver();
            return;
        }
    }

    timeDisplay.innerText = sec.toString().padStart(2, '0') + ':' + ms.toString().padStart(2, '0');
}


let timerIntervalID = "";
const startTimer = () => {
    if (timerIntervalID)   return;
    if (document.getElementById("display-time").innerText === "00:00")  return;

    timerIntervalID = setInterval(updateDisplayDown, 10)
}
const stopTimer = () => {
    if (!timerIntervalID)    return;

    clearInterval(timerIntervalID);
    timerIntervalID = "";
}
const resetTimer = () => {
    if (timerIntervalID)    return;

    setTimer();
}
const setTimer = () => {
    const inputBox = document.getElementById("timer-set-input");
    const targetSecond = Number(inputBox.value);
    inputBox.value = "";

    if (targetSecond < 0)  return;

    const timeDisplay = document.getElementById("display-time");
    timeDisplay.innerText = targetSecond.toString().padStart(2, '0') + ':00';
}

function setTimerButtonClickEvents() {
    const startBtn = document.getElementById("btn-start");
    const stopBtn = document.getElementById("btn-stop");
    const resetBtn = document.getElementById("btn-reset");
    const timerSetBtn = document.getElementById("btn-timer-set");

    startBtn.removeEventListener("click", startStopWatch);
    stopBtn.removeEventListener("click", stopStopWatch);
    resetBtn.removeEventListener("click", resetStopWatch);

    startBtn.addEventListener("click", startTimer);
    stopBtn.addEventListener("click", stopTimer);
    resetBtn.addEventListener("click", resetTimer);
    timerSetBtn.addEventListener("click", setTimer);
}

export { setTimerButtonClickEvents, startTimer, stopTimer, resetTimer };