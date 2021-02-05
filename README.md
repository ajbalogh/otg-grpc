# OpenTrafficGenerator IxNetwork GRPC

Access IxNetwork using Open Traffic Generator openapi models and GRPC.

## Pre-requisites
- Install go.
- Reading: https://medium.com/@lorenzhofmann.w/how-to-build-a-rest-api-with-grpc-and-get-the-best-of-two-worlds-9a4e491f30ae
- Install gnostic libraries
```
go get -u github.com/googleapis/gnostic-grpc
go get -u github.com/googleapis/gnostic
go get -u github.com/golang/protobuf/protoc-gen-go
go get -u google.golang.org/grpc
```
- get googleapis 
```
git clone https://github.com/googleapis/googleapis.git
```
- install python tools
```
pip install grpcio_tools
```

## Get the latest Open Traffic Generator Models
```
curl --location https://github.com/open-traffic-generator/models/releases/latest/download/openapi.yaml --output openapi.yaml
```

## Generate Protobuf
```
gnostic --grpc-out=./ openapi.yaml
```

## Generate Grpc src
```
python -m grpc_tools.protoc -I=./ -I=./googleapis --python_out=./src --grpc_python_out=./src ./openapi.proto
```

## Build Docker image
```
docker build -t otg-ixn-grpc .
```

## Run Docker image
```
docker run --tty --privileged --detach --publish 5050:5050 --name otg-ixn-grpc otg-ixn-grpc
```

This repository contains the following 3 python based components:
- OpenTrafficGenerator service
- GRPC server that hosts the OpenTrafficGenerator service
- GRPC client that interacts with the OpenTrafficGenerator service

# Getting started
The quickest way to see it in action is to run the server in demo
mode that will produce dummy metrics.

Start the server:
python grpc_server.py --demo

Run the client:

## GNMI Server
