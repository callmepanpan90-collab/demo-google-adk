import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from .tools import (
    get_jira_ticket, get_figma_spec, inspect_repo,
    run_mock_tests, prepare_pr_draft,
)

load_dotenv()

# Cho phép tuỳ chọn model qua biến môi trường (.env), mặc định gemini-2.5-flash
MODEL_NAME = os.getenv("GEMINI_MODEL") or os.getenv("MODEL") or "gemini-2.5-flash"

root_agent = Agent(
    name="developer_agent",
    model="gemini-2.5-flash-lite",
    description="Analyze Jira mock tickets and prepare safe PR drafts.",
    instruction="""You are a Developer Agent running a controlled demo.
    When asked to analyze ticket PROJ-123:
    1. Call get_jira_ticket before reasoning about requirements.
    2. Use get_figma_spec with the figma_id from the ticket.
    3. Use inspect_repo to inspect mock repository metadata.
    4. Use run_mock_tests to check simulated tests.
    5. Call prepare_pr_draft ONLY as a text draft, with the real test status.
    Never claim to have edited code, run real tests, created a Git branch,
    opened a real PR, merged anything, or connected to real Jira/Figma.
    If tests fail, clearly say the result failed and requires human action.
    Clearly label all source data as simulated. Respond in Vietnamese.
    """,
    tools=[get_jira_ticket, get_figma_spec, inspect_repo,
           run_mock_tests, prepare_pr_draft],
)
