from agents.report_generator import create_report


def test_create_report():
    summary = "Dependency error"
    cause = "pandas missing"
    fix = "pip install pandas"

    report = create_report(summary, cause, fix)

    assert "Dependency error" in report
    assert "pandas missing" in report
    assert "pip install pandas" in report