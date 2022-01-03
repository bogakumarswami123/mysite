from rest_framework import status
from rest_framework.generics import (GenericAPIView)
from rest_framework.response import Response
from user.utils import ResponseInfo
import requests

class  GetArticlesAPIView(GenericAPIView):
    """
    Class for creating API view for getting the Requests for particular status .
    """
    authentication_classes = ()
    permission_classes = ()

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(GetArticlesAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        Function for getting the requests for particular status if valid.
        """
        url = "https://newsapi.org/v2/everything?q={0}&from={1}&sortBy=publishedAt&apiKey=880b677eef3e45029b2893df000373db"
        url = url.format(request.data.get("search"), request.data.get("date"))
        print(url)
        try:
            data = requests.get(url, params=request.GET)
        except requests.exceptions.RequestException:
            return "Could not grab api text."
        data = data.json()
        try:
            self.response_format["status_code"] = status.HTTP_200_OK
            self.response_format["error"] = None
            self.response_format['data'] = data
            return Response(self.response_format, status.HTTP_200_OK)

        except Exception as e:
            print(e)
            self.response_format["status_code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format["message"] = "Something went wrong, please try again"
            return Response(self.response_format, status.HTTP_500_INTERNAL_SERVER_ERROR)





