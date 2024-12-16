from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Permission

def home_view(request):
    return render(request, 'reserva/home.html')

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Adicionando permissões personalizadas relacionadas ao modelo Reserva
            permissions = Permission.objects.filter(codename__in=[
                'can_add_reserva',
                'can_delete_reserva',
                'can_change_reserva',
                'can_view_reserva'
            ])
            
            # Adicionando as permissões ao usuário
            if permissions.exists():
                user.user_permissions.add(*permissions)

            login(request, user)
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'reserva/registro.html', {'form': form})


def login_view(request):
    return render(request, 'reserva/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')