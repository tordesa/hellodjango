from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.


class HomepageView(TemplateView):
    template_name = "index.html"

    def good_bye(self):
        return 'Goodbye'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_statement'] = 'Nice to see you!'
        return context

    