# main.py

from app.router.web import Web

app = Web.init()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
