#!/usr/bin/env python3
"""Single, nonresetting five-place trace. Optional local source verification."""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import ceil, comb, floor
from pathlib import Path
import re
from zipfile import ZipFile

# Anonymous example for the 3+2 theorem: three first ports, two second ports.
ROUTES = ((1,0,2,4,3), (0,2,1,3,4))
Y = (0,2,3)
Z = (1,2,4)
SOURCE = '1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d'


def permute(v, route):
    return tuple(v[i] for i in route)


def total(v, positions):
    return sum(v[i] for i in positions)


def path(r, word, routes=ROUTES):
    yield r
    for g in word:
        r = permute(r, routes[int(g)])
        yield r


def observations(x, h, word, routes=ROUTES, y=Y, z=Z):
    return tuple((total(a,y), total(a,z), total(b,y))
                 for a,b in zip(path(x,word,routes),path(h,word,routes)))


def masks(word):
    return tuple(tuple(sorted(t[i] for i in Y)) for t in path(tuple(range(5)),word))


def det(M):
    if not M:
        return 1
    return sum((-1)**i * v * det([r[:i]+r[i+1:] for r in M[1:]])
               for i,v in enumerate(M[0]) if v)


def row(indices):
    return tuple(int(i in indices) for i in range(5))


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for i in range(n+1):
        for rest in compositions(n-i,k-1):
            yield (i,*rest)


def from_x_coordinates(mu, y0,z0,y1,y3):
    return (y1+y3-mu, y1+z0-mu, y0+z0-mu,
            2*mu-z0-y1-y3, 2*mu-y0-z0-y1)


def from_h_coordinates(S, k0,k1,k2,k3):
    return (k1+k3-S, k1+k2-S, k0+k2-S, 2*S-k1-k2-k3, 2*S-k0-k1-k2)


def feasible(mu,S,boxes):
    # Four triples (ordinary y, ordinary z, tagged k); mu,S exact. Inclusive endpoints.
    def integers(t,j):
        lo,hi=boxes[t][j]
        return range(max(0,ceil(lo)),min(mu,floor(hi))+1)
    xs = set()
    for vals in product(integers(0,0), integers(0,1), integers(1,0), integers(3,0)):
        x = from_x_coordinates(mu,*vals)
        if min(x)>=0:
            xs.add(x)
    hs = set()
    for counts in product(*(integers(t,2) for t in range(4))):
        h = from_h_coordinates(S,*counts)
        if min(h)>=0:
            hs.add(h)
    ans = set()
    for x,h in product(xs,hs):
        if any(b>a for a,b in zip(x,h)):
            continue
        rec = observations(x,h,'101')
        if all(l <= a <= u for line,box in zip(rec,boxes) for a,(l,u) in zip(line,box)):
            ans.add((x,h))
    return ans


def graph_and_words():
    orbit = {tuple(range(5))}
    while True:
        more = orbit | {permute(t,g) for t in orbit for g in ROUTES}
        if more==orbit:
            break
        orbit=more
    forms = sorted({tuple(sorted(t[i] for i in Y)) for t in orbit})
    assert len(orbit)==12 and len(forms)==6
    tree_rows = {tuple(inds):det([(1,)*5]+[row(forms[i]) for i in inds])
                 for inds in combinations(range(6),4)}
    assert Counter(abs(v) for v in tree_rows.values())=={0:3,1:12}
    levels = []
    words3={}
    for n in range(8):
        all_edges,full_rank = [],[]
        for word in map(''.join,product('01',repeat=n)):
            edges=masks(word)
            ids = sorted({forms.index(e) for e in edges})
            if len(ids)==6:
                all_edges.append(word)
            if any(tree_rows[tuple(t)] for t in combinations(ids,4)):
                full_rank.append(word)
            if n==3:
                words3[word]=det([(1,)*5]+[row(s) for s in edges])
        levels.append({'length':n,'all_six':all_edges,'full_rank_count':len(full_rank)})
    assert [w for w,d in words3.items() if d]==['101']
    assert all(not m['all_six'] for m in levels[:7]) and levels[7]['all_six']==['1010101']
    assert not any(m['full_rank_count'] for m in levels[:3])
    g=(1,1,1,-2,-2)
    assert all(total(g,r)==0 for r in forms) and sum(g)==-1
    return {'group_order':len(orbit),'six_sorted_index_sets':forms,'tree_counts':{'singular':3,'unimodular':12},
            'three_command_determinants':words3,'word_census':levels,
            'fully_excited_101_matrix':[(1,)*5]+[row(t) for t in masks('101')],
            'all_future_unknown_margin_kernel':g}


