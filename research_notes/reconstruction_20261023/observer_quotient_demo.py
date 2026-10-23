"""Reuse canonical T6 and check why same-observation nondeterminism needs care."""
import json

from enterprise_math.operation_quotient import (
    family_future_partition_sequence, family_descends, word_observation_signature)
from enterprise_math.predictive_quotient import finite_horizon_partition


def main():
    states=tuple(range(4))
    actions={'step':{0:1,1:2,2:3,3:3}}
    observation={0:0,1:0,2:0,3:1}
    stages=family_future_partition_sequence(states,actions,observation)
    assert len(stages)==3 and [len(set(p.values())) for p in stages]==[2,3,4]
    assert not family_descends(states,actions,stages[1])
    assert family_descends(states,actions,stages[-1])
    for h,p in enumerate(stages):
        for x in states:
            for y in states:
                assert (p[x]==p[y]) == (word_observation_signature(x,actions,observation,h)
                                        == word_observation_signature(y,actions,observation,h))
    # Also use the callable API, instead of rebuilding the canonical quotient.
    assert finite_horizon_partition(states,{'step':lambda x:actions['step'][x]},
                                    observation.__getitem__,1)[0:2]==(0,0)

    alphabet=('a','b','c')
    pub={'p':0,'q':0,'u':1,'v':1,'w':1,'end':2}
    moves={'p':{'a':('SAFE',('u','v'))},'q':{'a':('SAFE',('u','v','w'))},
           'u':{'b':('SAFE',('end',)),'c':('UNSAFE',())},
           'v':{'b':('UNSAFE',()),'c':('SAFE',('end',))},
           'w':{'b':('SAFE',('end',)),'c':('SAFE',('end',))},'end':{}}

    def traces(state,h):
        result={(pub[state],)}
        if not h:return result
        for action in alphabet:
            tag,successors=moves[state].get(action,('ILLEGAL',()))
            if tag!='SAFE':result.add((pub[state],(action,tag)))
            for target in successors:
                for suffix in traces(target,h-1):
                    result.add((pub[state],(action,tag,'same-public-o'))+suffix)
        return result

    def signature(state,h):
        if not h:return (pub[state],)
        parts=[]
        for action in alphabet:
            tag,successors=moves[state].get(action,('ILLEGAL',()))
            parts.append((action,tag,frozenset(('same-public-o',signature(t,h-1))
                                               for t in successors)))
        return (pub[state],tuple(parts))

    for horizon in range(5):
        assert traces('p',horizon)==traces('q',horizon)
    assert signature('p',2)!=signature('q',2)
    print(json.dumps({'canonical_T6_profile':[2,3,4],
       'finite_horizon_one_partition_is_not_action_closed':True,
       'same_public_observation_nondeterministic_trace_counterexample':{
           'equal_complete_prefix_trace_sets_through_depth':4,
           'successor_signature_separates_at_depth':2,
           'required_repair':'one belief successor per action/observation, or state the stronger bisimulation claim'},
       'tool_reuse':'REUSE_EXECUTED: operation_quotient and predictive_quotient'},indent=2))


if __name__=='__main__':
    main()
