# Developer Agent — Google ADK Demo

## Scope
Safe mock tools for Jira, Figma, repository and tests. The PR is a text draft only. No code, branch, pull request, or real integration is modified.

## Setup
Python >= 3.10. From `google_adk_developer_agent_demo`:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp developer_agent/.env.example developer_agent/.env
```

Edit `developer_agent/.env` and provide your Gemini API key. **Never commit API keys.**

```bash
adk web --port 8000
# or: adk run developer_agent
```

Open http://localhost:8000 and select `developer_agent`.

## Demo A — normal flow

Prompt:

> Đọc Jira PROJ-123, tóm tắt yêu cầu, đối chiếu Figma và source code, chạy kiểm tra mô phỏng rồi chuẩn bị PR draft. Hãy ghi rõ phần nào là dữ liệu giả lập.

Inspect function-call events in ADK web. Tool order may vary.

## Demo B — simulated fail

Close the server, run:

```bash
TEST_FORCE_FAIL=1 adk web --port 8000
```

On Windows PowerShell: `$env:TEST_FORCE_FAIL='1'; adk web --port 8000`.

Enter the same prompt. Agent must report failure; it cannot repair code without an editing tool.

## Lựa chọn LLM (Model Selection)

Dự án hỗ trợ 2 cách chọn LLM:

1. **Chọn trực tiếp trên giao diện ADK Web (Dropdown góc trên bên trái):**
   - `developer_agent`: Sử dụng model mặc định hoặc model cấu hình trong file `.env` (`gemini-2.5-flash`).
   - `developer_agent_gemini3`: Chạy mô hình thế hệ mới `gemini-3-flash-preview`.
   - `developer_agent_lite`: Chạy mô hình siêu nhẹ và nhanh `gemini-2.5-flash-lite`.

2. **Cấu hình qua file `.env`:**
   Mở file `.env` (hoặc `developer_agent/.env`) và đổi giá trị biến `MODEL`:
   ```env
   MODEL=gemini-2.5-flash
   # Hoặc: gemini-3-flash-preview, gemini-2.5-flash-lite, gemini-3.1-flash-lite-preview
   ```

## References
- https://adk.dev/get-started/python/
- https://adk.dev/tools-custom/
