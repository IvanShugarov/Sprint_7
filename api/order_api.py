import requests
from urls import ORDERS
import json

class OrdersApi:
    def create_order(self,payload):
        payload_string = json.dumps(payload)
        response = requests.post(ORDERS,data=payload_string,headers={"Content-Type": "application/json"})
        return response
    
    def get_order_list(self):
        response = requests.get(ORDERS)
        return response