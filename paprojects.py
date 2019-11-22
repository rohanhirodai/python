from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def pa_project(request):
    print('Incoming request')
    return Response('<body><h1>This is a PA project!</h1></body>')


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('pa', '/')
        config.add_view(pa_project, route_name='pa')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)