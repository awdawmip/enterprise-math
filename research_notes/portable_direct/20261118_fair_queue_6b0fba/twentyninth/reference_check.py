"""Exact checks for helical shell observation, time mismatch, tail, and A3 calibration.
Run python reference_check.py. Requires SymPy; no numerical solver or external data.
"""
import json
from collections import Counter, defaultdict
from itertools import product
from math import isqrt

import sympy as sp

R, I, V = sp.Rational, sp.I, sp.Matrix
ZERO = V([0, 0, 0])


def sq(k):
    return sum(a*a for a in k)


def add(k, p):
    return tuple(a+b for a, b in zip(k, p))


def negative(k):
    return tuple(-a for a in k)


def shell(m):
    t = isqrt(m)
    return [k for k in product(range(-t, t+1), repeat=3) if sq(k) == m]


def canon(k):
    return next(a>0 for a in k if a)


def expand(v):
    return v.applyfunc(sp.expand)


def pair(p, u, q, v):
    # Combined two orderings of +P((u.grad)v); dot is the bilinear Fourier dot.
    k = V(add(p,q))
    if not k.dot(k):
        return ZERO
    raw = I*(u.dot(V(q))*v + v.dot(V(p))*u)
    return expand(raw-k*(k.dot(raw)/k.dot(k)))


def field(positive):
    terms = dict(positive)
    terms.update({negative(p):(u.conjugate(), lam) for p,(u,lam) in positive.items()})
    return terms


def residual(data):
    # First keep every ordered source separately. Merge only by common output and rate.
    labelled = []
    for p, (u, lam) in data.items():
        assert V(p).dot(u) == 0
        if lam != sq(p):
            labelled.append((p,lam,(sq(p)-lam)*u))
        for q,(v, mu) in data.items():
            k = V(add(p,q))
            if not k.dot(k):
                continue
            raw = I*u.dot(V(q))*v
            labelled.append((tuple(k),lam+mu,raw-k*(k.dot(raw)/k.dot(k))))
    merged = defaultdict(lambda:ZERO)
    for k,lam,w in labelled:
        merged[k,lam] = merged[k,lam]+w
    merged = {key:expand(v) for key,v in merged.items()}
    return {key:v for key,v in merged.items() if v != ZERO}


def gram(packets):
    # Returns exact coefficients of 1/sqrt(d) for d=|k|^2, including cross-rate terms.
    result = defaultdict(lambda:sp.S.Zero)
    for (k,lam), u in packets.items():
        for (p,mu),v in packets.items():
            if p==k:
                result[sq(k)] += sp.re(sp.expand(u.dot(v.conjugate())))/(lam+mu)
    return {d:sp.factor(v) for d,v in sorted(result.items())}


def helical(p, radius):
    # Rational, nonunit h for integer radius, one column per complex input coefficient.
    e = V([0,0,0])
    e[min(range(3), key=lambda j:abs(p[j]))] = 1
    k=V(p)
    h=e-k*k.dot(e)/sq(p)+I*k.cross(e)/radius
    assert expand(I*k.cross(h)-radius*h) == ZERO
    return h


def rank_test():
    q=(0,0,3)
    beam=V([1,I,0])
    cols=[]
    for p in [p for p in shell(25) if canon(p)]:
        h=helical(p,5)
        for scalar in [1,I]:
            col=defaultdict(lambda:ZERO)
            for pp,u in [(p,scalar*h),(negative(p),(scalar*h).conjugate())]:
                for qq,v in [(q,beam),(negative(q),beam.conjugate())]:
                    k=add(pp,qq)
                    if canon(k):
                        col[k] = col[k]+pair(pp,u,qq,v)
            cols.append(col)
    ks=sorted(set().union(*(c.keys() for c in cols)))
    def rank(keys):
        rows=[[part(c.get(k,ZERO)[j]) for c in cols] for k in keys
              for j in range(3) for part in (sp.re,sp.im)]
        return sp.Matrix(rows).rank()
    plane=[k for k in ks if k[2]==0]
    full_rank,plane_rank=rank(ks),rank(plane)
    assert (len(cols),full_rank,plane_rank)==(30, 28, 4)
    return {"real_domain_dimension":len(cols),"full_real_rank":full_rank,
            "collision_plane_real_rank":plane_rank,"collision_plane_up_to_sign":plane}


