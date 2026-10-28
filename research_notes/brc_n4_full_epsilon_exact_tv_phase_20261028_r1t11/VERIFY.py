#!/usr/bin/env python3
"""Exact Fraction verifier for the complete epsilon phase, reusing pinned N4 kernel.
Run from a checkout containing the earlier immutable N4 triple-positive
research_notes directory and this directory. No SciPy or LP dependency.
"""
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from runpy import run_path

BASE = Path(__file__).resolve().parent
OLD = BASE.parent / 'brc_n4_triple_positive_strict_tv_superadd_20261028_r1t11'
prior = OLD / 'VERIFY.py'
b = prior.read_bytes()
assert sha1(b'blob ' + str(len(b)).encode() + b'\x00' + b).hexdigest() == '6630a89ffb960d40ebb3a8be12f9432b9e58209c'
core = run_path(str(prior))  # Runs prior exact tree/Bellman + S3 phase tests.
check_flow = core['check_flow']; law = core['law']; full = core['full']
dot = core['dot']; W = core['WEIGHTS']; M = core['expected_min']

blocks = {}; current = None
for line in (BASE / 'CERTIFICATES.txt').read_text(encoding='utf-8').splitlines():
    line = line.strip()
    if not line or line.startswith('#'): continue
    if line.startswith('['):
        current = line[1:-1].split()[0]
        assert current not in blocks
        blocks[current] = {(1,'A','C'): F(1), (1,'B','C'): F(1)}
        continue
    left, value = line.split('=')
    t,h,k = left.split('.')
    key = int(t),h,k
    assert key not in blocks[current]
    blocks[current][key] = F(value)
assert set(blocks) == {'S2_E0','S2_EHALF','S23_E0','S23_EHALF'}

vals = {'S2': (F(1,3036),F(1,759)),
        'S23': (F(1037,1884240),F(2753,1884240))}
zero=F(0); one=F(1); half=F(1,2)

for mode,(v0,vhalf) in vals.items():
    x0, out0=check_flow(blocks[mode+'_E0'], mode, zero, (v0,v0))
    xh, outh=check_flow(blocks[mode+'_EHALF'],mode,half,(vhalf,vhalf))
    assert M[mode] - dot(W[mode], law(full(zero))) == v0
    assert M[mode] - dot(W[mode], law(full(half))) == vhalf
    for eps in (zero,F(1,100),F(1,10),F(1,4),F(255,572),F(9,20),F(49,100),half):
        a=2*eps
        x={key: (one-a)*x0[key]+a*xh[key] for key in x0}
        expected=(one-a)*v0+a*vhalf
        check_flow(x,mode,eps,(expected,expected))
        assert M[mode]-dot(W[mode],law(full(eps))) == expected

def d2(e): return F(1,3036) + e/F(506)
def d23(e): return F(1037,1884240)+F(143,78510)*e
def d3(e): return F(143,31000)*max(zero,e-F(255,572))
def G(e): return d23(e)-d2(e)-d3(e)
crit=F(255,572)
root=F(1682800345,3522923148)
assert zero < crit < F(9,20) < root < half
assert G(root)==0 and G(zero)==F(105341,476712720)
assert G(half)==-F(2537459,23835636000)
assert G(crit)==F(10357483,68169918960)
assert G(F(9,20))==F(243712321,1847261790000)>0
assert d2(crit)>zero and d3(crit)==zero and d3(root)>zero
# The all-real interval theorem uses the affine causal-face argument in PROOF,
# not interpolation of numerical sample results.
print('PASS_EXACT_RATIONAL_N4_FULL_EPSILON_TV_PHASE_REUSE')
print('d2(e) = 1/3036 + e/506')
print('d23(e) = 1037/1884240 + 143*e/78510')
print('critical_epsilon =',crit,'gap_root =',root)
