from django.shortcuts import render

import requests
from django.http import JsonResponse

def api_test(request):
	url = "https://pokeapi.co/api/v2/pokemon/"


	nxt = request.GET.get('next_page')
	prv = request.GET.get('previous_page')

	if nxt:
		response = requests.get(nxt).json()
	elif prv:
		response = requests.get(prv).json()
	else:
		response = requests.get(url).json()

	
	context ={
	"response": response,
	}
	return render(request, 'api.html', context)

def api_detail(request):
	url = request.GET.get('detail')
	response = requests.get(url).json()

	context = {
	"r":response,
	}
	return render(request,"detail.html",context)