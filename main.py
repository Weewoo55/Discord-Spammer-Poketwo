from webserver import keep_alive
import requests

channelID = 987677929561526293
headers = {
    "authorization":
    "MTAyMTA2NDQ5MzMzNTMxODU3OA.Ge4KcW.9c1i11_EzicYu3FK6crTsQ_rB3VKLII_kbazvY"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
