from fractions import Fraction
from itertools import product
from collections import Counter,defaultdict
import json,hashlib,sys
MATS={
'S4':[
[[[-5,2],[0,0],[2,0]],[[-4,1],[4,0],[-2,1]],[[-1,0],[0,-4],[-1,-6]]],
[[[-5,-2],[0,0],[2,0]],[[-4,-1],[4,0],[-2,-1]],[[-1,0],[0,4],[-1,6]]],
[[[-5,-2],[0,0],[2,0]],[[-3,2],[4,0],[1,4]],[[-2,1],[0,-4],[-4,-3]]],
[[[-5,2],[0,0],[2,0]],[[-3,-2],[4,0],[1,-4]],[[-2,-1],[0,4],[-4,3]]],
[[[-5,-2],[0,0],[2,0]],[[-3,1],[0,0],[-5,3]],[[-2,-2],[4,4],[2,2]]],
[[[-5,2],[0,0],[2,0]],[[-3,-1],[0,0],[-5,-3]],[[-2,-2],[4,4],[2,2]]]],
'S7':[
[[[-6,1],[4,0],[0,1]],[[-2,0],[0,0],[5,-2]],[[-2,1],[-4,0],[-4,1]]],
[[[-6,-1],[4,0],[0,-1]],[[-2,-1],[-4,0],[-4,-1]],[[-2,0],[0,0],[5,2]]],
[[[-5,3],[0,0],[-3,1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,2]]],
[[[-5,-3],[0,0],[-3,-1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,-2]]],
[[[-4,-3],[0,4],[-2,1]],[[-4,1],[0,-4],[-2,-3]],[[-2,0],[0,0],[5,2]]],
[[[-4,-1],[0,4],[-2,3]],[[-4,3],[0,-4],[-2,-1]],[[-2,0],[0,0],[5,-2]]]]}

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def norm(a):return a[0]*a[0]+a[1]*a[1]
def g(a):return str(a.numerator) if a.denominator==1 else f'{a.numerator}/{a.denominator}'
Z=(0,0);ONE=(1,0);Q=[(1,0),(0,1),(-1,0),(0,-1)];W=[(0,0),(2,0),(-2,0),(0,2),(0,-2),(2,2),(-2,-2)]
# Verify all immutable 12 matrices’ Gram via 16H-S
H=[[3,-1,0],[-1,2,1],[0,1,3]]
count=0
for k, mats in MATS.items():
 S=[1,0,2] if k=='S4' else [2,0,1]
 for M in mats:
  for x in range(3):
   for y in range(3):
    lhs=Z
    for row in M:lhs=add(lhs,mul(conj(row[x]),row[y]))
    assert lhs==(16*H[x][y]-(S[x] if x==y else 0),0),(k,x,y,lhs)
    count+=1
assert count==108


# PREVIOUS RESOURCE: adversarial/unspecified row unit (for regression only).
# NEW RESOURCE: experimenter may choose one C4 row unit for the selected retained Port.
rows=[]; hist_prior=Counter(); hist_controlled=Counter(); evaluations=0
for kind,mats in MATS.items():
 for ix,M in enumerate(mats,1):
  for iq,q in enumerate(Q):
   per=[]
   for ir,row in enumerate(M,1):
    pr=[]
    for iu,u in enumerate(Q):
     m0,m1,m2=[mul(x,u) for x in row]
     T=add(sub(m1,m0),m2)
     assert norm(T)>0, (kind,ix,iq,ir,iu)
     bestnum=-1; corner=None
     for wE,wC,wR in product(W,repeat=3):
      evaluations+=1
      N=sub(sub(mul((4,0),wR),mul(m0,wE)),mul(m2,mul(q,wC)))
      numerator=norm(sub(mul(T,wE),N))+norm(N)+norm(add(mul(T,mul(q,wC)),N))
      if numerator>bestnum:
       bestnum=numerator;corner=[wE,wC,wR]
     pr.append({'value':Fraction(bestnum,norm(T)), 'witness_corner':corner,
                'numerator':bestnum,'denominator':norm(T), 'T':T})
    per.append(pr)
   prior=min(max(p['value'] for p in row) for row in per)
   controlled=min(p['value'] for row in per for p in row)
   winners=[(ir,iu) for ir in range(3) for iu in range(4) if per[ir][iu]['value']==controlled]
   ir,iu=winners[0]
   hist_prior[g(prior)]+=1;hist_controlled[g(controlled)]+=1
   rows.append({'kind':kind,'representative_1_based':ix,'q_phase_index':iq,
    'prior_unspecified_phase_squared_gain':g(prior),
    'controlled_phase_squared_gain':g(controlled),
    'chosen_port_1_based':ir+1,'chosen_u_phase_index':iu,
    'per_port_four_phase_gains':[[g(z['value']) for z in row] for row in per],
    'corner_numerator':per[ir][iu]['numerator'],'corner_denominator':per[ir][iu]['denominator'],
    'corner_wE_wC_wR':per[ir][iu]['witness_corner'],
    'T':per[ir][iu]['T']})
