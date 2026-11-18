"""EC49BZ: exact native-X6 packed-transfer versus sparse-DP certificate."""
import json,importlib.util
from collections import defaultdict
from pathlib import Path
D=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('brc',D/'source/signed_brc.py')
brc=importlib.util.module_from_spec(sp);sp.loader.exec_module(brc)
Z=(0,)*6; S=tuple(range(1,7))+tuple(range(-1,-7,-1)); W=(2,3,3,2,1,1)
Q=[(i,j) for i in range(3) for j in range(3)]; J={v:i for i,v in enumerate(Q)}
sw=lambda a:(2 if a>0 else -2) if abs(a)==1 else ((1 if a>0 else -1) if abs(a)==2 else a)
w=lambda a:W[a-1] if a>0 else 1
dfa=lambda q,a:2 if q==2 or(q==1 and a==2) else (1 if a==1 else 0)
to=lambda i,a:J[(dfa(Q[i][0],a),dfa(Q[i][1],sw(a)))]
atom=lambda i:f'{int(Q[i][0]==2)}{int(Q[i][1]==2)}'
def dp(n):
 F={(Z,0):(1,1,1)}
 for _ in range(n):
  T={}
  for (x,i),(u,v,c) in F.items():
   for a in S:
    y=list(x);y[abs(a)-1]+=1 if a>0 else -1
    key=(tuple(y),to(i,a));p,q,r=T.get(key,(0,0,0))
    T[key]=(p+u*w(a),q+v*w(sw(a)),r+c)
  F=T
 out={k:[0,0,0] for k in ('00','01','10','11')}
 for (x,i),vals in F.items():
  if x==Z:
   a=out[atom(i)]
   for j in range(3):a[j]+=vals[j]
 return out

def packed(n,g):
 if n==0:return {'00':1,'01':0,'10':0,'11':0}
 radix=2*n+1; powers=[radix**k for k in range(6)]
 bits=((12*max(W))**n).bit_length()+1;mask=(1<<bits)-1
 A=[[0]*9 for _ in range(9)]
 for i in range(9):
  for a in S:
   pos=sum(powers)+(powers[abs(a)-1] if a>0 else -powers[abs(a)-1])
   A[i][to(i,a)]+=w(a if g==0 else sw(a))<<(bits*pos)
 def mm(A,B):
  C=[[0]*9 for _ in range(9)]
  for i in range(9):
   for k in range(9):
    if A[i][k]:
     for j in range(9):
      if B[k][j]:C[i][j]+=A[i][k]*B[k][j]
  return C
 row=[1]+[0]*8;t=n
 while t:
  if t&1:row=[sum(row[k]*A[k][j] for k in range(9)) for j in range(9)]
  t//=2
  if t:A=mm(A,A)
 out={k:0 for k in ('00','01','10','11')}
 shift=bits*n*sum(powers)
 for i,x in enumerate(row):out[atom(i)]+=(x>>shift)&mask
 return out

def detect(word):
 q=0;r=0
 for a in word:q,r=dfa(q,a),dfa(r,sw(a))
 return (q,r)

def main():
 results={}
 for n in (0,2,4,6,8):
  d=dp(n);tot=[sum(v[i] for v in d.values()) for i in range(3)]
  expected=[int(brc.endpoint_weight(n,Z,W,(1,)*6))]*2+[brc.endpoint_multiplicity(n,Z)]
  assert tot==expected,(n,tot,expected)
  if n<=4:
   for g in (0,1):assert packed(n,g)=={a:v[g] for a,v in d.items()}
  results[str(n)]={'native_totals':tot,'atoms':d,'packed_checked':n<=4}
 # Exact equal current terminal observation, unequal future append observation.
 p=(1,-1);q=(-1,1);suffix=(2,-2)
 assert all(sum(1 if a==i else -1 if a==-i else 0 for a in v)==0 for v in (p,q,p+suffix,q+suffix) for i in range(1,7))
 assert detect(p)==(0,0) and detect(q)==(1,0)
 assert atom(J[detect(p)])==atom(J[detect(q)])=='00'
 assert [__import__('math').prod(w(a if g==0 else sw(a)) for a in p) for g in (0,1)]==[2,3]
 assert [__import__('math').prod(w(a if g==0 else sw(a)) for a in q) for g in (0,1)]==[2,3]
 assert atom(J[detect(p+suffix)])=='00' and atom(J[detect(q+suffix)])=='10'
 return {'results':results,'append_counterexample':{'p':p,'q':q,'suffix':suffix,'before_weights':[2,3],'after_weights':[6,6],'before_atoms':['00','00'],'after_atoms':['00','10']},'native_kernel_git_blob':'300a96e3dc24bf6fff73743037a0347a8bc83176'}
if __name__=='__main__':
 report=main();payload=json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
 (D/'EXACT_REPORT_EC49BZ.json').write_text(payload,encoding='utf8')
 print(payload,end='')
