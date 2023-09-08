from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests
import json
from collections import namedtuple
from django.conf import settings
from django.contrib import messages


Candidate = namedtuple("Candidate", "name emails phones avatar created_at referrer")

BASE_URL = f"https://api.recruitee.com/c/{settings.RECRUITEE_COMPANY_ID}/"
headers = {
    'accept': 'application/json', 
    'authorization': f'Bearer {settings.RECRUITEE_API_KEY}', 
    "Content-Type": "application/json"
}

class HomeView(TemplateView):
    template_name = "index.html"

def all_cadidates(request):
    candidates = []
    URL = BASE_URL + "candidates/" 
    response = requests.get(URL, headers=headers)
    candidates_dict = json.loads(response.text)
    for candidate in candidates_dict["candidates"]:
        
        cols = (
            candidate["name"], 
            " ".join(candidate["emails"]), 
            " ".join(candidate["phones"]), 
            candidate["photo_thumb_url"], 
            candidate["created_at"], 
            candidate["referrer"]
        )
        
        candidates.append(Candidate._make(cols))
    return render( request,'retrieve_candidate.html', {"candidates": candidates})

    
def new_cadidate(request):
    if request.method == "POST":
        candidate_payload = {"candidate": {
            "name": request.POST.get("fullName"),
            "emails": [request.POST.get("email")],
            "phones":[request.POST.get("phone")],
            "social_links":[request.POST.get("portfolio")],
            "links": [request.POST.get("website")],
            "cover_letter": request.POST.get("coverLetter")
        }}
        URL = BASE_URL + "candidates/"
        response = requests.post(URL, headers=headers, json=candidate_payload)
        if response.status_code == 201:
            messages.success(request, "New candidate created successfully.")
            return redirect("/candidates")
                

    return render( request,'create_candidate.html', {})