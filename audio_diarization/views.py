import asyncio
import json

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services.audio_transcription import transcribe_audio
from .services.title_generator import generate_blog_titles


@csrf_exempt
def transcription_view(request):
    """
    View to handle audio transcription requests with speaker diarization.
    """
    if request.method == "POST":
        if 'audio_file' not in request.FILES:
            return JsonResponse({"error": "No audio file uploaded."}, status=400)

        # Saving uploaded audio file to a temporary location
        audio_file = request.FILES['audio_file']
        file_path = default_storage.save(audio_file.name, audio_file)
        file_path = default_storage.path(file_path)

        try:
            # Calling the transcription service asynchronously
            transcription_response = asyncio.run(transcribe_audio(file_path))
            if "error" in transcription_response:
                return JsonResponse({"error": transcription_response["error"]}, status=500)

            return JsonResponse(transcription_response, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            default_storage.delete(file_path)

    return JsonResponse(
        {"message": "Send a POST request with an audio file."},
        status=400
    )


@csrf_exempt
def title_suggestions(request):
    """
    API endpoint to generate blog title suggestions.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            content = body.get("content", "").strip()

            if not content:
                return JsonResponse({"error": "Blog content is required."}, status=400)

            # Generating title suggestions (default 3)
            titles = generate_blog_titles(content, num_titles=3)
            return JsonResponse({"titles": titles})

        except ValueError as ve:
            return JsonResponse({"error": str(ve)}, status=400)
        except RuntimeError as re:
            return JsonResponse({"error": str(re)}, status=500)
        except Exception as e:
            return JsonResponse(
                {"error": f"Unexpected error: {str(e)}"},
                status=500
            )

    return JsonResponse(
        {"error": "Only POST requests are allowed."},
        status=405
    )
