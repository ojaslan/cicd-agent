from utils.llm import ask_llm


def generate_fix(log_text):

    prompt = f"""
    Suggest exact commands and code fixes.

    Log:
    {log_text}
    """

    return ask_llm(prompt)
