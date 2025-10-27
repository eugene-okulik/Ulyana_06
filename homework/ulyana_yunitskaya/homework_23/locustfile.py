from locust import HttpUser, task, between
import random


class ObjectUser(HttpUser):


    @task(2)
    def get_all_objects(self):
        self.client.get("/object")


    @task(1)
    def get_one_object(self):
        obj_id = random.choice([3691, 3696, 3703])
        self.client.get(f"/object/{obj_id}")


    @task(3)
    def create_object(self):
        body = {
            "data": {
                "color": random.choice(["blue", "pink", "green"]),
                "size": random.choice(["small", "biggest"])
            },
            "name": f"Object_{random.randint(1000, 9999)}"
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/object", json=body, headers=headers)
        if response.status_code == 200:
            obj_id = response.json().get("id")
            self.client.delete(f"/object/{obj_id}")
