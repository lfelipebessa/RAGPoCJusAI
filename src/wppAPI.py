# src/wppAPI.py
import os
import sys
import requests

from config import EVOLUTION_BASE_URL, EVOLUTION_API_KEY



class EvolutionAPI():
    def __init__(self):
        pass
    def send_msg(self, message, instance, instance_key, sender_number):
        url = f"http://localhost:8080/message/sendText/{instance}"

        payload = {
            "number": sender_number,
            "text": message,
            "delay": 2000,
        }
        headers = {
            "apikey": instance_key,
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        return response