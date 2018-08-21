from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
		request.session['log'] = []
	return render(request, 'file/page.html')

def process(request, loc):
	if request.method != 'POST':
		return redirect('/')
	if loc == 'farm':
		gold = random.randrange(10,21)
		log_str = ('gain', 'Earned {} gold from the {} ({})'.format(gold, loc, datetime.datetime.now()))
	if loc == 'cave':
		gold = random.randrange(5,11)
		log_str = ('gain', 'Earned {} gold from the {} ({})'.format(gold, loc, datetime.datetime.now()))
	if loc == 'house':
		gold = random.randrange(2,6)
		log_str = ('gain', 'Earned {} gold from the {} ({})'.format(gold, loc, datetime.datetime.now()))
	if loc == 'casino':
		gold = random.randrange(-50,51)
		if gold < 0:
			log_str = ('loss', 'Lost {} gold from the {} ({})'.format(gold, loc, datetime.datetime.now()))
		else:
			log_str = ('gain', 'Earned {} gold from the {} ({})'.format(gold, loc, datetime.datetime.now()))
	
	request.session['gold'] += gold
	request.session['log'].insert(0,log_str)
	print request.session['log']
	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')