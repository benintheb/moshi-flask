from flask import Flask, render_template
import os
import subprocess, signal
import g

app = Flask(__name__)

@app.route('/')
def index():

  return render_template('index.html')

@app.route('/light/<status>')
def lightStatus(status):
  if (status == "on"):
    print("lightOn", status)
    os.system("./light.sh on")
  elif (status == "off"):
    print("lightOff", status)
    os.system("./light.sh off")
  return render_template('index.html')

@app.route('/sensor/<status>')
def sensorStatus(status):
  if (status == "on"):
    print("sensorOn", status)
    global sensor
    sensor = subprocess.Popen(["python3", "./sensor.py"])
  elif (status == "off"):
    print("sensorOff", status)
    sensor.kill()
  return render_template('index.html')

@app.route('/color/<color>')
def colorChange(color):
  if (color == "silver"):
    print("silver", color)
    os.system("./light.sh color silver")
  elif (color == "green"):
    print("green", color)
    os.system("./light.sh color green")
  elif (color == "blue"):
    print("blue", color)
    os.system("./light.sh color blue")
  elif (color == "yellow"):
    print("yellow", color)
    os.system("./light.sh color yellow")
  elif (color == "red"):
    print("red", color)
    os.system("./light.sh color red")
  elif (color == "magenta"):
    print("magenta", color)
    os.system("./light.sh color magenta")
  return render_template('index.html')

@app.route('/dim/<value>')
def dimControl(value):
  print("dimvalue: ", value)
  os.system("./light.sh brightness " + value)
  return render_template('index.html')

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == '__main__':
	app.run(host=host_addr, port=port_num, debug=True)
