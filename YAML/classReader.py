import yaml
import json


def main():
    with open("classdataX.json", "r") as classD:
        decodedJSON= json.load(classD)
        with open("classdata.yml", "w") as classY:
            yaml.dump(decodedJSON, classY)
            with open('classdata.yml', 'r') as yamfile:
                x=yaml.full_load(yamfile)
                me = {'color': 'Green', 'ice cream': 'Mint Chip', 'movie': 'Harry Potter'}
                x.append(me)
                print(x)
                yaml.dump(x,classY)



main()