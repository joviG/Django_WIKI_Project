from markdown2 import markdown
from django.shortcuts import render

from . import util
from .util import get_entry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def encyclopedia_entry(request, title):
    '''
    Calls the utility function to get the content of requested encyclopedia
    '''
    try:
        content = get_entry(title)
        content_html = markdown(content)
        return render(request, 'entry.html', {      # Render a page that displays the content of the entry
            'title': title,
            'content': content_html
        })

    except:
        content = get_entry(title)
        return render(request, 'error.html', {
            'error_message': 'Page not found'
        })

    # # pass the title as a parameter to the function
    # content = get_entry(title)

    # if not content:
    #     return render(request, 'error.html', {  # Render an error page indicating that the requested page was not found
    #         'error_message': 'Page not found'
    #     })

    # content_html = markdown(content)
    # return render(request, 'entry.html', {      # Render a page that displays the content of the entry
    #     'title': title,
    #     'content': content_html
    # })
