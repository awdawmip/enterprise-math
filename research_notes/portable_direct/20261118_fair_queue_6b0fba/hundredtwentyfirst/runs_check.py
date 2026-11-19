"""All-multiplier native Hart scans, matched streaming counts and independent torus polygons.
Run with Python 3: python runs_check.py > runs_checked.json
"""
import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from math import ceil, floor, gcd, isqrt
from pathlib import Path

PRIOR = Path(__file__).resolve().parents[1] / 'twentysecond' / 'hart_runs_check.py'
spec = importlib.util.spec_from_file_location("wave22_hart", PRIOR)
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)


def clip(poly, fun):
    ans = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp, fq = fun(*p), fun(*q)
        if fp >= 0:
            ans.append(p)
        if fp * fq < 0:
            t = fp / (fp - fq)
            ans.append(tuple(u + t * (v-u) for u, v in zip(p, q)))
    return ans


def area(poly):
    return abs(sum(p[0]*q[1]-q[0]*p[1]
                   for p,q in zip(poly, poly[1:]+poly[:1]))) / 2


def torus_section(alpha, c, length):
    """Clip original two phases against all integer translates at each extra offset."""
    start = [(F(0),F(0)),(alpha,F(0)),(alpha,alpha),(F(0),alpha)]
    faces = [start]
    for j in range(2, length):
        def read(a,b):
            return (1-j)*a+j*b+c*j*(j-1)/2
        nxt = []
        for poly in faces:
            values = [read(*p) for p in poly]
            for k in range(ceil(min(values)-alpha), floor(max(values))+1):
                part = clip(poly, lambda a,b: read(a,b)-k)
                part = clip(part, lambda a,b: k+alpha-read(a,b))
                if part and area(part):
                    nxt.append(part)
        faces = nxt
    return sum((area(poly) for poly in faces), F(0))


def resonant_shapes():
    samples = {}
    for q in (2, 3, 4):
        c = F(1, q)
        data = []
        for k in range(q):
            b = (F(k, q)-c*q/2) % 1
            points = sorted({(b*j+c*j*j/2) % 1 for j in range(q)})
            gaps = [y-x for x,y in zip(points,points[1:]+[points[0]+1])]
            width = 1-max(gaps)
            assert width == {2:F(1,4),3:F(1,3),4:F(1,2)}[q]
            # Compare with both a direct 8-period orbit and the extremal cut-and-unwrap description.
            assert set(points) == {(b*j+c*j*j/2) % 1 for j in range(8*q)}
            bounding = min(max((x-base)%1 for x in points) for base in points)
            assert width == bounding
            data.append(dict(slope=str(b),phases=[str(x) for x in points],width=str(width)))
        samples[str(q)] = data
    return samples


