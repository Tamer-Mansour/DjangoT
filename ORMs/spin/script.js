const wheel = document.querySelector(".inner-wheel");
const spinButton = document.querySelector("#spin-button");
const choiceForm = document.querySelector("#choice-form");
const choiceInput = document.querySelector("#choice-input");
const winChoicesList = document.querySelector("#win-choices");
const winPercentageForm = document.querySelector("#win-percentage-form");
const winPercentageInput = document.querySelector("#win-percentage-input");

let choices = [
  "Section 1",
  "Section 2",
  "Section 3",
  "Section 4",
  "Section 5",
  "Section 6",
];
let winChoices = [];
let winPercentage = 50;

function spinWheel() {
  spinButton.classList.add("disabled");
  wheel.style.transform = "rotate(720deg)";
  setTimeout(() => {
    const degrees = wheel.style.transform.match(/(\d+)/)[0] % 360;
    const sectionIndex = Math.floor((degrees / 60) % 6);
    const section = choices[sectionIndex];
    const randomValue = Math.floor(Math.random() * 100);
    if (randomValue < winPercentage) {
      winChoices.push(section);
    }
    updateWinChoices();
    wheel.style.transform = `rotate(${
      degrees + (360 - (degrees % 60)) + 30
    }deg)`;
    spinButton.classList.remove("disabled");
  }, 6000);
}

function addChoice(event) {
  event.preventDefault();
  const choice = choiceInput.value.trim();
  if (choice !== "") {
    choices.push(choice);
    choiceInput.value = "";
    updateChoices();
  }
}

function setWinPercentage(event) {
  event.preventDefault();
  const percentage = parseInt(winPercentageInput.value);
  if (!isNaN(percentage) && percentage >= 0 && percentage <= 100) {
    winPercentage = percentage;
    winPercentageInput.value = "";
  }
}

function updateChoices() {
  const innerWheel = document.querySelector(".inner-wheel");
  innerWheel.innerHTML = "";
  choices.forEach((choice, index) => {
    const section = document.createElement("div");
    section.classList.add("section");
    section.textContent = choice;
    section.style.backgroundColor = `hsl(${index * 60 + 30}, 75%, 60%)`;
    innerWheel.appendChild(section);
  });
}

function updateWinChoices() {
  winChoicesList.innerHTML = "";
  winChoices.forEach((choice) => {
    const li = document.createElement("li");
    li.textContent = choice;
    winChoicesList.appendChild(li);
  });
}

spinButton.addEventListener("click", spinWheel);
choiceForm.addEventListener("submit", addChoice);
winPercentageForm.addEventListener("submit", setWinPercentage);

updateChoices();
updateWinChoices();
