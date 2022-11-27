from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
    """Manager para usuarios"""

    def create_user(self, email, name, apellidos,  ci, tfno, password=None, **extra_fields):
        """Crea un nuevo Usuario"""
        if not email:
            raise ValueError("El usuario debe tener un email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          apellidos=apellidos, ci=ci, tfno=tfno, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, apellidos,  ci, tfno, password=None, **extra_fields):
        user = self.create_user(email, name, apellidos, ci, tfno,
                                password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Modelo BD para Users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    ci = models.CharField(max_length=11, unique=True, null=False, blank=False)
    tfno = models.CharField(max_length=50)
    apto = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'apellidos', 'ci', 'tfno']

    def get_full_name(self):
        return "%s %s" % (self.name, self.apellidos)

    def get_short_name(self):
        return self.name

    def __str__(self):
        """Return String"""
        return self.email


class TipoMedicamento(models.Model):
    nombre = models.CharField(
        max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        """Return String"""
        return self.nombre


class TarjetaEstiba(models.Model):
    no_serie = models.CharField(
        max_length=255, unique=True, null=False, blank=False)
    precio = models.IntegerField(blank=False, null=False)
    cant_medi = models.IntegerField(blank=False, null=False)
    fecha_creacion = models.DateField(blank=False, null=False, auto_now=True)

    class Meta:
        ordering = ['no_serie', 'fecha_creacion']

    def __str__(self):
        return "%s %s %s %s" % (self.no_serie, self.precio, self.cant_medi, self.fecha_creacion)


class Medicamento(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    no_lote = models.CharField(
        max_length=255, unique=True, null=False, blank=False)
    fecha_cad = models.DateField(blank=False, null=False, default=(
        timezone.now() + timedelta(days=1825)))
    tarjeta_estiba_id = models.OneToOneField(
        TarjetaEstiba, on_delete=models.CASCADE, primary_key=True)
    tipo_medicamento_id = models.ForeignKey(
        TipoMedicamento, on_delete=models.CASCADE)

    class Meta:
        ordering = ['fecha_cad', 'no_lote', 'nombre']

    def __str__(self):
        return "%s - %s - %s" % (self.nombre, self.no_lote, self.fecha_cad)


class Pedido(models.Model):
    cantidad_medicamento = models.IntegerField(blank=False, null=False)
    fecha = models.DateField(blank=False, null=False, auto_now=True)
    medicamentos = models.ManyToManyField(Medicamento)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return "%s %s" % (self.cantidad_medicamento, self.fecha)


class Compra(models.Model):
    fecha = models.DateField(blank=False, null=False, auto_now=True)
    tarjeta_bancaria = models.CharField(
        max_length=255, null=False, blank=False)
    total_pagado = models.IntegerField(blank=False, null=False)
    medicamentos = models.ManyToManyField(Medicamento)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
