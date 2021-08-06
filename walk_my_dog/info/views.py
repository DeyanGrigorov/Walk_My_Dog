from django.views.generic import TemplateView


class HowItWorksView(TemplateView):
    template_name = 'info/how_it_works.html'
