#!/usr/bin/env python3
"""Stage267: reproducible exact N=12 ternary-IID Bellman/ordered-history certificate.
All mathematical arithmetic is fractions.Fraction, no floating point or external packages.
The state-count DP and ordered-path DFS independently form the four observers.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

N=12
PP=(F(1,8),F(1,24),F(5,6))
QQ=(F(1,12),F(1,12),F(5,6))
LP=F(9423522781990912,69612694876029)
LQ=F(1710217803414276,23204231625343)
A=F(3776724593681,49533891379200)
B=F(1799211749497,2321901158400)
T1=(0,0,5)
T2=(1,2,0)
STATES=[(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
assert len(STATES)==455


def child(s,k):
    return tuple(s[t]+int(k==t) for t in range(3))


def pq(s):
    i,j,k=s
    return PP[0]**i*PP[1]**j*PP[2]**k,QQ[0]**i*QQ[1]**j*QQ[2]**k


def exact_bellman():
    val={};costs={};gaps=[];ties={};numactions=0
    for s in reversed(STATES):
        p,q=pq(s)
        a={'P':LQ*q,'Q':LP*p}
        if sum(s)<N:
            a['C']=q+sum(val[child(s,k)] for k in range(3))
        v=min(a.values());val[s]=v;costs[s]=a
        best=tuple(x for x in a if a[x]==v)
        if len(best)>1:ties[s]=best
        assert all(z>=v for z in a.values())
        gaps += [z-v for z in a.values() if z>v]
        numactions+=len(a)
    assert numactions==1274
    assert ties=={T1:('P','C'),T2:('Q','C')},ties
    assert len(gaps)==817
    assert val[(0,0,0)]==F(616068176019744340149581,8418426920416535390208)
    assert min(gaps)==F(3670356301907,22987917777350752638861312)
    return val,costs,ties,gaps,numactions


def policy_for(val,costs,rbit,ubit):
    p={s:next(a for a,v in costs[s].items() if v==val[s]) for s in STATES}
    p[T1]='C' if rbit else 'P'
    p[T2]='C' if ubit else 'Q'
    assert all(costs[s][a]==val[s] for s,a in p.items())
    return p


def by_count_flow(policy):
    # Independent count-state path-multiplicity propagation: ONE unit is ONE ordered prefix.
    active=defaultdict(int);active[(0,0,0)]=1
    eP=eQ=tP=tQ=F(0)
    for s in STATES:
        m=active[s]
        if not m:continue
        p,q=pq(s)
        d=policy[s]
        if d=='P':eQ+=m*q
        elif d=='Q':eP+=m*p
        else:
            assert d=='C' and sum(s)<N
            tP+=m*p;tQ+=m*q
            for k in range(3):active[child(s,k)]+=m
    return (eP,eQ,tP,tQ),active


def by_ordered_history(policy):
    # Distinct verifier: enumerates *actual ordered histories* with source mass updated
    # multiplicatively on every symbol. Never uses multiplicity/count-state flow.
    result=[F(0) for _ in range(4)]
    normalized=[F(0),F(0)]
    nodes=leaves=0
    def visit(h,mp,mq):
        nonlocal nodes,leaves
        nodes+=1
        s=(h.count(0),h.count(1),h.count(2))
        d=policy[s]
        if d=='P':
            result[1]+=mq;normalized[0]+=mp;normalized[1]+=mq;leaves+=1
        elif d=='Q':
            result[0]+=mp;normalized[0]+=mp;normalized[1]+=mq;leaves+=1
        else:
            assert d=='C' and len(h)<N
            result[2]+=mp;result[3]+=mq
            for k in range(3):visit(h+(k,),mp*PP[k],mq*QQ[k])
    visit((),F(1),F(1))
    assert normalized==[F(1),F(1)],normalized
    return tuple(result),nodes,leaves


def orient(x,y,z):
    return (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])


def solve2(d1,d2,target):
    det=orient((F(0),F(0)),d1,d2)
    assert det!=0
    r=(target[0]*d2[1]-target[1]*d2[0])/det
    u=(d1[0]*target[1]-d1[1]*target[0])/det
    return r,u


def main():
    val,costs,ties,gaps,numactions=exact_bellman()
    observations={};node_total=leaf_total=0;paths={}
    for rb,ub in product((0,1),repeat=2):
        pol=policy_for(val,costs,rb,ub)
        obs,m=by_count_flow(pol)
        ob2,nn,ll=by_ordered_history(pol)
        assert ob2==obs
        assert m[T1]==1 and m[T2]==1
        assert obs[3]>obs[2]
        assert LP*obs[0]+LQ*obs[1]+obs[3]==val[(0,0,0)]
        observations[(rb,ub)]=obs
        paths[(rb,ub)]=(nn,ll)
        node_total+=nn;leaf_total+=ll
    J5,L5,J6,L6=(observations[(0,0)],observations[(0,1)],observations[(1,0)],observations[(1,1)])
    assert J5==tuple(map(F,('555154589/7739670528','3425906045/4353564672','13459124989/2902376448','330916723/60466176')))
    assert J6==tuple(map(F,('1253006053/15479341056','4425329935/5804752896','9918023951/1934917632','2919174409/483729408')))
    assert L5==tuple(map(F,('378878551937/5283615080448','146176716655/185752092672','27566628769787/5944066965504','254184258235/46438023168')))
    assert L6==tuple(map(F,('15836509331/195689447424','424845849965/557256278016','10156836789929/1981355655168','280280958235/46438023168')))
    assert tuple(L5[i]-J5[i] for i in range(4))==tuple(L6[i]-J6[i] for i in range(4))
    d1=(J6[0]-J5[0],J6[1]-J5[1]);d2=(L5[0]-J5[0],L5[1]-J5[1]);tgt=(A-J5[0],B-J5[1])
    area=abs(orient(J5,J6,L5))
    assert area==F(72513223829196875,276030719456218208796672)
    assert orient(J5,J6,L5)<0
    I5=(F(1763120017,23219011584),F(6802983965,8707129344))
    assert orient(J5,J6,I5)>0
    assert orient(J5,J6,(A,B))==F(-47704025643875,11501279977342425366528)
    r,u=solve2(d1,d2,tgt)
    w=(1-r-u,r,u)
    assert w==(F(14334589146395604771,29005289531678750000),F(14212741739101945229,29005289531678750000),F(9159172923624,580105790633575))
    assert all(x>0 for x in w) and sum(w)==1 and 0<r<1 and 0<u<1
    primal=tuple(sum(wk*obs[i] for wk,obs in zip(w,(J5,J6,L5))) for i in range(4))
    v=val[(0,0,0)]-LP*A-LQ*B
    assert primal[:2]==(A,B)
    assert primal[3]-primal[2]==F(125208080113635537589672243,143674486108442203992883200)>0
    assert primal[3]==v==F(5161630421173538432550553,897965538177763774955520)
    old_ub=F(3336652788737,580475289600)
    assert old_ub>v
    # Stage268 handoff: independently executable exact strictly-outside feasible point.
    wpol=policy_for(val,costs,0,1)  # L5
    assert wpol[(3,3,5)]=='Q'
    wpol[(3,3,5)]='C'
    W,wmass=by_count_flow(wpol)
    Wpath,Wnodes,Wleaves=by_ordered_history(wpol)
    assert Wpath==W and wmass[(3,3,5)]==21
    assert W==tuple(map(F,('378877764437/5283615080448','146176760405/185752092672','27566635857287/5944066965504','254184389485/46438023168')))
    future=tuple(F(49,100)*L5[i]+F(49,100)*L6[i]+F(1,50)*W[i] for i in range(4))
    assert future[0]==F(134248354729,1761205026816)
    assert future[1]==F(215912422795,278628139008)
    assert orient(L5,L6,J5)>0 and orient(L5,L6,future)<0
    assert future[3]>future[2]
    assert LP*future[0]+LQ*future[1]+future[3]-val[(0,0,0)]==F(32602722110875,179593107635552754991104)>0
    print('STAGE267_EXACT_ALL_REAL_FACE_PASS')
    print('states',len(STATES),'legal_action_costs',numactions,'strict_positive_gaps',len(gaps),'tie_states',ties)
    print('minimum_positive_gap',min(gaps))
    print('lambdaP',LP,'lambdaQ',LQ,'thetaP',0,'thetaQ',1,'H',val[(0,0,0)])
    print('a267',A,'b267',B,'V267',v,'decimal',format(float(v),'.15f'))
    for key in ((0,0),(1,0),(1,1),(0,1)):
        print('vertex',key,','.join(map(str,observations[key])),'ordered_nodes_leaves',paths[key])
    print('face_area',area,'edge_shared_J5_J6',True,'all_real_iff_from_Bellman_compactness',True)
    print('mixture_J5_J6_L5',','.join(map(str,w)),'tQ_minus_tP',primal[3]-primal[2])
    print('full_history_nodes',node_total,'leaves',leaf_total,'all_PQ_terminal_masses_exactly_one',True)
    print('prior_witness_upper_bound',old_ub,'strict_improvement',old_ub-v)
    print('stage268_W',','.join(map(str,W)),'ordered_nodes_leaves',(Wnodes,Wleaves),'reaching_3_3_5_paths',wmass[(3,3,5)])
    print('stage268_feasible_caps',future[0],future[1],'timeQ_upper_bound',future[3])
    print('stage268_target_outside_orientation',orient(L5,L6,future),'old_stage267_support_slack',LP*future[0]+LQ*future[1]+future[3]-val[(0,0,0)])
    print('STAGE268_RESEARCH_QUESTION: cross L5-L6 edge with exact feasible external point; derive next support or separating certificate')


if __name__=='__main__':
    main()
