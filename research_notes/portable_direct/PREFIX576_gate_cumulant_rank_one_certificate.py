#!/usr/bin/env python3
"""PREFIX-576: exact third/fourth gate-cumulant rates by BRC rank-one perturbation.

Frozen science pin: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reuses, unchanged at runtime, the published PREFIX565/566 native BRC kernel and
37-class gate-preserving quotient, plus PREFIX575's exact first/second Poisson
potentials.  Standard-library Fraction/integer arithmetic only.
"""
from collections import Counter, deque
from fractions import Fraction
import json

from PREFIX565_positive_marginal_certificate import (
    SCIENCE_PIN, ZERO_ROOT, ROOTS, ACTIONS, edge
)
from PREFIX566_gate_quotient_certificate import marginal_gate_rows, weighted_quotient
from PREFIX575_gate_count_poisson_certificate import PIN, H, W

PIN_EXPECTED = "f42f2906d77f24085c123f3ccfe9667d41caa96d"

# Mean-zero resolvent Poisson potentials for (I-P)^(-1), (I-P)^(-2), (I-P)^(-3).
X = (-25,-19,-43,-40,344,-19,-28,-1,-19,-28,29,-19,-16,-19,-37,347,
     -40,344,-37,26,-19,-28,29,-19,-34,11,-10,-37,-28,26,-16,-7,-10,17,26,26,-34)
Y = (-373,-115,-1183,-988,3620,-79,-556,299,-259,-556,653,-259,-76,-115,
     -841,3767,-988,3620,-889,578,-259,-556,653,-259,-670,599,-142,-889,
     -556,578,-76,5,-142,245,578,578,-670)
Z = (-3709,2957,-26551,-18940,36356,5801,-10012,7907,-2803,-10012,8333,
     -2803,3716,2957,-14833,40463,-18940,36356,-17041,7970,-2803,-10012,
     8333,-2803,-9406,12815,-4414,-17041,-10012,7970,3716,-307,-4414,
     941,7970,7970,-9406)

def reach(graph, start):
    seen={start}; q=deque([start])
    while q:
        i=q.popleft()
        for j in graph[i]:
            if j not in seen:
                seen.add(j); q.append(j)
    return seen

