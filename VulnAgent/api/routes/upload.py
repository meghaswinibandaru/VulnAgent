from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from agent.orchestrator import run_agent
import json, os, aiofiles, tempfile

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    selected_ips: str = Form(...)
):
    ip_prefixes = json.loads(selected_ips)

    # ✅ Use system temp dir — works on Windows, Linux, Mac
    tmp_dir = tempfile.gettempdir()
    tmp_path = os.path.join(tmp_dir, file.filename)

    async with aiofiles.open(tmp_path, "wb") as f:
        content = await file.read()
        await f.write(content)

    output_path, summary = run_agent(tmp_path, ip_prefixes)
    filename = os.path.basename(output_path)

    return JSONResponse({
        "download_url": f"/download/{filename}",
        "summary": summary
    })