const sensorBtn = document.getElementById("sensorIcon");

sensorBtn.onclick = (e) => {
  e.preventDefault();
  fetch("/sensor").then(console.log("sensor click"));
};
