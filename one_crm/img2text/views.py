from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CardForm


class CardFormView(FormView):
    template_name = "img2text/card_form.html"
    form_class = CardForm

    def form_valid(self, form):
        self.pk = form.parse_card()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("leads:lead-update", kwargs={"pk": self.pk})


card_form_view = CardFormView.as_view()
