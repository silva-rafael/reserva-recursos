from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Permission
from .forms import ReservaForm
from .models import Reserva


def home_view(request):
    user=request.user
    reservas = Reserva.objects.filter(usuario=user)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados diretamente no banco
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('home')
    else:
        form = ReservaForm()

    return render(request, 'reserva/home.html', {
        'form': form,
        'user': user,
        'reservas': reservas,
    })



#------------------------------------------------------------------------


# def reserva_view(request):
#     if request.method == 'POST':
#         form = ReservaForm(request.POST)
#         if form.is_valid():
#             form.save()  # Salva os dados diretamente no banco
#             return redirect('success')
#     else:
#         form = ReservaForm()

#     return render(request, 'create_book.html', {'form': form})

#------------------------------------------------------------------------


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



#------------------------------------------------------------------------

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'reserva/login.html', {'form':form})


#------------------------------------------------------------------------


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')