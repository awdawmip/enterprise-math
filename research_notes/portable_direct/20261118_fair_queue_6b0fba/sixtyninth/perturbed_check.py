"""Certified tagged inventory transport on the pinned R11 closed cube."""
import argparse
import gzip
import hashlib
import importlib.util
import json
import sys
import time
from collections import Counter
from dataclasses import replace
from fractions import Fraction
from itertools import product
from pathlib import Path

HORIZON = 116
MASK = (4,2,1)
D = (1,2,3)
PINS = {
    'test_cycles.py':'49d1c6ed0be596b82fa8bfa963df934fc1702cf91feda1680fb7f8d8e961c6d7',
    'PARENT_BYTES.json':'f30e7e13eed4eacab90cbd95f81a3377b1c7c14deda553442e263f72ab5925eb',
    'run2/FULL_PREFIX_CYCLE_STATES.json.gz':'8b0e2a6958103e0ea5f5a87f2957860674a6c1a154e71fda8e9850b2e1887de1',
    'run2/CHECKPOINTS.json.gz':'f1fe67c0090419286788dca335c706fefd17f8c836847cdce3e3b8c91d3f6ca8',
}
LOCAL = '21257ae2289545b0fb6894cbbe98c7355ccab40a9df52e0ce647f85e0fd10a3b'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def signature(obj):
    return digest(json.dumps(obj,sort_keys=True,separators=(',',':')).encode())


def base_from_archive(root):
    # Read just the first two whole states in the byte-pinned archive, uniformly indexed.
    with gzip.open(root/'run2/FULL_PREFIX_CYCLE_STATES.json.gz','rt') as stream:
        text=stream.read(1024*1024)
    prefix='[{"case":"uniform-0","states":['
    assert text.startswith(prefix)
    decode=json.JSONDecoder().raw_decode
    _,end=decode(text,len(prefix))
    state,_=decode(text,end+1)
    assert state['t']==1 and len(state['cells'])==5832
    return state


def material(s,loc):
    return s.q,tuple(sorted(s.pending.items())),s.wall,tuple(s.b[i] for i in loc)


def first_repeat(keys):
    seen={}
    for t,x in enumerate(keys):
        if x in seen:
            return [seen[x],t-seen[x]]
        seen[x]=t
    raise AssertionError('no exact equality within the stated budget')


def support(s,bg,loc):
    a={k[0] for k in set(s.pending)|set(bg.pending) if s.pending.get(k,0)!=bg.pending.get(k,0)}
    return a|{v for v,i in enumerate(loc) if s.q[v]!=bg.q[v] or s.wall[v]!=bg.wall[v] or s.b[i]!=bg.b[i]}


def half_stocks(s):
    # Number already intended for v, including initial outstanding commitments from w.
    return [[s.q[v][j]+sum(n for (src,port,role,r),n in s.pending.items()
                             if (src,port,role)==(v^MASK[j],j,j))
             for j in range(3)] for v in range(8)]


def cycle_bounds(stock,phase):
    edges={v:[(v,1,2)]+[(v^mask,stock[v][j],D[j]+((phase[v^mask]-phase[v]-stock[v][j]-D[j])%3))
                          for j,mask in enumerate(MASK)] for v in range(8)}
    cycles=[]
    def extend(path,inventory,lag):
        for w,b,l in edges[path[-1]]:
            if w==path[0]:
                cycles.append((tuple(path),inventory+b,lag+l))
            elif w>path[0] and w not in path:
                extend(path+[w],inventory+b,lag+l)
    for v in range(8):
        extend([v],0,0)
    best=max(Fraction(l,h) for _,h,l in cycles)
    optimal=[list(p) for p,h,l in cycles if Fraction(l,h)==best]
    return edges,dict(directed_simple_cycles=len(cycles),max_delay_per_release=str(best),
                      max_cycles=optimal)


