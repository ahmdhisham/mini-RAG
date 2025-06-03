# mini-RAG
First RAG project for learning purposes. This is a minimal impelementation of a RAG model for question answering.

## Requirements
- Python 3.10

#### Install Python
**Remove each "$" from the commands or copy them without it; it's only a declaration for using the command-line interface**
1) Download python 3.10 from the official website of python
2) Install it and add it to the **System PATH**
3) Open the terminal from your project dirctory ***or*** head to your IDE terminal and change the working directory to your project directory 
(e.g. ```ahmed@ahmed-virtual-machine:~/Desktop/Projects/mini-RAG```)
4) Create a new virtual environment using the following command 
```bash
$ python3 -m venv .venv
```
5) Activate the environment using the following command
```bash 
$ source .venv/bin/activate
```
### (Optional) Setup your command line interface for better readability
```bash
$ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages
**Install the required packages using this command in the same virtual environment**  
```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```
**Set your environment variables in the ".env" file. Like "OPENAI_API_KEY" value**

## Run fastapi server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 7000
```

## Add main.py

**Adjust the path_env at the first line in the main.py file to match this --> path_env = ".env"**