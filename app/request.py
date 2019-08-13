import urllib.request,json
from .models import Quote

api_key = None

def configure_request(app):
    global api_key
    api_key=app.config['QUOTE_URL']


def get_random_quote():
    '''
    Function that gets the random quote
    '''
    get_quote_url = api_key

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        quote_json = json.loads(get_quote_data)

        quote_result = None

        if quote_json:
            qoute_item = quote_json
            quote_result = process_quote_data(qoute_item)

    return quote_result

def process_quote_data(source_list):
    '''
    this function will process all the quotes from the api key as per quote class arguments
    each quote should have an author and the quote
    '''
    processed_quote = []
    quote = source_list['quote']
    author = source_list['author']

    new_quote = Quote(quote, author)
    print('PROCESSED QUOTE',new_quote)

    processed_quote.append(new_quote)
    return processed_quote