from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Django is running on Vercel!"})
