#!/usr/bin/env python3
"""Stage380-B: exact rational checker; no third-party dependencies."""
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
from pathlib import Path
import argparse, csv, io
W=(1,3,3,1); M=(61,21,9,9)
P=(F('0.2308'),F('0.2345'),F('0.55'),F('0.56'))
Q=(F('0.2365'),F('0.239'),F('0.57566'),F('0.57574'))
S={'xa':'-+++','xb':'--++','ya':'++--','yb':'--++'}
PW={"++":('0.23081','0.55010'),'+-':('0.23081','0.55500'),
    '-+':('0.23400','0.55500'),'--':('0.23081','0.55990')}
QW={'+L':('0.23890','0.57568'),'-L':('0.23660','0.57568'),
    '+H':('0.23890','0.57571'),'-H':('0.23660','0.57571')}
CO=((1,-3,3,-1),(0,1,-2,1),(0,0,1,-1),(0,0,0,1))
def B(k,z):return z**k*(1-z)**(3-k)
def db(k,z):return (k*z**(k-1)*(1-z)**(3-k) if k else 0)-((3-k)*z**k*(1-z)**(2-k) if k<3 else 0)
def R(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def mm(k,a,b):
    if k==0:return B(k,b),B(k,a)
    if k==3:return B(k,a),B(k,b)
    if k==1 and b<F(1,3):return B(k,a),B(k,b)
    if k==1 and a>F(1,3):return B(k,b),B(k,a)
    assert k==2 and b<F(2,3)
    return B(k,a),B(k,b)
def sign(l,h):return '+' if l>0 else '-' if h<0 else '?'
def bc(x,y):
    budget=F(5,32)*sum(W[k]*abs(R(k,x,y)) for k in range(4))
    D=lambda a,z:sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))/2
    cost=(63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256
    return budget,cost
def reduced(x,y):
    budget=F(15,16)*R(2,x,y)+F(5,16)*max(R(0,x,y),0)+F(15,16)*max(R(1,x,y),0)
    cost=F(5157,32768)-F(189,256)*x+F(93,128)*x*x-F(61,256)*x**3+F(33,512)*y*y-F(29,512)*y**3+F(21,512)*abs(F(9,64)-B(2,y))
    return budget,cost
def check():
    rows=[]
    for name,box in [('P',P),('Q',Q)]:
        xl,xh,yl,yh=box
        for k in range(4):
            a,b=mm(k,xl,xh);c,d=mm(k,yl,yh)
            lo,hi=(4*a+c)/5-F(M[k],160),(4*b+d)/5-F(M[k],160)
            assert sign(lo,hi)==({'P':'??+-','Q':'-?+-'}[name][k])
            rows.append((name,'residual',f'r{k}',str(lo),str(hi),sign(lo,hi)))
        for axis,lo,hi in [('x',xl,xh),('y',yl,yh)]:
            for a,anchor in [('a',F(1,4)),('b',F(3,4))]:
                for k in range(4):
                    mn,mx=mm(k,lo,hi);mn,mx=B(k,anchor)-mx,B(k,anchor)-mn
                    sg=sign(mn,mx)
                    assert sg==('?' if name=='Q' and axis=='y' and a=='b' and k==2 else S[axis+a][k])
                    rows.append((name,'audit',axis+a+str(k),str(mn),str(mx),sg))
    assert len(rows)==40
    assert [sum(W[k]*CO[k][j] for k in range(4)) for j in range(4)]==[1,0,0,0]
    assert sum(W[k]*M[k] for k in range(4))==160
    assert [CO[1][j]+CO[2][j] for j in range(4)]==[0,1,-1,0]
    C=F(0);X=[F(0)]*4;Y=[F(0)]*4
    for axis,anchor,weight in [('x',F(1,4),63),('x',F(3,4),1),('y',F(1,4),9),('y',F(3,4),7)]:
        for k in range(4):
            if axis=='y' and anchor==F(3,4) and k==2:continue
            t=F(weight*W[k],512)*(1 if S[axis+('a' if anchor==F(1,4) else 'b')][k]=='+' else -1)
            C+=t*B(k,anchor)
            for j in range(4):(X if axis=='x' else Y)[j]-=t*CO[k][j]
    assert (C+X[0]+Y[0],X[1],X[2],X[3],Y[1],Y[2],Y[3])==(F(5157,32768),-F(189,256),F(93,128),-F(61,256),0,F(33,512),-F(29,512))
    q=lambda z:16*z*z-4*z-3
    assert q(Q[2])<0<q(Q[3]) and q(P[3])<0
    assert P[0]<P[1]<Q[0]<Q[1]<F(1,2)
    assert (1-P[1])**2>2*(1-P[2])**2
    assert db(2,P[1])<2*db(2,P[3])
    assert db(2,Q[3])>0
    for z in (F(0),F(1,8),F(1,4),F(1,3)):
        for t in (0,1):
            v=F(3,4)*db(2,z)+F(1,4)*db(0,z)+F(3*t,4)*db(1,z)
            assert v==(-F(3,4)*(2*z-1)**2 if not t else -F(3,4)*z*z)
        N=(1-z)*(63-61*z);Np=-(63-61*z)-61*(1-z)
        assert (Np*(1-2*z)+2*N)==2+122*z*(1-z)
        assert F(9,64)-B(2,z)==(4*z-3)*q(z)/64
    assert 378*P[0]*(1-P[0])>62 and Q[0]-P[1]==F(1,500)
    assert F(3,4)*(1-2*Q[1])==F(783,2000)
    witnesses=[]
    for (sp,(px,py)),(sq,(qx,qy)) in product(PW.items(),QW.items()):
        px,py,qx,qy=map(F,(px,py,qx,qy))
        assert P[0]<px<P[1] and P[2]<py<P[3] and Q[0]<qx<Q[1] and Q[2]<qy<Q[3]
        assert ('+' if R(0,px,py)>0 else '-')==sp[0]
        assert ('+' if R(1,px,py)>0 else '-')==sp[1]
        assert ('+' if R(1,qx,qy)>0 else '-')==sq[0]
        assert ('L' if F(9,64)>B(2,qy) else 'H')==sq[1]
        assert bc(px,py)==reduced(px,py) and bc(qx,qy)==reduced(qx,qy)
        if sp=='-+' and sq[0]=='+':
            for x,y in [(px,py),(qx,qy)]:
                assert bc(x,y)[0]==F(3,16)*(4*x*(1-x)+y*(1-y))-F(45,256)
        witnesses.append((sp,sq,*map(str,(px,py,qx,qy))))
    assert len(witnesses)==16
    out=io.StringIO(newline='');cw=csv.writer(out,lineterminator='\n')
    cw.writerow(['region','type','label','lower_or_x','upper_or_y','sign_or_qx','qy'])
    for name,kind,label,lo,hi,sg in rows:cw.writerow((name,kind,label,lo,hi,sg,''))
    for sp,sq,px,py,qx,qy in witnesses:cw.writerow(('WITNESS',sp,sq,px,py,qx,qy))
    return out.getvalue().encode()
def main():
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path);p.add_argument('--verify',type=Path);a=p.parse_args()
    raw=check()
    if a.emit:a.emit.write_bytes(raw);assert a.emit.read_bytes()==raw
    if a.verify:assert a.verify.read_bytes()==raw
    print('STAGE380B_PARETO_FACE_REDUCTION_PORTABLE_PASS')
    print('exact_bounds=40; all_open_chambers=16; resolved_audit_signs=31/32')
    print('residual_wedge=r0(P)<=0<=r1(P),r1(Q)>=0; budget=ACTIVE')
    print('face_union=r0(P)*r1(P)*r1(Q)=0; quadratic_budget=EXACT')
    print('marginal_x_transfer_slope<-783/1000000')
    print('csv_bytes='+str(len(raw))+'; sha256='+sha256(raw).hexdigest())
if __name__=='__main__':main()
