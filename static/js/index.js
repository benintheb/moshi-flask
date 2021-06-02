const sensorBtnOff = document.getElementById("sensorIconOff");

const sensorBtnOn = document.getElementById("sensorIconOn");

sensorBtnOff.onclick = (e) => {
  e.preventDefault();
  fetch("/sensoron");

  sensorBtnOff.classList.add("hidden");
  sensorBtnOn.classList.remove("hidden");
};

sensorBtnOn.onclick = (e) => {
  e.preventDefault();
  fetch("/sensoroff");

  sensorBtnOn.classList.add("hidden");
  sensorBtnOff.classList.remove("hidden");
};
