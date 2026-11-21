"""Exact elimination of three source phases and radial scale for a rational lattice.

B = A / denominator, det(A) = denominator**2, theta = p / q.
The resulting moment is a finite rational linear combination of rational
gamma-th powers. No floating arithmetic enters coverage or integration.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from collections import defaultdict
from pathlib import Path
import argparse, json, time


def candidates(A, d, p, q):
    a,b,c,e=A
    assert d>0 and a*e-b*c==d*d and 0<p<q
    t=min(p,q-p)
    # C = max row absolute sum / (2d), integer endpoint bound = 4Cd/t_theta.
    R=F(2*q*max(abs(a)+abs(b),abs(c)+abs(e)),t)
    mb=int(R*(abs(e)+abs(b))/(d*d))
    nb=int(R*(abs(c)+abs(a))/(d*d))
    vectors=[]
    for n in range(-nb,nb+1):
        for m in range(-mb,mb+1):
            if gcd(abs(m),abs(n))!=1:continue
            u=a*m+b*n;v=c*m+e*n
            if max(abs(u),abs(v))>R:continue
            # Orient by endpoint u, then v. The opposite is included later.
            if u<0 or (u==0 and v<0):continue
            marks=(q*u,(q-p)*u+p*v,q*v)
            vectors.append((marks,(m,n)))
    vectors.sort(key=lambda x:(max(abs(x[0][0]),abs(x[0][2])),sum(abs(z)for z in x[0])))
    kept=[]
    single_pruned=pair_pruned=0
    def dominates(w,v):
        return all((x==0 or x*y>0) and abs(x)<=abs(y) for x,y in zip(w,v))
    for v,n in vectors:
        if any(dominates(w,v) or dominates(tuple(-z for z in w),v) for w,_ in kept):
            single_pruned+=1;continue
        # If v succeeds, every endpoint-wise smaller vector also passes the
        # two endpoint cells. Two such middle intervals cover all middle phases
        # whenever their opposite signed lengths sum to at most 1/sigma.
        # Since sigma <= 1/max(|v0|,|v2|), the following is phase-uniform.
        positive=negative=None;zero=False
        for ww,_ in kept:
            for w in [ww,tuple(-z for z in ww)]:
                if not all((w[j]==0 or w[j]*v[j]>0) and abs(w[j])<=abs(v[j]) for j in [0,2]):continue
                m=w[1]
                if m==0:zero=True;break
                if m>0:positive=m if positive is None else min(positive,m)
                else:negative=-m if negative is None else min(negative,-m)
            if zero:break
        if zero or (positive is not None and negative is not None
                    and positive+negative<=max(abs(v[0]),abs(v[2]))):
            pair_pruned+=1;continue
        kept.append((v,n))
    return kept,{'initial_unoriented':len(vectors),'retained_unoriented':len(kept),
                 'single_direction_pruned':single_pruned,'two_direction_cover_pruned':pair_pruned,
                 'integer_box':[mb,nb],'integer_endpoint_radius':str(R)}


def endpoint_cells(coords,num,den):
    # Cut is (constant, slope) = a+b*lambda; sort at lambda=num/den.
    cuts={(0,0),(1,0)}
    for c in coords:
        for a,b in [(0,-c),(1,-c)]:
            value=a*den+b*num
            if 0<value<den:cuts.add((a,b))
    cuts=sorted(cuts,key=lambda z:z[0]*den+z[1]*num)
    cells=[]
    for l,h in zip(cuts,cuts[1:]):
        da,db=h[0]-l[0],h[1]-l[1]
        if da*den+db*num==0:continue
        mask=0
        for i,c in enumerate(coords):
            at=(l[0]+h[0])*den+(l[1]+h[1]+2*c)*num
            if 0<at<2*den:mask|=1<<i
        cells.append((da,db,mask))
    return cells


def curve(A,d,p,q):
    kept,meta=candidates(A,d,p,q)
    marks=[v for v,_ in kept]+[tuple(-z for z in v)for v,_ in kept]
    cols=list(zip(*marks))
    minM=min(max(abs(v[0]),abs(v[2])) for v in marks)
    breaks={minM}
    for col in cols:
        sizes={0}|{abs(z)for z in col}
        breaks.update(a+b for a in sizes for b in sizes if a+b>=minM)
    denominators=sorted(breaks,reverse=True)
    intervals=[]
    previous=None
    middle_cache={}
    for n in denominators:
        if previous is None:num,den=1,2*n
        else:num,den=previous+n,2*previous*n
        xc=endpoint_cells(cols[0],num,den)
        yc=endpoint_cells(cols[2],num,den)
        poly=[0,0,0,0]
        for xa,xb,xmask in xc:
            for ya,yb,ymask in yc:
                mask=xmask&ymask
                if mask not in middle_cache:
                    positive=negative=None;zero=False
                    for i,m in enumerate(cols[1]):
                        if not(mask>>i&1):continue
                        if m==0:zero=True;break
                        if m>0:positive=m if positive is None else min(positive,m)
                        else:negative=-m if negative is None else min(negative,-m)
                    middle_cache[mask]=(positive,negative,zero)
                positive,negative,zero=middle_cache[mask]
                if zero:continue
                ma=-1;mb=0
                for c in [positive,negative]:
                    if c is None or c*num>=den:ma+=1
                    else:mb+=c
                if ma*den+mb*num<=0:continue
                endpoint=[xa*ya,xa*yb+xb*ya,xb*yb]
                for k,v in enumerate(endpoint):
                    poly[k]+=v*ma;poly[k+1]+=v*mb
        if intervals and intervals[-1][2]==tuple(poly):
            intervals[-1]=(intervals[-1][0],n,tuple(poly))
        else:intervals.append((previous,n,tuple(poly)))
        previous=n
    assert intervals[-1][1]==minM
    meta.update({'radial_breaks':len(denominators),'polynomial_intervals':len(intervals),
                 'middle_sets':len(middle_cache),'scale_denominator':q*d,
                 'max_scale':str(F(q*d,minM))})
    return intervals,meta


def moment_terms(intervals,scale,gamma=F(1,10),cutoff=None):
    """Return rational-base -> rational-coefficient expression for E min(S,cutoff)^gamma."""
    terms=defaultdict(F)
    end=F(1,intervals[-1][1])
    if cutoff is not None:end=min(end,F(cutoff,scale))
    terms[end*scale]+=1
    for ln,hn,poly in intervals:
        low=F(0) if ln is None else F(1,ln)
        high=min(F(1,hn),end)
        if low>=high:continue
        for k,c in enumerate(poly):
            if c==0:continue
            coefficient=gamma*c/(gamma+k)
            terms[high*scale]-=coefficient*high**k
            if low:terms[low*scale]+=coefficient*low**k
    return {a:c for a,c in terms.items() if c}


def root_bounds(x,power=10,bits=100):
    x=F(x);D=1<<bits
    n=x.numerator*(D**power)//x.denominator
    lo,hi=0,1<<((n.bit_length()+power-1)//power)
    if hi**power<=n:hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if m**power<=n:lo=m
        else:hi=m
    return F(lo,D),F(hi,D)


def evaluate(terms,bits=100):
    lo=hi=F(0)
    for base,c in terms.items():
        a,b=root_bounds(base,bits=bits)
        if c>=0:lo+=c*a;hi+=c*b
        else:lo+=c*b;hi+=c*a
    return lo,hi


def encode_terms(terms):return [{'base':str(a),'coefficient':str(c)}for a,c in sorted(terms.items())]


def compare(A,d):
    result={'basis_integer':A,'basis_denominator':d,'positions':{}}
    expressions=[]
    for p,q in [(1,4),(1,2)]:
        start=time.time();intervals,meta=curve(A,d,p,q)
        terms=moment_terms(intervals,q*d);expressions.append(terms)
        lo,hi=evaluate(terms)
        result['positions'][f'{p}/{q}']={'coverage':meta,'moment_terms':encode_terms(terms),
              'interval':[str(lo),str(hi)],'display':[float(lo),float(hi)],'seconds':time.time()-start}
    diff=defaultdict(F)
    for a,c in expressions[0].items():diff[a]+=c
    for a,c in expressions[1].items():diff[a]-=c
    diff={a:c for a,c in diff.items()if c};lo,hi=evaluate(diff)
    result['difference']={'moment_terms':encode_terms(diff),'interval':[str(lo),str(hi)],
                          'display':[float(lo),float(hi)]}
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--basis',type=int,nargs=4,default=[1,0,0,1]);ap.add_argument('--denominator',type=int,default=1);ap.add_argument('--output',type=Path)
    args=ap.parse_args();result=compare(args.basis,args.denominator)
    out=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(out)
    print(out)
