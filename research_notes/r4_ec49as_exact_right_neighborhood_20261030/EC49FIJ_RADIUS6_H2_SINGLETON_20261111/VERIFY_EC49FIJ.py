#!/usr/bin/env python3
"""Exhaustive exact radius-six H2-lift + single-demand screen (A/B).
Requires frozen sibling EC49FGW_RADIUS5_EXACT_SCREENS_20261110.
All arithmetic is integer and complete within the declared finite catalogue.
"""
import sys,itertools,collections,math,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'
sys.path.insert(0,str(SOURCE))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,pref,raw_key,validate_profile

def index(catalog,labels,key_filter,baseline):
    best=[10**6]*24; groups=[{} for _ in range(24)]
    pos={lab:i for i,lab in enumerate(labels)}
    for lab,w in catalog:
        if key_filter is not None and raw_key(w) not in key_filter:continue
        j=pos[lab];wordpref=pref(w);L=len(wordpref)
        best[j]=min(best[j],L)
        for p in wordpref:
            if p in baseline:
                s=baseline[p]; groups[j][s]=min(groups[j].get(s,10**6),L-len(p))
    return best,[tuple(x.items()) for x in groups]

def solve(profile,catalog):
    rows,ps=validate_profile(profile)
    labels=[(r['window'],r['signature']) for r in rows]
    h2={i for i,(h,s) in enumerate(labels) if h==2}
    assert len(h2)==2
    sup=collections.defaultdict(int);ksup=collections.defaultdict(int)
    for i,(r,pp) in enumerate(zip(rows,ps)):
        ksup[raw_key(r['word'])]|=1<<i
        for p in pp:sup[p]|=1<<i
    assert len(sup)==94 and len(ksup)==7
    base7,idx7=index(catalog,labels,set(ksup),sup)
    baseall,idxall=index(catalog,labels,None,sup)
    counts=collections.Counter();hist=collections.Counter()
    for Q in itertools.combinations(range(24),6):
        mask=sum(1<<i for i in Q)
        B=sum((s&mask)==s for s in sup.values())-1
        if B<0:counts['fixed94']+=1;continue
        if h2.intersection(Q):counts['radius5_lift']+=1;continue
        released=any((s&mask)==s for s in ksup.values())
        typ='released' if released else 'fixed7'
        counts[typ+'_input']+=1
        base,idx=(baseall,idxall) if released else (base7,idx7)
        # Exact singleton min: candidate word length minus its longest
        # prefix still in the fixed prefix-closed background.
        reject=False
        for j in Q:
            v=base[j]
            for s,cost in idx[j]:
                if (s & ~mask) and cost<v:v=cost
            if v>B:reject=True;break
        counts[typ+('_reject' if reject else '_remain')]+=1
        if not reject:hist[(typ,B)]+=1
    assert sum(counts[k] for k in ('fixed94','radius5_lift','released_input','fixed7_input'))==math.comb(24,6)
    return {'profile':profile['profile_id'],'counts':dict(counts),'remaining_budget_hist':{f'{k}:{b}':v for (k,b),v in sorted(hist.items())}}

def run():
    catalog=list(all_words());assert len(catalog)==178850
    h2=collections.Counter(lab for lab,w in catalog if lab[0]==2)
    assert h2=={(2,16):1,(2,32):1}
    result={'schema':'EC49FIJ_RADIUS6_EXACT_SCREEN_V1','scientific_pin':PIN,
            'catalog_words':len(catalog),'positions_per_profile':math.comb(24,6),
            'H2_included_positions':math.comb(24,6)-math.comb(22,6),
            'profiles':[solve(prof,catalog) for prof in W['profiles']]}
    for p in result['profiles']:
        c=p['counts']
        assert c=={'fixed94':18564,'radius5_lift':49427,
                   'released_input':4084,'released_reject':2072,'released_remain':2012,
                   'fixed7_input':62521,'fixed7_reject':22548,'fixed7_remain':39973},(p['profile'],c)
    (HERE/'EXACT_REPORT_EC49FIJ.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,indent=2,ensure_ascii=False)); print('EC49FIJ_EXACT_PASS')
if __name__=='__main__':run()
