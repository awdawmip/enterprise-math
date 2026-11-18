"""Exact BRC row check for the residue model. Run with PYTHONPATH=<EM>/src."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path

from enterprise_math import brc_control_port
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.brc_transport import Affine, eye, matrix, mm
from enterprise_math.heartbeat_carry_peak import HIT, compile_carry_peak, projective_lattice_key
from enterprise_math.heartbeat_peak_orbits import threshold_action_equivalent
from enterprise_math.heartbeat_peak_quotient import compile_peak_quotient, passage_law, peak_observation_chain

def block(a):
    return matrix([[a[i%2][j%2] if i//2==j//2 else 0 for j in range(6)] for i in range(6)])

def packet(k, split):
    u,v=block(((2,0),(0,1))),block(((1,0),(0,2)))
    e=block(((1,2**k),(0,1)))
    rows=[(u,F(1,4)),(v,F(1,4))]
    if split: rows=[(u,F(1,8)),(mm(u,e),F(1,8)),(v,F(1,4))]
    return ControlPacket.from_edges(2,0,1,[(0,0,w,Affine(a,(0,)*6),1) for a,w in rows]+[
            (0,1,F(1,2),Affine(eye(6),(0,)*6),1),(1,1,1,Affine(eye(6),(0,)*6),1)])

def spread(d,x,D):
    e=0 if x==0 else D-((x&-x).bit_length()-1)
    return max(d,2*e-d)

def states(k,R,split):
    D=max(0,R-k-2) if split else 0
    return D,[(d,x) for x in range(1<<D) for d in range(1-R,R) if spread(d,x,D)<R]

def children(k,R,D,d,x,split):
    # Values are integer numerators with denominator eight; stop is separate.
    if d+1>=R:
        yield 'H',2
    else:
        up=(d+1,x)
        if split:
            exponent=k+D-d
            assert exponent>=0
            y=(x+(1<<exponent))% (1<<D) if exponent<D else x
            twist=(d+1,y)
            yield 'H' if spread(*up,D)>=R else up,1
            yield 'H' if spread(*twist,D)>=R else twist,1
        else:
            yield 'H' if spread(*up,D)>=R else up,2
    down=(d-1,x)
    yield 'H' if spread(*down,D)>=R else down,2

@lru_cache(None)
def oriented(d,x,D):
    a=max(D,d,0)
    return projective_lattice_key(block(((1<<a,x*(1<<(a-D))),(0,1<<(a-d)))),2)

def prefix(k,R,n,split):
    D,_=states(k,R,split)
    active={(0,0):1}
    out=[F(0)]
    for t in range(1,n+1):
        nex=defaultdict(int); hit=0
        for (d,x),mass in active.items():
            for z,weight in children(k,R,D,d,x,split):
                if z=='H':hit+=mass*weight
                else:nex[z]+=mass*weight
        out.append(F(hit,8**t))
        active=nex
    return out

def verify_rows(k,R,split):
    p=packet(k,split); D,ss=states(k,R,split)
    assert len(ss)==(2*R-2*D+1)*(1<<D)-2
    a=compile_carry_peak(p,2,R,max_states=2*len(ss)+2)
    assert a.complete and len(a.states)==2*len(ss)
    keys={oriented(d,x,D):(d,x) for d,x in ss}
    assert len(keys)==len(ss)
    parsed=[(s.control,keys[s.lattice]) for s in a.states]
    assert parsed[0]==(0,(0,0))
    observed=[Counter() for s in a.states]
    for b in a.edges:
        assert b.multiplicity==1
        target='H' if b.target==HIT else parsed[b.target]
        observed[b.source][target]+=b.mass
    for i,(port,(d,x)) in enumerate(parsed):
        if port==1: assert observed[i]=={(1,(d,x)):1};continue
        expected=Counter({(1,(d,x)):F(1,2)})
        for target,mass in children(k,R,D,d,x,split):
            expected['H' if target=='H' else (0,target)]+=F(mass,8)
        assert expected==observed[i]
    result={'k':k,'R':R,'split':split,'safe_six_axis_states':len(a.states),'row_checks':len(a.states)}
    if k==1 and R in (3,4):
        chain=peak_observation_chain(p,a)
        mini=compile_peak_quotient(chain)
        result['minimal_bisimulation_blocks_including_terminals']=len(mini.chain.colors)
        result['eventual_hit']=str(passage_law(mini.chain).probability[mini.chain.initial])
    return result

def main():
    src=Path(brc_control_port.__file__).resolve().parent
    old=json.loads((src.parents[1]/'research_notes/heartbeat_weighted_lift_20260927_AD0416/RESULTS.json').read_text())['frozen_brc_sources']
    for name,digest in old.items():assert hashlib.sha256((src/name).read_bytes()).hexdigest()==digest
    rows=[]
    for k,R in [(1,1),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(2,6),(3,5),(3,6),(4,7)]:
        rows.extend(verify_rows(k,R,s) for s in (False,True))
        u=block(((2,0),(0,1)));e=block(((1,1<<k),(0,1)))
        assert threshold_action_equivalent(u,mm(u,e),2,R)==(R<=k+1)
    parameters=0
    for k in range(1,13):
        for R in range(1,k+9):
            t=R+2*k+2
            x=prefix(k,R,t+2,False);y=prefix(k,R,t+2,True)
            if R<=k+2:
                assert x==y
            else:
                assert x[:t]==y[:t]
                assert y[t]-x[t]==F(R-k-2,2*4**t)
            parameters+=1
    print(json.dumps({'wl_sha256_matched':len(old),'reported_rows':rows,
          'all_R_prefix_pairs_checked':parameters,'unknown_mass':0},indent=2))

if __name__=='__main__':main()
