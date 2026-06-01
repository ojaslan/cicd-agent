def create_report(summary, cause, fix):
    return f"""
# CI/CD Failure Report

## Error Summary
{summary}

## Root Cause
{cause}

## Suggested Fix
{fix}
"""