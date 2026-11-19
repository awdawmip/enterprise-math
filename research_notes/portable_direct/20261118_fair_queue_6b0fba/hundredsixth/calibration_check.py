"""Exact calibration flats in F_3^d and positive-path execution of selected gate words."""
import argparse
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from hashlib import sha1
from itertools import permutations, product
from math import prod
import json
from pathlib import Path
import sys

PINS = {
    "research_tasks/RS-EULER-RR-03-CALIBRATION-20261011.md": "925f903096f9d7039a8c28b6903465499c1f9566",
    "research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md": "03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b",
    "research_notes/chatgpt_direct/20261010_EULER_PASSIVE_SAMPLING_AND_NOISE.md": "bd80290c259cc60995069613a5f4b5f5b41a13d1",
    "src/enterprise_math/brc_weighted.py": "3f205696709e847909958a153f8fe10d3f6b70f0",
    "src/enterprise_math/brc_logarithm.py": "4732e5fc381ce613d240c4381ccbef03c27a69c7",
    "src/enterprise_math/exact_arithmetic.py": "35ea95b0916494b83a92386e3e313928362dd79e",
}


def projective(x):
    u = next((j for j in x if j),0)
    return tuple((j*u)%3 for j in x)


def gaussian(d,m):
    ratio = F(1)
    for k in range(m):
        ratio *= F(3**(d-k)-1,3**(m-k)-1)
    assert ratio.denominator==1
    return int(ratio)


def shear(x,i,j,sign=1):
    y=list(x)
    y[i]=(y[i]+sign*y[j])%3
    return tuple(y)


def flat_graph(d,n):
    """Pull back the success flat by one gate; stored words are in physical time order."""
    pts=sorted({projective(x) for x in product(range(3),repeat=d) if any(x)})
    index={x:i for i,x in enumerate(pts)}
    initial=tuple(i for i,x in enumerate(pts) if not any(x[:n]))
    inverse={}
    for i,j in permutations(range(d),2):
        inverse[i,j]=[index[projective(shear(x,i,j,-1))] for x in pts]
    words={initial:()}
    pending=deque([initial])
    while pending:
        flat=pending.popleft()
        for step,action in inverse.items():
            new=tuple(sorted(action[k] for k in flat))
            if new not in words:
                words[new]=(step,)+words[flat]
                pending.append(new)
    assert len(words)==gaussian(d,d-n)
    return pts,words


