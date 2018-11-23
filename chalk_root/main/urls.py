from django.urls import path

from chalk_root.main.views import *

app_name = "main"
urlpatterns = [
    path("", HomePageView.as_view(), name='HomePageView'),
    path("school/<school_id>", SchoolView.as_view(), name='SchoolView'),
    path("add/school/", SchoolCreateView.as_view(), name='create_school'),
    path("list/", search_view, name='SchoolListView'),
    path("compare/", CompareSchoolView.as_view(), name='compare'),
]
