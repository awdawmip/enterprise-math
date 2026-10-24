#!/usr/bin/env python3
"""C291 author-level exact 4D Hessian enclosures for the frozen 79-node model.

Input source: C275/C284/C288 and C290 original Fraction reference code.
Scope: 125 full padded boxes, no native X6 or Source admission.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import C290_PADDED_CHART_EXACT as c

ZERO=F(0);ONE=F(1);Q=c.Q
# Controlled exact dyadic outward rounding: each [lo,hi] replacement is a superset.
# Keeps 79*125*10 interval products bounded in integer size while remaining rigorous.
D=2**72

def floor_d(x):return F((x*D).numerator//(x*D).denominator,D)
def ceil_d(x):return -floor_d(-x)
def enclosing(x):return (floor_d(x[0]),ceil_d(x[1]))
def product_d(a,b):
    ab=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return (floor_d(min(ab)),ceil_d(max(ab)))


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def minus(a,b):return (a[0]-b[1],a[1]-b[0])
def neg(a):return (-a[1],-a[0])
def mul(a,b):
    pp=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return (min(pp),max(pp))
def square_recip(d):
    assert d[0]*d[1]>0,('zero in denominator',d)
    a,b=abs(d[0]),abs(d[1])
    return (ONE/max(a,b)**2,ONE/min(a,b)**2)
def bp(x):return (x,x)
def upperabs(x):return max(abs(x[0]),abs(x[1]))

def moving_kernel_prime(p):
    """Derivative of 6p Σ_{d∈{2,3}} (d-p²)⁻¹; positive increasing on 0<p<1."""
    assert 0<p[0]<=p[1]<1
    def value(v):
        return sum((6/(d-v*v)+12*v*v/(d-v*v)**2 for d in (2,3)),ZERO)
    return (value(p[0]),value(p[1]))

def log_hess_bounds(j,B):
    H=[[bp(ZERO) for k in range(4)] for r in range(4)]
    if j in c.s.J:
        for k in range(4):
            zk=square_recip(c.minus(bp(c.s.Z),B[k]))
            uk=square_recip(c.minus(bp(c.s.U[j]),B[k]))
            H[k][k]=minus(uk,zk)
    else:
        i=c.s.I.index(j)
        p=B[i]
        H[i][i]=moving_kernel_prime(p)
        for j_fixed in c.s.J:
            H[i][i]=add(H[i][i],square_recip(c.minus(p,bp(c.s.U[j_fixed]))))
        for k in range(4):
            if k==i:continue
            pik=square_recip(c.minus(p,B[k]))
            H[i][i]=add(H[i][i],pik)
            H[i][k]=H[k][i]=neg(pik)
            H[k][k]=minus(pik,square_recip(c.minus(bp(c.s.Z),B[k])))
    return H

def Hessian_interval(B,W):
    mid=tuple((a+b)/2 for a,b in B)
    radius=tuple((b-a)/2 for a,b in B)
    out=[[bp(ZERO) for k in range(4)] for l in range(4)]
    max_rho=ZERO
    for j in range(79):
        g_raw=c.log_grad_bounds(j,B)
        g=tuple(enclosing(x) for x in g_raw)
        lh_raw=log_hess_bounds(j,B)
        lh=[[enclosing(x) for x in row] for row in lh_raw]
        rho_hi=ceil_d(sum(upperabs(g[k])*radius[k] for k in range(4)))
        assert ZERO<=rho_hi<F(1,1000)
        max_rho=max(max_rho,rho_hi)
        mid_mass=c.branch_at_midpoint(j,mid,W)
        mass=enclosing((mid_mass/Q,mid_mass/Q))
        M_lo=product_d(mass,bp(ONE-rho_hi))[0]
        M_hi=ceil_d(mass[1]/(ONE-rho_hi))
        M=(M_lo,M_hi)
        for a in range(4):
            for b in range(a,4):
                kernel=add(product_d(g[a],g[b]),lh[a][b])
                contrib=product_d(M,kernel)
                out[a][b]=add(out[a][b],contrib)
                if a!=b: out[b][a]=out[a][b]
    return tuple(tuple(out[a][b] for b in range(4)) for a in range(4)),max_rho

def run():
    paths,_=c.c288.build_paths()
    W,_=c.s.floor_fixed_masses()
    assert len(paths)==125
    maxabs=[[ZERO]*4 for _ in range(4)]
    globallo=[[None]*4 for _ in range(4)]
    globalhi=[[None]*4 for _ in range(4)]
    maxrho=ZERO
    for n,p in enumerate(paths):
        B=tuple((lo-c.PAD,hi+c.PAD) for lo,hi in p['box'])
        L,r=Hessian_interval(B,W)
        maxrho=max(maxrho,r)
        for a in range(4):
            for b in range(4):
                l,h=L[a][b];assert l<=h
                if globallo[a][b] is None or l<globallo[a][b]:globallo[a][b]=l
                if globalhi[a][b] is None or h>globalhi[a][b]:globalhi[a][b]=h
                maxabs[a][b]=max(maxabs[a][b],abs(l),abs(h))
        if (n+1)%25==0:print('CHECKPOINT',n+1,'/125 Hessian enclosures verified',flush=True)
    print('HESSIAN ABS QUOTIENT MATRIX (float display only)')
    for row in maxabs:print([round(float(v),7) for v in row])
    # Explicit coarse symmetric rational majorants; all 125 4D boxes certified.
    candidates=[F(50),F(100),F(200),F(400),F(800),F(1600),F(3200),F(6400),F(12800),F(25600),F(51200),F(102400),F(204800),F(409600),F(819200),F(1638400)]
    rational_bounds=[[next(b for b in candidates if maxabs[a][bidx]<b) for bidx in range(4)] for a in range(4)]
    assert rational_bounds==[list(row) for row in zip(*rational_bounds)]
    # For f=F/Q and tau=q/Q, the local implicit map y=Phi(x1,x2,x3,tau)
    # uses |Phi_x| < (5/2,5/3,4/3), |Phi_tau| < 5/6.
    # T_i=(e_i,Phi_i) is lifted into ambient coordinate order (v5,v50,v55,v56).
    # |D² Phi_ij| < (5/6) sum_ab C_ab * A_ai * A_bj,
    # because f_y > 6/5 on every padded box.
    C=max(sum(rational_bounds[a]) for a in range(4))
    A=((ONE,ZERO,ZERO,ZERO),
       (ZERO,ONE,ZERO,ZERO),
       (F(5,2),F(5,3),F(4,3),F(5,6)),
       (ZERO,ZERO,ONE,ZERO))
    chart_K=[[F(5,6)*sum(A[a][i]*rational_bounds[a][b]*A[b][j]
                   for a in range(4) for b in range(4)) for j in range(4)]
             for i in range(4)]
    assert chart_K==[list(row) for row in zip(*chart_K)]
    chart_max=max(x for row in chart_K for x in row)
    chart_inf_row=max(sum(row) for row in chart_K)
    report={
        'schema':'EM_C291_ALL_125_FULL_PADDED_HESSIAN_EXACT_V1',
        'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
        'n_paths':len(paths),'n_4d_padded_boxes':len(paths),'n_branch_hessians':125*79,
        'n_second_partials_checked':125*10,
        'axes':['v5','v50','v55','v56'],
        'hessian_uniform_abs_over_Q_matrix':[[str(v) for v in row] for row in rational_bounds],
        'hessian_global_inf_row_sum_over_Q_lt':str(C),
        'normal_v55_pure_second_over_Q_lt':str(rational_bounds[2][2]),
        'hessian_min_max_over_Q_approx_display_only':[[[round(float(globallo[i][j]),6),round(float(globalhi[i][j]),6)] for j in range(4)] for i in range(4)],
        'chart_parameter_order':['v5','v50','v56','tau=q/Q'],
        'chart_second_derivative_bound_matrix':[[str(x) for x in row] for row in chart_K],
        'max_chart_second_partial_abs_lt':str(chart_max),
        'chart_gradient_lipschitz_linf_lt':str(chart_inf_row),
        'max_log_mass_radius_lt_1_over_1000':bool(maxrho<F(1,1000)),
        'all_comparisons_exact_Fraction':True,
        'symmetric_hessian':True,
        'only_author_level':True,'source_result_published':False,'driver_accepted':False,
        'native_GF2_BRC_X6_transfer':False,
    }
    with open('C291_AUTHOR_EXACT_AUDIT_20261025.json','w',encoding='utf-8') as f:
        json.dump(report,f,ensure_ascii=False,sort_keys=True,indent=2);f.write('\n')
    print('C291_125_FULL_4D_HESSIAN_AUTHOR_EXACT_PASS',125,'boxes',125*79,'branch Hessians',125*10,'unique second partials')
    print('uniform global infinity-row bound <',C,'Q')
    print('uniform implicit chart max Hessian entry <',chart_max,'and gradient Lipschitz infinity row sum <',chart_inf_row)
    return report
if __name__=='__main__':run()
