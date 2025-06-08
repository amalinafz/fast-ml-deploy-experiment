# fast-ml-deploy
This repo is a fork from https://github.com/rodrigo-arenas/fast-ml-deploy and tried based on the an article explaining the content of this repo can be found in this [medium link](https://medium.com/analytics-vidhya/serve-a-machine-learning-model-using-sklearn-fastapi-and-docker-85aabf96729b)

Example repo of machine learning model deployment with FastAPI and Docker

# Demo instructions

As per in the medium link and additional deployment to Azure 

## Docker

### 1. Build the docker image

```
docker build -t iris-ml-build .
```

### 2. Run the container

```
docker run -d -p 8080:80 --name iris-api-v4 iris-ml-build 
```
![image](https://github.com/user-attachments/assets/14d7254c-e779-4082-b134-f074d4ae188b)

## Deploy with Azure Container 
Tutorial on how to deploy via Azure Container Instance https://www.youtube.com/watch?v=HyCO6nMdxC0

### 1. Deploy the docker image into Container Registry 

Create container registry and once created, get the details for below at container registry > Setting > Access keys

Tick the Admin user to get the username & password

```
docker **login** containerRegistryLoginServer.azurecr.io -u Username -p password
```

```
docker **build** -t containerRegistryLoginServer.azurecr.io/imageName:image-tag.   
```

```
docker **push** -t containerRegistryLoginServer.azurecr.io/imageName:image-tag.
```

### 2. Deploy Container Instance based on Container Registry

Create container instance
![image](https://github.com/user-attachments/assets/2df72978-be38-4244-a64c-5bfdbe2f30f6)


### 3. Access the container
```
Test it via http://20.17.158.187/docs

Payload Request Body:
{
  "data": [
    [4.0, 3.0, 1.0, 0.0],
    [2.0, 1.0, 2.0, 1.0]
  ]
}
```
![image](https://github.com/user-attachments/assets/0fdbefa5-9037-4d4d-a75d-565ce6fe08a8)

![image](https://github.com/user-attachments/assets/c2862636-eac5-436f-8b45-8dc9b8838fd1)

The Azure Container will be disable on 9 June 2025 at 5.00pm