def complete_half_circle_census():
    accepted = Counter()
    cases = 0
    for q in range(1, 12):
        for s in range(1, q//2+1):
            if gcd(s,q)>1 or 32*s*s < q*q:
                continue
            for k in range(q):
                mod = 2*q
                phases = sorted({(s*j*j+(2*k-s*q)*j)%mod for j in range(q)})
                max_gap = max(y-x for x,y in zip(phases,phases[1:]+[phases[0]+mod]))
                width = mod-max_gap
                assert width == min(max((x-b)%mod for x in phases) for b in phases)
                if 2*width < mod:
                    accepted[str(F(s,q)),str(F(width,mod))] += 1
                cases += 1
    assert accepted=={('1/2','1/4'):2,('1/3','1/3'):3,('2/5','2/5'):5}
    return dict(denominators_checked=list(range(1,12)),templates_checked=cases,
                short_arcs=[dict(curvature=c,width=w,slopes=n) for (c,w),n in sorted(accepted.items())])


def witnesses():
    tests=0
    for alpha in (F(3,16),F(1,5),F(7,32),F(1,4)):
        for i in range(18,51):
            c=F(i,100)
            assert torus_section(alpha,c,4)==max(F(0),alpha-c)**2/2
            if c>F(1,6):
                assert torus_section(alpha,c,5)==0
            tests+=1
    # At c=1/2 the two alternating routes persist even under all seven constraints.
    area_8=torus_section(F(3,10),F(1,2),8)
    assert area_8>0
    # Integrate twice the two available upper-edge distances, using E sqrt(1-X)=2/3.
    unit_volume=2*(1+2*F(2,3)**2)
    assert unit_volume==F(34,9) and 2*F(4,3)*unit_volume==F(272,27)
    return dict(complete_half_circle_census=complete_half_circle_census(),
                exact_resonances=resonant_shapes(), rational_curvature_cutoff_pairs=tests,
                eight_hit_endpoint_section_at_three_tenths=str(area_8),
                parabola_volume=str(unit_volume),two_parity_jacobian_coefficient=str(2*F(4,3)*unit_volume))


CUTS=(F(7,40),F(1,5),F(1,4),F(13,50),F(5,18),F(3,10),F(13,40))
LABELS=[str(q) for q in CUTS]+['1/(4sqrt(2))']
RANGES=(1,2,3,4,5,6,8,12,16,24,32,64)


def shell(p,q):
    assert native.isprime(p) and native.isprime(q) and p!=q
    n=p*q
    lo0=native.icbrt(n)
    lo=lo0+(lo0**3<n)
    hi=native.icbrt(8*n)
    batch=[0]*len(LABELS)
    hist=[Counter() for _ in LABELS]
    starts=[None]*len(LABELS)
    scores=[[0]*len(RANGES) for _ in LABELS]
    num=[q.numerator for q in CUTS]
    den=[q.denominator for q in CUTS]
    for k in range(lo,hi+1):
        h=4*n*k
        x=1+isqrt(h-1)
        e=x*x-h
        a=2*x-1
        hits=[e*d<=a*b for d,b in zip(den,num)]+[32*e*e<=a*a]
        for j,hit in enumerate(hits):
            if hit:
                batch[j]+=1
                for i,r in enumerate(RANGES):
                    if batch[j]<r: break
                    scores[j][i]+=1
            elif batch[j]:
                hlen=batch[j]
                if not hist[j] or hlen>max(hist[j]): starts[j]=k-hlen
                hist[j][hlen]+=1
                batch[j]=0
    for j,hlen in enumerate(batch):
        if hlen:
            if not hist[j] or hlen>max(hist[j]): starts[j]=hi-hlen+1
            hist[j][hlen]+=1
    data={}
    for j,label in enumerate(LABELS):
        runs=hist[j]
        longest=max(runs,default=0)
        assert all(scores[j][i]==sum(max(0,s-r+1)*count for s,count in runs.items())
                   for i,r in enumerate(RANGES))
        for r in RANGES:
            xr=sum(max(0,s-r+1)*count for s,count in runs.items())
            xr1=sum(max(0,s-r)*count for s,count in runs.items())
            assert xr-xr1==sum(count for s,count in runs.items() if s>=r)
            assert r*(xr-xr1)+xr1==sum(s*count for s,count in runs.items() if s>=r)
        if j in (0,len(LABELS)-1): assert longest<=3
        if j in (1,2): assert longest<=4
        data[label]=dict(longest=longest,first_start_of_longest=starts[j],
                         run_histogram=dict(sorted(runs.items())),consecutive_windows=dict(zip(RANGES,scores[j])))
    return dict(primes=[p,q],N=n,multiplier_interval=[lo,hi],score_evaluations=hi-lo+1,thresholds=data)


def main():
    examples=((1009,1013),(1000003,1000033),(1000000007,1000000009),(16777213,16777291),(3,93824992236293))
    samples=[shell(*pair) for pair in examples]
    ref=json.loads(PRIOR.with_name('hart_runs_checked.json').read_text())
    checked=0
    for s in samples:
        old=next((v for v in ref['integer_shells'] if v['N']==s['N']), None)
        if old is None:
            continue
        for a in ('1/5','1/4'):
            assert old['three_hits'][a]==s['thresholds'][a]['consecutive_windows'][3]
            checked+=1
    control=samples[-2]
    assert control['multiplier_interval']==[65537,131072]
    for key,expected in [('1/5',(4,130389,1,0)),('1/4',(4,115950,28,0)),('3/10',(7,66857,153,14))]:
        row=control['thresholds'][key]
        assert (row['longest'],row['first_start_of_longest'],
                row['consecutive_windows'][4],row['consecutive_windows'][5])==expected
    imbalanced=samples[-1]
    assert imbalanced['multiplier_interval']==[65536,131071]
    for label, expected in [('1/4',(4,106431,22,0)),('13/50',(6,65556,38,2)),('3/10',(26,65536,157,31))]:
        row=imbalanced['thresholds'][label]
        assert (row['longest'],row['first_start_of_longest'],
                row['consecutive_windows'][4],row['consecutive_windows'][5])==expected
    print(json.dumps(dict(arithmetic=witnesses(),previous_native_third_counts_cross_checked=checked,
                          finite_samples=samples),indent=2))


if __name__=='__main__':
    main()
