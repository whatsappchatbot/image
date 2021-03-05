import requests
import base64
url="https://api.imgbb.com/1/upload"  ### using imgbb

def upload_and_get_link(filename):        ### put address here of image file
    with open(filename, "rb") as file:
        payload = {
            "key": "4a05d0ef6da23523ac0b6c93eb131bb7",
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)    ##3uploading the image
        abc  = res.json()
        return abc['data']['url']        #### get hhtp url of it..
    
    
    
    
    
    
    
    
    
    
    
"""    
with open("curd.jpg", "rb") as file:
    payload = {
        "key": "4a05d0ef6da23523ac0b6c93eb131bb7",
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)
with open("ghee.jpg", "rb") as file:
    payload = {
        "key": "4a05d0ef6da23523ac0b6c93eb131bb7",
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)
with open("Paneer.jpg", "rb") as file:
    payload = {
        "key": "4a05d0ef6da23523ac0b6c93eb131bb7",
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)"""
