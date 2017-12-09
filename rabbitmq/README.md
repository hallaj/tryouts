# RabbitMQ tryout

Basic rabbitmq functionality, with docker-compose, Makefile

## Requirements

* docker
* docker-compose
* make

## Usage Instructions

1. Clone the repository
```
git clone https://github.com/hallaj/rabbitmq_tryout
```
2. Change to the directory
```
cd rabbitmq_tryout
```
3. Build the necessary image with docker-compose
```
docker-compose build
```
4. Start the application
```
make start
```

## What's next

* Probably a UI on the node end to display the changes made gets there
* Integrate flask-login with the credentials created from master
* I'll think of something else, I hope
