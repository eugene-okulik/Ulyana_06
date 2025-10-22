import requests
import allure


from test_api_uyunitskaya.methods.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('Create new object')
    def create_new_obj(self, body):
        self.response = requests.post(
            self.url,
            json=body,
            headers=self.headers
        )
        self.json = self.response.json()
        return self.response
