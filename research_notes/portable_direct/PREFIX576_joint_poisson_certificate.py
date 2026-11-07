#!/usr/bin/env python3
"""PREFIX-576: joint X6-BRC axis/gate Poisson and covariance certificate.
Imports the unchanged published PREFIX565/566 native BRC kernel and quotient.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm
import json
from PREFIX565_positive_marginal_certificate import (
    SCIENCE_PIN, ROOTS, ZERO_ROOT, ACTIONS, PHASES, edge
)
from PREFIX566_gate_quotient_certificate import (
    marginal_gate_rows, weighted_quotient, native_involution
)
PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"

def solve_square(A,b):
    n=len(A); aug=[list(A[i])+[b[i]] for i in range(n)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if aug[r][col]),None)
        if pivot is None: raise AssertionError("singular reduced Poisson system")
        if pivot!=col: aug[col],aug[pivot]=aug[pivot],aug[col]
        p=aug[col][col]; aug[col]=[x/p for x in aug[col]]
        for r in range(n):
            if r==col: continue
            f=aug[r][col]
            if f: aug[r]=[aug[r][c]-f*aug[col][c] for c in range(n+1)]
    return [aug[i][-1] for i in range(n)]

def primitive_scale(values,extra=()):
    den=1
    for x in list(values)+list(extra): den=lcm(den,x.denominator)
    nums=[int(x*den) for x in values]
    g=0
    for x in nums: g=gcd(g,abs(x))
    if g>1: den//=g; nums=[x//g for x in nums]
    return den,nums

def main(depth=64):
    assert SCIENCE_PIN==PIN and len(PHASES)==48 and len(ACTIONS)==6 and len(ROOTS)==9
    native=[[edge(i,a,ZERO_ROOT) for a in ACTIONS] for i in range(96)]
    indegree=Counter(j for row in native for j,w in row)
    assert len(indegree)==96 and set(indegree.values())=={6}
    gate_edges=sorted((i,j) for i,row in enumerate(native) for j,w in row if w[6])
    assert gate_edges==[(7,9),(29,9),(31,9)]

    rows=marginal_gate_rows(ZERO_ROOT)
    assert all(marginal_gate_rows(r)==rows for r in ROOTS)
    ids,Q,growth=weighted_quotient(rows)
    n=len(Q); assert n==37 and growth==[1,4,13,21,33,37]
    sizes=Counter(ids); assert sum(sizes.values())==96
    pi=[F(sizes[i],96) for i in range(n)]
    assert sum(pi)==1
    for k in range(n):
        incoming=sum(sizes[i]*m for i in range(n)
                     for (j,a,b,g),m in Q[i].items() if j==k)
        assert incoming==6*sizes[k]

    P=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,row in enumerate(Q):
        for (j,a,b,g),m in row.items(): P[i][j]+=F(m,6)
    rewards=[]
    for coord in range(3):
        rewards.append([sum(F(m*key[coord+1],6) for key,m in Q[i].items())
                        for i in range(n)])
    mu=[sum(pi[i]*rewards[k][i] for i in range(n)) for k in range(3)]
    assert mu==[F(1,6),F(1,6),F(1,192)]

    IP=[[F(int(i==j))-P[i][j] for j in range(n)] for i in range(n)]
    def poisson(rhs):
        h=[F(0)]+solve_square([row[1:] for row in IP[1:]],rhs[1:])
        assert all(sum(IP[i][j]*h[j] for j in range(n))==rhs[i] for i in range(n))
        return h
    h=[poisson([rewards[k][i]-mu[k] for i in range(n)]) for k in range(3)]
    DEN=768; MU=[int(DEN*x) for x in mu]
    H=[[int(DEN*x) for x in v] for v in h]
    assert all(F(H[k][i],DEN)==h[k][i] for k in range(3) for i in range(n))
    def eta(i,j,a,b,g):
        r=(a,b,g)
        return [DEN*r[k]-MU[k]+H[k][j]-H[k][i] for k in range(3)]
    for i,row in enumerate(Q):
        for k in range(3):
            assert sum(m*eta(i,j,a,b,g)[k] for (j,a,b,g),m in row.items())==0

    cond=[[[F(0) for _ in range(3)] for _ in range(3)] for _ in range(n)]
    for i,row in enumerate(Q):
        for (j,a,b,g),m in row.items():
            e=eta(i,j,a,b,g)
            for k in range(3):
                for l in range(3):
                    cond[i][k][l]+=F(m*e[k]*e[l],6*DEN*DEN)
    Sigma=[[sum(pi[i]*cond[i][k][l] for i in range(n))
            for l in range(3)] for k in range(3)]
    expected=[
        [F(11,216),F(-7,216),F(-1,1728)],
        [F(-7,216),F(11,216),F(-1,1728)],
        [F(-1,1728),F(-1,1728),F(1127,221184)]
    ]
    assert Sigma==expected
    principal_minors=[Sigma[0][0], Sigma[0][0]*Sigma[1][1]-Sigma[0][1]*Sigma[1][0],
                     Sigma[0][0]*(Sigma[1][1]*Sigma[2][2]-Sigma[1][2]*Sigma[2][1])
                     -Sigma[0][1]*(Sigma[1][0]*Sigma[2][2]-Sigma[1][2]*Sigma[2][0])
                     +Sigma[0][2]*(Sigma[1][0]*Sigma[2][1]-Sigma[1][1]*Sigma[2][0])]
    assert principal_minors==[F(11,216),F(1,648),F(373,47775744)]

    pairs=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    wpot={}; scales={}
    for k,l in pairs:
        w=poisson([cond[i][k][l]-Sigma[k][l] for i in range(n)])
        wpot[(k,l)]=w
        den,nums=primitive_scale(w,[Sigma[k][l]])
        scales[(k,l)]=(den,[int(x*den) for x in w],int(Sigma[k][l]*den))

    H575=[0,2,-6,-5,123,2,-1,8,2,-1,18,2,3,2,-4,124,-5,123,-4,
          17,2,-1,18,2,-3,12,5,-4,-1,17,3,6,5,14,17,17,-3]
    W575=[0,4448,-13464,-11245,236819,4424,-2197,17888,4544,-2197,
          40032,4544,6723,4448,-9000,238296,-11245,236819,-8968,
          37871,4544,-2197,40032,4544,-6777,26712,11351,-8968,
          -2197,37871,6723,13536,11351,31424,37871,37871,-6777]
    assert H[2]==H575
    assert primitive_scale(wpot[(2,2)])[0]==1769472
    assert primitive_scale(wpot[(2,2)])[1]==W575

    # Native axis-5/axis-6 swap, preserving ordered actions and gate bit.
    lift=native_involution()
    assert all(lift[lift[i]]==i for i in range(96))
    fixed=sum(lift[i]==i for i in range(96)); assert fixed==32
    class_lift={}
    for i in range(96):
        if ids[i] in class_lift: assert class_lift[ids[i]]==ids[lift[i]]
        else: class_lift[ids[i]]=ids[lift[i]]
    assert len(class_lift)==37
    swap_checks=0
    for i in range(96):
        for action in ACTIONS:
            j,w=edge(i,action,ZERO_ROOT)
            matches=[a for a in ACTIONS if edge(lift[i],a,ZERO_ROOT)==
                     (lift[j],w[:4]+(w[5],w[4])+w[6:])]
            assert len(matches)==1; swap_checks+=1
    assert all(h[0][i]==h[1][class_lift[i]] for i in range(n))
    assert all(h[2][i]==h[2][class_lift[i]] for i in range(n))

    # Independent 96-port dynamic programming for all martingale moments.
    native_edges=[]
    for i in range(96):
        row=[]
        for action in ACTIONS:
            j,w=edge(i,action,ZERO_ROOT)
            m=[DEN*w[4+k]-MU[k]+H[k][ids[j]]-H[k][ids[i]] for k in range(3)]
            row.append((j,m))
        native_edges.append(row)
    mass=[1]*96; sumM=[[0]*96 for _ in range(3)]
    sumMM={p:[0]*96 for p in pairs}
    sumW={p:[scales[p][1][ids[i]] for i in range(96)] for p in pairs}
    mean_checks=second_checks=0
    for d in range(depth+1):
        for i in range(96):
            for k in range(3):
                assert sumM[k][i]==0; mean_checks+=1
            for p in pairs:
                den,wnum,sig_num=scales[p]
                assert sumMM[p][i]*den==DEN*DEN*(
                    d*sig_num*mass[i]+wnum[ids[i]]*mass[i]-sumW[p][i])
                second_checks+=1
        assert all(x==6**d for x in mass)
        if d==depth: break
        nmass=[0]*96; nsumM=[[0]*96 for _ in range(3)]
        nsumMM={p:[0]*96 for p in pairs}; nsumW={p:[0]*96 for p in pairs}
        for i,row in enumerate(native_edges):
            for j,m in row:
                nmass[i]+=mass[j]
                for k in range(3): nsumM[k][i]+=sumM[k][j]+m[k]*mass[j]
                for p in pairs:
                    k,l=p
                    nsumMM[p][i]+=sumMM[p][j]+m[k]*sumM[l][j]+m[l]*sumM[k][j]+m[k]*m[l]*mass[j]
                    nsumW[p][i]+=sumW[p][j]
        mass,sumM,sumMM,sumW=nmass,nsumM,nsumMM,nsumW
    assert mass[0]==6**depth

    transform=[[1,1,0],[1,-1,0],[0,0,1]]
    transformed=[[sum(transform[i][a]*Sigma[a][b]*transform[j][b]
                      for a in range(3) for b in range(3))
                  for j in range(3)] for i in range(3)]
    assert transformed==[
        [F(1,27),F(0),F(-1,864)],
        [F(0),F(1,6),F(0)],
        [F(-1,864),F(0),F(1127,221184)]
    ]
    mean_pots={}
    for name,vec in zip(("q5","q6","gate"),h):
        den,nums=primitive_scale(vec)
        mean_pots[name]={"denominator":den,"numerators":nums}
    second_pots={}
    for k,l in pairs:
        den,wnum,sig_num=scales[(k,l)]
        second_pots[f"{k}{l}"]={
            "common_denominator":den,"numerators":wnum,
            "covariance_rate_numerator":sig_num
        }
    return {
        "status":"ALL_CHECKS_PASS","science_pin":PIN,
        "model":"four-STAR native X6-BRC; 48 phases; 96 ordered ports; six labeled actions",
        "observer":"q1=q2=q3=q4=1; retain q5,q6 and gate z; r5=r6=0",
        "roots_checked":9,"native_ports":96,"native_actions":576,
        "gate_edges":[list(x) for x in gate_edges],
        "quotient_growth":growth,"quotient_classes":n,
        "class_sizes":[sizes[i] for i in range(n)],
        "stationary_class_weights":[str(x) for x in pi],
        "mean_rates":{"q5":"1/6","q6":"1/6","gate":"1/192"},
        "mean_potentials":mean_pots,
        "mean_correction_bounds":{
            "q5":str(max(h[0])-min(h[0])),
            "q6":str(max(h[1])-min(h[1])),
            "gate":str(max(h[2])-min(h[2]))
        },
        "covariance_rate":[[str(x) for x in row] for row in Sigma],
        "covariance_principal_minors":[str(x) for x in principal_minors],
        "sum_difference_gate_covariance_rate":[[str(x) for x in row] for row in transformed],
        "second_poisson_potentials":second_pots,
        "axis_swap_fixed_native_ports":fixed,"axis_swap_checked_edges":swap_checks,
        "conditional_martingale_mean_equations":n*3,
        "second_poisson_equations":n*6,
        "native_direct_dp_depths":[0,depth],
        "native_direct_dp_mean_checks":mean_checks,
        "native_direct_dp_second_moment_checks":second_checks,
        "native_direct_dp_total_checks":mean_checks+second_checks,
        "martingale_identity":"E_i[M_k(d)M_l(d)] = d*Sigma_kl + w_kl(i) - E_i[w_kl(X_d)]",
        "admission":"AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED"
    }

if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,indent=2))
