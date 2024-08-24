# Visual Model Server

This server is running on a Django backend.

## Instructions
1. Create a python virtual environment (venv). DO NOT push this virtual environment into the repository. I'll ban you if you do (jk).

```bash
python -m venv pettodex-venv
```

2. Activate the virtual environment.

```bash
source pettodex-venv/bin/activate
```

3. Install the relevant packages.

```bash
pip install tensorflow numpy==1.21.1 django pillow
```

If that doesn't work, install the packages one by one.

```bash
pip install tensorflow
pip install numpy==1.21.1
pip install django
pip install pillow
```

4. Run the server.

```bash
python manage.py runserver
```

If the server does not run, check if your current terminal instance is running virtual environment. Repeat step 2 on your new instance if you are using multiple terminals.
