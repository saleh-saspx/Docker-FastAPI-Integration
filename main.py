# main.py

from app.router.web import Web
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--port', type=int, help='The port number')
args = parser.parse_args()
ـport = args.port

app = Web.init()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=ـport)
