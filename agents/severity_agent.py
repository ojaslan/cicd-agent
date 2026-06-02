from utils.llm import ask_llm

def classify_severity(log_text):

    prompt = f"""
    You are a DevOps incident classifier.

    Classify the severity of this error.

    Return ONLY one:
    Critical
    High
    Medium
    Low

    Log:
    {log_text}
    """

    return ask_llm(prompt)