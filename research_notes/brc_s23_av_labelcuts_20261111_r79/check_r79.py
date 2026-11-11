#!/usr/bin/env python3
"""R79 exact latest-source decision, piecewise original-label cuts only.
No source-time phase cuts in the algorithm; independent full-R77 strata oracle
is used solely to validate small random models.
"""
from fractions import Fraction as Q
from math import floor, ceil
from random import Random
import json
from time import perf_counter

def frac(x):return x-floor(x)

def direct_present(t,j,x,a,b,z):
    A,B=frac(a*z),frac(b*z)
    S=frac(x+(t-j)*z)
    return (A<=S<B if A<B else (S>=A or S<B) if A>B else False)

def win(E,j,x,a,b,z):
    yes=[e for e in E if direct_present(e[0],j,x,a,b,z)]
    return max(yes) if yes else None

def integer_cuts_of_affine(slope,constant,L,U):
    if slope==0:return []
    lo,hi=sorted((slope*L+constant,slope*U+constant))
    return [(Q(k)-constant)/slope for k in range(ceil(lo),floor(hi)+1)]

def label_cuts(a,b,L,U):
    return sorted({L,U,*integer_cuts_of_affine(a,Q(0),L,U),
                   *integer_cuts_of_affine(b,Q(0),L,U),
                   *integer_cuts_of_affine(a-b,Q(0),L,U)})

def affine_point(alpha,beta,u,v,negative):
    pts=[u,v]
    if alpha:
        root=-beta/alpha
        if u<root<v:pts=[u,root,v]
    for A,B in zip(pts,pts[1:]):
        z=(A+B)/2
        h=alpha*z+beta
        if h<0 if negative else h>=0:return z
    return None

def source_open(e,j,x,a,b,u,v,ka,kb,q):
    t,branch=e
    # On this open label cell the canonical lifted membership test is {F}<w.
    fm=(u+v)/2
    slope=t-j-a
    def F(z):return x+slope*z+ka
    def width(z):return (b-a)*z+ka-kb+q
    assert 0<width(fm)<1
    fl,fr=F(u),F(v)
    low,high=min(fl,fr),max(fl,fr)
    k=floor(low)+1
    if low<k<high:
        # One full phase wrap inside the open cell ensures both possibilities.
        assert slope!=0
        z_yes=(Q(k)-x-ka)/slope
        w0=width(z_yes)
        assert u<z_yes<v and 0<w0<1
        delta=(1-w0)/8
        dw=abs(b-a)
        if dw:
            delta=min(delta,(1-w0)*abs(slope)/(8*dw))
        delta=min(delta,(Q(k)-low)/2)
        z_no=(Q(k)-delta-x-ka)/slope
        assert u<z_no<v and direct_present(t,j,x,a,b,z_yes) and not direct_present(t,j,x,a,b,z_no)
        return z_yes,z_no
    km=floor(F(fm))
    # If there is no interior phase integer, F's floor is fixed on (u,v).
    # The threshold H=F-km-w is one affine function.
    alpha=t-j-b
    beta=x+kb-km-q
    z_yes=affine_point(alpha,beta,u,v,True)
    z_no=affine_point(alpha,beta,u,v,False)
    assert (z_yes is None or direct_present(t,j,x,a,b,z_yes))
    assert (z_no is None or not direct_present(t,j,x,a,b,z_no))
    return z_yes,z_no

def interval_status(E,j,x,a,b,u,v):
    middle=(u+v)/2
    A,B=frac(a*middle),frac(b*middle)
    assert A!=B
    ka,kb=floor(a*middle),floor(b*middle)
    q=0 if A<B else 1
    for e in sorted(E,reverse=True):
        zi,zo=source_open(e,j,x,a,b,u,v,ka,kb,q)
        if zi is None:continue
        assert win(E,j,x,a,b,zi)==e
        if zo is None:return ('STABLE',e,zi)
        wout=win(E,j,x,a,b,zo)
        assert wout!=e
        return ('CHANGES',zi,zo,e,wout)
    return ('STABLE_NONE',None,middle)

