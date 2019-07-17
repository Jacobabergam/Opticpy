init:
    pip install virtualenv
    
    virtualenv Opticspy --python=python3.7 \env
    pip install -r requirements.txt



test:
    py.test tests

.PHONY: init test/