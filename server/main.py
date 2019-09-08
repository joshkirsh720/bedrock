from flask import Flask
import time

app = Flask(__name__)

lastBeat = time.time()
beatInterval = 10 #seconds

def isAlive():
  return time.time() - lastBeat < beatInterval

@app.route("/beat/")
def set():
  global lastBeat
  lastBeat = time.time()
  return str(lastBeat)

@app.route("/checkAlive/")
def checkAlive():
  return "Alive" if isAlive() else "Dead"
  
if __name__ == "__main__":
  app.run()
  app.run(host = '0.0.0.0', port="5000")
  