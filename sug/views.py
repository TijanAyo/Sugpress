from django.shortcuts import render

Post = [
    {
        'author': 'Sug',
        'title': 'My first Blog Post',
        'content': 'Dummy Text file',
        'date_posted': '12-02-1999'
    },
    {
        'author': 'Clone',
        'title': 'My second Blog Post',
        'content': 'Dummy Text file for the second blog post',
        'date_posted': '12-03-1999'
    }
]


def index(request):
    return render(request, 'index.html')

def press(request):

    context = {'post': Post}
    return render(request, 'press.html', context)
