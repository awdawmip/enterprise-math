from fractions import Fraction as F
from itertools import product
from math import gcd
from collections import defaultdict
from pathlib import Path
import json

def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    points=sorted(set(points)); lo=[];hi=[]
    for p in points:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return tuple(lo[:-1]+hi[:-1])

def bezout(a,b):
    for c in range(-10,11):
        for d in range(-10,11):
            if a*d-b*c==1:return c,d
    raise ValueError((a,b))

def root_edge(poly,i):
    p=poly[i];r=poly[(i+1)%len(poly)]
    dx,dy=r[0]-p[0],r[1]-p[1];g=gcd(abs(dx),abs(dy));a,b=dx//g,dy//g
    c,d=bezout(a,b)
    pts=[((x-p[0])*d-(y-p[1])*c,-(x-p[0])*b+(y-p[1])*a) for x,y in poly]
    assert min(y for x,y in pts)==0
    def canonical(xs):
        h=min(y for x,y in xs if y>0)
        q=min(x for x,y in xs if y==h)//h
        return tuple(sorted((x-q*y,y)for x,y in xs))
    canon=min(canonical(pts),canonical([(g-x,y)for x,y in pts]))
    return g,canon

def configurations(generators):
    for choices in product([1,-1,0],repeat=len(generators)):
        pts=[(0,0)];coef=F(1)
        for v,ch in zip(generators,choices):
            if ch:pts.append((ch*v[0],ch*v[1]))
            else:
                coef=-coef;pts.extend([v,(-v[0],-v[1])])
        yield choices,hull(pts),coef

def run():
    out=defaultdict(F);raw=[]
    for name,gens,mult in [('edge',[(1,0),(0,1)],F(1,4)),
                           ('face',[(1,0),(0,1),(1,1)],-F(1,6))]:
        for choices,poly,coef in configurations(gens):
            for i in range(len(poly)):
                length,canonical=root_edge(poly,i)
                contribution=mult*coef*length/2
                out[canonical]+=contribution
                raw.append({'kind':name,'choices':choices,'poly':poly,'edge':i,'gcd':length,
                            'canonical':canonical,'coefficient':str(contribution)})
    result={'kernel_terms':[{'polygon':p,'coefficient':str(c)} for p,c in sorted(out.items()) if c],
            'all_families':len(out),'raw_edges':len(raw),'raw':raw}
    Path(__file__).with_name('width_kernels.json').write_text(json.dumps(result,indent=2)+'\n')
    return result

if __name__=='__main__':
    d=run();print(json.dumps({k:v for k,v in d.items()if k!='raw'},indent=2))
