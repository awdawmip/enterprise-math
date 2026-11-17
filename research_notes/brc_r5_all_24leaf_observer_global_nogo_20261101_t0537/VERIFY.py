"""Exact rational certificate for all-real 24-leaf fourth-linear-observer no-go.
Fixed two-source 12-decision FULL vs four-key seedless LR model.
4096+16 terminal mass corners, 240*Q integer arithmetic. Standard Python only.
"""
from fractions import Fraction as F
from itertools import product

LEAF=('A','D','Y','C','DH','YH','LD','LY','LC','L4D','L4Y','L4C')
I={name:j for j,name in enumerate(LEAF)}
TIME=(1,2,2,2,3,3,3,3,3,4,4,4)
RATIO=(F(1),F(1,2),F(3,2),F(1),F(1,4),F(2),*(F(1),)*6)
W=(10,15,45,8,12,12)

def masses(bits):
    assert len(bits)==12
    z=[0]*24
    def add(i,name,weight):z[12*i+I[name]]+=weight
    for i in (0,1):
        a,d,y,ld,ly,lc=bits[6*i:6*i+6]
        if not a:
            add(i,'A',120)
            continue
        dm,ym,cs,cl=((30,30,15,45) if i==0 else (24,24,60,12))
        if d:
            add(i,'DH',2*dm//3)
            add(i,'L4D' if ld else 'LD',dm//3)
        else:add(i,'D',dm)
        if y:
            add(i,'YH',ym//2)
            add(i,'L4Y' if ly else 'LY',ym//2)
        else:add(i,'Y',ym)
        add(i,'C',cs)
        add(i,'L4C' if lc else 'LC',cl)
    assert sum(z)==240 and all(v>=0 for v in z)
    assert sum(z[12*i+j]*RATIO[j] for i in (0,1) for j in range(12))==240
    return tuple(z)

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def features(z):
    return (sum(z),
            z[I['DH']]+z[12+I['DH']],
            z[I['YH']]+z[12+I['YH']],
            sum(z[12*i+j]*TIME[j] for i in (0,1) for j in range(12)),
            F(5,4)*z[I['A']]+z[12+I['A']])

def echelon(rows):
    if not rows:return (),()
    a=[[F(v) for v in row] for row in rows]
    i=0;piv=[]
    for col in range(len(a[0])):
        idx=next((r for r in range(i,len(a)) if a[r][col]),None)
        if idx is None:continue
        a[i],a[idx]=a[idx],a[i]
        p=a[i][col];a[i]=[q/p for q in a[i]]
        for r in range(len(a)):
            if r!=i and a[r][col]:
                q=a[r][col];a[r]=[v-q*w for v,w in zip(a[r],a[i])]
        piv.append(col);i+=1
        if i==len(a):break
    return tuple(tuple(a[k]) for k in range(i)),tuple(piv)

def rank(rows):return len(echelon(rows)[1])

def determinant(a):
    n=len(a);assert all(len(row)==n for row in a)
    v=[[F(x) for x in row] for row in a];d=F(1)
    for i in range(n):
        j=next((j for j in range(i,n) if v[j][i]),None)
        if j is None:return F(0)
        if j!=i:v[i],v[j]=v[j],v[i];d=-d
        p=v[i][i];d*=p
        for j in range(i+1,n):
            if v[j][i]:
                q=v[j][i]/p
                for k in range(i,n):v[j][k]-=q*v[i][k]
    return d

def in_span(row,base,piv):
    z=[F(v) for v in row]
    for b,col in zip(base,piv):
        if z[col]:
            q=z[col];z=[v-q*w for v,w in zip(z,b)]
    return not any(z)

def run():
    bits=list(product((0,1),repeat=12))
    FULL=[masses(b) for b in bits]
    LR=[masses((a,d,y,l,l,l)*2) for a,d,y,l in product((0,1),repeat=4)]
    assert len(FULL)==4096 and len(LR)==16
    assert all(sum(z)==240 for z in FULL+LR)
    print('Q_240_NORMALIZATION=4096_FULL_PLUS_16_LR; P_NORMALIZATION=PASS')
    def f0(z):
        _,X,U,T,_=features(z)
        return 4*T-39*X-8*U-960
    def f1(z):
        _,X,U,T,_=features(z)
        return 2*T-3*X-26*U-480
    assert all(f0(z)>=0 and f1(z)>=0 for z in LR)
    def deficit(z,which):
        _,X,U,T,_=features(z)
        return ((f0(z)+U) if which==0 else
                (f0(z)+f1(z)) if which==1 else (f1(z)+X))
    for which,k in enumerate((12,14,10)):
        assert {j for j,z in enumerate(LR) if deficit(z,which)==0}==set(range(8))|{k}
    print('EARLY_EDGE_EXPOSURE: f0>=0,f1>=0; three_forced_edges=PASS')
    edges=((48,12),(56,14),(40,10))
    E=[]
    for j,k in edges:
        fv=features(FULL[j]);lv=features(LR[k]);v0=features(LR[0])
        assert all(9*fv[q]==5*v0[q]+4*lv[q] for q in range(5))
        E.append(tuple(9*FULL[j][h]-5*LR[0][h]-4*LR[k][h] for h in range(24)))
    bb=(1,1,1,0,0,0)*2
    assert masses(bb)==LR[14] and sum(W)==102
    ports=[]
    for p in range(6):
        choice=list(bb)
        choice[(p//3)*6+3+(p%3)]=1
        late=masses(tuple(choice));w=W[p]
        ports.append(tuple(102*late[h]-(102-w)*LR[14][h]-w*LR[15][h] for h in range(24)))
    assert all(sum(port[j] for port in ports)==0 for j in range(24))
    E.extend(ports[:5])
    rref,piv=echelon(E)
    assert len(piv)==8
    minor=determinant([[row[col] for col in piv] for row in E])
    assert minor==-5817825199521792000000
    print('EIGHT_FORCED_EDGE_RESIDUALS_RANK=8; COLUMN_PIVOTS=',piv)
    print('EIGHT_BY_EIGHT_INTEGER_MINOR=',minor)
    print('THREE_EARLY_WITNESS_INDICES=',tuple(j for j,k in edges),'INGRESS_PORT_COUNT=5_OF_6')
    basis_idx=(0,2048,3072,2560,3328,2688,2112,32,48,40,52,42,33)
    basis,piv13=echelon([FULL[k] for k in basis_idx])
    assert len(piv13)==13
    minor13=determinant([[FULL[i][col] for col in piv13] for i in basis_idx])
    assert minor13==-870712934400000000
    assert all(in_span(row,basis,piv13) for row in FULL)
    print('FULL_24_LEAF_MASS_LINEAR_RANK=13; 4096_ROWS_IN_13_BASIS=PASS')
    print('THIRTEEN_BY_THIRTEEN_INTEGER_MINOR=',minor13,'PIVOTS=',piv13)
    C0=[F(1)]*24
    CX=[F(0)]*24;CX[I['DH']]=CX[12+I['DH']]=F(1)
    CU=[F(0)]*24;CU[I['YH']]=CU[12+I['YH']]=F(1)
    CT=[F(t) for i in (0,1) for t in TIME]
    CZ=[F(0)]*24;CZ[I['A']]=F(5,4);CZ[12+I['A']]=F(1)
    assert all(dot(row,phi)==0 for row in E for phi in (C0,CX,CU,CT,CZ))
    feat=[features(z) for z in FULL]
    assert rank(feat)==5
    choice=[];curr=[]
    for idx,vec in enumerate(feat):
        if rank(curr+[vec])>len(curr):
            choice.append(idx);curr.append(vec)
        if len(curr)==5:break
    minor5=determinant(curr)
    assert minor5==-66355200
    print('E_NEUTRAL_FEATURE_SPAN=5; FEATURE_MINOR_ROWS=',tuple(choice),'DET=',minor5)
    print('IMAGE_OF_ALL_E_NEUTRAL_24_LEAF_LINEAR_OBSERVERS=SPAN(1,x,u,t,zA) EXACT')
    def Hscaled(z):
        one,X,U,T,ZA=features(z)
        return 45*T+59*ZA-90*X-135*U-26730
    lrhs=[Hscaled(v) for v in LR]
    assert max(lrhs)==0 and min(lrhs)<0
    fw=FULL[2112]
    assert bits[2112]==(1,0,0,0,0,1,0,0,0,0,0,0)
    assert features(fw)==(240,0,0,450,120)
    assert Hscaled(fw)==600
    assert rank([features(v) for v in LR])==5
    print('LR_A_STOP_FOUR_DIMENSIONAL_AFFINE_RANK=4')
    print('SIGNED_SUPPORT: H=45t+59zA-90x-135u-891/8; max_LR=0; FULL_2112=5/2')
    print('ALL_REAL_COEFFICIENTS_DICHOTOMY: E_NOT_ZERO=>SEPARATION; E_ZERO=>rank<=3_OR_SEPARATION')
    print('SCOPE=finite_two_source_positive_measure_auxiliary_stop_model; not_native_X6')
    print('STATUS=AUTHOR_PROVED_EXACT_FRACTION_CHECKED_UNREVIEWED_NOT_ADMITTED')
    print('PASS_EXACT_R5_24_SOURCE_LABELED_LEAF_LINEAR_OBSERVER_GLOBAL_NO_GO')
if __name__=='__main__':run()