def finite_domain():
    classes=[Counter() for _ in range(4)]
    margins=Counter()
    paired=[]
    for mu in range(7):
        for src in compositions(mu,10):
            h=src[:5]
            x=tuple(a+b for a,b in zip(h,src[5:]))
            S=sum(h)
            margins[mu,S]+=1
            rec=observations(x,h,'101')
            assert from_x_coordinates(mu,rec[0][0],rec[0][1],rec[1][0],rec[3][0])==x
            assert from_h_coordinates(S,*(v[2] for v in rec))==h
            for t in range(4):
                classes[t][(mu,S,*rec[:t+1])]+=1
            paired.append((x,h))
    assert len(paired)==comb(16,10) and all(n==1 for n in classes[3].values())
    # Exact intervals for every entry. Two labelled hypotheses differ in one tagged reading.
    x=(1,0,0,1,0)
    h1=(1,0,0,0,0)
    h2=(0,0,0,1,0)
    r1=observations(x,h1,'101')
    r2=observations(x,h2,'101')
    boxes=tuple(tuple((Fraction(min(a,b)),Fraction(max(a,b))) for a,b in zip(ra,rb))
                for ra,rb in zip(r1,r2))
    posterior=feasible(2,1,boxes)
    assert posterior=={(x,h1),(x,h2)}
    # Compare a varied family of interval inversions against independent full enumeration.
    pools = [(a,b) for a,b in paired if sum(a)==4 and sum(b)==2]
    tests=0
    for x0,h0 in pools[::7]:
        record=observations(x0,h0,'101')
        boxes2=tuple(tuple((Fraction(v)-Fraction((i+j)%3,2), Fraction(v)+Fraction((i+j+1)%3,2))
                           for j,v in enumerate(line)) for i,line in enumerate(record))
        direct={(a,b) for a,b in pools if all(lo<=v<=hi for line,box in zip(observations(a,b,'101'),boxes2)
                                                for v,(lo,hi) in zip(line,box))}
        assert feasible(4,2,boxes2)==direct
        tests+=1
    return {'total_paired_states':len(paired),'finite_domain_total_maximum':6,
            'route_applications_per_colored_column':len(paired)*3,
            'pairs_of_routed_columns':len(paired)*3,'source_sensitive_generated_readings':len(paired)*4,
            'ordinary_generated_readings':len(paired)*8,
            'exact_prefix_classes':[len(v) for v in classes],
            'indistinguishable_unordered_pairs_by_prefix_including_preparation':
                [sum(comb(v,2) for v in bins.values()) for bins in [margins,*classes]],
            'largest_fibre_by_prefix':[max(v.values()) for v in classes],
            'posterior_vs_full_scan_rational_box_queries':tests,
            'closed_half_error_example':{'cell_totals':x,'source_total':1,'first':h1,'second':h2,
                'records':[r1,r2],'feasible_initials':len(posterior),
                'feasible_current':sorted(tuple(path(b,'101'))[-1] for a,b in posterior)}}


