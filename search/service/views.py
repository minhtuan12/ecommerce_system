from rest_framework.decorators import api_view

from constants import MODEL
from helpers import call_api, response_error
from search.decorators import verify_token, check_permission


# Create your views here.


@verify_token
@api_view(['GET'])
def search_by_key(request):
    q = request.GET.get("q")
    model_type = request.GET.get("model_type")
    params = {'q': q}

    match model_type:
        case 0:
            return call_api(request, "", params)
        case 1:
            return call_api(request, "", params)
        case 2:
            return call_api(request, "", params)
        case _:
            return response_error("Model type must be 0, 1 or 2 respectively represent for Book, Clothes, Mobile")


@verify_token
@api_view(['GET'])
def search_by_voice(request):
    return


@verify_token
@check_permission
@api_view(['GET'])
def admin_search_book_by_key(request):
    return
