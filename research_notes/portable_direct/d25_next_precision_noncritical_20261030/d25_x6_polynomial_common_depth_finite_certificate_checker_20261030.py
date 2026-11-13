#!/usr/bin/env python3
"""Exact bounded-degree integer-polynomial X6 quotient certificate.

Covers declared polynomial candidates, not native heartbeat dynamics.
A degree-d map's finite grid of d**6 points proves an integer polynomial
relative-observer descent identity globally by multivariate interpolation.
"""
from itertools import product
from pathlib import Path
import json

DIM=6
ZERO=(0,)*DIM


class Poly:
    def __init__(self, terms=None):
        self.terms={k:int(v) for k,v in (terms or {}).items() if v}
        assert all(len(k)==DIM for k in self.terms)
    @staticmethod
    def const(c):return Poly({ZERO:c})
    @staticmethod
    def var(j):
        v=list(ZERO);v[j]=1
        return Poly({tuple(v):1})
    def __add__(self,other):
        if isinstance(other,int):other=Poly.const(other)
        z=self.terms.copy()
        for k,v in other.terms.items():z[k]=z.get(k,0)+v
        return Poly(z)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.terms.items()})
    def __sub__(self,other):return self+-other
    def __rsub__(self,other):return (-self)+other
    def __mul__(self,other):
        if isinstance(other,int):other=Poly.const(other)
        z={}
        for k,a in self.terms.items():
            for l,b in other.terms.items():
                m=tuple(x+y for x,y in zip(k,l));z[m]=z.get(m,0)+a*b
        return Poly(z)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        z=Poly.const(1)
        for _ in range(n):z=z*self
        return z
    def evaluate(self,x):return sum(v*__import__('math').prod(int(x[i])**k[i] for i in range(DIM)) for k,v in self.terms.items())
    def degree(self):return max((sum(k) for k in self.terms),default=0)
    def coefficients(self):return [{"exp":list(k),"coefficient":v} for k,v in sorted(self.terms.items())]


def build_candidates(z):
    q0=z[0]-z[5];q1=z[1]-z[5];q2=z[2]-z[5];h=z[5]
    def add_first(expr):
        out=z.copy();out[0]=out[0]+expr
        return out
    return {
       "relative_quadratic_safe":add_first(q0*q0+q1),
       "depth_quadratic_bad":add_first(h*h),
       "mixed_depth_quadratic_bad":add_first(q0*h),
       "relative_cubic_safe":add_first(q0**3+q1*q2),
       "mixed_depth_cubic_bad":add_first(q0*(h**2)),
       "common_axis_depth_quadratic_safe":[a+h*h for a in z],
    }


def delta_relative_polynomials(candidate):
    # q1..q5,h variables; z_i=q_i+h (i<5), z_6=h
    q=[Poly.var(i) for i in range(5)];h=Poly.var(5)
    z=q_to_z=[a+h for a in q]+[h]
    out=build_candidates(z)[candidate]
    f=[out[i]-out[5] for i in range(5)]
    zplus=[v+1 for v in z]
    outp=build_candidates(zplus)[candidate]
    fp=[outp[i]-outp[5] for i in range(5)]
    return out, [fp[i]-f[i] for i in range(5)]


def main():
    cand=build_candidates([Poly.var(i) for i in range(6)])
    report={}
    checked=0
    for name,zpolys in cand.items():
        d=max(p.degree() for p in zpolys)
        assert d in (2,3)
        out,diff=delta_relative_polynomials(name)
        assert all(p.degree()<=d-1 for p in diff)
        coef_nonzero=sum(len(p.terms) for p in diff)
        safe=coef_nonzero==0
        points=0; nonzero_samples=0; witness=None
        # d points per variable, 6 chart variables; zero on this exact grid iff
        # all components of degree <=d-1 vanish identically.
        for qh in product(range(d),repeat=6):
            q,h=qh[:5],qh[5];z=tuple(q[i]+h for i in range(5))+(h,)
            shifted=tuple(c+1 for c in z)
            def apply(vec):return tuple(p.evaluate(vec) for p in zpolys)
            first,second=apply(z),apply(shifted)
            raw_delta=tuple((second[i]-second[5])-(first[i]-first[5]) for i in range(5))
            symbolic_delta=tuple(p.evaluate(qh) for p in diff)
            assert raw_delta==symbolic_delta
            differs=any(raw_delta)
            if differs:
                nonzero_samples+=1
                if witness is None:
                    witness={"q":list(q),"h":h,"z":list(z),"z_plus_delta":list(shifted),
                             "same_initial_relative_observation":list(q),
                             "relative_one_step_difference":list(raw_delta)}
            points+=1
            checked+=1
        assert safe==(nonzero_samples==0)
        report[name]={"declared_total_degree":d,
                      "finite_exact_interpolation_grid_side":d,
                      "grid_points_checked":points,
                      "all_integer_states_relative_descends":safe,
                      "difference_nonzero_monomial_count":coef_nonzero,
                      "nonzero_grid_witness_count":nonzero_samples,
                      "difference_polynomial_coefficients":[p.coefficients() for p in diff],
                      "first_failure_witness":witness}
    assert report['relative_quadratic_safe']['all_integer_states_relative_descends']
    assert report['relative_cubic_safe']['all_integer_states_relative_descends']
    assert report['common_axis_depth_quadratic_safe']['all_integer_states_relative_descends']
    assert not report['depth_quadratic_bad']['all_integer_states_relative_descends']
    assert not report['mixed_depth_quadratic_bad']['all_integer_states_relative_descends']
    assert not report['mixed_depth_cubic_bad']['all_integer_states_relative_descends']
    output={"schema":"D25_X6_POLYNOMIAL_QUOTIENT_EXACT_GRID_AUTHOR_CHECK_V1",
        "date":"2026-10-30","status":"PASS", "mode":"AUTHOR_EXACT_INTEGER_SYMBOLIC_AND_GRID",
        "candidate_count":len(cand),"state_pair_grid_checks":checked,
        "identity":"delta(q,h)=D[T(Eq+(h+1)delta)-T(Eq+h delta)]",
        "scope":"Declared Z6 polynomial candidates only, not an actual native heartbeat program",
        "cases":report}
    target=Path(__file__).with_name('d25_x6_polynomial_common_depth_finite_certificate_author_check_20261030.json')
    target.write_text(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding='utf-8')
    print(json.dumps({"status":"PASS","cases":len(cand),"grid_checks":checked,
                      "classifications":{k:x['all_integer_states_relative_descends'] for k,x in report.items()}},ensure_ascii=False))

if __name__=='__main__':main()
