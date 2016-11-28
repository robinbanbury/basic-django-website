from django.shortcuts import render
# 'render' looks in a templates directory at the ROOT of the website

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',
                  {'page_content': ['If you would like to contact me, please email me',
                                    'robinsmith@me.com'],
                   }
                  )
# You can pass in Django/Jinja variables using this
