#!/usr/bin/env python3
"""Post the demo images (one folder each) to a running Postgram API.

  python3 post.py 05-beach     # post one folder (prefix match works too: post.py 05)
  python3 post.py all          # post all 24

Override the API base if the backend is not on port 8000:
  POSTGRAM_API=http://localhost:8001/api  python3 post.py all
"""
import glob, json, os, sys, urllib.request

API = os.environ.get("POSTGRAM_API", "http://localhost:8000/api")
HERE = os.path.dirname(os.path.abspath(__file__))

def parse(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    caption = lines[0] if lines else ""
    author = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("author:")), "guest")
    url = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("image_url:")), "")
    return {"image_url": url, "caption": caption, "author": author}

def post(path):
    body = json.dumps(parse(path)).encode()
    req = urllib.request.Request(API + "/posts", body, {"Content-Type": "application/json"})
    folder = os.path.basename(os.path.dirname(path))
    try:
        r = json.load(urllib.request.urlopen(req, timeout=15))
        print(f"posted {folder}  ->  {r['id'][:8]}  ({r['author']})")
    except Exception as e:
        print(f"FAILED {folder}: {e}  (is the backend running at {API}?)")

arg = sys.argv[1] if len(sys.argv) > 1 else "all"
if arg == "all":
    files = sorted(glob.glob(os.path.join(HERE, "*", "caption.txt")))
else:
    files = sorted(glob.glob(os.path.join(HERE, f"{arg}*", "caption.txt")))
if not files:
    print(f"no folder matching {arg!r}")
for f in files:
    post(f)
