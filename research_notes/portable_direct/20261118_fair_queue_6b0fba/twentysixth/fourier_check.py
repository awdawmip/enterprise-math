"""Order-blind bounded low-bit tests. All probability brackets use exact rational arithmetic."""
from collections import Counter
from fractions import Fraction as F
from functools import cache
from math import gcd, isqrt
import json


def ceiling(x):
    return -((-x.numerator)//x.denominator)


def bracket(lo,hi,bits=60):
    den = 1<<bits
    return F((lo*den).__floor__(),den),F(ceiling(hi*den),den)


def display(interval):
    return [str(v) for v in interval]


@cache
def cosine(d,j,bits):
    """Outward dyadic bracket for cos(pi*j/d), with d a power of two."""
    j %= 2*d
    if j>d:
        return cosine(d,2*d-j,bits)
    if j==0: return F(1),F(1)
    if j==d: return F(-1),F(-1)
    if 2*j==d: return F(0),F(0)
    if 2*j>d:
        lo,hi=cosine(d,d-j,bits)
        return -hi,-lo
    lo,hi=cosine(d//2,j,bits)
    scale=1<<bits
    l=(1+lo)*scale**2/2
    u=(1+hi)*scale**2/2
    a,b=isqrt(l.__floor__()),isqrt(u.__floor__())
    return F(a,scale),F(b+int(b*b<u),scale)


def mass(d,s,b,bits=74):
    """s is an audited descriptor in this helper, never an input to the bit search."""
    if s>=d: return (F(1,d),)*2
    q,t=divmod(d,s)
    if s*b%d==0: return (F((s-t)*q*q+t*(q+1)**2,d*d),)*2
    if t==0: return (F(0),)*2
    precis=bits+8
    while True:
        dl,dh=cosine(d,2*s*b,precis)
        x,y=cosine(d,2*t*b,precis)
        z,w=cosine(d,2*(s-t)*b,precis)
        if dh<1:
            l=((s-t)*(1-y)+t*(1-w))/(d*d*(1-dl))
            h=((s-t)*(1-x)+t*(1-z))/(d*d*(1-dh))
            if h-l < F(1,1<<bits):
                return bracket(max(F(0),l),min(F(1),h),bits)
        precis*=2


class Ring:
    def __init__(self,n):
        self.n=n
        self.counts=Counter()
    def mul(self,x,y):
        self.counts["modular_multiplications"]+=1
        return x*y%self.n
    def power(self,x,n):
        y=1
        while n:
            if n&1: y=self.mul(y,x)
            n//=2
            if n: x=self.mul(x,x)
        return y
    def inverse(self,x):
        self.counts["inverses"]+=1
        return pow(x,-1,self.n)
    def project(self,a,depth):
        for _ in range(depth):
            a=self.mul(a,a)
        return a


class Blocks:
    def __init__(self,ring,g,width):
        self.ring=ring
        self.width=width
        self.table={}
        u=1
        for i in range(width):
            self.table.setdefault(u,i)
            u=ring.mul(u,g)
        self.stride=ring.inverse(u)
    def locate(self,target,count):
        for start in range(0,count,self.width):
            self.ring.counts["giant_probes"]+=1
            i=self.table.get(target)
            if i is not None and start+i<count: return start+i
            if start+self.width<count: target=self.ring.mul(target,self.stride)
        return None


def factor_from_odd(ring,a,h,j):
    z=ring.power(a,h)
    if z==1: return {"status":"odd original order","two_exponent":0}
    for v in range(1,j+1):
        w=ring.mul(z,z)
        if w==1:
            ring.counts["factor_gcds"]+=2
            factors=[gcd(z-1,ring.n),gcd(z+1,ring.n)]
            return {"status":"proper" if any(1<f<ring.n for f in factors) else "trivial",
                    "two_exponent":v, "half_power":z,"gcd_pair":factors}
        z=w
    raise AssertionError("unverified odd return")


def cutoff(d,threshold,cost=None):
    low,high=0,d//2
    gap=abs(threshold-F(1,2))
    while low<high:
        mid=(low+high)//2
        h=d+1+2*mid
        if cost is not None: cost["cutoff_integer_comparisons"]+=1
        if 2*(2*d*gap)**2 <= (2*d-h)**2: low=mid+1
        else: high=mid
    return low


def same_threshold_cell(d,lo,hi):
    return (hi<F(1,2) or lo>F(1,2)) and cutoff(d,lo)==cutoff(d,hi)


def random_input_cell(d,bits):
    # For a uniform-certified quarter prefix use sequential independent fair bits.
    value=0
    for j,bit in enumerate(bits,1):
        value=2*value+bit
        lo,hi=F(value,1<<j),F(value+1,1<<j)
        if same_threshold_cell(d,lo,hi):
            return (lo+hi)/2,j
    return None


def quarter_decision(n,h,b,d,threshold):
    # For b=d/4 and h odd, cos(pi*b*h/d) is +/-1/sqrt(2).
    assert b==d//4 and h%2
    sign=1 if h%8 in (1,7) else -1
    shift=threshold-F(1,2)
    if shift*sign<0: return int(sign<0)
    compare=2*(n*shift)**2-(n-h)**2
    if sign>0: return int(compare>=0)
    return int(compare<=0)


def tie_at_threshold(d,s,b,threshold):
    # Compare child and parent over the primitive 2d-th root basis 1,...,z^(d-1).
    poly=[0]*d
    def add(exp,coeff):
        index=exp%(2*d)
        poly[index%d] += coeff if index<d else -coeff
    for size,power,weight in ((2*d,1,threshold.denominator),(d,2,-4*threshold.numerator)):
        add(0,size*weight)
        for h in range(s,size,s):
            add(power*b*h,(size-h)*weight)
            add(-power*b*h,(size-h)*weight)
    return not any(poly)


def slow_comparison(d,s,b,threshold):
    bits=24
    while True:
        lower,upper=mass(d,s,b,bits)
        if upper==0: return {"unreachable":True}
        lower=max(lower,F(2,3*d*d))
        child_lo,child_hi=mass(2*d,s,b,bits)
        l,h=child_lo/upper,min(F(1),child_hi/lower)
        if threshold<l or threshold>=h:
            return {"bit":int(threshold>=h),"probability_zero":display(bracket(l,h)),"precision":bits}
        if bits==24 and tie_at_threshold(d,s,b,threshold):
            return {"bit":1,"exact_tie":True,"precision":bits}
        bits*=2


def query(modulus,a,m,k,b,threshold):
    """One quarter-prefix query; 0<=threshold<1. Counts include cold parent certification."""
    d=1<<k
    n=2*d
    assert k>=2 and k<m and b==d//4 and 0<=threshold<1 and gcd(a,modulus)==1
    ring=Ring(modulus); j=m-k-1
    child=ring.project(a,j)
    parent=ring.mul(child,child)
    width=isqrt(d-1)+1
    blk=Blocks(ring,parent,width)
    ring.counts['baby_keys']=len(blk.table)
    prior=blk.locate(ring.inverse(parent),d-1)
    if prior is not None:
        s=prior+1
        if s%2==0 or ring.power(child,s)!=1:
            lower,upper=mass(d,s,b)
            if upper==0: return {"unreachable":True,"cost":dict(ring.counts)}
            return {"bit":int(threshold>=F(1,2)),"fair":True,"cost":dict(ring.counts)}
        lower,upper=mass(d,s,b)
        if upper==0: return {"unreachable":True,"cost":dict(ring.counts)}
        factor=factor_from_odd(ring,a,s,j)
        out=slow_comparison(d,s,b,threshold)
        out.update(factor=factor,cost=dict(ring.counts))
        return out
    # Algebraic endpoint envelope: search only h for which a decision can change.
    count=cutoff(d,threshold,ring.counts)
    idx=None
    if count:
        target=ring.inverse(ring.power(child,d+1))
        idx=blk.locate(target,count)
    out={"tested_odd_candidates":count,"giant_width":width,"possible_odd_return_witness":None}
    if idx is None:
        out["bit"]=int(threshold>=F(1,2))
    else:
        h=d+1+2*idx
        assert ring.power(child,h)==1
        ring.counts["bit_algebraic_comparisons"]+=1
        out.update(bit=quarter_decision(n,h,b,d,threshold),possible_odd_return_witness=h,
                   factor=factor_from_odd(ring,a,h,j))
    out["cost"]=dict(ring.counts)
    return out


def work_joint(n,a,Q,d):
    """Complete work-label x low-residue joint for d=2 or 4; exact Gaussian integers."""
    fibers={}
    u=1
    for x in range(Q):
        fibers.setdefault(u,[]).append(x)
        u=u*a%n
    root=[(1,0),(0,1),(-1,0),(0,-1)]
    out={}
    for w,xs in sorted(fibers.items()):
        row=[]
        for b in range(d):
            cells={}
            for x in xs:
                t,z=divmod(x,Q//d)
                re,im=cells.get(z,(0,0))
                h,j=root[(4//d*b*t)%4]
                cells[z]=(re+h,im+j)
            row.append(F(sum(v*v+t*t for v,t in cells.values()),Q*d))
        out[w]=row
    assert sum(map(sum,out.values()))==1
    return out


def denominators(y,Q):
    p,q=y,Q
    old,cur=1,0
    while q:
        d,r=divmod(p,q)
        old,cur=cur,d*cur+old
        yield cur
        p,q=q,r


def event(a,n,y,Q):
    for q in denominators(y,Q):
        if 2<=q<=n and q%2==0 and pow(a,q,n)==1:
            h=pow(a,q//2,n)
            if any(1<gcd(h+s,n)<n for s in (-1,1)):
                return True
    return False


def main():
    d=256; b=64
    demos={str(u):query(1357,2,22,8,b,u) for u in
           [F(1,128),F(1,4),F(1,2),F(3,4),F(7,8),F(127,128)]}
    witness=[v for v in demos.values() if v["possible_odd_return_witness"] is not None]
    assert all(v["possible_odd_return_witness"]==319 and sorted(v["factor"]["gcd_pair"])==[23,59] for v in witness)
    root,top=cosine(4,1,90)
    # Independent threshold census over the equally-spaced midpoint grid.
    calls=Counter();bits=Counter(); total=1024
    for i in range(total):
        u=F(2*i+1,2*total)
        row=query(1357,2,22,8,b,u)
        hit=row["possible_odd_return_witness"] is not None
        calls["factor_exits"]+=hit
        for key,v in row["cost"].items(): calls[key]+=v
        bits[row["bit"]]+=1
        lower=F(1,2)+F(193,512)*root
        upper=F(1,2)+F(193,512)*top
        assert (row["bit"]==0 and u<lower) or (row["bit"]==1 and u>=upper)
    # For K=1,...,d/2-1, P(K=k)=2*cos(pi/4)/d; the two endpoints
    # have probabilities 1-(1-1/d)*cos(pi/4), cos(pi/4)/d.
    cost_k=[]
    for k in range(d//2+1):
        threshold=F(0) if k==0 else F(1,2) if k==d//2 else F(1,2)+(root+top)/2*(1-F(d+2*k,2*d))
        probe=query(1357,2,22,8,d//4,threshold)
        assert probe["tested_odd_candidates"]==k
        cost_k.append(probe["cost"]["modular_multiplications"])
    extra=-F(d-1,d)*cost_k[0]+F(2,d)*sum(cost_k[1:-1])+F(cost_k[-1],d)
    controls=[query(7,2,16,8,64,F(1,3)),query(15,2,3,2,1,F(1,2)),
              query(21,2,3,2,1,F(9,16))]
    assert controls[1]["unreachable"] and controls[2]["fair"]
    cell_counts={}
    for depth in (6,8,10,12):
        size=1<<depth
        undecided=sum(not same_threshold_cell(d,F(x,size),F(x+1,size)) for x in range(size))
        assert undecided<=2*(d+1)
        cell_counts[depth]=undecided
    source=(int(ch) for ch in "010010111010110011011010111010110010110100100110")
    representative,j=random_input_cell(d,source)
    stream_demo=query(1357,2,22,8,64,representative)
    # Enumerate a separate full work x low-bit readout and a finite CF verifier.
    Q=128; a=2; n=35
    joint=work_joint(n,a,Q,4)
    parent=work_joint(n,a,Q,2)
    assert all(joint[w][p]+joint[w][p+2]==parent[w][p] for w in parent for p in range(2))
    u=1; s=0
    while s<Q:
        u=u*a%n; s+=1
        if u==1: break
    assert s==12
    by_residue=[[F(0),F(0)] for _ in range(4)]
    all_mass=[[F(0),F(0)] for _ in range(4)]
    success=[]
    powers=[]; w=1
    for _ in range(Q):
        powers.append(w);w=w*a%n
    edges=Counter((i-j)%Q for i,v in enumerate(powers) for j,w in enumerate(powers) if v==w)
    for y in range(Q):
        l,h=mass(Q,s,y)
        ll=hh=F(0)
        for displacement,multiplicity in edges.items():
            aa,bb=cosine(Q,2*y*displacement,90)
            ll+=aa*multiplicity;hh+=bb*multiplicity
        assert max(l,ll/(Q*Q))<=min(h,hh/(Q*Q))
        totals=all_mass[y%4]
        totals[0]+=l; totals[1]+=h
        if event(a,n,y,Q):
            v=by_residue[y%4];v[0]+=l;v[1]+=h;success.append(y)
    for b in range(4):
        exact=sum(v[b] for v in joint.values())
        assert all_mass[b][0]<=exact<=all_mass[b][1]
    floor_tests=0
    for width in (2,4,8,16,32,64,128):
        for order in range(1,width+2):
            for y in range(width):
                l,h=mass(width,order,y)
                if h:
                    assert l+F(1,1<<70)>=F(2,3*width**2)
                floor_tests+=1
    finite_minima={}
    for width in (16,32,64,128):
        ml,mh=mass(width,3,1)
        for order in range(1,width+2):
            for y in range(width):
                l,h=mass(width,order,y)
                if h and (order!=3 or y not in (1,width-1)): assert mh<l
        finite_minima[width]=display((ml,mh))
    print(json.dumps({"sharp_finite_minima":finite_minima,"quarter_query":{"input":[1357,2,22,8,64],"thresholds":demos,
                           "uniform_grid_midpoint_trials":total,"grid_counts":dict(calls),
                           "bit_counts":dict(bits),"probability_zero":display(bracket(lower,upper)),
                           "expected_modmul_constant_plus_coefficient_times_cos_pi_4":[cost_k[0],str(extra)],
                           "full_search_cold_modmul":cost_k[-1], "cached_order_and_support_controls":controls,
                           "dyadic_threshold_undecided_cell_counts":cell_counts,
                           "deterministic_bit_tape_demo":{"random_bits_read":j,"out":stream_demo},
                           "factor_exit_probability":display(bracket(F(193,256)*root,F(193,256)*top))},
                      "work_joint_reference":{"input":[35,2,128],"residues_mod_4":{
                         str(w):[str(z) for z in row] for w,row in joint.items()},
                         "column_masses":[str(sum(v[b] for v in joint.values())) for b in range(4)],
                         "reference_first_return":s,"verified_frequency_list":success,
                         "success_mass_by_residue":list(map(display,by_residue)),
                         "full_success_mass":display((sum(x[0] for x in by_residue),sum(x[1] for x in by_residue)))},
                      "prefix_floor_comparisons":floor_tests},sort_keys=True,indent=2))


if __name__=="__main__":
    main()
