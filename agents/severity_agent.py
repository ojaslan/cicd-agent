from utils.llm import ask_llm

def severity_agent(log_text):

    prompt = f"""
    You are a Site Reliability Engineer.

    Classify the incident severity.

    Levels:
    SEV-1 Critical
    SEV-2 High
    SEV-3 Medium
    SEV-4 Low
    SEV-5 Informational

    Log:
    {log_text}
    """

    return ask_llm(prompt)