import random

options = {
    "year": {
        "start": 1946,
        "end": 2020
    },
    "body": ["Sedan", "Wagon", "Hatchback", "Coupe", "SUV", "Utility", "MPV",
    "Convertible", "Van"],
    "engine_location": ["front", "mid", "rear"],
    "engine_mounting": ["transverse", "longitudinal"],
    "drive": ["FWD", "RWD", "AWD", "4x4"],
    "engine": {
        "aspiration": ["naturally aspirated", "turbocharged"],
        "layout": [
            {
                "Inline-": [3, 4, 5, 6]
            },
            {
                "60° V": [6, 8, 12]
            },
            {
                "90° V": [6, 8, 10]
            },
            {
                "Boxer-": [4, 6]
            }
        ]
    }
}

def choose_year():
    years = options["year"]
    inclusive_range = range(years["start"], years["end"] + 1)
    return random.choice(inclusive_range)

def choose_body():
    return random.choice(options["body"])

def choose_engine_location():
    return random.choice(options["engine_location"])

def choose_engine_mounting():
    return random.choice(options["engine_mounting"])

def choose_drive():
    return random.choice(options["drive"])

def choose_engine():
    aspiration = random.choice(options["engine"]["aspiration"])
    style = random.choice(options["engine"]["layout"])
    style_name = list(style.keys())[0]
    cyl_count = random.choice(style[style_name])
    engine_string = aspiration + " " + style_name + str(cyl_count)
    return engine_string

# Make it a class for the fuck of it lol
class Car:
    def __init__(self):
        self.year = choose_year()
        self.engine_location = choose_engine_location()
        self.engine_mounting = choose_engine_mounting()
        self.drive = choose_drive()
        self.engine = choose_engine()
        self.body = choose_body()

    def describe(self):
        return f"A {self.year} {self.drive} {self.body} with a {self.engine_location}-"\
        f"{self.engine_mounting} mounted {self.engine}!"

car = Car()
print("Your next car will be:")
print(car.describe())
input("Press enter to close")
