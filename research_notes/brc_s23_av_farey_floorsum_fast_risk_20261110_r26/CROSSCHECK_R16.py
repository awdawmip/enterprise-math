#!/usr/bin/env python3
import random,csv,hashlib,sys,time
from bisect import bisect_right
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from VERIFY_R26 import eval_risk
src=Path('/mnt/data/em_r16/AFFINE_RUNS_1T.tsv')
rows=list(csv.DictReader(src.open(),delimiter='\t'))
rows=[{k:int(v) for k,v in row.items()} for row in rows]
starts=[r['n0'] for r in rows]
assert len(rows)==298 and starts==sorted(starts)
def lookup(n):
 idx=bisect_right(starts,n)-1
 row=rows[idx]
 assert row['n0']<=n<=row['n1']
 d=n-row['n0']
 return(row['A0']+d*row['dA'],row['B0']+d*row['dB'])
points=set([128,129,10**12,10**12+128,2000128])
for row in rows:
 for s in (row['n0']-1,row['n0'],row['n0']+1,row['n1']-1,row['n1'],row['n1']+1):
  if 128<=s<=10**12+128:points.add(s)
rng=random.Random(20261110)
points.update(rng.randint(128,10**12+128) for _ in range(250))
start=time.perf_counter()
for ix,n in enumerate(sorted(points)):
 (a,b),_,_,_,_=eval_risk(n)
 want=lookup(n)
 assert (a,b)==want,(n,(a,b),want)
print('PASS_R26_CROSSCHECK_R16_AFFINE_1T')
print('R16_TSV_ROWS',len(rows),'SHA256',hashlib.sha256(src.read_bytes()).hexdigest())
print('EXACT_CHECKED',len(points),'RANGE',min(points),max(points))
print('DURATION_SEC',round(time.perf_counter()-start,3))
print('AT_ONE_TRILLION_FUTURE',eval_risk(10**12+128)[0])
