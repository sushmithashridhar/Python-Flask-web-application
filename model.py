from IModel import IModel

class AppModel(IModel):

    dict = [{'termoffered':'Fall',
            'yearoffered':2018,
            'timeoftheweekoffered': 'Monday',
            'instructor': 'Wu Chang Feng',
            'review':'Teaches Cloud and Inernet',
            'rating':5},
            {'termoffered': 'Fall',
             'yearoffered': 2018,
             'timeoftheweekoffered': 'Tuesday',
             'instructor': 'David Maier',
             'review': 'Intro to Database management',
             'rating': 5},
            ]

    def fetchall(self, dict):
        return [{'termoffered':'Fall',
            'yearoffered':2018,
            'timeoftheweekoffered': 'Monday',
            'instructor': 'Wu Chang Feng',
            'review':'Teaches Cloud and Inernet',
            'rating':5},
            {'termoffered': 'Fall',
             'yearoffered': 2018,
             'timeoftheweekoffered': 'Tuesday',
             'instructor': 'David Maier',
             'review': 'Intro to Database management',
             'rating': 5},
            ]
