"""Independent author implementation, literal ordered-word DFS with integer P/Q weights."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from collections import defaultdict
import json
from pathlib import Path
N=14; WP=(3,1,20);WQ=(1,1,10);DENP=24**N;DENQ=12**N
K=F(3787884,5905);L=F(3551272,5905)
A=(12,7,3);B=(11,0,1)
@lru_cache(None)
def best(n,a,b):
 offers={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:offers['C']=1+sum(F(WP[j],24)*best(n+1,a+int(j==0),b+int(j==1))[0] for j in range(3))
 m=min(offers.values())
 return m,tuple(op for op,v in offers.items() if v==m)
assert best(0,0,0)[0]==F(38329289789453267095823,86261060643965632512)
assert best(*A)[1]==('P','C') and best(*B)[1]==('Q','C')
def enumerate_words(w,u):
 sums=[0]*4;hits=defaultdict(lambda:[0,0,0]);stats=[0,0]
 def visit(n,a,b,p,q):
  stats[0]+=1;s=(n,a,b)
  if s in (A,B):
   h=hits[s];h[0]+=1;h[1]+=p*24**(N-n);h[2]+=q*12**(N-n)
  op=('Q' if w else 'C') if s==B else ('P' if u else 'C') if s==A else best(n,a,b)[1][0]
  assert op in best(n,a,b)[1]
  if op=='C':
   for j in range(3):visit(n+1,a+int(j==0),b+int(j==1),p*WP[j],q*WQ[j])
  else:
   stats[1]+=1;pp=p*24**(N-n);qq=q*12**(N-n)
   if op=='Q':sums[0]+=pp
   else:sums[1]+=qq
   sums[2]+=n*pp;sums[3]+=n*qq
 visit(0,0,0,1,1)
 return {'moments':[str(F(sums[0],DENP)),str(F(sums[1],DENQ)),str(F(sums[2],DENP)),str(F(sums[3],DENQ))],
  'prefix_visits':stats[0],'terminal_words':stats[1],
  'first_hits':{str(s):{'literal_word_count':h[0],'P':str(F(h[1],DENP)),'Q':str(F(h[2],DENQ))} for s,h in hits.items()}}
c={f'{w}{u}':enumerate_words(w,u) for w,u in product((0,1),repeat=2)}
M={k:tuple(map(F,v['moments'])) for k,v in c.items()}
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
mul=lambda x,a:tuple(v*a for v in x)
m=M['00'];dB=sub(M['10'],m);dA=sub(M['01'],m)
assert M['11']==add(add(m,dB),dA)
err=lambda x:x[0]-x[1]
w0=-err(m)/err(dB);slope=-err(dA)/err(dB)
assert w0==F(23520936469043837,81438720000000000)
assert slope==F(18849,192800000000)
pt=lambda u:add(add(m,mul(dB,w0+slope*u)),mul(dA,u))
start,end=pt(F(0)),pt(F(1))
assert start[0]==F(36696744084893090695,105616844785075617792)
assert end[0]==F(36696744092375906695,105616844785075617792)
assert end[2]==F(660257035708884947227,52808422392537808896)
for p in (start,end):
 assert p[0]==p[1] and p[2]>p[3]
 assert p[2]+K*p[1]+L*p[0]==best(0,0,0)[0]
assert 0<w0<w0+slope<1
assert c['00']['first_hits'][str(A)]['literal_word_count']==3168
assert c['00']['first_hits'][str(B)]['literal_word_count']==11
assert [(c[k]['prefix_visits'],c[k]['terminal_words']) for k in ('00','01','10','11')]==[(775522,517015),(756514,504343),(775390,516927),(756382,504255)]
Path(__file__).with_name('ordered_evidence131_portable.json').write_text(json.dumps({'grade':'AUTHOR_INDEPENDENT_LOCAL_ALGORITHM','corners':c},indent=2),encoding='utf8')
print('PASS STAGE131 literal-word integer DFS')
print('HITS',json.dumps(c['00']['first_hits']))