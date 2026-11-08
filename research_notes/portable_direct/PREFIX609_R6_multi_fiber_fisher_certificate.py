#!/usr/bin/env python3
"""PREFIX609-R6: exact independent-multipair Fisher information for native BRC."""
import hashlib, io, json
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import sympy as S

BASE=Path(__file__).resolve().parent
source=(BASE/'PREFIX565_positive_marginal_certificate.py').read_bytes()
blob=hashlib.sha1(f'blob {len(source)}\0'.encode()+source).hexdigest()
assert blob=='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41'
with redirect_stdout(io.StringIO()):
    from PREFIX565_positive_marginal_certificate import PHASES,NEXT,SCIENCE_PIN
    import PREFIX605_R6_binary_tag_certificate as prev
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
order,pos,ei,pairs=prev.order,prev.pos,prev.ei,prev.pairs
assert len(order)==48 and len(pairs)==6

h=[]; input_groups=[]; output_groups=[]
for e,f in pairs:
    w=[prev.A(prev.M(prev.NX,{0:F(prev.VW[e][i])}),
              prev.M(prev.H,{0:F(prev.VW[f][i])})) for i in range(24)]
    for block in (0,24):
        vec=[0]*48
        for i,c in enumerate(w):
            if c:
                p=order[block+i]
                vec[block+i]=1 if ei[(PHASES[p][0],abs(PHASES[p][2]))]==e else -1
        assert vec.count(1)==vec.count(-1)==2
        h.append(vec)
        ip={i for i,a in enumerate(vec) if a}
        op={pos[NEXT[order[i]][j]] for i in ip for j in range(3)}
        assert len(ip)==len(op)==4
        input_groups.append(ip); output_groups.append(op)
assert set.union(*input_groups)==set(range(48))
assert set.union(*output_groups)==set(range(48))
assert sum(map(len,input_groups))==sum(map(len,output_groups))==48
for groups in (input_groups,output_groups):
    assert all(not(groups[i]&groups[j]) for i in range(12) for j in range(i+1,12))
for g,ip in enumerate(input_groups):
    for i in ip:
        for j in range(3):
            assert pos[NEXT[order[i]][j]] in output_groups[g]

x=S.symbols('x0:6',positive=True)
t=[None]*12
for z,(e,f) in enumerate(pairs):
    t[e]=x[z];t[f]=1/(4*x[z])
C=[[[S.Integer(0) for _ in range(48)] for _ in range(48)] for _ in range(3)]
for i,p in enumerate(order):
    a=ei[(PHASES[p][0],abs(PHASES[p][2]))]
    for j in range(3):
        q=pos[NEXT[p][j]]
        C[j][i][q]+=(1 if j==0 else t[a])/(1+2*t[a])
P=[[sum(C[j][i][q] for j in range(3)) for q in range(48)] for i in range(48)]
for v in h:
    for q in range(48):
        assert S.cancel(sum(v[i]*P[i][q] for i in range(48) if v[i]))==0

records=[]
for j in range(3):
    a=[S.cancel(sum(C[j][i][q] for i in range(48))/48) for q in range(48)]
    b=[S.cancel(sum(P[i][q]-C[j][i][q] for i in range(48))/48) for q in range(48)]
    d=[[S.cancel(sum(v[i]*C[j][i][q] for i in range(48) if v[i]))
        for q in range(48)] for v in h]
    for l in range(12):
        assert {q for q,val in enumerate(d[l]) if val} <= output_groups[l]
        fisher=S.Integer(0)
        for q in output_groups[l]:
            if d[l][q]!=0:
                assert a[q].is_positive is not False and b[q].is_positive is not False
                fisher+=d[l][q]**2*(1/a[q]+1/b[q])
        fisher=S.cancel(fisher)
        assert fisher==[192,96,96][j],(j,l,fisher)
        records.append({'slot':j,'pair':l//2,'signed_block':l%2,
                        'Fisher_at_uniform':str(fisher),'endpoint_support_size':len(output_groups[l])})
    for l in range(12):
        for m in range(l+1,12):
            assert not ({q for q,v in enumerate(d[l]) if v} &
                        {q for q,v in enumerate(d[m]) if v})
res={'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,'native_git_blob':blob,
     'sympy_version':S.__version__,
     'domain':'any set of k critical incidence pairs; positive weights on all 12 incidences; six independent critical x when all six selected; 48-phase uniform baseline',
     'experimental_observer':'one independent draw of initial phase; one native weighted slot; (terminal_phase, Boolean_slot_j)',
     'directions':'two signed +1,+1,-1,-1 source contrasts per active critical pair',
     'endpoint_partition_sizes':[len(z) for z in output_groups],
     'source_partition_sizes':[len(z) for z in input_groups],
     'symbolic_null_equations':12*48,
     'symbolic_diagonal_fisher_checks':len(records),
     'structural_off_diagonal_pairs_per_tag':12*11//2,
     'all_critical_FIM_diagonal':{'slot0':'192*I_12','slot1':'96*I_12','slot2':'96*I_12'},
     'k_critical_FIM_diagonal':{'slot0':'192*I_(2k)','slot1':'96*I_(2k)','slot2':'96*I_(2k)'},
     'trace_inverse_single_trial':{'slot0':'k/96','slot1':'k/48','slot2':'k/48'},
     'baseline_MSE_for_N_independent_draws':{'slot0':'k/(96*N)','slot1':'k/(48*N)','slot2':'k/(48*N)'},
     'fisher_certificates':records,
     'claim_stage':'AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED'}
(BASE/'PREFIX609_R6_RESULTS.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':res['status'],'null_equations':res['symbolic_null_equations'],
    'fisher_checks':len(records),'FIM':res['all_critical_FIM_diagonal'],
    'sympy_version':S.__version__},indent=2))
