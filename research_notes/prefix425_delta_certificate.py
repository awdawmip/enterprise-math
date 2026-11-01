#!/usr/bin/env python3
"""PREFIX-425 exact extension to frozen PREFIX-423 checker.
Run: python prefix425_delta_certificate.py path/to/prefix423_exact_certificate.py
The predecessor is archived in research_notes/PREFIX423_CODE_EVIDENCE.tar.br
at commit 9a1ea3ab71469ff6a4f645852d1be9f33b09fdc9.
"""
import runpy
import sys
from pathlib import Path
from fractions import Fraction as Fr
from collections import Counter

src=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('prefix423_exact_certificate.py'))
assert src.is_file(), f'Missing exact predecessor: {src}'
d=runpy.run_path(str(src))
IV,Q,model=d['IV'],d['Q'],d['model']
rbox,sbox,beta,E=d['rbox'],d['sbox'],d['beta'],d['E']
left,right=Fr(1,500),Fr(39,2000)
lam=Q(Fr(39,20))
assert (16-E*lam).lo>0
end_vs=model(rbox,sbox,Q(right))['Vs']
assert end_vs.hi<0, ('end Vs',end_vs.dec())

def margins(a,b):
    eta=IV.b(a,b)
    m=model(rbox,sbox,eta,-1)
    r,s=rbox,sbox
    a0=(s-r-1)/2
    phase=(r-a0*a0).sqrt()
    J=(53+29*r)/2+39*a0-4*phase
    A=36+28*a0+12*phase
    B=-20-12*a0+28*phase
    P=(245*(1+a0)+123*phase)/16
    W=(-123*(1+a0)+245*phase)/16
    c=Q(Fr(709,64))*(s-2)
    Ap=A-lam*P; Bp=B-lam*W
    F=J+lam*(eta-c)+(16-E*lam)*beta+beta.sqrt()*(Ap*Ap+Bp*Bp).sqrt()
    return {
        'Nbeta-K^2':m['R'],
        'mu':m['mu'],
        'D':m['D'],
        'tau':m['tau'],
        'eta+h':eta+m['h'],
        'eta-h':eta-m['h'],
        '-V_r':-m['Vr'],
        'V_s_eta':m['Vse'],
        'V-41':m['V']-41,
        '41-F':41-F,
        '82-V-F':82-m['V']-F,
    }

stack=[(left,right,0)]
accepted=[]
failures=Counter()
while stack:
    a,b,k=stack.pop()
    vals=margins(a,b)
    bad=[name for name,v in vals.items() if v.lo<=0]
    if bad:
        failures.update(bad)
        assert k<24,(a,b,k,bad)
        mid=(a+b)/2
        stack.extend([(mid,b,k+1),(a,mid,k+1)])
    else:
        accepted.append((a,b,k,vals))
accepted.sort(key=lambda item:item[0])
assert accepted[0][0]==left and accepted[-1][1]==right
assert all(accepted[j][1]==accepted[j+1][0] for j in range(len(accepted)-1))
assert len(accepted)<100000
print('PREFIX425_RANGE',left,right,'ALL_EPS',0,beta.dec())
print('PREFIX425_LAMBDA',Fr(39,20),'END_V_s_UPPER',end_vs.dec())
print('PREFIX425_EXACT_CHECKS',11*len(accepted)+1,'CLOSED_SUBBOXES',len(accepted),'MAX_DEPTH',max(k for _,_,k,_ in accepted))
print('PREFIX425_REFINED_FAILURE_TESTS',dict(failures))
for key in accepted[0][3]:
    lowest=min(x[3][key].lo for x in accepted)
    print('PREFIX425_STRICT',key,'LOWER_CERTIFICATE',Fr(lowest,d['SC']))
print('PASS_PREFIX425_FULL_ETA_0p002_TO_0p0195_GLOBAL_NEGATIVE_CORNER_PHASE_DOMINANCE')
