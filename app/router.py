from fastapi import APIRouter, Request, Depends, HTTPException
from depends import read_all, con_db
from model import Otzyv

router_test = APIRouter(prefix='/router', tags=['Baza'])

@router_test.get('/check', tags=['Baza'])
def dnt_matter():
    return {'message':'ok'}

@router_test.get('/get_all_from_db')
def get_from_db_all():
    return read_all()

@router_test.get("/info")
def get_info(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "user_agent": request.headers.get("user-agent"),
        "db": "connected" if request.app.state.conn else "disconnected"
    }

@router_test.post("/add_bd")
def add_to_bd(otz: Otzyv, con = Depends(con_db)):
    try:
        cursor = con.cursor()
        cursor.execute(''' 
        INSERT INTO otzyvy (text,
        mail,
        phone,
        mood) 
        VALUES (%s, %s, %s, %s)''',
        (otz.text,
        otz.mail,
        otz.phone,
        otz.mood))
    except:
        raise HTTPException(status_code=500, detail='error bd')

