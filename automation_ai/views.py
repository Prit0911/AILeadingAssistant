from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Query
from django.contrib import messages
from google import genai
import json, csv

import os

client = genai.Client(api_key = 'YOUR_API_KEY')

def base(req):
    return render(req, 'base.html')

def index(req):
    return render(req, 'home.html')

def query(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        cname = req.POST.get('cname')
        message = req.POST.get('message')

        prompt = f"""
            Analyze this business lead.

            Return ONLY valid JSON.

            Example:

            {{
                "priority": "High",
                "summary": "Customer is interested in AI services.",
                "next_action": "Schedule a call."
            }}

            Name: {name}
            Company: {cname}
            Message: {message}

            Do not return markdown.
            Do not return explanations.
            Only return JSON.
        """
        
        try:
            response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents= prompt,
            )
        except Exception as e:
            print(e)
            messages.error(
                req, 
                "AI service temporarily unavailable. Please try again later"
            )

            return redirect('query')
        
        try:
            clean_text = response.text.replace("'''json","").replace("'''","").strip()
            result = json.loads(clean_text)
        except Exception as e:
            print('Json Error:',e)
            print('Response:',response.text)

            message.error(req, 'Failed to parse AI response.')
            return redirect('query')
        

        entry = Query(name=name, email=email, company=cname, message=message, priority=result['priority'], summary=result['summary'], next_action= result['next_action'])
        entry.save()
        
        file_exits = os.path.isfile('leads.csv')
        with open("leads.csv",'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exits:
                writer.writerow([
                    "Priority",
                    "Summary",
                    "Next Action",
                    "Name",
                    "Email",
                    "Company",
                    "Message"
                ])

                writer.writerow([
                    result['priority'],
                    result['summary'],
                    result['next_action'],
                    name,
                    email,
                    cname,
                    message
                ])
            
        messages.success(req, 'Data Sent...')
        return redirect('query')
    return render(req, 'query.html')

def about(req):
    return render(req, 'about.html')
