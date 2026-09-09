import argparse,subprocess,json,hashlib,time,sys
from pathlib import Path
from datetime import datetime,timezone
p=argparse.ArgumentParser();p.add_argument("--id",required=True);p.add_argument("--cwd",required=True);p.add_argument("command",nargs=argparse.REMAINDER);a=p.parse_args()
root=Path(r"D:/em/TEMP/r005-q78553-review-81273a-20260910/checks");root.mkdir(parents=True,exist_ok=True)
cmd=a.command[1:] if a.command and a.command[0]=="--" else a.command
assert cmd
pre=root/a.id
for suffix in [".stdout.log",".stderr.log",".run.json"]:
 if Path(str(pre)+suffix).exists():raise FileExistsError(str(pre)+suffix)
start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
r=subprocess.run(cmd,cwd=a.cwd,capture_output=True)
receipt={"schema":"R005_DRIVER_ACTUAL_REVIEW_RUN_V1","driver_id":"EM-DVR-81273A","argv":cmd,"cwd":a.cwd,"started_at":start,"ended_at":datetime.now(timezone.utc).isoformat(),"elapsed_seconds":time.perf_counter()-tick,"exit_code":r.returncode}
for name,data in [("stdout",r.stdout),("stderr",r.stderr)]:
 path=Path(str(pre)+"."+name+".log");path.write_bytes(data)
 receipt[name]={"path":str(path),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
Path(str(pre)+".run.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
sys.stdout.buffer.write(r.stdout);sys.stderr.buffer.write(r.stderr)
print(json.dumps(receipt,ensure_ascii=True))
raise SystemExit(r.returncode)

