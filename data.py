import json
from pathlib import Path


DATA_FOLDER = Path(__file__).parent / "data"


def load_json(filename):

    path = DATA_FOLDER / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_universities():

    return load_json("universities.json")


def get_degrees():

    return load_json("degrees.json")


def get_scholarships():

    return load_json("scholarships.json")


def get_entrance_tests():

    return load_json("entrance_tests.json")


def search_universities(city=None):

    universities = get_universities()

    if not city:
        return universities

    return [
        university
        for university in universities
        if university["city"].lower() == city.lower()
    ]


def search_scholarships():

    return get_scholarships()
