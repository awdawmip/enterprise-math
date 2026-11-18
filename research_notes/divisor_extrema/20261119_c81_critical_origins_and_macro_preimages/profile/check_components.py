"""Direct rational-grid row/column means and complex integrals for small catalogues."""
from collections import Counter
from fractions import Fraction as F
from random import Random
import json
from mpmath import mp
import phase_components as C
mp.dps=60

def axis(values,q):
    bases=[s//q for s in values]
    events=sorted({q-(s%q) for s in values if s%q})
    ranks={e:j+1 for j,e in enumerate(events)}
    num=len(events)+1
    times=[ranks.get(q-(s%q),num) for s in values]
    cuts=[s*(C.Q//q) for s in [0,*events,q]]
    return bases,times,num,cuts

def integral(j,q,k):
    if k==0: return mp.mpf(1)/q
    t=2j*mp.pi*k
    return (mp.exp(t*(j+1)/q)-mp.exp(t*j/q))/t

def check(points,q):
    n=len(points)
    x=axis([z[0] for z in points],q)
    y=axis([z[1] for z in points],q)
    m,v,vx,modes,bounds=C.run_axis(x,y)
    m2,v2,vy,modes2,bounds2=C.run_axis(y,x)
    grid=[]
    for a in range(q):
        row=[]
        for b in range(q):
            counts=Counter(((i+a)//q,(j+b)//q) for i,j in points)
            row.append(sum(t==1 for t in counts.values()))
        grid.append(row)
    g=sum(map(sum,grid))
    mean=F(g,n*q*q)
    var=F(sum(t*t for row in grid for t in row),n*n*q*q)-mean*mean
    marginal=lambda rows:F(sum(sum(row)**2 for row in rows),n*n*q**3)-mean*mean
    assert (m,m2,v,v2,vx,vy)==(mean,mean,var,var,marginal(grid),marginal(zip(*grid)))
    assert bounds==bounds2==[min(map(min,grid)),max(map(max,grid))]
    for name,(u,w) in {'x':(1,0),'y':(0,1),'plus':(1,1),'minus':(1,-1)}.items():
        a=[integral(i,q,u) for i in range(q)]
        b=[integral(j,q,w) for j in range(q)]
        coeff=abs(sum(a[i]*b[j]*grid[i][j] for i in range(q) for j in range(q))/n)
        lo,hi=modes[name]
        assert lo<=10**14*coeff<=hi
        lo2,hi2=modes2[{'x':'y','y':'x'}.get(name,name)]
        assert lo2<=10**14*coeff<=hi2
def main():
    cases=[([(0,0)],4), ([(3,4),(4,4)],8), ([(0,0),(0,0),(8,8),(7,4),(3,1)],8)]
    rng=Random(20261119)
    for q in [4,8,16]:
        for n in range(2,17):
            cases.append(([(rng.randrange(-q,3*q),rng.randrange(-q,3*q)) for _ in range(n)],q))
    for points,q in cases:
        check(points,q)
    return {'checks':len(cases),'checked':'two extrema, mean, variance, both main-effect variances, plus and minus diagonal and both axial Fourier amplitudes in both axis orders'}
if __name__=='__main__':
    print(json.dumps(main(),indent=2))
