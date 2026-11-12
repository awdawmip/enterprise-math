"""PREFIX-725: exact rational edge Bernstein / witness-switch certificate.
Independent polynomial moment toy; frozen Gamma kernel is NOT evaluated.
"""
from fractions import Fraction as F
from math import comb
import json

MU={(0,0):F(1),(1,0):F(1),(0,1):F(1)}
W={(0,0):F(3,4),(1,0):F(1,4),(0,1):F(1,4),(1,1):F(-4)}
S=(F(1,5),F(3,10))
E=((F(0),F(1,2)),(F(0),F(2,5)))
T=(F(0),F(1,4),F(1,2))

def ev(poly,p,z):
    return sum((c*p**i*z**j for (i,j),c in poly.items()),F(0))

def edge(poly,axis,k,lo,hi):
    """Substitute p=k or z=k; the other coordinate is lo+(hi-lo)*s."""
    out={}
    for (i,j),c in poly.items():
        degree=j if axis=='p' else i
        fixed=i if axis=='p' else j
        for h in range(degree+1):
            out[h]=out.get(h,F(0))+c*k**fixed*comb(degree,h)*lo**(degree-h)*(hi-lo)**h
    return out

def bernstein(poly,n):
    return [sum((poly.get(k,F(0))*F(comb(i,k),comb(n,k)) for k in range(i+1)),F(0))
            for i in range(n+1)]

def edge_upper(t):
    candidates=[]
    for axis in ('p','z'):
        for c in S:
            m=edge(MU,axis,c,*S)
            w=edge(W,axis,c,*S)
            n=max(max(m),max(w))
            f={k:w.get(k,F(0))-t*m.get(k,F(0)) for k in range(n+1)}
            candidates.extend(bernstein(f,n))
    return max(candidates)

assert ev(MU,*E[0])==F(3,2) and ev(MU,*E[1])==F(7,5)
assert ev(W,*E[0])==F(7,8) and ev(W,*E[1])==F(17,20)
assert (ev(W,*E[0])-ev(W,*E[1]))/(ev(MU,*E[0])-ev(MU,*E[1]))==F(1,4)
# MU_p=MU_z=1; M2=MU**2+W => J=4*(z-p), K=4>0.
# W is nonnegative on [0,1/2]^2 (bilinear; its minimum at a corner is 0).
rows=[]
for t in T:
    upper=edge_upper(t)
    lower=max(ev(W,*e)-t*ev(MU,*e) for e in E)
    delta=lower-upper
    assert upper==F(69,100)-F(7,5)*t
    assert delta>=F(4,25)
    rows.append({'t':str(t),'edge_bernstein_upper':str(upper),
                 'best_external_witness':str(lower),'strict_gap':str(delta)})
assert min(F(r['strict_gap']) for r in rows)==F(4,25)
for t in T:
    for i in range(21):
        x=S[0]+(S[1]-S[0])*F(i,20)
        for p,z in ((S[0],x),(S[1],x),(x,S[0]),(x,S[1])):
            assert ev(W,p,z)-t*ev(MU,p,z)<=edge_upper(t)
result={'schema':'PREFIX725_R6_EDGE_BERNSTEIN_SWITCH_V1',
 'date':'2026-11-12','prior':'PREFIX-724-R6',
 'frozen_gamma_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'scientific_model':'independent polynomial moment toy; not frozen Gamma computation',
 'mu':'1+p+z','W':'3/4+(p+z)/4-4*p*z','J':'4*(z-p)','K':'4',
 'candidate_patch':'[1/5,3/10]^2','parameter_t':'[0,1/2]',
 'witnesses':[['0','1/2'],['0','2/5']], 'checks':rows,
 'verified_continuous_t_gap':'4/25',
 'witness_continuous_q_advantage':'for every real q>=2, max_e V_q(e)-max_patch V_q >= 4*q^2/25',
 'gamma_method_conditional':'If the frozen Gamma patch certifies mu_p>0, mu_z>0 and K>0, mean-fiber boundary reduction and exact 1D-edge Bernstein plus witness-switch nodes apply.',
 'frozen_189_row_edge_degree_cap':'mu,M2 <=188; W<=376; four degree-376 edge arrays have 1508 coefficients, while degree-376 tensor has 142129',
 'status':'EXACT_FRACTION_TOY_CHECKED / GAMMA_METHOD_CONDITIONAL / UNREVIEWED / NOT_ADMITTED'}
if __name__=='__main__':
    with open('/mnt/data/PREFIX725_R6_RESULTS.json','w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print('ALL_CHECKS_PASS PREFIX725-R6')
    print(rows)
