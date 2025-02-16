from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        # Se o formulário não for válido, renderize o formulário novamente com os erros
        return render(request, 'register.html', {'user_form': user_form})
    else:
        user_form = UserCreationForm()
        return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_posts')
        else:
            # Se o login falhar, renderize o formulário com uma mensagem de erro
            login_form = AuthenticationForm()
            return render(request, 'login.html', {'login_form': login_form, 'error': 'Usuário ou senha inválidos'})
    else:
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('lista_posts')