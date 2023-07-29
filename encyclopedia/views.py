import re
import random

from markdown2 import markdown
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
from .util import get_entry

wiki_entries_directory = "entries/"


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": "Home",
        "heading": "All Pages"
    })


def entry_page(request, title):
    '''
    Calls the utility function to get the content of requested encyclopedia
    '''
    entry_contents = get_entry(title)
    html_entry_contents = markdown(entry_contents) if entry_contents else None

    return render(request, "encyclopedia/entry.html", {
        "title": title if entry_contents is not None else "Error",
        "body_content": html_entry_contents,
        "entry_exists": entry_contents is not None
    })


def search(request):
    query = request.GET['q']
    if util.get_entry(query):
        # query matches a title
        return HttpResponseRedirect(reverse("entry", args=(query,)))
    else:
        # query does not match!
        return render(request, "encyclopedia/index.html", {
            "entries": [entry for entry in util.list_entries() if query.lower() in entry.lower()],
            "title": f'"{query}" search results',
            "heading": f'Search Results for "{query}"'
        })


def new_page(request):
    return render(request, "encyclopedia/new-page.html", {
        'edit_mode': False,
        'edit_page_title': '',
        'edit_page_contents': ''
    })


def save_page(request, title=None):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse("index"))
    else:
        assert (request.method == 'POST')
        entry_content = request.POST['entry-content']
        if not title:
            # We are saving a new page
            title = request.POST['title']
            if title.lower() in [entry.lower() for entry in util.list_entries()]:
                return render(request, "encyclopedia/error.html", {
                    "error_title": "saving page",
                    "error_message": "An entry with that title already exists! Please change the title and try again."
                })

        filename = wiki_entries_directory + title + ".md"
        with open(filename, "w") as f:
            f.write(entry_content)
        return HttpResponseRedirect(reverse("entry", args=(title,)))


def edit_page(request, title):
    entry_contents = util.get_entry(title)
    if entry_contents is None:
        return HttpResponseRedirect(reverse("index"))

    return render(request, "encyclopedia/new-page.html", {
        'edit_mode': True,
        'edit_page_title': title,
        'edit_page_contents': entry_contents
    })


def random_page(request):
    entry_title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry", args=(entry_title,)))
