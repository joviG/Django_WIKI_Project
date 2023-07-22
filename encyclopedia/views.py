from markdown2 import markdown
from django.shortcuts import render

from . import util
from .util import get_entry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    '''
    Calls the utility function to get the content of requested encyclopedia
    '''
    entry_contents = get_entry(title)
    html_entry_content = markdown(entry_contents) if entry_contents else None

    return render(request, "encyclopedia/entry.html", {
        "title": title if entry_contents is not None else "Error",
        "body_content": html_entry_content,
        "entry_exists": entry_contents is not None
    })


def new_page(request):
    return render(request, "encyclopedia/new-page.html", {
        'edit_page_title': '',
        'edit_page_content': ''
    })
