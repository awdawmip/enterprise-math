"""Independent leaf-consistent exact path certificates, including mandatory bit guard facts.
Inference may use the complete table offline. Online fallback gets only actual responses."""
import argparse,json
from functools import cache
from itertools import product
from pathlib import Path
from oracle import Program,Worlds
from oracle_checks import examples

@cache
def certificate(x,keys,q):
    assert x not in keys
    return min((m for m in range(1<<q) if all((x^k)&m for k in keys)),key=lambda m:(m.bit_count(),m))

def optimal(p,x,entry=None):
    x=tuple(x);rows=[];dom=entry or (p.all,)*p.r
    def visit(pc,slots,d,needs,charge,trans):
        if pc<0:
            masks=tuple(certificate(x[i],tuple(sorted(ks)),p.q) for i,ks in enumerate(needs))
            rows.append((charge+8*sum(m.bit_count() for m in masks),trans,masks));return
        e=p.nodes[pc][0];kind=e[0];s=e[1]
        def actual(o):return x[o] if o>=0 else -o-1
        def end(obs,ss,dd,nn,fee):
            visit(p.dest(pc,obs),tuple(ss),tuple(dd),nn,charge+fee,trans+((pc,obs),))
        if kind=='round':
            for k in p.keys(s):
                if any(actual(o)==k for o in slots):continue
                new=[set(a) for a in needs]
                for o in set(slots):
                    if o>=0 and d[o]>>k&1:new[o].add(k)
                ss=list(slots);ss[e[2]]=-1-k
                end(k,ss,d,new,p.create_price(s,k))
        else:
            src=e[2] if kind=='copy' else s
            o=slots[src];val=actual(o);ss=list(slots);dd=list(d)
            if kind=='bit':
                mask=p.ones[e[2]];obs=(val>>e[2])&1;allowed=mask if obs else p.all^mask;fee=8
            elif kind=='copy' and src!=s:
                obs=val;allowed=1<<val;fee=p.cp(val);ss[s]=o
            else:
                obs=int(bool(val));allowed=p.all^1 if val else 1;fee=p.q+9 if kind=='drop' else 8
                if kind=='drop':ss[s]=-1
            if o>=0:dd[o]&=allowed
            end(obs,ss,dd,needs,fee)
    visit(len(p.nodes)-1,tuple(range(p.r)),tuple(dom),[set() for _ in x],0,())
    return min(rows)

def replay(p,hint,read,act,entry=None):
    D=list(entry or (p.all,)*p.r);masks=hint[2];path=dict(hint[1]);pc=len(p.nodes)-1;cost=0;rescues=0
    def get(i,b):
        nonlocal cost
        z=read(i,b);cost+=8;D[i]&=p.ones[b] if z else p.all^p.ones[b]
        assert D[i];return z
    for i,m in enumerate(masks):
        for b in range(p.q):
            if m>>b&1:get(i,b)
    while pc>=0:
        e=p.nodes[pc][0];kind=e[0];s=e[1];k=None
        if kind=='round':
            def safe(k):return k in p.keys(s) and not any(m>>k&1 for m in D)
            k=path.get(pc,-1)
            if not safe(k):
                rescues+=1
                if not any(safe(c) for c in p.keys(s)):
                    for i in range(p.r):
                        for b,one in enumerate(p.ones):
                            if D[i]&one and D[i]&~one:get(i,b)
                k=min((k for k in p.keys(s) if safe(k)),key=lambda k:(p.create_price(s,k),k))
        z,fee=act(e,k);cost+=fee
        if kind=='round':D[e[2]]=1<<k
        elif kind=='bit':D[s]&=p.ones[e[2]] if z else p.all^p.ones[e[2]]
        elif kind=='drop':D[s]=1
        elif e[1]==e[2]:D[s]&=p.all^1 if z else 1
        else:D[s]=D[e[2]]=1<<z
        pc=p.dest(pc,z)
    return cost,rescues

def harness(p,x,hint,entry=None):
    live=tuple(x)
    def rd(i,b):return live[i]>>b&1
    def do(e,k):
        nonlocal live
        z,live,fee=p.physical(e,live,k);return z,fee
    return replay(p,hint,rd,do,entry)

def run():
    suite=examples()[:6]
    p=Program(2);end=p.add(('round',0,1));drop=p.add(('drop',1),end)
    mid=p.add(('round',1,0),end,[(4,drop)]);gate=p.add(('bit',1,0),mid,[(1,end)])
    p.add(('round',0,0),gate);suite.append(('late_obligatory_bit',p))
    cases=[];n=0;replays=0;rescues=0
    for name,p in suite:
        w=Worlds(p);xs=list(product(range(p.limit+1),repeat=p.r));hints=set();scores=[]
        for x in xs:
            h=optimal(p,x);cost,miss=harness(p,x,h)
            assert cost==h[0]==w.value(x) and miss==0
            n+=1;scores.append(cost);hints.add(h)
        rr=0
        for h in hints:
            for x in xs:
                c,f=harness(p,x,h);rr+=int(f>0)
        replays+=len(hints)*len(xs);rescues+=rr
        cases.append(dict(program=name,pointwise_range=[min(scores),max(scores)],distinct_hints=len(hints),replays=len(hints)*len(xs),replays_using_fallback=rr))
    return dict(status='PASS',pointwise_matches=n,other_and_same_input_replays=replays,replays_using_fallback=rescues,cases=cases)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('path_results.json'));a=ap.parse_args();r=run();a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(r['pointwise_matches'],r['other_and_same_input_replays'],r['replays_using_fallback'])