def adaptive_capacity():
    def separable(x,group,w,steps):
        if len(group)<=1:
            return True
        if not steps:
            return False
        for g in '01':
            children={}
            for h in group:
                record=observations(x,h,w+g)[-1][2]
                children.setdefault(record,[]).append(h)
            if all(separable(x,v,w+g,steps-1) for v in children.values()):
                return True
        return False
    below=0
    for mu in range(4):
        for x in compositions(mu,5):
            groups={}
            for h in product(*(range(a+1) for a in x)):
                groups.setdefault((sum(h),total(h,Y)),[]).append(h)
            for group in groups.values():
                assert separable(x,group,'',2)
                below+=1
    x=(1,1,0,1,1)
    group=[h for h in product(*(range(a+1) for a in x)) if sum(h)==2 and total(h,Y)==1]
    assert len(group)==4 and not separable(x,group,'',2)
    for mu in range(29):
        b=mu//7
        x=tuple(b*abs(a)+(mu%7 if i==0 else 0) for i,a in enumerate((1,1,1,-2,-2)))
        candidates=[(t,t,t,2*b-2*t,2*b-2*t) for t in range(b+1)]
        key=masks('1010101')
        assert all(min(h)>=0 and all(a<=v for a,v in zip(h,x)) for h in candidates)
        assert len({tuple(total(h,r) for r in key) for h in candidates})==1
    return {'two_step_identifiability_with_known_x_all_classes_below_mass_four':below,
            'first_failure_known_x':x4_record(),
            'unknown_source_amount_sharp_max_fibre_tested_through_mass':28}


def x4_record():
    x=(1,1,0,1,1)
    candidates=sorted(h for h in product(*(range(a+1) for a in x)) if sum(h)==2 and total(h,Y)==1)
    return {'x':x,'S':2,'source_rows':candidates,
            'words_to_four_observation_signatures':{
                w:[tuple(v[2] for v in observations(x,h,w)) for h in candidates]
                for w in ('00','01','10','11')}}


def source_check(file):
    if sha256(file.read_bytes()).hexdigest()!=SOURCE:
        raise ValueError('Local input does not match the published fingerprint.')
    with ZipFile(file) as zf:
        txt=zf.read('CONVERSATION_FRONTIER.md').decode()
    def fields(pattern):
        return re.search(pattern,txt).group(1)
    names=fields(r'x=\(([a-z,]+)\)').split(',')
    routes=[tuple(names.index(s) for s in fields(fr'U{g}=\(([a-z,]+)\)').split(',')) for g in range(2)]
    y,z=[tuple(names.index(s) for s in fields(fr'(?<![A-Za-z]){var}=([a-z+]+)').split('+')) for var in 'yz']
    # Establish the anonymous equivalence by trying every bijection. No private name is exported.
    from itertools import permutations
    def conjugates(p):
        return (all(permute(p,r)==tuple(ROUTES[g][i] for i in p) for g,r in enumerate(routes))
                and {p[i] for i in y}==set(Y) and {p[i] for i in z}==set(Z))
    choices=[p for p in permutations(range(5)) if conjugates(p)]
    assert len(choices)==1
    p=choices[0]
    # All unit basis contributions, actual permutations both ways, including all words through seven.
    checks=0
    for word in (''.join(w) for n in range(8) for w in product('01', repeat=n)):
        for i in range(5):
            basis=tuple(int(k==i) for k in range(5))
            bcanon=tuple(int(k==p[i]) for k in range(5))
            assert observations(basis,basis,word,routes,y,z)==observations(bcanon,bcanon,word)
            checks+=1
    return {'matched_archive_fingerprint':SOURCE,'anonymous_coordinate_bijections':len(choices),
            'operator_and_observation_word_basis_checks':checks,'word_lengths':[0,7],
            'physical_sensor_calls':0}


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--intake',type=Path,help='Optional original local archive.')
    cli.add_argument('--out',type=Path)
    args=cli.parse_args()
    result={'graph':graph_and_words(),'enumeration':finite_domain(),'sharp_bounds':adaptive_capacity()}
    if args.intake:
        result['private_input_comparison']=source_check(args.intake)
    data=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.out:
        args.out.write_text(data,encoding='utf-8')
    else:
        print(data,end='')

if __name__=='__main__':
    main()
