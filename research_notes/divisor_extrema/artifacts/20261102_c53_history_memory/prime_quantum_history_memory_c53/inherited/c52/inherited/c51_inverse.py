"""C51 finite joint-observer inversion. Integers/Fractions throughout.
The score-pair observer is sufficient for fixed-target terminal reweighting.
It is not claimed sufficient for arbitrary later insertion/deletion.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, math, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import c12_core
native=c12_core.native
Interval=tuple[F,F]

def add(a:Interval,b:Interval)->Interval:return a[0]+b[0],a[1]+b[1]
def sub(a:Interval,b:Interval)->Interval:return a[0]-b[1],a[1]-b[0]
def mul(a:Interval,b:Interval)->Interval:
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def div(a:Interval,b:Interval)->Interval:
    if b[0]<=0<=b[1]:raise ValueError('Division interval contains zero')
    return mul(a,(min(1/b[0],1/b[1]),max(1/b[0],1/b[1])))
def scale(a:Interval,k:F)->Interval:return mul(a,(F(k),F(k)))

def ln_unit(x:F,n:int=90)->Interval:
    """Exact atanh expansion, x in [1,2]."""
    if not 1<=x<=2:raise ValueError('ln_unit domain')
    z=(x-1)/(x+1)
    ans=sum((2*z**(2*j+1)/F(2*j+1) for j in range(n)),F())
    rem=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return ans,ans+rem

@lru_cache(None)
def log_interval(x:F,n:int=90)->Interval:
    x=F(x)
    if x<=0:raise ValueError('Log requires positive input')
    k=x.numerator.bit_length()-x.denominator.bit_length()
    while x<F(2)**k:k-=1
    while x>=F(2)**(k+1):k+=1
    return add(ln_unit(x/F(2)**k,n),scale(ln_unit(F(2),n),F(k)))

def log_box(x:Interval)->Interval:
    return log_interval(x[0])[0],log_interval(x[1])[1]

def integer_root(n:int,k:int)->int:
    if n<0 or k<=0:raise ValueError('Invalid root')
    if n<2:return n
    lo=0;hi=1<<((n.bit_length()+k-1)//k)
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    return lo

def root_interval(x:F,k:int,bits:int=100)->Interval:
    n=(x.numerator<<(k*bits))//x.denominator
    r=integer_root(n,k); den=1<<bits
    assert (F(r,den))**k<=x<(F(r+1,den))**k
    return F(r,den),F(r+1,den)

def words(counts:tuple[int,...]):
    def gen(left,prefix):
        if not any(left):yield tuple(prefix);return
        for i,a in enumerate(left):
            if a:
                nxt=list(left);nxt[i]-=1
                yield from gen(tuple(nxt),prefix+[i])
    yield from gen(counts,[])

def raw_scores(word:tuple[int,...])->tuple[int,int]:
    c=[word.count(i) for i in range(4)]
    # Route differences in order 2,3,5,7, with hidden coefficient separated.
    delta={(0,1):1,(0,2):-1,(0,3):1,(1,2):1,(1,3):-1}
    r=0;i57=0;used=[0]*4
    for p in word:
        r+=sum(used[j]*delta.get((j,p),0) for j in range(p))
        if p==3:i57+=used[2]
        used[p]+=1
    H0=sum(c[i]*c[j]*d for (i,j),d in delta.items())
    return 2*r-H0,2*i57-c[2]*c[3]

def joint_dp(counts:tuple[int,...])->Counter:
    """Retain counts and both signed scores until the terminal observer."""
    delta={(0,1):1,(0,2):-1,(0,3):1,(1,2):1,(1,3):-1}
    @lru_cache(None)
    def go(used):
        if used==counts:return {(0,0):1}
        out=Counter()
        for p in range(4):
            if used[p]<counts[p]:
                nxt=list(used);nxt[p]+=1
                dr=sum(used[j]*delta.get((j,p),0) for j in range(p))
                di=used[2] if p==3 else 0
                for (r,i),n in go(tuple(nxt)).items():out[r+dr,i+di]+=n
        return dict(out)
    H0=sum(counts[i]*counts[j]*d for (i,j),d in delta.items())
    cd=counts[2]*counts[3]
    return Counter({(2*r-H0,2*i-cd):n for (r,i),n in go((0,0,0,0)).items()})

def rational_probabilities(hist:Counter,q:F,gamma:F):
    """Cancel common gamma^2 when B=+-1; half-integer gamma gives rational weights."""
    if any(B*B!=1 for A,B in hist):raise ValueError('This exact specialization requires one 5 and one 7')
    exps={key:F(A*A)+2*gamma*A*B for key,(A,B) in ((key,key) for key in hist)}
    if any(x.denominator!=1 for x in exps.values()):raise ValueError('Use a certified irrational-weight routine for this gamma')
    # A common exponent shift preserves all probabilities and avoids weights >1.
    shift=min(exps.values());masses={};total=native.weight_histogram([]);calls=0
    for key,n in hist.items():
        weight=q**int(exps[key]-shift)
        branch=native.histogram_serial(native.WeightHistogram.from_counts({F(1):n}),native.weight_histogram([weight]));calls+=1
        masses[key]=branch.total_mass
        total=native.histogram_recoalesce(total,branch);calls+=1
    assert total.count==sum(hist.values())
    return {key:x/total.total_mass for key,x in masses.items()},calls

def infer_1260(p0:Interval,pplus:Interval,pminus:Interval):
    # Multiplicities M(0,1)=24 and M(+-2,1)=18 are retained.
    u=scale(div(pplus,p0),F(4,3));v=scale(div(pminus,p0),F(4,3))
    lu,lv=log_box(u),log_box(v);ls=add(lu,lv)
    if ls[1]>=0:raise ValueError('Data do not bound q strictly below 1')
    beta=scale(ls,F(-1,8));gamma=div(sub(lu,lv),ls)
    product=mul(u,v)
    q=(root_interval(product[0],8)[0],root_interval(product[1],8)[1])
    return {'u':u,'v':v,'beta':beta,'q':q,'gamma':gamma}

def predicted_1260(hist,u:F,v:F):
    mass={}
    for (A,B),n in hist.items():
        k=A//2
        assert A==2*k and B in (-1,1)
        e1=k*(k+B)//2;e2=k*(k-B)//2
        assert e1>=0 and e2>=0
        mass[A,B]=n*u**e1*v**e2
    z=sum(mass.values())
    return {key:x/z for key,x in mass.items()}

def run():
    checked=0;word_count=0
    for a in range(1,4):
      for b in range(1,4):
       for c in range(0,3):
        for d in range(0,3):
         counts=(a,b,c,d)
         size=math.factorial(sum(counts))//math.prod(math.factorial(k) for k in counts)
         if size>40000:continue
         direct=Counter(raw_scores(w) for w in words(counts))
         assert direct==joint_dp(counts)
         checked+=1;word_count+=size
    h=joint_dp((2,2,1,1));assert sum(h.values())==180
    assert {A:n for (A,B),n in h.items() if B==1}=={-8:1,-6:3,-4:11,-2:18,0:24,2:18,4:11,6:3,8:1}
    heldout=0;calls=0;calibrations=0
    for q in (F(1,2),F(2,3),F(3,4),F(4,5)):
      for g in (F(-1),F(-1,2),F(0),F(1,2),F(1),F(3,2)):
        ps,ncalls=rational_probabilities(h,q,g);calls+=ncalls
        u=F(4,3)*ps[2,1]/ps[0,1];v=F(4,3)*ps[-2,1]/ps[0,1]
        assert u*v==q**8
        ans=infer_1260((ps[0,1],)*2,(ps[2,1],)*2,(ps[-2,1],)*2)
        assert ans['q'][0]<=q<=ans['q'][1]
        assert ans['gamma'][0]<=g<=ans['gamma'][1]
        predicted=predicted_1260(h,u,v);assert predicted==ps
        calibrations+=1;heldout+=15
    ps,n=rational_probabilities(h,F(1,2),F(1,2));calls+=n
    pboxes=[(p*F(99,100),p*F(101,100)) for p in (ps[0,1],ps[2,1],ps[-2,1])]
    err=infer_1260(*pboxes)
    assert err['q'][0]<F(1,2)<err['q'][1]
    assert err['gamma'][0]<F(1,2)<err['gamma'][1]
    # A focused altered holdout: preserve all three calibration probabilities.
    altered=ps.copy();eps=ps[4,1]/10
    altered[4,1]+=eps;altered[-4,-1]-=eps
    assert all(altered[k]==ps[k] for k in ((0,1),(2,1),(-2,1)))
    assert altered!=predicted_1260(h,F(1,64),F(1,4))
    # Exact divisor record for the chosen composite, independent of model weights.
    tau=[0]*1261
    for d in range(1,1261):
        for j in range(d,1261,d):tau[j]+=1
    assert tau[1260]==36 and max(tau[1:1260])==32
    out={'method':'integer joint histograms, unchanged BRC positive weights, rational log/root certificates',
         'histogram_checks':checked,'direct_word_evaluations':word_count,'finite_calibrations':calibrations,
         'held_out_fiber_probabilities':heldout,'BRC_serial_and_recoalesce_calls':calls,
         'multiplicities':[{'A':A,'B':B,'count':n} for (A,B),n in sorted(h.items())],
         'witness_input_probabilities':{'P_0_1':ps[0,1],'P_2_1':ps[2,1],'P_minus2_1':ps[-2,1]},
         'witness_corrected_odds':{'u':F(1,64),'v':F(1,4)},
         'one_percent_input_boxes':pboxes,'one_percent_parameter_bounds':err,
         'one_percent_parameter_decimal':{k:[float(a),float(b)] for k,(a,b) in err.items()},
         'altered_holdout_rejected':True,
         'divisor_record':{'N':1260,'tau':36,'max_before':32},
         'original_and_prediction':[{'A':A,'B':B,'probability':p} for (A,B),p in sorted(ps.items())]}
    (ROOT/'results'/'finite_inverse.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
    print({k:out[k] for k in ('histogram_checks','direct_word_evaluations','finite_calibrations','held_out_fiber_probabilities','one_percent_parameter_decimal')})
if __name__=='__main__':run()
