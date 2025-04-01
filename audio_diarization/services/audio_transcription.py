from deepgram import Deepgram
from django.conf import settings


async def transcribe_audio(file_path: str) -> dict:
    """
    Transcribes an audio file using the Deepgram API.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        dict: Transcription response or error message.
    """
    dg_client = Deepgram(settings.DEEPGRAM_API_KEY)

    try:
        with open(file_path, "rb") as audio:
            source = {"buffer": audio, "mimetype": "audio/wav"}
            options = {"punctuate": True}
            response = await dg_client.transcription.prerecorded(source, options)
            return response
    except Exception as e:
        return {"error": str(e)}
