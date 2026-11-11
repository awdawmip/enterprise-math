"""R80 minimal independent exact GCD-period quotient reproduction (Python Fraction)."""
from fractions import Fraction as Q
from math import floor, ceil, gcd
from functools import reduce
from random import Random

def f(v): return v-floor(v)
def win(E,j,x,a,b,z):
    A,B=f(a*z),f(b*z)
    if A==B:return None
    return max((e for e in E if (A<=f(x+(e[0]-j)*z)<B if A<B else
                                 f(x+(e[0]-j)*z)>=A or f(x+(e[0]-j)*z)<B)),default=None)
def roots(c,d,L,U):
    if c==0:return []
    v,w=sorted((c*L+d,c*U+d))
    return [(Q(k)-d)/c for k in range(ceil(v),floor(w)+1)]
def status(E,j,x,a,b,L,U):
    Z={L,U}
    for c,d in [(a,0),(b,0),(a-b,0)]:Z.update(roots(c,Q(d),L,U))
    for t,_ in E:
        for c in [t-j,t-j-a,t-j-b]: Z.update(roots(c,x,L,U))
    Z=sorted(Z); pts=[]
    for i,z in enumerate(Z):
        pts.append(z)
        if i+1<len(Z):pts.append((z+Z[i+1])/2)
    values={win(E,j,x,a,b,z) for z in pts}
    return (('STABLE_NONE' if values=={None} else 'STABLE') if len(values)==1 else 'CHANGES',len(pts))
def fold(E,j,x,a,b,L,U):
    g=reduce(gcd,[abs(a),abs(b)]+[abs(t-j) for t,_ in E],0)
    if not E or a==b or g==0:return 'STABLE_NONE',1
    lo=g*L;hi=min(g*U,lo+1)
    seams=sorted({lo,hi,*roots(1,Q(0),lo,hi)})
    EE=[((t-j)//g,br) for t,br in E]
    values=set();n=0
    for i,z in enumerate(seams):
        q=f(z);v=win(EE,0,x,a//g,b//g,q)
        values.add(v);n+=1
        if i+1<len(seams) and z<seams[i+1]:
            m=f((z+seams[i+1])/2)
            shift=floor((z+seams[i+1])/2)
            u,v=z-shift,seams[i+1]-shift
            # A complete six-family exact oracle is applied to this reduced cell.
            cuts={u,v}
            for c,d in [(a//g,Q(0)),(b//g,Q(0)),((a-b)//g,Q(0))]: cuts.update(roots(c,d,u,v))
            for t,_ in EE:
                for c in [t,t-a//g,t-b//g]:cuts.update(roots(c,x,u,v))
            cuts=sorted(cuts)
            for k,p in enumerate(cuts):
                values.add(win(EE,0,x,a//g,b//g,p));n+=1
                if k+1<len(cuts):values.add(win(EE,0,x,a//g,b//g,(p+cuts[k+1])/2));n+=1
    return (('STABLE_NONE' if values=={None} else 'STABLE') if len(values)==1 else 'CHANGES',n)

def main():
    R=Random(80261111)
    for _ in range(120):
        g=R.choice([1,2,3,7,13]);j=R.randrange(-3,4)
        E=sorted(set((j+g*R.randrange(-5,6),R.randrange(0,3)) for _ in range(R.randrange(0,5))))
        a,b=g*R.randrange(-4,5),g*R.randrange(-4,5)
        x=Q(R.randrange(-4,5),R.randrange(1,8))
        L=Q(R.randrange(-10,11),R.randrange(1,8));U=L+Q(R.randrange(0,18),R.randrange(1,15))
        assert status(E,j,x,a,b,L,U)[0]==fold(E,j,x,a,b,L,U)[0]
    for g in [1,2,8,32,128,512,1024]:
        E=[(4*g,1)]
        assert status(E,0,Q(0),g,2*g,Q(0),Q(1))[0]=='CHANGES'
        assert fold(E,0,Q(0),g,2*g,Q(0),Q(1))[0]=='CHANGES'
    for bits in [32,128,512,1024,2048,4096]:
        g=(1<<bits)+3
        assert fold([(4*g,1)],0,Q(0),g,2*g,Q(0),Q(1))[0]=='CHANGES'
        assert win([(4*g,1)],0,Q(0),g,2*g,Q(7,20*g))==(4*g,1)
        assert win([(4*g,1)],0,Q(0),g,2*g,Q(1,4*g)) is None
    print('R80_MIN_PASS',120,7,6)
if __name__=='__main__':main()