def classify(E,j,x,a,b,L,U):
    assert L<=U
    if a==b:return {'status':'STABLE_NONE','label_cuts':2 if L<U else 1}
    cuts=label_cuts(a,b,L,U)
    first=None
    for i,z in enumerate(cuts):
        result=('STABLE',win(E,j,x,a,b,z),z)
        if first is None:first=(result[1],z)
        elif first[0]!=result[1]:
            return {'status':'CHANGES','in_theta':str(first[1]),'out_theta':str(z),
                    'winner_at_in':first[0],'winner_at_out':result[1], 'label_cuts':len(cuts)}
        if i+1>=len(cuts):continue
        open_result=interval_status(E,j,x,a,b,z,cuts[i+1])
        if open_result[0]=='CHANGES':
            assert win(E,j,x,a,b,open_result[1])!=win(E,j,x,a,b,open_result[2])
            return {'status':'CHANGES','in_theta':str(open_result[1]),'out_theta':str(open_result[2]),
                    'winner_at_in':open_result[3], 'winner_at_out':open_result[4], 'label_cuts':len(cuts)}
        if first[0]!=open_result[1]:
            return {'status':'CHANGES','in_theta':str(first[1]),'out_theta':str(open_result[2]),
                    'winner_at_in':first[0],'winner_at_out':open_result[1], 'label_cuts':len(cuts)}
    if first[0] is None:return {'status':'STABLE_NONE','label_cuts':len(cuts)}
    return {'status':'STABLE','winner':first[0],'label_cuts':len(cuts)}

def ref(E,j,x,a,b,L,U):
    cut={L,U}
    for coeff,c0 in [(a,Q(0)),(b,Q(0)),(a-b,Q(0))]:
        cut.update(integer_cuts_of_affine(coeff,c0,L,U))
    for t,_ in E:
        for coeff in (t-j,t-j-a,t-j-b):
            cut.update(integer_cuts_of_affine(coeff,x,L,U))
    cut=sorted(cut)
    pts=[]
    for i,z in enumerate(cut):
        pts.append(z)
        if i+1<len(cut):pts.append((z+cut[i+1])/2)
    W=[win(E,j,x,a,b,z) for z in pts]
    if all(w is None for w in W):return 'STABLE_NONE',None,len(pts)
    if all(w==W[0] for w in W):return 'STABLE',W[0],len(pts)
    return 'CHANGES',None,len(pts)

def run():
    rng=Random(791126)
    models=0;strata=0; stat={'STABLE_NONE':0,'STABLE':0,'CHANGES':0};lc=0;pointchecks=0
    for i in range(400):
        a=rng.randint(-4,4);b=rng.randint(-4,4)
        L=Q(rng.randint(-4,5),rng.randint(4,12))
        U=L+Q(rng.randint(0,8),rng.randint(6,15))
        x=Q(rng.randint(-5,5),rng.randint(1,9))
        E=list(set((rng.randint(-12,18),rng.randint(0,3)) for _ in range(rng.randint(0,8))))
        j=rng.randint(-3,4)
        r=classify(E,j,x,a,b,L,U)
        status,w,num=ref(E,j,x,a,b,L,U)
        assert r['status']==status,(i,a,b,E,L,U,r,status)
        if status=='STABLE':assert tuple(r['winner'])==w
        if status=='CHANGES':
            z1=Q(r['in_theta']);z2=Q(r['out_theta'])
            assert L<=z1<=U and L<=z2<=U
            assert win(E,j,x,a,b,z1)!=win(E,j,x,a,b,z2)
        models+=1;strata+=num;stat[status]+=1;lc+=r['label_cuts']
        for z in [L,U,(L+U)/2,L+(U-L)/5]:
            W=win(E,j,x,a,b,z)
            if status=='STABLE':assert W==w
            if status=='STABLE_NONE':assert W is None
            pointchecks+=1
    assert models==400
    # Source time can be huge; only original-label cuts are visited.
    large=[]
    for exp in (6,12,30,60,120):
        t=12*10**exp
        E=[(t,0)]
        r=classify(E,0,Q(0),1,2,Q(1,4),Q(1,3))
        assert r['status']=='CHANGES' and r['label_cuts']==2
        z1,z2=Q(r['in_theta']),Q(r['out_theta'])
        assert win(E,0,Q(0),1,2,z1)!=win(E,0,Q(0),1,2,z2)
        large.append({'time_bits':t.bit_length(),'label_cuts':r['label_cuts'],'status':r['status']})
    # Explicit original-boundary wrap/equality and branch-tie tests.
    E=[(5,1),(5,2),(7,1),(13,4)]
    for a,b,L,U in [(3,1,Q(1,5),Q(2,5)),(3,1,Q(1,4),Q(1,3)),(1,2,Q(1,4),Q(1,3)),(2,1,Q(-1,3),Q(1,2))]:
        r=classify(E,0,Q(1,7),a,b,L,U)
        assert r['status']==ref(E,0,Q(1,7),a,b,L,U)[0]
    return {'seed':791126,'random_models':models,'independent_full_strata':strata,
            'point_checks':pointchecks,'statuses':stat,'sum_label_cutpoints':lc,
            'large_time_models':large,'assertions':'PASS'}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2))
    with open('/mnt/data/em_r78/verification_r79.json','w') as f:json.dump(result,f,indent=2)
