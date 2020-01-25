# python-rest-101
This is a python rest srvice with the following rest point.


### to dos
* add test
* persist to mongo
* consume from a queue (eg. rabbitMQ)

HTTP method GET
```

http://localhost:5000/hello?name=foo

```
HTTP method POST
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

### docker

Build:
```
docker build -t rocazac1/python-rest-101 .
```

Run: 
```
docker run  -p 5000:5000 rocazac1/python-rest-101
```