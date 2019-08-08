#import section
import jinja2
import os
import webapp2
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def quotePicker():
    decider = random.randint(0,2)
    quotes = ['If you talk to a man in a language he understands, that goes to his head. If you talk to him in his language, that goes to his heart. \n - Nelson Mandela',
              'A different language is a different vision of life. \n -Federico Fellini',
              'With languages, you are at home anywhere. \n -Edmund de Waal ']
    chosen_quote = quotes[decider]
    return chosen_quote

def es_translator(x):
    if x[-1:] == 'z':
        return (x[:-1] + 'ces')
    elif x[-1:] == 'a' or x[-1:] == 'e' or x[-1:] == 'o' or x[-1:] == 'i' or x[-1:] == 'u':
        return (x + 's')
    else:
        return (x + 'es')



#handlers
class WelcomePageHandler(webapp2.RequestHandler):
    def get(self):
        welcome_page_template = the_jinja_env.get_template('templates/welcome_page_template.html')
        welcome_variables = {
            'quote': str(quotePicker())
        }
        self.response.write(welcome_page_template.render(welcome_variables))



class ListPageHandler(webapp2.RequestHandler):
    def get(self):
        list_page_template = the_jinja_env.get_template('templates/list_page_template.html')
        self.response.write(list_page_template.render())


class ResultPageHandler(webapp2.RequestHandler):
    def post(self):
        result_page_template = the_jinja_env.get_template('templates/result_page_template.html')
        item1 = self.request.get('Item 1')
        item2 = self.request.get('Item 2')
        item3 = self.request.get('Item 3')
        item4 = self.request.get('Item 4')
        item5 = self.request.get('Item 5')
        list_variables = {
            'firstitem': item1,
            'seconditem': item2,
            'thirditem': item3,
            'fourthitem': item4,
            'fifthitem': item5
        }
        self.response.write(result_page_template.render(list_variables))

#app configuration section
app = webapp2.WSGIApplication([
    ('/', WelcomePageHandler), #Welcome Page
    ('/list-go', ListPageHandler), #List Page
    ('/result', ResultPageHandler) #Results Page
], debug=True)
