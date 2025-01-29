import json
import sys
import requests
with open ("1.json", "r") as fh:
    json_data=json.load(fh)
    for ele in json_data:
        for key, value in ele.items():
            print(ele["Source URL"])
            print(key)
            print(value)
            print("___________")
    sys.exit()
