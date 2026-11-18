"""Independent rational, raw Fourier and binary64 edge checks. Run from this directory."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
import math
from random import Random
import sys

from envelope import ScalarPlan, VelocityPlan, upward
from leray_check import exact_column_norm

SOURCE = '9e24f54ea8640f5614a8d11a5d6a646562370846'


def fixture(dim, cutoff, count, label):
    """Held-out labels, frequency order, mask and coefficients derive from public SHA-256."""
    def h(tag,p,j=0):
        s = f'{SOURCE}|{dim}|{label}|{tag}|{p}|{j}'
        return int.from_bytes(sha256(s.encode('ascii')).digest(),'big')
    representatives = []
    for p in product(range(-cutoff,cutoff+1),repeat=dim):
        if next((v for v in p if v),0) > 0:
            representatives.append(p)
    representatives.sort(key=lambda p:h('location',p))
    points,rows,keep = [],[],[]
    for p in representatives[:count//2]:
        comps = []
        for j in range(2):
            iv = [int(h('numerator',p,2*i+j) % (2**22+1))-2**21 for i in range(dim)]
            power = (-30 - h('exponent',p,j)%25)
            if dim == 3:
                iv = [p[1]*iv[2]-p[2]*iv[1],p[2]*iv[0]-p[0]*iv[2],p[0]*iv[1]-p[1]*iv[0]]
            else:
                iv = iv[:1]
            comps.append([math.ldexp(v,power) for v in iv])
        row = tuple(complex(x,y) for x,y in zip(*comps))
        points.extend((p,tuple(-v for v in p)))
        rows.extend((row,tuple(z.conjugate() for z in row)))
        keep.extend([bool(h('retention',p)%4)]*2)
    assert len(rows) == count
    return points,rows,keep


def reference(dim,cutoff,points,rows,keep,mode):
    mass = [[F(abs(z.real))+F(abs(z.imag)) for z in row] for row in rows]
    if mode == 'angular':
        ds = [sum(x*x for x in p) for p in points]
        # Form the exact all-pairs rational numerator grouped by radii, without using the angular ordering.
        sums = {}
        for i,(x,y) in enumerate(points):
            for j in range(i):
                if (keep[i] and keep[j]) or ds[i]==ds[j]:
                    continue
                u,v=points[j]
                cross=abs(x*v-y*u)
                if cross:
                    key = tuple(sorted((ds[i],ds[j])))
                    sums[key] = sums.get(key,0) + cross*mass[i][0]*mass[j][0]
        return sum((1/F(a)-1/F(b))*value for (a,b),value in sums.items())
    if dim == 2:
        a,b = [F(0),F(0)],[F(0),F(0)]
        for p,row,k in zip(points,mass,keep):
            a[k] += F(sum(map(abs,p)),sum(x*x for x in p))*row[0]
            b[k] += max(map(abs,p))*row[0]
        return a[0]*b[1]+a[1]*b[0]+a[0]*b[0]
    a,b = [[F(0)]*3 for _ in range(2)],[[F(0)]*3 for _ in range(2)]
    for row,p,k in zip(mass,points,keep):
        for j in range(3):
            a[k][j] += row[j]
            b[k][j] += abs(p[j])*sum(row)
    return exact_column_norm(cutoff)*sum(a[1][j]*b[0][j]+a[0][j]*b[1][j]+a[0][j]*b[0][j] for j in range(3))


def raw_loss(dim,cutoff,points,rows,keep):
    # Direct ordered convolution of exact Gaussian rationals, then a projection for each output.
    table = {}
    zz=[[(F(z.real),F(z.imag)) for z in row] for row in rows]
    def mul(z,w):
        a,b=z; c,d=w
        return (a*c-b*d,a*d+b*c)
    for i,p in enumerate(points):
        for j,q in enumerate(points):
            k=tuple(a+b for a,b in zip(p,q))
            if (keep[i] and keep[j]) or max(map(abs,k))>cutoff:
                continue
            out = table.setdefault(k,[[F(0),F(0)] for _ in rows[j]])
            if dim == 2:
                weight = F(p[1]*q[0]-p[0]*q[1],sum(v*v for v in p))
                z = mul(zz[i][0],zz[j][0])
                for t in (0,1): out[0][t] += weight*z[t]
            else:
                dot = [sum(q[l]*zz[i][l][t] for l in range(3)) for t in (0,1)]
                for l,z in enumerate(zz[j]):
                    a,b = mul(dot,z)
                    out[l][0] += b
                    out[l][1] -= a
    total=F(0)
    for k,out in table.items():
        norm=sum(v*v for v in k)
        if dim==3 and norm:
            for t in (0,1):
                dot=sum(k[j]*out[j][t] for j in range(3))
                for j in range(3):
                    out[j][t] -= (k[j]/F(norm))*dot
        total+=sum(abs(v) for z in out for v in z)
    return total


def run_case(dim,cutoff,points,rows,keep,raw=False,bits=24):
    modes=['basic','angular'] if dim==2 else ['vector']
    truth = raw_loss(dim,cutoff,points,rows,keep) if raw else None
    plan=(ScalarPlan(points,cutoff,bits) if dim==2 else VelocityPlan(points,cutoff))
    result = {}
    for mode in modes:
        v=(plan.bound(rows,keep,detailed=(mode=='angular')) if dim==2 else plan.bound(rows,keep))
        ref=reference(dim,cutoff,points,rows,keep,mode)
        if truth is not None: assert truth<=ref
        assert math.isinf(v) or F(v)>=ref
        limit=ref*(1+F(1,2**bits)) if dim==2 else ref
        assert v<=upward(limit.numerator,limit.denominator)
        result[mode]={'up_hex':v.hex(),'reference_up_hex':upward(ref.numerator,ref.denominator).hex()}
    if raw: result['raw_observed_rectangular_norm']=str(truth)
    return result


def main():
    thresholds=[(0,1),(1,2**1075),(1,2**1074),(2**53+1,2**53),
                (2**54-1,2**54),(2**1024-2**971,1),(2**1024-2**971+1,1),(2**5000,1)]
    for n,d in thresholds:
        y=upward(n,d)
        assert math.isinf(y) or F(y)>=F(n,d)
        assert y==0 or F(math.nextafter(y,0))<F(n,d)
    failures=0
    for value in (math.nan,math.inf,-math.inf,complex(0,math.nan)):
        for plan,row in [(ScalarPlan([(1,0)],1),[(value,)]),(VelocityPlan([(1,0,0)],1),[(value,0.,0.)])]:
            try: plan.bound(row,[False])
            except ValueError: failures+=1
            else: raise AssertionError('nonfinite input accepted')
    result={'format_edge_ratios':len(thresholds),'nonfinite_rejections':failures}
    adversarial={}
    for name,points,scale in [('equal_shell',[(1,2),(-2,1),(2,1)],1.),('collinear',[(-1,-2),(2,4),(-3,-6)],1.),
                              ('all_zero',[(1,2),(-3,1)],0.),('subnormal',[(1,1),(1,-2)],2.**-1074),
                              ('overflow',[(1,1),(1,-2)],sys.float_info.max)]:
        rows=[(complex(scale,-scale),) for _ in points]
        adversarial[name]=run_case(2,6,points,rows,[False]*len(rows),True)
    result['adversarial']=adversarial
    rng=Random(23371)
    for dim in (2,3):
        pts=[p for p in product(range(-2,3),repeat=dim) if any(p)]
        comps=1 if dim==2 else 3
        for case in range(48):
            p=rng.sample(pts,rng.randrange(1,10))
            z=[tuple(complex(rng.randint(-9,9),rng.randint(-9,9))/16 for _ in range(comps)) for _ in p]
            keep=[rng.randrange(2)==0 for _ in p]
            run_case(dim,2,p,z,keep,True,bits=case%9+1)
    result['small_raw_ordered_convolution_cases']=96
    result['holdout']=[]
    for dim in (2,3):
        for cutoff,count in [(8,56),(16,240),(32,960)]:
            p,z,k=fixture(dim,cutoff,count,'holdout_v1')
            case=run_case(dim,cutoff,p,z,k,raw=(count==56))
            result['holdout'].append({'dim':dim,'cutoff':cutoff,'n':count,'kept':sum(k),'certificates':case})
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
