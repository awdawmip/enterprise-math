#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
from itertools import product
import json
from pathlib import Path
import sympy as sp

EVENT='NS-FINITE-RELATIONAL-STABILIZER-20260916-D5C00D-18'
I=sp.I
P1={
 'I':sp.eye(2),
 'X':sp.Matrix([[0,1],[1,0]]),
 'Y':sp.Matrix([[0,-I],[I,0]]),
 'Z':sp.diag(1,-1),
}
LETTERS='IXYZ'

def kron_all(ms):
    out=sp.Matrix([[1]])
    for m in ms: out=sp.kronecker_product(out,m)
    return out

def pmatrix(word, sign=1):
    return sign*kron_all([P1[c] for c in word])

def key(M):
    return tuple(sp.simplify(x) for x in M)

CACHE={}
def identifier(n):
    if n in CACHE:return CACHE[n]
    d={}
    for word in map(''.join, product(LETTERS, repeat=n)):
        for s in (1,-1):
            d[key(pmatrix(word,s))]=(s,word)
    CACHE[n]=d
    return d

H=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
S=sp.diag(1,I)
CNOT=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

ID1=identifier(1);ID2=identifier(2)
HMAP={c:ID1[key(H*P1[c]*H.H)] for c in LETTERS}
SMAP={c:ID1[key(S*P1[c]*S.H)] for c in LETTERS}
CMAP={a+b:ID2[key(CNOT*pmatrix(a+b)*CNOT.H)] for a in LETTERS for b in LETTERS}

def apply_single(label,q,table):
    s,word=label
    ls=list(word); ds,c=table[ls[q]];ls[q]=c
    return (s*ds,''.join(ls))

def apply_cnot(label,c,t):
    s,word=label
    pair=word[c]+word[t]
    ds,out=CMAP[pair]
    ls=list(word);ls[c],ls[t]=out[0],out[1]
    return (s*ds,''.join(ls))

def gate_group(group, gate):
    kind,*args=gate
    if kind=='H': return frozenset(apply_single(x,args[0],HMAP) for x in group)
    if kind=='S': return frozenset(apply_single(x,args[0],SMAP) for x in group)
    if kind=='C': return frozenset(apply_cnot(x,args[0],args[1]) for x in group)
    raise ValueError(gate)

def rho_from_group(group):
    return sp.simplify(sum((pmatrix(w,s) for s,w in group),sp.zeros(8))/8)

def exp_pauli(group, word):
    if (1,word) in group:return sp.Integer(1)
    if (-1,word) in group:return sp.Integer(-1)
    return sp.Integer(0)

def initial_group():
    return frozenset([
      (1,'III'),(1,'ZII'),(1,'IZI'),(1,'IIZ'),
      (1,'ZZI'),(1,'ZIZ'),(1,'IZZ'),(1,'ZZZ')])

def bfs_orbit():
    gates=[('H',q) for q in range(3)]+[('S',q) for q in range(3)]+[('C',c,t) for c in range(3) for t in range(3) if c!=t]
    start=initial_group();seen={start};Q=deque([start])
    while Q:
        g=Q.popleft()
        for gate in gates:
            h=gate_group(g,gate)
            if h not in seen: seen.add(h);Q.append(h)
    return seen,gates

def dualrail_isometry():
    E=sp.zeros(64,8)
    for x in range(8):
        logical=[(x>>(2-q))&1 for q in range(3)]
        bits=[]
        for b in logical: bits += [0,1] if b==0 else [1,0]
        idx=sum(bit<<(5-j) for j,bit in enumerate(bits))
        E[idx,x]=1
    return E

def pair_number_operator(pair):
    diag=[]
    for idx in range(64):
        bits=[(idx>>(5-j))&1 for j in range(6)]
        diag.append(bits[2*pair]+bits[2*pair+1])
    return sp.diag(*diag)

def H_pair():
    U=sp.eye(4);U[1,1]=U[1,2]=U[2,1]=sp.sqrt(2)/2;U[2,2]=-sp.sqrt(2)/2
    return U

