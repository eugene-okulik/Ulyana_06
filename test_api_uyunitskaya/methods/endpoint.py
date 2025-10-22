import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None

    @allure.step('Check status code')
    def check_statuscode_is_200(self):
        assert self.response.status_code == 200, f"Expected 200, got {self.response.status_code}"

    @allure.step('Check color')
    def check_color(self, color):
        assert self.json['data']['color'] == color, f"Expected color '{color}', got '{self.json['data']['color']}'"

    @allure.step('Check size')
    def check_size(self, size):
        assert self.json['data']['size'] == size, f"Expected size '{size}', got '{self.json['data']['size']}'"

    @allure.step('Check name')
    def check_name(self, name):
        assert self.json['name'] == name, f"Expected name '{name}', got '{self.json['name']}'"

    @allure.step('Check status code 400')
    def check_statuscode_is_400(self):
        assert self.response.status_code == 400, f"Expected 400, got {self.response.status_code}"

    @allure.step('Check object id')
    def check_object_id(self, object_id):
        assert str(self.json['id']) == str(object_id), f"Expected id '{object_id}', got '{self.json['id']}'"

    @allure.step('Check object not found')
    def check_statuscode_is_404(self):
        assert self.response.status_code == 404, f"Expected 404, got {self.response.status_code}"
