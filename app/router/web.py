from fastapi import FastAPI
from app.service.Docker import DockerHub
class Web:
    def init():
        """
        Initialize the FastAPI application.
        """
        app = FastAPI()

        @app.get("/list")
        async def list_containers():
            return {
                "data": {"containers": DockerHub.list()},
                "message": "Success"
            }

        @app.get('/show/{container_id}')
        async def show_container(container_id):
            return {
                "data": DockerHub.show(container_id),
                "message" : "Accept"
            }
        @app.get("/kill/{container_id}")
        async def kill_container(container_id):
           return {
               "message" :  DockerHub.kill(container_id)
           }
        
        @app.get("/start/{container_id}")
        async def start_container(container_id):
            return {
                "message" : DockerHub.start(container_id)
            }

        # Return the FastAPI application
        return app

