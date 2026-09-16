#!/usr/bin/env python3
"""Exact ternary Pauli-relation comparator; no physical/native-force admission.

Run from any directory; dependencies Python 3 and SymPy. Parent helpers are
imported unchanged and hash checked. All runtime relation updates are finite
letter/sign arithmetic. Matrices independently certify the declared comparator.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys
from collections import deque
from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import sympy as sp

EVENT='NS-TRIADIC-RELATION-GATE-20260916-D5C00D-20'
HERE=Path(__file__).resolve().parent
P18=HERE.parent/'ns_finite_relation_d5c00d/check_stabilizer_relation.py'
P19=HERE.parent/'ns_local_relation_d5c00d/check_local_relation.py'
HASHES={P18:'6ff48da0bbd6a041f580696f464353216696bd21a27d0ac411b0e2dafe4202a4',
        P19:'e3ea2ebb040b00969a5896164978b92c4726bd53bc7f1c4e6784d08c573c98a7'}
for p,h in HASHES.items():
    if hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise RuntimeError(f'parent mismatch: {p}')
spec=importlib.util.spec_from_file_location('local19',P19)
loc=importlib.util.module_from_spec(spec);sys.modules[spec.name]=loc;spec.loader.exec_module(loc)
old=loc.old
WORDS=tuple(map(''.join,product('IXYZ',repeat=3)))
TRIPLES=tuple(map(''.join,product('XYZ',repeat=3)))
# Derive every one-site Pauli product, including its phase, from the parent.
MUL={}
for a,b in product('IXYZ',repeat=2):
    val=old.P1[a]*old.P1[b]
    matches=[(k,c) for k in range(4) for c in 'IXYZ' if val==(sp.I**k)*old.P1[c]]
    assert len(matches)==1;MUL[a,b]=matches[0]

def anti(a,b):return a!='I' and b!='I' and a!=b

def row_update(letters,phases,p='XXX'):
    """Permutation-equivariant endpoint rule; each sign stays at a real port."""
    if len(letters)!=3 or len(phases)!=3 or p not in TRIPLES:raise ValueError('three endpoints required')
    if any(s not in (-1,1) for s in phases):raise ValueError('signs must be +/-1')
    count=sum(anti(a,b) for a,b in zip(p,letters))
    if count%2==0:return tuple(letters),tuple(phases)
    out=[];signs=list(phases)
    for q,(a,b) in enumerate(zip(p,letters)):
        k,c=MUL[a,b];out.append(c)
        if k==3:signs[q]*=-1
        if count==3:signs[q]*=-1  # product of three minuses supplies -i*i^3
    return tuple(out),tuple(signs)

def label_update(label,p='XXX'):
    s,w=label;l,sg=row_update(tuple(w),(s,1,1),p)
    return (sg[0]*sg[1]*sg[2],''.join(l))

TABLE={p:{(s,w):label_update((s,w),p) for w in WORDS for s in (-1,1)} for p in TRIPLES}
def group_update(g,p='XXX'):return frozenset(TABLE[p][x] for x in g)
def distributed_update(st,p='XXX'):
    rows=[row_update(l,s,p) for l,s in zip(st.letters,st.phases)]
    return loc.Distributed(tuple(r[0] for r in rows),tuple(r[1] for r in rows))

def partial(R,keep):
    keep=tuple(keep);rest=tuple(i for i in range(3) if i not in keep);d=2**len(keep);out=sp.zeros(d)
    for a,b in product(range(d),repeat=2):
        for rb in product((0,1),repeat=len(rest)):
            ba=[0]*3;bb=[0]*3
            for j,q in enumerate(keep):ba[q]=(a>>(len(keep)-1-j))&1;bb[q]=(b>>(len(keep)-1-j))&1
            for j,q in enumerate(rest):ba[q]=bb[q]=rb[j]
            ia=sum(x<<(2-j) for j,x in enumerate(ba));ib=sum(x<<(2-j) for j,x in enumerate(bb))
            out[a,b]+=R[ia,ib]
    return out.applyfunc(sp.simplify)

def operator_cut_rank(U,q):
    other=[i for i in range(3) if i!=q];out=sp.zeros(4,16)
    for a,b in product(range(8),repeat=2):
        ab=[(a>>(2-j))&1 for j in range(3)];bb=[(b>>(2-j))&1 for j in range(3)]
        r=2*ab[q]+bb[q];c=(2*ab[other[0]]+ab[other[1]])*4+2*bb[other[0]]+bb[other[1]]
        out[r,c]=U[a,b]
    return out.rank()

@dataclass(frozen=True)
class State:
    phase:int
    positions:tuple
    relation:loc.Distributed

def step(st,sources,anchor=loc.ZERO):
    if st.phase==0:
        if st.positions!=sources:raise ValueError('gather starts at declared sources')
        return State(1,(anchor,)*3,st.relation)
    if st.phase==1:
        if st.positions!=(anchor,)*3:raise ValueError('all three must be colocated')
        return State(2,st.positions,distributed_update(st.relation))
    if st.phase==2:
        if st.positions!=(anchor,)*3:raise ValueError('scatter starts at the common Cell')
        return State(0,sources,st.relation)
    raise ValueError('phase must be 0,1,2')

def run():
    matrix_cases=0;raw_cases=0;symmetry=0
    matrices={w:old.pmatrix(w) for w in WORDS}
    for p in TRIPLES:
        P=matrices[p];U=(sp.eye(8)-sp.I*P)/sp.sqrt(2)
        assert sp.simplify(U.H*U)==sp.eye(8)
        for w in WORDS:
            s,v=TABLE[p][(1,w)]
            assert sp.simplify(U*matrices[w]*U.H)==s*matrices[v];matrix_cases+=1
            for phases in product((-1,1),repeat=3):
                a,b=row_update(w,phases,p)
                start=(tuple(w),phases);nxt=start
                for _ in range(4):nxt=row_update(*nxt,p)
                assert nxt==start;raw_cases+=1
                for perm in permutations(range(3)):
                    trans=lambda z:tuple(z[i] for i in perm)
                    aa,bb=row_update(trans(w),trans(phases),''.join(trans(p)))
                    assert (aa,bb)==(trans(a),trans(b));symmetry+=1
    # Odd-weight preservation is checked on every row and proved for arbitrary n in note.
    for p in TRIPLES:
        for w in WORDS:
            _,v=TABLE[p][1,w]
            assert sum(c!='I' for c in w)%2==sum(c!='I' for c in v)%2
    assert old.apply_cnot((1,'XII'),0,1)==(1,'XXI')
    # Consume parent's finite orbit; this is regression/reuse, not a new 1080 discovery.
    orbit,_=old.bfs_orbit();assert len(orbit)==1080
    for g in orbit:
        for p in TRIPLES:assert group_update(g,p) in orbit
    seen={old.initial_group()};queue=deque(seen)
    while queue:
        g=queue.popleft()
        successors=[old.gate_group(g,(kind,q)) for kind in ('H','S') for q in range(3)]
        successors += [group_update(g,p) for p in TRIPLES]
        for nxt in successors:
            if nxt not in seen:seen.add(nxt);queue.append(nxt)
    assert seen==orbit
    P=matrices['XXX'];U=(sp.eye(8)-sp.I*P)/sp.sqrt(2)
    st0=loc.start_dist();st1=distributed_update(st0)
    assert st1.global_rows()==((-1,'YXX'),(-1,'XYX'),(-1,'XXY'))
    group=st1.full_group();rho=old.rho_from_group(group)
    z=sp.zeros(8,1);z[0]=1;o=sp.zeros(8,1);o[7]=1
    psi=(z-sp.I*o)/sp.sqrt(2);psi2=(z+sp.I*o)/sp.sqrt(2)
    rho2=sp.simplify(psi2*psi2.H)
    assert rho==sp.simplify(psi*psi.H)
    cuts=[operator_cut_rank(U,q) for q in range(3)];assert cuts==[2,2,2]
    for q in range(3):assert partial(rho,[q])==sp.eye(2)/2
    mix=(z*z.T+o*o.T)/2
    for keep in ((0,),(1,),(2,),(0,1),(0,2),(1,2)):
        assert partial(rho,keep)==partial(rho2,keep)==partial(mix,keep)
    assert sp.simplify(U*rho*U.H)==o*o.T
    assert sp.simplify(U*rho2*U.H)==z*z.T
    M=matrices['YYY']-matrices['YXX']-matrices['XYX']-matrices['XXY']
    assert sp.trace(M*rho)==4 and sp.trace(M*mix)==0
    lhs=set()
    for x1,y1,x2,y2,x3,y3 in product((-1,1),repeat=6):
        lhs.add(y1*y2*y3-y1*x2*x3-x1*y2*x3-x1*x2*y3)
    assert lhs=={-2,2}
    probabilities=0
    for setting in map(''.join,product('XY',repeat=3)):
        probs=old.joint_probs(rho,setting);probabilities+=len(probs)
        for q in range(3):
            for sign in (-1,1):assert sum(p for out,p in probs.items() if out[q]==sign)==sp.Rational(1,2)
    # Product-X eigenstate countercontrol: structural support is NOT change on every input.
    plus=sp.ones(8,1)/sp.sqrt(8)
    assert sp.simplify(U*(plus*plus.H)*U.H)==sp.simplify(plus*plus.H)
    # Known pair-gate decomposition certifies that nonfactorization is not force-primitivity.
    def cn(c,t):
        mat=sp.zeros(8)
        for x in range(8):
            bits=[(x>>(2-j))&1 for j in range(3)];bits[t]^=bits[c]
            y=sum(b<<(2-j) for j,b in enumerate(bits));mat[y,x]=1
        return mat
    V=cn(0,2)*cn(1,2);W=old.kron_all([old.H]*3)*V
    Rz=(sp.eye(8)-sp.I*matrices['IIZ'])/sp.sqrt(2)
    assert sp.simplify(W*Rz*W.H)==U
    # Physical six binary internal modes: identity off the dual-rail code.
    E=old.dualrail_isometry();F=E*E.T
    Uphys=E*U*E.T+sp.eye(64)-F
    assert sp.simplify(Uphys.H*Uphys)==sp.eye(64)
    for q in range(3):
        N=old.pair_number_operator(q);assert Uphys*N==N*Uphys
        assert N*E*psi==E*psi
    bareN=(3*sp.eye(8)-matrices['ZII']-matrices['IZI']-matrices['IIZ'])/2
    assert U*bareN!=bareN*U and sp.trace(bareN*rho)==sp.Rational(3,2)
    # Gauge test uses the unchanged parent representation and gauge operation.
    for choices in product(range(4),repeat=3):
        gs=loc.gauge(st0,choices);ref=st0
        for _ in range(4):
            gs=distributed_update(gs);ref=distributed_update(ref)
            assert gs.full_group()==ref.full_group()
    # Full closed current-state controller: one unit gather, gate, one unit scatter.
    cycles=0;moves=0
    for axes in permutations(range(6),3):
        for signs in product((-1,1),repeat=3):
            src=tuple(loc.unit(i,s) for i,s in zip(axes,signs))
            initial=State(0,src,st0);st=initial
            for t in range(12):
                nxt=step(st,src)
                for a,b in zip(st.positions,nxt.positions):
                    if a!=b:loc.assert_primitive(a,b);moves+=1
                st=nxt
                assert st!=initial or t==11
            assert st==initial;cycles+=1
    assert cycles==960 and moves==23040
    # Nonlocal application is rejected rather than repaired by an inserted channel.
    try:step(State(1,((0,)*6,loc.unit(0),loc.unit(1)),st0),(loc.ZERO,)*3)
    except ValueError:rejected=True
    else:raise AssertionError('separated input was accepted')
    return {'schema':'EM_TRIADIC_RELATION_GATE_RESULTS_V1','event_id':EVENT,
      'parents':{str(p.relative_to(HERE.parent.parent)):h for p,h in HASHES.items()},
      'checks':{'exact_conjugations':matrix_cases,'raw_row_cases':raw_cases,'endpoint_permutation_equalities':symmetry,
       'orbit_states_reused':len(orbit),'triple_gate_state_images':len(orbit)*27,'odd_gate_state_orbit':len(seen),
       'gauge_lifts':64,'gauge_steps_each':4,'all_XY_joint_probabilities':probabilities,
       'signed_three_axis_routes':cycles,'nonzero_primitive_moves':moves,'rejected_nonlocal_gate':rejected},
      'results':{'rows_after_R':st1.global_rows(),'operator_cut_ranks':cuts,'mermin':4,'classical_Mermin_bound':2,
       'mixture_Mermin':0,'pair_marginals_equal_opposite_phases':True,'same_gate_after_opposite_phases':['111','000'],
       'bare_excitation_after_gate':'3/2','dual_rail_each_pair_excitation':1,'dual_rail_total_excitation':3,
       'gate_density_period':4,'closed_router_ticks':12,'odd_weight_parity_invariant':True,
       'CNOT_excluded_on_same_register_without_extra_resources':True,'pair_circuit_decomposition_exists':True,
       'density_entries_grid':'(Z+iZ)/8 for fixed three-qubit pure stabilizer orbit'},
      'scope':['All rules are explicit comparator assumptions, not P000-derived primitive force laws.',
       'Three-party structural indispensability does not mean every state changes or the gate is elementary.',
       'Reachability of all 1080 pure stabilizer states does not imply every Clifford channel can be implemented.',
       'No measurement reset in the closed recurrent process; no irreversibility or instability inferred.',
       'Conserved excitation is an indicator, not complete physical energy.',
       'No local hidden-variable measurement model, NS theorem, independent review or Lean build.']}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=HERE/'results.json');args=ap.parse_args()
    data=run();args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks':data['checks'],'results':data['results']},ensure_ascii=False,indent=2))
