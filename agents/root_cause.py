from utils.llm import ask_llm


def root_cause(log_text):

    prompt = f"""
    Find the exact root cause.

    Explain in simple language.

    Log:
    {log_text}
    """

    return ask_llm(prompt)
