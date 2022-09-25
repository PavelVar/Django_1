from django.shortcuts import render


def index(request):
    data = {'page_name': 'Main',
            'title': 'Main page',
            'values': ['word_1', 'word_2', 'word_3'],
            'my_dict': {'param_1': 123, 'param_2': 'some text', 'param_3': 'text again'}
            }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

