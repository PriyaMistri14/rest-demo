from django.urls import path, include

from . import views
urlpatterns = [
    path('demo/', views.demo_list),
    path('demo/<int:pk>/', views.demo_list),
    path('demo_class/',views.DemoList.as_view()),
    path('demo_class/<int:pk>/',views.DemoDetail.as_view()),
    path('demo_class_mixin/',views.DemoListMixin.as_view()),
    path('demo_class_mixin_detail/',views.DemoDetailMixin.as_view()),
    path('demo_class_generic/',views.DemoListGeneric.as_view(), name= "demo_list"),
    path('demo_class_generic_detail/<int:pk>/',views.DemoDetailGeneric.as_view(),name='demo_detail'),
    path('users/',views.UserList.as_view(),name="user_list"),
    path('users/<int:pk>/',views.UserDetail.as_view(), name="user_detail"),
    path('api-auth/',include('rest_framework.urls')),
    path('',views.api_root),
    path('demo_class_generic/<int:pk>/highlight/', views.DemoHighlight.as_view(),name='demo_highlight'),


]


demo_list=views.DemoViewSet.as_view({
    'get':'list',
    'post':'create'
})

demo_detail=views.DemoViewSet.as_view({
    'get':'retrieve',
    'patch' : 'partial_update',
    'put':'update',
    'delete':'destroy'

})



demo_highlight=views.DemoViewSet.as_view({
    'get':'highlight'
})




user_list = views.UserViewSet.as_view({
    'get':'list'
})

user_detail= views.UserViewSet.as_view({
    'get':'retrieve'
})





