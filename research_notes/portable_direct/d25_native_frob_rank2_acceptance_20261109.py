#!/usr/bin/env python3
"""Exact rank-2 semilinear-Frobenius consistency oracle (not native H0/B0).

Research TASK D25, p^2 precision, original E3 geometric sign +p.
This validates a proposed full-integral Frobenius matrix only when a
separately authenticated comparison to original geometric cohomology exists.
It does not construct the original H0/B0 divided-power [X]U or kappa.
"""
import json


def ring(p):
    m = p * p

    def add(x, y):
        return ((x[0]+y[0])%m, (x[1]+y[1])%m)

    def neg(x):
        return (-x[0]%m, -x[1]%m)

    def mul(x,y):
        return ((x[0]*y[0]+2*x[1]*y[1])%m,
                (x[0]*y[1]+x[1]*y[0])%m)

    def sigma(x):
        return (x[0]%m, -x[1]%m)

    def inv(x):
        n=(x[0]*x[0]-2*x[1]*x[1])%m
        return mul(sigma(x),(pow(n,-1,m),0))

    Z=(0,0); O=(1,0)

    def mm(A,B):
        return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j]))
                 for j in range(2)] for i in range(2)]

    def sigm(A):
        return [[sigma(a) for a in row] for row in A]

    def det(A):
        return add(mul(A[0][0],A[1][1]),neg(mul(A[0][1],A[1][0])))

    def im(A):
        d=inv(det(A))
        return [[mul(A[1][1],d),mul(neg(A[0][1]),d)],
                [mul(neg(A[1][0]),d),mul(A[0][0],d)]]

    return m, mul, sigma, mm, sigm, det, im, Z, O


def validate(p):
    m,mul,sigma,mm,sigm,det,im,Z,O=ring(p)
    pp=(p,0)
    U=[[O,(0,1)],[(1,1),(2,0)]]
    detU=det(U)
    assert detU == (0,m-1)
    assert mm(im(U),U)==[[O,Z],[Z,O]]
    outcomes={"p":p,"coefficient_ring":f"(Z/{m})[T]/(T^2-2)",
              "gauge_det":list(detU),"gauge_det_norm":(-2)%m}
    for epsilon in (+1,-1):
        A=[[Z,((epsilon*p)%m,0)],[O,Z]]
        A1=mm(mm(im(U),A),sigm(U))
        target=[[(epsilon*p%m,0),Z],[Z,(epsilon*p%m,0)]]
        assert mm(A1,sigm(A1)) == target
        d=det(A1)
        assert d[0]%p == d[1]%p == 0
        assert any(x[0]%p or x[1]%p for row in A1 for x in row)
        assert not (d[0]%(p*p)==0 and d[1]%(p*p)==0)
        outcomes[f"sign_{epsilon:+d}"]={
            "F2_equals":f"{epsilon:+d}p I (mod p^2)",
            "matrix_mod_p2":[[list(x) for x in row] for row in A1],
            "det_mod_p2":list(d),
            "matrix_rank_mod_p":1,
            "elementary_divisor_valuations":[0,1],
            "pass":True,
        }
    if p==373:
        alpha=(92060,21788)
        norm=mul(alpha,sigma(alpha))
        assert norm==(122102,0)
        outcomes["ordinary_Hesse_negative_control"]={
            "a":list(alpha),"N(a)_mod_p2":list(norm),
            "N(a)_mod_p":norm[0]%p,"complete_geometric_F2_match":False,
            "source_type":"previous ordinary-Hesse candidate; not H0/B0"
        }
    return outcomes


if __name__ == "__main__":
    observations=[validate(p) for p in (13,19,373)]
    print(json.dumps({"schema":"D25_RANK2_FROBENIUS_EXACT_V1",
                      "test_kind":"SYNTHETIC_MODEL_REGRESSION_NOT_NATIVE_BENCHMARK",
                      "observer":"full free integral rank-two semilinear F^2=eps*pI",
                      "cases":observations,"all_pass":True},
                      ensure_ascii=False,indent=2))
