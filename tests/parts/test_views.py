import json

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.test import APIClient

from parts.models import Part


class TestPartViews(TestCase):
    api_client = APIClient()
    endpoint = "/parts/"

    @classmethod
    def setUpTestData(cls):
        Part.objects.create(
            name="Heavy Coil",
            sku="SDJDDH8111GGG",
            description="Tightly wound nickel-gravy alloy spring",
            weight_ounces=25,
            is_active=True,
        )
        Part.objects.create(
            name="Microchip",
            sku="123RTYU89QPSD",
            description="Used for heavy-load computing",
            weight_ounces=1,
            is_active=True,
        )

    def test_get_list_parts(self):
        response = self.api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_get_part_by_id(self):
        response = self.api_client.get(self.endpoint + "2/")
        assert response.status_code == 200
        assert json.loads(response.content)["id"] == 2

    def test_get_part_by_id_not_exists(self):
        response = self.api_client.get(self.endpoint + "100/")
        assert response.status_code == 404

    def test_post_parts(self):
        payload = {
            "name": "Test part",
            "sku": "TTTT00EEEECV4",
            "description": "This is a test",
            "weight_ounces": 17,
            "is_active": False,
        }
        response = self.api_client.post(self.endpoint, data=payload)
        assert response.status_code == 201
        new_part = response.data
        new_part.pop("id")
        assert new_part == payload

    def test_post_parts_wo_all_fields(self):
        payload = {
            "name": "Test part",
        }
        response = self.api_client.post(self.endpoint, data=payload)
        assert response.status_code == 400

    def test_put_part(self):
        payload = {
            "name": "New name",
            "sku": "TTTT00EEEECV4",
            "description": "This is a test",
            "weight_ounces": 17,
            "is_active": False,
        }
        response = self.api_client.put(self.endpoint + "1/", payload)
        assert response.status_code == 200
        assert Part.objects.get(pk=1).name == "New name"

    def test_patch_part(self):
        payload = {
            "name": "New name",
        }
        response = self.api_client.patch(self.endpoint + "1/", payload)
        assert response.status_code == 200
        assert Part.objects.get(pk=1).name == "New name"

    def test_delete_part(self):
        part = Part.objects.create(
            name="Another part",
            sku="S11GGGTG43DVB",
            description="Another part description",
            weight_ounces=20,
            is_active=True,
        )
        part_id = part.id
        response = self.api_client.delete(self.endpoint + f"{part_id}/")
        assert response.status_code == 204
        with self.assertRaises(
            ObjectDoesNotExist,
        ):
            Part.objects.get(pk=part_id)

    def test_top_words(self):
        Part.objects.create(
            name="Another part",
            sku="S11GGGTG43DVB",
            description="Word word word word word word",
            weight_ounces=20,
            is_active=True,
        )
        Part.objects.create(
            name="Test part",
            sku="S11GGGTG43DVB",
            description="Another test, another test. Another test; Another Test?",
            weight_ounces=20,
            is_active=True,
        )
        response = self.api_client.get(self.endpoint + "top-words")
        assert response.status_code == 200
        words = response.data["words"]
        assert words[0] == "word"
        assert len(words) == 5
