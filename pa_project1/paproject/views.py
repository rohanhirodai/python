from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(route_name='hello')
class PaprojectViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'PaprojectViews'

    @property
    def full_name(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return first + ' ' + last

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        return {'page_title': 'Home View'}

  
    @view_config(renderer='hello.pt')
    def hello(self):
        return {'page_title': 'Hello View'}

