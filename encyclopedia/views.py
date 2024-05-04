import random
from django.shortcuts import render

from . import util
import markdown2
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

# Get list of all pages
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Get content of a page
def content(request, title):
    # Retrieve the page content
    page_content = util.get_entry(title)

    if page_content is None:
        # If page content does not exist, set title to "Page not found" and content to None
        title = "Page not found"
        page_content = None
    else:
        # Convert Markdown content to HTML
        page_content = markdown2.markdown(page_content)

    return render(request, "encyclopedia/content.html", {
        "title": title,
        "content": page_content
    })

# Search for a page
def search(request):
    if request.method == "POST":
        query = request.POST.get("q")
        entries = util.list_entries()
        if query in entries:
            # If query matches an entry, redirect to content page for that entry
            return redirect('content', title=query)
        else:
            suggestions = [entry for entry in entries if query.lower() in entry.lower()]
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })
    else:
        # If request method is not POST, redirect to index page
        return redirect('index')

# Create new page
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        # Check if entry already exists
        if util.get_entry(title) is not None:
            messages.error(request, f"Entry '{title}' already exists. Please choose a different title.")
            return redirect('new_page')

        # Save new entry
        util.save_entry(title, content)
        return redirect('content', title=title)

    return render(request, "encyclopedia/newpage.html", {'messages': messages.get_messages(request)})


# Edit page
def edit_page(request, title):
    if request.method == "POST":
        new_title = request.POST.get("title")
        content = request.POST.get("content")
        
        # Check if either title or content is empty
        if not new_title or not content:
            messages.error(request, "Please fill in both the title and content fields.")
            return redirect('edit_page', title=title)  # Redirect back to the edit page with the same title
        
        # Save the entry with the new title
        util.save_entry(new_title, content)
        
        # Redirect to the original entry page
        return redirect('content', title=title)

    # Retrieve the existing content
    page_content = util.get_entry(title)

    if page_content is None:
        title = "Page not found"
        page_content = None
    else:
        page_content = markdown2.markdown(page_content)

    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "content": page_content
    })

# Random page
def random_page(request):
    entries = util.list_entries()
    random_page = entries[random.randint(0, len(entries)-1)]
    return redirect('content', title=random_page)