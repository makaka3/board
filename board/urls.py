
from django.contrib import admin
from django.urls import path, include
from bboar.views import view_rubric, view_create_product, view_index, view_product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name='index'),
    path('user/', include('users.urls', namespace='users')),
    path('<int:rubric_id>/', view_rubric, name='rubric'),
    path('create_product/', view_create_product, name='create_product'),
    path("product/<int:product_id>/",view_product,name="product")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
