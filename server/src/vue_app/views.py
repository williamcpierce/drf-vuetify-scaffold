from django.shortcuts import render
from django.views import View


class Index(View):
    @staticmethod
    def get(request):
        return render(request, "vue_index.html")
