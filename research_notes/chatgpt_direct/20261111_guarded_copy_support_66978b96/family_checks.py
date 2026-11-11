"""Fixed-observation endogenous copy fanout: optimal predecision read crossover.
Independent single-unknown minimax and unmodified BRC business words."""
from pathlib import Path
from functools import cache
import json,argparse,sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from copylife.kernel_checks import Physical,core

def pars(b):
    B=1<<b;r=B-2;q=b+2
    assert (3*(B-1)).bit_length()==q
    D=8*b+2*q+41
    return B,r,q,D
def predicted(b,m):
    B,r,q,D=pars(b);C=r*(q+9)+2*D+10;g=9*q+7
    return C+8+g*m+min(m,8*(q-1))
def exact(b,m):
    B,r,q,D=pars(b);n=3*(B-1)
    choices=tuple(range(B,2*B-1))
    w=lambda k:2*k.bit_count()+4*(1-((k>>(b-1))&1))
    g=lambda k:9*q+2+k.bit_count()+4*(1-((k>>(q-1))&1))
    scores=[(k, min(w(k)+w(l)+m*g(k) for l in choices if l!=k),
                 min(w(k)+w(l)+m*g(l) for l in choices if l!=k)) for k in choices]
    masks=[sum(1<<i for i in range(n+1) if (i>>j)&1) for j in range(q)]
    @cache
    def before(U):
        ans=10**16
        for k,negative,positive in scores:
            if (U>>k)&1:continue
            price=max(negative if U&1 else 0,positive if U&~1 else 0)
            ans=min(ans,price)
        for test in masks:
            a=U&test;d=U&~test
            if a and d:ans=min(ans,8+max(before(a),before(d)))
        assert ans<10**16
        return ans
    return r*(q+9)+2*D+before((1<<(n+1))-1)
def physical(C,b,m,method,y):
    B,r,q,D=pars(b);h=B//2;a=B;c=B+h
    initial=tuple(y if i==1 else ((3*i+1)%(3*(B-1)+1)) for i in range(r))
    p=Physical(C,initial)
    for i in range(r):
        if i!=1:p.drop(i)
    if method=='short':
        k=a if p.probe(1,b-1) else c
    elif p.probe(1,0):k=c
    elif p.probe(1,b-1):k=a+1
    else:
        nonzero=any(p.probe(1,j) for j in range(q) if j not in (0,b-1))
        k=c if nonzero else a
    npre=p.probes
    p.round(1,0,k);assert p.events[-1]['key']==k
    p.drop(1);positive=bool(p.C.observe_result(p.J))
    l=c if k==a else a
    p.round(1,1,l);assert p.events[-1]['key']==l
    for _ in range(m):p.copy(0,1) if positive else p.copy(1,0)
    assert p.probes==npre
    return dict(y=y,first=k,second=l,guard=positive,read_count=npre,actual=p.cost)
def run():
    selects=[]
    for b in range(2,7):
        _,_,q,_=pars(b);L=8*(q-1)
        for m in sorted(set([0,1,2,L-1,L,L+1,L+7])):
            val=exact(b,m);assert val==predicted(b,m)
            selects.append(dict(b=b,r=(1<<b)-2,m=m,value=val))
    actual=[]
    for b in (2,3):
        B,r,q,D=pars(b);comp=core.prior.Compiler(slots=r);L=8*(q-1)
        for m in (L,L+1):
            methods={}
            for method in ('short','identify'):
                paths=[physical(comp,b,m,method,y) for y in range(3*(B-1)+1)]
                methods[method]=dict(worst=max(z['actual'] for z in paths),paths=paths)
            H=r*(q+9)+2*D+10;g=9*q+7
            assert methods['short']['worst']==H+8+(g+1)*m
            assert methods['identify']['worst']==H+8*q+g*m
            assert min(z['worst'] for z in methods.values())==predicted(b,m)
            actual.append(dict(b=b,r=r,m=m,cases=methods))
    return dict(status='PASS',scope='original BRC: each surviving full key y for the stated two/six-slot preparations; other initial slots follow a fixed nontrivial pattern and are obligatorily dropped. Exact theorem concerns every independent old table.',independent_uniform_DPs=selects,physical_runs=sum(len(z['paths']) for row in actual for z in row['cases'].values()),original_runs=actual)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('family_results.json'));a=ap.parse_args();z=run();a.out.write_text(json.dumps(z,indent=2,sort_keys=True)+'\n');print(len(z['independent_uniform_DPs']),z['physical_runs'])
