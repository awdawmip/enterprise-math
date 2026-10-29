#!/usr/bin/env python3
"""Stage273 exact Bellman/entire-ordered-history proof audit, Python 3 stdlib only.
Frozen predecessor: Stage272, immutable Git commit 4d077327bc4607ef9c59b50f1ff6610580d3fb4c.
External ternary IID experiment, NOT P000 native X6, and NOT Source admission.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product

P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
N=12
Z=[(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
root=(0,0,0); T=(0,0,5); S2=(1,2,5); S3=(1,2,6)

def nxt(s,k):
    a=list(s); a[k]+=1; return tuple(a)
def mass(s):
    i,j,k=s
    return P[0]**i*P[1]**j*P[2]**k, Q[0]**i*Q[1]**j*Q[2]**k

def bellman(lp,lq):
    val={}; choices={}; ties={}; gaps=[]
    for s in reversed(Z):
        p,q=mass(s)
        opts={'P':lq*q,'Q':lp*p}
        if sum(s)<N:
            opts['C']=q+sum(val[nxt(s,k)] for k in range(3))
        best=min(opts.values()); val[s]=best; choices[s]=opts
        eq=tuple(a for a in opts if opts[a]==best)
        if len(eq)>1: ties[s]=eq
        gaps.extend(cost-best for cost in opts.values() if cost>best)
    return val,choices,ties,gaps

def flow(policy):
    """Independent count-state integer multiplicity propagation."""
    visits=defaultdict(int); visits[root]=1
    obs=[F(0)]*4; mass_end=[F(0),F(0)]
    for s in Z:
        count=visits[s]
        if count==0: continue
        p,q=mass(s); choice=policy[s]
        if choice=='P': obs[1]+=count*q
        elif choice=='Q': obs[0]+=count*p
        else:
            assert choice=='C' and sum(s)<N
            obs[2]+=count*p; obs[3]+=count*q
            for k in range(3): visits[nxt(s,k)]+=count
        if choice!='C':
            mass_end[0]+=count*p; mass_end[1]+=count*q
    assert mass_end==[F(1),F(1)]
    return tuple(obs),visits

def ordered(policy):
    """Unmerged word tree: no count multiplicity shortcut for likelihood propagation."""
    obs=[F(0)]*4; masses=[F(0),F(0)]
    nodes=0; leaves=0; reached_S2=0; via_T=0
    def go(word,pp,qq,passed_T):
        nonlocal nodes,leaves,reached_S2,via_T
        nodes+=1
        s=(word.count(0),word.count(1),word.count(2))
        if s==S2:
            reached_S2+=1
            via_T+=int(passed_T)
        a=policy[s]
        if a=='P':obs[1]+=qq
        elif a=='Q':obs[0]+=pp
        else:
            assert a=='C' and len(word)<N
            obs[2]+=pp;obs[3]+=qq
            for k in range(3):
                go(word+(k,),pp*P[k],qq*Q[k],passed_T or s==T)
        if a!='C':
            masses[0]+=pp;masses[1]+=qq;leaves+=1
    go((),F(1),F(1),False)
    assert masses==[F(1),F(1)]
    return tuple(obs),nodes,leaves,reached_S2,via_T

def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def vecsub(b,a): return tuple(b[i]-a[i] for i in range(4))

def derive_dual(g,h,k):
    # Solve lp*d_eP + lq*d_eQ + d_tQ = 0 for both independent legal policy edges.
    x=vecsub(h,g); y=vecsub(k,g)
    det=x[0]*y[1]-x[1]*y[0]
    assert det!=0
    lp=(-x[3]*y[1]+y[3]*x[1])/det
    lq=(-x[0]*y[3]+y[0]*x[3])/det
    assert lp>0 and lq>0
    return lp,lq,det

# Exact predecessor independently checked policy observers Gplus, Hplus and K.
Gprev=tuple(map(F,('187155450011/2641807540224','219610483345/278628139008',
    '13822107249481/2972033482752','127792519715/23219011584')))
Hprev=tuple(map(F,('211509050011/2641807540224','212768333345/278628139008',
    '5091349349827/990677827584','140840869715/23219011584')))
Kprev=tuple(map(F,('557277756283/7925422620672','4579991515/5804752896',
    '13841471030731/2972033482752','64078877045/11609505792')))
lp,lq,det=derive_dual(Gprev,Hprev,Kprev)
assert (lp,lq)==(F(326994117632,2080594473),F(56789098740,693531491))
v,cs,ties,gap=bellman(lp,lq)
H=v[root]
assert H==F(1307211413240495165209,16103115723397791744)
assert len(Z)==455 and sum(len(costs) for costs in cs.values())==1274
assert ties=={T:('P','C'),S2:('Q','C')}
assert len(gap)==817 and min(gap)==F(626146193,2748265083459889790976)

baseline={s:next(a for a in cs[s] if cs[s][a]==v[s]) for s in Z}
policies={};obs={};counts={};nodes=leaves=0
for r,u in product((0,1),repeat=2):
    pol=baseline.copy();pol[T]='C' if r else 'P';pol[S2]='C' if u else 'Q'
    policies[r,u]=pol
    ob,cnt=flow(pol)
    other,n,l,reached,via=ordered(pol)
    assert ob==other and cnt[T]==1 and cnt[S2]==reached==55+r
    assert via==r  # exactly one S2 ordered prefix passes through optional T
    assert lp*ob[0]+lq*ob[1]+ob[3]==H
    assert ob[3]>ob[2]
    assert all(cs[s][pol[s]]==v[s] for s in Z)
    obs[r,u]=ob;counts[r,u]=cnt
    nodes+=n;leaves+=l
G,K,Hplus,J=obs[0,0],obs[0,1],obs[1,0],obs[1,1]
assert (G,Hplus,K)==(Gprev,Hprev,Kprev)
assert vecsub(J,Hplus)==tuple(F(56,55)*x for x in vecsub(K,G))
assert all(obs[x][3]>obs[x][2] for x in obs)

# Entire equality family: T coin r in [0,1]; 55+r unit-provenance S2 histories;
# their total continuation weight k in [0,55+r].  At each S2 word the
# source likelihood and suffix law are identical. This is an exact affine
# two-parameter image of a trapezoid, not an unjustified independent-coin box.
# Its four vertices are (0,0),(1,0),(1,56),(0,55).
quad=[G,Hplus,J,K]
turns=[orient(quad[i],quad[(i+1)%4],quad[(i+2)%4]) for i in range(4)]
assert all(z<0 for z in turns)
area=abs(sum(quad[i][0]*quad[(i+1)%4][1]-quad[(i+1)%4][0]*quad[i][1]
             for i in range(4)))/2
assert area==F(250592433271484375,46005119909369701466112)
old_G=tuple(map(F,('1129087690691/15850845241344','146299619105/185752092672')))
assert orient(G,Hplus,old_G)>0
assert orient(G,Hplus,K)<0 and orient(G,Hplus,J)<0

# Strict interior point: predecessor 49% Gplus + 49% Hplus + 2% K.
a=F(298591185079,3962711310336);b=F(48058313785,61917364224)
point=tuple(F(49,100)*G[i]+F(49,100)*Hplus[i]+F(1,50)*K[i] for i in range(4))
assert (point[0],point[1])==(a,b)
assert point[2]==F(807441417617,165112971264)
assert point[3]==F(89462343935,15479341056)
assert point[3]>point[2]
assert H-lp*a-lq*b==point[3]
assert all(orient(quad[i],quad[(i+1)%4],point)<0 for i in range(4))

# Genuine next exterior witness across the K-J edge, with 80 reached S3 words.
nextpol=policies[0,1].copy(); assert nextpol[S3]=='Q'
assert counts[0,1][S3]==80
nextpol[S3]='C'
M,newcnt=flow(nextpol)
Md,nn,nl,ns,nv=ordered(nextpol)
assert M==Md and M[3]>M[2]
assert M==tuple(map(F,('183995918761/2641807540224','13758880795/17414258688',
    '13862981030731/2972033482752','21429209015/3869835264')))
assert lp*M[0]+lq*M[1]+M[3]-H==F(124418778359375,62902795794522624)>0
external=tuple(F(49,100)*K[i]+F(49,100)*J[i]+F(1,50)*M[i] for i in range(4))
assert external==tuple(map(F,('131763207049/1761205026816',
  '865980121505/1114512556032','3234116608093/660451885056',
  '538252197985/92876046336')))
assert orient(K,J,G)>0 and orient(K,J,external)==F(-8809426630859375,69007679864054552199168)<0
assert external[3]>external[2]

print('STAGE273_EXACT_ALL_REAL_FACE_PASS')
print('dual_lambda_P',lp,'dual_lambda_Q',lq,'root_H',H)
print('states',len(Z),'legal_actions',sum(map(len,cs.values())),
      'strict_positive_action_gaps',len(gap),'minimum_gap',min(gap),'tie_states',ties)
for key,label in (((0,0),'Gplus'),((1,0),'Hplus'),((1,1),'J'),((0,1),'K')):
    print(label,','.join(map(str,obs[key])),'S2_reached',counts[key][S2])
print('trapezoid_S2_history_counts',55,56,'T_count',1,'KJ_ratio',F(56,55))
print('R273_area',area,'strict_convex_turns',','.join(map(str,turns)))
print('shared_R272_edge',orient(G,Hplus,old_G),orient(G,Hplus,K))
print('witness_a_b_tP_tQ',','.join(map(str,point)),'optimum',point[3],
      'time_gap',point[3]-point[2])
print('four_vertex_ordered_DFS_nodes_leaves',nodes,leaves,'all_P_Q_end_mass_one',True)
print('STAGE274_FEASIBLE_EXTERIOR_PASS',','.join(map(str,external)),
      'M_lagrangian_slack',lp*M[0]+lq*M[1]+M[3]-H,
      'outer_orientation',orient(K,J,external),'M_ordered_nodes_leaves',nn,nl)
