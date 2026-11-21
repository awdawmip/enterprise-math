"""Replay the incumbent table against the archived native components."""
from pathlib import Path
import json,subprocess,sys,argparse,os
from templates import verify,BASE
if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--original',type=Path,default=Path(__file__).resolve().parents[1]/'original')
 a=p.parse_args()
 subprocess.run([sys.executable,'-B',str(BASE/'native/replay.py'),'--original',str(a.original.resolve()),'--labels','13'],check=True)
 print(json.dumps(verify(),sort_keys=True))
