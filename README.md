# python-rest-101

This is a python rest srvice with the following rest point.


```

http://localhost:5000/hello?name=foo

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