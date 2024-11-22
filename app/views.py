from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def priya(request):
    return HttpResponse('priya from tamil nadu')

def nithya(request):
    return HttpResponse('<h1>nithya very good person </h1>')

def keerthi(request):
    return HttpResponse('<h1><marquee>keerthi also from tamil nadu </marquee></h1>')

def biodata(request):
    return HttpResponse('''
    <h1>Name is janani</h1>
    <i> age is 21 </i>
    <b>fav actors sk</b>
    <img src='https://tse1.mm.bing.net/th?id=OIP.Qi1uIygCclDq04fBZoCTHQHaFj&pid=Api&P=0&h=180'>
                        ''')
