

class Guitar:
    def __init__(self, name='', year=0, cost=0):
        pass

    def get_age(self, year):

        age = 2018 - int(year)
        return age

    def is_vintage(self, age):
        if age > 50:
            vintage = 'Yes'
        else:
            vintage = 'No'
        return vintage