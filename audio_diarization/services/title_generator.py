import google.generativeai as genai
from django.conf import settings

# Configuring the Gemini API key
genai.configure(api_key=settings.API_KEY)


def generate_blog_titles(content: str, num_titles: int = 3) -> list:
    """
    Generates multiple creative, short, SEO-friendly blog titles using the Gemini Pro model.

    Args:
        content (str): Blog content for which the titles need to be generated.
        num_titles (int): Number of title suggestions to generate. Default is 3.

    Returns:
        list: List of generated blog titles.
    """
    if not content.strip():
        raise ValueError("Content cannot be empty.")

    input_prompt = (
        f"Generate {num_titles} creative, short, SEO-friendly blog titles and one concise summary "
    f"for the following content:\n\n{content}\n\nTitles and Summary:"
    )

    try:
        # Using Gemini Pro to generate titles
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(input_prompt)

        # Splitting the response text into separate titles
        titles = [title.strip() for title in response.text.split("\n") if title.strip()]
        return titles[:num_titles]
    except Exception as e:
        raise RuntimeError(f"Error generating blog titles: {str(e)}")
