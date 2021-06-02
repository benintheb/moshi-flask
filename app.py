from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('controller.html')

@app.route('/sensor')
def sensor():
  os.system("cd controller && python3 sensor.py")
  return render_template('controller.html')



host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == '__main__':
	app.run(host=host_addr, port=port_num, debug=True)