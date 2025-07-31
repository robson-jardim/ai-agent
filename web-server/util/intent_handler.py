from gpt_service import ask_gpt

def detect_intent(user_input: str) -> str:
    user_input = user_input.lower()
    if "workout" in user_input:
        return "generate_workout"
    elif "motivate" in user_input or "tired" in user_input:
        return "motivation"
    elif "track" in user_input or "progress" in user_input:
        return "track_progress"
    else:
        return "general_chat"

def handle_intent(intent: str, user_input: str) -> str:
    if intent == "generate_workout":
        return ask_gpt(f"Create a workout plan: {user_input}")
    elif intent == "motivation":
        return ask_gpt(f"Give motivation to: {user_input}")
    elif intent == "track_progress":
        return ask_gpt(f"Help track progress for: {user_input}")
    else:
        return ask_gpt(user_input)
