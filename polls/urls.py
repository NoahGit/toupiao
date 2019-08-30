from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('ulogin/', views.ulogin, name='ulogin'),        # 血的教训---'ulogin/'前面绝对不能有/,绝对不能写成'/ulogin/'
    path('user_login/', views.user_login, name='user_login')


    # ex: /pools/
    # path('', views.index, name='index'),
    # ex: /pools/5/
    # 问题详情页——展示某个投票的问题和不带结果的选项列表。
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # 问题结果页——展示某个投票的结果。
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # 投票处理器——用于响应用户为某个问题的特定选项投票的操作。
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # path有四个参数
    # （route匹配url的准则，类似正则表达式，例如www.b.com/myApp/?page=3中，只会匹配myApp/
    # view当找到了匹配的准则，就会调用这个特定的视图函数，并传入一个HttpResponse对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。
    # kwargs任意一个关键字参数可以作为一个字典传递给目标视图函数。
    # name为你的url取名能使你在Django的任意地方唯一的引用它，尤其是在模版中。这个特性允许你只改一个文件就能全局地修改某个url模式。）
]
