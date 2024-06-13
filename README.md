Build your image
```
docker build -t rc-1
```

Run your image with

```
docker run --pid=host -d rc-1
```

Optionally you can set environment variable PROCESS_NAME_FILTER to filter results by regex,
ENABLE_TESTING (boolean) to enable test application to parse result json and print tests result into error.txt

```
docker run --pid=host -d -e PROCESS_NAME_FILTER='containerd' rc-1

docker run --pid=host -d -e ENABLE_TESTING=true rc-1

```
