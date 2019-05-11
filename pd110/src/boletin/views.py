# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo = "HOLA"
	abc = "123"
	if request.user.is_authenticated():
		tirulo = "Bienvenido %s" %(request.user)
	form = RegForm(request.POST or None)
#	print (dir(form))
	if form.is_valid():
		form_data = form.cleaned_data
		abc =  form_data.get("email")
		abc2 =  form_data.get("nombre")
		obj = Registrado.objects.create(email=abc, nombre=abc2)

#		obj = Registrado()
#		obj.email = abc
#		obj.save()

	context = {
		"titulo": titulo,
		"abc": abc,
		"el_form": form,
	}
	return render(request, "inicio.html", context)