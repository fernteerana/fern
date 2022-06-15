from typing import Union

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def read_root():
    data = "Teerana Boonloed"
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name_2(name,last_name):
    data = "{} {}".format(name, last_name)
    return data

@app.get("/formula")
def formula(s,t):
    v = float(s) / float(t)
    data = "v = {:2f}".format(v)
    return data

@app.get("/r")
def r(r1,r2,r3):
    rt1 = float(r1)+float(r2)+float(r3)
    rt2 = ((1/float(r1)) + (1/float(r2) + (1/float(r3))))**-1
    #data = 
    data = {"อนุกรม":rt1, "ขนาน":rt2}
    return data


if __name__=="__main__":
    uvicorn.run(app, host="192.168.171.203", port=8000)