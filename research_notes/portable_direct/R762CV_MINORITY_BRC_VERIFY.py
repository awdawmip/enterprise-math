#!/usr/bin/env python3
"""R762CVb: exact minority-Port two-branch conditional N-BRC verifier."""
import itertools, json
axes=range(6)
triads=tuple(tuple((i,s) for i,s in zip(c,bits))
             for c in itertools.combinations(axes,3)
             for bits in itertools.product((0,1),repeat=3))
perms=tuple(itertools.permutations(axes))
def act(p,t): return tuple(sorted((p[i],s) for i,s in t))
def nneg(t): return sum(s for i,s in t)
def target(t):
    kk=nneg(t)
    assert kk in (1,2)
    rare=1 if kk==1 else 0
    sup=tuple(i for i,s in t)
    return tuple(tuple((i,rare if i==chosen else 1-rare) for i in sup)
                 for chosen in sup if (chosen,rare) not in t)

mixed=[t for t in triads if nneg(t) in (1,2)]
assert len(mixed)==120
edges=0
for t in mixed:
    dest=target(t)
    assert len(dest)==2 and len(set(dest))==2
    assert all(d!=t and nneg(d)==nneg(t) and
               {i for i,_ in d}=={i for i,_ in t} for d in dest)
    assert all(t in target(d) for d in dest)
    for p in perms:
        assert set(target(act(p,t)))==set(act(p,d) for d in dest)
        edges+=1

seen=set();sizes=[]
for t in mixed:
    if t in seen: continue
    todo={t};component=set()
    while todo:
        x=todo.pop()
        if x in component:continue
        component.add(x);todo.update(target(x))
    seen|=component;sizes.append(len(component))
assert len(sizes)==40 and set(sizes)=={3}
maxh=30
for t in mixed:
    count={t:1}
    for h in range(maxh+1):
        assert sum(count.values())==2**h
        diag=(2**h+2*((-1)**h))//3
        off=(2**h-((-1)**h))//3
        assert all(count.get(d,0)==(diag if d==t else off) for d in (t,)+target(t))
        new={}
        for source,num in count.items():
            for dst in target(source):new[dst]=new.get(dst,0)+num
        count=new

out={
 'study':'R762CV_TWO_BRANCH_MINORITY_PORT_BRC',
 'scope':'mixed-sign signed triads, same supports, sign-count preservation, unit positive branches, S6 covariance',
 'total_signed_candidates':160,'mixed_sign_states':120,'components':40,
 'component_sizes':{'3':40},'outdegree':2,'group_size':720,
 'equivariance_checks':edges,'path_formula_checks':len(mixed)*(maxh+1)*3,
 'max_horizon_checked':maxh,'eigenvalues_per_component':[2,-1,-1],
 'minimal_changed_support_preserving_branch_count':2,
 'status':'AUTHOR_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED',
 'native_event_licence':'NOT_EVALUATED','all_checks_passed':True,
}
print(json.dumps(out,indent=2,sort_keys=True))
