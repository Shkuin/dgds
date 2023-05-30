from .metadata_template import template
from path import Path
import requests
import os
import json
from .defense import *


def upload_file_to_ipfs_from_django(file):
    # with Path(file).open("rb") as fp:
    file_binary = file.read()
    ipfs_url = "http://127.0.0.1:5001"
    endpoint = "/api/v0/add"
    response = requests.post(ipfs_url + endpoint, files={"file": file_binary})
    ipfs_hash = response.json()["Hash"]
    filename = str(file)
    file_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
    print(file_uri)
    return file_uri


def convert_game_file_to_metadata(file):
    game_file_uri = upload_file_to_ipfs_from_django(file)
    cipher = AESCipher("")
    encrypted_message = cipher.encrypt(game_file_uri)
    key = cipher.key
    return game_file_uri, encrypted_message, key


def upload_array_to_ipfs(array):
    uri_array = []
    for file in array:
        uri_array.append(upload_file_to_ipfs_from_django(file))
    return uri_array


def upload_json_to_ipfs(metadata_template):
    metadata_json = json.dumps(metadata_template)
    api_url = "http://127.0.0.1:5001/api/v0"
    files = {"file": ("metadata.json", metadata_json)}
    response = requests.post(f"{api_url}/add", files=files)
    ipfs_hash = response.json()["Hash"]
    return f"https://ipfs.io/ipfs/{ipfs_hash}?filename=metadata.json"


def create_metadata_json(
    name, genre, description, platform, icon, images, price, wallet_address, nft_address
):
    metadata_template = template
    metadata_template["name"] = name
    metadata_template["genre"] = genre
    metadata_template["description"] = description
    metadata_template["platform"] = platform
    metadata_template["icon"] = upload_file_to_ipfs_from_django(icon)
    metadata_template["images"] = upload_array_to_ipfs(images)
    metadata_template["price"] = float(price)
    metadata_template["wallet_address"] = wallet_address
    metadata_template["nft_address"] = nft_address

    return json.dumps(metadata_template)