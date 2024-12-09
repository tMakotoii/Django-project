import debug_toolbar

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from news import views

urlpatterns = [
    path("", views.index_handler, name='homepage'),

    path("blog/", views.blog_handler, name='blog'),
    path("blog/page/<number>/", views.blog_handler, name='blog_pager'),

    path("category/<cat_slug>", views.blog_handler, name='category'),
    path("category/<cat_slug>/page/<number>/", views.blog_handler, name='category_pager'),

    path("post/<post_slug>", views.page_handler, name='article'),

    path("about/", views.about_handler, name='about'),
    path("contact/", views.contact_handler, name='contact'),

    path("robots.txt", views.robots_handler),

    path('summernote/', include('django_summernote.urls')),

    path("admin/", admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)


if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)