import json
import os

FILE_PATH = "data/incidents.json"


def load_incidents():

    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []


def save_incident(incident):

    incidents = load_incidents()

    incidents.append(incident)

    with open(FILE_PATH, "w") as file:
        json.dump(
            incidents,
            file,
            indent=4
        )