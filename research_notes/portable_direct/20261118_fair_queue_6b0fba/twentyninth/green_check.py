"""Six-dimensional Green and flux checks. Python standard library, exact integers."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, isqrt, prod
import json

ZERO=(0,)*6


def compositions(total, dimension):
    if dimension==1:
        yield (total,)
    else:
        for i in range(total+1):
            for rest in compositions(total-i,dimension-1):
                yield (i,)+rest


def neighbors(x):
    for j in range(6):
        for sign in (-1,1):
            v=list(x)
            v[j]+=sign
            yield tuple(v),j


def word_count(w,n,x):
    gap=n-sum(x)
    if gap<0 or gap%2:
        return 0
    out=0
    for v in compositions(gap//2,6):
        counts=tuple(a+b for a,b in zip(v,x))
        denom=prod(factorial(a)*factorial(b) for a,b in zip(v,counts))
        out+=factorial(n)//denom*prod(a**(j+k) for a,j,k in zip(w,v,counts))
    return out


def kernel(w,blocks):
    d=2*sum(w)
    def orbit(x):
        i=0
        result=[]
        for width in blocks:
            result.extend(sorted(map(abs,x[i:i+width]),reverse=True))
            i+=width
        return tuple(result)
    keys=sorted({orbit(x) for n in range(10) for x in compositions(n,6)},key=lambda x:(sum(x),x))
    transfer={x:[(orbit(y),w[j]) for y,j in neighbors(x)] for x in keys}
    p=[{ZERO:1}]; g=[{ZERO:1}]
    for n in range(1,10):
        p.append({x:sum(wj*p[-1].get(y,0) for y,wj in transfer[x]) for x in keys})
        assert all(p[-1][x]==word_count(w,n,x) for x in keys)
        if n<9:
            g.append({x:d*g[-1].get(x,0)+p[-1][x] for x in keys})
    # Store the exact number per individual point, in orbit representatives, for every cutoff.
    gtable={}
    for x in keys:
        if sum(x)<=8:
            gtable[''.join(map(str,x))]=[gn.get(x,0) for gn in g[sum(x):]]
    flux={}
    for R in (1,2,3):
        ball=Counter()
        boundary=Counter()
        for x in product(range(-R,R+1),repeat=6):
            rsq=sum(t*t for t in x)
            if rsq>R*R:
                continue
            ox=orbit(x)
            ball[ox]+=1
            for y,j in neighbors(x):
                if rsq+y[j]**2-x[j]**2>R*R:
                    boundary[(ox,orbit(y))]+=w[j]
        data=[]
        for n,gn in enumerate(g):
            out=sum(mass*gn.get(x,0) for (x,y),mass in boundary.items())
            inward=sum(mass*gn.get(y,0) for (x,y),mass in boundary.items())
            inside=sum(mult*p[n+1].get(x,0) for x,mult in ball.items())
            assert out-inward==d**(n+1)-inside
            data.append([out,inward,inside])
        flux[str(R)]={"ball_size":sum(ball.values()),"rows":data}
    return {"step_denominator":d,"axis_signed_numerators":w,"symmetry_blocks":blocks,
            "G_N_per_point":{"rule":"array starts at N=sum(digits) through 8, denominator d^N; missing orbits have zero",
                             "representatives":gtable},
            "boundary":{"rule":"rows ordered N=0..8; outward,inward,P(X_(N+1) in ball) numerators over d^(N+1)",
                        "by_radius":flux}}


def series_product(a,b):
    n=len(a)
    return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(n)]


def eta_product(n,start,exps):
    coeff=[0]*(n+1)
    coeff[start]=1
    for level,e in exps:
        for step in range(level,n+1,level):
            for _ in range(abs(e)):
                if e>0:
                    for i in range(n,step-1,-1):
                        coeff[i]-=coeff[i-step]
                else:
                    for i in range(step,n+1):
                        coeff[i]+=coeff[i-step]
    return coeff


def theta(n=900):
    t=[0]*(n+1); t4=[0]*(n+1)
    for a in range(-isqrt(n),isqrt(n)+1):
        t[a*a]+=1
        t4[a*a]+=a**4
    p=t[:]
    for _ in range(4):
        p=series_product(p,t)
    r6=series_product(p,t)
    sq4=series_product(p,t4)
    f=eta_product(n,1,((1,-4),(2,22),(4,-4)))
    g=eta_product(n,2,((1,4),(2,-2),(4,12)))
    def chi(k):
        return (0,1,0,-1)[k%4]
    def coeff_product(a,b):
        x,y=a
        z,v=b
        return (x*z-15*y*v,x*v+y*z)
    odd_primes=[p for p in range(3,n+1,2) if all(p%d for d in range(2,isqrt(p)+1))]
    eigen=[(a-2*b,2*b) for a,b in zip(f,g)]
    hecke_checks=0
    for p in odd_primes:
        for j in range(1,n//p+1):
            u,v=coeff_product(eigen[p],eigen[j])
            if j%p==0:
                x,y=eigen[j//p]
                u-=chi(p)*p**6*x
                v-=chi(p)*p**6*y
            assert (u,v)==eigen[j*p]
            hecke_checks+=1
        assert eigen[p]==((f[p],0) if chi(p)>0 else (0,f[p]))
    for j in range(1,n+1):
        E=sum(chi(j//d)*d*d for d in range(1,j+1) if j%d==0)
        assert (f[j]-E)%16==0
        if j%8==7:
            assert (f[j]-E)%32==0
        assert 60*f[j]==48*sq4[j]-3*j*j*r6[j]
        assert r6[j]==sum(16*chi(j//d)*d*d-4*chi(d)*d*d for d in range(1,j+1) if j%d==0)
        if 2*j<=n:
            assert f[2*j]==4*f[j]-64*g[j] and g[2*j]==f[j]
        assert f[j]%2 == int(isqrt(j)**2==j and j%2==1)
    def dyad(j):
        m=2**j
        return [j,r6[m],f[m],str(F(180*f[m],r6[m]*m))]
    return {"checked_through":n,"odd_primes":len(odd_primes),"hecke_pairs":hecke_checks,
            "mod32_checked_at_7_mod8":(n+1)//8,"coefficients_f_1_12":f[1:13],"coefficients_g_1_12":g[1:13],
            "dyadic":[dyad(j) for j in range(n.bit_length())],
            "dyadic_columns":["j","r6(2^j)","f(2^j)","m^4 times shell correction, multiplied by pi^3"]}


def pd_coeffs(z,axis,w):
    """Constant-free potentials as Taylor polynomials on one coordinate section."""
    q=[F(1,ww) for ww in w]
    def add(a,b):
        return [x+y for x,y in zip(a,b)]
    def mul(a,b):
        return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(5)]
    def power(a,k):
        out=[1,0,0,0,0]
        for _ in range(k):
            out=mul(out,a)
        return out
    def scale(c,a):
        return [c*t for t in a]
    R=[0]*5;b2=[0]*5;b4=[0]*5
    for i in range(6):
        y=[z[i],int(i==axis),0,0,0]
        y2=mul(y,y)
        R=add(R,scale(q[i],y2))
        b2=add(b2,scale(q[i]**2,y2))
        b4=add(b4,scale(q[i]**3,mul(y2,y2)))
    inv=[1/R[0]]
    for i in range(1,5):
        inv.append(-sum(R[j]*inv[i-j] for j in range(1,i+1))/R[0])
    y=scale(F(1,2),power(inv,2))
    c=add(scale(sum(q),power(inv,3)),scale(-12,mul(b2,power(inv,4))))
    c=scale(F(1,4),add(c,scale(16,mul(b4,power(inv,5)))))
    return y,c


def anisotropic_shells(M=18):
    def shell_points(dim):
        buckets=[[] for _ in range(M+1)]
        b=isqrt(M)
        for x in product(range(-b,b+1), repeat=dim):
            n=sum(a*a for a in x)
            if n<=M:
                buckets[n].append(sum(a**4 for a in x))
        return buckets
    p2,p4=shell_points(2),shell_points(4)
    rows=[]
    for m in range(1,M+1):
        mass=0
        leading=F(0)
        correction=F(0)
        for j in range(m+1):
            i=m-j
            D=i+2*j
            a,b=p2[i],p4[j]
            pairs=len(a)*len(b)
            quartic=len(b)*sum(a)+8*len(a)*sum(b)
            mass+=pairs
            leading+=F(8*pairs,D**2)
            correction+=F(40*pairs,D**3)-F(48*pairs*(i+4*j),D**4)+F(64*quartic,D**5)
        if m in (1,2,3,5,8,13,18):
            rows.append([m,mass,str(leading/mass),str(correction/mass)])
    assert rows[0]==[1,12,'4','74/3']
    return rows


def continuum():
    outs=[]
    for w in ((F(1,6),)*6,(F(1,4),)*2+(F(1,8),)*4):
        jac=isqrt(int(prod(1/a for a in w)))
        points=[(1,0,0,0,0,0),(0,0,1,0,0,0),(1,-2,0,3,4,-1),(2,3,5,-6,7,4)]
        vals=[]
        for x in points:
            parts=[pd_coeffs(x,i,w) for i in range(6)]
            assert sum(w[i]*parts[i][0][2] for i in range(6)) == 0
            assert sum(w[i]*(parts[i][1][2]+parts[i][0][4]) for i in range(6))==0
            vals.append([x,str(jac*parts[0][0][0]),str(jac*parts[0][1][0])])
        outs.append(vals)
    return {"axis_and_other_values_of_pi_cubed_times_L_and_A":outs,
            "identities":"sum p_i L_ii=0 and sum p_i(A_ii/2+L_iiii/24)=0"}


if __name__=="__main__":
    print(json.dumps({"uniform":kernel((1,)*6,(6,)),
                      "two_plus_four":kernel((2,2,1,1,1,1),(2,4)),
                      "theta":theta(),"potential":continuum(),
                      "anisotropic_shells_m_count_pi3L_pi3A":anisotropic_shells()},indent=1))
