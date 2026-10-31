"""Stage217 candidate exact dual first-switch scan from Stage216 K; dual only."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14;PN=(3,1,20);P=tuple(F(x,24) for x in PN)
K=F(908057789003279736,9275758227422879);H=F(10060422269700525971327026167740407,127032717449378935977323595300864)
T=(1,0,1);Z=(14,0,0);S=(0,0,0)
A216=F(7504698785088745369,21035720123168587776)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def nxt(s,j):return s[0]+1,s[1]+(j==0),s[2]+(j==1)
def rho(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def bell(s):
  ac={'P':K*rho(s),'Q':K}
  if s[0]<N:ac['C']=1+sum(P[j]*bell(nxt(s,j))[0] for j in range(3))
  v=min(ac.values());return v,tuple(k for k,x in ac.items() if x==v)
@lru_cache(None)
def choose(s):
  if s==T:return 'Q' # Stage216 high-alpha endpoint u=1
  if s==Z:return 'Q'
  acts=bell(s)[1];assert len(acts)==1,(s,acts)
  return acts[0]
@lru_cache(None)
def triple(s):return via(s,choose(s))
def via(s,a):
  if a=='P':return F(0),rho(s),F(0)
  if a=='Q':return F(0),F(0),F(1)
  ch=[triple(nxt(s,j)) for j in range(3)]
  return tuple(F(k==0)+sum(P[j]*ch[j][k] for j in range(3)) for k in range(3))
def cost(v,k):return v[0]+k*(v[1]+v[2])
flat=[];switching=[];positive=0
for s in states:
  old=choose(s)
  for new in ('P','Q')+(('C',) if s[0]<N else ()):
    if new==old:continue
    x=triple(s);y=via(s,new)
    dc=tuple(y[i]-x[i] for i in range(3))
    g=cost(dc,K);sl=dc[1]+dc[2]
    assert g>=0,(s,old,new,g)
    if g==0:flat.append((s,old,new,sl))
    else:
      positive+=1
      if sl>0:switching.append((g/sl,s,old,new))
assert {a[0] for a in flat}=={T,Z},flat
assert all(row[3]<=0 for row in flat),flat
step,state,old,new=min(switching)
Knext=K-step
@lru_cache(None)
def bellnext(s):
  ac={'P':Knext*rho(s),'Q':Knext}
  if s[0]<N:ac['C']=1+sum(P[j]*bellnext(nxt(s,j))[0] for j in range(3))
  v=min(ac.values());return v,tuple(a for a,x in ac.items() if x==v),tuple(x-v for x in ac.values() if x>v)
Hnext=bellnext(S)[0]
ties={str(s):list(bellnext(s)[1]) for s in states if len(bellnext(s)[1])>1}
gaps=[x for s in states for x in bellnext(s)[2]]
assert positive==1238 and len(gaps)==1238 and len(states)==680
assert Hnext==H+2*A216*(Knext-K),(Hnext,H+2*A216*(Knext-K))
assert Knext<K
assert str(Z) in ties and str(state) in ties
cert={
 'schema':'EM_STAGE217_DUAL_SCAN_V1','classification':'DUAL_CANDIDATE_ONLY',
 'K216':str(K),'H216':str(H),'alpha216':str(A216),
 'K217':str(Knext),'H217':str(Hnext),'first_switch_downstep':str(step),
 'new_tie':list(state),'old_action':old,'new_action':new,'ties':ties,
 'Bellman_states':len(states),'positive_gaps':len(gaps),'minimum_positive_gap':str(min(gaps)),
 'contact_identity':True,'fixed_Stage216_support_right_margin_slope':str(2*(K-Knext))
}
Path(__file__).with_name('certificate217_dual.json').write_text(json.dumps(cert,indent=2)+'\n')
print('STAGE217_DUAL_SCAN_PASS')
print('K217',Knext,'H217',Hnext,'state',state,old,'->',new,'downstep',step)
print('ties',ties,'gaps',len(gaps),'min',min(gaps))
print('slope margin',2*(K-Knext))
