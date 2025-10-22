import pytest
import allure


from test_api_uyunitskaya.methods.create_obj import CreateObject
from test_api_uyunitskaya.methods.put_obj import PutObject
from test_api_uyunitskaya.methods.patch_obj import PatchObject
from test_api_uyunitskaya.methods.delete_obj import DeleteObject
from test_api_uyunitskaya.methods.get_obj import GetObject


@allure.feature('Main_obj')
@allure.story('Creating multiple objects')
@pytest.mark.critical
@pytest.mark.parametrize("name", ["^&*", "P", " "])
def test_create_object(name, create_new_object_up):
    body = {
        "data": {"color": "blue", "size": "biggest"},
        "name": name
    }
    create_new_object_up.create_new_obj(body)
    create_new_object_up.check_statuscode_is_200()
    create_new_object_up.check_name(name)
    create_new_object_up.check_color("blue")
    create_new_object_up.check_size("biggest")
    object_id = create_new_object_up.json["id"]
    DeleteObject().delete_object(object_id)
    print(f"Object with name '{name}' created and deleted successfully")


@allure.feature('Main_obj')
@allure.story('Updating an object with PUT')
@pytest.mark.medium
def test_put_object(test_object, updated_object_up):
    object_id = test_object["id"]
    body = {
        "data": {"color": "pink", "size": "small"},
        "name": test_object["name"]
    }
    updated_object_up.put_object(body, object_id)
    updated_object_up.check_statuscode_is_200()
    updated_object_up.check_color("pink")
    updated_object_up.check_size("small")
    print(f"Object with ID {object_id} updated successfully with PUT")


@allure.feature('Main_obj')
@allure.story('Updating an object with PATCH')
def test_patch_object(test_object, patch_update_object_up):
    object_id = test_object["id"]
    body = {
        "data": {"color": "green"}
    }
    patch_update_object_up.patch_object(body, object_id)
    patch_update_object_up.check_statuscode_is_200()
    patch_update_object_up.check_color("green")
    print(f"Object with ID {object_id} updated successfully with PATCH")


@allure.feature('Main_obj')
@allure.story('Get an object by ID')
def test_get_object_by_id(test_object, get_object_up):
    object_id = test_object["id"]
    get_object_up.get_object(object_id)
    get_object_up.check_statuscode_is_200()
    get_object_up.check_object_id(object_id)
    print(f"Object with ID {object_id} fetched successfully")


@allure.feature('Main_obj')
@allure.story('Deleting an object')
def test_delete_object(test_object, delete_object_up, get_object_up):
    object_id = test_object["id"]
    delete_object_up.delete_object(object_id)
    delete_object_up.check_statuscode_is_200()
    get_object_up.get_object(object_id)
    get_object_up.check_statuscode_is_404()
    print(f"Object with ID {object_id} deleted successfully.")
