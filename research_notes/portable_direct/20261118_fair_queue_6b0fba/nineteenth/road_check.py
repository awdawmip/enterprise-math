"""Rational outward intervals for the analytic anchored road kernel (stdlib)."""
import json
from fractions import Fraction as F
from itertools import product

SCALE=10**18
ROOT4=((1,0),(0,1),(-1,0),(0,-1))


def cmul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def unit(n,j):
    a,b=ROOT4[(n*j)%4]
    return (1-a,-b)


def enclosure(w,M=0,blocks=1024):
    """Sum over n>M of periodic signed weights w[n mod q]/n²."""
    q=len(w)
    T=q*((M+q-1)//q+blocks)
    low=high=0
    for n in range(M+1,T+1):
        a=SCALE*w[n%q]
        low+=a//(n*n)
        high-=(-a)//(n*n)
    lo,hi=F(low,SCALE),F(high,SCALE)
    for r in range(1,q+1):
        w0=w[r%q]
        u=F(w0,q*(T+r))
        v=u+F(w0,(T+r)**2)
        lo+=min(u,v)
        hi+=max(u,v)
    return lo,hi


def intersect(a,b):
    assert max(a[0],b[0])<=min(a[1],b[1])


def scale(k,a):
    v=sorted((k*a[0],k*a[1]))
    return (v[0],v[1])


def atan_inverse(a,n=20):
    s=sum(F((-1)**j,(2*j+1)*a**(2*j+1)) for j in range(n))
    return tuple(sorted((s,s+F((-1)**n,(2*n+1)*a**(2*n+1)))))


def display(pair):
    lo,hi=pair
    return [lo.numerator*SCALE//lo.denominator,-((-hi.numerator*SCALE)//hi.denominator)]


def bridge(x,y):
    return min(x,y)-x*y


def mesh_weights(x,q):
    i=min(q-1,int(q*x))
    t=q*x-i
    return ((F(i,q),1-t),(F(i+1,q),t))


def run():
    at5,at239=atan_inverse(5),atan_inverse(239)
    pi=(16*at5[0]-4*at239[1],16*at5[1]-4*at239[0])
    pi2=(pi[0]**2,pi[1]**2)
    # θ=jπ/2, φ=kπ/2. All signed components here are integers.
    Cl=[enclosure(tuple(ROOT4[(j*n)%4][1] for n in range(4)),blocks=2048) for j in range(4)]
    kernels={}
    for j,k in product(range(4),repeat=2):
        w=[cmul(unit(n,j),(unit(n,k)[0],-unit(n,k)[1])) for n in range(4)]
        re=enclosure([a for a,b in w])
        im=enclosure([b for a,b in w])
        exact_re=scale(2*bridge(F(j,4),F(k,4)),pi2)
        exact_im=(Cl[k][0]-Cl[j][1]+Cl[(j-k)%4][0],
                  Cl[k][1]-Cl[j][0]+Cl[(j-k)%4][1])
        intersect(re,exact_re);intersect(im,exact_im)
        if (j,k)==(1,2):
            kernels['pi_over_2_pi']={'real':display(re),'imag':display(im)}
    # E(1,-i)-E(1,+i) from direct norm; no kernel cross term used.
    diff=[]
    for n in range(4):
        x,y=unit(n,1),unit(n,2)
        iy=cmul((0,1),y)
        norm=lambda z:z[0]**2+z[1]**2
        diff.append(norm((x[0]-iy[0],x[1]-iy[1]))-norm((x[0]+iy[0],x[1]+iy[1])))
    assert diff==[0,8,0,-8]
    direct=enclosure(diff)
    intersect(direct,scale(8,Cl[1]))
    kernels['E_1_minus_i_minus_E_1_plus_i']=display(direct)
    mesh_tests=0
    for q in range(2,9):
        for i,j in product(range(3*q+1),repeat=2):
            x,y=F(i,3*q),F(j,3*q);wx,wy=mesh_weights(x,q),mesh_weights(y,q)
            interp=sum(a*b*bridge(s,t) for s,a in wx for t,b in wy)
            err=bridge(x,y)-interp
            exp=(q*(min(x,y)-wx[0][0])*(wx[1][0]-max(x,y)) if wx[0][0]==wy[0][0] else 0)
            assert err==exp and 0<=err<=F(1,4*q)
            mesh_tests+=1
    # Raw b includes zero-frequency term; F_0=0 for both lists.
    tail_cases=[]
    for b in [((1,0),(0,-1),(-1,0),(0,1)),((-1,-1),(2,0),(-1,2),(0,-1))]:
        assert tuple(map(sum,zip(*b)))==(0,0)
        C=sum(i*i+j*j for i,j in b)
        w=[]
        for n in range(4):
            terms=[cmul(z,ROOT4[(n*j)%4]) for j,z in enumerate(b)]
            a,im=map(sum,zip(*terms));w.append(a*a+im*im)
        assert sum(w)==4*C
        for M in (0,3,17,128):
            interval=enclosure([v-C for v in w],M,128)
            bound=F(3*C*4,(M+1)**2)
            assert -bound<=interval[0]<=interval[1]<=bound
            tail_cases.append({'b':b,'M':M,'C':C,'centered_tail':display(interval),'bound':str(bound)})
    filters={}
    for q,m in ((4,1),(5,1),(7,3),(8,1)):
        pos=enclosure([int(r==m) for r in range(q)],blocks=512)
        neg=enclosure([int(r==q-m) for r in range(q)],blocks=512)
        ratio=(2*pos[0]/(pos[0]+neg[1]),2*pos[1]/(pos[1]+neg[0]))
        assert F(1)<ratio[0]<=ratio[1]<2
        # Independent reindexing certificate for q^-2 S(m/q) and its negative-frequency mate.
        for a, direct in ((m,pos),(q-m,neg)):
            t=F(a,q);J=80
            partial=sum(1/(k+t)**2 for k in range(J))
            tail=1/(J+t)
            intersect(direct,((partial+tail)/(q*q),(partial+tail+1/(J+t)**2)/(q*q)))
        filters[f'{m}/{q}']={'positive':display(pos),'negative':display(neg),'two_eta':display(ratio)}
    return {'interval_unit':'10^-18, inclusive integer endpoints','Machin_pi':display(pi),
            'Catalan':display(Cl[1]),'kernels':kernels,'q4_kernel_entries':16,
            'normalized_bridge_interpolation_tests':mesh_tests,'one_sided_tail_cases':tail_cases,
            'residue_filters':filters,'filter_normalization':'F_n=1 when n=m mod q; positive/negative energies q^-2 S(m/q) and q^-2 S(1-m/q)',
            'scope':'finite rational enclosures and 4th-root witnesses; general spacing inequality is not inferred from tests'}


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=1))
