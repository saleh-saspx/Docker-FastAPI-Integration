import pytest
from unittest.mock import Mock

from app.service.Docker import DockerHub

class TestDockerHub:

    def test_list_containers(self):        
        result = DockerHub.listTest()
        assert result == {
                "id": 'test_1',
                "name": 'test',
                "status": 'running',
                "port" : "8080"
            }