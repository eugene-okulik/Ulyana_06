import allure
import requests


from test_api_uyunitskaya.methods.endpoint import Endpoint


class PatchObject(Endpoint):
    @allure.step('Patch a object')
    def patch_object(self, body, object_id):
        self.response = requests.patch(
            f"{self.url}/{object_id}",
            json=body,
            headers=self.headers
        )
        self.json = self.response.json()
        return self.response
