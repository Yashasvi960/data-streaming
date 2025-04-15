from fastapi import FastAPI

app = FastAPI()


yoga = ["HeadStand", "Cobra", "shoulderStand", "Plough", "Sitting_Bend_And_Forward", "Fish", "Locust", "Bow", "Half spinal twist", "Crow", "Standing forward bend","Triangle"]

@app.get('/')
def read_root():
    return {"message": yoga}
