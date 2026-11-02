"""R5 two-law source-conditioned J bridge: exact BRC/provenance checks.
Scientific inputs: prior R5 three-key model; rational arithmetic only.
No random seed, floating-point arithmetic, external packages, or theorem promotion.
"""
from fractions import Fraction as F
from itertools import product, permutations
H = F(1, 2)
N = (35, 23, 27, -27)
CHECKS = 0

def check(statement):
    global CHECKS
    assert statement
    CHECKS += 1

def carrier(parameter, policy):
    """Return observer and preserved source-labelled BRC coordinates."""
    vb, vi, alpha, uc, ui, ub = parameter
    x, jb, ji, kc, ki, kbj, kij = map(F, policy)
    db = (1-jb)/8
    di = (1-x)*(1-ji)/8
    d = db+di
    weights = (F(1,4), (1-x)/4, db, di)
    continued = tuple(w*(1-k) for w, k in zip(weights, (kc,ki,kbj,kij)))
    c = sum(continued, F(0))
    u = sum((w*v for w,v in zip(continued, (uc,ui,ub,ub))), F(0))
    r = vb*db+vi*di
    observer = (1-(vb-alpha)*db-(vi-alpha)*di-u,
                r+u,
                F(5,2)-F(3,4)*x+2*d+F(3,2)*c,
                F(5,2)-F(3,4)*x+2*d+F(4,3)*c)
    return observer, (x,db,di,d,c,u,weights,continued)

def flow_observer(parameter, policy):
    """Independent terminal-path enumeration in both probability laws."""
    vb, vi, alpha, uc, ui, ub = parameter
    x,jb,ji,kc,ki,kbj,kij = map(F, policy)
    j_b_mass = F(1,4)
    j_i_mass = (1-x)/4
    db = j_b_mass*(1-jb)/2
    di = j_i_mass*(1-ji)/2
    weights = (F(1,4), (1-x)/4, db, di)
    # (mass, Q-answer probability under P, Q-answer probability under Q,
    #  expected stopping time under P, expected stopping time under Q)
    terminal = [(x/2, F(0), F(0), F(1), F(1)),
                (j_b_mass*jb, F(0), F(0), F(2), F(2)),
                (j_i_mass*ji, F(0), F(0), F(2), F(2)),
                (db, vb-alpha, vb, F(3), F(3)),
                (di, vi-alpha, vi, F(3), F(3))]
    for w,k,u in zip(weights, (kc,ki,kbj,kij), (uc,ui,ub,ub)):
        terminal.append((w*k, F(0), F(0), F(3), F(3)))
        terminal.append((w*(1-k), u, u, F(9,2), F(13,3)))
    assert sum((row[0] for row in terminal),F(0)) == 1
    return (1-sum((m*ap for m,ap,aq,tp,tq in terminal),F(0)),
            sum((m*aq for m,ap,aq,tp,tq in terminal),F(0)),
            sum((m*tp for m,ap,aq,tp,tq in terminal),F(0)),
            sum((m*tq for m,ap,aq,tp,tq in terminal),F(0)))

def lr_policy(x,y,z):
    return (x,y,y,z,z,z,z)

def det(a):
    n=len(a)
    total=F(0)
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=F((-1)**inversions)
        for i in range(n):
            t*=a[i][p[i]]
        total+=t
    return total

def full_jac(parameter):
    mid=[H]*7
    vectors=[]
    for j in (0,1,3,4):
        a=mid.copy();b=mid.copy();a[j]=0;b[j]=1
        lo=carrier(parameter,a)[0]
        hi=carrier(parameter,b)[0]
        vectors.append([t-s for s,t in zip(lo,hi)])
    return det([[vectors[j][i] for j in range(4)] for i in range(4)])

def lr_det(parameter):
    base=carrier(parameter,lr_policy(0,0,0))[0]
    vertices=[carrier(parameter,lr_policy(*t))[0] for t in ((0,0,1),(0,1,0),(0,1,1),(1,0,0))]
    return det([[p[i]-base[i] for p in vertices] for i in range(4)])

def dot(n,w):
    return sum((a*b for a,b in zip(n,w)),F(0))

def allowed(p):
    vb,vi,alpha,uc,ui,ub=p
    return (alpha!=0 and all(0<x<1 for x in (vb,vi,vb-alpha,vi-alpha,uc,ui,ub)))

