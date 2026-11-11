"""R87: exact single-time polarities and champion witness certificate.
Only Python standard library. Auxiliary rational circle model, not native BRC.
"""
from fractions import Fraction as F
from random import Random
from collections import Counter
import json


def fract(z):
    return z - z.numerator // z.denominator


def member(t, theta, j, x, a, b):
    s, A, B = fract(x + (t-j)*theta), fract(a*theta), fract(b*theta)
    return ((A <= s < B) if A < B else
            (s >= A or s < B) if A > B else False)


def cuts_for_time(t, I, j, x, a, b):
    L, U = I
    cuts = {L,U}
    for c,d in ((a,F(0)),(b,F(0)),(a-b,F(0)),
                (t-j,x),(t-j-a,x),(t-j-b,x)):
        if not c: continue
        lo, hi = sorted((c*L+d,c*U+d))
        kl = -( (-lo).numerator // (-lo).denominator ) # ceil(lo)
        ku = hi.numerator // hi.denominator
        for k in range(kl,ku+1):
            p = (F(k)-d)/c
            if L<=p<=U: cuts.add(p)
    return sorted(cuts)


def atoms(cuts):
    for i,p in enumerate(cuts):
        yield p
        if i+1<len(cuts):yield (p+cuts[i+1])/2


def polarity_witness(t, want, I, j, x, a, b, stats):
    stats['oracle_calls'] += 1
    cuts = cuts_for_time(t,I,j,x,a,b)
    stats['per_time_cuts'] += len(cuts)
    for q in atoms(cuts):
        stats['atom_tests'] += 1
        if member(t,q,j,x,a,b)==want:return q
    return None


def winner_at(present,theta,j,x,a,b,stats=None):
    for t,br in sorted(present, reverse=True):
        if stats is not None: stats['point_tests'] += 1
        if member(t,theta,j,x,a,b):return (t,br)
    return None


def champion(present,I,j,x,a,b,cache=None,stats=None):
    """Exact complete STABLE_NONE / STABLE(identity) / CHANGES.
    Reuses signature-specific positive and negative witness caches across versions.
    """
    stats = Counter() if stats is None else stats
    cache = {} if cache is None else cache
    L,_ = I
    base = winner_at(present,L,j,x,a,b,stats)
    unique_times = sorted({t for t,_ in present}, reverse=True)
    def witness(t,want):
        key=(I,j,x,a,b,t,want)
        if key not in cache:cache[key]=polarity_witness(t,want,I,j,x,a,b,stats)
        else:stats['cache_hits'] += 1
        return cache[key]
    if base is None:
        for t in unique_times:
            q=witness(t,True)
            if q is not None:
                w=winner_at(present,q,j,x,a,b,stats)
                assert w is not None
                return ('CHANGES',(L,base),(q,w))
        return ('STABLE_NONE',None,None)
    for t in unique_times:
        if t > base[0]:
            q=witness(t,True)
            if q is not None:
                w=winner_at(present,q,j,x,a,b,stats)
                assert w!=base
                return ('CHANGES',(L,base),(q,w))
    q=witness(base[0],False)
    if q is not None:
        w=winner_at(present,q,j,x,a,b,stats)
        assert w!=base
        return ('CHANGES',(L,base),(q,w))
    return ('STABLE',base,None)


def independent_profile(present,I,j,x,a,b,stats):
    cuts={*I}
    for t in {t for t,_ in present}:
        tc=cuts_for_time(t,I,j,x,a,b)
        stats['reference_source_profiles_built'] += 1
        stats['reference_source_cut_sums'] += len(tc)
        cuts.update(tc)
    vals=[]
    for p in atoms(sorted(cuts)):
        stats['reference_atom_tests'] += 1
        vals.append((p,winner_at(present,p,j,x,a,b)))
    if all(w==vals[0][1] for _,w in vals):
        return ('STABLE_NONE' if vals[0][1] is None else 'STABLE', vals[0][1])
    return ('CHANGES',None)


def check():
    rng=Random(8720261112)
    checked=0; changes=0; stable=0; history=0
    total=Counter(); cache={}
    # Randomized version histories and changing signatures including degenerate arcs.
    for run in range(64):
        L=F(rng.randint(-3,2),rng.randint(3,9)); U=L+F(rng.randint(0,3),rng.randint(5,18))
        I=(L,U); j=rng.randint(-4,4); x=F(rng.randint(-4,4),rng.randint(2,9))
        a=rng.randint(-5,5); b=rng.randint(-5,5)
        cur=set(); versions=[]
        for step in range(10):
            who=(rng.randint(-20,20),rng.randint(-2,3))
            if who in cur:cur.remove(who)
            else:cur.add(who)
            versions.append(frozenset(cur))
            # Audit current and one historic source version.
            for present in [versions[-1],versions[rng.randrange(len(versions))]]:
                res=champion(present,I,j,x,a,b,cache,total)
                ref=independent_profile(present,I,j,x,a,b,total)
                assert res[0]==ref[0], (run,step,I,j,x,a,b,present,res,ref)
                if res[0]=='STABLE': assert res[1]==ref[1]
                if res[0]=='CHANGES':
                    for q,w in res[1:]:
                        assert I[0]<=q<=I[1]
                        assert winner_at(present,q,j,x,a,b)==w
                    assert res[1][1]!=res[2][1]
                    changes+=1
                else:stable+=1
                checked+=1
            history+=1
    # A family with many lower times but the top qualifying throughout I.
    benefit=[]
    for n in [16,64,256,512]:
        I=(F(1,4),F(1,4)+F(1,10**8))
        x=F(0);j=0;a=1;b=2
        present={(t,0) for t in range(1,n+1)} | {(4*n+1,1)}
        sc=Counter(); result=champion(present,I,j,x,a,b,{},sc)
        assert result[:2]==('STABLE',(4*n+1,1))
        refstats=Counter(); reference=independent_profile(present,I,j,x,a,b,refstats)
        assert reference==('STABLE',(4*n+1,1))
        benefit.append({'source_identities':len(present),'champion_oracle_calls':sc['oracle_calls'],
                        'champion_point_tests':sc['point_tests'],
                        'champion_atom_tests':sc['atom_tests'],
                        'reference_atom_tests':refstats['reference_atom_tests'],
                        'reference_source_profiles_built':refstats['reference_source_profiles_built'],
                        'reference_source_cut_sums':refstats['reference_source_cut_sums']})
    # Necessary polarities: top source qualifies at L but drops later;
    # top source not qualified at L but becomes member later.
    assert champion({(5,0)},(F(1,4),F(1,3)),0,F(0),1,2)[0]=='CHANGES'
    assert champion({(8,0)},(F(1,4),F(3,10)),0,F(0),1,2)[0]=='CHANGES'
    return {'seed':8720261112,'random_history_edits':history,
            'independent_version_comparisons':checked,'stable_results':stable,
            'changes_results':changes,'oracle_calls':total['oracle_calls'],
            'oracle_cache_hits':total['cache_hits'],
            'per_time_cuts_enumerated':total['per_time_cuts'],
            'champion_atom_tests':total['atom_tests'],
            'independent_profile_atom_tests':total['reference_atom_tests'],
            'reference_source_profiles_built':total['reference_source_profiles_built'],
            'reference_source_cut_sums':total['reference_source_cut_sums'],
            'top_stable_family':benefit,'assertions':'PASS'}

if __name__=='__main__':
    r=check()
    with open(__file__.replace('check_r87.py','verification.json'),'w') as f:
        json.dump(r,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print('R87_PASS',r['independent_version_comparisons'],r['changes_results'],r['oracle_calls'],r['oracle_cache_hits'])
