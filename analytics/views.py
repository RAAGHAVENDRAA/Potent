from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PageView

@csrf_exempt
def track_profile_view(request):
    print("Method:", request.method)

    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    obj, _ = PageView.objects.get_or_create(page_name="profile")

    if request.method == "POST":
        obj.count += 1
        obj.save()

    return JsonResponse({"count": obj.count})
