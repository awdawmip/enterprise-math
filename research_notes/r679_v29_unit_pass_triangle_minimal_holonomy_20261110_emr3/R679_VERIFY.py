#!/usr/bin/env python3
"""R679 exact integer certificate: unit 3-PASS cycle + V29 TRANSFER bias.
Scientific inputs are the V23/V27/V29 definitions pinned by R462.
No floating point, no external dependencies. Prints machine-readable JSON.
"""
import itertools
import json
from functools import lru_cache

AXES=tuple(range(6))
TRIADS=tuple(itertools.combinations(AXES,3))
MATCHINGS=(
    ((0,1),(2,3),(4,5)),
    ((0,2),(1,4),(3,5)),
    ((0,3),(1,5),(2,4)),
    ((0,4),(1,3),(2,5)),
)
PASS_CYCLE=((0,1),(1,2),(2,0))
IDENTITY=(0,1,2)

def codeword(T):
    out=[]
    for pairs in MATCHINGS:
        bits=[]
        for a,b in pairs:
            if a in T: bits.append(0)
            elif b in T: bits.append(1)
            else: break
        out.append((-1)**sum(bits) if len(bits)==3 else 0)
    return tuple(out)
CODE={T:codeword(T) for T in TRIADS}
NEIGHBORS={S:tuple(T for T in TRIADS if len(set(S)&set(T))==2) for S in TRIADS}

def skew_from_passes(passes):
    M=[[0]*4 for _ in range(4)]
    for a,b in passes: M[a][b]+=1
    return tuple(tuple(M[i][j]-M[j][i] for j in range(4)) for i in range(4))

def fields_u_from_passes(passes):
    u=[0]*4
    for a,b in passes:
        u[a]+=1;u[b]-=1
    return tuple(u)

def score(S,T,u,omega):
    a=CODE[S];b=CODE[T]
    return sum(u[i]*b[i] for i in range(4))+sum(a[i]*omega[i][j]*b[j] for i in range(4) for j in range(4))

@lru_cache(maxsize=8)
def prepared(omega):
    return {S:tuple((*(CODE[T]),sum(CODE[S][i]*omega[i][j]*CODE[T][j] for i in range(4) for j in range(4)),T) for T in NEIGHBORS[S]) for S in TRIADS}

def selector(u,omega,early=False):
    table=prepared(omega)
    ans={};minimum_gap=None;number_tied=0
    a,b,c,d=u
    for S in TRIADS:
        items=table[S]
        scored=[(a*x+b*y+c*z+d*w+constant,T) for x,y,z,w,constant,T in items]
        maximum=max(score for score,T in scored)
        winners=[T for score,T in scored if score==maximum]
        if len(winners)>1:
            number_tied+=1
            if early:return {},number_tied,None
        else:
            gap=maximum-max(score for score,T in scored if T!=winners[0])
            minimum_gap=gap if minimum_gap is None else min(gap,minimum_gap)
        ans[S]=winners[0]
    return ans,number_tied,minimum_gap

def recurrent_cycles(succ):
    seen=set();cycles=[]
    for S in TRIADS:
        if S in seen:continue
        path=[];positions={};curr=S
        while curr not in seen and curr not in positions:
            positions[curr]=len(path);path.append(curr);curr=succ[curr]
        if curr in positions:cycles.append(tuple(path[positions[curr]:]))
        seen.update(path)
    return tuple(cycles)

def frame_transport(cycle):
    starting=cycle[0];frame=starting
    for now,then in zip(cycle,cycle[1:]+cycle[:1]):
        removed=next(a for a in now if a not in then)
        inserted=next(a for a in then if a not in now)
        frame=tuple(inserted if a==removed else a for a in frame)
    assert set(frame)==set(starting)
    return tuple(starting.index(a) for a in frame)

def norm_shell(k):
    """Each length-four signed integer tuple of exact L1 norm k once."""
    for a in range(k+1):
        for b in range(k-a+1):
            for c in range(k-a-b+1):
                vals=(a,b,c,k-a-b-c)
                for signs in itertools.product((-1,1),repeat=4):
                    if any(x==0 and s==-1 for x,s in zip(vals,signs)):
                        continue
                    yield tuple(x*s for x,s in zip(vals,signs))

