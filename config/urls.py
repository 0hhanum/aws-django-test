from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("favs/", include("favs.urls", namespace="favs")),
    path("movies/", include("movies.urls", namespace="movies")),
    path("books/", include("books.urls", namespace="books")),
    path("genres/", include("categories.urls", namespace="genres")),
    path("people/", include("people.urls", namespace="people")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
]


# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
