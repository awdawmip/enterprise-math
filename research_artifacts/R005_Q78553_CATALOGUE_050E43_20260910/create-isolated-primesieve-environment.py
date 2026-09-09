from pathlib import Path
import hashlib, json, urllib.request, zipfile, sys
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parent
ENV = ROOT / "py39-sieve"
ART = Path("D:/em/r005-q78553-research-050e43-20260910/research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910")
ENV.mkdir(exist_ok=True)
downloads = ROOT / "third-party-downloads"
downloads.mkdir(exist_ok=True)
manifest = []
def get(url, name, expected=None):
    target=downloads/name
    if target.exists():
        data=target.read_bytes()
    else:
        data=urllib.request.urlopen(url, timeout=45).read()
        target.write_bytes(data)
    digest=hashlib.sha256(data).hexdigest()
    if expected is not None and digest != expected:
        raise RuntimeError("Download hash mismatch: "+name)
    manifest.append(dict(url=url,path=str(target),bytes=len(data),sha256=digest,expected_sha256=expected,observed_at=datetime.now(timezone.utc).isoformat()))
    return target
def unpack(path, target):
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            dest=(target/info.filename).resolve()
            if not dest.is_relative_to(target.resolve()):
                raise RuntimeError("Archive path leaves isolated environment")
        z.extractall(target)
py=get("https://www.python.org/ftp/python/3.9.13/python-3.9.13-embed-amd64.zip","python-3.9.13-embed-amd64.zip")
unpack(py,ENV)
pypi=json.loads((ART/"pypi-primesieve-2.3.0.json").read_text())
pw=next(x for x in pypi["urls"] if x["filename"]=="primesieve-2.3.0-cp39-cp39-win_amd64.whl")
unpack(get(pw["url"],pw["filename"],pw["digests"]["sha256"]),ENV/"site-packages")
url="https://pypi.org/pypi/numpy/1.26.4/json"
raw=urllib.request.urlopen(url,timeout=30).read()
(ART/"pypi-numpy-1.26.4.json").write_bytes(raw)
nd=json.loads(raw)
nw=next(x for x in nd["urls"] if x["filename"]=="numpy-1.26.4-cp39-cp39-win_amd64.whl")
unpack(get(nw["url"],nw["filename"],nw["digests"]["sha256"]),ENV/"site-packages")
(ENV/"python39._pth").write_text("python39.zip\n.\nsite-packages\nimport site\n")
(ART/"isolated-primesieve-environment-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(dict(environment=str(ENV),downloads=manifest),indent=2))

