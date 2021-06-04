const sensorBtnOff = document.getElementById("sensorIconOff");
const sensorBtnOn = document.getElementById("sensorIconOn");
const lightBtnOff = document.getElementById("lightIconOff");
const lightBtnOn = document.getElementById("lightIconOn");

const dimControl = document.getElementById("rangeInput");

sensorBtnOff.onclick = (e) => {
  e.preventDefault();
  fetch("/sensor/on");

  sensorBtnOff.classList.add("hidden");
  sensorBtnOn.classList.remove("hidden");
};

sensorBtnOn.onclick = (e) => {
  e.preventDefault();
  fetch("/sensor/off");

  sensorBtnOn.classList.add("hidden");
  sensorBtnOff.classList.remove("hidden");
};

lightBtnOff.onclick = (e) => {
  e.preventDefault();
  fetch("/light/on");

  lightBtnOff.classList.add("hidden");
  lightBtnOn.classList.remove("hidden");
};

lightBtnOn.onclick = (e) => {
  e.preventDefault();
  fetch("/light/off");

  lightBtnOn.classList.add("hidden");
  lightBtnOff.classList.remove("hidden");
};

dimControl.onchange = (e) => {
  fetch("/dim/" + e.target.value);
};
