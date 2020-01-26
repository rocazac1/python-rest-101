# python-rest-101
This is a python rest service with the following rest point..


### to dos
* add test
* persist to mongo
* consume from a queue (eg. rabbitMQ)

/health HTTP method GET
```
http://localhost:5000/health
```

/hello HTTP method GET
```
http://localhost:5000/hello?name=foo
```

/todos HTTP method POST
```
http://localhost:5000/todos
```

Request eg.:
```
{
    "age": 24,
    "name": "Robert"
}
```

### development

```
pip install --no-cache-dir  -r requirements.txt
LOG_DIR=$(pwd)/logs python src/main.py
```

### testing

```
cd src && python -m unittest test_models.py
```

### docker

Build:
```
./build.sh
```

Run:
```
./run.sh
```
