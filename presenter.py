from view_header import Route, PresentView, Flash

class Presenter:

    def __init__(self, model):
        self.model = model

    def index(self):
        return 'index.html'

    def review(self):
        review = self.model.fetchall('review')
        args = {'review': review}
        route = Route(False, 'review.html', args)
        return PresentView(route)
