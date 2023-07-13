# para que se conecte con el front


from django.urls import path , include
from .views import      EmpanadaListView\
                    ,   EmpanadaCreateView\
                    ,   EmpanadaUpdateView\
                    ,   EmpanadaDetailView\
                    ,   EmpanadaDeleteView
from .router import router

app_name = "empanadas"

urlpatterns = [
    path('', EmpanadaListView.as_view(), name = "all"),
    path('create/', EmpanadaCreateView.as_view(), name = "create"),
    path('<int:pk>/detail/', EmpanadaDetailView.as_view(), name = "detail"),  ## indicar la primary key  -- en este caso es el ID
    path('<int:pk>/update/', EmpanadaUpdateView.as_view(), name = "update"),
    path('<int:pk>/delete/', EmpanadaDeleteView.as_view(), name = "delete")
]


urlpatterns += router.urls