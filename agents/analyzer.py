from utils.llm import ask_llm


def analyze_log(log_text):

    prompt = f"""
    You are a DevOps expert.

    Analyze the following CI/CD log.

    Return:
    - Error Summary
    - Severity
    - Affected Component

    Log:
    {log_text}
    """

    return ask_llm(prompt)
