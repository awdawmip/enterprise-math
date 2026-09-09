"""Capture an actual command's argv, exact streams, exit status and byte digests."""
import argparse, hashlib, json, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument("--log-prefix",type=Path,required=True)
p.add_argument("command",nargs=argparse.REMAINDER)
a=p.parse_args()
argv=a.command[1:] if a.command and a.command[0]=="--" else a.command
if not argv:
    p.error("a real command is required")
prefix=a.log_prefix
prefix.parent.mkdir(parents=True,exist_ok=True)
stdout_path=Path(str(prefix)+".stdout.log")
stderr_path=Path(str(prefix)+".stderr.log")
receipt_path=Path(str(prefix)+".run.json")
if any(x.exists() for x in (stdout_path,stderr_path,receipt_path)):
    raise FileExistsError("Run logs already exist; preserve them and choose a new run name")
started=datetime.now(timezone.utc).isoformat()
tick=time.perf_counter()
with stdout_path.open("wb") as fout, stderr_path.open("wb") as ferr:
    child=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=ferr)
    for line in iter(child.stdout.readline,b""):
        fout.write(line);fout.flush()
        sys.stdout.buffer.write(line);sys.stdout.buffer.flush()
    code=child.wait()
receipt={"schema":"R005_ACTUAL_COMMAND_RUN_V1","argv":argv,"cwd":str(Path.cwd()),"started_at":started,"completed_at":datetime.now(timezone.utc).isoformat(),"elapsed_seconds":time.perf_counter()-tick,"exit_code":code}
for name,path in (("stdout",stdout_path),("stderr",stderr_path)):
    data=path.read_bytes()
    receipt[name]={"path":str(path),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
receipt_path.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"run_receipt":str(receipt_path),"exit_code":code}),flush=True)
raise SystemExit(code)

