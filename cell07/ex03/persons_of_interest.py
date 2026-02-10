#!/usr/bin/python

def famous_births(persons_dict):
    # sort the dictionary by the person's date of birth
    sorted_persons = dict(sorted(persons_dict.items(), key=lambda item: item[1]["date_of_birth"]))
    for key in sorted_persons:
        person = sorted_persons[key]
        name = person["name"]
        dob = person["date_of_birth"]
        print(f"{name} is a great scientist born in {dob}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)