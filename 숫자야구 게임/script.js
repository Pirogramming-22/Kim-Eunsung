function setTargetNumbers() {
    const numbers = new Set();

    while (numbers.size < 3) {
        const randomNum = Math.floor(Math.random() * 10);
        numbers.add(randomNum);
    }

    return Array.from(numbers);
}

function generateResult(inputNumbers) {
    result = {
        "strike" : 0,
        "ball" : 0
    };

    for(let i = 0; i < 3; i++) {
        if (inputNumbers[i] === targetNumbers[i])   result["strike"] += 1;
        else if (targetNumbers.includes(inputNumbers[i]))   result["ball"] += 1;
    }

    return result;
}

function updateHTML(inputNumbers, result) {
    const resultHTMLString = (result["strike"] === 0 && result["ball"] === 0) ? "<span class=\"num-result out\">O</span>" : `${result["strike"]} <span class=\"num-result strike\">S</span> ${result["ball"]} <span class=\"num-result ball\">B</span>`;

    const num_result = document.createElement("span");
    num_result.className = "num-result";
    num_result.innerText = `${inputNumbers[0]} ${inputNumbers[1]} ${inputNumbers[2]}`;

    const result_divider = document.createElement("span");
    result_divider.innerText = ":"

    const check_result = document.createElement("span");
    check_result.className = "num-result";
    check_result.innerHTML = resultHTMLString;

    const resultContainer = document.createElement("div");
    resultContainer.className = "check-result";
    resultContainer.appendChild(num_result);
    resultContainer.appendChild(result_divider);
    resultContainer.appendChild(check_result);

    result_display.appendChild(resultContainer);
}

function gameOvered(success) {
    // 버튼 비활성화
    const button = document.getElementsByClassName("submit-button")[0];
    button.disabled = true;

    // 이미지 출력
    const resultImg = document.getElementById("game-result-img");
    resultImg.src = success ? "success.png" : "fail.png";

}

function check_numbers() {
    const inputBox1 = document.getElementById("number1");
    const inputBox2 = document.getElementById("number2");
    const inputBox3 = document.getElementById("number3");
    if (inputBox1.value == '' || inputBox2.value == '' || inputBox3.value == '') {
        inputBox1.value = '';
        inputBox2.value = '';
        inputBox3.value = '';
        return;
    }

    const inputNumbers = [Number(inputBox1.value), Number(inputBox2.value), Number(inputBox3.value)]
    result = generateResult(inputNumbers);

    // box 비우기
    inputBox1.value = '';
    inputBox2.value = '';
    inputBox3.value = '';
    
    updateHTML(inputNumbers, result);
    if (result["strike"] === 3) {
        gameOvered(true);
    }
    
    attempts -= 1;
    attemptsDOM.innerText = attempts;
    if (attempts  == 0) {
        gameOvered(false);
    }
}

// Main

// 1. 게임 초기화
// 1. 시도 가능 횟수를 설정합니다. > 입력한 숫자를 확인할 때마다 1씩 감소합니다.
let attempts = 9;
const attemptsDOM = document.getElementById("attempts");
attemptsDOM.innerText = attempts;

// 2. 중복되지 않는 3개의 랜덤한 숫자를 설정합니다.
const targetNumbers = setTargetNumbers();

// 3. html의 input과 결과창의 내용을 비웁니다.
const result_display = document.getElementsByClassName("result-display")[0];
result_display.innerHTML = '';