def optimum(d,n,law,graph):
    pts,words=graph
    masses=Counter()
    for x,p in law.items():
        masses[projective(x)]+=p
    origin=masses[(0,)*d]
    comparable=origin+sum(sorted([masses[x] for x in pts],reverse=True)[:(3**(d-n)-1)//2])
    scores={flat:origin+sum(masses[pts[i]] for i in flat) for flat in words}
    best=max(scores.values())
    flat=min((f for f,v in scores.items() if v==best),key=lambda f:(len(words[f]),words[f]))
    word=words[flat]
    direct=F(0)
    for x,p in law.items():
        y=x
        for i,j in word:
            y=shear(y,i,j)
        direct+=p*int(not any(y[:n]))
    assert direct==best
    return best,comparable,word


def uniform(rows):
    return {x:F(1,len(rows)) for x in rows}


def physical(kernel,law,d,n,word):
    """One source-independent calibration, followed by n writes along a single old-source path."""
    counts=Counter()
    ready=kernel.CWM_ZERO
    residues=defaultdict(set)
    outcomes=Counter()
    # Two opposite receiver frames, three common roots, and three old-source rotations.
    for x,px in law.items():
        for a,j0,sheet in product(range(3),range(3),(1,-1)):
            regs=[(a+v)%3 for v in x]
            w=kernel.cwm_edge(px/18)
            j=j0
            for dest,src in word:
                turns=(sheet*(regs[src]-a))%3
                for _ in range(turns or 1):
                    w=kernel.cwm_propagate(w,kernel.CWM_ONE)
                    if turns:
                        regs[dest]=(regs[dest]+sheet)%3
                counts["calibration_contact_path_incidences"]+=turns
                counts["calibration_holds"]+=int(turns==0)
            before_write=tuple((v-a)%3 for v in regs)
            original=tuple(x)
            for dest,src in reversed(word):
                before_write=shear(before_write,dest,src,-1)
            assert before_write==original
            # w=1 on the passive source; the active writer flag is zero at all times.
            source_sheet=F2=0
            reports=[]; true=[]
            for slot in range(n):
                true.append(j)
                turns=(sheet*(j-a))%3
                for _ in range(turns or 1):
                    w=kernel.cwm_propagate(w,kernel.CWM_ONE)
                    if turns:
                        regs[slot]=(regs[slot]+sheet)%3
                counts["record_contact_path_incidences"]+=turns
                counts["record_holds"]+=int(turns==0)
                reports.append(regs[slot])
                source_sheet^=F2
                F2^=1
                j=(j+(-1)**source_sheet)%3
            correct=tuple(int(v==j) for v,j in zip(reports,true))
            outcomes[correct]+=w.total
            if all(correct):
                ready=kernel.cwm_recoalesce(ready,w)
                residues[a,j0,sheet].add(tuple(regs[n:]))
            counts["true_complete_preparations"]+=1
    assert sum(outcomes.values())==1
    return dict(joint_success=str(ready.total),success_event_distribution={''.join(map(str,k)):str(v) for k,v in sorted(outcomes.items())},
                residual_work_states_on_success=sorted({len(set_) for set_ in residues.values()}),ledger=counts)


def run(repo):
    for name,expected in PINS.items():
        raw=(repo/name).read_bytes()
        assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==expected
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as kernel
    graphs={}
    dimensions={}
    for d in range(1,6):
        counts=[]
        for n in range(d+1):
            graphs[d,n]=flat_graph(d,n)
            counts.append(len(graphs[d,n][1]))
        dimensions[d]=counts
    axes=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
    cap=uniform([tuple((v*s)%3 for v in axis) for axis in axes for s in (1,2)])
    c,s,word=optimum(3,1,cap,graphs[3,1])
    assert c==F(1,2) and s==1
    cap_run=physical(kernel,cap,3,1,word)
    assert cap_run['joint_success']==str(c)
    hidden=uniform([(a,b,(a+b)%3,(a-b)%3) for a,b in product(range(3),repeat=2)])
    c2,s2,word2=optimum(4,2,hidden,graphs[4,2])
    assert c2==s2==1
    hidden_run=physical(kernel,hidden,4,2,word2)
    assert hidden_run['joint_success']=='1' and hidden_run['residual_work_states_on_success']==[9]
    hidden_zero=physical(kernel,hidden,4,2,())
    assert hidden_zero['joint_success']=='1/9'
    marginal_cases=[]
    for d in range(2,8):
        h=[1]*d
        if d%3==0:
            h[-1]=2
        xs=list(product(range(3),repeat=d))
        hyper=[x for x in xs if sum(a*b for a,b in zip(h,x))%3==0]
        counts=[Counter() for _ in range(d+1)]
        for x in hyper:
            for a in range(3):
                registers=(a,)+tuple((a+i)%3 for i in x)
                for i in range(d+1):
                    counts[i][registers[:i]+registers[i+1:]]+=1
        assert all(len(row)==3**d and set(row.values())=={1} for row in counts)
        if d<=5:
            assert optimum(d,1,uniform(hyper),graphs[d,1])[0]==1
            assert optimum(d,1,uniform(xs),graphs[d,1])[0]==F(1,3)
        marginal_cases.append(dict(d=d,proper_marginals=d+1,retained_states_each=3**d))
    laws=[(F(1,2),F(1,3),F(1,6)),(F(4,5),F(1,10),F(1,10)),
          (F(2,3),F(1,3),F(0)),(F(1,3),)*3]
    independent={x:prod(q[j] for q,j in zip(laws,x)) for x in product(range(3),repeat=4)}
    observed=[]
    for n in range(5):
        r=optimum(4,n,independent,graphs[4,n])[0]
        assert r==prod(sorted([q[0] for q in laws],reverse=True)[:n])
        observed.append(str(r))
    return dict(task="RS-EULER-RR-03-CALIBRATION-20261011",input_git_blobs=PINS,flats_by_d_and_N=dimensions,
        cap=dict(linear_success=str(c),full_equivariant_success=str(s),minimal_word=word,observed=cap_run),
        two_records=dict(source_constraint="(a,b,a+b,a-b) in reference-relative coordinates",minimal_word=word2,
                         honest_uncalibrated=hidden_zero,calibrated=hidden_run),
        all_proper_marginal_pairs=marginal_cases,independent_zero_mode_success=observed)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path.cwd())
    print(json.dumps(run(ap.parse_args().repo),indent=2,sort_keys=True))
