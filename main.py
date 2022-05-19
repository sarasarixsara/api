from fastapi import FastAPI
#from nntplib import GroupInfo
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

salida1=19
salida2=21

GPIO.setup(salida1, GPIO.OUT)
GPIO.setup(salida2,GPIO.OUT)

app = FastAPI()

bloqueado = False;
arriba = False;

@app.get("/up")
async def up():
    
    GPIO.output(salida1,1)
    GPIO.output(salida2,0)
    return {"salida1: " + str(GPIO.input(salida1))+ "salida2: " + str(GPIO.input(salida2))}

@app.get("/down")
async def down():
    GPIO.output(salida1,0)
    GPIO.output(salida2,1)
    return {"salida1: " + str(GPIO.input(salida1))+ "salida2: " + str(GPIO.input(salida2))}

@app.get("/stop")
async def stop():
    GPIO.output(salida1,1)
    GPIO.output(salida2,1)
    return {"salida1: " + str(GPIO.input(salida1))+ "salida2: " + str(GPIO.input(salida2))}


@app.get("/auto")
async def auto():
    GPIO.output(salida1,0)
    GPIO.output(salida2,0)
    return {"salida1: " + str(GPIO.input(salida1))+ "salida2: " + str(GPIO.input(salida2))}


