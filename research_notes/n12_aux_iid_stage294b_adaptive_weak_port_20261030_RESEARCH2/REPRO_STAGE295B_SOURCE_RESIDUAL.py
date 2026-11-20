#!/usr/bin/env python3
"""Stage295-B partial: exact source-conditioned TV for source-blind adaptive policies.
Action words remain part of the observation. Python 3 standard library only.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

O = {'a':0, 'b':0, 'c':1}
T = {
'L':{'a':{'a':F(1,2),'b':F(1,4),'c':F(1,4)},'b':{'b':F(1,4),'c':F(3,4)},'c':{'c':F(1)}},
'R':{'a':{'b':F(1,4),'c':F(3,4)},'b':{'a':F(1,2),'b':F(1,4),'c':F(1,4)},'c':{'c':F(1)}}
}

def process(source, horizon, policy):
    d={(source,(O[source],),()):F(1)}
    for t in range(horizon):
        nd=defaultdict(F)
        for (s,ow,aw),mass in d.items():
            p=policy(t,ow,aw)
            assert F(0)<=p<=F(1)
            for action,w in (('L',p),('R',1-p)):
                if not w:continue
                for ns,tr in T[action][s].items():
                    nd[(ns,ow+(O[ns],),aw+(action,))]+=mass*w*tr
        d=nd
    result=defaultdict(F)
    for (s,ow,aw),mass in d.items():result[(ow,aw)]+=mass
    assert sum(result.values())==F(1)
    return dict(result)

def tv(p,q):
    return sum(abs(p.get(k,F(0))-q.get(k,F(0))) for k in set(p)|set(q))/2

def average(p,q):
    return {k:(p.get(k,F(0))+q.get(k,F(0)))/2 for k in set(p)|set(q)}

def check(source_blind_policy,horizon):
    pa=process('a',horizon,source_blind_policy)
    pb=process('b',horizon,source_blind_policy)
    pooled=average(pa,pb)
    dist=tv(pa,pb)
    risk=(tv(pa,pooled)+tv(pb,pooled))/2
    expected=F(0) if horizon==0 else F(1,2)
    assert dist==expected,(horizon,dist)
    assert risk==dist/2
    return len(set(pa)|set(pb))

def main():
    tested=0;word_cases=0
    for h in range(8):
        for actions in product('LR',repeat=h):
            policy=lambda t,ow,aw,actions=actions: F(1) if actions[t]=='L' else F(0)
            word_cases+=check(policy,h)
            tested+=1
    policies=[
      lambda t,ow,aw:F(1,2),
      lambda t,ow,aw:F(3,4) if ow[-1]==0 else F(1,4),
      lambda t,ow,aw:F(1) if (t+len(aw)+ow[-1])%2==0 else F(0),
      lambda t,ow,aw:F(2,3) if not aw or aw[-1]=='R' else F(1,3),
    ]
    adaptive=0
    for h in range(8):
        for pol in policies:
            check(pol,h)
            adaptive+=1
    # Counterexample if the first action tag is discarded: fair L/R mixture
    # gives the same first-observation law for sources a and b.
    pa=process('a',1,policies[0]);pb=process('b',1,policies[0])
    def marginal(p):
        d=defaultdict(F)
        for (ow,aw),w in p.items():d[ow]+=w
        return dict(d)
    assert tv(pa,pb)==F(1,2)
    assert tv(marginal(pa),marginal(pb))==F(0)
    assert tested==255 and adaptive==32
    print(f'STAGE295B_SOURCE_RESIDUAL_EXACT_PASS action_words={tested} observation_action_cases={word_cases} adaptive_checks={adaptive}')
    print('H>=1 source_conditional_TV=1/2; optimal_source_blind_risk=1/4; H=0 risk=0')
    print('ACTION_TAG_REMOVAL_COUNTEREXAMPLE: horizon1 fair LR action, pooled_output_TV=0 while tagged_TV=1/2')

if __name__=='__main__':
    main()
