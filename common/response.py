from rest_framework import status
from rest_framework.response import Response


def api_response(
        *,
        data=None,
        message="Success",
        success=True,
        status_code=status.HTTP_200_OK,
        errors=None,
        meta=None,
):
    payload = {
        "success": success,
        "message": message,
        "data": data
    }

    if meta is not None:
        payload["meta"] = meta

    if errors is not None:
        payload["errors"] = errors

    return Response(payload, status=status_code)
