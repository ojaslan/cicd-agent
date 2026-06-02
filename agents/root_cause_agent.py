from utils.llm import ask_llm

def root_cause_agent(log_text):

    prompt = f"""
    You are a Senior DevOps Engineer.

    Analyze the CI/CD failure log.

    Find:
    1. Root Cause
    2. Explanation

    Keep answer concise.

    Log:
    {log_text}
    """

    return ask_llm(prompt)