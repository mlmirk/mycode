#!/usr/bin/env python3

def main():
    #read dracula
    vampcount=0
    with open("dracula.txt", "r" ) as vamp:
        data = vamp.read().replace('\n', ' ')
        data = data.split(".")
        for line in data:
            with open("vampirelines.txt", "a") as record:
                if "vampire" in line.lower():
                    vampcount+=1
                    record.write(line +"." "\n")

    print(f"there are {vampcount} lines that contain vampire")



if __name__ == "__main__":
    main()          
