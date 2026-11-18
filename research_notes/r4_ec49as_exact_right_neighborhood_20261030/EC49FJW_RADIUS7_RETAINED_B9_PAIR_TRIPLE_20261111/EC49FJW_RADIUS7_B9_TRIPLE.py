#!/usr/bin/env python3
"""Complete exact triple necessary-condition screen for radius-seven B9 pairscreen survivors."""
import json,collections,itertools,sys,time
from pathlib import Path
from EC49FJW_RADIUS7_B9_PAIR import g, B, bykey, choices_by_label

def antichain_masks(masks):
    xs=sorted(set(masks),key=lambda x:(x.bit_count(),x))
    out=[]
    for s in xs:
        if not any((p&s)==p for p in out):out.append(s)
    return out

def triple_budget_feasible(labs,opts):
    # All list elements are native-prefix bitmasks in one background.
    candidates=[opts[l] for l in labs]
    if any(not x for x in candidates):return False
    candidates.sort(key=len)
    if any(x==0 for x in candidates[0]):
        pass
    states=antichain_masks(candidates[0])
    for choices in candidates[1:]:
        states=antichain_masks((s|m for s in states for m in choices if (s|m).bit_count()<=B))
        if not states:return False
    return True

def check(profile,old):
    rows,ps=g.validate_profile(profile);labels=[(x['window'],x['signature']) for x in rows]
    keys=set(g.raw_key(x['word']) for x in rows)
    sup=collections.defaultdict(int)
    for i,pp in enumerate(ps):
        for p in pp:sup[p]|=1<<i
    saved=collections.defaultdict(list)
    for q,gid in old['unexcluded']:
        mask=sum(1<<i for i in q)
        deleted=tuple(sorted(p for p,s in sup.items() if (s&mask)==s))
        saved[deleted].append((q,gid))
    assert len(saved)==12
    excluded=[];unresolved=[];group_results=[];triple_tests=0
    for gid,(deleted,entries) in enumerate(sorted(saved.items()),1):
        F=set(sup).difference(deleted)
        raw=choices_by_label(F,keys)
        universe={p for sets in raw.values() for s in sets for p in s}
        mapping={p:i for i,p in enumerate(sorted(universe))}
        opts={lab:sorted({sum(1<<mapping[p] for p in s) for s in sets},key=lambda n:n.bit_count()) for lab,sets in raw.items()}
        memo={};cert=0
        for Q,prior_gid in entries:
            found=None
            for ijk in itertools.combinations(Q,3):
                ll=tuple(sorted(labels[i] for i in ijk))
                if ll not in memo:
                    triple_tests+=1
                    memo[ll]=triple_budget_feasible(ll,opts)
                if not memo[ll]:
                    found=ijk;break
            if found:
                cert+=1
                excluded.append({'Q':list(Q),'triple':list(found),'labels':[list(labels[i]) for i in found], 'prior_group':prior_gid})
            else:
                unresolved.append({'Q':list(Q),'prior_group':prior_gid})
        group_results.append({'group':gid,'contexts':len(entries),'triple_excluded':cert,'triple_survived':len(entries)-cert,'distinct_triple_tests':len(memo), 'universe_prefixes':len(universe)})
        print(profile['profile_id'],'triple group',gid,'excl',cert,'survive',len(entries)-cert,'tests',len(memo),flush=True)
    return {'profile':profile['profile_id'],'input_pair_survivors':len(old['unexcluded']),'new_triple_exclusions':len(excluded),'triple_survivors':len(unresolved),'distinct_tests':triple_tests,'groups':group_results,'certificates':excluded,'unresolved':unresolved}

if __name__=='__main__':
    s=time.time();old=json.load(open(Path(__file__).with_name('EC49FJW_B9_PAIR_REPORT.json')))
    res=[check(p,r) for p,r in zip(g.W['profiles'],old['profiles'])]
    out={'schema':'EC49FJW_BRC_R7_B9_TRIPLE_V1','source_pin':g.PIN,'profiles':res,'elapsed_seconds':round(time.time()-s,3)}
    Path(__file__).with_name('EC49FJW_B9_TRIPLE_REPORT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('FINAL',[(r['profile'],r['new_triple_exclusions'],r['triple_survivors']) for r in res])
