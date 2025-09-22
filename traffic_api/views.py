# traffic_api/views.py

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TrafficData

@csrf_exempt
def receive_data(request):
    """
    API endpoint to receive traffic data from the Python script.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            current_density = data.get('current_density', 0)
            accident_detected = data.get('is_accident', False)

            # Create a new record in the database
            TrafficData.objects.create(
                current_density=current_density,
                accident_detected=accident_detected
            )
            return JsonResponse({"status": "success", "message": "Data received and saved."}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Only POST requests are allowed"}, status=405)


def get_analysis_data(request):
    """
    API endpoint to send traffic data to the frontend for analysis.
    """
    if request.method == 'GET':
        try:
            # Fetch the latest 50 records from the database
            latest_data = TrafficData.objects.all().order_by('-timestamp')[:50]
            data_list = []
            for record in latest_data:
                data_list.append({
                    "timestamp": record.timestamp.isoformat(),
                    "current_density": record.current_density,
                    "accident_detected": record.accident_detected
                })
            return JsonResponse({"data": data_list}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Only GET requests are allowed"}, status=405)