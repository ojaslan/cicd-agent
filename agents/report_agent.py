from utils.llm import ask_llm

def report_agent(
    severity,
    root_cause,
    fix,
    prevention
):

    prompt = f"""
    Generate a professional incident report.

    Severity:
    {severity}

    Root Cause:
    {root_cause}

    Fix:
    {fix}

    Prevention:
    {prevention}

    Format nicely with headings.
    """

    return ask_llm(prompt)