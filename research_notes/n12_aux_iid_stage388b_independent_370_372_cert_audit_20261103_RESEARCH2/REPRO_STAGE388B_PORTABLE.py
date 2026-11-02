#!/usr/bin/env python3
"""Stage388-B independent Horner/Fraction real-domain audit, frozen Research2.
Emit identical original Stage370 and Stage372 CSV certificates with --emit-dir DIR.
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import argparse
A=((1,-3,3,-1),(0,1,-2,1),(0,0,1,-1),(0,0,0,1))
W=(1,3,3,1); M=(61,21,9,9); lam=F(6,5)
ports=((63,F(1,4),0),(1,F(3,4),0),(9,F(1,4),1),(7,F(3,4),1))
@lru_cache(None)
def B(k,z):
    a=A[k]; return ((a[3]*z+a[2])*z+a[1])*z+a[0]
@lru_cache(None)
def band(k,u,v):
    t=[B(k,u),B(k,v)]; q=F(k,3)
    if u<q<v:t.append(B(k,q))
    return min(t),max(t)
def gap(q,u,v):return max(F(0),u-q,q-v)
def bound(J):
    x0,x1,y0,y1=J
    q=([band(k,x0,x1) for k in range(4)],[band(k,y0,y1) for k in range(4)])
    b=F(5,32)*sum(W[k]*gap(F(M[k],160),(4*q[0][k][0]+q[1][k][0])/5,(4*q[0][k][1]+q[1][k][1])/5) for k in range(4))
    c=sum(F(coef,512)*sum(W[k]*gap(B(k,a),*q[axis][k]) for k in range(4)) for coef,a,axis in ports)
    return b,c
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def budget(x,y):return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def cost(x,y):return sum(F(coef,512)*sum(W[k]*abs(B(k,a)-B(k,(x,y)[axis])) for k in range(4)) for coef,a,axis in ports)
def fr(a):return f'{a.numerator}/{a.denominator}'
def cover(tag,root,target,kind):
    todo=[(*root,0)]; rows=[]; splits=0; area=F(0)
    while todo:
        x0,x1,y0,y1,d=todo.pop(); b,c=bound((x0,x1,y0,y1)); v=c+lam*b if kind=='L' else b
        if v>target:
            rows.append((tag,d,x0,x1,y0,y1,b,c,v)); area+=(x1-x0)*(y1-y0);continue
        assert d<40,(tag,d,x0,x1,y0,y1,v)
        splits+=1
        if 5*(x1-x0)>=y1-y0:
            mid=(x0+x1)/2;todo.extend(((x0,mid,y0,y1,d+1),(mid,x1,y0,y1,d+1)))
        else:
            mid=(y0+y1)/2;todo.extend(((x0,x1,y0,mid,d+1),(x0,x1,mid,y1,d+1)))
    assert len(rows)==splits+1 and area==(root[1]-root[0])*(root[3]-root[2])
    return rows,splits
def csv(rows,column):
    return ('region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,'+column+'\n'+
            ''.join(','.join([tag,str(d)]+[fr(z) for z in values])+'\n' for tag,d,*values in rows)).encode()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--emit-dir');args=parser.parse_args()
    xl,xu=F(2310839,10**7),F(2310840,10**7)
    yl,yu=F(5555086,10**7),F(5555091,10**7)
    assert r(0,xl,yu)>0>r(0,xu,yl) and r(1,xl,yl)>0>r(1,xl,yu) and r(1,xu,yl)>0>r(1,xu,yu)
    assert r(2,xl,yl)>0>r(3,xu,yu)
    BMAX=F(61,6250); CMAX=F(6319,100000)
    assert 2*F(15,16)*r(2,xu,yu)+F(11,5000)<BMAX
    P=(F(231138,10**6),F(555681,10**6));Q=(F(237807,10**6),F(575694,10**6))
    assert budget(*P)+budget(*Q)<2*F(15,16)*r(2,xl,yl)+F(11,5000)
    assert cost(*P)+cost(*Q)==F(16174439790495832521,256000000000000000000)<CMAX
    cut=F(469,2000)
    left,ls=cover('LEFT_X',(F(577,2500),cut,F(27,50),F(59,100)),F(1873,50000),'L')
    right,rs=cover('RIGHT_X',(cut,F(239,1000),F(27,50),F(59,100)),F(49,10000),'b')
    assert (ls,len(left),max(v[1] for v in left))==(4199,4200,20)
    assert (rs,len(right),max(v[1] for v in right))==(50,51,14)
    assert 2*F(1873,50000)-lam*BMAX-CMAX==F(9,500000)
    assert 2*F(49,10000)-BMAX==F(1,25000)
    one=csv(left+right,'target_lower')
    assert len(one)==782383 and sha256(one).hexdigest()=='5608a0843c3105eafa75c65b7496050391e3781919c337acb4c861d2303c6323'
    R=(F(219,1000),F(239,1000),F(51,100),F(16,25))
    base,gs=cover('R_GLOBAL',R,F(373,10000),'L')
    low,los=cover('LOW_Y',(R[0],R[1],R[2],F(27,50)),F(3767,100000),'L')
    high,his=cover('HIGH_Y',(R[0],R[1],F(59,100),R[3]),F(3795,100000),'L')
    assert (gs,len(base),max(v[1] for v in base))==(1190,1191,16)
    assert (los,len(low),max(v[1] for v in low))==(1661,1662,17)
    assert (his,len(high),max(v[1] for v in high))==(94,95,15)
    assert F(373,10000)+F(3767,100000)-lam*BMAX-CMAX==F(17,250000)
    assert F(373,10000)+F(3795,100000)-lam*BMAX-CMAX==F(87,250000)
    two=csv(low+high,'L_lower')
    assert len(two)==257043 and sha256(two).hexdigest()=='b21fe204b5baa2485dfb08d529cd9a003f2491caf83d2e27012cb83b8dab58a0'
    if args.emit_dir:
        p=Path(args.emit_dir);p.mkdir(parents=True,exist_ok=True)
        (p/'CERTIFICATE_STAGE372B_REGENERATED.csv').write_bytes(one)
        (p/'CERTIFICATE_STAGE370B_REGENERATED.csv').write_bytes(two)
    print('STAGE388B_INDEPENDENT_STAGE370_AND_STAGE372_PASS')
    print('stage372_leaves=4251;stage370_leaves=2948;total=7199;unclosed=0')
    print('stage372_bytes=782383;sha256='+sha256(one).hexdigest())
    print('stage370_bytes=257043;sha256='+sha256(two).hexdigest())
    print('left_gap=9/500000;right_gap=1/25000;low_gap=17/250000;high_gap=87/250000')
if __name__=='__main__':main()
