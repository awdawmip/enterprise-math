"""Joint two-output triadic gate; consumes or restores shared binary operands.

All state updates use the unchanged inherited matching kernel. Histories are
composed and merged with the inherited positive CWM. Not native physics.
"""
from __future__ import annotations
import argparse
import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_direct_fold as d
p, m, e, r, f = d.p, d.m, d.e, d.r, d.f
ONE, ZERO = d.ONE, d.ZERO
CHECKS = 0

def ck(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)

def init(bits, offsets):
    return m.canon(h for bit, o in zip(bits, offsets) for h in p.reg(o, bit))

def domains(offsets):
    sets = [set(range(o+1, o+7)) for o in offsets]
    if any(sets[i] & sets[j] for i in range(len(sets)) for j in range(i)):
        raise ValueError('Whole registers must be pairwise disjoint')
    return sets

def joint(x=0, y=6, lo=12, hi=18):
    """15 commands; consume x/y; sorted Boolean pair in empty lo/hi."""
    domains((x,y,lo,hi))
    H = set().union(*(p.library(o) for o in (x,y,lo,hi)))
    qa = tuple(sorted((x+4,y+4,lo+4)))
    qo = tuple(sorted((x+3,y+3,hi+3)))
    H.update((qa,qo))
    lh,lt = p.reg(lo,0); rh,rt = p.reg(lo,1)
    uh,ut = p.reg(hi,0); vh,vt = p.reg(hi,1)
    opening = [p.one(x+1), p.one(y+1)]
    left = [p.add(qa),p.add(lt),p.add(rt)]
    right = [p.add(qo),p.add(vt),p.add(ut)]
    cleanup = [p.one(x+4),p.one(x+3),p.one(y+5)]
    finish = [p.add(rh),p.add(lh),p.add(vh),p.add(uh)]
    return H, opening+left+right+cleanup+finish

def restoring(x=0,y=6,lo=12,hi=18):
    """Open both once; 7+7 independent-port bodies; restore both once."""
    H,_ = joint(x,y,lo,hi)
    def body(out, sign):
        port = 4 if sign == 'AND' else 3
        q = tuple(sorted((x+port,y+port,out+port)))
        lh,lt=p.reg(out,0);rh,rt=p.reg(out,1)
        first,second=(lt,rt) if sign=='AND' else (rt,lt)
        return [p.add(q),p.add(first),p.add(second),p.one(out+port),
                p.add(first),p.add(rh),p.add(lh)]
    bodies=[body(lo,'AND'),body(hi,'OR')]
    opening=[p.one(x+1),p.one(y+1)]
    closing=[p.add(p.reg(o,b)[0]) for o in (x,y) for b in (0,1)]
    return H,opening,bodies,closing

def sq_observer(bits):
    terms=[ONE if b else ZERO for b in bits]
    return f.total(r.serial(v,v) for v in terms)

def cases():
    H,W=joint(); out=[]
    ck(len(W)==15 and len(set().union(*H))==24,'15 commands / 24 members')
    HR,opening,bodies,closing=restoring()
    for bits in product((0,1),repeat=2):
        J=init(bits,(0,6)); ans=f.execute(J,W,H,True)
        v=(bits[0]&bits[1],bits[0]|bits[1]); wanted=init(v,(12,18))
        ck(ans['end']==wanted,'exact joint endpoint and both operands consumed')
        ck(sq_observer(bits)==sq_observer(v),'BRC square observer preserved at endpoint')
        rr=f.execute(J,opening+sum(bodies,[])+closing,HR,True)
        ck(rr['end']==m.canon(J+wanted),'20-step both-input restoration')
        # Existing preserving AND followed by consuming OR is a 23-step baseline.
        ha,wa=d.preserving_gate(0,6,12);ho,wo=d.direct_gate(0,6,18,'OR')
        seq=f.execute(J,wa+wo,ha|ho)
        ck(len(wa+wo)==23 and seq['end']==wanted,'23-step legitimate shared-input baseline')
        # Preserve the orientation in one real six-member register before sorting.
        hc,wc=p.copy_program(0,24,31)
        remembered=f.execute(J,wc+W,H|hc,True)
        ck(remembered['end']==m.canon(wanted+p.reg(24,bits[0])), 'actual copied source witness remains')
        low,high,orientation=(p.read(remembered['end'],o) for o in (12,18,24))
        recovered=(orientation,low | (high & (1-orientation)))
        ck(recovered==bits,'ordered input reconstructed from comparator outputs plus source bit')
        out.append(dict(bits=bits,joint=ans,restoring=rr,baseline_length=23,
                        square_CWM=e.cw(sq_observer(v)),with_orientation=remembered))
    ck(out[1]['joint']['end']==out[2]['joint']['end'],'01/10 full endpoint collision')
    # A future copy can distinguish the two original orientations, not sorted endpoints.
    hc,wc=p.copy_program(0,24,31)
    aa=f.execute(init((0,1),(0,6)),wc,hc|p.library(6))
    bb=f.execute(init((1,0),(0,6)),wc,hc|p.library(6))
    ck(p.read(aa['end'],24)==0 and p.read(bb['end'],24)==1,'same original square sum not future equivalent')
    return dict(rows=out,source_distinguishing_copy=[aa,bb])

