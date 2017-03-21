from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import QuoteForm
from .models import Quote
from .forms import QuoteForm
import random

# Create your views here.



class Welcome(View):
	def get(self, request):
		form = QuoteForm()

		rquote = random.choice(Quote.objects.all())
		
		speakerButtons = [rquote, random.choice(Quote.objects.all()), random.choice(Quote.objects.all())]
		random.shuffle(speakerButtons)
		print 'speakerButtons'
		print speakerButtons[0].speaker
		print speakerButtons[1].speaker
		print speakerButtons[2].speaker
		context = {
		'rquote':rquote,
		'speakerButtons':speakerButtons,	
		'form':form,
		'quotes':Quote.objects.all()
		}
		return render(request, 'quotes/index.html', context)



class Quotes(View):
	def get(self, request):
		# fetch all quotes and display on index page
		print request
		context = {
		'quotes': Quote.objects.all()
		}
		print 'inside Quotes/get'
		return render(request, 'quotes/quotes_index.html', context)

	def post(self, request):
		# retrieve form data
		bound_form = QuoteForm(request.POST)
		if bound_form.is_valid():
			Quote.objects.create(quote=request.POST['quote'], speaker=request.POST['speaker'])
		# redirect to the 'get' of quotes
			print 'inside Quotes/post'
			return redirect('/quotes')
		else:
			return redirect('/')

class Speakers(View):
	def get(self, request):
		rquote = random.choice(Quote.objects.all())
		speakerButtons = [rquote, random.choice(Quote.objects.all()), random.choice(Quote.objects.all())]
		random.shuffle(speakerButtons)
		context = {
		'rquote':rquote,
		'speakerButtons':speakerButtons
		}
		return render(request, 'quotes/speakers_index.html', context)

	def post(self, request):
		pass

class Categories(View):
	def get(self, request, cat):
		
		if cat == 'All':
			quotes = Quote.objects.all()
		else:
			quotes = Quote.objects.filter(category=cat)

		context = {
		'quotes': quotes
		}
		return render(request, 'quotes/quotes_index.html', context)
	def post(self, request, cat):
		pass

