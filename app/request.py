from app import app
import urllib.request,json
from .models import User

User=user.User

#random quote generator
base_url=app.config['QUOTES_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)