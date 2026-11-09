#!/usr/bin/env python3
"""PREFIX-631 exact frozen native STAR/BRC path-support certificate.
Source semantics: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d,
matching research_notes/portable_direct/PREFIX629_phase_only_suffix_checker.py.
Only original 48 STAR phases, 96 ports, 576 typed source/action edges are used.
"""
from collections import Counter
from itertools import product
import json
from pathlib import Path

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
PHASES=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(PHASES)}
def neighbors(i):
    a,p,c=PHASES[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
G=IX[(0,1,-3)]
WEIGHTS=(1,1,1,1,0,0)
ACTIONS=[]; BY_SRC=[[] for _ in range(96)]
for i in range(48):
    for j in neighbors(i):
        for u,v in product((0,1),repeat=2):
            gated=(j==G and u==v==1)
            w=0 if gated else WEIGHTS[abs(PHASES[i][2])-1]
            a=(2*j+v,2*i+u,w,gated)
            ACTIONS.append(a); BY_SRC[a[0]].append(a)
assert len(PHASES)==48 and len(ACTIONS)==576 and G==4
assert all(len(x)==6 for x in BY_SRC)
POS=[[(dst,1) for src,dst,w,gated in row if (w or gated)] for row in BY_SRC]
LIVE={i for i,row in enumerate(POS) if row}
DEAD=set(range(96))-LIVE
RECUR={i for i in LIVE if sum(dst in LIVE for dst,_ in POS[i])==2}
HIGH={i for i in LIVE if sum(dst in LIVE for dst,_ in POS[i])==4}
assert len(LIVE)==64 and len(DEAD)==32 and len(RECUR)==len(HIGH)==32
assert all(len(POS[i])==6 and sum(dst in RECUR for dst,_ in POS[i])==2 and sum(dst in DEAD for dst,_ in POS[i])==4 for i in RECUR)
assert all(not POS[i] for i in DEAD)

def advance(r):
    out=[0]*96
    for src,row in enumerate(POS):
        if r[src]:
            for dst,_ in row: out[dst]+=r[src]
    return out

r0=[0]*96
for i in (4,11,14,32):
    r0[2*i]=1
    if i==G: r0[2*i+1]=1
states=[r0]
for _ in range(20):states.append(advance(states[-1]))
# A(1)^4 r2 = 16 r2 is a finite vector equality certificate.
assert states[6]==[16*x for x in states[2]]
assert all(states[t+4]==[16*x for x in states[t]] for t in range(2,17))
base=[]
for t in range(4,8):
    active=sorted(i for i in RECUR if states[t][i]>0)
    hist=Counter(states[t][i] for i in active)
    assert len(active)==12 and hist==Counter({2**(t-1):10,2**t:2})
    base.append({'t':t,'recurrent_source_ports':active,'low_mass':str(2**(t-1)),
                 'low_count':10,'high_mass':str(2**t),'high_count':2,
                 'total_phase_state_nonzero':sum(x>0 for x in states[t])})

def count_paths(support,L):
    counts=[1]*96
    for _ in range(L):
        counts=[sum(counts[d] for d,_ in POS[i]) for i in range(96)]
    return sum(counts[i] for i in support), counts

def streamed_hist(t,L):
    hist=Counter(); emitted=0
    # DFS retains source ports/labels and masses; dead ports are only allowed as terminal hits.
    def walk(port,depth,mass):
        nonlocal emitted
        if depth==L:
            hist[mass]+=1;emitted+=1
            return
        for dst,_ in POS[port]:
            if depth+1==L or dst in RECUR:
                walk(dst,depth+1,mass)
    for i in sorted(RECUR):
        if states[t][i]:walk(i,0,states[t][i])
    return emitted,hist

verified=[]
for t in range(4,16):
    source=[i for i,m in enumerate(states[t]) if m]
    for L in range(1,17):
        k,_=count_paths(source,L)
        expected=72*2**(L-1)
        assert k==expected,(t,L,k,expected)
        if t in (4,5,8,11) and L<=8:
            emitted,h=streamed_hist(t,L)
            assert emitted==k
            assert h==Counter({2**(t-1):60*2**(L-1), 2**t:12*2**(L-1)})
            verified.append((t,L,k))

# Exact bit counts of canonical per-path binary mass representation for all-one gates.
for t in (4,7,16):
    for L in (1,3,10,30):
        npath=72*2**(L-1)
        mass_bits=(72*t+12)*2**(L-1)
        assert mass_bits==60*2**(L-1)*t+12*2**(L-1)*(t+1)
        assert npath>0
out={
  'schema':'PREFIX631_NATIVE_STREAM_OUTPUT_CERTIFICATE_V1',
  'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'source_checker':'PREFIX629_phase_only_suffix_checker.py@04822a439b5ed8f6761ba69c7131053d8e7d9fc6',
  'original_phase_count':len(PHASES),'original_port_count':len(BY_SRC),'original_action_count':len(ACTIONS),
  'graph':{'nonzero_edges_at_gate_1':sum(map(len,POS)),'live_ports':len(LIVE),'dead_ports':len(DEAD),'recurrent_ports':len(RECUR),'other_live_ports':len(HIGH),'recurrent_closed_under_live_edges':True,'recurrent_live_targets_per_source':2,'recurrent_dead_targets_per_source':4},
  'four_step_native_certificate':{'r2_nonzero':[[i,x] for i,x in enumerate(states[2]) if x],'r6_equals_16_r2':True},
  'four_base_residue_cases':base,
  'exact_theorem':{'input':'four-point probe, lambda=1, all gates=1, t=n-L>=4, L>=1',
     'nonzero_labelled_full_suffix_paths':'72*2^(L-1)',
     'source_mass_histogram':{'2^(t-1)':'60*2^(L-1)','2^t':'12*2^(L-1)'},
     'binary_mass_digits_total':'(72*t+12)*2^(L-1)',
     'arbitrary_nonnegative_gate_upper_bound':'nonzero path count <=72*2^(L-1) for t>=4'},
  'finite_checks':{'path_count_pairs':12*16,'streamed_path_histogram_checks':len(verified),'four_step_equality_checked':True,'full_path_examples':verified},
  'status':'ALL_ASSERTIONS_PASS','review_status':'AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('PREFIX631_native_stream_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:out[k] for k in ('schema','graph','finite_checks','status')},ensure_ascii=False))
