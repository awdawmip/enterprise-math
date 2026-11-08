#!/usr/bin/env python3
"""PREFIX-603-R6: exact native internal-slot tagged repair at singular BRC phase weights.
Run alongside the pinned PREFIX565, PREFIX600, PREFIX601 and PREFIX602 sources.
Only typed original BRC phase edges and the declared incidence reweighting are used.
"""
import hashlib, json
from fractions import Fraction as F
from pathlib import Path
import io
from contextlib import redirect_stdout
with redirect_stdout(io.StringIO()):
    from PREFIX565_positive_marginal_certificate import NEXT, PHASES, PHASE_INDEX, SCIENCE_PIN, ROOTS
    from PREFIX600_R6_compact_native_certificate import W,U,V,J,Wi,plus,minus
    from PREFIX601_R6_weighted_short_certificate import pairs
    from PREFIX602_R6_native_phase_repair_certificate import rank

assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
p=Path(__file__).with_name('PREFIX565_positive_marginal_certificate.py'); b=p.read_bytes()
assert hashlib.sha1(('blob %d\0'%len(b)).encode()+b).hexdigest()=='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41'
assert len(ROOTS)==9 and len(plus)==len(minus)==24
order=plus+minus; position={p:i for i,p in enumerate(order)}
sigma=[position[NEXT[p][0]] for p in order]
assert sorted(sigma)==list(range(48))
E=sorted({(PHASES[p][0],abs(PHASES[p][2])) for p in plus})
ei={e:i for i,e in enumerate(E)}
assert len(E)==12

def weighted_kernel(t):
    s=[];P=[[F(0)]*48 for _ in range(48)];C=[[F(0)]*48 for _ in range(48)]
    for i,p in enumerate(order):
        e=ei[(PHASES[p][0],abs(PHASES[p][2]))]
        mass=1+2*t[e]; assert mass>0
        s.append(mass)
        for slot,q in enumerate(NEXT[p]):
            P[i][position[q]]+=(F(1) if slot==0 else t[e])/mass
        C[i][sigma[i]]=1/mass
    assert all(sum(row)==1 for row in P)
    assert all(sum(row)==1/x for row,x in zip(C,s))
    return P,C,s

def left_null_basis(t,s):
    vw=[[sum(V[e][j]*Wi[j][i] for j in range(24)) for i in range(24)] for e in range(12)]
    L=[]
    for e,f in pairs:
        if 4*t[e]*t[f]!=1:continue
        u=[F(0)]*12;u[e]=F(1);u[f]=-2*t[e]
        w=[-sum(u[h]*t[h]*vw[h][i] for h in range(12)) for i in range(24)]
        for offset in (0,24):
            ell=[F(0)]*48
            for i in range(24):ell[offset+i]=w[i]*s[offset+i]
            assert any(ell)
            L.append(ell)
    return L

def validate_case(t,tag):
    P,C,s=weighted_kernel(t)
    L=left_null_basis(t,s);k=len(L)//2
    assert rank(P)==48-2*k
    assert rank(C)==48
    for i in range(48):
        pi=[F(0)]*48;pi[i]=1
        z=[sum(pi[p]*C[p][q] for p in range(48)) for q in range(48)]
        recovered=[s[p]*z[sigma[p]] for p in range(48)]
        assert recovered==pi
    Fcols=[]
    for ell in L:
        assert [sum(ell[i]*P[i][j] for i in range(48)) for j in range(48)]==[0]*48
        f=[F(0)]*48
        for i in range(48):f[sigma[i]]=s[i]*ell[i]
        assert [sum(C[i][j]*f[j] for j in range(48)) for i in range(48)]==ell
        Fcols.append(f)
    augmented=[P[i]+[sum(C[i][j]*f[j] for j in range(48)) for f in Fcols] for i in range(48)]
    assert rank(augmented)==48
    witness=None
    if L:
        ell=L[0]
        eps=F(1,96*(max(abs(v) for v in ell)+1))
        pi_plus=[F(1,48)+eps*ell[i] for i in range(48)]
        pi_minus=[F(1,48)-eps*ell[i] for i in range(48)]
        assert min(pi_plus)>0 and min(pi_minus)>0
        assert sum(pi_plus)==sum(pi_minus)==1
        assert [sum(pi_plus[i]*P[i][j] for i in range(48)) for j in range(48)]==[sum(pi_minus[i]*P[i][j] for i in range(48)) for j in range(48)]
        assert [sum(pi_plus[i]*C[i][j] for i in range(48)) for j in range(48)]!=[sum(pi_minus[i]*C[i][j] for i in range(48)) for j in range(48)]
        witness={'positive_collision_untagged':True,'separated_by_binary_tag':True,'epsilon':str(eps),'signed_support_size':sum(x!=0 for x in ell)}
    return {'family':tag,'critical_pairs':k,'untagged_rank':rank(P),'tag_internal_rank':rank(C),'minimal_tag_derived_scalar_repairs':2*k,'minimal_augmented_rank':rank(augmented),
      'tag_feature_support_counts':[sum(x!=0 for x in f) for f in Fcols],
      'inverse_is_permutation_and_row_mass':True,'witness':witness}

one=[F(1)]*12
cases=[(one,'original_frozen_all_one'),([F(0)]*12,'all_cross_zero'),
       ([F(i+1,i+3) for i in range(12)],'twelve_distinct_regular')]
for count in (1,2,6):
    t=one.copy()
    for e,f in pairs[:count]:
        t[e]=F(1,2);t[f]=F(1,2)
    cases.append((t,'critical_pairs_'+str(count)))
results=[validate_case(t,tag) for t,tag in cases]
assert [x['critical_pairs'] for x in results]==[0,0,0,1,2,6]
print(json.dumps({'status':'ALL_CHECKS_PASS','pin':SCIENCE_PIN,'native_source_git_blob':'7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41','checked_origins':48,'roots':9,
  'theorem':'Binary native slot-0-origin tag plus terminal phase perfectly reconstructs source phase for every nonnegative t; 2k signed tagged projections are optimal extra linear measurements when k critical pairs',
  'test_cases':results},indent=2))
