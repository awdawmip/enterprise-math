#!/usr/bin/env python3
"""R133 exact arrangement cell and centroid witness checker."""
from fractions import Fraction as F

def frac(z): return z-(z.numerator//z.denominator)
def dist(z):
    r=frac(z)
    return min(r,1-r)
def rot_word(alpha,y,m):
    return tuple(int(frac(y+i*alpha)<alpha) for i in range(m))
def original_word(alpha,B,m):
    return tuple(int(frac((B+i)*alpha)<alpha) for i in range(m))
def nearest(z):
    return (z+F(1,2)).numerator//(z+F(1,2)).denominator

def lines(m):
    return [(i,k) for i in range(-1,m) for k in range(min(0,i),max(1,i+1)+1)]

def val(line,p):
    i,k=line; a,y=p
    return y+i*a-k

def clip(poly,line,side):
    if not poly: return []
    result=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        vp=side*val(line,p); vq=side*val(line,q)
        if vp>=0:result.append(p)
        if (vp>0 and vq<0) or (vp<0 and vq>0):
            t=vp/(vp-vq)
            result.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    distinct=[]
    for z in result:
        if not distinct or distinct[-1]!=z: distinct.append(z)
    if len(distinct)>1 and distinct[0]==distinct[-1]:distinct.pop()
    return distinct

def noncollinear(p,q,r):
    return (q[0]-p[0])*(r[1]-p[1]) != (q[1]-p[1])*(r[0]-p[0])

def certificate(m):
    arr=lines(m)
    alpha_vals={F(0),F(1)}
    for i,k in arr:
        for j,h in arr:
            if i==j: continue
            z=F(k-h,j-i)
            if 0<z<1:alpha_vals.add(z)
    aa=sorted(alpha_vals)
    seen=set(); words=set(); count=0; max_den=0; min_eta=None
    B=2*m**4
    for low,high in zip(aa,aa[1:]):
        alpha=(low+high)/2
        ys=sorted({F(0),F(1)}|{F(k)-i*alpha for i,k in arr if 0 < F(k)-i*alpha <1})
        for ylo,yhi in zip(ys,ys[1:]):
            y=(ylo+yhi)/2
            sig=tuple(1 if val(line,(alpha,y))>0 else -1 for line in arr)
            if sig in seen:continue
            seen.add(sig)
            poly=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
            for ln,side in zip(arr,sig):
                poly=clip(poly,ln,side)
                if len(poly)<3:raise AssertionError(('empty polygon',m,alpha,y))
            triangle=None
            for p in poly:
                for q in poly:
                    for r in poly:
                        if noncollinear(p,q,r):triangle=(p,q,r);break
                    if triangle:break
                if triangle:break
            assert triangle
            ac=sum((z[0] for z in triangle),F(0))/3
            yc=sum((z[1] for z in triangle),F(0))/3
            assert 0<ac<1 and 0<yc<1
            eta=min([dist(yc+i*ac) for i in range(m)]+[dist(yc+(i-1)*ac) for i in range(m)])
            assert eta>=F(1,3*m**3),(m,eta,ac,yc)
            assert min(ac,1-ac)>=F(1,3*m**3)
            k=nearest(B*ac-yc)
            theta=(F(k)+yc)/B
            assert 0<theta<1
            w=rot_word(ac,yc,m)
            assert original_word(theta,B,m)==w,(m,ac,yc,theta,w)
            words.add(w);count+=1
            max_den=max(max_den,ac.denominator,yc.denominator)
            min_eta=eta if min_eta is None else min(min_eta,eta)
    return {'m':m,'B':B,'cells':count,'generic_words':len(words),'max_centroid_den':max_den,
            'min_eta':str(min_eta),'slabs':len(aa)-1}

if __name__=='__main__':
    for m in range(1,7): print('R133_UNIFORM_GRID_PASS',certificate(m))
