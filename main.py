#!/usr/bin/env python
import os
import jinja2
import webapp2
from KalkulatorClass import calculator


# Poiskusi vsako metodo posebej
# e.g.:
# print os.path.dirname(__file__)
#  da vidis kaj naredi,
# poglej tudi dokumentacijo
# https://docs.python.org/2/library/os.path.html
template_dir = os.path.join(os.path.dirname(__file__), "templates")
# Povej jinji kje lahko najete nase template
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    """Ta class nam poenostavi delo s templati.
    Definiramo nekaj metod ki nam bodo pomagale,
    predvsem da se ne ponavljamo in da ne pisemo
    vec vrstic ampak le eno - klicemo metodo.
    """

    def write(self, *args, **kwargs):
        # Uporabo *args in **kwargs si preberi na
        # http://stackoverflow.com/questions/3394835/args-and-kwargs
        # http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-python-parameters
        return self.response.out.write(*args, **kwargs)

    def render_str(self, template, **params):
        template = jinja_env.get_template(template)
        return template.render(params)

    def render(self, template, **kwargs):
        return self.write(self.render_str(template, **kwargs))

    def render_template(self, view_filename, params=None):
        # POZOR! None se vedno primerja z "is"!
        # http://stackoverflow.com/questions/14247373/python-none-comparison-should-i-use-is-or
        # http://stackoverflow.com/questions/3257919/is-none-vs-none
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class RezultatHandler(BaseHandler):
    def post(self):
        a = self.request.get("vnosA")
        b = self.request.get("vnosB")
        operator = self.request.get("vnosOperator")
        return self.write(calculator(a,b,operator))


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/rezultat', RezultatHandler),
], debug=True)