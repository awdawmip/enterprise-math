#!/usr/bin/env python3
"""External 14-step ternary IID: exact primal corner proof and next dual scanner.

All arithmetic Fraction, with an independent *unmerged ordered history* DFS
whose 24-adic integer P/Q path masses are never replaced by count aggregation.
This is an auxiliary stochastic model, not native X6 dynamics.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from dataclasses import dataclass
from typing import Tuple
import json
from pathlib import Path
P_N=(3,1,20);Q_N=(2,2,20);D=24;N=14
P=tuple(F(x,D) for x in P_N);Q=tuple(F(x,D) for x in Q_N)
ROOT=(0,0,0);Z=(N,0,0)
STATES=tuple((n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1))
assert len(STATES)==680
next_state=lambda s,j:(s[0]+1,s[1]+(j==0),s[2]+(j==1))
S=lambda q:f'{q.numerator}/{q.denominator}'

def bellman(K):
    @lru_cache(None)
    def opt(s):
        n,a,b=s
        actions={'P':K*F(2**(a+b),3**a),'Q':K}
        if n<N:actions['C']=1+sum(P[j]*opt(next_state(s,j))[0] for j in range(3))
        v=min(actions.values())
        return v,tuple(k for k,x in actions.items() if x==v),actions
    opt(ROOT)
    ties={s:opt(s)[1] for s in STATES if len(opt(s)[1])>1}
    gaps=[x-opt(s)[0] for s in STATES for x in opt(s)[2].values() if x>opt(s)[0]]
    return opt,ties,gaps

def primal(stage,K,T,T_action_0,T_action_1,alpha_left,val_left,expected_nodes=None,allow_zero_delta=False):
    opt,ties,gaps=bellman(K)
    assert set(ties)=={T,Z} and set(ties[T])=={T_action_0,T_action_1} and ties[Z]==('P','Q'),(T,ties)
    assert len(gaps)==1238 and min(gaps)>0,(len(gaps),min(gaps))
    # u=0 means first listed action; u=1 second. z=0 means P, z=1 Q.
    def action(s,u,z):
        if s==T:return (T_action_0,T_action_1)[u]
        if s==Z:return ('P','Q')[z]
        x=opt(s)[1];assert len(x)==1,(s,x)
        return x[0]
    @lru_cache(None)
    def suffix(s,u,z):
        a=action(s,u,z)
        if a!='C':return (F(a=='Q'),F(a=='P'),F(0),F(0))
        children=[suffix(next_state(s,j),u,z) for j in range(3)]
        return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*children[j][k] for j in range(3)) for k in range(4))
    def independent_dfs(u,z):
        stack=[(0,0,0,1,1)];masses=[0]*4;visits=0
        while stack:
            n,a,b,p,q=stack.pop();visits+=1
            c=action((n,a,b),u,z)
            if c=='C':
                for j in range(3):stack.append((n+1,a+(j==0),b+(j==1),p*P_N[j],q*Q_N[j]))
            else:
                mul=D**(N-n)
                if c=='P':masses[1]+=q*mul
                else:masses[0]+=p*mul
                masses[2]+=n*p*mul;masses[3]+=n*q*mul
        return tuple(F(x,D**N) for x in masses),visits
    corner={};nodes={}
    for u,z in product((0,1),repeat=2):
        x=suffix(ROOT,u,z)
        y,v=independent_dfs(u,z)
        assert x==y,(u,z,x,y)
        corner[f'{u}{z}']=x;nodes[f'{u}{z}']=v
    if expected_nodes is not None:assert sum(nodes.values())==expected_nodes
    vecadd=lambda a,b:tuple(x+y for x,y in zip(a,b))
    vecsub=lambda a,b:tuple(x-y for x,y in zip(a,b))
    o=corner['00'];du=vecsub(corner['10'],o);dz=vecsub(corner['01'],o)
    mixed=vecsub(vecsub(corner['11'],corner['10']),dz)
    assert mixed==(F(0),)*4,('nonlinear coin',mixed)
    # symbolic proof mixed=0 from monotone observation counts: T has positive a or b;
    # Z=(14,0,0) has zero a and b, and Z is terminal; hence no path reaches both.
    assert (T[1]>0 or T[2]>0) and Z[1]==Z[2]==0 and Z[0]==N
    denom=dz[0]-dz[1]
    assert denom!=0
    z0=-(o[0]-o[1])/denom;zs=-(du[0]-du[1])/denom
    assert 0<=z0<=1 and 0<=z0+zs<=1,(z0,zs)
    def mix(u):return tuple(o[k]+u*du[k]+(z0+zs*u)*dz[k] for k in range(4))
    L,R=mix(F(0)),mix(F(1));assert L[0]==L[1] and R[0]==R[1]
    assert L[0]==alpha_left and L[2]==val_left,(stage,'contact-left',L,alpha_left,val_left)
    assert (R[0]>L[0] or allow_zero_delta and R[0]==L[0]) and L[2]>L[3] and R[2]>R[3]
    assert L[2]+2*K*L[0]==R[2]+2*K*R[0]==opt(ROOT)[0]
    report={
      'stage':stage,'model':{'N':N,'P':P_N,'Q':Q_N,'denominator':D,'policy':'all randomized ordered-history stopping policies'},
      'K':S(K),'H':S(opt(ROOT)[0]),'T':T,'T_action_u0':T_action_0,'T_action_u1':T_action_1,
      'Z':Z,'Z_action_z0':'P','Z_action_z1':'Q','corners':{k:[S(v) for v in obs] for k,obs in corner.items()},
      'dfs_nodes':nodes,'total_dfs_nodes':sum(nodes.values()),'states':len(STATES),
      'positive_gaps':len(gaps),'min_positive_gap':S(min(gaps)),
      'du':[S(x) for x in du],'dz':[S(x) for x in dz],
      'mixed':[S(x) for x in mixed],'z0':S(z0),'zs':S(zs),'z1':S(z0+zs),
      'alpha_left':S(L[0]),'alpha_right':S(R[0]),'delta':S(R[0]-L[0]),
      'value_left':S(L[2]),'value_right':S(R[2]),'slope':S(-2*K),
      'time_margin_left':S(L[2]-L[3]),'time_margin_right':S(R[2]-R[3]),
      'eP_eQ_along_curve':'equal for each real u in [0,1]',
      'proof_status':'AUTHOR_EXACT_NOT_INDEPENDENTLY_REVIEWED', 'is_nontrivial_interval':bool(R[0]>L[0])
    }
    print('STAGE',stage,'EXACT_PASS',report['total_dfs_nodes'],'DELTA',report['delta'], 'K',report['K'])
    print('ALPHA_RIGHT',report['alpha_right'],'VALUE_RIGHT',report['value_right'])
    return report

# Use affine functions (A,B), so A+B*K. At K0, tie select the action
# with largest K-derivative for strictly smaller K. Scan first crossing.
def next_dual(K0):
    def add(a,b):return a[0]+b[0],a[1]+b[1]
    def mul(k,a):return k*a[0],k*a[1]
    @lru_cache(None)
    def fit(s):
        n,a,b=s
        actions={'P':(F(0),F(2**(a+b),3**a)),'Q':(F(0),F(1))}
        if n<N:
            v=(F(1),F(0))
            for j in range(3):v=add(v,mul(P[j],fit(next_state(s,j))[0]))
            actions['C']=v
        k=min(actions,key=lambda act:(actions[act][0]+K0*actions[act][1],-actions[act][1]))
        return actions[k],k,actions
    fit(ROOT)
    thresholds=[]
    for s in STATES:
        val,choice,acts=fit(s)
        for k,(a,b) in acts.items():
            diff_a=a-val[0];diff_b=b-val[1]
            now=diff_a+K0*diff_b
            assert now>=0,(s,k,choice,now)
            if now==0:continue
            if diff_b>0:
                cross=-diff_a/diff_b
                if 0<cross<K0:thresholds.append((cross,s,k,choice))
    assert thresholds
    Knew=max(t[0] for t in thresholds)
    opt,ties,gaps=bellman(Knew)
    winner=[{'state':s,'action':k,'old_action':c} for cross,s,k,c in thresholds if cross==Knew]
    assert len(gaps)>0
    result={'K':S(Knew),'H':S(opt(ROOT)[0]),'ties':{str(s):list(a) for s,a in ties.items()},
            'events':winner,'states':len(STATES),'strict_gaps':len(gaps),'min_gap':S(min(gaps)),
            'method':'exact global first breakpoint below K0 using affine suffix Bellman support'}
    return result



def stage229_polytope(left_alpha, left_value):
    """Exact four-tie corner hull at K=72, with all-history Markovization lemma.

    At every count-state, P/Q prefix likelihood ratio is constant. Therefore
    arbitrary history-dependent action probabilities can be Markovized while
    preserving both P/Q occupancies, expected time and errors. Every Markovized
    tie-only observation is in the convex hull of 2^4 deterministic corners.
    """
    from itertools import combinations
    K=F(72)
    opt,ties,gaps=bellman(K)
    T=((12,1,0),(13,1,0),(13,1,1))
    assert set(ties)==set(T)|{Z}
    optabove=bellman(K+F(1,10**5))[0]
    pairs={t:(optabove(t)[1][0],next(a for a in ties[t] if a!=optabove(t)[1][0])) for t in T}
    assert pairs=={(12,1,0):('C','P'),(13,1,0):('C','P'),(13,1,1):('C','Q')}
    @lru_cache(None)
    def action(s,bits):
        if s in pairs:return pairs[s][bits[T.index(s)]]
        if s==Z:return ('P','Q')[bits[3]]
        a=opt(s)[1];assert len(a)==1,(s,a)
        return a[0]
    @lru_cache(None)
    def suffix(s,bits):
        a=action(s,bits)
        if a!='C':return (F(a=='Q'),F(a=='P'),F(0),F(0))
        kids=[suffix(next_state(s,j),bits) for j in range(3)]
        return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*kids[j][k] for j in range(3)) for k in range(4))
    def dfs(bits):
        stack=[(0,0,0,1,1)];mass=[0]*4;vis=0
        while stack:
            n,a,b,p,q=stack.pop();vis+=1
            c=action((n,a,b),bits)
            if c=='C':
                for j in range(3):stack.append((n+1,a+(j==0),b+(j==1),p*P_N[j],q*Q_N[j]))
            else:
                mul=D**(N-n)
                mass[1 if c=='P' else 0]+=(q if c=='P' else p)*mul
                mass[2]+=n*p*mul;mass[3]+=n*q*mul
        return tuple(F(x,D**N) for x in mass),vis
    corners={};visits={}
    for bits in product((0,1),repeat=4):
        x=suffix(ROOT,bits)
        y,n=dfs(bits)
        assert x==y and x[2]+K*(x[0]+x[1])==opt(ROOT)[0]
        corners[bits]=x;visits[bits]=n
    assert len(corners)==16 and len(gaps)==1236 # 4 ties yield 1236 strictly positive alternatives
    assert all(v[2]>v[3] for v in corners.values())
    feasible=[]
    for bits,v in corners.items():
        if v[0]==v[1]:feasible.append((v[0],(bits,),(F(1),),v))
    for b1,b2 in combinations(corners,2):
        x,y=corners[b1],corners[b2]
        d1=x[0]-x[1];d2=y[0]-y[1]
        if d1*d2>=0:continue
        w=-d2/(d1-d2)
        assert 0<w<1
        v=tuple(w*x[i]+(1-w)*y[i] for i in range(4))
        assert v[0]==v[1]
        feasible.append((v[0],(b1,b2),(w,1-w),v))
    lo=min(feasible,key=lambda q:q[0]);hi=max(feasible,key=lambda q:q[0])
    assert len(feasible)==64
    assert lo[0]==left_alpha and lo[3][2]==left_value
    assert hi[0]==F(2406332872015,6687075336192)
    assert hi[0]>left_alpha and hi[3][2]>hi[3][3]
    assert hi[3][2]+2*K*hi[0]==opt(ROOT)[0]
    assert lo[1]==((0,0,0,0),(0,0,0,1))
    assert hi[1]==((1,1,1,0),(1,1,1,1))
    report={
      'stage':229,'model':{'N':N,'P':P_N,'Q':Q_N,'denominator':D},
      'K':S(K),'H':S(opt(ROOT)[0]),'tie_pairs':{str(t):list(v) for t,v in pairs.items()},
      'Z_actions':['P','Q'],'positive_gaps':len(gaps),'min_gap':S(min(gaps)),
      'state_count':len(STATES),'corners':{''.join(map(str,k)):[S(z) for z in v] for k,v in corners.items()},
      'dfs_nodes':{''.join(map(str,k)):visits[k] for k in corners},
      'total_dfs_nodes':sum(visits.values()),
      'all_corner_Ptime_gt_Qtime':True,
      'equal_error_vertices':len(feasible),
      'left_witness_bits':[''.join(map(str,k)) for k in lo[1]],
      'left_witness_weights':[S(w) for w in lo[2]],
      'right_witness_bits':[''.join(map(str,k)) for k in hi[1]],
      'right_witness_weights':[S(w) for w in hi[2]],
      'alpha_left':S(left_alpha),'alpha_right':S(hi[0]),
      'delta':S(hi[0]-left_alpha),'value_left':S(left_value),
      'value_right':S(hi[3][2]),
      'P_minus_Q_time_left':S(lo[3][2]-lo[3][3]),
      'P_minus_Q_time_right':S(hi[3][2]-hi[3][3]),
      'max_observation':[S(x) for x in hi[3]],
      'algorithm':'exact 16 corner DP/integer ordered DFS; 64 opposite-sign edges LP at equal errors',
      'classification':'AUTHOR_EXACT_NOT_ADMITTED'
    }
    print('STAGE229_EXACT_POLYTOPE_PASS',sum(visits.values()),'vertices',len(feasible),'delta',report['delta'])
    return report


def main():
    K228=F(22177458672696,263038955731)
    alpha227=F(938194997485383047,2629465015396073472)
    V227=F(511508195322329735,54780521154084864)
    r228=primal(228,K228,(4,2,2),'C','Q',alpha227,V227)
    assert r228['total_dfs_nodes']==18472
    K=K228
    null=[]
    null_ties={1:(8,4,3),2:(7,4,3),3:(11,6,4)}
    for n in range(1,4):
        q=next_dual(K)
        k=F(q['K']);t=null_ties[n]
        assert q['ties']=={str(t):['Q','C'],str(Z):['P','Q']}
        r=primal('NULL_'+str(n),k,t,'C','Q',F(r228['alpha_right']),F(r228['value_right']),allow_zero_delta=True)
        assert r['delta']=='0/1' and r['du']==['0/1']*4
        assert F(q['H'])==F(r228['H'])+2*F(r228['alpha_right'])*(k-K228)
        # The null tie state cannot be reached under any optimal root policy.
        opt,ties,_=bellman(k)
        reachable={ROOT}
        for s in STATES:
            if s not in reachable:continue
            if 'C' in opt(s)[1]:
                for j in range(3):reachable.add(next_state(s,j))
        assert t not in reachable and len(reachable)==115
        null.append({'K':S(k),'state':t,'root_reachable':False,
                     'delta':r['delta'],'total_dfs_nodes':r['total_dfs_nodes'],
                     'four_corner_certificate':r})
        K=k
    assert next_dual(K)['K']=='72/1'
    r229=stage229_polytope(F(r228['alpha_right']),F(r228['value_right']))
    H72=F(r229['H'])
    assert H72==F(r228['H'])+2*F(r228['alpha_right'])*(F(72)-K228)
    q230=next_dual(F(72))
    assert q230['K']=='43416/607' and q230['ties']=={str((11,1,0)):['P','C'],str(Z):['P','Q']}
    assert F(q230['H'])==H72+2*F(r229['alpha_right'])*(F(q230['K'])-F(72))
    r230=primal(230,F(q230['K']),(11,1,0),'C','P',F(r229['alpha_right']),F(r229['value_right']))
    assert r230['total_dfs_nodes']==16210
    q231=next_dual(F(q230['K']))
    assert F(q231['H'])==F(r230['H'])+2*F(r230['alpha_right'])*(F(q231['K'])-F(q230['K']))
    assert q231['ties']=={str((10,1,0)):['P','C'],str(Z):['P','Q']}
    outputs={'certificate228.json':r228,'null_pivots_228_to_229.json':null,
             'certificate229_polytope.json':r229,'certificate230.json':r230,
             'certificate231_dual.json':q231}
    here=Path(__file__).resolve().parent
    for name,obj in outputs.items():
        (here/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('STAGE228_230_AUTHOR_EXACT_PASS',
          r228['total_dfs_nodes']+sum(x['total_dfs_nodes'] for x in null)+r229['total_dfs_nodes']+r230['total_dfs_nodes'])
    print('STAGE231_DUAL_ONLY',q231['K'],q231['ties'])

if __name__=='__main__':
    main()
