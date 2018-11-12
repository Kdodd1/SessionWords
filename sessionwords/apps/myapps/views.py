from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
import re

WORD_REGEX = re.compile(r'^[a-zA-z]*$')
def index(request):
	try: 
		request.session['words']
	except KeyError as e:
		print(e)
		request.session['words'] = []
	return render(request, 'myapps/index.html')

def process(request):
	time = strftime('%#H:%M:%S%p, %B, %#d %Y', localtime())
	if 'big_fonts' in request.POST:
		showbig = "big"
	else: 
		showbig = "small"

	if request.POST['word'] == '':
		messages.warning(request, '*Please enter a word.')
		return redirect('/')
	elif not WORD_REGEX.match(request.POST['word']):
		messages.warning(request, "*Please don't use special characters or numbers")
		return redirect('/')

	else:

		temp_list = request.session['words']
		temp_list.append({"word": request.POST['word'], "color": request.POST['color'], "big_fonts": showbig, "time": time})
		request.session['words'] = temp_list

		print('*'*90)
		print(request.session['words'])
		print('*'*90)
		return redirect('/')

def clear(request):
	request.session.clear()

	return redirect('/')
