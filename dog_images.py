import webbrowser
import requests


def generate_dog_image():
    r = requests.get("https://random.dog/woof.json")
    if r.status_code == 200:
        image_url = r.json()["url"]
        return image_url
    else:
        return "an error occured while generating dog image!"


if __name__ == "__main__":
    dog_image = generate_dog_image()
    webbrowser.open(dog_image)
