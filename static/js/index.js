const lightBtn = document.getElementById("lightIcon");
const sensorBtn = document.getElementById("sensorIcon");
const colorInputs = document.getElementsByClassName("radioInput");
const dimControl = document.getElementById("rangeInput");

lightBtn.onclick = (e) => {
  e.preventDefault();

  if (lightBtn.src.slice(-6, -4) === "On") {
    lightBtn.src = "/static/img/lightOff.png";
    fetch("/light/off");
  } else if (lightBtn.src.slice(-6, -4) === "ff") {
    lightBtn.src = "/static/img/lightOn.png";
    fetch("/light/on");
  }
};

sensorBtn.onclick = (e) => {
  e.preventDefault();

  if (sensorBtn.src.slice(-6, -4) === "On") {
    sensorBtn.src = "/static/img/sensorOff.png";
    fetch("/sensor/off");
  } else if (sensorBtn.src.slice(-6, -4) === "ff") {
    sensorBtn.src = "/static/img/sensorOn.png";
    fetch("/sensor/on");
  }
};

for (let i = 0; i < colorInputs.length; i++) {
  colorInputs[i].onchange = (e) => {
    fetch(`/color/${e.target.id}`);
  };
}

dimControl.onchange = (e) => {
  fetch(`/dim/${e.target.value}`);
};
