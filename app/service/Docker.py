import docker
class DockerHub():
    def list():
        """
            Retrieve a list of all Docker containers.
            Returns:
            dict: A dictionary containing container information.
        """
        client = docker.from_env()
        containers = client.containers.list()
        container_list = []
        for container in containers:
            container_list.append({
                "id": container.id,
                "name": container.name,
                "status": container.status
            })
        return container_list
    
    def kill(container_id):
            """
            Kill a specific container.

            Args:
                container_id (str): The ID of the container to kill.

            Returns:
                dict: A message indicating success or failure.
            """
            client = docker.from_env()
            try:
                container = client.containers.get(container_id)
                container.kill()
                return 'Accept'
            except docker.errors.NotFound:
              return "Container Not Found"
            except docker.errors.APIError as e:
              return str(e)

    def show(container_id):
            """
            Retrieve information and logs for a specific container.

            Args:
                container_id (str): The ID of the container.

            Returns:
                dict: A dictionary containing container information and logs.
            """
            client = docker.from_env()
            container = client.containers.get(container_id)
            logs = container.logs(tail=10)
            return {
                        "id": container.id,
                        "name": container.name,
                        "status": container.status,
                        "logs": logs.decode("utf-8").split("\n")
            }
        
    def start(container_id):
            """
            Start a specific container.

            Args:
                container_id (str): The ID of the container to start.

            Returns:
                dict: A message indicating success or failure.
            """
            client = docker.from_env()
            try:
                container = client.containers.get(container_id)
                container.start()
                return "Accept"
            except docker.errors.NotFound:
                return "Container Not Found"
            except docker.errors.APIError as e:
                return str(e)
