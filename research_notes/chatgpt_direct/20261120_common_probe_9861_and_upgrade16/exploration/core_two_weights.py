"""Derive integer dual search weights and run exact cover on two-core branches.
LP output is rounded downward and every reduced cost is checked as an integer.
Only the integer cover output may certify an exclusion.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,json,sys,subprocess,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
HERE=Path(__file__).resolve().parent
PREV=HERE.parent/'previous';THIRD=PREV/'previous/previous/previous/previous';SECOND=THIRD/'previous'
sys.path[:0]=[str(PREV/'twelve_cores'),str(THIRD/'low'),str(SECOND/'curve'),str(SECOND/'bounds')]
from replay import placements
from verify import lower,MINIMA

def main():
 p=argparse.ArgumentParser();p.add_argument('--budget',type=int,default=9860);p.add_argument('--case',type=int,default=0);p.add_argument('--all',action='store_true');a=p.parse_args()
 w=HERE/f'core2_{a.budget}';w.mkdir(exist_ok=True)
 source=HERE/'core3_9870'
 frames=[];seen=set()
 for line in (source/'cores2.txt').read_text().splitlines():
  lo,hi,*centres=map(int,line.split());free=lo+(hi<<64)
  for bits in range(4):
   picked=[v for j,v in enumerate(centres)if bits>>j&1]
   if len(picked)!=len(set(picked)):continue
   inserted=sum(1<<v for v in picked)
   if inserted&~free:continue
   pair=free^inserted,2208+192*len(picked)
   if pair not in seen:seen.add(pair);frames.append(pair)
 assert len(frames)==19
 (w/'manifest.json').write_text(json.dumps({'budget':a.budget,'frames':frames},indent=2)+'\n')
 def run(i):
  mask,spent=frames[i];left=a.budget-spent;caps=[left-lower(mask.bit_count()-s,9)for s in range(14)]
  available=list(map(int,(source/'caps').read_text().split()))
  assert all(cap<=available[s]for s,cap in enumerate(caps)if s and cap>=MINIMA[s])
  least=next(s for s in range(1,14)if caps[s]>=MINIMA[s]);inp=w/f'i{i}';data=w/f'd{i}';wf=w/f'w{i}';out=w/f'result_{i}.json'
  if out.exists():return json.loads(out.read_text())
  inp.write_text(' '.join(map(str,[mask%2**64,mask>>64,least,13,*caps[least:]]))+'\n')
  subprocess.run([source/'filter',source/'global.bin',inp,data,'1'],check=True)
  rows=np.fromfile(data,dtype=[('points','u1',(13,)),('size','u1'),('price','<u2')])
  n=len(rows);maxs=int(rows['size'].max())
  inds=[];coeff=[];ptr=[0]
  for r in rows:
   s=int(r['size']);inds.extend(r['points'][:s].tolist()+[125]);coeff.extend([1.]*(s+1));ptr.append(len(inds))
  A=csc_matrix((coeff,inds,ptr),shape=(126,n));b=np.array([float(mask>>i&1)for i in range(125)]+[10.])
  print('LP',i,'rows',n,'budget',left,flush=True);start=time.time()
  lp=linprog(rows['price'].astype(float),A_eq=A,b_eq=b,bounds=(0,None),method='highs-ds',options={'time_limit':120})
  print('LP done',i,lp.status,lp.fun,time.time()-start,flush=True)
  assert lp.success,lp.message
  weights=np.floor(1000*lp.eqlin.marginals).astype(np.int64)
  rc=rows['price'].astype(np.int64)*1000-np.asarray(A.T@weights).ravel().astype(np.int64)
  correction=min(0,int(rc.min()));weights[125]+=correction
  rc-=correction;assert rc.min()>=0
  wf.write_text(' '.join(map(str,weights.tolist()))+'\n')
  meta={'case':i,'budget':a.budget,'rows':n,'lp_objective_float':float(lp.fun),'weights':weights.tolist(),'minimum_reduced_cost':int(rc.min()),'label_rounding_correction':correction}
  (w/f'weights_{i}.json').write_text(json.dumps(meta,indent=2)+'\n')
  del A,rows,inds,coeff,ptr
  print('COVER',i,'slack',left*1000-int(b@weights),flush=True);start=time.time()
  q=subprocess.run([source/'cover',data,wf,inp,str(left),'10'],capture_output=True,text=True)
  words=list(map(int,q.stdout.split()));assert q.returncode==0
  result={'case':i,'budget':a.budget,'raw':q.stdout.strip(),'seconds':time.time()-start,'objective':words[0],'legal_candidates':words[1],'weighted_candidates':words[2],'nodes':words[3],'solutions':words[4]}
  out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
  return result
 indices=range(19)if a.all else[a.case]
 for i in indices:run(i)
if __name__=='__main__':main()
