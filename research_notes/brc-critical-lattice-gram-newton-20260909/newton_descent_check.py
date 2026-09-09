#!/usr/bin/env python3
"""Algebra/regression checks for the causal Newton residual identity and safe score step."""
from __future__ import annotations
import json, math, random
from pathlib import Path
import sympy as s

theta=s.symbols('theta', real=True)
R,C,G=s.symbols('R C G', real=True)
poly=s.expand((1-theta)**2*R+2*theta**2*(1-theta)*C+theta**4*G)
assert s.diff(poly,theta).subs(theta,0)==-2*R

rng=random.Random(20260909)
max_ratio=0.0
for _ in range(2000):
    M=rng.random()*0.98
    rho=10**rng.uniform(-3,3)
    step=min(0.5,(1-M)/(2*rho))
    ratio=math.exp(2*M*step)*(1-step+rho*step*step)**2
    assert ratio < 1.0+1e-14
    max_ratio=max(max_ratio,ratio)

result={
  'status':'PASS',
  'exact_residual_polynomial':str(poly),
  'derivative_at_zero':'-2 R',
  'safe_step_rule':'theta <= min(1/2,(1-M)/(2 rho)) for M<1',
  'random_regressions':2000,
  'max_score_upper_ratio':max_ratio,
  'random_tests_are_not_proofs':True
}
Path(__file__).with_name('newton_descent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
