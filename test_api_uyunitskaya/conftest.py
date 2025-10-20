import pytest
import requests


from test_api_uyunitskaya.methods.create_obj import CreateObject
from test_api_uyunitskaya.methods.put_obj import PutObject
from test_api_uyunitskaya.methods.patch_obj import PatchObject
from test_api_uyunitskaya.methods.delete_obj import DeleteObject
from test_api_uyunitskaya.methods.get_obj import GetObject


@pytest.fixture()
def create_new_object_up():
    return CreateObject()


@pytest.fixture()
def test_object(create_new_object_up):
    body = {
        "data": {"color": "blue", "size": "biggest"},
        "name": "Test object"
    }
    create_new_object_up.create_new_obj(body)
    object_id = create_new_object_up.json["id"]
    yield create_new_object_up.json
    DeleteObject().delete_object(object_id)


@pytest.fixture()
def updated_object_up():
    return PutObject()


@pytest.fixture()
def patch_update_object_up():
    return PatchObject()


@pytest.fixture()
def delete_object_up():
    return DeleteObject()


@pytest.fixture()
def get_object_up():
    return GetObject()
