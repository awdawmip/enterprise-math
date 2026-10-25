#!/usr/bin/env python3
"""Stage143 first Bellman directional gap closure from exact Stage142 dual, candidate only."""
from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6))
K=F(395290882339224,875825669873);L=F(54591710813272,125117952839)
dk=-F(43,1536);dl=-F(7,288)
B=(11,0,1);J=(4,3,0)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):
 n,a,b=s;return F(2**(a+b),3**a)
v={};dv={};cand=[]
for s in reversed(S):
 c={'P':K*ratio(s),'Q':L};d={'P':dk*ratio(s),'Q':dl}
 if s[0]<14:
  c['C']=1+sum((P[i]*v[t] for i,t in enumerate(child(s))),F())
  d['C']=sum((P[i]*dv[t] for i,t in enumerate(child(s))),F())
 z=min(c.values());a=('Q' if s==B else 'P' if s==J else next(b for b in c if c[b]==z))
 assert c[a]==z
 v[s]=c[a];dv[s]=d[a]
 for b in c:
  if b==a:continue
  gap=c[b]-z;slope=d[b]-d[a]
  if not gap:assert slope>=0
  elif slope<0:cand.append((gap/-slope,s,a,b))
t,s,a,b=min(cand)
assert len(cand)==834 and (s,a,b)==((3,3,0),'C','P')
assert t==F(36775812459682145214747988992,39950391891606071321645969)
kk=K+dk*t;ll=L+dl*t
assert kk==F(19411949464309662,45614547809953)
assert ll==F(18882041753802888,45614547809953)
V={};ties=[];gaps=[]
for s in reversed(S):
 c={'P':kk*ratio(s),'Q':ll}
 if s[0]<14:c['C']=1+sum((P[i]*V[x] for i,x in enumerate(child(s))),F())
 z=min(c.values());best=[a for a in c if c[a]==z]
 if len(best)>1:ties.append((s,best))
 gaps.extend([x-z for x in c.values() if x>z]);V[s]=z
assert len(V)==680 and len(gaps)==1238
assert set((s,tuple(a)) for s,a in ties)=={(B,('Q','C')),((3,3,0),('P','C'))}
assert min(gaps)==F(1685757022745149,59116453961699088)
assert V[(0,0,0)]==F(42222189293875024646776690163383,138821594513174762290616991744)
print('PASS_STAGE143_DUAL_ONLY')
