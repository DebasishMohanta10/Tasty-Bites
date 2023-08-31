from django.urls import path,include
from . import views

urlpatterns = [
    # User Registration and authentication
    path("",include("djoser.urls")),
    path("",include("djoser.urls.authtoken")),
    path("",include("djoser.urls.jwt")),
    # Category End Points
    path("categories/",views.CategoryListViews.as_view(),name="category-list"),
    path("categories/<slug:slug>",views.CategoryDetailsView.as_view(),name="category-details"),
    # MenuItems End Point
    path("menu-items/",views.MenuItemListView.as_view(),name="menuitems-list"),
    path("menu-items/<slug:slug>",views.MenuItemsDetailsView.as_view(),name="menuitems-details"),
    # User Group Management Endpoints
    path("groups/manager/users/",views.AddManger.as_view({
        "get": "list",
        "post": "create"
    })),
    path("groups/manager/users/<str:username>",views.RemoveManager.as_view({
        "delete": "destroy"
    }))
]

