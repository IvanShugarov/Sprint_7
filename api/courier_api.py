import requests
from urls import CREATE_COURIER, LOGIN_COURIER

class CourierApi:
    def create_courier(self,payload):
        response = requests.post(CREATE_COURIER,data=payload)
        return response
    
    def login_courier(self,payload):
        response = requests.post(LOGIN_COURIER,data=payload)
        return response

    def delete_courier(self,courier_id):
        response = requests.delete(CREATE_COURIER+"/"+str(courier_id))
        return response