class Counts:
    """Independent firing-prefix observer; no calls to the original transition."""
    def __init__(self,R,a,loc,s):
        self.R,self.a,self.loc,self.base=R,a,loc,s
        self.N=[(0,)*8]
        self.fires=[(0,)*8]
        self.phase=tuple(s.b[i] for i in loc)
        self.old={(v,j):[(r,n) for (w,port,role,r),n in s.pending.items()
                         if (w,port,role)==(v,j,j)] for v in range(8) for j in range(3)}
    def step(self):
        t=len(self.N)
        a=self.a
        q=[]
        fires=[]
        M=[]
        labels={}
        for v in range(8):
            planned=[]
            for j,d in enumerate(D):
                w=v^MASK[j]
                received=a.total(n for r,n in self.old[w,j] if r<=t)
                received=a.add(received,self.N[max(0,t-d)][w])
                planned.append(a.gap(a.add(self.base.q[v][j],received),self.N[-1][v]))
                hand=a.total(n for r,n in self.old[v,j] if r==t)
                if t>d:
                    hand=a.add(hand,self.fires[t-d][v])
                if hand:
                    labels[f'handoff:{v}:{j}:{j}']=hand
            oldphase=self.R.R10.ROT[1][self.phase[v]]
            fire=int(oldphase==0 and min(planned)>0)
            M.append(self.R.R10.TURN[oldphase] if fire else oldphase)
            fires.append(fire)
            q.append(tuple(a.gap(x,fire) for x in planned))
            if fire:
                labels[f'groups:{v}:0']=1
                for j in range(3):
                    labels[f'commit:{v}:{j}:{j}']=1
        self.phase=tuple(M)
        self.fires.append(tuple(fires))
        self.N.append(tuple(a.add(x,y) for x,y in zip(self.N[-1],fires)))
        pp={}
        for v in range(8):
            for j,d in enumerate(D):
                for r in range(1,d+1):
                    remaining=a.total(n for r0,n in self.old[v,j] if r0==r+t)
                    sent=t-d+r
                    if sent>0:
                        remaining=a.add(remaining,self.fires[sent][v])
                    if remaining:
                        pp[v,j,j,r]=remaining
        b=[self.R.R10.ROT[t%3][x] for x in self.base.b]
        for v,g in enumerate(self.loc):
            b[g]=M[v]
        return self.R.State(a.add(self.base.t,t),tuple(q),pp,self.base.wall,tuple(b)),labels


