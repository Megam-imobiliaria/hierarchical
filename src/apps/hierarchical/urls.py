from django.urls import path, register_converter

from .converters import SectionConverter
from .views import SectionListView, create, delete, update

register_converter(SectionConverter, 'section')

urlpatterns = [
    path('', SectionListView.as_view(), name='root'),
    path('section/<section:relative>/', SectionListView.as_view(), name='section'),
    path('create/', create, name='create'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
]