def spectral_check():
    q=(0,0,3)
    M,N=25,9
    v=V([1,I,0])
    all_paths=defaultdict(list)
    for p in shell(M):
        u=helical(p,5)
        for qq, w in [(q,v),(negative(q),v.conjugate())]:
            k=add(p,qq)
            out=pair(p,u,qq,w)
            dot=V(p).dot(V(qq))
            sine2=1-R(dot**2,M*N)
            expected=(5-3)**2*sine2*(1+R((5+3)**2,sq(k)))/4
            # Both test helicity vectors have norm sqrt(2), so divide by four.
            assert sp.expand(out.dot(out.conjugate()))==4*expected
            all_paths[k].append(out)
    common=[(k,rows) for k,rows in all_paths.items() if len(rows)==2]
    for k,(a,b) in common:
        assert k[2]==0 and sq(k)==16 and a!=ZERO and b!=ZERO
        inner=sp.expand(a.dot(b.conjugate()))
        assert sp.expand(inner*inner.conjugate()-a.dot(a.conjugate())*b.dot(b.conjugate()))==0
    # Give the complete squared singular spectrum with exact algebraic entries.
    # Combine latitude +/-z first; other accidental equalities can be read by summing multiplicities.
    byz=Counter(abs(p[2]) for p in shell(M))
    result=[]
    for z,count in sorted(byz.items()):
        sine2=1-R(z*z,M)
        def weight(d):
            return (5-3)**2*sine2*(1+R(64,d))/(4*68*sp.sqrt(d))
        if z==3:
            sides,mid=weight(52),weight(16)
            for w in (sides,sides+2*mid):
                result.append({"abs_z":z,"multiplicity":count//2,"eigenvalue":str(w)})
        else:
            w=weight(34+6*z)+weight(34-6*z)
            result.append({"abs_z":z,"multiplicity":count,"eigenvalue":str(w)})
    assert sum(a['multiplicity'] for a in result)==30
    assert sum(a['multiplicity'] for a in result if a['eigenvalue']!='0')==28
    return {"raw_path_squared_norms_checked":60,"complex_collinearity_checks":len(common),
            "spectrum_for_unit_beam_by_latitude":result}


def coherent_case(sign, delta):
    p=(4,0,-3)
    r=(4,0,3)
    q=(0,0,3)
    h1=V([-R(3,5),I,-R(4,5)])
    h2=V([R(3,5),I,-R(4,5)])
    g=V([1,I,0])
    phase=(3+4*I)/5
    for zz,h in [(p,h1),(r,h2),(q,g)]:
        assert expand(I*V(zz).cross(h)-isqrt(sq(zz))*h) == ZERO
    for pos in ({p:(h1,25),r:(h2,25)}, {q:(g,9)}):
        assert residual(field(pos)) == {}
    data=field({p:(h1,25+delta),r:(sp.expand(sign*phase**2)*h2,25),
                q:(phase*g,9)})
    packets=residual(data)
    by_radius=gram(packets)
    time=2*R(delta**2,5*(25+delta))
    cent=R(32,5)*(R(1,2*(34+delta))+R(1,68)+R(2*sign,68+delta))
    side=R(1856,325)*(R(1,34+delta)+R(1,34))
    predicted={d:v for d,v in [(16,4*cent),(25,5*time),(52,side)] if v}
    assert by_radius==predicted
    for k,lam in packets:
        assert (negative(k),lam) in packets
        assert expand(packets[negative(k),lam]-packets[k,lam].conjugate())==ZERO
    count=len({k for k,lam in packets})
    return {"phase_sign":sign,"wrong_rate_delta":delta,"nonzero_frequencies":count,
            "nonzero_mode_rate_packets":len(packets),
            "linear_time_Y2":str(time),"collision_plane_Y2":str(cent),
            "tail_above_radius_5_Y2_times_sqrt13":str(side/2),
            "gram_coefficients_of_inverse_radius":{str(k):str(v) for k,v in by_radius.items()}}


def a3_calibration():
    # Unique-path closed form on freeze's actual unit-helicity A3 input (A=B=nu=1).
    positive=[(1,1,0),(1,0,1),(0,1,1)]
    beam=(2,-2,0)
    counts=Counter()
    radial=defaultdict(lambda:sp.S.Zero)
    keys=set()
    for p0 in positive:
        for p in (p0,negative(p0)):
            for q in (beam,negative(beam)):
                k=add(p,q)
                assert k not in keys
                keys.add(k)
                d=sq(k)
                dot=sum(x*y for x,y in zip(p,q))
                sine2=1-R(dot**2,16)
                norm2=2*sine2*(1+R(18,d))/4
                radial[d]+=norm2/(20*d)  # coefficient of sqrt(d), not 1/sqrt(d)
                counts[d]+=1
    assert dict(radial)=={6:R(1,20),10:R(7,250),14:R(3,245)} and len(keys)==12
    return {"nonzero_modes_by_radius_squared":dict(sorted(counts.items())),
            "coefficient_of_sqrt_d":{str(d):str(radial[d]) for d in sorted(radial)}}


def contraction():
    # Rational intervals for the inherited all-mode growth envelope at epsilon=1/8.
    def sqrt_bounds(x):
        x=R(x)
        scale=10**12
        n=isqrt(int(sp.floor(x*scale**2)))
        return R(n,scale),R(n+1,scale)
    def exp_bounds(x):
        term=total=sp.S.One
        for i in range(1,17):
            term*=x/i
            total+=term
        assert 0<x<1
        return total,total+(term*x/17)/(1-x/18)
    def outward(a,b):
        scale=10**6
        return [str(sp.floor(a*scale)/scale),str(sp.ceiling(b*scale)/scale)]
    b=[]
    l=[]
    alpha=[]
    inputs=zip(sqrt_bounds(2),sqrt_bounds(6),sqrt_bounds(R(4,3)),sqrt_bounds(R(2,3)))
    for i,(s2,s6,t,c) in enumerate(inputs):
        b.append(s2*(4*(R(1,2)+s6)/5+R(5,3))/8)
        l.append(t*exp_bounds(b[i])[i])
        alpha.append(l[i]*R(9503,1000)*c)
    lo,hi=sqrt_bounds(13)
    e0=[R(928,5525)/hi,R(928,5525)/lo]
    out={"epsilon":"1/8","radius":"1/100","growth_exponent":outward(*b),
         "inverse_envelope":outward(*l),"alpha_envelope":outward(*alpha)}
    for name,center in [('dark',0),('bright',R(32,85))]:
        eta=[l[i]*sqrt_bounds(e0[i]+center)[i]/64 for i in (0,1)]
        test=[4*alpha[i]*eta[i] for i in (0,1)]
        out[name]={"eta":outward(*eta),"four_alpha_eta":outward(*test)}
        if name=='dark':
            radius=R(1,100)
            margin=radius-eta[1]-alpha[1]*radius**2
            lip=2*alpha[1]*radius
            assert margin>R(239,10**6) and lip<R(366,1000)
            assert exp_bounds(b[1])[1]<R(51,25)
            assert exp_bounds(b[1])[1]/10000<margin
            out[name].update({"initial_perturbation_Hhalf_radius":"1/10000",
                              "homogeneous_gain_strict_upper":"51/25",
                              "inclusion_margin_strict_lower":"239/1000000",
                              "Lipschitz_strict_upper":"183/500"})
        else:
            assert test[0]>R(1746,1000)
    return out


def main():
    counts=[len(shell(n)) for n in range(1,65)]
    def excluded(n):
        while n%4==0:
            n//=4
        return n%8==7
    assert all((v==0)==excluded(n) for n,v in enumerate(counts,1))
    lattice=[]
    for M in range(1,65):
        for q in [(0,0,1),(0,0,3),(1,1,0),(1,2,2)]:
            beam=set(shell(M))
            double=set(add(p,q) for p in beam)&set(add(p,negative(q)) for p in beam)
            double.discard((0,0,0))
            expected={k for k in (shell(M-sq(q)) if M>sq(q) else [])
                      if sum(a*b for a,b in zip(k,q))==0}
            assert expected==double
            if q[:2]==(0,0) and M>sq(q):
                n=M-sq(q)
                assert len(double)==4*sum((d%4==1)-(d%4==3) for d in range(1,n+1) if n%d==0)
            lattice.append(len(double))
    print(json.dumps({"rank":rank_test(),"spectrum":spectral_check(),"shell_counts_1_to_64":counts,
        "collision_count_identities_checked":len(lattice),"A3_calibration":a3_calibration(),
        "inherited_all_mode_test":contraction(),
        "witness":[coherent_case(1,0),coherent_case(-1,0),coherent_case(-1,1)]},
        indent=2,ensure_ascii=False))


if __name__=="__main__":
    main()
