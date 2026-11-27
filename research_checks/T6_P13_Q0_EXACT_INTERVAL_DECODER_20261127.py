"""T6 p13 weighted-q0 exact one-candidate interval decoder; 2026-11-27.
Uses original kernel rows reproduced from b156cda43bb477cd809c91d724d7877f0d10ed67.
Only the row order changes. No author campaign is rerun.
"""
from fractions import Fraction as F
from math import ceil, floor
from random import Random
from sympy import Matrix
P=13; CAP=2331; W=[P*j-1 for j in range(1,P)]
U=[[52,-163,-2,27,-16,7,16,-1,-4,2,-6,-4],[-112,-87,-29,38,29,5,-31,25,-16,15,5,-2],[55,-58,-9,47,-59,9,-9,24,-4,5,31,0],[-344,41,64,-38,-44,-15,8,-3,-7,-14,-13,-12],[-105,-39,-34,-67,-33,10,-65,-5,-13,-18,17,-8],[356,73,-4,-30,45,-39,38,34,-22,-14,-22,12],[-62,27,67,60,54,65,11,-15,-13,23,-1,1],[278,-68,114,32,-39,-9,-16,2,11,-6,6,-7],[-73,103,9,-39,2,-24,28,-15,-45,0,9,-9],[-233,17,43,-2,-15,-24,-7,7,-33,5,2,18],[-102,136,-14,84,-7,6,-7,-12,-27,-25,5,-16],[-210,-62,-9,-44,3,-30,13,-11,-22,-55,23,3]]
PERM=[9,4,1,11,0,6,8,2,3,7,10,5]
assert abs(Matrix(U).det())==P**21
assert all(sum(row[j-1]*pow(j,-k,P**k) for j in range(1,P))%P**k==0 for row in U for k in range(1,7))

def setup(rows):
    R=[[x*w for x,w in zip(row,W)] for row in rows]
    B=[];D=[];mu=[];bounds=[]
    for row in R:
        v=list(map(F,row));m=[]
        for b,d in zip(B,D):
            c=sum(x*y for x,y in zip(v,b))/d;m.append(c)
            v=[x-c*y for x,y in zip(v,b)]
        d=sum(x*x for x in v);B.append(v);D.append(d);mu.append(m)
        a=[x/d for x in v];bounds.append((min(0,min(a)),max(0,max(a))))
    inv=[[F(x) for x in row] for row in Matrix(rows).inv().tolist()]
    return rows,inv,D,mu,bounds
OLD=setup(U); NEW=setup([U[i] for i in PERM]); s=max(hi-lo for lo,hi in NEW[4]); assert s*2*CAP<1
assert s==F(100391772970311605414307379645,471503599360518379739494386363648)
assert min(OLD[2])==F(78577530278042129705264382752517501995032553011464356025,4243983974238642688103181306691645151538473248349)

def coord(x,inv): return [sum(a*inv[j][i] for j,a in enumerate(x))%1 for i in range(12)]
def reconstruct(z,rows):
    v=[sum(z[j]*rows[j][i] for j in range(12)) for i in range(12)]
    assert all(x.denominator==1 for x in v);return tuple(map(int,v))
def masses(v): return tuple(sum(w*max(0,sgn*x) for w,x in zip(W,v)) for sgn in (1,-1))
def fit(v,a,b):
    m,n=masses(v);return m<=a and n<=b

def decode(x,a,b):
    rows,inv,D,mu,bounds=NEW;c=coord(x,inv);z=c[:]
    for i in reversed(range(12)):
        t=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,12))
        l,h=bounds[i];lo=a*l-b*h;hi=a*h-b*l
        assert hi-lo<1
        ni=ceil(lo-t)
        if ni>floor(hi-t):return None
        z[i]=c[i]+ni
    v=reconstruct(z,rows)
    return v if fit(v,a,b) else None

def sphere(x,a,b):
    rows,inv,D,mu,_=OLD;c=coord(x,inv);z=c[:];R=a*a+b*b;out=[]
    assert R<min(D)
    def visit(i,spent):
        if i<0:
            v=reconstruct(z,rows)
            if fit(v,a,b):out.append(v)
            return
        t=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,12))
        j=floor(-t)
        for k in (j,j+1):
            val=spent+D[i]*(t+k)**2
            if val<=R:
                z[i]=c[i]+k;visit(i-1,val)
        z[i]=c[i]
    visit(11,F(0));assert len(out)<=1;return out[0] if out else None

# Independent affine initializer: invert the first six moment columns modulo p^6.
# Each row's desired residue may be lifted arbitrarily to this common modulus.
M=P**6
aug=[[pow(j,-k,M) for j in range(1,7)]+[int(k-1==i) for i in range(6)] for k in range(1,7)]
for i in range(6):
    r=next(j for j in range(i,6) if aug[j][i]%P);aug[i],aug[r]=aug[r],aug[i]
    v=pow(aug[i][i],-1,M);aug[i]=[x*v%M for x in aug[i]]
    for j in range(6):
        if j!=i:
            t=aug[j][i];aug[j]=[(x-t*y)%M for x,y in zip(aug[j],aug[i])]
MI=[row[6:] for row in aug]
def rhs(pos,neg):return [(sum(pow(P*q+r,-k,P**k) for q,r in neg)-sum(pow(P*q+r,-k,P**k) for q,r in pos))%P**k for k in range(1,7)]
def particular(y):
    x=[sum(t*v for t,v in zip(row,y))%M for row in MI]+[0]*6
    assert all(sum(x[j-1]*pow(j,-k,P**k) for j in range(1,P))%P**k==y[k-1] for k in range(1,7));return x

def mass(a):return sum(P*(P*q+r)-1 for q,r in a)
if __name__=='__main__':
    rng=Random(131327); count=valid=0
    # Known feasible cosets with a changed integer representative.
    for _ in range(256):
        v=[rng.randint(-2,2) for _ in W];a,b=masses(v)
        a=min(CAP,a+rng.randrange(20));b=min(CAP,b+rng.randrange(20));assert fit(v,a,b)
        x=[v[i]+sum(rng_coeff*row[i] for rng_coeff,row in zip([2,-1,0,0,1,0,0,0,0,0,0,0],U)) for i in range(12)]
        assert decode(x,a,b)==tuple(v)==sphere(x,a,b);count+=1;valid+=1
    # Full-budget and varying-budget arbitrary residue targets, including zero.
    for i in range(256):
        y=[rng.randrange(P**k) if i else 0 for k in range(1,7)];x=particular(y)
        a,b=(CAP,CAP) if i%2==0 else (rng.randrange(CAP+1),rng.randrange(CAP+1))
        got=decode(x,a,b);assert got==sphere(x,a,b);count+=1;valid+=got is not None
    # Exact actual q13 split49 vertical rosters, not an exhaustive branch search.
    for i in range(256):
        pos=[(q,rng.randrange(1,P)) for q in ([4],[1,3],[2,2],[1,1,2],[1,1,1,1])[i%5]]
        neg=[(q,rng.randrange(1,P)) for q in ([1]*7+[2],[1]*9)[i%2]]
        a,b=CAP-mass(pos),CAP-mass(neg)
        if min(a,b)<0 or set(pos)&set(neg):continue
        x=particular(rhs(pos,neg));got=decode(x,a,b);assert got==sphere(x,a,b);count+=1;valid+=got is not None
    print('determinant',P**21,'spread',s,'max_width',s*2*CAP,'cap_threshold',float(1/s))
    print('crosschecks',count,'feasible',valid,'all passed')
