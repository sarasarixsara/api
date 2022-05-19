from fastapi import FastAPI

app = FastAPI()

bloqueado = False;
arriba = False;

@app.get("/up")
async def up():
    arriba = False;
    bloqueado = False;
    return {"message": "Estoy subiendo, bloqueado: " + str(bloqueado)}

@app.get("/down")
async def down():
    bloqueado = False;
    return {"message": "Estoy bajando, bloqueado: " + str(bloqueado)}

@app.get("/stop")
async def stop():
    bloqueado = True;
    return {"message": "bloqueado: " + str(bloqueado)}


