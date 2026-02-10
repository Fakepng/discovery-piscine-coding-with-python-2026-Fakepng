#!/usr/bin/python

def array_of_names(persons):
    names = []
    for fist, last in persons.items():
        names.append(f"{fist.title()} {last.title()}")
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))