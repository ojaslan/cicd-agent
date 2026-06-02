from utils.llm import ask_llm

def prevention_agent(log_text, root_cause):

    prompt = f"""
    You are a Senior Site Reliability Engineer.

    Log:
    {log_text}

    Root Cause:
    {root_cause}

    Suggest:

    1. Prevention Steps
    2. Monitoring Improvements
    3. CI/CD Improvements
    4. Best Practices

    Keep answer concise.
    """

    return ask_llm(prompt)