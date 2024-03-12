from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
import openai
# import requests
# import json


openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    # print(message)
    # maxSols = 3
    # resp = requests.post("http://10.10.166.240:8000/getAnswer/", headers={"Content-Type": "application/json"},
    #                       data=json.dumps({"description": message}))
    # answer = resp.json()["answer"]
    # return answer
    # # return eval(answer)["solutions"][:maxSols]
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful mobile technical support assistant. "},
            {"role": "user", "content": message},
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer



#Login
def login_det(request):
    if request.method == "POST":
        user_email = request.POST['user']
        pass1 = request.POST['password']
        user = authenticate(username=user_email, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/login/companies/'+user_email+'')
        
        else:
            messages.success(request,("Invalid user"))
            return redirect('login')
    else:
        return render(request,"login/login.html",{})



#companies
def comp(request, mem_id):
    context = {
    'mem_id': mem_id,
    }
    return render(request,"home/companies.html",context)



#Chat
def open_chat(request, mem_id):
    context = {
    'mem_id': mem_id,
    }
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request,"chat/chat.html",context)




#home page
def home_page_log(request,mem_id):
    context = {
        'mem_id': mem_id,
    }
    return render(request,"home/index.html",context)


def home_page(request):
    return render(request,"home/index.html")