assert evaluations==12*4*3*4*7**3
assert hist_prior==Counter({'40':16,'771/25':8,'1880/53':8,'19':8,'16':8}),hist_prior
assert hist_controlled==Counter({'1532/53':16,'176/5':8,'1928/53':8,'19':8,'16':8}),hist_controlled
assert sum(Fraction(r['controlled_phase_squared_gain'])<Fraction(r['prior_unspecified_phase_squared_gain']) for r in rows)==32
assert max(Fraction(r['controlled_phase_squared_gain']) for r in rows)==Fraction(1928,53)
sharp=next(r for r in rows if (r['kind'],r['representative_1_based'],r['q_phase_index'])==('S4',3,0))
assert (sharp['chosen_port_1_based'],sharp['chosen_u_phase_index'])==(1,1)
assert sharp['T']==(-2,7) and sharp['corner_numerator']==1928 and sharp['corner_denominator']==53
assert sharp['corner_wE_wC_wR']==[(2,2),(2,2),(-2,-2)]

# SOURCE-TAGGED BRC evaluation, all ordered source pairs; no amplitude-only stand-in.
# Scale amplitudes by 8: each bin's exact mass is /64.
carrier=[(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1)]
checks={'labelled_instrument_inputs':0,'direct_BRC_mass_readouts':0,
        'ordered_source_path_pairs':0,'reference_interference_identities':0}
def brc_mass(paths):
 total=Z
 for label_a,amp_a in paths:
  for label_b,amp_b in paths:
   total=add(total,mul(amp_a,conj(amp_b)))
   checks['ordered_source_path_pairs']+=1
 assert total[1]==0 and total[0]>=0
 summ=Z
 for _,amp in paths:summ=add(summ,amp)
 assert total==(norm(summ),0), ('BRC ordered-source identity',paths,total,summ)
 checks['direct_BRC_mass_readouts']+=1
 return total[0]
for kind,mats in MATS.items():
 for ix,M in enumerate(mats,1):
  for iq,q in enumerate(Q):
   result=next(r for r in rows if r['kind']==kind and r['representative_1_based']==ix and r['q_phase_index']==iq)
   rotated_index=result['chosen_port_1_based']-1
   chosen_u=Q[result['chosen_u_phase_index']]
   q2=mul(q,q);qinverse=conj(q)
   for a in product(carrier,repeat=3):
    b=[a[0],mul(q,a[1]),mul(q2,a[2])]
    eventE=[('src0',mul((4,0),b[0])),('src1',mul((4,0),b[1]))]
    eventC=[('src1',neg(mul((4,0),mul(qinverse,b[1])))),
            ('src2',mul((4,0),mul(qinverse,b[2])))]
    kept=[]
    for j,row in enumerate(M):
     unit=chosen_u if j==rotated_index else ONE
     kept.append([('src'+str(l),mul(mul(unit,row[l]),b[l])) for l in range(3)])
    for paths in [eventE,eventC]+kept:
     q0=brc_mass(paths)
     q1=brc_mass(paths+[('ref:+1',(8,0))])
     qi=brc_mass(paths+[('ref:+i',(0,8))])
     sum_amp=Z
     for _,v in paths:sum_amp=add(sum_amp,v)
     assert q1-q0-64==16*sum_amp[0]
     assert qi-q0-64==16*sum_amp[1]
     checks['reference_interference_identities']+=2
    checks['labelled_instrument_inputs']+=1
assert checks=={
 'labelled_instrument_inputs':10368,
 'direct_BRC_mass_readouts':155520,
 'ordered_source_path_pairs':1731456,
 'reference_interference_identities':103680}, checks

output={
 'schema':'EM_PREFIX307_CONTROLLED_C4_PHASE_SHARP_STABILITY_V1',
 'date':'2026-10-28',
 'global_knowledge_snapshot':'09f6bcbb89e7d7a3599ca5b9426db94d9c423068',
 'enterprise_math_input_snapshot':'ad1150668851f01074b1df93576a9712377e7b2d',
 'input_matrix_git_blob':'b6acffe158f014469235f5428d2889ff43b62810',
 'prior_checkpoint':'d69d13f84e26004821ff24936d750088065c4975',
 'model':'Auxiliary Q(i)^3 BRC; 5 free base masses E,C,R1..R3; six reference masses E,C,one retained R with 1 and i; 9 mass errors individually bounded by eps; known q,M and experimenter-selectable C4 phase of selected retained R.',
 'phase_index_order':['1','i','-1','-i'],
 'analytical_coverage':'All Q(i)^3, because inversion error is linear in 9 mass errors; convex-square norm max attained among 7^3 exact Gaussian corners.',
 'gram_exact_entries':count,
 'corner_numerator_evaluations':evaluations,
 'configurations':len(rows),
 'prior_unspecified_phase_optimum_squared_gain':'40',
 'controlled_phase_optimum_squared_gain':'1928/53',
 'controlled_amplitude_gain':'sqrt(1928/53)*epsilon',
 'configuration_gain_histogram':dict(sorted(hist_controlled.items())),
 'prior_gain_histogram':dict(sorted(hist_prior.items())),
 'improved_configurations':32,
 'sharp_witness':sharp,
 'source_tagged_BRC_check':checks,
 'rows':rows,
 'status':'AUTHOR_SIDE_EXACT_FINITE_OPTIMIZATION_CERTIFICATE_UNREVIEWED_NOT_ADMITTED',
 'next':'PREFIX-308: optimize full five-Port plus six/eight/ten references; test full Q(i)^3 adaptive depth <=5; verify native C4 reference gate implementability and calibrated phase costs.'
}
raw=json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
if len(sys.argv)>1 and sys.argv[1]=='--digest':
 print(hashlib.sha256(raw.encode()).hexdigest())
else:
 sys.stdout.write(raw)
