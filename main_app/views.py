from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
import main_app.forms as _forms
import main_app.models as _models


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="login")
    else:
        return HttpResponseRedirect(redirect_to="principal")


class LoginFormView(LoginView):
    form_class = _forms.LoginForm
    template_name = "sign-in/login.html"
    success_url = reverse_lazy('principal')


class RegisterView(CreateView, SuccessMessageMixin):
    model = _models.User
    template_name = "sign-in/register.html"
    form_class = _forms.RegisterForm
    success_url = reverse_lazy('login')
    success_message = "Usuario registrado"


class PrincipalTemplateView(LoginRequiredMixin, TemplateView, PermissionRequiredMixin):
    template_name = "administrador_index.html"
    permission_required = 'main_app.view_user'


"""---------------------------------------------------------------
-----------------------------MEDICAMENTOS VIEW ------------------------
---------------------------------------------------------------"""


class MedicamentosView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    template_name = 'pages/admin_views/medicamentos.html'
    model = _models.Medicamento
    permission_required = "main_app.view_medicamento"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medicamentos'
        return context


class MedicamentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = _models.Medicamento
    template_name = 'pages/admin_views/medicamentos.html'
    success_url = reverse_lazy('medicamentos')
    success_message = "El medicamento ha sido eliminado"
    permission_required = 'main_app.delete_medicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar medicamento'
        return context


"""---------------------------------------------------------------
-----------------------------COMPRAS VIEW ------------------------
---------------------------------------------------------------"""


class ComprasView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    template_name = 'pages/admin_views/compras.html'
    permission_required = "main_app.view_compra"
    model = _models.Compra

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Compras'
        return context


"""---------------------------------------------------------------
-----------------------------TARJETA ESTIBA VIEW ------------------------
---------------------------------------------------------------"""


class TarjetasEstibaView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    template_name = 'pages/admin_views/tarjeta_estiba.html'
    permission_required = "main_app.view_tarjeta_estiba"
    model = _models.TarjetaEstiba

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tarjetas de Estiba'
        return context


"""---------------------------------------------------------------
-----------------------------TIPOS MEDICAMENTOS VIEW ------------------------
---------------------------------------------------------------"""


class TiposMedicamentosView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    template_name = 'pages/admin_views/tipo_medicamento.html'
    permission_required = "main_app.view_tipo_medicamento"
    model = _models.TipoMedicamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Medicamentos'
        return context


"""---------------------------------------------------------------
-----------------------------PEDIDOS VIEW ------------------------
---------------------------------------------------------------"""


class PedidosView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    template_name = 'pages/admin_views/pedidos.html'
    permission_required = "main_app.view_pedido"
    model = _models.Pedido

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pedidos'
        return context


"""---------------------------------------------------------------
-----------------------------USUARIOS VIEW ------------------------
---------------------------------------------------------------"""


class UsuariosView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    template_name = 'pages/admin_views/usuarios.html'
    permission_required = "main_app.view_user"
    model = _models.User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        return context
