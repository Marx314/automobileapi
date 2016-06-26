import json
from unittest import TestCase
from unittest.mock import Mock
from automobileapi.automobileapi import AutoMobileApi


class AutoMobileApiTest(TestCase):
    request_mock = Mock()
    response_mock = Mock()

    def setUp(self):
        self.auto = AutoMobileApi(request_lib=self.request_mock)

    def test_get_auto_test(self):
        car = {"ExtensionData": {}, "Id": "JTDKDTB37F1092345", "Name": "3041", "ModelName": "PRIUS-C",
               "Immat": "FKD8655", "EnergyLevel": 100, "Position": {"ExtensionData": {}, "Lat": 42.42, "Lon": -73.42}}
        response_content = '({"ExtensionData":{},"UserPosition":{"ExtensionData":{},"Lat":45.54,"Lon":-73.58},' \
                           '"Vehicules":[' + json.dumps(car) + ']})\n'

        self.request_mock.get.return_value = self.response_mock
        self.response_mock.configure_mock(content=response_content.encode('utf-8'), encoding='utf-8')

        cars = self.auto.get_available_cars()
        self.assertEqual(1, len(cars))
        self.assertDictEqual(cars[0], car)
