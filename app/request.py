from app import app
import urllib.request,json
from .models import User

User=user.User

#random quote generator
api_key=app.config['QUOTE_URL']

def get_random_quote():
    '''
    Function that gets the random quote
    '''
    get_quote_url = base_url

    with urllib.request.urlopen(api_key) as url:
        get_quote_data = url.read()
        quote_json = json.loads(get_quote_data)

        quote_result = None

        if quote_json:
            qoute_item = quote_json
            quote_result = process_quote_data(qoute_item)

    return quote_result