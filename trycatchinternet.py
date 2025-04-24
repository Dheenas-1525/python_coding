import requests

try:
    img = requests.get("")
    open("image.jpg", "wb").write(img.content)
    print("Image downloaded successfully.")
except:
    print("Something went wrong. Please check your internet connection.")
