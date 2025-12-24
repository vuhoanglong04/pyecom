from django.http import HttpResponse


def health_check(request):
    try:
        from django.db import connection
        connection.ensure_connection()
        html = '<body style="background-color:green"></body>'
        return HttpResponse(html, status=200)
    except Exception:
        html = '<body style="background-color:red"></body>'
        return HttpResponse(html, status=500)