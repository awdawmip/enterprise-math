#!/usr/bin/env python3
"""Generate exact, deterministic p17 T6 order8 finite input for the C++17
outward-integer-interval checker. Reuse verified saturated q0 basis and
integer modular lifts from the canonical order5 exact checker.
Python 3.12, sympy 1.14. No floating-point decisions.
Invocation:
 python research_checks/T6_P17_Q8_INTERVAL_GENERATOR_20261123.py ./t6q8_run
 g++ -O3 -std=c++17 research_checks/T6_P17_Q8_INTERVAL_EXHAUSTIVE_CHECK_20261123.cpp -o ./t6q8_check
 ./t6q8_check ./t6q8_run 2 6
 ./t6q8_check ./t6q8_run 3 5
 ./t6q8_check ./t6q8_run 4 4
"""
import importlib.util
import hashlib, sys
from pathlib import Path
from itertools import combinations_with_replacement, product
from fractions import Fraction
src=Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p17_q5_exact",src)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else Path.cwd()
OUT.mkdir(parents=True,exist_ok=True)
P=17; CAP=2331
W=old.W;U=old.U;Q=old.Q;D=old.D;mu=old.mu;N=old.N
assert Q==24137569 and min(D)>3354730
ATOM={}
for q in range(1,9):
    for r in range(1,17):
        cost=289*q+17*r-1
        if cost>CAP:continue
        u=old.particular_atom(q,r)
        co=tuple(sum(u[j]*N[j][i] for j in range(16)) for i in range(16))
        ATOM[q,r]=(co,cost)
def partitions(s,least=1):
    if not s:yield ()
    else:
        for q in range(least,s+1):
            for tail in partitions(s-q,q):yield (q,)+tail
def states(s):
    for pt in partitions(s):
        opts=[[(q,r) for r in combinations_with_replacement(range(1,17),pt.count(q))]
              for q in sorted(set(pt))]
        for grp in product(*opts):
            atoms=tuple((q,r) for q,rr in grp for r in rr)
            cost=sum(ATOM[a][1] for a in atoms) if all(a in ATOM for a in atoms) else CAP+1
            if cost>CAP:continue
            coord=tuple(sum(ATOM[a][0][i] for a in atoms) for i in range(16))
            yield atoms,cost,coord
S={d:list(states(d)) for d in (2,3,4,5,6)}
assert [len(S[d]) for d in (2,3,4,5,6)]==[152,1088,6460,30040,47628]
for d,ss in S.items():
    with (OUT/f't6q8_states{d}.txt').open('w') as f:
        f.write(str(len(ss))+'\n')
        for atoms,cost,coord in ss:
            f.write(str(cost)+' '+str(len(atoms))+' '+
                    ' '.join(f'{q*16+r-1}' for q,r in atoms)+' '+
                    ' '.join(str(x%Q) for x in coord)+'\n')
SCALE=1<<32
with (OUT/'t6q8_interval_constants.txt').open('w') as f:
    f.write(f'{Q} {SCALE}\n')
    f.write(' '.join(str(v.numerator//v.denominator) for v in D)+'\n')
    for row in mu:
        f.write(' '.join(str((v.numerator*SCALE)//v.denominator) for v in row)+'\n')
    for row in mu:
        f.write(' '.join(str(-((-v.numerator*SCALE)//v.denominator)) for v in row)+'\n')
    f.write(' '.join(str(w) for w in W)+'\n')
    for row in U:f.write(' '.join(str(v) for v in row)+'\n')
for d in (2,3,4,5,6):
    path=OUT/f't6q8_states{d}.txt'
    print(d,len(S[d]),hashlib.sha256(path.read_bytes()).hexdigest())
path=OUT/'t6q8_interval_constants.txt'
print('GS',hashlib.sha256(path.read_bytes()).hexdigest())
