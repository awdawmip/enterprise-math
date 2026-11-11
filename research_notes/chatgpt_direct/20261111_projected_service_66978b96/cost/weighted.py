"""Variable business length; minimize paid read commands plus exact preserved service.
Run from a package root containing projected/ and copylife/. Standard library."""
import argparse,json,sys
from functools import cache
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent))
from projected.kernel.subset_kernel import prefix,initial,emit,marker_slot,least_one,core

tests={j:sum(1<<h for h in range(8) if (h==j if j<8 else bool(h&(1<<(j-8))))) for j in range(1,11)}
states=lambda S:[h for h in range(8) if S&(1<<h)]
def business(k):
    return 97+2*k.bit_count()+4*int(k&8==0)
def demand(m):return list(range(1,8))+[1]*m
def chosen(h,m):return [15 if k==h else k for k in demand(m)]
def weights(m):return [sum(map(business,chosen(h,m))) for h in range(8)]
def solver(base):
    @cache
    def f(S,remaining):
        if S.bit_count()==1:return (base[states(S)[0]],0,0)
        if remaining<=0:return (float('inf'),0,0)
        opts=[]
        for j,M in tests.items():
            a,b=S&M,S&~M
            if a and b:
                va,da,_=f(a,remaining-1);vb,db,_=f(b,remaining-1)
                opts.append((8+max(va,vb),1+max(da,db),j))
        return min(opts)
    return f

def constrained(depth=7):
    # h=1 has depth cap t, all other worlds minimize max(fixed business+8*own depth).
    base=weights(0)
    @cache
    def V(S,t,left):
        if S==2:return -float('inf') if t>=0 else float('inf')
        if S&2 and t<=0:return float('inf')
        if S.bit_count()==1:return base[states(S)[0]]
        if not left:return float('inf')
        return 8+min(max(V(S&M,t-1,left-1),V(S&~M,t-1,left-1)) for M in tests.values() if S&M and S&~M)
    return [V(255,t,depth) for t in range(1,8)]
def runone(C,m,cap,h):
    P=prefix(C,initial(h));pref=P.cost
    f=solver(weights(m));u=255;l=cap;trace=[]
    # Controller receives a physical reader only; family and prices are public.
    while u.bit_count()>1:
        _,_,j=f(u,l)
        v=P.probe(marker_slot(j),least_one(j));trace.append([j,v])
        u&=tests[j] if v else ~tests[j]
        l-=1
    recovered=states(u)[0];keys=chosen(recovered,m)
    after=P.cost;table=P.codes();jobs=emit(P,keys)
    assert (P.codes()==table and keys==chosen(h,m) and P.cost-after==weights(m)[h]
            and all(sum(row['words'])==business(k) for row,k in zip(jobs,keys)))
    return dict(h=h,decisions=trace,delivered=keys,pre=pref,business=P.cost-after,total=P.cost)
def run():
    intercepts=constrained();assert intercepts==[765,763,757,757,757,757,757]
    assert constrained(depth=4)[:3]==intercepts[:3]
    cases=[]
    for m in range(65):
        w=weights(m);f=solver(w)
        pred=min(max(c+103*m,733+105*m+8*t) for t,c in enumerate(intercepts,1))
        assert pred==f(255,7)[0] and f(255,3)[0]==757+105*m
        cases.append(dict(m=m,min_commands=pred,best_at_depth3=f(255,3)[0],min_depth_at_optimum=f(255,7)[1]))
    C=core.prior.Compiler(slots=15);real=[]
    for m in (3,4,8,9,12):
        for cap in (3,7):
            traces=[runone(C,m,cap,h) for h in range(8)]
            assert max(a['total']-a['pre'] for a in traces)==solver(weights(m))(255,cap)[0]
            real.append(dict(m=m,depth_cap=cap,paths=traces,worst=max(a['total'] for a in traces)))
    return dict(status='PASS',footnote='fixed 15-slot emitter, fallback 15 for this test; numbers in finite_cases exclude pre, physical includes pre; decision interface may probe existing marker bits only',intercepts=intercepts,finite_cases=cases,real_runs=80,physical=real)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'weighted_results.json');a=ap.parse_args()
    out=run();a.out.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print('weighted ok',out['real_runs'],[(x['m'],x['depth_cap'],x['worst']) for x in out['physical']])
