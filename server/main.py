from flask import Flask
import time

app = Flask(__name__)

lastBeat = time.time()
beatInterval = 5 #seconds
missedBeats = 0

shouldDispense = False

def isAlive():
  return time.time() - lastBeat < beatInterval

@app.route("/beat/")
def set():
  global lastBeat
  lastBeat = time.time()
  return str(lastBeat)

@app.route("/checkAlive/")
def checkAlive():
  #calc missed beats
  diff = time.time() - lastBeat
  missedBeats = int(diff / beatInterval)

  print(diff, missedBeats, lastBeat)

  if(missedBeats > 3):
    return "Dead"
  else:
    return "Alive"
  
@app.route("/sendDispense/")
def sendDispense():
  global shouldDispense
  shouldDispense = True

  return str(shouldDispense)

@app.route("/shouldDispense/")
def checkDispense():
  global shouldDispense
  if(shouldDispense):
    shouldDispense = False
    return "True"
  else:
    return "False"

if __name__ == "__main__":
  app.run()
  app.run(host = '0.0.0.0', port="5000")