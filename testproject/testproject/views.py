from django.views.generic import TemplateView
from django.shortcuts import render
from testproject.forms import IndexForm
offset=0

class index_view(TemplateView):
    template_name = "index.html"

    def get(self, request):
        form = IndexForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            global offset
            offset= form.cleaned_data['offset']


            print(offset)
            args = {'form': form, 'offset':offset}
            return render(request, self.template_name, args)


