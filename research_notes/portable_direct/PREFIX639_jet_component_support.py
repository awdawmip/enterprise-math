#!/usr/bin/env python3
"""PREFIX639: typed original BRC+AC six-jet Boolean component support compiler.
Uses exact source implementation from preceding PREFIX638; no replacement of native actions.
"""
import json,sys,time
from fractions import Fraction as Q
from collections import Counter
from pathlib import Path
# Import the exactly pinned native checker when locally expanded, otherwise
# decode the byte-identical frozen SOURCE dependency shipped alongside this file.
import importlib.util, types, gzip, base64, hashlib
HERE=Path(__file__).resolve().parent
PINNED_KERNEL_SHA256="48d6521bab630f7f2d9de8ac7158ff074ff448267c1893a0dd064e4335c264f1"
local=HERE/"PREFIX638_native_jet_support.py"
encoded=HERE/"PREFIX639_PINNED_PREFIX638_native_jet_support.py.gz.b64"
if local.exists():
    source=local.read_bytes()
else:
    source=gzip.decompress(base64.b64decode(encoded.read_bytes()))
assert hashlib.sha256(source).hexdigest()==PINNED_KERNEL_SHA256, 'frozen native checker changed'
core=types.ModuleType('PREFIX638_native_jet_support')
core.__file__=str(local)
exec(compile(source,str(local),'exec'),core.__dict__)


Z,U,V,UU,UV,VV=(1,2,4,8,16,32)

def mm(a,b):
    out=0
    if a&Z and b&Z:out|=Z
    if (a&U and b&Z) or (a&Z and b&U):out|=U
    if (a&V and b&Z) or (a&Z and b&V):out|=V
    if (a&UU and b&Z) or (a&U and b&U) or (a&Z and b&UU):out|=UU
    if (a&UV and b&Z) or (a&U and b&V) or (a&V and b&U) or (a&Z and b&UV):out|=UV
    if (a&VV and b&Z) or (a&V and b&V) or (a&Z and b&VV):out|=VV
    return out
MUL=[[mm(a,b) for b in range(64)] for a in range(64)]

def step_mask():
    M={}
    for s in range(96):
        for q in range(core.S):
            row={}
            for aid,d,w,gated in core.BY[s]:
                wt=1 if gated else w
                if not wt:continue
                q2,h=core.TRANS[q][aid]
                mask=Z
                if h&1:mask|=U|UU
                if h&2:mask|=V|VV
                if h==3:mask|=UV
                dest=d*core.S+q2
                row[dest]=row.get(dest,0)|mask
            if row:M[s*core.S+q]=row
    return M

def matmul(A,B):
    C={}
    for s,row in A.items():
        dest={}
        for mid,a in row.items():
            for j,b in B.get(mid,{}).items():
                dest[j]=dest.get(j,0)|MUL[a][b]
        if dest:C[s]=dest
    return C

def coverage(M):
    return {'all_positions':sum(map(len,M.values())), 'mask_hist':dict(sorted(Counter(x for row in M.values() for x in row.values()).items())),
      'coefficient_positions':{str(i):sum(bool(mask & (1<<i)) for row in M.values() for mask in row.values()) for i in range(6)},
      'components_total':sum(mask.bit_count() for row in M.values() for mask in row.values()),
      'all_six_positions':sum(mask==63 for row in M.values() for mask in row.values())}

def run():
    A=step_mask();B={s:set(v) for s,v in A.items()}; assert B==core.support(core.Q(1))
    P={1:A}; table=[]; start=time.monotonic()
    for k in range(1,25):
        if k>1:P[k]=matmul(P[k-1],A)
        table.append({'k':k,**coverage(P[k])})
        print('k',k,'size',table[-1]['all_positions'],'coeff',list(table[-1]['coefficient_positions'].values()),'seconds',round(time.monotonic()-start,2), flush=True)
        if k>=5 and P[k]==P[k-4]:
            print('FOUND_PERIOD4_START',k-4)
            break
    # Distinguish the exact first k with 4-periodic mask support.
    smaller_periods={str(j): P[j]==P[j+4] for j in range(1,k-4)}
    assert all(not v for v in smaller_periods.values()), smaller_periods
    assert P[10]==P[14] and P[9]!=P[13]
    # The positive-gate certificate is a sharp universal upper bound for nonnegative gates.
    assert max(x['components_total'] for x in table)==10584
    assert max(int(x['coefficient_positions'][str(i)]) for x in table for i in range(1,6))==1260
    assert coverage(P[10])['mask_hist']=={1:3024,63:1260}
    assert coverage(P[11])['mask_hist']=={1:2128,63:1260}
    assert all(not (mask & U) or (mask & V) for m in P.values() for row in m.values() for mask in row.values())
    prev=P[k]; prov=[]
    for i in range(max(5,k-4),k+1):
        if i+4 in P: prov.append([i,P[i]==P[i+4]])
    # identity holds for all later powers if P[k] = P[k-4] proved finite
    M=core.jet_step(core.Q(1))
    for len_ in (1,2,3,4,5,6):
        assert {s:{d:sum((1<<i) for i,v in enumerate(z) if v) for d,z in row.items()} for s,row in M.items()}==P[len_]
        if len_<6:M=core.jet_product(M,core.jet_step(core.Q(1)))
    # Independently compare mask semiring to the six exact Fraction moments
    # over the actual enumerated original actions, including zero gates.
    numeric_checks=[]
    for name,gates in (
        ('positive',[Q(1),Q(3,2),Q(2,3),Q(5,4),Q(7,2),Q(4,5),Q(1,1)]),
        ('zero_gates',[Q(0),Q(3,2),Q(0),Q(5,4),Q(7,2),Q(0),Q(1,1)]),
        ('all_zero',[Q(0)]*7),
        ):
        M=None
        for j,g in enumerate(gates,1):
            M=core.jet_step(g) if M is None else core.jet_product(M,core.jet_step(g))
            masks={s:{d:sum((1<<idx) for idx,val in enumerate(z) if val) for d,z in row.items()} for s,row in M.items()}
            assert all((mask & P[j].get(s,{}).get(d,0))==mask for s,row in masks.items() for d,mask in row.items())
            if name=='positive': assert masks==P[j]
            assert all((mask & 1)!=0 for row in masks.values() for mask in row.values())
            numeric_checks.append({'class':name,'k':j,'entries':sum(map(len,masks.values()))})
    assert len(numeric_checks)==21
    out={'schema' :'PREFIX639_BRC_JET_COMPONENT_SUPPORT_CERTIFICATE_V1','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'PREF638_code':'original-native positive-gate 48/96/576 AC 7 states','computed_table':table,'first_period_4_certificate':(k-4 if k>=5 and P[k]==P[k-4] else None),
         'earlier_four_period_equalities':smaller_periods,
         'sharp_uniform_component_field_upper_bound':10584,
         'sharp_max_nonzero_coefficient_positions_each_higher_moment':1260,
         'fraction_vs_mask_crosschecks':numeric_checks,
         'checked_fraction_powers':6,'status':'ALL_ASSERTIONS_PASS','role':'AUTHOR_UNREVIEWED'}
    target=Path(__file__).with_name('PREFIX639_jet_component_support_results.json');target.write_text(json.dumps(out,indent=2)+'\n');print('SAVED',str(target))
if __name__=='__main__':run()
