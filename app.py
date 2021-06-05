from flask import Flask, render_template, session, redirect, url_for
import os, subprocess, signal

app = Flask(__name__)
app.secret_key = 'whatisthiswhatisthis'

@app.route('/')
def reset():
  print("reset def")
  session["light"] = "off"
  session["sensor"] = "off"
  session["color"] = "none"
  session["dim"] = ""
  print("switch status: " + session["sensor"], session["light"])
  return redirect(url_for('index'))

@app.route('/home')
def index():
  return render_template('index.html', lightStatus=session["light"], sensorStatus=session["sensor"], colorStatus=session["color"], dimStatus=session["dim"])

@app.route('/light/<status>')
def lightStatus(status):
  session["light"] = status
  if (status == "on"):
    os.system("./light.sh on")
  elif (status == "off"):
    os.system("./light.sh off")
  return render_template('index.html')

@app.route('/sensor/<status>')
def sensorStatus(status):
  session["sensor"] = status
  if (status == "on"):
    global sensor
    sensor = subprocess.Popen(["python3", "./sensor.py"])
  elif (status == "off"):
    sensor.kill()
  return render_template('index.html')

@app.route('/color/<color>')
def colorChange(color):
  session["color"] = color
  if (color == "silver"):
    os.system("./light.sh color silver")
  elif (color == "green"):
    os.system("./light.sh color green")
  elif (color == "blue"):
    os.system("./light.sh color blue")
  elif (color == "yellow"):
    os.system("./light.sh color yellow")
  elif (color == "red"):
    os.system("./light.sh color red")
  elif (color == "magenta"):
    os.system("./light.sh color magenta")
  return render_template('index.html')

@app.route('/dim/<value>')
def dimControl(value):
  session["dim"] = value
  os.system("./light.sh brightness " + value)
  return render_template('index.html')

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == '__main__':
	app.run(host=host_addr, port=port_num, debug=True)
