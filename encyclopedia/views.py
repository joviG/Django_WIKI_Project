from markdown2 import markdown
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
from .util import get_entry

wiki_entries_directory = "entries/"


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
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


def new_page(request):
    return render(request, "encyclopedia/new-page.html", {
        'edit_mode': False
    })


def save_page(request, title=None):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse("index"))
    else:
        # Used an assert method to check if method condition hold true during the execution
        assert (request.method == 'POST')
        entry_content = request.POST['entry-content']
        if not title:
            # now saving the new page
            title = request.POST['title']
            if title.lower() in [entry.lower() for entry in util.list_entries()]:
                return render(request, "encyclopedia/error.html", {
                    "error_title": "saving page",
                    "error_message": "An entry with that title already exists! Please change the title and try again."
                })

        filename = wiki_entries_directory + title + ".md"
        with open(filename, "w") as f:
            f.write(entry_content)
        return HttpResponseRedirect(reverse("entry", args=(title)))
