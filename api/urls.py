from django.urls import path, include
from . import views
from rest_framework.routers import  DefaultRouter

# For viewSet you use routers
router = DefaultRouter()
router.register("asserts", views.AssertsViewset, basename="asserts")


urlpatterns = [
    path("students/", views.studentsView),
    path("students/<int:pk>/", views.studentDetailView),
    path("employees/", views.Employees.as_view()),
    path("employees/<int:pk>/", views.EmployeeDetail.as_view()),
    path("products/", views.Products.as_view()),
    path("products/<int:pk>/", views.ProductDetail.as_view()),
    # path("asserts/", views.Asserts.as_view()),
    # path("asserts/<int:pk>/", views.AssertDetail.as_view()),
    path("", include(router.urls)),
    path("comments/", views.CommentsView.as_view()),
    path("comments/<int:pk>/",views.CommentDetail.as_view()),
    path("blogs/", views.BlogsView.as_view()),
    path("blogs/<int:pk>/", views.BlogDetail.as_view()),
]