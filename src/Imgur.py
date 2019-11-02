import requests
import json


class Imgur:

    def __init__(self, client_id):
        self.url_upload_image = 'https://api.imgur.com/3/image'
        self.client_id = client_id

    def upload_image(self, image):
        payload = {'image': image}

        headers = {
            'Authorization': 'Client-ID ' + self.client_id
        }

        response = requests.post(self.url_upload_image, data=payload, headers=headers)

        if response.status_code == 200:
            json_response = json.loads(response.text)

            link = json_response.get("data").get("link")

            return link
