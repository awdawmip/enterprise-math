from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,sys
here=Path(__file__).resolve().parent
ids=list(map(int,sys.argv[1:]))or list(range(1,19))
def run(i):
 with (here/f'core2_9860_case{i}.log').open('w')as f:
  p=subprocess.run([sys.executable,'-B',here/'core_two_weights.py','--budget','9860','--case',str(i)],stdout=f,stderr=subprocess.STDOUT)
 print(i,p.returncode,flush=True)
 assert p.returncode==0
with ThreadPoolExecutor(2)as pool:list(pool.map(run,ids))
