"""Exact rational verifier for the six source-and-route L-ingress ports.
Scope: auxiliary finite two-measure stop/continue model, not native X6.
Pure standard library; 4096 FULL and 16 seedless-LR deterministic corners.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import prod
A=(F(1,4),F(1,5)); K=(F(3,4),F(1,6))
LEAVES=('A','D','Y','C','DH','YH','LD','LY','LC','L4D','L4Y','L4C')
TIMES=(1,2,2,2,3,3,3,3,3,4,4,4)
RATIOS=(F(1),F(1,2),F(3,2),F(1),F(1,4),F(2),F(1),F(1),F(1),F(1),F(1))
I={name:i for i,name in enumerate(LEAVES)}
PORTS=((0,'D'),(0,'Y'),(0,'C'),(1,'D'),(1,'Y'),(1,'C'))
W=(F(1,24),F(1,16),F(3,16),F(1,30),F(1,20),F(1,20))
W_TOTAL=sum(W)

def masses(bits):
    assert len(bits)==12
    z=[F(0)]*24
    def add(i,name,q):z[12*i+I[name]]+=q
    for i,(alpha,kappa) in enumerate(zip(A,K)):
        aa,dd,yy,ld,ly,lc=bits[6*i:6*i+6]
        cont=F(aa,2)
        add(i,'A',F(1,2)-cont)
        d=cont*alpha; y=cont*alpha; c=cont*(1-2*alpha)
        if dd:
            add(i,'DH',F(2,3)*d)
            add(i,'L4D' if ld else 'LD',d/3)
        else:add(i,'D',d)
        if yy:
            add(i,'YH',y/2)
            add(i,'L4Y' if ly else 'LY',y/2)
        else:add(i,'Y',y)
        add(i,'C',c*(1-kappa))
        add(i,'L4C' if lc else 'LC',c*kappa)
    assert min(z)>=0 and sum(z)==1
    assert sum(z[12*i+j]*RATIOS[j] for i in range(2) for j in range(12))==1
    return tuple(z)

def xut(z):
    x=sum(z[12*i+I['DH']] for i in range(2))
    u=sum(z[12*i+I['YH']] for i in range(2))
    t=sum(z[12*i+j]*TIMES[j] for i in range(2) for j in range(12))
    return x,u,t

def det4(rows):
    a=[list(row) for row in rows]; s=F(1)
    for k in range(4):
        j=next((j for j in range(k,4) if a[j][k]),None)
        if j is None:return F(0)
        if j!=k:a[k],a[j]=a[j],a[k];s=-s
        v=a[k][k];s*=v
        for j in range(k+1,4):
            r=a[j][k]/v
            for h in range(k,4):a[j][h]-=r*a[k][h]
    return s

def detn(rows):
    a=[list(row) for row in rows]
    n=len(a); result=F(1)
    for k in range(n):
        j=next((j for j in range(k,n) if a[j][k]),None)
        if j is None:return F(0)
        if j!=k:a[k],a[j]=a[j],a[k];result=-result
        pivot=a[k][k];result*=pivot
        for j in range(k+1,n):
            r=a[j][k]/pivot
            for h in range(k,n):a[j][h]-=r*a[k][h]
    return result

def run():
    full_bits=list(product((0,1),repeat=12))
    full=[masses(b) for b in full_bits]
    lbits=list(product((0,1),repeat=4))
    lr=[masses((b[0],b[1],b[2],b[3],b[3],b[3])*2) for b in lbits]
    assert len(full)==4096 and len(lr)==16
    print('MODELS FULL=4096 LR=16 SOURCE_LABELED_TERMINALS=24 P_Q_EXACT_NORMALIZATION=PASS')
    assert W_TOTAL==F(17,40)
    assert W==tuple(masses((1,1,1,0,0,0)*2)[12*i+I['L'+route]] for i,route in PORTS)
    print('INGRESS_WEIGHTS=',','.join(map(str,W)),'W=',W_TOTAL)
    xstar,ustar=F(3,20),F(9,80)
    t0=xut(lr[14])[2];t1=xut(lr[15])[2]
    assert (t0,t1,t1-t0)==(F(43,16),F(249,80),W_TOTAL)
    assert [j for j,z in enumerate(lr) if xut(z)[:2]==(xstar,ustar)]==[14,15]
    other_deficits=[sum((xstar-xut(z)[0],ustar-xut(z)[1])) for j,z in enumerate(lr) if j not in (14,15)]
    assert min(other_deficits)==F(9,80)
    print('EXPOSED_EDGE LR=(14,15) x=3/20 u=9/80 t0=43/16 t1=249/80 other_deficit_min=9/80')
    face=[]
    for j,z in enumerate(full):
        x,u,t=xut(z)
        if (x,u)!=(xstar,ustar):continue
        lam=(t-t0)/W_TOTAL
        res=tuple(z[i]-(1-lam)*lr[14][i]-lam*lr[15][i] for i in range(24))
        face.append((j,lam,res))
    assert len(face)==64
    b=(1,1,1,0,0,0)*2
    stop=masses(b)
    port_residuals=[]
    for port_no,(i,route) in enumerate(PORTS):
        bb=list(b);bb[6*i+3+('D','Y','C').index(route)]=1
        z=masses(tuple(bb));lam=W[port_no]/W_TOTAL
        assert xut(z)[:2]==(xstar,ustar)
        assert xut(z)[2]==t0+W[port_no]
        r=tuple(z[k]-(1-lam)*lr[14][k]-lam*lr[15][k] for k in range(24))
        expected=[-lam*(lr[15][k]-lr[14][k]) for k in range(24)]
        expected[12*i+I['L'+route]]-=W[port_no]
        expected[12*i+I['L4'+route]]+=W[port_no]
        assert tuple(expected)==r
        port_residuals.append(r)
        assert r==next(q[2] for q in face if q[0]==full_bits.index(tuple(bb)))
    determinant_5=prod(W[:5])*W[5]/W_TOTAL
    minor_5=detn([[port_residuals[j][12*i+I['L4'+route]] for i,route in PORTS[:5]]
                   for j in range(5)])
    assert minor_5==determinant_5==F(1,10444800)
    assert all(sum(port_residuals[j][k] for j in range(6))==0 for k in range(24))
    assert all(all(res[k]==sum(port_residuals[p][k]
                               for p,(i,route) in enumerate(PORTS)
                               if full_bits[j][6*i+3+('D','Y','C').index(route)])
                   for k in range(24)) for j,_,res in face)
    print('MAX_FACE_FULL_POLICIES=64 EDGE_RESIDUAL_RANK=5 BY_5x5_MINOR',determinant_5)
    print('ALL_REAL_FIBER_CONDITION=equal_six_stop_continue_contrasts (necessary_and_sufficient_on_exposed_face)')
    zidx=I['L4D']
    def obs(z):return xut(z)+(z[zidx],)
    h=lambda z: z[zidx]-F(5,51)*(xut(z)[2]-t0)+3*(xut(z)[0]+xut(z)[1]-xstar-ustar)
    assert max(h(z) for z in lr)==0
    bb=list(b);bb[3]=1
    fw=masses(tuple(bb)); fwidx=full_bits.index(tuple(bb))
    assert h(fw)==F(23,612)
    assert obs(fw)==(xstar,ustar,t0+F(1,24),F(1,24))
    print('SOURCE_CONDITIONED_WITNESS_FULL_IDX',fwidx,'OBS=',','.join(map(str,obs(fw))))
    print('EXPLICIT_SEPARATOR H=z-(5/51)*(t-43/16)+3*(x+u-21/80): max_LR=0 FULL=',h(fw))
    V=[obs(z) for z in lr]
    det_w=None
    for ids in combinations(range(1,16),4):
        v0=V[0]
        dd=det4([[V[j][i]-v0[i] for i in range(4)] for j in ids])
        if dd:det_w=((0,)+ids,dd);break
    assert det_w is not None
    print('LR_FOUR_RANK_MINOR indices=',det_w[0],'det=',det_w[1])
    coeff=(F(2),F(-3,2),F(7,3),F(0),F(-9,4),F(5))
    def zval(v):
        return sum(coeff[j]*(v[12*i+I['L4'+r]]-v[12*i+I['L'+r]]) for j,(i,r) in enumerate(PORTS))
    avg=sum(w*coeff[j] for j,w in enumerate(W))/W_TOTAL
    assert all(zval(full[j])-((1-lam)*zval(lr[14])+lam*zval(lr[15]))==
               sum(W[k]*(full_bits[j][6*i+3+('D','Y','C').index(r)]-lam)*2*coeff[k] for k,(i,r) in enumerate(PORTS))
               for j,lam,_ in face)
    print('SIGNED_PORT_FIBER_IDENTITY_64_OF_64=PASS')
    print('AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY')
    print('PASS_EXACT_R5_SIX_PORT_FIBER_RANK5_SOURCE_OBSERVER_SEPARATOR')
if __name__=='__main__':run()
