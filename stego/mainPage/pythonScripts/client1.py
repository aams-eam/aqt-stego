import requests



# CONFIGURATION VARIABLES
MESSAGE = "stego"
PASSWORD = "1234"

def main():
    print(MESSAGE, PASSWORD)
    payload = {'msg': MESSAGE, 'pass': PASSWORD}
    r = requests.post("http://127.0.0.1:8000/shop", data=payload)
    if(r.status_code == 200):
        print("MSG published!")
    elif(r.status_code == 404):
        print("Error: The message could not be encoded!")
    else:
        print("Server Error!")


if __name__ == "__main__":
    main()