def preserving_shuffles():
    H,opening,words,closing=restoring(); records=[]
    for bits in product((0,1),repeat=2):
        J=init(bits,(0,6)); start=f.execute(J,opening,H)['end']
        states={((0,0),start):e.prep(start)}; peak=1
        tails=set(start)
        for depth in range(14):
            nxt={}
            for (pcs,K),mass in states.items():
                for i,pos in enumerate(pcs):
                    if pos==7:continue
                    pp=list(pcs);pp[i]+=1
                    L,_=f.step(K,words[i][pos],H)
                    ck(tails<=set(L),'source tails stay physically present in every interleaving')
                    f.put(nxt,(tuple(pp),L),r.serial(mass,ONE))
            states=nxt;peak=max(peak,len(states))
        merged={}
        expected=m.canon(J+init((bits[0]&bits[1],bits[0]|bits[1]),(12,18)))
        for (_,K),mass in states.items():
            L=f.execute(K,closing,H)['end'];ck(L==expected,'all body shuffles preserve exact endpoint')
            f.put(merged,L,mass)
        total=f.total(merged.values());positional=d.b.old.positional_mass((7,7),0,0)[0]
        ck(total==positional,'all shuffles accounted by independent positional CWM')
        records.append(dict(bits=bits,lengths=(7,7),CWM=e.cw(total),peak_states=peak,
                            endpoints=len(merged)))
    return records

def protected_gates():
    H,W=joint(); families=[]; needed=[]
    for slot in range(15):
        witness=None
        for bits in product((0,1),repeat=2):
            z=f.execute(init(bits,(0,6)),W,H,omitted=(slot,))
            expected=init((bits[0]&bits[1],bits[0]|bits[1]),(12,18))
            if z['end']!=expected:
                witness=dict(slot=slot+1,bits=bits,end=z['end']);break
        ck(witness is not None,'each base position has an omission failure')
        needed.append(witness)
    for bits in product((0,1),repeat=2):
        J=init(bits,(0,6));expected=init((bits[0]&bits[1],bits[0]|bits[1]),(12,18))
        for budget in (1,2):
            word=d.a.rep(W,budget);states={(J,0):e.prep(J)}
            for op in word:
                nxt={}
                for (K,used),mass in states.items():
                    L,_=f.step(K,op,H);f.put(nxt,(L,used),r.serial(mass,ONE))
                    if used<budget:f.put(nxt,(K,used+1),r.serial(mass,ONE))
                states=nxt
            layers={}
            for (K,used),mass in states.items():
                ck(K==expected,'budgeted omissions preserve joint complete endpoint')
                f.put(layers,used,mass)
            ck(layers==d.a.layers(len(word),budget),'all omitted-position histories retained')
            families.append(dict(bits=bits,budget=budget,commands=len(word),
                         layers=[dict(omitted=j,CWM=e.cw(v)) for j,v in sorted(layers.items())]))
    return dict(families=families,necessary_positions=needed)

