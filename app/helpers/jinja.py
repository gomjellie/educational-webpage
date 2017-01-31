from app import app
import re
import arrow


date_format = 'MM-DD'

# Custom filter method
@app.add_template_filter
def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)

@app.add_template_filter
def remove_milli_second(s):
    return re.sub('(\.\d{6})', '', s)
