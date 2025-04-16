from fastapi import FastAPI
import redis

app = FastAPI()

redis_client = redis.Redis(
    host='redis-16385.c73.us-east-1-2.ec2.redns.redis-cloud.com',
    port=16385,
    decode_responses=True,
    username="default",
    password="uDXZDYeMul1YBFroyegxe4lZFIkHrLQ5",
)

yoga = ["HeadStand", "Cobra", "shoulderStand", "Plough", "Sitting_Bend_And_Forward", "Fish", "Locust", "Bow", "Half spinal twist", "Crow", "Standing forward bend","Triangle"]

@app.get("/yoga/{yoga_id}")
def read_root(yoga_id:int):
    return {"yoga_id":yoga_id}

@app.get("/yoga/{yoga_id}")
def read_item(yoga_id:int):
    cached_item = redis_client.get(f"item_{yoga_id}")

    if cached_item:
        return {"item_id": yoga_id, "cached": True, "data": cached_item.decode('utf-8')}

    item_data = f"Item data for {yoga_id}"

    redis_client.set(f"item_{yoga_id}", item_data)

    return {"item_id": yoga_id, "cached": False, "data": item_data}