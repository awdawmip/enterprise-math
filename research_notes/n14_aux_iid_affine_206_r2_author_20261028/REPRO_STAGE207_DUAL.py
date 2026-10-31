"""Stage207 exact Bellman switch search after Stage206 right endpoint; dual candidate only."""
from fractions import Fraction as F
from functools import lru_cache
from json import dump
P=(F(3,24),F(1,24),F(20,24)); N=14; K=F(25155568056,213144883)
W=(5,0,1); Z=(14,0,0); S=(0,0,0)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def bell(s):
    actions={'P':K*lr(s),'Q':K}
    if s[0]<N:actions['C']=1+sum(P[i]*bell(child(s,i))[0] for i in range(3))
    v=min(actions.values());return v,tuple(a for a in actions if actions[a]==v)
@lru_cache(None)
def selected(s):
    if s==W:return 'Q'
    if s==Z:return 'Q'
    choices=bell(s)[1]
    assert len(choices)==1,(s,choices)
    return choices[0]
@lru_cache(None)
def coef(s):return byaction(s,selected(s))
def byaction(s,a):
    if a=='P':return F(0),lr(s),F(0)
    if a=='Q':return F(0),F(0),F(1)
    ch=[coef(child(s,i)) for i in range(3)]
    return tuple(F(j==0)+sum(P[i]*ch[i][j] for i in range(3)) for j in range(3))
def cost(c,k):return c[0]+k*(c[1]+c[2])
flat=[];cands=[]
for s in states:
    old=selected(s)
    for alt in ('P','Q')+(('C',) if s[0]<N else ()):
        if alt==old:continue
        ca,cb=coef(s),byaction(s,alt)
        d=tuple(cb[i]-ca[i] for i in range(3))
        gap=cost(d,K);slope=d[1]+d[2]
        assert gap>=0,(s,old,alt,gap)
        if gap==0:flat.append((s,old,alt,slope))
        elif slope>0:cands.append((gap/slope,s,old,alt))
assert {x[0] for x in flat}=={W,Z}
assert all(x[3]<=0 for x in flat),flat
step,s,old,new=min(cands)
newK=K-step
@lru_cache(None)
def bel2(s):
    ac={'P':newK*lr(s),'Q':newK}
    if s[0]<N:ac['C']=1+sum(P[i]*bel2(child(s,i))[0] for i in range(3))
    v=min(ac.values());return v,tuple(a for a in ac if ac[a]==v),tuple(x-v for x in ac.values() if x>v)
ties={str(s):list(bel2(s)[1]) for s in states if len(bel2(s)[1])>1}
pos=[x for s in states for x in bel2(s)[2]]
a206=F(413520058350802705,1168651117953810432)
H206=bell(S)[0];H207=bel2(S)[0]
print('K206',K,'H206',H206,'K207',newK,'H207',H207)
print('switch',s,old,'->',new,'step',step,'ties',ties,'positive',len(pos),'minimum',min(pos))
print('contact_check H207 = H206+2alpha206*(K207-K206)',H207==H206+2*a206*(newK-K))
assert H207==H206+2*a206*(newK-K)
assert newK<K
assert set(ties)=={str(Z),str(s)}
assert len(pos)==1238
with open('certificate207_dual.json','w') as f:
    dump({'schema':'EM_STAGE207_DUAL_SCAN_V1','status':'DUAL_CANDIDATE_ONLY',
      'K206':str(K),'H206':str(H206),'K207':str(newK),'H207':str(H207),
      'downstep':str(step),'first_state':list(s),'first_transition':[old,new],
      'ties':ties,'Bellman_states':len(states),'positive_gaps':len(pos),'minimum_positive_gap':str(min(pos)),
      'stage206_alpha_right':str(a206),'contact_identity':True,
      'global_read_snapshot':'a935c2321a618259b517ed476e73b3b0d81fca60'},f,indent=2)
    f.write('\n')
print('STAGE207_DERIVED_DUAL_SCAN_PASS')
