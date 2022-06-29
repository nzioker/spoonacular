from django.shortcuts import render
import requests
import os


def index(request):
    spoonacular_endpoint = 'https://api.spoonacular.com/recipes/complexSearch' 
    spoonacular_api_key = os.environ.get('spoonacular_api_key')
    my_params = {
        'cuisine': 'Chinese'
    }

    headers = {
        "x-api-key": spoonacular_api_key,     
    }

    final_url = spoonacular_endpoint
    s_api_call = requests.get(final_url, headers=headers, params=my_params)
    s_data = s_api_call.json()
    total_results = s_data['results']
    queried_r = [total_results[i] for i in range(0,10)]
    context={"results":queried_r}
    
    return render(request, 'index.html', context)