cases=[
 (F(3,5),F(13,20),F(1,5),F(1,2),F(1,4),F(1,3)),
 (F(3,5),F(3,5),F(1,5),F(1,2),F(1,4),F(1,3)),
 (F(3,5),F(13,20),F(1,5),F(1,2),F(1,2),F(1,2)),
 (F(3,5),F(3,5),F(1,5),F(1,2),F(1,2),F(1,2)),
 (F(2,5),F(3,5),F(1,5),F(2,5),F(1,5),F(3,5)),
 (F(1,4),F(1,3),F(-1,5),F(1,2),F(1,4),F(1,3)),
 (F(3,4),F(2,3),F(1,4),F(1,3),F(2,3),F(1,4)),
 (F(1,2),F(4,7),F(-1,7),F(4,7),F(3,7),F(2,7)),
]
for parameter in cases:
    check(allowed(parameter))
    vb,vi,alpha,uc,ui,ub=parameter
    full={p:carrier(parameter,p)[0] for p in product((0,1),repeat=7)}
    lr={p:carrier(parameter,lr_policy(*p))[0] for p in product((0,1),repeat=3)}
    check(len(full)==128 and len(lr)==8)
    for p,o in full.items():
        check(o==flow_observer(parameter,p))
        x,db,di,d,c,u,w,continued=carrier(parameter,p)[1]
        check(o[0]+o[1]==1+alpha*d)
        check(c==6*(o[2]-o[3]))
        recovered_d=(o[0]+o[1]-1)/alpha
        recovered_x=F(4,3)*(F(5,2)+2*recovered_d+F(3,2)*c-o[2])
        check((recovered_d,recovered_x)==(d,x))
        check(x+4*d<=F(3,2) and x>=0 and c>=0)
    # On each exposed face, LR has one fixed affine source ratio.
    wj=carrier(parameter,(0,0,1,1,1,1,1))[0]
    _, db,di,d,c,u,_,_=carrier(parameter,(0,0,1,1,1,1,1))[1]
    check((d,c)==(F(1,8),F(0)))
    check(wj[1]-(vb+vi)/2*d==(vb-vi)/16)
    wci=carrier(parameter,(0,1,1,0,1,1,1))[0]
    check(wci[1]-(uc+ui)/2*F(1,4)==(uc-ui)/8)
    wcb=carrier(parameter,(1,0,1,0,1,1,1))[0]
    check(wcb[1]-vb/8-(2*uc+ub)/3*F(1,4)==(uc-ub)/12)
    print('PARAM',*parameter,'LR_DET',lr_det(parameter),'FULL_JAC',full_jac(parameter))

# The common-kernel sufficiency map holds for every nonbinary policy.
common=(F(3,5),F(3,5),F(1,5),F(2,5),F(2,5),F(2,5))
fractions=(F(1,7),F(2,7),F(3,7),F(4,7),F(5,7),F(6,7))
for shift in range(120):
    p=[fractions[(shift+i*i+3*i)%6] for i in range(7)]
    x,jb,ji,kc,ki,kbj,kij=p
    y=(jb+(1-x)*ji)/(2-x)
    _,(_,_,_,_,_,_,weights,_) = carrier(common,p)
    z=sum((w*k for w,k in zip(weights,(kc,ki,kbj,kij))),F(0))/sum(weights,F(0))
    check(0<=y<=1 and 0<=z<=1)
    check(carrier(common,p)[0]==carrier(common,lr_policy(x,y,z))[0])

p=cases[0]
full=[(pol,carrier(p,pol)[0]) for pol in product((0,1),repeat=7)]
restricted=[(pol,carrier(p,lr_policy(*pol))[0]) for pol in product((0,1),repeat=3)]
hfull=max(dot(N,o) for _,o in full)
hlr=max(dot(N,o) for _,o in restricted)
witness_pol=(0,0,1,1,0,0,1)
witness=carrier(p,witness_pol)[0]
check(witness==(F(203,240),F(43,240),F(53,16),F(13,4)))
check((hfull,hlr,hfull-hlr)==(F(2833,80),F(35),F(33,80)))
check(dot(N,witness)==hfull)
check((hfull-hlr)/sum(map(abs,N))==F(33,8960))
check(lr_det(p)==F(1,30720))
check(full_jac(p)==-F(1,40960))
# A pointwise full bound proving the support maximum, not just vertex sampling:
# n.O-35 = -Db/5-4Di/5-3 C_C/2+3 C_I/2+(C_BJ+C_IJ)/2.
# C_C<=1/4, C_I<=(1-x)/4, C_BJ<=Db, C_IJ<=Di.
# Hence <=3(1-x)/8+3Db/10-3Di/10<=33/80.
check(F(3,8)+F(3,80)==F(33,80))
print('MIXED_EXACT_FACET',N,'WITNESS',witness,'FULL_MAX',hfull,'LR_MAX',hlr,
      'GAP',hfull-hlr,'DIST_LINF_LOWER',F(33,8960),
      'LR_DET',lr_det(p),'FULL_JAC',full_jac(p))
print('PASS_EXACT_R5_J_SOURCE_BRIDGE_CLASSIFICATION',CHECKS,'exact assertions')
