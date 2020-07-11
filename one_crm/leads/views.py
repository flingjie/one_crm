from django.urls import reverse_lazy

from .models import Lead

from django.views.generic import (  # isort:skip
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)


class LeadCreateView(CreateView):
    """
        新建视图
    """

    model = Lead
    fields = ["name", "title", "contact", "email", "description", "attachment"]


lead_create_view = LeadCreateView.as_view()


class LeadUpdateView(UpdateView):
    """
        更新视图
    """

    model = Lead
    fields = ["name", "title", "contact", "email", "description", "attachment"]


lead_update_view = LeadUpdateView.as_view()


class LeadDeleteView(DeleteView):
    """
        删除视图
    """

    model = Lead

    success_url = reverse_lazy("leads:lead-list")


lead_delete_view = LeadDeleteView.as_view()


class LeadListView(ListView):
    """
        线索列表视图
    """

    model = Lead


lead_list_view = LeadListView.as_view()


class LeadDetailView(DetailView):
    """
        线索详情视图
    """

    model = Lead


lead_detail_view = LeadDetailView.as_view()
