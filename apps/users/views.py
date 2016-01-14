from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse, HttpResponse, Http404


def Logout(request):
    logout(request)
    return redirect('/')


def loginAjax(request):

    if request.is_ajax():

        username_ajax = request.POST['username']
        password_ajax = request.POST['password']

        user = authenticate(username = username_ajax,
            password = password_ajax)
        if user is not None and user.is_active:
            login(request, user)
            response = JsonResponse({'status_login': 'success'})
        else:
            response = JsonResponse({'status_login': 'error'})
        return HttpResponse(response.content)
    else:
        raise Http404
