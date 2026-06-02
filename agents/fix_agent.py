from utils.llm import ask_llm

def fix_agent(log_text):

    prompt = f"""
    You are a DevOps Engineer.

    Analyze the log and suggest:

    1. Exact Fix
    2. Commands to Run
    3. Prevention Tips

    Log:
    {log_text}
    """

    return ask_llm(prompt)