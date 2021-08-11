from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from car_app.newsletters.forms import NewsLetterModelForm

# Create your views here.


class NewNewsLetterView(FormView):
    template_name = 'newsletters/subscribe.html'
    form_class = NewsLetterModelForm
    success_url = reverse_lazy('newsletters:success')

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)


class SuccessTemplateView(TemplateView):
    template_name = 'newsletters/success.html'
