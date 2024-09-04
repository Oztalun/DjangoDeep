from django.urls import path
from . import views


app_name = "articles"
urlpatterns = [
    # article
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
    # article comment
    path("<int:article_pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("comments/<int:comment_pk>/", views.CommentDetailAPIView.as_view(), name="comment_list"),
    path("check-sql-LazyLoading/", views.check_sql_LazyLoading, name="check_sql"),
    path("check-sql-select_related/", views.check_sql_select_related, name="check_sql"),
    path("check-sql-prefetch_related/", views.check_sql_prefetch_related, name="check_sql"),
    # 
    path("html/", views.article_list_html, name="article_list_html"),
    path("json-01/", views.json_01, name="json_01"),
    path("json-02/", views.json_02, name="json_02"),
    path("json-drf/", views.json_drf, name="json_drf"),
]
