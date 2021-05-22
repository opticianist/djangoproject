
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class AnasayfaSayfaGorunumu(TemplateView):
   template_name = "anasayfa.html"

class HakkimdaSayfaGorunumu(TemplateView):
    template_name="hakkimda.html"

class IletisimSayfaGorunumu(TemplateView):
    template_name="iletisim.html"
