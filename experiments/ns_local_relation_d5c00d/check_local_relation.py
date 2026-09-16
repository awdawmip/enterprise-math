#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from itertools import product, permutations
from pathlib import Path
import importlib.util, hashlib, json, sys
import sympy as sp

EVENT='NS-LOCAL-RELATION-PROPAGATION-20260916-D5C00D-19'
HERE=Path(__file__).resolve().parent
PARENT=HERE.parent / 'ns_finite_relation_d5c00d' / 'check_stabilizer_relation.py'
EXPECTED='6ff48da0bbd6a041f580696f464353216696bd21a27d0ac411b0e2dafe4202a4'
if hashlib.sha256(PARENT.read_bytes()).hexdigest()!=EXPECTED:
    raise RuntimeError('event18 parent checker mismatch')
spec=importlib.util.spec_from_file_location('stabilizer18',PARENT)
old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old;spec.loader.exec_module(old)

ZERO=(0,)*6
def unit(i,s=1):return tuple(s*int(j==i) for j in range(6))
def add(a,b):return tuple(x+y for x,y in zip(a,b))

def ptrace_one(R,q):
    out=sp.zeros(2)
    for a,b in product(range(2),repeat=2):
        val=0
        for rest in product(range(2),repeat=2):
            aa=list(rest);bb=list(rest);aa.insert(q,a);bb.insert(q,b)
            ia=4*aa[0]+2*aa[1]+aa[2];ib=4*bb[0]+2*bb[1]+bb[2]
            val+=R[ia,ib]
        out[a,b]=sp.simplify(val)
    return out

@dataclass(frozen=True)
class Distributed:
    letters: tuple[tuple[str,str,str],tuple[str,str,str],tuple[str,str,str]]
    phases: tuple[tuple[int,int,int],tuple[int,int,int],tuple[int,int,int]]
    def global_rows(self):
        ans=[]
        for letters,phases in zip(self.letters,self.phases):
            ans.append((phases[0]*phases[1]*phases[2],''.join(letters)))
        return tuple(ans)
    def full_group(self):
        gens=self.global_rows();mats=[old.pmatrix(w,s) for s,w in gens]
        ident=old.identifier(3);out=set()
        for mask in range(8):
            M=sp.eye(8)
            for r in range(3):
                if (mask>>r)&1:M=M*mats[r]
            out.add(ident[old.key(M)])
        return frozenset(out)

def start_dist():
    return Distributed((('Z','I','I'),('I','Z','I'),('I','I','Z')),
                       ((1,1,1),(1,1,1),(1,1,1)))

def local_single(st,q,table):
    letters=[list(x) for x in st.letters];ph=[list(x) for x in st.phases]
    for r in range(3):
        ds,c=table[letters[r][q]];letters[r][q]=c;ph[r][q]*=ds
    return Distributed(tuple(tuple(x) for x in letters),tuple(tuple(x) for x in ph))

def local_cnot(st,c,t):
    letters=[list(x) for x in st.letters];ph=[list(x) for x in st.phases]
    for r in range(3):
        ds,out=old.CMAP[letters[r][c]+letters[r][t]]
        letters[r][c],letters[r][t]=out
        ph[r][c]*=ds
    return Distributed(tuple(tuple(x) for x in letters),tuple(tuple(x) for x in ph))

def global_reference(g,gate):return old.gate_group(g,gate)
def support(row):return sum(c!='I' for c in row)

def gauge(st,choices):
    evens=((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1))
    ph=[list(x) for x in st.phases]
    for r,ch in enumerate(choices):
        g=evens[ch]
        for q in range(3):ph[r][q]*=g[q]
    return Distributed(st.letters,tuple(tuple(x) for x in ph))

def move(pos,party,axis,sign):
    out=list(pos);out[party]=add(out[party],unit(axis,sign));return tuple(out)

def assert_primitive(a,b):
    d=tuple(y-x for x,y in zip(a,b));assert sum(abs(x) for x in d)==1 and sum(x!=0 for x in d)==1

def protocol(axis_b=0,sign_b=1,axis_c=1,sign_c=1,initial=None):
    assert axis_b!=axis_c and sign_b in (-1,1) and sign_c in (-1,1)
    st=start_dist() if initial is None else initial
    ref=old.initial_group();pos=(ZERO,unit(axis_b,sign_b),unit(axis_c,sign_c));records=[]
    def record(name):
        g=st.full_group();assert g==ref
        records.append({'stage':name,'rows':[(s,w) for s,w in st.global_rows()],
                        'row_supports':[support(w) for s,w in st.global_rows()],
                        'positions':pos,'rho':old.rho_from_group(g)})
    record('start')
    st=local_single(st,0,old.HMAP);ref=global_reference(ref,('H',0));record('H_A')
    oldp=pos[1];pos=move(pos,1,axis_b,-sign_b);assert pos[1]==pos[0];assert_primitive(oldp,pos[1]);record('B_gather')
    beforeC=ptrace_one(records[-1]['rho'],2)
    st=local_cnot(st,0,1);ref=global_reference(ref,('C',0,1));record('CNOT_AB')
    assert ptrace_one(records[-1]['rho'],2)==beforeC
    oldp=pos[1];pos=move(pos,1,axis_b,sign_b);assert_primitive(oldp,pos[1]);record('B_return')
    oldp=pos[2];pos=move(pos,2,axis_c,-sign_c);assert pos[2]==pos[0];assert_primitive(oldp,pos[2]);record('C_gather')
    beforeB=ptrace_one(records[-1]['rho'],1)
    st=local_cnot(st,0,2);ref=global_reference(ref,('C',0,2));record('CNOT_AC')
    assert ptrace_one(records[-1]['rho'],1)==beforeB
    oldp=pos[2];pos=move(pos,2,axis_c,sign_c);assert_primitive(oldp,pos[2]);record('C_return')
    return st,ref,pos,records

