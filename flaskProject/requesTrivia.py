import requests
import json

def main():
    url ="http://127.0.0.1:2224/jsonify"

    response= requests.get(url)
    jsonDict= json.loads(response.json())
    print(f"There are {jsonDict.__len__()} questions returned from the API they are:")
    for z in range(0,jsonDict.__len__()):
        print(f"Question {z+1} is: {jsonDict[str(z)]['Question']}")

if __name__ == "__main__":
    main()

