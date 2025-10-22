import requests
import allure


from test_api_uyunitskaya.methods.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Get object by ID')
    def get_object(self, object_id):
        self.response = requests.get(
            f"{self.url}/{object_id}",
            headers=self.headers
        )
        self.json = self.response.json() if self.response.ok else None
        return self.response
