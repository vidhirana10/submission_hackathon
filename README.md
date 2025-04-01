# AI-Powered Call Summary Generation with Key Points and Suggested Titles

## Overview
This Django-based application automates the generation of structured summaries from audio recordings of conversations or meetings. It utilizes AI-powered transcription with speaker diarization to identify different speakers, summarize the key discussion points, and generate three suggested titles to facilitate summary archiving.

## Features
- **Audio-to-Summary Conversion:**
  - Accepts an audio recording of a meeting or call as input.
  - Transcribes the audio and distinguishes between speakers.
  - Summarizes the key discussion points automatically.
- **Title Suggestions:**
  - Generates three AI-powered summary titles encapsulating the meeting's essence.

## Project Structure
```
SUBMISSION_HACKATHON/
│── audio_diarization/
│   ├── __pycache__/
│   ├── migrations/
│   ├── services/
│   │   ├── audio_transcription.py
│   │   ├── title_generator.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── views.py
│── audiotize/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django
- Required dependencies in `requirements.txt`

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd SUBMISSION_HACKATHON
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the Django server:
   ```sh
   python manage.py runserver
   ```

## API Usage
### Endpoint: Generate Summary
- **URL:** `POST /api/generate-summary/`
- **Input:** Audio file
- **Output:** JSON response containing:
  ```json
  {
      "summary": "Key points from the discussion...",
      "suggested_titles": [
          "Title 1",
          "Title 2",
          "Title 3"
      ],
      "full_transcription": "Full transcript with speaker diarization."
  }
  ```

### Sample API Call
Use `curl` to test the API:
```sh
curl -X POST "http://localhost:8000/api/generate-summary/" \
     -H "Content-Type: multipart/form-data" \
     -F "audio_file=@/path/to/audio.mp3"
```

## Contributing
Contributions are welcome! Feel free to open issues and submit pull requests.

## License
This project is licensed under the MIT License.
