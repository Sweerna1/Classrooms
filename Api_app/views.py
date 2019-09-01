from django.shortcuts import render

import requests
from django.http import JsonResponse

def api_test(request):
	url = "https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20"
	response = requests.get(url).json()

	context ={
	"results": response['results'],
	}
	return render(request, 'api.html', context)

def api_detail(request):
	url = request.GET.get('detail')
	response = requests.get(url).json()

	context = {
	"r":response,
	}
	return render(request,"detail.html",context)