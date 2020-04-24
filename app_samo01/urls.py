from django.urls import path
from .views import AppViewIdx, AppViewPage01

app_name = 'app_name_01'

urlpatterns = [
    path('ns_idx/',
         AppViewIdx.as_view(template_name='app_samp01/index.html'),
         name='name_idx'),
    path('ns_pg01/',
         AppViewPage01.as_view(template_name='app_samp01/page01.html'),
         name='name_pg01'),
]