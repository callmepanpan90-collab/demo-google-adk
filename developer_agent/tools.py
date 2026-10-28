"""Safe mock tools: no external Jira/Figma/GitLab calls."""
import os


def get_jira_ticket(ticket_id: str) -> dict:
    """Get a Jira ticket requirement by ID from demo mock data."""
    if ticket_id != "PROJ-123":
        return {"status": "not_found", "ticket_id": ticket_id}
    return {"status": "ok", "ticket_id": ticket_id,
            "title": "Forgot Password", "description": "Add forgot password UI",
            "criteria": ["Validate email", "Show loading", "Show success/error"],
            "figma_id": "FIGMA-123"}


def get_figma_spec(figma_id: str) -> dict:
    """Read the mocked Figma specification for a design ID."""
    if figma_id != "FIGMA-123":
        return {"status": "not_found", "figma_id": figma_id}
    return {"status": "ok", "figma_id": figma_id,
            "fields": ["email"], "button": "Send reset link",
            "states": ["idle", "loading", "success", "error"]}


def inspect_repo(feature: str) -> dict:
    """Inspect read-only mocked frontend repository metadata for a feature."""
    return {"status": "ok", "feature": feature, "framework": "React",
            "relevant_files": ["src/pages/Login.tsx", "src/api/auth.ts", "src/tests/auth.test.ts"],
            "note": "This is fake metadata; no filesystem is modified."}


def run_mock_tests(feature: str) -> dict:
    """Run simulated tests for the specified feature, never real shell commands."""
    if os.getenv("TEST_FORCE_FAIL", "0") == "1":
        return {"status": "fail", "feature": feature,
                "tests": ["email-validation: FAIL"],
                "details": "Missing validation for invalid email (simulated)"}
    return {"status": "pass", "feature": feature,
            "tests": ["email-validation: PASS", "loading-state: PASS", "success-state: PASS"],
            "note": "All results simulated; does not prove code has been implemented."}


def prepare_pr_draft(ticket_id: str, summary: str, test_status: str) -> dict:
    """Prepare a text-only pull request draft. Does not create a real PR."""
    return {"status": "draft_only", "ticket_id": ticket_id,
            "title": f"[{ticket_id}] Forgot Password implementation plan",
            "summary": summary, "test_status": test_status,
            "warning": "DRAFT ONLY: no branch, commit, code modification, or PR created."}
