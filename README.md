```
# Docker FastAPI Integration

This project demonstrates the integration of FastAPI with Docker to manage Docker containers via a RESTful API. It provides endpoints to list containers, show container details and logs, kill containers, and start containers.

## Installation

### Python 3 Installation

#### Mac OS:

1. Open Terminal.
2. Check if Python 3 is already installed by running:
   ```
   python3 --version
   ```
3. If Python 3 is not installed, download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/).

#### Linux:

1. Open Terminal.
2. Use the package manager to install Python 3:
   ```
   sudo apt update
   sudo apt install python3
   ```

#### Windows:

1. Download the Python 3 installer from the official Python website: [Python Downloads](https://www.python.org/downloads/).
2. Run the installer and follow the installation instructions.

### Pip Installation

Pip is the package installer for Python. You can install it using the following steps:

1. Download `get-pip.py` from [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py).
2. Open Terminal (or Command Prompt on Windows).
3. Navigate to the directory containing `get-pip.py`.
4. Run the following command:
   ```
   python get-pip.py
   ```

### Installing Requirements

After installing Python and Pip, navigate to the project directory and run the following command to install the project dependencies:

```
pip install -r requirements.txt
```

This will install FastAPI and Docker packages necessary for the project.

## Usage

To run the application, use the following command:

```
uvicorn main:app --reload --port 8000
```

This command starts the FastAPI server with auto-reload enabled, listening on port 8000. You can access the API at `http://localhost:8000`.
```