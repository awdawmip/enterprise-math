"""Next first-Bellman-switch exact scan from Stage212 K212; candidate only."""
from fractions import Fraction as F
from functools import cache
from json import dumps
from pathlib import Path
PN=(3,1,20); P=tuple(F(x,24) for x in PN);N=14
K=F(626616,6055);H=F(86217082286260423009,1036550173712449536)
T=(10,3,1);Z=(14,0,0);ROOT=(0,0,0)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def child(s,j):return (s[0]+1,s[1]+(j==0),s[2]+(j==1))
def rho(s):return F(2**(s[1]+s[2]),3**s[1])
@cache
def bell(s):
  ac={'P':K*rho(s),'Q':K}
  if s[0]<N: ac['C']=1+sum(P[j]*bell(child(s,j))[0] for j in range(3))
  v=min(ac.values());return v,tuple(k for k,x in ac.items() if x==v)
@cache
def choose(s):
  if s==T:return 'P' # Stage212 high-alpha endpoint u=1
  if s==Z:return 'Q'
  val=bell(s)[1]; assert len(val)==1,(s,val)
  return val[0]
@cache
def triple(s): return via(s,choose(s))
def via(s,a):
  if a=='P':return F(0),rho(s),F(0)
  if a=='Q':return F(0),F(0),F(1)
  ch=[triple(child(s,j)) for j in range(3)]
  return tuple(F(k==0)+sum(P[j]*ch[j][k] for j in range(3)) for k in range(3))
def cost(c,k):return c[0]+k*(c[1]+c[2])
flat=[]; switching=[]; gapn=0
for s in states:
  old=choose(s)
  for alternative in ('P','Q')+(('C',) if s[0]<N else ()):
    if alternative==old:continue
    x=triple(s);y=via(s,alternative)
    dc=tuple(y[i]-x[i] for i in range(3))
    g=cost(dc,K);sl=dc[1]+dc[2]
    assert g>=0,(s,old,alternative,g)
    if g==0:flat.append((s,old,alternative,sl))
    else:
      gapn+=1
      if sl>0:switching.append((g/sl,s,old,alternative))
print('flat',flat)
assert {row[0] for row in flat}=={T,Z}
assert all(row[3]<=0 for row in flat)
step,state,old,new=min(switching)
Knext=K-step
@cache
def bel2(s):
  ac={'P':Knext*rho(s),'Q':Knext}
  if s[0]<N:ac['C']=1+sum(P[j]*bel2(child(s,j))[0] for j in range(3))
  v=min(ac.values());return v,tuple(k for k,x in ac.items() if x==v),tuple(x-v for x in ac.values() if x>v)
ties={str(s):list(bel2(s)[1]) for s in states if len(bel2(s)[1])>1}
gaps=[x for s in states for x in bel2(s)[2]]
a212=F(3740051857643324945,10517860061584293888)
Hnext=bel2(ROOT)[0]
assert len(states)==680
assert gapn==1238
assert len(gaps)==1238
assert Hnext==H+2*a212*(Knext-K)
assert Knext<K
assert str(Z) in ties and str(state) in ties
print('K212',K,'H212',H,'K213',Knext,'H213',Hnext)
print('switch',state,old,new,'step',step,'ties',ties,'gaps',len(gaps),'min',min(gaps))
print('CONTACT',Hnext==H+2*a212*(Knext-K),'slope margin',2*(K-Knext))
cert={'schema':'EM_STAGE213_DUAL_SCAN_V1','classification':'DUAL_CANDIDATE_ONLY','K212':str(K),'H212':str(H),'K213':str(Knext),'H213':str(Hnext),'first_switch_downstep':str(step),'new_tie':list(state),'old_action':old,'new_action':new,'ties':ties,'Bellman_states':len(states),'positive_gaps':len(gaps),'minimum_positive_gap':str(min(gaps)),'stage212_alpha_right':str(a212),'contact_identity':True}
Path('/mnt/data/em212_work/certificate213_dual.json').write_text(dumps(cert,indent=2)+'\n')
print('STAGE213_DUAL_SCAN_PASS')
