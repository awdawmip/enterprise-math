"""Boundary-reversible lift of the pinned triadic comparator.

All scientific matching transitions execute the unchanged parent kernel;
serial/alternative history algebra uses the parent's positive CWM.
Not a physical reversibility model. No parent main suites are run.
"""
from __future__ import annotations
import argparse, json, sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_joint_gate as j
p,m,e,r,f=j.p,j.m,j.e,j.r,j.f
ONE,ZERO=j.ONE,j.ZERO
CHECKS=0

def ck(ok: bool, label: str):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

def forward(x=0,y=6,lo=12,hi=18,record=24,work=31):
    """24 calls: save the left source then apply the 15-call comparator."""
    j.domains((x,y,lo,hi,record))
    h,w=p.copy_program(x,record,work)
    h2,w2=j.joint(x,y,lo,hi)
    return h|h2,w+w2

def inverse(lo=12,hi=18,record=24,x=0,y=6,work=31):
    """19 calls: recover x=r and y=(r?lo:hi), consuming all three inputs.

The domain needed for a genuine inverse is lo <= r <= hi. The program
also produces a well-defined multiplexer result on other full triples,
which is explicitly NOT evidence that such a triple was a valid lift.
"""
    j.domains((lo,hi,record,x,y))
    H,copy=p.copy_program(record,x,work)
    # A real copy, but omit only the two source-head restoration proposals.
    W=[op for i,op in enumerate(copy) if i not in (5,6)]
    H|=set().union(*(p.library(o) for o in (lo,hi,y)))
    q0=tuple(sorted((record+3,hi+4,y+4)))
    q1=tuple(sorted((record+4,lo+4,y+4)))
    H|={q0,q1}
    lh,lt=p.reg(y,0);rh,rt=p.reg(y,1)
    W += [p.one(lo+1),p.one(hi+1),p.add(q0),p.add(q1),
          p.add(lt),p.add(rt),p.one(record+3),p.one(record+4),
          p.one(lo+5),p.one(hi+5),p.add(lh),p.add(rh)]
    return H,W

def cases():
    HF,FW=forward();HI,IW=inverse();H=HF|HI
    ck(len(FW)==24 and len(IW)==19,'24 forward / 19 inverse calls')
    ck(len(set().union(*H))==31,'five registers plus one private work member')
    rows=[];prefixes=[set() for _ in range(44)]
    for bits in product((0,1),repeat=2):
        start=j.init(bits,(0,6)); expected=j.init((bits[0]&bits[1],bits[0]|bits[1],bits[0]),(12,18,24))
        a=f.execute(start,FW,H,True)
        ck(a['end']==expected,'exact lifted endpoint')
        b=f.execute(a['end'],IW,H,True)
        ck(b['end']==start,'inverse restores original addresses and empties records/scratch')
        backward=f.execute(start,FW+IW,H,True)
        prefixes[0].add(start)
        for t,row in enumerate(backward['trace'],1): prefixes[t].add(row['after'])
        c=f.execute(a['end'],IW+FW,H)
        ck(c['end']==a['end'],'two-sided inverse on the valid image')
        ck(j.sq_observer(bits)==j.sq_observer((bits[0]&bits[1],bits[0]|bits[1])), 'data-only BRC square observer')
        rows.append(dict(bits=bits,forward=a,inverse=b))
    ck(all(len(s)==4 for s in prefixes),'all four inputs distinguishable at every common program position')
    triples=[]
    for low,high,record in product((0,1),repeat=3):
        J=j.init((low,high,record),(12,18,24))
        z=f.execute(J,IW,H)
        want=j.init((record,low if record else high),(0,6))
        ck(z['end']==want,'actual multiplexer on all eight full triples')
        roundtrip=f.execute(z['end'],FW,H)['end']
        valid=low<=record<=high
        ck((roundtrip==J)==valid,'image membership exactly low <= record <= high')
        triples.append(dict(triple=(low,high,record),valid_image=valid,end=z['end'],roundtrip=roundtrip))
    # A valid-looking but wrong record swaps unlike sources, undetected by square readout.
    damaged=j.init((0,1,1),(12,18,24))
    z=f.execute(damaged,IW,H,True)
    ck(z['end']==j.init((1,0),(0,6)),'flipped record recovers a different valid ordering')
    ck(j.sq_observer((0,1))==j.sq_observer((1,0)), 'square cannot detect record corruption')
    # Reverse command order is not an inverse of the primitive word.
    reverse=f.execute(rows[1]['forward']['end'],list(reversed(FW)),H,True)
    ck(reverse['end']!=j.init((0,1),(0,6)),'reversing a list of idempotent commands is not inversion')
    # Forgetting the record makes opposite sources literally indistinguishable.
    forgotten=[]
    for bits in ((0,1),(1,0)):
        z=f.execute(j.init(bits,(0,6)),FW+p.clear_word(24),H)
        forgotten.append(z['end'])
    ck(forgotten[0]==forgotten[1],'clearing the origin before recovery creates a real collision')
    return dict(rows=rows,triples=triples,prefix_distinct_counts=list(map(len,prefixes)),
                bad_record=dict(initial=damaged,run=f.execute(damaged,IW,H,True)),
                reverse_word=reverse,erased_record_ends=forgotten)

