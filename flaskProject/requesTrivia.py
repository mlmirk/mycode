import requests
import json

def main():
    #target flask route when running locally
    url ="http://127.0.0.1:2224/jsonify"
    #make request and store response
    response= requests.get(url)
    jsonDict= json.loads(response.json())
    #display something human readable 
    print(f"There are {jsonDict.__len__()} questions returned from the API they are:")
    for z in range(0,jsonDict.__len__()):
        print(f"Question {z+1} is: {jsonDict[str(z)]['Question']}")

if __name__ == "__main__":
    main()

