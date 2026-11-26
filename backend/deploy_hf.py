"""Deploy the proxy to a Hugging Face Docker Space with the Gemini key as a Space SECRET.
Env needed (never printed): HF_TOKEN (write token), GEMINI_API_KEY.
Usage: HF_TOKEN=... GEMINI_API_KEY=... python3 deploy_hf.py [space-name]
"""
import os, sys, pathlib
from huggingface_hub import HfApi

here = pathlib.Path(__file__).parent
api = HfApi(token=os.environ["HF_TOKEN"])
user = api.whoami()["name"]
name = sys.argv[1] if len(sys.argv) > 1 else "ms-store-smart-bot"
repo = f"{user}/{name}"
api.create_repo(repo, repo_type="space", space_sdk="docker", exist_ok=True)
api.add_space_secret(repo, "GEMINI_API_KEY", os.environ["GEMINI_API_KEY"])
for f, dest in [("server.mjs", "server.mjs"), ("catalog.json", "catalog.json"), ("Dockerfile", "Dockerfile"), ("SPACE_README.md", "README.md")]:
    api.upload_file(path_or_fileobj=str(here / f), path_in_repo=dest, repo_id=repo, repo_type="space")
print("space:", f"https://huggingface.co/spaces/{repo}")
print("api url:", f"https://{user.lower()}-{name}.hf.space")