def network(n):
    """Fixed adjacent network; one genuine left-source record per comparator."""
    if not 2<=n<=6: raise ValueError('Executed finite suite uses n=2..6')
    wires=[6*i for i in range(n)];free=[6*n,6*(n+1)]
    q=n*(n-1)//2;record_offsets=[6*(n+2+t) for t in range(q)]
    work=6*(n+2+q)+1;H=set();FW=[];stages=[]
    for limit in range(n-1,0,-1):
        for i in range(limit):
            x,y=wires[i:i+2];lo,hi=free;rr=record_offsets[len(stages)]
            h,w=forward(x,y,lo,hi,rr,work);H|=h
            hr,wr=inverse(lo,hi,rr,x,y,work);H|=hr
            stages.append(dict(index=i,x=x,y=y,lo=lo,hi=hi,record=rr,
                               forward=w,inverse=wr,before=tuple(wires)))
            FW+=w;wires[i:i+2]=[lo,hi];free=[x,y]
            stages[-1]['after']=tuple(wires)
    IW=sum((s['inverse'] for s in reversed(stages)),[])
    return H,FW,IW,stages,wires,free,record_offsets,work

def networks():
    data=[]
    for n in range(2,7):
        H,FW,IW,stages,wires,free,records,work=network(n);q=len(stages)
        ck(len(FW)==24*q and len(IW)==19*q,'network command costs')
        ck(len(set().union(*H))==6*(n+2+q)+1,'network inventory with actual record registers')
        states={}; sorted_fibers={}; runs=[]
        for bits in product((0,1),repeat=n):
            J=j.init(bits,[6*i for i in range(n)]);K=J;record_values=[];brief=[]
            for s in stages:
                before=tuple(p.read(K,o) for o in s['before']);source=before[s['index']]
                rr=f.execute(K,s['forward'],H)
                K=rr['end'];record_values.append(source)
                observed=tuple(p.read(K,o) for o in s['after'])
                ck(all(v in (0,1) for v in observed),'full records at every forward comparator boundary')
                ck(j.sq_observer(observed)==j.sq_observer(bits),'data-only BRC squares survive forward comparator')
                ck(p.read(K,s['record'])==source,'record is actually written by primitive copy')
            sorted_bits=tuple(p.read(K,o) for o in wires)
            ck(sorted_bits==tuple(sorted(bits)),'forward result sorted; expected value only in checker')
            ck(K==m.canon(j.init(sorted_bits,wires)+j.init(record_values,records)),'no unlisted forward junk')
            forward_end=K
            ck(K not in states,'lifted final matching is injective on tested source words')
            states[K]=bits
            f.put(sorted_fibers,sorted_bits,e.prep(J))
            for s in reversed(stages):
                K=f.execute(K,s['inverse'],H)['end']
                observed=tuple(p.read(K,o) for o in s['before'])
                ck(all(v in (0,1) for v in observed),'full source records after each inverse')
                ck(p.restrict(K,s['record'])==(),'used residual register really reclaimed')
                ck(j.sq_observer(observed)==j.sq_observer(bits),'data-only BRC squares survive reconstruction')
            ck(K==J,'complete sorting and unsorting returns exact original matching, all history/work blank')
            runs.append(dict(input=bits,sorted=sorted_bits,record_values=record_values,forward_end=forward_end,restored=K))
        all_mass=f.total(sorted_fibers.values())
        ck(all_mass==f.total(ONE for _ in product((0,1),repeat=n)), 'positive provenance weights retained')
        data.append(dict(n=n,comparators=q,forward_calls=len(FW),inverse_calls=len(IW),members=len(set().union(*H)),
                         lifted_distinct=len(states),coarse_distinct=len(sorted_fibers),
                         fibers=[dict(output=k,CWM=e.cw(v)) for k,v in sorted(sorted_fibers.items())],runs=runs))
    return data

