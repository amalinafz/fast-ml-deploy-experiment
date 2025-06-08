# fast-ml-deploy
This repo is a fork from https://github.com/rodrigo-arenas/fast-ml-deploy and tried based on the an article explaining the content of this repo can be found in this [medium link](https://medium.com/analytics-vidhya/serve-a-machine-learning-model-using-sklearn-fastapi-and-docker-85aabf96729b)

Example repo of machine learning model deployment with FastAPI and Docker

# Demo instructions


### 1. Build the docker image

```
docker build -t iris-ml-build .
```

### 2. Run the container

```
docker run -d -p 80:80 --name iris-api iris-ml-build 
```

### 3. Run Pytest with coverage
```
docker exec -it iris-api pytest --ignore=tests/ --cov=app tests/ --cov-config=.coveragerc
```

### 4. Go to localhost
http://127.0.0.1/docs


### 5. Try out the post /predict method
```
curl -X POST "http://127.0.0.1/v1/iris/predict" -H\
 "accept: application/json"\
 -H "Content-Type: application/json"\
 -d "{\"data\":[[4.8,3,1.4,0.3],[2,1,3.2,1.1]]}"
```