def cnot_pairs(c,t):
    U=sp.zeros(64)
    for idx in range(64):
        pairvals=[]
        for q in range(3):
            b1=(idx>>(5-2*q))&1;b2=(idx>>(4-2*q))&1
            pairvals.append((b1,b2))
        out=list(pairvals)
        if pairvals[c] in ((0,1),(1,0)) and pairvals[t] in ((0,1),(1,0)):
            bc=1 if pairvals[c]==(1,0) else 0
            bt=1 if pairvals[t]==(1,0) else 0
            bt ^= bc
            out[t]=(1,0) if bt else (0,1)
        bits=[b for pair in out for b in pair]
        j=sum(bit<<(5-k) for k,bit in enumerate(bits))
        U[j,idx]=1
    return U

def embed_pair_gate(U4,q):
    mats=[]
    for k in range(3): mats.append(U4 if k==q else sp.eye(4))
    return kron_all(mats)

def joint_probs(rho, settings):
    ops=[P1[c] for c in settings]
    out={}
    for signs in product((-1,1),repeat=3):
        P=sp.Matrix([[1]])
        for s,O in zip(signs,ops): P=sp.kronecker_product(P,(sp.eye(2)+s*O)/2)
        p=sp.simplify(sp.trace(rho*P));assert p.is_Rational and p>=0
        out[signs]=p
    assert sum(out.values())==1
    return out

