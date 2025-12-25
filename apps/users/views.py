from django.http import HttpResponse
from rest_framework import viewsets, status

from apps.users.models import User
from apps.users.serializers import UserSerializer
from common.pagination import CustomPagination
from common.response import api_response


def health_check(request):
    try:
        from django.db import connection
        connection.ensure_connection()
        html = '<body style="background-color:green"></body>'
        return HttpResponse(html, status=200)
    except Exception:
        html = '<body style="background-color:red"></body>'
        return HttpResponse(html, status=500)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request, view=self)

        serializer = self.get_serializer(page, many=True)

        return api_response(
            data=serializer.data,
            message="User list fetched successfully",
            meta=paginator.get_meta(),
        )

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)

        return api_response(
            data=serializer.data,
            message="User detail fetched successfully",
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            data=serializer.data,
            message="User created successfully",
            status_code=status.HTTP_201_CREATED,
        )
