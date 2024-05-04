import docker
class DockerHub():
    
    def listTest():
         return {
                "id": 'test_1',
                "name": 'test',
                "status": 'running',
                "port" : "8080"
            }
    
    def list():
        """
            Retrieve a list of all Docker containers.
            Returns:
            dict: A dictionary containing container information.
        """
        client = docker.from_env()
        containers = client.containers.list(all=True)
        container_list = []
        for container in containers:
            container_info = container.attrs
            ports = container_info['HostConfig']['PortBindings']
            container_list.append({
                "id": container.id,
                "name": container.name,
                "status": container.status,
                "port" : container.ports
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
            container_info = container.attrs
            ports = container_info['HostConfig']['PortBindings']
            return {
                        "id": container.id,
                        "name": container.name,
                        "status": container.status,
                        "logs": logs.decode("utf-8").split("\n"),
                        "port":ports
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

    def logs(container_id, logs=10):
        """
        This function retrieves logs of a Docker container and returns them in chronological order.

        :param container_id: string, the ID or name of the Docker container.
        :param logs: integer, the number of log lines you want to retrieve. Default is 10 lines.
        :return: list of strings, the container logs in chronological order (from newest to oldest).
        """
        client = docker.from_env()
        container = client.containers.get(container_id)
        raw_logs = container.logs(tail=logs).decode('utf-8')  # Decode the string as UTF-8
        log_lines = raw_logs.split("\n") # Split the logs line by line
        log_lines.reverse()  # Reverse the logs
        return log_lines
