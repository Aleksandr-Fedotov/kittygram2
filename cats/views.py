from rest_framework import viewsets

from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    # отправляем авторизованного пользователя в хозяева кота
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    # При подобных операциях с PUT- и PATCH-запросами
    # следует переопределить метод perform_update(),
    # а в остальном всё работает так же.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
