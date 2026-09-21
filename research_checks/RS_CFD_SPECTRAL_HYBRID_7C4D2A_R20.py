from fractions import Fraction
from itertools import product
import json


def wmax(n, k, u, rho):
    assert n >= 1 and 0 <= k <= n and 0 <= u <= n-k and rho >= 1
    m = k + u
    if m == 0:
        return Fraction(0)
    return Fraction(m) * rho / (Fraction(m) * rho + (n-m))


def speedup_ceiling(n, k, u, rho, alpha, f, h):
    w = wmax(n,k,u,rho)
    den = Fraction(1) - alpha*f*w + h
    if den <= 0:
        return None
    return Fraction(1,1) / den


def tau_for_target(q, alpha, f, h):
    assert q > 1
    af = alpha*f
    if af == 0:
        return None
    return (Fraction(1) - Fraction(1,1)/q + h) / af


def max_total_eligible_for_target(n, rho, q, alpha, f, h):
    tau = tau_for_target(q, alpha, f, h)
    if tau is None:
        return n
    if tau >= 1:
        return n
    assert tau > 0
    threshold = tau*n / (rho*(1-tau)+tau)
    return min(n, threshold.numerator // threshold.denominator)


def max_unknown_for_target(n,k,rho,q,alpha,f,h):
    return max_total_eligible_for_target(n,rho,q,alpha,f,h)-k


grid_checks = 0
sharp_checks = 0
for n in range(1,6):
    for k in range(n+1):
        for u in range(n-k+1):
            K=set(range(k))
            U=list(range(k,k+u))
            for rho_i in range(1,5):
                rho=Fraction(rho_i)
                bound=wmax(n,k,u,rho)
                for mask in range(1<<u):
                    E=K|{U[j] for j in range(u) if (mask>>j)&1}
                    for bits in product([0,1], repeat=n):
                        d=[rho if b else Fraction(1) for b in bits]
                        D=sum(d, Fraction(0))
                        w=sum((d[i] for i in E), Fraction(0))/D if E else Fraction(0)
                        assert w <= bound
                        grid_checks += 1
                E=K|set(U)
                d=[rho if i in E else Fraction(1) for i in range(n)]
                D=sum(d, Fraction(0))
                w=sum((d[i] for i in E), Fraction(0))/D if E else Fraction(0)
                assert w == bound
                sharp_checks += 1

inversion_checks=0
for n in range(1,11):
  for k in range(n+1):
    for u in range(n-k+1):
      for rho_i in range(1,4):
        rho=Fraction(rho_i)
        for q in [Fraction(11,10),Fraction(5,4)]:
          for alpha in [Fraction(1,2),Fraction(1)]:
            for f in [Fraction(1,2),Fraction(1)]:
              for h in [Fraction(0),Fraction(1,50)]:
                tau=tau_for_target(q,alpha,f,h)
                lhs=wmax(n,k,u,rho) <= tau
                mmax=max_total_eligible_for_target(n,rho,q,alpha,f,h)
                rhs=(k+u)<=mmax
                assert lhs==rhs
                sceil=speedup_ceiling(n,k,u,rho,alpha,f,h)
                speed_ok=(sceil is not None and sceil <= q)
                assert speed_ok == lhs
                inversion_checks += 1

zero_effect_checks=0
for alpha,f in [(Fraction(0),Fraction(1)),(Fraction(1),Fraction(0))]:
    for u in range(6):
        assert max_total_eligible_for_target(5,Fraction(3),Fraction(11,10),alpha,f,Fraction(1,50)) == 5
        assert speedup_ceiling(5,0,u,Fraction(3),alpha,f,Fraction(1,50)) <= 1
        zero_effect_checks+=1

n=20; rho=Fraction(2); alpha=Fraction(7,10); f=Fraction(4,5); h=Fraction(1,50); q=Fraction(11,10)
tau=tau_for_target(q,alpha,f,h)
assert tau == Fraction(61,308)
assert max_total_eligible_for_target(n,rho,q,alpha,f,h) == 2
assert wmax(20,2,0,rho) == Fraction(2,11)
assert speedup_ceiling(20,2,0,rho,alpha,f,h) == Fraction(110,101)
assert max_unknown_for_target(20,2,rho,q,alpha,f,h) == 0
assert max_unknown_for_target(20,1,rho,q,alpha,f,h) == 1
assert max_unknown_for_target(20,0,rho,q,alpha,f,h) == 2
assert wmax(20,2,1,rho) == Fraction(6,23)
assert speedup_ceiling(20,2,1,rho,alpha,f,h) == Fraction(230,201)
assert Fraction(230,201) > q

out={
  "schema":"ENTERPRISE_MATH_CFD_ROUTE_UNCERTAINTY_CERTIFICATE_V1",
  "status":"EXACT_DERIVATION_PLUS_FINITE_CHECK_NO_NATIVE_BENCHMARK",
  "theorem":{
    "m":"k+u",
    "eligible_dense_work_share_upper":"m*rho/(m*rho+n-m)",
    "trajectory_speedup_upper":"1/(1-alpha_bar*f_bar*w_max+h_floor)",
    "target_tau":"(1-1/q+h_floor)/(alpha_bar*f_bar)",
    "target_m_max_when_0_lt_tau_lt_1":"floor(tau*n/(rho*(1-tau)+tau))"
  },
  "finite_checks":{
    "route_and_cost_grid":grid_checks,
    "sharp_witnesses":sharp_checks,
    "target_inversion_grid":inversion_checks,
    "zero_effect_boundaries":zero_effect_checks
  },
  "illustration_not_measurement":{
    "n":20,"rho":"2","alpha_bar":"7/10","f_bar":"4/5","h_floor":"1/50","q":"11/10",
    "tau":"61/308","m_max":2,
    "k2_u_max":0,"k1_u_max":1,"k0_u_max":2,
    "k2_u0_ceiling":"110/101",
    "k2_u1_ceiling":"230/201"
  },
  "boundary":"Unknown-route calls are treated worst-case as eligible. Requires a separately certified finite dense-call heterogeneity bound rho and valid alpha_bar,f_bar,h_floor bounds. No native-host timing claim."
}
print(json.dumps(out,indent=2,sort_keys=True))