def network(n):
    """Fixed bubble comparison network, reusing two empty registers.

Logical wire -> physical register assignment depends on the schedule, not values.
"""
    if not 2<=n<=6:raise ValueError('This finite execution suite uses 2..6 inputs')
    wires=[6*i for i in range(n)];free=[6*n,6*(n+1)];H=set();W=[];stages=[]
    for limit in range(n-1,0,-1):
        for i in range(limit):
            x,y=wires[i:i+2];lo,hi=free
            h,w=joint(x,y,lo,hi);H|=h;W+=w
            wires[i:i+2]=[lo,hi];free=[x,y]
            stages.append(dict(end=len(W),wires=tuple(wires),free=tuple(free)))
    return H,W,stages,wires,free

def sorting():
    results=[]
    for n in range(2,7):
        H,W,stages,wires,free=network(n); fibers={};origins={};runs=[]
        ck(len(set().union(*H))==6*(n+2),'n full registers and two recycled empty ones')
        for bits in product((0,1),repeat=n):
            K=init(bits,[6*i for i in range(n)]);before=sq_observer(bits);mass=e.prep(K);at=0;trace=[]
            for stage in stages:
                z=f.execute(K,W[at:stage['end']],H,keep=(n==3 and bits==(1,0,1)))
                K=z['end'];at=stage['end'];mass=r.serial(mass,ONE)
                observed=tuple(p.read(K,o) for o in stage['wires'])
                ck(all(v in (0,1) for v in observed),'all network gate boundaries carry full bits')
                ck(K==init(observed,stage['wires']),'no unexpected bridge or old input remains')
                ck(sq_observer(observed)==before,'CWM square signal preserved after each comparator')
                if z['trace']:trace.extend(z['trace'])
            observed=tuple(p.read(K,o) for o in wires)
            ck(observed==tuple(sorted(bits)),'fixed adjacent comparator sequence sorts every tested word')
            f.put(fibers,observed,mass);origins.setdefault(observed,[]).append(bits)
            runs.append(dict(input=bits,output=observed,end=K,trace=trace))
        total=f.total(fibers.values());input_total=f.total(ONE for _ in product((0,1),repeat=n))
        ck(total==input_total,'all original unit histories conserved after output-only merge')
        results.append(dict(n=n,commands=len(W),comparators=len(stages),members=len(set().union(*H)),
                    wire_registers=wires,empty_registers=free,CWM=e.cw(total),
                    fibers=[dict(output=k,origins=origins[k],CWM=e.cw(v)) for k,v in sorted(fibers.items())],
                    runs=runs))
    return results

def failures():
    H,W=joint();J=init((0,1),(0,6))
    ha,wa=d.direct_gate(0,6,12,'AND');ho,wo=d.direct_gate(0,6,18,'OR')
    sequential=f.execute(J,wa+wo,ha|ho,True)
    ck(tuple(p.read(sequential['end'],o) for o in (12,18))==(0,0), 'two consuming calls on same operands lose the second result')
    early=W[:5]+W[8:11]+W[5:8]+W[11:]
    zz=f.execute(init((1,0),(0,6)),early,H,True)
    ck(zz['end']!=init((0,1),(12,18)),'cleanup before second decision is unsound')
    # Missing input is not Boolean zero: the admission condition cannot be removed.
    partial=f.execute(p.reg(6,1),W,H,True)
    return dict(double_consume=sequential,early_cleanup=zz,missing_input=partial)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['cases','shuffle','faults','sorting','all'],default='all');parser.add_argument('--output',default='results.json');args=parser.parse_args()
    run={'cases':lambda:dict(cases=cases(),failures=failures()),'shuffle':preserving_shuffles,'faults':protected_gates,'sorting':sorting}
    data={k:fun() for k,fun in run.items() if args.mode in (k,'all')}
    result=dict(mode=args.mode,new_checks=CHECKS,uncached_kernel_calls=f.CALLS,transition_uses=f.USES,data=data)
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='data'}))
if __name__=='__main__':main()
