import requests


class Kid(object):
    def ask_mommy_for_food(self):
        response = requests.get('http://mommy:5000/food')
        return response.json()['answer']

    def ask_daddy_for_food(self):
        response = requests.get('http://daddy:4567/food')
        return response.json()['answer']
