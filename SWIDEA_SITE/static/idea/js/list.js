function ZzimToggle(btn, id) {
    fetch(`/${id}/zzim`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('meta[name="csrf-token"]').content
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json(); // JSON 파싱
    })
    .then(data => {
        if (data['zzim'])
            btn.classList.add('zzim');
        else
            btn.classList.remove('zzim');
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function interestUp(id) {
    fetch(`/${id}/interestup`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('meta[name="csrf-token"]').content
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json(); // JSON 파싱
    })
    .then(data => {
        const interestText = document.querySelector(`.list--idea-interest${id}`)
        interestText.innerHTML = data['interest']
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
function interestDown(id) {
    fetch(`/${id}/interestdown`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('meta[name="csrf-token"]').content
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json(); // JSON 파싱
    })
    .then(data => {
        const interestText = document.querySelector(`.list--idea-interest${id}`)
        interestText.innerHTML = data['interest']
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

const pageBtn = document.querySelectorAll('.mx-1')
for(let i=0; i<pageBtn.length; i++) {
    pageBtn[i].textContent = String.fromCharCode(Number(pageBtn[i].textContent) + 9311);
}