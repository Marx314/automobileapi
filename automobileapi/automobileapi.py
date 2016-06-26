import json

import requests


class AutoMobileApi(object):
    def __init__(self, base_url="https://www.reservauto.net/WCF/LSI/", request_lib=requests):
        self.base_url = base_url
        self.requests = request_lib

    def get_available_cars(self, longitude=-73.58, latitude=45.54):
        response = self.requests.get(self._get_car_listing_url(latitude, longitude))
        payload = self._jsonp2json(response.content, response.encoding)

        car_data = json.loads(payload)

        return car_data['Vehicules']

    def _get_car_listing_url(self, latitude, longitude):
        car_listing_url = "LSIBookingService.asmx/" \
                          "GetVehicleProposals?" \
                          "Callback=&CustomerID=&Longitude={0}&Latitude={1}".format(longitude, latitude)
        url = self.base_url + car_listing_url
        return url

    @staticmethod
    def _jsonp2json(content, encoding):
        return content[1:-2].decode(encoding)
