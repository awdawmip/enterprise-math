#!/usr/bin/env python3
"""EC49FAR exact certificate; Python 3 standard library only. Output a JSON report."""
import itertools,json
from fractions import Fraction
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
START=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
WORDS=('de','ed','ce','ec','feg','gef')
CLAUSES=(('ed','feg'),('ce','feg'),('de','gef'),('ec','gef'))
MINIMA=({0,1,2,3},{0,3,4},{1,2,5},{4,5})
def steps(w):return tuple(s for c in w for s in OPS[c])
def obs(w):
 out=[]
 for state,prev in START:
  for s in steps(w):
   if prev==1 and s==2:
    if state=='N':state='A'
    elif state=='B':state='BA'
   elif prev==2 and s==1:
    if state=='N':state='B'
    elif state=='A':state='AB'
   prev=s
  out.append(('N','A','B','AB','BA').index(state))
 return tuple(out)
def matrix(ss):return [[int(sig[j]==b) for j in range(9)] for sig in ss for b in range(5)]
def rank(M):
 A=[[Fraction(x) for x in r] for r in M];k=0
 for j in range(9):
  p=next((i for i in range(k,len(A)) if A[i][j]),None)
  if p is None:continue
  A[k],A[p]=A[p],A[k];v=A[k][j]
  for t in range(j,9):A[k][t]/=v
  for i in range(k+1,len(A)):
   v=A[i][j]
   if v:
    for t in range(j,9):A[i][t]-=v*A[k][t]
  k+=1
 return k

def det(M):
 A=[r[:] for r in M];d=1;sgn=1
 for k in range(8):
  if not A[k][k]:
   j=next(i for i in range(k+1,9) if A[i][k]);A[j],A[k]=A[k],A[j];sgn=-sgn
  p=A[k][k]
  for i in range(k+1,9):
   for j in range(k+1,9):
    v=A[i][j]*p-A[i][k]*A[k][j];assert v%d==0;A[i][j]=v//d
   A[i][k]=0
  d=p
 return sgn*A[8][8]

def run():
 sig={w:obs(w) for w in WORDS}
 expected={'de':(2,3,2,3,3,2,4,3,4),'ed':(2,2,2,3,3,2,2,3,4),
 'ce':(1,1,4,1,3,4,4,3,4),'ec':(1,1,1,1,1,4,4,3,4),
 'feg':(0,0,2,1,3,2,2,3,4),'gef':(0,1,0,1,1,2,4,3,4)}
 assert sig==expected
 pair_masks={}
 for i,j in itertools.combinations(range(9),2):
  m={w for w in WORDS if sig[w][i]!=sig[w][j]}
  assert any(set(c)<=m for c in CLAUSES)
  pair_masks[f'{i+1}-{j+1}']=[w for w in WORDS if w in m]
 for c in CLAUSES:
  assert sum(set(v)==set(c) for v in pair_masks.values())==2
 rank_counts={};winning=[]
 for mask in range(64):
  sel={i for i in range(6) if mask>>i&1};r=rank(matrix([sig[WORDS[i]] for i in sel]))
  pred=all(any(WORDS[i] in c for i in sel) for c in CLAUSES)
  assert (r==9)==pred
  assert (r==9)==any(m<=sel for m in MINIMA)
  rank_counts[str(r)]=rank_counts.get(str(r),0)+1
  if r==9:winning.append(mask)
 minors={
 'de,ed,ce,ec':(('de',2),('de',3),('de',4),('ed',2),('ed',3),('ce',1),('ce',3),('ec',1),('ec',3)),
 'de,ec,feg':(('de',2),('de',3),('de',4),('ec',1),('ec',3),('feg',0),('feg',1),('feg',2),('feg',3)),
 'ed,ce,gef':(('ed',2),('ed',3),('ed',4),('ce',1),('ce',3),('gef',0),('gef',1),('gef',2),('gef',3)),
 'feg,gef':(('feg',0),('feg',1),('feg',2),('feg',3),('feg',4),('gef',0),('gef',1),('gef',2),('gef',3))}
 dets={k:det([[int(sig[w][j]==b) for j in range(9)] for w,b in v]) for k,v in minors.items()}
 assert dets=={'de,ed,ce,ec':-1,'de,ec,feg':1,'ed,ce,gef':1,'feg,gef':-1}
 assert rank_counts=={'0':1,'3':4,'5':14,'7':20,'9':25}
 return {'status':'PASS','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'subsets_checked':64,'histogram':rank_counts,'rank9_count':len(winning),
 'four_clauses':[list(c) for c in CLAUSES],
 'minimal_rank9_sets':[[WORDS[i] for i in sorted(x)] for x in MINIMA],
 'integral_minor_determinants':dets,'initial_history_pair_masks':pair_masks,
 'signatures':{w:list(s) for w,s in sig.items()}}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
