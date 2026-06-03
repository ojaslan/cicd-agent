from agents.report_generator import create_report


def test_create_report():
    summary = "Dependency error"
    cause = "pandas missing"
    fix = "pip install pandas"

    report = create_report(summary, cause, fix)

    assert "Dependency error" in report  # nosec B101
    assert "pandas missing" in report  # nosec B101
    assert "pip install pandas" in report  # nosec B101