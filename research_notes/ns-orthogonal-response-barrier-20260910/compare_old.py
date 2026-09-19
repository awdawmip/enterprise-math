#!/usr/bin/env python3
"""Rerun the unchanged parent dual certificate at a=0.157."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parent
PAR=next(p for p in [ROOT/'parent',ROOT.parent/'ns-goal-primal-dual-certificate-20260910'] if (p/'certify_goal.py').is_file())
assert hashlib.sha256((PAR/'certify_goal.py').read_bytes()).hexdigest()=='954caee644e7a251e7a4631bf94cdca32dd19cd14d7d9577506235b2f59c9a81'
sys.path.insert(0,str(PAR))
import certify_goal as C
if __name__=='__main__':
 d=C.construct();r=C.verify_case(d,F(157,1000),d[0],'dictionary_obstruction')
 (ROOT/'output').mkdir(exist_ok=True)
 (ROOT/'output/old_fixed_norm_obstruction_0157.json').write_text(json.dumps(r,indent=2)+'\n')
