from django.views.generic.base import TemplateView


class AppViewIdx(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = "Index"
        return context


class AppViewPage01(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = "Page01"
        return context