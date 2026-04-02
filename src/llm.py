import json
from openai import OpenAI
from src.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def mock_response(system_prompt: str) -> dict:
    prompt_lower = system_prompt.lower()

    if "product messaging strategist" in prompt_lower or "target_audience" in prompt_lower:
        return {
            "target_audience": "Young adults seeking low-pressure emotional support late at night",
            "pain_points": [
                "loneliness at night",
                "anxiety when support is hard to access",
                "hesitation to seek formal help"
            ],
            "key_message": "A calm, multilingual AI companion for late-night emotional support and reflection",
            "trust_angles": [
                "clear non-therapy positioning",
                "empathetic tone",
                "privacy-aware messaging"
            ]
        }

    if "content generation agent" in prompt_lower:
        return {
            "landing_page_copy": "CalmLoop is a multilingual AI companion designed for late-night moments when emotional support feels hardest to access.",
            "linkedin_post": "CalmLoop explores how AI can provide low-pressure emotional support and guided reflection in a multilingual, approachable format.",
            "x_post": "Late-night anxiety can feel isolating. CalmLoop offers multilingual AI support and reflection in a calm, low-pressure space.",
            "faq_snippet": "No. CalmLoop is designed as a supportive companion, not a replacement for professional mental health care."
        }

    if "critic agent" in prompt_lower:
        return {
            "clarity_score": 4,
            "trustworthiness_score": 4,
            "specificity_score": 3,
            "empathy_score": 5,
            "platform_fit_score": 4,
            "spamminess_score": 5,
            "strengths": [
                "clear tone",
                "empathetic framing",
                "good trust positioning"
            ],
            "weaknesses": [
                "could be more specific about user scenarios",
                "value proposition can be sharper"
            ],
            "revision_instructions": [
                "add more specific context",
                "strengthen value proposition",
                "keep calm and trustworthy tone"
            ]
        }

    if "refiner agent" in prompt_lower:
        return {
            "landing_page_copy": "CalmLoop is a multilingual AI companion built for moments when emotional support feels hardest to access, especially late at night. It offers gentle conversation and guided reflection in a calm, low-pressure space.",
            "linkedin_post": "Emotional support is often hardest to access in the exact moments people need it most. CalmLoop is designed for late-night loneliness and anxiety, offering multilingual, low-pressure support and reflection.",
            "x_post": "Late-night anxiety can feel isolating. CalmLoop is a multilingual AI companion designed for calm, low-pressure support and reflection.",
            "faq_snippet": "No. CalmLoop provides supportive conversation and reflection, but it does not replace licensed mental health care or crisis services."
        }

    if "platform adaptation agent" in prompt_lower:
        return {
            "website_version": "CalmLoop is a multilingual AI companion for moments when emotional support feels hardest to access.",
            "blog_intro": "What happens when emotional support is hardest to access in the moments people need it most? CalmLoop explores a low-pressure, multilingual AI approach.",
            "linkedin_version": "CalmLoop is designed to offer multilingual, low-pressure emotional support and reflection in moments of loneliness or anxiety.",
            "x_version": "CalmLoop offers multilingual AI support and reflection for late-night loneliness and anxiety."
        }

    return {"raw_text": "Mock response not found."}

def call_llm(system_prompt: str, user_prompt: str) -> str:
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.output_text

def call_llm_json(system_prompt: str, user_prompt: str) -> dict:
    try:
        text = call_llm(system_prompt, user_prompt)
        return json.loads(text)
    except Exception:
        return mock_response(system_prompt)