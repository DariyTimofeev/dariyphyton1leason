import requests

def analyze_users():
    url = "https://dummyjson.com/users"

    try:
        r = requests.get(url)
        users = r.json()["users"]

        u30 = 0
        green_eyes = 0
        sf = 0

        for user in users:
            if user["age"] < 30:
                u30 += 1
            if user["gender"] == "female" and user["eyeColor"] == "green":
                green_eyes += 1
            if user["address"]["city"] == "San Francisco":
                sf += 1

        print("Людей молодше 30:", u30)
        print("Женщин с зеленимы глазами:", green_eyes)
        print("Сколько людей живут в Сан-Франциско:", sf)

    except:
        print("Error :(")

analyze_users()