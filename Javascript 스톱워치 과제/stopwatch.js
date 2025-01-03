const updateDisplay = () => {
    const timeDisplay = document.getElementById("display-time");

    const temp = timeDisplay.innerText.split(":");
    let sec = Number(temp[0]);
    let ms = Number(temp[1]);

    ms++;
    if (ms === 100) {
        ms = 0;
        sec++;
    }

    timeDisplay.innerText = sec.toString().padStart(2, '0') + ':' + ms.toString().padStart(2, '0');
}
const updateRecord = () => {
    const parent = document.getElementsByClassName("records")[0];

    const newRecord = document.createElement("div");
    newRecord.className = "record-item";

    const checkbox = document.createElement("input");
    checkbox.className = "checkbox-circle checkbox-individual";
    checkbox.type = "checkbox";
    setCheckBoxEvent(checkbox);

    const timeH2 = document.createElement("h2");
    const time = document.getElementById("display-time").innerText;
    timeH2.innerText = time.split(':').join(' : ');

    const emptyDiv = document.createElement("div");

    newRecord.appendChild(checkbox);
    newRecord.appendChild(timeH2);
    newRecord.appendChild(emptyDiv);

    parent.appendChild(newRecord);

    // 스크롤 맨 밑으로..
    parent.scrollTop = parent.scrollHeight;
}
const resetDisplay = () => {
    const timeDisplay = document.getElementById("display-time");
    timeDisplay.innerText = "00:00";
}

let intervalID = "";
const startStopWatch = () => {
    if (intervalID)   return;

    intervalID = setInterval(updateDisplay, 10)
}
const stopStopWatch = () => {
    if (!intervalID)    return;

    clearInterval(intervalID);
    updateRecord();
    intervalID = "";
}
const resetStopWatch = () => {
    if (intervalID)    return;

    resetDisplay();
}
const deleteRecord = () => {
    const items = document.getElementsByClassName("record-item");
    
    // side effect 방지하기 위해 역으로 iterate
    for (let i = items.length - 1; i >= 0; i--) {
        const item = items[i];
        
        const checkbox = item.children[0];
        if (checkbox.checked) {            
            item.remove();
        }
    }
    
    checkAll.checked = false;
}

function setButtonClickEvents() {
    const startBtn = document.getElementById("btn-start");
    const stopBtn = document.getElementById("btn-stop");
    const resetBtn = document.getElementById("btn-reset");
    const deleteBtn = document.getElementById("btn-delete");

    startBtn.addEventListener("click", startStopWatch);
    stopBtn.addEventListener("click", stopStopWatch);
    resetBtn.addEventListener("click", resetStopWatch);
    deleteBtn.addEventListener("click", deleteRecord);
}

function setCheckBoxEvent(checkbox) {
    checkbox.addEventListener("change", () => {
        const allCheckbox = document.getElementsByClassName("checkbox-individual");

        // 모든 체크박스가 체크상태면 전체선택도 자동체크됨. 하나라도 안체크상태면 전체선택도 안체크.
        let allChecked = true;
        for (let i = 0; i < allCheckbox.length; i++) {
            if(!allCheckbox[i].checked) {
                allChecked = false;
                break;
            }
        }
        document.getElementById("check-all").checked = allChecked;

    }) 
}



// Main
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
