from django.urls import path
from django.contrib.auth.views import LogoutView
from main_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin-fabrim/principal/',
         views.PrincipalTemplateView.as_view(), name='principal'),

    path('admin-fabrim/medicamentos/',
         views.MedicamentosView.as_view(), name='medicamentos'),
    path('admin-fabrim/medicamentos/delete/<int:pk>/',
         views.MedicamentoDeleteView.as_view(), name='delete_medicamento'),



    path('admin-fabrim/tipos-medicamentos/',
         views.TiposMedicamentosView.as_view(), name='tipos-medicamentos'),
    path('admin-fabrim/tarjetas-estiba/',
         views.TarjetasEstibaView.as_view(), name='tarjetas-estiba'),
    path('admin-fabrim/usuarios/',
         views.UsuariosView.as_view(), name='usuarios'),
    path('admin-fabrim/compras/',
         views.ComprasView.as_view(), name='compras'),
    path('admin-fabrim/pedidos/',
         views.PedidosView.as_view(), name='pedidos'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
