# This is social network KORTEX

## Setup

- Create a `.env` file by example `.env_example`
- Setup virtual enviroment
    - Create python virtual enviroment by command: `python3 -m venv venv`
    - Move all scripts in `.bin` directory to `/venv/bin`
    - Execute `source venv/bin/activate`

Now u can use `pymanage {command}` command instead `python3 manage.py {command}`
- Install requirements by command: `pip install -r requirements.txt`

## Description
This is my education project. At this moment we are able to sign in and sign up

## Possible errors
### Ubuntu 22.04
If you get "libpq-fe.h: No such file or directory" error by pip:
```
sudo apt-get install libpq-dev
```