def main(depth=128):
    assert SCIENCE_PIN == PIN == PIN_EXPECTED
    assert len(ROOTS)==9 and len(ACTIONS)==6

    native = [[edge(i,a,ZERO_ROOT) for a in ACTIONS] for i in range(96)]
    assert all(len(row)==6 for row in native)
    indegree=Counter(j for row in native for j,w in row)
    assert set(indegree)==set(range(96)) and set(indegree.values())=={6}
    native_gate_edges=sorted((i,j) for i,row in enumerate(native) for j,w in row if w[6])
    assert native_gate_edges==[(7,9),(29,9),(31,9)]

    rows=marginal_gate_rows(ZERO_ROOT)
    assert len(rows)==96
    assert all(marginal_gate_rows(root)==rows for root in ROOTS)
    ids,Q,growth=weighted_quotient(rows)
    assert len(Q)==37 and growth==[1,4,13,21,33,37]

    n=37
    C=[[0]*n for _ in range(n)]
    g=[0]*n
    gate_edges=[]
    for i,row in enumerate(Q):
        for (j,a5,a6,mark),mult in row.items():
            C[i][j]+=mult
            g[i]+=mult*mark
            if mark:
                gate_edges.append((i,j,mult,a5,a6))
    assert all(sum(row)==6 for row in C)
    assert sorted(gate_edges)==[(4,5,1,0,0),(15,5,1,0,0),(17,5,1,0,0)]
    assert [(i,v) for i,v in enumerate(g) if v]==[(4,1),(15,1),(17,1)]

    sizes=Counter(ids)
    assert sum(sizes.values())==96
    # Pushforward of uniform native-port counting is stationary.
    assert all(sum(sizes[i]*C[i][j] for i in range(n))==6*sizes[j] for j in range(n))
    pi=[Fraction(sizes[i],96) for i in range(n)]
    gate_source_mass=sum(pi[i]*g[i] for i in range(n))
    assert gate_source_mass==Fraction(1,32)
    a=gate_source_mass/6
    assert a==Fraction(1,192)

    # The gate-marked matrix is exactly rank one: g e_5^T / 6.
    # P(z)=P(1)+(z-1)g e_5^T/6.
    adj=[{j for j,v in enumerate(C[i]) if v} for i in range(n)]
    rev=[set() for _ in range(n)]
    for i in range(n):
        for j in adj[i]: rev[j].add(i)
    assert len(reach(adj,0))==len(reach(rev,0))==37
    color=[None]*n; color[0]=0; q=deque([0])
    while q:
        i=q.popleft()
        for j in adj[i]:
            if color[j] is None:
                color[j]=1-color[i]; q.append(j)
            else:
                assert color[j]==1-color[i]
    assert (color.count(0),color.count(1))==(17,20)
    assert 7 in adj[0] and 0 in adj[7]  # period exactly 2

    # Recheck PREFIX575's first/second Poisson identities on the exact same quotient.
    assert len(H)==len(W)==37
    assert all(6*H[i]-sum(C[i][j]*H[j] for j in range(n))==768*g[i]-24
               for i in range(n))
    V=[]
    for i,row in enumerate(Q):
        v=0
        for (j,a5,a6,mark),mult in row.items():
            m=768*mark-4+H[j]-H[i]
            v+=mult*m*m
        V.append(v)
    assert all(6*W[i]-sum(C[i][j]*W[j] for j in range(n))==3*V[i]-54096
               for i in range(n))
    assert sum(sizes[i]*V[i] for i in range(n))==1731072

    # L=6I-C.  X/384, Y/4608, Z/55296 are successive mean-zero
    # group-inverse potentials for g-(pi g)1, X/384, Y/4608.
    L=[[6*(i==j)-C[i][j] for j in range(n)] for i in range(n)]
    assert len(X)==len(Y)==len(Z)==n
    assert all(sum(L[i][j]*X[j] for j in range(n))==2304*g[i]-72 for i in range(n))
    assert all(sum(L[i][j]*Y[j] for j in range(n))==72*X[i] for i in range(n))
    assert all(sum(L[i][j]*Z[j] for j in range(n))==72*Y[i] for i in range(n))
    assert sum(sizes[i]*X[i] for i in range(n))==0
    assert sum(sizes[i]*Y[i] for i in range(n))==0
    assert sum(sizes[i]*Z[i] for i in range(n))==0

    # Laurent coefficients of R(lambda)=e_5^T(lambda I-P)^(-1)g/6.
    r0=Fraction(X[5],384*6)
    r1=-Fraction(Y[5],4608*6)
    r2=Fraction(Z[5],55296*6)
    assert (r0,r1,r2)==(Fraction(-19,2304),Fraction(79,27648),Fraction(5801,331776))

    # Solve 1=(z-1)R(lambda) for lambda(z)=1+sum c_j(z-1)^j.
    c1=a
    c2=a*r0
    c3=a*r0*r0+a*a*r1
    c4=a*r0**3+3*a*a*r0*r1+a**3*r2
    k1=c1
    k2=c1+2*c2-c1*c1
    k3=c1+6*c2+6*c3-3*c1*c1-6*c1*c2+2*c1**3
    u1=c1
    u2=c1/2+c2
    u3=c1/6+c2+c3
    u4=c1/24+Fraction(7,12)*c2+Fraction(3,2)*c3+c4
    k4=24*(u4-(u1*u3+u2*u2/2)+u1*u1*u2-u1**4/4)
    assert (k1,k2,k3,k4)==(
        Fraction(1,192),
        Fraction(1127,221184),
        Fraction(206963,42467328),
        Fraction(434651857,97844723712)
    )

    # Exact stationary-initial DP for raw moments through order four.
    trans=[]
    for row in Q:
        c=Counter()
        for (j,a5,a6,mark),mult in row.items():
            c[(j,mark)]+=mult
        trans.append(c)
    count=[int(sizes[i]) for i in range(n)]
    m1=[0]*n; m2=[0]*n; m3=[0]*n; m4=[0]*n
    snapshots=[]
    for d in range(depth+1):
        total=sum(count)
        assert total==96*(6**d)
        E1=Fraction(sum(m1),total)
        E2=Fraction(sum(m2),total)
        E3=Fraction(sum(m3),total)
        E4=Fraction(sum(m4),total)
        var=E2-E1**2
        cum3=E3-3*E2*E1+2*E1**3
        cum4=E4-4*E3*E1-3*E2**2+12*E2*E1**2-6*E1**4
        if d:
            assert E1==Fraction(d,192)
        if d in (10,20,40,80,128):
            snapshots.append({
                "depth":d,
                "total_paths":str(total),
                "mean_per_step":str(E1/d),
                "variance_per_step":str(var/d),
                "third_cumulant_per_step":str(cum3/d),
                "fourth_cumulant_per_step":str(cum4/d)
            })
        if d==depth:
            break
        nc=[0]*n; nm1=[0]*n; nm2=[0]*n; nm3=[0]*n; nm4=[0]*n
        for i,row in enumerate(trans):
            for (j,b),mult in row.items():
                nc[j]+=mult*count[i]
                nm1[j]+=mult*(m1[i]+b*count[i])
                nm2[j]+=mult*(m2[i]+2*b*m1[i]+b*count[i])
                nm3[j]+=mult*(m3[i]+3*b*m2[i]+3*b*m1[i]+b*count[i])
                nm4[j]+=mult*(m4[i]+4*b*m3[i]+6*b*m2[i]+4*b*m1[i]+b*count[i])
        count,m1,m2,m3,m4=nc,nm1,nm2,nm3,nm4

    p=Fraction(1,192)
    iid=(p*(1-p),p*(1-p)*(1-2*p),p*(1-p)*(1-6*p*(1-p)))
    return {
        "status":"ALL_CHECKS_PASS",
        "line":"PREFIX-576",
        "science_pin":PIN_EXPECTED,
        "model":"frozen four-STAR native X6-BRC; 96 ordered ports; six uniformly selected labeled actions",
        "observer":"q1=q2=q3=q4=q5=q6=1; gate counter retained",
        "quotient":{"native_ports":96,"classes":37,"partition_growth":growth,
                    "class_sizes":[sizes[i] for i in range(n)],
                    "stationary_distribution":"pi_i=class_size_i/96",
                    "gate_sources":[4,15,17],"gate_target":5,
                    "gate_perturbation":"P(z)=P(1)+(z-1) g e_5^T/6",
                    "bipartition":[17,20],"period":2},
        "resolvent_laurent":{"a_minus1":str(a),"r0":str(r0),"r1":str(r1),"r2":str(r2)},
        "poisson_potentials":{
            "X_denominator":384,"X":list(X),
            "Y_denominator":4608,"Y":list(Y),
            "Z_denominator":55296,"Z":list(Z),
            "integer_equations":["(6I-C)X=2304g-72*1","(6I-C)Y=72X","(6I-C)Z=72Y"],
            "weighted_mean_zero":True},
        "lambda_delta_coefficients":{"c1":str(c1),"c2":str(c2),"c3":str(c3),"c4":str(c4)},
        "asymptotic_cumulant_rates":{"kappa1":str(k1),"kappa2":str(k2),
                                     "kappa3":str(k3),"kappa4":str(k4)},
        "scaled_cumulant_generating_function_through_order_4":
            "s/192 + 1127*s^2/442368 + 206963*s^3/254803968 + 434651857*s^4/2348273369088 + O(s^5)",
        "iid_bernoulli_same_mean":{"kappa2":str(iid[0]),"kappa3":str(iid[1]),"kappa4":str(iid[2])},
        "finite_stationary_integer_DP":{"depths_checked":[0,depth],
                                        "raw_moment_orders":[1,2,3,4],
                                        "snapshots":snapshots},
        "validation":{"native_gate_edges":native_gate_edges,
                      "quotient_gate_edges":sorted(gate_edges),
                      "first_poisson_rows":37,"second_poisson_rows":37,
                      "higher_poisson_integer_rows":[37,37,37],
                      "moment_DP_states":37,
                      "moment_DP_transition_types":sum(len(x) for x in trans),
                      "all_assertions_pass":True},
        "status_boundary":"AUTHOR_PROVED / EXACT_RATIONAL_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED",
        "limitations":["q1..q6 are specialized to 1; no x,y parameterized gate cumulants",
                       "gate index counts ordered native actions, not physical time",
                       "independent review and native activity/claim/result remain pending"]
    }

if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,indent=2))