def main(output):
    orbit,gates=bfs_orbit()
    assert len(orbit)==1080
    maxden=1;entry_values=set()
    for g in orbit:
        R=rho_from_group(g)
        assert R.H==R and sp.trace(R)==1
        for x in R:
            re,im=sp.re(x),sp.im(x)
            assert re.is_Rational and im.is_Rational
            maxden=max(maxden,int(sp.denom(re)),int(sp.denom(im)))
            entry_values.add(str(x))
    assert maxden<=8

    g=initial_group();
    for gate in [('H',0),('C',0,1),('C',0,2)]:g=gate_group(g,gate)
    for item in [(1,'XXX'),(1,'ZZI'),(1,'ZIZ'),(-1,'XYY'),(-1,'YXY'),(-1,'YYX')]: assert item in g
    rho=rho_from_group(g)
    ket000=sp.zeros(8,1);ket000[0]=1
    ket111=sp.zeros(8,1);ket111[7]=1
    ghz=(ket000+ket111)/sp.sqrt(2)
    assert rho==sp.simplify(ghz*ghz.H)

    mix=(ket000*ket000.T+ket111*ket111.T)/2
    def ptrace_one(R,q):
        out=sp.zeros(2)
        for a,b in product(range(2),repeat=2):
            val=0
            for rest in product(range(2),repeat=2):
                bitsa=list(rest);bitsb=list(rest)
                bitsa.insert(q,a);bitsb.insert(q,b)
                ia=4*bitsa[0]+2*bitsa[1]+bitsa[2];ib=4*bitsb[0]+2*bitsb[1]+bitsb[2]
                val += R[ia,ib]
            out[a,b]=sp.simplify(val)
        return out
    for q in range(3):assert ptrace_one(rho,q)==ptrace_one(mix,q)==sp.eye(2)/2
    for word in ('ZZI','ZIZ','IZZ'):
        assert sp.trace(rho*pmatrix(word))==sp.trace(mix*pmatrix(word))==1
    for word,sgn in [('XXX',1),('XYY',-1),('YXY',-1),('YYX',-1)]:
        assert sp.trace(rho*pmatrix(word))==sgn and sp.trace(mix*pmatrix(word))==0
    mermin=sum(s*sp.trace(rho*pmatrix(w)) for w,s in [('XXX',1),('XYY',-1),('YXY',-1),('YYX',-1)])
    assert mermin==4
    classical=set()
    for vals in product((-1,1),repeat=6):
        x1,y1,x2,y2,x3,y3=vals
        classical.add(x1*x2*x3-x1*y2*y3-y1*x2*y3-y1*y2*x3)
    assert classical=={-2,2}

    settings=('XXX','XYY','YXY','YYX')
    distributions={}
    for s in settings:
        pr=joint_probs(rho,s);distributions[s]={''.join('+' if x==1 else '-' for x in k):str(v) for k,v in pr.items() if v}
        expected=int(sp.trace(rho*pmatrix(s)))
        assert set(v for v in pr.values())<={0,sp.Rational(1,4)}
        assert all((a*b*c==expected) == (p==sp.Rational(1,4)) for (a,b,c),p in pr.items())
        for q in range(3):
            for val in (-1,1):assert sum(p for out,p in pr.items() if out[q]==val)==sp.Rational(1,2)

    E=dualrail_isometry(); logical0=sp.zeros(8,1);logical0[0]=1
    phys0=E*logical0
    H1=embed_pair_gate(H_pair(),0);C12=cnot_pairs(0,1);C13=cnot_pairs(0,2)
    Ns=[pair_number_operator(q) for q in range(3)]
    for U in (H1,C12,C13):
        assert U.H*U==sp.eye(64)
        for N in Ns: assert U*N==N*U
    phys=C13*C12*H1*phys0
    assert phys==E*ghz
    for N in Ns:assert N*phys==phys
    Ntot = Ns[0] + Ns[1] + Ns[2]
    assert Ntot*phys==3*phys

    XL=sp.eye(4);XL[1,1]=XL[2,2]=0;XL[1,2]=XL[2,1]=1
    YL=sp.eye(4);YL[1,1]=YL[2,2]=0;YL[1,2]=-I;YL[2,1]=I
    Npair=sp.diag(0,1,1,2)
    for O in (XL,YL):assert O.H==O and O*O==sp.eye(4) and O*Npair==Npair*O

    def swap23(label):
        s,w=label;ls=list(w);ls[1],ls[2]=ls[2],ls[1];return (s,''.join(ls))
    gswap=frozenset(swap23(x) for x in g)
    assert (1,'XXX') in gswap and (-1,'XYY') in gswap
    routes=[]
    for axis,sgn in product(range(6),(-1,1)):
        step=tuple(sgn*int(i==axis) for i in range(6));assert sum(abs(x) for x in step)==1;routes.append(step)

    data={
      'schema':'EM_FINITE_RELATIONAL_STABILIZER_RESULTS_V1','event_id':EVENT,
      'orbit':{'three_qubit_stabilizer_states_enumerated':len(orbit),'clifford_generators':len(gates),'density_entry_max_denominator':maxden,'distinct_density_entry_values':len(entry_values)},
      'ghz':{'stabilizers':['+XXX','+ZZI','+ZIZ','-XYY','-YXY','-YYX'],'mermin_quantum':str(mermin),'mermin_local_hidden_bound':2,'outcomes':distributions},
      'brc_witness':{'same_all_one_qubit_marginals':True,'same_Z_pair_relations':True,'coherent_mixture_mermin':[4,0],'lost_joint_coordinate':'global phase stabilizer XXX'},
      'dual_rail':{'physical_modes':6,'logical_qubits':3,'total_excitation':3,'each_pair_excitation':1,'H_CNOT_commute_with_pair_numbers':True,'X_Y_measurements_commute_with_pair_number':True},
      'transport':{'signed_native_steps_checked':len(routes),'relation_survives_party_swap':True},
      'scope':['Stabilizer/Clifford/Born rules are explicit quantum-comparison assumptions, not derived from P000.','Finite closure is certified for the three-logical-qubit stabilizer/Clifford plus Pauli-measurement subtheory only.','Dropping the global stabilizer generator is unsafe for future Mermin observations even though all one-party marginals and Z-pair relations survive.','No classical local-hidden-variable residual model follows; Mermin bound remains 2 under locality and setting independence.','No primitive-force, NS, independent-review or Lean claim.']
    }
    Path(output).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'orbit':len(orbit),'maxden':maxden,'mermin':str(mermin),'output':str(output)}))

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',default='results_18.json');a=p.parse_args();main(a.output)
