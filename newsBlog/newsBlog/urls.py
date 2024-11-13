import debug_toolbar

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from polls.views import index, detail
from news import views

urlpatterns = [
    path("", index),
    path("polls/<int:question_id>/", detail),

    path("blog/", views.blog_handler),
    path("about/", views.about_handler),
    path("page/", views.page_handler),
    path("contact/", views.contact_handler),
    path("index/", views.index_handler),

    path("robots.txt", views.robots_handler),

    path("admin/", admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns