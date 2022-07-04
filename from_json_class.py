import json


class from_json:
    def convert_to_json_method(self):
        person = {"name": "John", "age": "30", "city": "new york",
                  "hasChildren": False, "titles": ["enginerring", "programming"]}
        person_to_json = json.dumps(person, indent=4, sort_keys=True)
        print(person_to_json)
        # convert to json and write into file
        with open('person.json', 'w') as file:
            json.dump(person, file, indent=4)

    def convert_from_json_method(self):
        person = {"name": "John", "age": "30", "city": "new york",
                  "hasChildren": False, "titles": ["enginerring", "programming"]}
        person_to_json = json.dumps(person, indent=4, sort_keys=True)
        person_from_json = json.loads(person_to_json)
        print(person_from_json)
        # read from file and desirilaze to python
        with open('./person.json', 'r') as file:
            persons = json.load(file)
            print(sorted(persons.items()))
