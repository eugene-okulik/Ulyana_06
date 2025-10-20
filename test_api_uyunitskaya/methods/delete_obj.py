import requests
import allure


from test_api_uyunitskaya.methods.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.response = requests.delete(
            f"{self.url}/{object_id}",
            headers=self.headers
        )
        return self.response