def finite_certificate(kmax=19):
    omega=skew_from_passes(PASS_CYCLE)
    stats=[];witnesses=[]
    for k in range(kmax+1):
        total=strict=nonflat=0
        for u in norm_shell(k):
            total+=1
            suc,ties,gap=selector(u,omega,early=True)
            if ties:continue
            strict+=1
            cycles=recurrent_cycles(suc)
            perms=[frame_transport(c) for c in cycles]
            if any(p!=IDENTITY for p in perms):
                nonflat+=1
                if k==19:
                    witnesses.append({'u':list(u),'min_gap':gap,'cycles':[[list(t) for t in cyc] for cyc in cycles],'perms':[list(p) for p in perms]})
        expected_shell = 1 if k==0 else sum((2**j)*__import__('math').comb(4,j)*__import__('math').comb(k-1,j-1) for j in range(1,min(4,k)+1))
        assert total==expected_shell,(k,total,expected_shell)
        stats.append({'l1':k,'vectors':total,'strict_twenty':strict,'nonflat_strict':nonflat})
    assert sum(item['vectors'] for item in stats)==97281
    assert sum(item['strict_twenty'] for item in stats)==9078
    assert sum(item['nonflat_strict'] for item in stats)==6
    assert len(witnesses)==6
    return stats,witnesses

def event_trace():
    # Bridge beta(port)=field: 0->0, 1->2, 2->1, 3->3.
    beta=(0,2,1,3)
    # At the central Cell, nine outgoing and ten incoming unit transfers.
    # Counts over ports (not fields); all matched at neighboring Cells.
    out_port=(2,3,4,0)
    in_port=(0,0,0,10)
    u_port=tuple(in_port[p]-out_port[p] for p in range(4))
    u_boundary=tuple(u_port[beta.index(i)] for i in range(4))
    assert u_port==(-2,-3,-4,10)
    assert u_boundary==(-2,-4,-3,10)
    # Native PASS port order is beta^{-1}(0->1->2->0).
    pass_port=tuple((beta.index(a),beta.index(b)) for a,b in PASS_CYCLE)
    assert pass_port==((0,2),(2,1),(1,0))
    steps=[];passes=[]
    for _ in range(4):
        omega=skew_from_passes(passes)
        intrinsic=fields_u_from_passes(passes)
        u=tuple(u_boundary[i]+intrinsic[i] for i in range(4))
        sel,ties,gap=selector(u,omega)
        cycles=recurrent_cycles(sel) if ties==0 else ()
        steps.append({'pass_count':len(passes),'u':list(u),'tied_active_triads':ties,
          'minimum_gap_if_all_strict':gap if ties==0 else None,
          'recurrent_cycles':[[list(t) for t in cyc] for cyc in cycles],
          'holonomy':[list(frame_transport(cyc)) for cyc in cycles]})
        if len(passes)<3:passes.append(PASS_CYCLE[len(passes)])
    assert steps[0]['tied_active_triads']==0
    assert steps[1]['tied_active_triads']==2
    assert steps[2]['tied_active_triads']==3
    assert steps[3]['tied_active_triads']==0
    assert [2,1,0] in steps[3]['holonomy']
    assert [2,1,0] not in steps[0]['holonomy']
    # V29 correct reconstruction: M has one in/out per 0,1,2.
    I=tuple((1 if a<3 else 0)+in_port[beta.index(a)] for a in range(4))
    O=tuple((1 if a<3 else 0)+out_port[beta.index(a)] for a in range(4))
    assert I==(1,1,1,10) and O==(3,5,4,0)
    assert tuple(I[i]-O[i] for i in range(4))==u_boundary
    return {'beta_port_to_field':list(beta),'pass_port_pairs':[list(t) for t in pass_port],
       'field_I':list(I),'field_O':list(O),
       'local_u_sum':sum(u_boundary),'local_transfer_events':19,
       'pass_events':3,'total_events':22,'snapshots':steps}

def main():
    assert len(CODE)==20 and len(set(CODE.values()))==20
    assert all(len(NEIGHBORS[x])==9 for x in TRIADS)
    assert CODE[(0,1,2)]==(0,0,1,1)
    stats,witnesses=finite_certificate()
    events=event_trace()
    assert any(w['u']==[-2,-4,-3,10] for w in witnesses)
    print(json.dumps({'status':'R679_UNIT_PASS_TRIANGLE_MINIMAL_ODD_HOLONOMY_EXACT_PASS',
      'scientific_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'model':'V23 4-field code; V27 fixed post-ledger selector; V29 nonnegative primitive PASS/TRANSFER; V17 slot inheritance',
      'pass_counts':[[0,1],[1,2],[2,0]],
      'shells':stats,'checked_vectors':sum(i['vectors'] for i in stats),
      'min_boundary_transfers':19,'min_total_primitive_events':22,
      'minimum_witnesses':witnesses,'event_trace':events},indent=2,ensure_ascii=False))
if __name__=='__main__':main()