def simulate(R,repair,meta,base,background,flows,j,timed):
    a=R.P.Arithmetic(ledger=False)
    m=R.instantiate(a,meta,R.config('uniform',0))
    q=list(map(list,base.q))
    q[0][j]=a.gap(q[0][j],1)
    q[MASK[j]][j]=a.add(q[MASK[j]][j],1)
    start=replace(base,q=tuple(map(tuple,q)))
    assert m.normalized(start) and m.total(start)==48
    s=local=start
    observer=Counts(R,a,m.locations,start)
    stock=half_stocks(s)
    assert all(stock[v][j]+stock[v^mask][j]==4 for v in range(8) for j,mask in enumerate(MASK))
    edges,bounds=cycle_bounds(stock,[start.b[i] for i in m.locations])
    seen_material=[material(s,m.locations)]
    seen_full=[R.field_key(s)]
    changed={v:0 for v in support(s,base,m.locations)}
    first_labels={}
    local_nodes=0
    old_hits=[]
    trace=[]
    totals={}
    labels_by_time=[]
    for t in range(1,HORIZON+1):
        begin=time.perf_counter()
        a.stage='literal'
        s,labels,_=R.run_one(m,s,True)
        m.trace.clear()
        timed['literal']+=time.perf_counter()-begin
        begin=time.perf_counter()
        a.stage='local'
        bg=background[t%6]
        bgflow=flows[(t-1)%6]
        local,localflow,n=repair(R,m,local,background[(t-1)%6],bg,bgflow)
        local_nodes+=n
        timed['local']+=time.perf_counter()-begin
        begin=time.perf_counter()
        a.stage='prefix_counts'
        expect,observed=observer.step()
        timed['prefix_counts']+=time.perf_counter()-begin
        begin=time.perf_counter()
        assert expect==local==s and observed==localflow==labels
        assert m.normalized(s) and m.total(s)==48
        cur_H=half_stocks(s)
        assert all(cur_H[v][j]==stock[v][j]+observer.N[t][v^mask]-observer.N[t][v]
                   for v in range(8) for j,mask in enumerate(MASK))
        for v in support(s,bg,m.locations):
            changed.setdefault(v,t)
        for label in labels.keys()|bgflow.keys():
            if labels.get(label,0)!=bgflow.get(label,0):
                first_labels.setdefault(label,t)
        a.stage='labelled_cumulative'
        totals=R.flow_add(a,totals,labels)
        seen_full.append(R.field_key(s))
        seen_material.append(material(s,m.locations))
        labels_by_time.append(labels)
        if any(R.field_key(b)==seen_full[-1] for b in background):
            old_hits.append(t)
        trace.append([m.compact(s),s.b[0],sorted(labels.items())])
        timed['verify_and_keys']+=time.perf_counter()-begin
    assert not old_hits
    events=[[t for t in range(1,HORIZON+1) if observer.fires[t][v]] for v in range(8)]
    maxeq=0
    for v in range(8):
        for k,t in enumerate(events[v],1):
            if k>max(h for _,h,_ in edges[v]):
                arrivals=[events[w][k-h-1]+l for w,h,l in edges[v]]
                assert t==max(arrivals)
                maxeq+=1
    mu,period=first_repeat(seen_full)
    mut,pt=first_repeat(seen_material)
    cycle_totals=[sum(observer.fires[t][v] for t in range(mu+1,mu+period+1)) for v in range(8)]
    assert len(set(cycle_totals))==1 and Fraction(period,cycle_totals[0])==Fraction(bounds['max_delay_per_release'])
    assert all(seen_full[t]==seen_full[t-period] for t in range(mu+period,HORIZON+1))
    assert all(labels_by_time[t-1]==labels_by_time[t-1-pt] for t in range(mut+pt+1,HORIZON+1))
    expected=[14,51] if j==2 else [0,6]
    assert [mu,period]==expected and [mut,pt]==([14,17] if j==2 else [0,2])
    assert len(first_labels)==(56 if j==2 else 0)
    gap_residues=[]
    if j==2:
        for v in range(8):
            word=[observer.fires[mut+t+1][v] for t in range(pt)]
            hits=[i for i in range(pt) if word[i] and not word[(i-1)%pt] and not word[(i-2)%pt]]
            assert len(hits)==1
            r=(mut+1+hits[0])%pt
            assert all(observer.fires[t][v]==int((t-r)%17 in {0,2,4,6,8,10,12}) for t in range(15,HORIZON+1))
            gap_residues.append(r)
    return dict(port=j,full_first_repeat=[mu,period],material_first_repeat=[mut,pt],
                equality_to_old_orbit=False,changed_nodes_first_ticks=sorted(changed.items()),
                first_changed_flow_label=dict(sorted(first_labels.items())),bounds=bounds,
                releases_per_vertex_full_period=cycle_totals,steady_restart_mod17=gap_residues,
                indexed_time_recurrence_checks=maxeq,integrated_counts_sha256=signature(totals),
                full_compact_trace_and_named_flow_sha256=signature(trace),
                work=dict(literal_ticks=HORIZON,literal_material_nodes=8*HORIZON,
                          sparse_nodes_rebuilt=local_nodes,exact_whole_field_and_increment_checks=HORIZON,
                          finite_period_states_examined=mu+period+1,source_brc_counts=a.counts))


