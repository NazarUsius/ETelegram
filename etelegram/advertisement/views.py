from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Advertisement
from .forms import AddCreate, ApproveAddCreate
from django.urls import reverse_lazy

class AddListView(ListView):
    model = Advertisement
    template_name = "advertisement/advertisement_list.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["approved_advertisements"] = Advertisement.objects.filter(status="Approved")
        return context

class AddCreateView(CreateView):
    model = Advertisement
    template_name = "advertisement/advertisement_create.html"
    form_class = AddCreate
    success_url = reverse_lazy('add_list')

    def form_valid(self, form):
        form.instance.status = "In queue"
        return super().form_valid(form)

class ApproveListView(ListView):
    model = Advertisement
    template_name = "advertisement/in_queue_advertisement_list.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["approved_advertisements"] = Advertisement.objects.filter(status="In queue")
        return context

class ApproveUpdateView(UpdateView):
    model = Advertisement
    template_name = "advertisement/advertisement_create.html"
    form_class = ApproveAddCreate
    success_url = reverse_lazy('approve_list')

    def form_valid(self, form):
        advertisement = Advertisement.objects.get(pk=self.kwargs['pk'])
        form.instance.title = advertisement.title
        form.instance.media = advertisement.media
        form.instance.description = advertisement.description
        form.instance.status = "Approved"
        return super().form_valid(form)
