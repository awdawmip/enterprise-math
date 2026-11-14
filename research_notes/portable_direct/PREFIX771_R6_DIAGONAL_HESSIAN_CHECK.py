"""PREFIX-771 independent exact third-jet diagonal Gamma phase calculation.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
stdlib Python; positive rational/whole-integer checks, decimals for display only.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from decimal import Decimal, localcontext
import json
N,W=189,1<<18
@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n
@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    m=k*W//n
    assert inside(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t): b=t
            else:a=t
        lo,hi=a,b
    a,b=m,W
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t): a=t
        else:b=t
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise ArithmeticError((n,k))
rows=[{0:1}]
for n in range(1,N+1):
    v=defaultdict(int)
    for k,x in rows[-1].items():v[k]+=x;v[k+1]+=x
    rows.append({k:x for k,x in v.items() if wide(n,k)})
assert len(rows)==190 and len(rows[-1])==0 and sum(map(len,rows[:N]))==9529
@lru_cache(None)
def kernels():
    return [tuple(comb(i+j,i) << (376-i-j) for j in range(i,N)) for i in range(N)]
def bilinear(v,w, L=False):
    z=0
    for i,row in enumerate(kernels()):
        for h,k in enumerate(row):
            j=i+h
            z+=k*(i+j+1 if L else 1)*(v[i]*w[j] if i==j else v[i]*w[j]+v[j]*w[i])
    return z

def jets(x,B):
    P=[1]; R=[1]
    for i in range(N):P.append(P[-1]*x);R.append(R[-1]*(B-x))
    S=[[],[],[],[]]
    for n,row in enumerate(rows[:N]):
        vals=[0,0,0,0]
        for k,v in row.items():
            j=n-k
            for order in range(4):
                z=0
                for a in range(order+1):
                    b=order-a
                    if a>k or b>j:continue
                    ff=1
                    for t in range(a):ff*=k-t
                    for t in range(b):ff*=j-t
                    z+=(-1)**b*comb(order,a)*ff*P[k-a]*R[j-b]
                vals[order]+=v*z
        for order in range(4):
            S[order].append(vals[order]*B**(191+order-n))
    return S

def calc(x,B):
    J=B**191;T=1<<377;E=J*J*T
    s,d,e,f=jets(x,B)
    A=bilinear(d,d); A1=2*bilinear(e,d); A2=2*bilinear(f,d)+2*bilinear(e,e)
    B0=bilinear(d,d,True); B1=2*bilinear(e,d,True); B2=2*bilinear(f,d,True)+2*bilinear(e,e,True)
    m=2*sum(s)*J*T-bilinear(s,s)
    v=sum(d)*J*T-bilinear(d,s)
    w=sum(e)*J*T-bilinear(e,s)
    v1=w-A
    v2=sum(f)*J*T-bilinear(f,s)-3*bilinear(e,d)
    m1=2*v;m2=2*v1
    D=B0*E+2*v*v-2*m*A
    D1=B1*E+4*v*v1-2*m1*A-2*m*A1
    D2=B2*E+4*v1*v1+4*v*v2-2*m2*A-4*m1*A1-2*m*A2
    assert A>0 and D>0
    qnum=A*E
    qp=E*(A1*D-A*D1)
    qpp=E*((A2*D-A*D2)*D-2*(A1*D-A*D1)*D1)
    # ratio Q=A E/D ; derivative Q'=qp/D^2, second Q''=qpp/D^3
    with localcontext() as ctx:
        ctx.prec=34
        view={'u':str(Decimal(x)/B),'Q':str(Decimal(qnum)/D),'Qprime':str(Decimal(qp)/Decimal(D**2)), 'Qsecond':str(Decimal(qpp)/Decimal(D**3))}
    return (A,D,qp,qpp,view)

if __name__=='__main__':
    tests=[]
    for B,points in ((10**10,(502971451,502971452)),):
        for x in points:
            A,D,qp,qpp,view=calc(x,B)
            assert (qp<0 if x==points[0] else qp>0)
            assert 4*D**3<qpp<5*D**3
            tests.append({'u':f'{x}/{B}','Qprime_sign':'negative' if qp<0 else 'positive',
                          'Qsecond_exact_bound':'4<Qsecond<5','decimal_display':view})
            if B==10**10 and x==points[1]:
                E=B**382*(1<<377)
                bound=28518591162857609314
                assert 10**21*A*E<bound*D
                bound_numerator=bound
    result={
      'schema':'PREFIX771_DIAGONAL_JET_PHASE_V2',
      'frozen_science_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'auxiliary_model':'189-layer killed Pascal BRC stopping; independent Gamma-clock maximum',
      'survivor_nonzero_positions':9529,'terminal_layer_empty':True,
      'certified_stationary_bracket':['502971451/10000000000','502971452/10000000000'],
      'bracket_width':'1/10000000000',
      'pointwise_global_qc_upper':'28518591162857609314/1000000000000000000000',
      'upper_strict':True,
      'tests':tests,
      'validation':'ALL_CHECKS_PASS PREFIX771 DIAGONAL_JET',
      'status':'AUTHOR_EXACT_INTEGER_CERTIFICATE / UNREVIEWED / NOT_ADMITTED',
      'scope_limit':'stationary existence from opposite Qprime signs; uniqueness, global min and native X6 transfer not asserted'
    }
    with open('/mnt/data/PREFIX771_R6_DIAGONAL_SECOND_JET_RESULTS.json','w') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS PREFIX771 DIAGONAL_JET')