def first_gate_census(R,base,loc,a):
    # On either face of the cube, x/z inventory choices alone can inhibit a gate.
    hist=Counter()
    a.stage='one_face_threshold'
    checks=0
    for transfer in product(range(-2,3),range(-2,3),range(-1,2),range(-1,2)):
        q=list(map(list,base.q))
        predicted=set()
        for (v,w,j),n in zip(((0,4,0),(1,5,0),(0,1,2),(4,5,2)),transfer):
            donor,receiver=(v,w) if n>=0 else (w,v)
            q[donor][j]=a.gap(q[donor][j],abs(n))
            q[receiver][j]=a.add(q[receiver][j],abs(n))
            if abs(n)==base.q[v][j]:
                predicted.add(donor)
        observed=set()
        for v in (0,1,4,5):
            # The only arriving role at this step is 1. Both endpoint quantities,
            # even after any legal type-1 transfer, give at least one available.
            q[v][1]=a.add(q[v][1],1)
            phase=R.R10.ROT[1][base.b[loc[v]]]
            groups,_,_=R.R10.burst_unit(a,min(q[v]),phase,{0},R.R10.TURN)
            if not groups:
                observed.add(v)
            checks+=1
        assert observed==predicted
        hist[len(observed)]+=1
    face=[hist[k] for k in range(5)]
    assert face==[9,60,110,44,2]
    cube=[81*sum(face[i]*face[k-i] for i in range(5) if 0<=k-i<5) for k in range(9)]
    assert sum(cube)==5**4*3**8 and cube[0]==3**8
    return dict(face_polynomial=face,full_cube_polynomial=cube,valid_inventory_choices=sum(cube),
                forever_same_labelled_flows=cube[0],one_face_original_gate_calls=checks)


def main(root,local_path):
    for name,pin in PINS.items():
        assert digest((root/name).read_bytes())==pin
    files=json.loads((root/'PARENT_BYTES.json').read_text())['files']
    for name,pin in files.items():
        assert digest((root/name).read_bytes())==pin
    assert digest(local_path.read_bytes())==LOCAL
    spec=importlib.util.spec_from_file_location('repair69',local_path)
    medium=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(medium)
    sys.path.insert(0,str(root))
    import test_cycles as R
    meta=json.loads((R.R10.R9.PARENT/'COORDINATES.json').read_text())
    a=R.P.Arithmetic(ledger=False)
    m=R.instantiate(a,meta,R.config('uniform',0))
    assert [m.target(0,j) for j in range(3)]==list(MASK)
    s,_,_=R.run_one(m,R.prepare(m,R.config('uniform',0)),True)
    assert m.full(s)==base_from_archive(root)
    checkpoints=json.loads(gzip.decompress((root/'run2/CHECKPOINTS.json.gz').read_bytes()))
    assert ['uniform-0',1,59,0,6,6] in checkpoints
    bg=[];flows=[]
    for i in range(6):
        bg.append(s)
        s,inc,_=R.run_one(m,s,True)
        flows.append(inc)
    assert R.field_key(s)==R.field_key(bg[0])
    times=Counter()
    results=[simulate(R,medium.repair_one,meta,bg[0],bg,flows,j,times) for j in range(3)]
    answer=dict(frozen_files=PINS,prior_local_sha256=LOCAL,ancestor_files_verified=len(files),
                material_addresses=list(m.locations),full_addresses=len(m.codes),horizon=HORIZON,cases=results,
                first_gate_census=first_gate_census(R,bg[0],m.locations,a))
    return answer,times


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--r11',type=Path,required=True)
    parser.add_argument('--prior-local',type=Path,default=Path(__file__).resolve().parents[1]/'fiftyeighth/delay_local.py')
    parser.add_argument('--out',type=Path)
    parser.add_argument('--timing',type=Path,help='Optional machine-dependent process timings.')
    args=parser.parse_args()
    ts=time.perf_counter()
    data,times=main(args.r11,args.prior_local)
    first=time.perf_counter()
    result=json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(result)
    else:
        print(result,end='')
    times['result_serialization_and_write']=time.perf_counter()-first
    times['whole_run']=time.perf_counter()-ts
    if args.timing:
        args.timing.write_text(json.dumps(times,indent=2,sort_keys=True)+'\n')
