"""Exact finite checks for C53; run from the package directory."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product,combinations
from collections import defaultdict
from pathlib import Path
import json,time,sys
import sympy as sp
import history_memory as h

ROOT=Path(__file__).resolve().parent
stats=defaultdict(int)
t0=time.time()

# Symbolic identity verification uses full product laws, not the inverse formulas.
x,y,z,theta=sp.symbols('x y z theta',positive=True)
def symprob(w):
    left=[w.count(i) for i in range(4)];last=0;ans=sp.Integer(1)
    for p in w:
        rr=(x,y,z*theta**last,sp.Integer(1))
        ans*=rr[p]*left[p]/sum(rr[j]*left[j] for j in range(4))
        left[p]-=1
        if p==0:last=1
        elif p==1:last=-1
    return sp.factor(ans)
ps={w:symprob(w) for w in h.CALIBRATION_WORDS}
a=z*theta;b=z/theta
identities=[(ps[h.W0]/ps[h.W7],a),(ps[h.W30]/ps[h.W37],b),
(ps[h.W0]/ps[h.W2],x*(x+1)*a/(b*(a+1))),
(ps[h.W30]/ps[h.W3],y*(y+1)*b/(a*(b+1))),
(ps[h.W0]/ps[h.WP],a*(b+1)*(a+y+1)/(b*(a+1)*(x+b+1))),
(ps[h.W0]/ps[h.WM],(2*x+y+b+1)*(x+y+a+1)/((x+y+b+1)*(x+2*y+a+1)))]
for left,right in identities:
    assert sp.factor(left-right)==0
    stats['symbolic_identities']+=1

# 32 preparation configurations, each with 10 terminal configurations.
for xx,yy,zz,tt in product((F(1),F(2)),(F(1,2),F(3)),(F(1),F(3)),(F(1,2),F(1),F(2),F(3))):
    rates=(xx,yy,zz,F(1));base=h.reference(rates,tt)
    assert sum(base.values())==1
    hist=defaultdict(F)
    for w,p in base.items():hist[h.raw_scores(w)]+=p
    assert h.memory_histogram(h.COUNTS,rates,tt)==dict(hist)
    stats['memory_dp_comparisons']+=1
    stats['reference_word_evaluations']+=len(base)
    for q,gamma in product((F(1,2),F(2,3)),(F(-1),F(0),F(1,2),F(1),F(2))):
        Q,calls=h.terminal_selected(base,q,gamma,use_brc=(q==F(1,2) and gamma==F(1,2)))
        stats['brc_serial_and_recoalesce_calls']+=calls
        data={w:Q[w] for w in h.CALIBRATION_WORDS}
        got=h.infer(data)
        assert got['rates']==rates and got['theta']==tt
        assert got['u']==q**int(4+4*gamma)
        assert got['v']==q**int(4-4*gamma)
        assert got['u']*got['v']==q**8
        assert h.cross_ratio(data)==tt**2
        predicted=h.predict_all(got['rates'],got['theta'],got['u'],got['v'])
        assert predicted==Q
        stats['six_parameter_calibrations']+=1
        stats['held_out_word_probabilities']+=len(Q)-len(data)
        stats['cross_ratio_identities']+=1
    # Preparation neutral design continues to hold for nonquadratic even laws.
    for weight in [lambda A,B:F(1,1+(A+F(1,2)*B)**2),
                   lambda A,B:F(1,1+(A+F(1,2)*B)**4),
                   lambda A,B:1+(A+F(1,2)*B)**2]:
        Q=h.old.selected_general(base,weight)
        prep=h.recover_preparation(Q)
        assert prep['rates']==rates and prep['theta']==tt
        stats['even_weight_preparation_recoveries']+=1
    # No parity assumption is needed for the four-path contrast.
    for weight in [lambda A,B:F(2)**(A+3*B),
                   lambda A,B:F(3+A*A+2*(B+1)),
                   lambda A,B:F(1,2+(A-2*B)**2)]:
        Q=h.old.selected_general(base,weight)
        assert h.cross_ratio(Q)==tt**2
        stats['arbitrary_score_weight_cross_ratios']+=1

# A varying-by-counts reference: the stronger no-history null still has C=1.
for scale in range(1,13):
    def countprob(w):
        used=[0]*4;left=[w.count(i) for i in range(4)];ans=F(1)
        for p in w:
            rates=[F((i+1)*(scale+1)+(i+2)*sum((j+1)*used[j] for j in range(4)),scale+1) for i in range(4)]
            ans*=rates[p]*left[p]/sum(rates[j]*left[j] for j in range(4))
            left[p]-=1;used[p]+=1
        return ans
    base={w:countprob(w) for w in h.ALL_WORDS}
    assert sum(base.values())==1
    for wt in [lambda A,B:F(2)**(A+B),lambda A,B:F(1,1+A*A+B*B)]:
        Q=h.old.selected_general(base,wt)
        assert h.cross_ratio(Q)==1
        stats['count_dependent_null_checks']+=1

# Representative finite example and all prefix conditionals.
rates=tuple(map(F,(1,2,3,1)));tt=F(2);q=gamma=F(1,2)
base=h.reference(rates,tt);Q,_=h.terminal_selected(base,q,gamma)
nextprob,kernel=h.completion_kernel(rates,tt,q,gamma)
prefixes={w[:i] for w in h.ALL_WORDS for i in range(len(w))}
for prefix in sorted(prefixes):
    assert nextprob(prefix)==h.old.conditional_next(Q,prefix)
    stats['h_transform_prefix_checks']+=1
v=h.word('2332');u=h.word('3223')
assert h.prefix_state(v)[:3]==h.prefix_state(u)[:3]
assert h.prefix_state(v)[3]!=h.prefix_state(u)[3]
assert nextprob(v)[2]==F(6,7) and nextprob(u)[2]==F(3,5)

# Cross-ratio errors and full six-parameter interval calculation.
errors={}
for eps in (F(1,100),F(1,1000)):
    inp={w:(Q[w]*(1-eps),Q[w]*(1+eps)) for w in h.CALIBRATION_WORDS}
    box=h.inverse_box(inp)
    for key,actual in zip(('x','y','z','theta','q','gamma'),(F(1),F(2),F(3),F(2),F(1,2),F(1,2))):
        assert box[key][0]<=actual<=box[key][1]
        stats['interval_truth_containments']+=1
    odds=F(4);factor=(1-eps)/(1+eps)
    cb=(odds*factor**2,odds/factor**2)
    assert cb[0]>1
    errors[str(eps)]={'six_parameter_bounds':box,'cross_ratio_bounds':cb,
                     'theta_from_four_only':(2*factor,2/factor)}

example={'inputs':{h.text(w):Q[w] for w in h.CALIBRATION_WORDS},
         'reference_prefix_mass':{h.text(p):sum(x for w,x in base.items() if w[:len(p)]==p) for p in (v,u)},
         'selected_next_5':{'2332':nextprob(v)[2],'3223':nextprob(u)[2]},
         'cross_ratio':h.cross_ratio(Q),'input_error_bounds':errors}

# Weighted DP also works before a visible occurrence and on smaller initial numbers.
for counts in [(0,0,0,0),(1,0,0,0),(0,1,0,0),(2,0,0,0),(0,0,1,0)]:
    br=h.reference(rates,tt,counts)
    assert len(br)==1 and sum(br.values())==1
    assert sum(h.memory_histogram(counts,rates,tt).values())==1
    stats['initial_1_to_5_checks']+=1

# Additional small populations, direct word counts vs the state-matched DP.
for counts in product(range(3),range(3),range(2),range(2)):
    br=h.reference(rates,tt,counts);mass=defaultdict(F)
    for w,p in br.items():mass[h.scores_for_counts(w)]+=p
    assert dict(mass)==h.memory_histogram(counts,rates,tt)
    stats['other_population_dp_checks']+=1
    stats['other_population_word_evaluations']+=len(br)

# Minimal collision in binary factor words: one occurrence of one type gives
# a unique inversion count. First collision occurs for (2,2), length four.
collisions=[]
for length in range(1,6):
    for aa in range(length+1):
        bb=length-aa;groups=defaultdict(list)
        for w in h.words((aa,bb,0,0)):
            inv=sum(p==0 and r==1 for i,p in enumerate(w) for r in w[i+1:])
            groups[inv].append(h.text(w))
        for inv,group in groups.items():
            if len(group)>1:collisions.append((length,aa,bb,inv,group))
        stats['binary_collision_populations']+=1
assert min(x[0] for x in collisions)==4

out={'status':'ALL_ASSERTIONS_PASSED','counts':dict(stats),'example':example,
     'first_binary_collisions':[x for x in collisions if x[0]==4],
     'elapsed_seconds':time.time()-t0}
(ROOT/'results'/'exact_checks.json').write_text(json.dumps(h.serialise(out),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(stats),indent=2))
print('EXAMPLE INPUTS',[(h.text(w),float(Q[w])) for w in h.CALIBRATION_WORDS])
for e,obj in errors.items():
    print('ERROR',e)
    for key in ('x','y','z','theta','q','gamma'):
        print(key,[float(t) for t in obj['six_parameter_bounds'][key]])
print('Elapsed',time.time()-t0)
