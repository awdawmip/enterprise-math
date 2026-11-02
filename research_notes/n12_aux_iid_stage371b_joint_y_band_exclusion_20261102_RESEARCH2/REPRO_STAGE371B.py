#!/usr/bin/env python3
"""Stage371-B exact 6384-leaf joint exclusion. Reuses Stage370 exact source.
Run in the repository's research_notes tree. No floating-point arithmetic.
"""
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from sys import argv
import sys

parent=Path(__file__).resolve().parents[1]
source=parent/'n12_aux_iid_stage370b_two_y_strip_exclusion_20261102_RESEARCH2'/'REPRO_STAGE370B.py'
assert source.is_file(),f'Missing pinned Stage370 dependency: {source}'
spec=spec_from_file_location('repro_stage370b',source)
module=module_from_spec(spec)
old_argv=sys.argv
try:
    sys.argv=[str(source)]
    with redirect_stdout(StringIO()):spec.loader.exec_module(module)
finally:
    sys.argv=old_argv

XL=(F(577,2500),F(239,1000))
LO=(*XL,F(27,50),F(14,25))
HI=(*XL,F(29,50),F(59,100))
TH_LO=F(3748,100000)
TH_HI=F(3746,100000)
low,low_splits=module.cover('LOW_Y',LO,TH_LO)
high,high_splits=module.cover('HIGH_Y',HI,TH_HI)
assert (low_splits,len(low),max(z[1] for z in low))==(6256,6257,20)
assert (high_splits,len(high),max(z[1] for z in high))==(126,127,18)
assert module.lam==F(6,5) and module.BUDGET_UP==F(61,6250)
assert module.CREF_UP==F(6319,100000)
gap=lambda a,b:a+b-module.lam*module.BUDGET_UP-module.CREF_UP
assert tuple(gap(a,b) for a,b in ((TH_LO,TH_LO),(TH_LO,TH_HI),(TH_HI,TH_HI)))==(F(29,500000),F(19,500000),F(9,500000))
fmt=lambda z:f'{z.numerator}/{z.denominator}'
rows=['region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower']
for row in low+high:
    rows.append(','.join((row[0],str(row[1]))+tuple(fmt(z) for z in row[2:])))
csv='\n'.join(rows)+'\n'
assert sha256(csv.encode()).hexdigest()=='8fba0070613f342bd96ac92f49f980bc94e56c723dc8ff443387c072ae47bf01'
assert len(csv.encode())==1194451
if len(argv)==3 and argv[1]=='--emit':Path(argv[2]).write_text(csv,encoding='utf-8')
else:assert len(argv)==1
print('STAGE371B_EXACT_JOINT_Y_BAND_EXCLUSION_PASS')
print('LOW_Y_leaves=',len(low),'LOW_Y_splits=',low_splits,'LOW_Y_max_depth=',max(z[1] for z in low))
print('HIGH_Y_leaves=',len(high),'HIGH_Y_splits=',high_splits,'HIGH_Y_max_depth=',max(z[1] for z in high))
print('joint_cost_gaps_LL_LH_HH=','29/500000,19/500000,9/500000')
print('CSV_bytes=',len(csv.encode()),'CSV_sha256=',sha256(csv.encode()).hexdigest())