def main(output):
    st,ref,pos,records=protocol()
    assert st.full_group()==ref
    for item in [(1,'XXX'),(1,'ZZI'),(1,'ZIZ'),(-1,'XYY'),(-1,'YXY'),(-1,'YYX')]:assert item in ref
    stages={r['stage']:r for r in records}
    assert stages['H_A']['rows'][0]==(1,'XII')
    assert stages['CNOT_AB']['rows'][0]==(1,'XXI')
    assert stages['CNOT_AC']['rows'][0]==(1,'XXX')
    assert [stages[x]['row_supports'][0] for x in ('H_A','CNOT_AB','CNOT_AC')]==[1,2,3]
    def local_endpoint(dist,q):return tuple((dist.letters[r][q],dist.phases[r][q]) for r in range(3))
    d0=start_dist();d1=local_single(d0,0,old.HMAP);d2=local_cnot(d1,0,1)
    assert local_endpoint(d2,2)==local_endpoint(d1,2)
    d3=local_cnot(d2,0,2);assert local_endpoint(d3,1)==local_endpoint(d2,1)
    gauges=0;reference_snapshots=[r['rho'] for r in records]
    for choices in product(range(4),repeat=3):
        gst=gauge(start_dist(),choices);_,_,_,grecs=protocol(initial=gst)
        assert [r['rho'] for r in grecs]==reference_snapshots;gauges+=1
    assert gauges==64
    variants=0;base_rows=[r['rows'] for r in records]
    for ab,ac in permutations(range(6),2):
        for sb,sc in product((-1,1),repeat=2):
            xst,xref,xpos,xrecs=protocol(ab,sb,ac,sc)
            assert xst.full_group()==ref and xref==ref
            assert [r['rows'] for r in xrecs]==base_rows
            assert xpos==(ZERO,unit(ab,sb),unit(ac,sc));variants+=1
    assert variants==120
    rho=old.rho_from_group(ref)
    mermin=sp.trace(rho*(old.pmatrix('XXX')-old.pmatrix('XYY')-old.pmatrix('YXY')-old.pmatrix('YYX')));assert mermin==4
    ket000=sp.zeros(8,1);ket000[0]=1;ket111=sp.zeros(8,1);ket111[7]=1
    mix=(ket000*ket000.T+ket111*ket111.T)/2
    assert sp.trace(mix*(old.pmatrix('XXX')-old.pmatrix('XYY')-old.pmatrix('YXY')-old.pmatrix('YYX')))==0
    for q in range(3):assert ptrace_one(rho,q)==ptrace_one(mix,q)==sp.eye(2)/2
    for w in ('ZZI','ZIZ','IZZ'):assert sp.trace(rho*old.pmatrix(w))==sp.trace(mix*old.pmatrix(w))==1
    vals=set()
    for a in product((-1,1),repeat=6):
        x1,y1,x2,y2,x3,y3=a;vals.add(x1*x2*x3-x1*y2*y3-y1*x2*y3-y1*y2*x3)
    assert vals=={-2,2}
    data={'schema':'EM_LOCAL_RELATION_PROPAGATION_RESULTS_V1','event_id':EVENT,
      'distributed_state':{'independent_relation_rows':3,'parties':3,'local_letters_per_endpoint':3,'local_phase_bits_per_endpoint':3,'raw_local_endpoint_alphabet_upper_bound':512,'gauge_lifts_exhausted':gauges,'all_gauges_same_global_trajectory':True},
      'local_generation':{'first_row_sequence':['XII','XXI','XXX'],'support_sequence':[1,2,3],'remote_endpoint_fragment_unchanged_at_each_pair_gate':True,'remote_one_party_marginal_unchanged_at_each_pair_gate':True},
      'native_transport':{'axis_sign_variants_checked':variants,'primitive_moves_per_protocol':4,'pair_gates_only_when_colocated':True,'final_parties_return_to_start_cells':True},
      'final':{'stabilizers':['+XXX','+ZZI','+ZIZ','-XYY','-YXY','-YYX'],'Mermin':4,'incoherent_same_local_pair_readout_Mermin':0,'local_hidden_bound':2},
      'scope':['Distributed stabilizer fragments and Clifford rules are quantum-comparison structures, not P000-derived force laws.','Finite local endpoint alphabet is internal relational state; spatial positions remain the discrete X6 torsor.','CNOT is not certified as a primitive two-force balance; a native triadic lift or other lawful implementation remains required.','Relation support growth is information/provenance growth, not energy or faster-than-light signalling.','No NS theorem, Foundation promotion, independent review or Lean build.']}
    Path(output).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'gauges':gauges,'variants':variants,'support':[1,2,3],'mermin':4,'output':str(output)}))

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',default='results_19.json');a=p.parse_args();main(a.output)