def retain_outputs():
    """Compute, copy desired sorted outputs, restore original input; clean history."""
    rows=[]
    for n in (2,3,6):
        H,FW,IW,stages,wires,free,records,work=network(n)
        q=len(stages);base=n+2+q
        outputs=[6*(base+1+i) for i in range(n)]
        CW=[]
        for src,dst in zip(wires,outputs):
            h,w=p.copy_program(src,dst,work);H|=h;CW+=w
        ck(len(FW+CW+IW)==43*q+9*n,'compute-copy-restore actual command length')
        ck(len(set().union(*H))==6*(2*n+2+q)+1,'only output copies add inventory')
        records_out=[]
        for bits in product((0,1),repeat=n):
            J=j.init(bits,[6*i for i in range(n)])
            z=f.execute(J,FW+CW+IW,H,keep=(n==3 and bits==(1,0,1)))
            expected=m.canon(J+j.init(tuple(sorted(bits)),outputs))
            ck(z['end']==expected,'original ordered input and sorted copy; all work/residuals blank')
            records_out.append(dict(input=bits,end=z['end'],trace=z['trace']))
        rows.append(dict(n=n,calls=len(FW+CW+IW),members=len(set().union(*H)),runs=records_out))
    return rows

def faults():
    HF,FW=forward();HI,IW=inverse();H=HF|HI;out=[]
    for bits in product((0,1),repeat=2):
        J=j.init(bits,(0,6))
        for budget in (1,2):
            W=j.d.a.rep(FW+IW,budget);states={(J,0):e.prep(J)};peak=1
            for op in W:
                nxt={}
                for (K,u),mass in states.items():
                    L,_=f.step(K,op,H)
                    f.put(nxt,(L,u),r.serial(mass,ONE))
                    if u<budget:f.put(nxt,(K,u+1),r.serial(mass,ONE))
                states=nxt;peak=max(peak,len(states))
            layers={}
            for (K,u),mass in states.items():
                ck(K==J,'protected complete forward+inverse restores entire matching')
                f.put(layers,u,mass)
            ck(layers==j.d.a.layers(len(W),budget),'all omission histories via independent CWM layers')
            out.append(dict(bits=bits,budget=budget,calls=len(W),peak=peak,layers=[dict(omitted=u,CWM=e.cw(v)) for u,v in sorted(layers.items())]))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['cases','networks','faults','retain'],required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    value={'cases':cases,'networks':networks,'faults':faults,'retain':retain_outputs}[a.mode]()
    result=dict(mode=a.mode,new_checks=CHECKS,uncached_kernel_calls=f.CALLS,transition_uses=f.USES,data=value)
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='data'}))
if __name__=='__main__':main()
