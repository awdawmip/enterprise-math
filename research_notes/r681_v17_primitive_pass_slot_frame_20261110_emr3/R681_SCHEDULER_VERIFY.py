#!/usr/bin/env python3
"""R681-B: exact bounded local event schedule, composing sibling R681_VERIFY.py."""
from collections import Counter
import importlib.util
import json

spec=importlib.util.spec_from_file_location('r681_base','R681_VERIFY.py')
R=importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

states=[]
for u0 in R.U0:
    for word in R.WORDS:
        if len(word)==3:
            continue
        u,M=list(R.prefix(u0,word))[-1]
        unused=set(range(3))-set(word)
        d={i:u[R.PASS[i][0]]-u[R.PASS[i][1]] for i in unused}
        w={i:R.W[R.PASS[i][0]]-R.W[R.PASS[i][1]] for i in unused}
        states.append((u0,word,d,w))
assert len(states)==60

metrics=[]
for K in range(1,8):
    tied=bad=0
    for u0,word,d,w in states:
        z={i:K*d[i]+w[i] for i in d}
        top=max(z.values())
        tied+=sum(score==top for score in z.values())!=1
        bad+=sum(d[a]>d[b] and z[a]<=z[b] for a in d for b in d)
    metrics.append({'K':K,'ties_for_best':tied,'strict_pair_order_violations':bad})
assert [v['strict_pair_order_violations'] for v in metrics]==[8,0,0,0,0,0,0]
assert all(v['ties_for_best']==0 for v in metrics)

words={};per={};unsorted=changed=0
for u0 in R.U0:
    u=list(u0);unused=set(range(3));events=[]
    while unused:
        scores={i:2*(u[R.PASS[i][0]]-u[R.PASS[i][1]])+R.W[R.PASS[i][0]]-R.W[R.PASS[i][1]] for i in unused}
        top=max(scores.values())
        winners=[i for i in scores if scores[i]==top]
        assert len(winners)==1
        e=winners[0]
        events.append(e)
        unused.remove(e)
        a,b=R.PASS[e]
        u[a]+=1
        u[b]-=1
    assert tuple(u)==u0
    key=','.join(map(str,u0))
    words[key]=''.join('ABC'[i] for i in events)
    v_unsorted=v_changed=0
    for s in R.TRIADS:
        f=R.frame_at(u0,tuple(events),s)
        v_unsorted+=f!=tuple(sorted(f))
        v_changed+=tuple(sorted(f))!=s
    per[key]={'ordered_frame_not_sorted':v_unsorted,'active_triad_changed':v_changed,'trials':20}
    unsorted+=v_unsorted
    changed+=v_changed
assert list(words.values())==['CBA','BCA','ABC','BCA','CAB','BAC']
assert [x['ordered_frame_not_sorted'] for x in per.values()]==[8,13,11,9,14,9]
assert (unsorted,changed)==(64,120)

out={
  'schema':'R681_BOUNDED_TYPED_PASS_SCHEDULER_EXACT_V1',
  'status':'AUTHOR_SIDE_CONSTRUCTIVE_FINITE_POLICY',
  'model':'R680 six baseline biases, 20 V23 starts, three one-shot PASS labels A/B/C',
  'eligibility':'M_ab=0 for corresponding permitted PASS edge under this explicitly bounded model',
  'score':'G_e=2*(u_source-u_target)+(w_source-w_target), w=(-1,1,-2,-1)',
  'complete_nonterminal_prefixes_checked':len(states),
  'integer_K_comparison':metrics,
  'minimum_K_for_all_strict_primary_pairwise_order':2,
  'generated_event_orders':words,
  'terminal_frame_counts_by_bias':per,
  'tested_complete_trajectories':120,
  'terminal_ordered_frames_not_sorted':unsorted,
  'terminal_unordered_triads_changed':changed,
  'typed_covariance':'Transport port labels and u,w simultaneously; then G_{Pe}(Pu,Pw)=G_e(u,w); unique maximizers transform equivariantly.',
  'scope':'Auxiliary one-shot resource and four-port rule; full X6 autonomous clock, V39 j and independent Driver review remain open.'
}
with open('R681_SCHEDULER_EVIDENCE.json','w',encoding='utf8') as f:
    json.dump(out,f,indent=2,sort_keys=True,ensure_ascii=False)
    f.write('\n')
print(json.dumps({k:out[k] for k in ('complete_nonterminal_prefixes_checked','minimum_K_for_all_strict_primary_pairwise_order','generated_event_orders','terminal_ordered_frames_not_sorted')},ensure_ascii=False,indent=2))
print('R681_BOUNDED_AUTONOMOUS_TYPED_PASS_SCHEDULER_PASS')
