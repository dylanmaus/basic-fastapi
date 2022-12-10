from fastapi import FastAPI

application = FastAPI()


@application.get("/")
def root():
    return {"message": "Hello World"}
