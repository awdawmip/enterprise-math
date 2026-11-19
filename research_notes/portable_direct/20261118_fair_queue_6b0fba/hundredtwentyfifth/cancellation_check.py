"""Exact Cauchy identities, direct lattice/old Fourier source, asymptotic diagnostics."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from math import exp, lgamma, log, pi, prod, sqrt
from pathlib import Path
from runpy import run_path
import json

PRIOR = Path(__file__).resolve().parents[1] / 'ninetythird' / 'heat_check.py'
assert sha256(PRIOR.read_bytes()).hexdigest() == '5150aa79f4a003601bf493e180be0bce09958ade092d7c2aa9664c1c90414e17'
old = run_path(str(PRIOR))


def factors(nodes):
    return [prod(Q(x+y, abs(x-y)) for y in nodes if x!=y) for x in nodes]


def gram(nodes):
    return [[Q(1,x+y) for y in nodes] for x in nodes]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def check_window(nodes):
    import sympy as s
    g = factors(nodes)
    mat = gram(nodes)
    w = [(-1)**i*2*x*a for i,(x,a) in enumerate(zip(nodes,g))]
    inverse = [[a*b*z for b,z in zip(w,row)] for a,row in zip(w,mat)]
    for i,row in enumerate(mat):
        for j,col in enumerate(inverse):
            assert dot(row,col) == int(i==j)
    det = prod(Q((y-x)**2,(y+x)**2) for i,x in enumerate(nodes) for y in nodes[i+1:])
    assert s.Matrix(mat).det()*prod(2*x for x in nodes) == det
    p = [u*u/sum(v*v for v in g) for u in g]
    mean = dot(p,nodes)
    var = dot(p,[(x-mean)**2 for x in nodes])
    bound = 1-var/(4*min(nodes)**2)
    assert bound > 0
    return {'rates':nodes,'det_normalized':str(det),'min_eigenvalue_lower':str(1/sum(v*v for v in g)),
            'ratio_of_upper_to_lower_enclosure':str(1/bound)}


def lattice_windows():
    total=0
    for k in ((1,0,0),(1,1,0),(1,1,1),(2,0,0),(2,2,0)):
        k2=dot(k,k)
        direct=old['direct_parents'](k,256)
        for a in (8,16,32,64):
            exact=[x for x in range(a,2*a) if 2*x-k2 in direct]
            criteria=[x for x in range(a,2*a) if old['feasible'](k,2*x-k2)]
            assert exact == criteria
            if len(exact)>1:
                check_window(exact[:7])
                total+=1
    return total


def exact_native(repo):
    import sympy as s
    source=repo/old['SOURCE_FILE']
    assert sha256(source.read_bytes()).hexdigest()==old['SOURCE_HASH']
    chains=[[(j,1,0) for j in range(1,5)],[(j,0,1) for j in range(1,5)]]
    vertices=sum(chains,[])
    source_field=run_path(str(source))['helical_data'](vertices,[s.Integer(2)]*len(vertices))
    receiver=s.Matrix([0,s.I,1])
    def coeff(p,q,field):
        raw=(s.sqrt(dot(p,p))-s.sqrt(dot(q,q)))*field[p].cross(field[q])
        return s.simplify(receiver.conjugate().dot(raw)/2)
    rates=[7,15,27]
    g=factors(rates)
    j=1
    desired=[(-1)**(i+j)*Q(2*x,x+rates[j])*a/g[j] for i,(x,a) in enumerate(zip(rates,g))]
    field={}
    for ci,chain in enumerate(chains):
        z=s.Integer(1)
        field[chain[0]]=source_field[chain[0]]
        for index,(p,v) in enumerate(zip(chain[1:],chain)):
            q=tuple(-x for x in v)
            c=coeff(p,q,source_field)
            target=s.I if ci==0 else s.Rational(desired[index])-s.I
            z=s.cancel(target/(c*z.conjugate()))
            field[p]=source_field[p]*z
    for p,val in list(field.items()):
        field[tuple(-x for x in p)]=val.conjugate()
    outcomes={}
    for p in field:
        q=(1-p[0],-p[1],-p[2])
        if p<q and q in field:
            r=dot(p,p)+dot(q,q)
            outcomes[r]=outcomes.get(r,0)+coeff(p,q,field)
    assert sorted(outcomes)==rates and all(s.simplify(outcomes[x]-v)==0 for x,v in zip(rates,desired))
    norm=dot(desired,[dot(row,desired) for row in gram(rates)])
    assert norm==1/(2*rates[j]*g[j]**2)
    return {'pinned_source':old['SOURCE_HASH'],'rates':rates,'output':'k=(1,0,0), negative helicity',
            'named_conjugate_modes':len(field),'target_amplitudes':list(map(str,desired)),
            'fixed_rate':rates[j],'least_heat_trace_squared':str(norm)}


def laplace_examples():
    s=sqrt(2.5)-1
    phi=(3+s)*log(3+s)-(2+s)*log(2+s)-s*log(s)-(1-s)*log(1-s)
    curvature=1/(2+s)+1/s+1/(1-s)-1/(3+s)
    samples=[]
    for shift in (0.0,0.5,-0.25):
        b=((3+s)/(2+s))**(2*shift-0.5)*sqrt((1-s)/s)/(4*pi*(1+s))
        for n in (32,128,512,2048):
            a=n+shift
            logs=[lgamma(2*a+i+n)-lgamma(2*a+i)-log(2*a+2*i)-lgamma(i+1)-lgamma(n-i)
                  for i in range(n)]
            m=max(logs)
            weights=[exp(2*(v-m)) for v in logs]
            total=sum(weights)
            mean=sum(w*i for i,w in enumerate(weights))/total
            var=sum(w*(i-mean)**2 for i,w in enumerate(weights))/total
            log_lower=-2*m-log(total)
            predicted=1.5*log(n)+0.5*log(curvature/pi)-2*log(b)-2*n*phi
            ratio=exp(log_lower-predicted)
            samples.append([shift,n,round(ratio,8),round(ratio/(1-var/(4*a*a)),8),
                            round(var/n,7)])
    return {'center_in_unit_interval':round(s,10),'potential_max':round(phi,10),
            'predicted_variance_over_n':round(1/(2*curvature),8),
            'diagnostic_columns':['shift','n','lower_over_asymptotic','upper_over_asymptotic','variance_over_n'],
            'diagnostics':samples}


def continuum(c):
    from math import asin
    from scipy.integrate import quad
    mid=sqrt(2.5)
    gap=sqrt(9-c*c)/2
    l,u=sqrt(2.5-gap),sqrt(2.5+gap)
    def f(x):
        if x<=l or x>=u:
            return 1.
        return 2/pi*asin(min(1.,c/(2*sqrt((x*x-1)*(4-x*x)))))
    cuts=sorted(set([1.,l,mid,u,2.]))
    def integrate(func):
        return sum(quad(func,a,b,epsabs=2e-11,epsrel=2e-11)[0] for a,b in zip(cuts,cuts[1:]))
    q=integrate(f)
    potentials=[]
    for probe in (mid,(mid+l)/2,(1+l)/2):
        parts=sorted(set(cuts+[probe]))
        v=sum(quad(lambda x:f(x)*log((x+probe)/abs(x-probe)),a,b,epsabs=1e-10,epsrel=1e-10)[0]
              for a,b in zip(parts,parts[1:]))
        potentials.append(v)
    assert abs(potentials[1]-potentials[0])<1e-8 and potentials[2]<potentials[0]
    return q,2*potentials[0]


def spectrum():
    import mpmath as mp
    from itertools import combinations
    import sympy as sym
    xs=[13,15,17,19,21,23]
    raw=sym.Matrix([[Q(2*y,x+y) for y in xs] for x in xs])   # similar to normalized heat Gram
    coeffs=raw.charpoly().all_coeffs()
    for m in range(len(xs)+1):
        minors=sum(prod(Q((y-x)**2,(y+x)**2) for x,y in combinations(subset,2))
                   for subset in combinations(xs,m))
        assert coeffs[m]==(-1)**m*minors
    from scipy.special import ellipk
    curvatures=[]
    for c in (0.5,1.5,2.5):
        q0,v0=continuum(c-0.0001)
        q1,v1=continuum(c+0.0001)
        l=(5-sqrt(9-c*c))/2
        u=5-l
        exact=2*pi*ellipk(l/u)/ellipk(1-l/u)
        assert abs((v1-v0)/(q1-q0)-exact)<1e-7
        curvatures.append([c,round(float(exact),8)])
    samples=[]
    levels=[(c,*continuum(c)) for c in (0.5,1.5,2.5)]
    for n in (12,24,48):
        with mp.workdps(3*n+35):
            xx=[mp.mpf(n)+i+mp.mpf('0.5') for i in range(n)]
            mat=mp.matrix([[2*mp.sqrt(x*y)/(x+y) for y in xx] for x in xx])
            vals=list(reversed(list(mp.eigsy(mat,eigvals_only=True))))
            assert vals[-1]>0
            lines=[]
            for c,q,v in levels:
                j=min(n,max(1,int(n*q+0.5)))
                lines.append([c,round(q,7),round(v,7),j,round(float(-mp.log(vals[j-1])/n),7)])
            samples.append({'n':n,'ordered_quantiles':lines,
                            'minus_log_det_over_n_squared':round(float(-sum(map(mp.log,vals))/n**2),8)})
    return {'arithmetic_grid':'x_i=n+1/2+i; common scaling has no effect',
            'exact_minors_all_orders_in_six_rate_example':True,'elliptic_curvature':curvatures,
            'ordered_quantile_columns':['c','limiting_fraction_q','limiting_minus_log_eigen_over_n','index','observed'],
            'predicted_minus_log_determinant_over_n_squared':round(9*log(4/3),8),'samples':samples}


def fixed_edge_modes(sizes=(64,256,1024), columns=7, modes=4):
    from mpmath import mp
    from math import factorial
    out=[]
    with mp.workdps(50):
        s=mp.sqrt(mp.mpf(5)/2)-1
        kappa=1/(2+s)+1/s+1/(1-s)-1/(3+s)
        c=1/(8*kappa*(1+s)**2)
        for n in sizes:
            ratios=[mp.mpf(1)]
            for i in range(n-1):
                ratio=mp.mpf(3*n+i)/(2*n+i)*(n+i)/(n+i+1)*(n-i-1)/(i+1)
                ratios.append(ratios[-1]*ratio**2)
            total=mp.fsum(ratios)
            m=[mp.mpf(0) for _ in range(2*columns+1)]
            center=n*(1+s)
            for i,w in enumerate(ratios):
                z=(n+i-center)/(n+i+center)
                u=w/total
                for j in range(len(m)):
                    m[j]+=u
                    u*=z
            # Gram of the exact first 'columns' features. Remainder trace equals m[-1].
            eig=mp.eigsy(mp.matrix([[m[i+j]-m[i+j+2] for i in range(columns)] for j in range(columns)]),eigvals_only=True)
            vals=[]
            for j in range(modes):
                normal=factorial(j)*(c/n)**j
                value=eig[columns-1-j]
                vals.append([round(float(value/normal),9), round(float((value+m[-1])/normal),9)])
            out.append(dict(n=n,column_count=columns,remaining_trace=float(mp.nstr(m[-1],8)),eigenvalue_ratios=vals))
    return out


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',required=True,type=Path)
    opt=ap.parse_args()
    result={'native':exact_native(opt.repo),'parent_lattice_windows':lattice_windows(),
            'exact_k_200_window_32_to_64':check_window([x for x in range(32,64) if old['feasible']((2,0,0),2*x-4)]),
            'laplace':laplace_examples(),'full_spectrum':spectrum(),'inverse_end_modes':fixed_edge_modes()}
    print(json.dumps(result,indent=2,sort_keys=True))
