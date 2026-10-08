"""Compare immutable published JSON evidence with independently calculated data.
Does not import any author implementation. Run after independent_audit.py.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from functools import reduce
import json
from independent_audit import primitive, enc

ROOT=Path(__file__).resolve().parent
INPUT=ROOT.parent/'inputs'
mine=json.loads((ROOT/'INDEPENDENT_CHECKS.json').read_text())
authd=json.loads((INPUT/'diagonal/RUN.json').read_text())
autho=json.loads((INPUT/'offdiagonal/offdiag_checks.json').read_text())
matches=[]
for original in authd['family_samples']:
    own=next(x for x in mine['diagonal'] if x['n']==original['n'])
    assert list(map(F,own['point']))==list(map(F,original['elliptic_point']))
    assert list(map(F,own['signed_fiber']))==list(map(F,original['raw_signed_triple']))
    assert list(map(F,own['primitive_six']))==list(map(F,original['primitive_sextuple']))
    ours=sorted(F(r) for c in own['cells'] for r in c['roots'])
    assert ours==sorted(map(F,original['outer_roots']))
    matches.append({'branch':'diagonal','n':original['n'],'exact_point_signed_fiber_primitive_roots':True})
for original in autho['rows']:
    own=next(x for x in mine['offdiagonal'] if x['n']==original['n'])
    for key in ('d','mu','nu','h','t'):assert F(own[key])==F(original[key])
    assert own['lcm']==original['D']
    assert list(map(F,own['point']))==list(map(F,original['point']))
    assert list(map(F,own['H']+own['T']))==list(map(F,original['datum']))
    for cell in own['cells']:
        key=str(tuple(cell['cell']))
        assert sorted(map(F,cell['roots']))==sorted(map(F,original['roots'][key]))
    matches.append({'branch':'offdiagonal','n':original['n'],'exact_point_cell_labeled_roots_AP':True})
witnesses=[]
for v in [(176,57,185,105,208,56),(2720,165,2725,1533,2444,2044)]:
    x,y,b,d,mu,nu=map(F,v);a=x+y;c=x-y
    assert x*x+y*y==b*b and d*d+mu*mu==a*a and d*d+nu*nu==c*c
    ds={(0,0):a,(0,1):b,(0,2):c,(1,0):mu,(1,2):nu,(2,0):a,(2,1):b,(2,2):c}
    data=primitive(F(0),d,(d*d-b*b)/4,x*y/2,ds)
    assert data['scale']==1
    witnesses.append({'sextuple':v,'independent_direct_pairability_and_gcd':True})
result={'schema':'P11_FROZEN_EVIDENCE_COMPARISON_V1','author_code_executed':False,'all_matches':True,'matching_published_rows':matches,'known_witnesses':witnesses,'unpublished_extra_control_multipliers':{'diagonal':[4,5,6,7,8],'offdiagonal':[13]},'documentary_limits':['ARITHMETIC.md is named in diagonal VALIDATION.md but absent from accepted output manifest; audit does not rely on it.','Temporary REPRODUCED.json and external PDF bytes are not contained in the accepted manifest; their historical byte claims were not independently reproduced.','Native source controls and immutable input artifacts were verified separately.','SymPy version is recorded by the independent audit run; source authors did not pin it in the offdiagonal manifest.']}
(ROOT/'FROZEN_EVIDENCE_COMPARISON.json').write_text(json.dumps(enc(result),indent=2)+'\n')
print(json.dumps({'status':'PASS','matching_published_rows':len(matches),'known_witnesses':len(witnesses),'author_code_executed':False}))
