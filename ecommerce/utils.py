from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import exception_handler, set_rollback
from rest_framework import status

def custom_exception_handler(exc, context):
    # # give more context on the error since DRF masks it as Not Found
    # if isinstance(exc, Http404):
    #     set_rollback()
    #     return Response(str(exc))

    # # Call REST framework's default exception handler after specific 404 handling,
    # # to get the standard error response.
    # response = exception_handler(exc, context)

    # # No response means DRF couldn't handle it
    # # Output a generic 500 in a JSON format
    # if response is None:
    #     set_rollback()
    #     return Response({'detail': 'Erro de Integridade'}, status=status.HTTP_403_FORBIDDEN)

    return "response"
    