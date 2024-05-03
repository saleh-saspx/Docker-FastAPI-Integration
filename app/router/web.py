from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.service.Docker import DockerHub
from fastapi.middleware.cors import CORSMiddleware

class Web:
    def init():
        """
        Initialize the FastAPI application.
        """
        app = FastAPI()
        origins = [
            "*",
        ]
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @app.get("/list")
        async def list_containers():
            """
            Retrieve a list of all Docker containers.

            Returns:
                dict: A dictionary containing container information.
            """
            return {
                "containers": DockerHub.list(),
                "message": "Success"
            }

        @app.get('/show/{container_id}')
        async def show_container(container_id: str):
            """
            Retrieve information about a specific Docker container.

            Args:
                container_id (str): The ID of the container.

            Returns:
                dict: A dictionary containing container information.
            """
            return {
                "data": DockerHub.show(container_id),
                "message": "Accept"
            }

        @app.get("/kill/{container_id}")
        async def kill_container(container_id: str):
            """
            Kill a specific Docker container.

            Args:
                container_id (str): The ID of the container to kill.

            Returns:
                dict: A message indicating success or failure.
            """
            return {
                "message": DockerHub.kill(container_id)
            }

        @app.get("/start/{container_id}")
        async def start_container(container_id: str):
            """
            Start a specific Docker container.

            Args:
                container_id (str): The ID of the container to start.

            Returns:
                dict: A message indicating success or failure.
            """
            return {
                "message": DockerHub.start(container_id)
            }

        @app.get("/docs", response_class=HTMLResponse)
        async def custom_swagger_ui_html():
            """
            Custom Swagger UI HTML page.
            """
            return get_swagger_ui_html(openapi_url=app.openapi_url, title="Swagger UI")

        @app.get("/redoc", response_class=HTMLResponse)
        async def custom_redoc_html():
            """
            Custom ReDoc HTML page.
            """
            return get_redoc_html(openapi_url=app.openapi_url, title="ReDoc")

        return app

# Instantiate the Web class to create the FastAPI app
