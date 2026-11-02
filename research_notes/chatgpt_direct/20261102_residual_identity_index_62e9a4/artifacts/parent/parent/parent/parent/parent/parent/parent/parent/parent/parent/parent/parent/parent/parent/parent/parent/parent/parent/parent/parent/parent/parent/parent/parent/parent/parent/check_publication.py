"""Guarded signed publication, monotone certificates, and polling without a join.

Conditional triadic matching model; not native physics. All matching transitions
use the unmodified inherited kernel; path alternatives/concatenation use CWM.
Imported parent modules are reused, and their main suites are not executed.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from itertools import product

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_contention as old

a, p, e, m, r = old.a, old.p, old.e, old.m, old.r
ONE, ZERO = old.ONE, old.ZERO
CHECKS = CALLS = USES = 0
CACHE = {}


def check(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def step(J, op, H):
    global CALLS, USES
    USES += 1
    if op[0] == 'reserve' and op[1] not in H:
        raise ValueError('undeclared event')
    key = (J, op)
    if key not in CACHE:
        K, _, success = e.step(J, op, H)
        CACHE[key] = K, success
        CALLS += 1
    return CACHE[key]


def put(d, key, mass):
    d[key] = r.merge(d.get(key, ZERO), mass)


def total(d):
    result = ZERO
    for weight in d.values():
        result = r.merge(result, weight)
    return result


def spec(i):
    H, W, bridge, probe = old.worker(i)
    o = old.flag(i)
    g = 200 + 10*i
    guard = (g, g+1, g+2)
    pos = tuple(sorted((g, o+4, 300)))
    neg = tuple(sorted((g, o+3, 310+i)))
    # No consumer can act on the register while guard occupies g.
    # Keep the signed tail directly: no full header is built or reopened.
    word = W[:5] + [W[-1], p.one(g+1)]
    H = H - {p.reg(o,0)[0], p.reg(o,1)[0]}
    return dict(H=H | {guard, pos, neg}, W=word, guard=guard,
                pos=pos, neg=neg, bridge=bridge, probe=probe, offset=o,
                plus=p.reg(o,1)[1], minus=p.reg(o,0)[1])


def collector(k, overwrite=False):
    if not 2 <= k <= 6:
        raise ValueError('this address allocation supports 2..6 workers')
    specs = [spec(i) for i in range(k)]
    H = set(p.library(400))  # true model constant 0 for AND(a,b)=Maj(a,b,0)
    samples = [500] + [520+10*i for i in range(k)]
    W = []
    if overwrite:
        for offset in samples + [700]:
            W += p.clear_word(offset)
    # Every round retries all guarded publications before its own sampling.
    W += [p.add(s['pos']) for s in specs]
    W += [p.add(s['neg']) for s in specs]
    H |= {s[key] for s in specs for key in ('pos','neg')}
    for port, offset in zip([300]+[310+i for i in range(k)], samples):
        h, w, _ = a.reader(port, offset, offset+7)
        H |= h; W += w
    cur = samples[1]; temporary = []
    for i in range(1,k):
        out = 700 if i == k-1 else 720+10*(i-1)
        h,w = old.majority((cur, samples[i+1],400), out)
        H |= h; W += w
        if out != 700: temporary.append(out)
        cur = out
    for offset in temporary:
        W += p.clear_word(offset)
    return H, W, samples


def setup(J, k):
    specs = [spec(i) for i in range(k)]
    HC, WC, samples = collector(k)
    H = a.SOURCE_H | HC | set().union(*(s['H'] for s in specs))
    init = m.canon(J + p.reg(400,0) + tuple(s['guard'] for s in specs))
    opened,_ = step(init,p.one(4),H)
    return H, opened, specs, WC, samples


def code(J):
    return (p.read(J,500),p.read(J,700))


def safety(J, K, specs, pcs, wins):
    # Published certificates preserve actual acquired/not-acquired facts.
    check(old.protected(J,K), 'source tail, old residual and source E preserved')
    for i,s in enumerate(specs):
        finished = pcs[i] == len(s['W'])
        check((s['guard'] not in K) == finished, 'guard removal tracks publication point')
        if finished:
            check((s['plus'] in K) == bool(wins & (1<<i)), 'published positive tail equals own acquisition')
            check((s['minus'] in K) != bool(wins & (1<<i)), 'published negative tail equals own non-acquisition')
        if s['pos'] in K:
            check(finished and bool(wins & (1<<i)), 'positive message requires completed successful acquisition')
        if s['neg'] in K:
            check(finished and not bool(wins & (1<<i)), 'negative message requires completed non-acquisition')


def run(J, word, H, omitted=(), trace=True):
    start = J; weight = e.prep(J); rows=[]; omit=frozenset(omitted)
    for index,op in enumerate(word):
        before=J
        J,ok=(J,None) if index in omit else step(J,op,H)
        weight=r.serial(weight,ONE)
        if trace:
            rows.append(dict(index=index+1,op=op,invoked=index not in omit,
                             success=ok,before=before,after=J))
    return dict(initial=start,end=J,commands=len(word),CWM=e.cw(weight),trace=rows)


def interleave(J, k, full_collector=False):
    H,initial,specs,WC,samples = setup(J,k)
    C = WC if full_collector else [p.add(s[key]) for key in ('pos','neg') for s in specs]
    words=[s['W'] for s in specs]+[C]
    lengths=tuple(map(len,words))
    d={((0,)*(k+1),initial,0):e.prep(initial)}
    peak=1
    for _ in range(sum(lengths)):
        nxt={}
        for (pcs,K,wins),mass in d.items():
            for i,j in enumerate(pcs):
                if j==lengths[i]:continue
                np=list(pcs);np[i]+=1;np=tuple(np)
                L,ok=step(K,words[i][j],H)
                nw=wins|((1<<i) if i<k and j==0 and ok else 0)
                safety(J,L,specs,np,nw)
                put(nxt,(np,L,nw),r.serial(mass,ONE))
        d=nxt;peak=max(peak,len(d))
    observed={};terms={}
    for (pcs,K,wins),mass in d.items():
        flag=code(K) if full_collector else (
            int(any(s['pos'] in K for s in specs)),
            int(all(s['neg'] in K for s in specs)))
        check(flag in ((0,0),(1,0),(0,1)), 'no contradictory result')
        check(flag[0] != 1 or a.signed(J)==1,'yes never false')
        check(flag[1] != 1 or a.signed(J)==0,'no never false')
        put(observed,flag,mass)
        terms[K]=wins
    # A disjoint position-only CWM verifies that no schedule was discarded.
    expected=old.positional_mass(lengths,0,0)[0]
    check(total(d)==expected,'complete schedule weight conserved')
    # A later round is normal polling, not an oracle testing producer completion.
    h,retry,_=collector(k,overwrite=full_collector)
    # For message-only runs outputs are still blank, so no overwrite is needed.
    for K in terms:
        end=run(K,retry,H|h,trace=False)['end']
        check(code(end)==((1,0) if a.signed(J) else (0,1)),
              'one polling round after all publication completes resolves')
    return dict(workers=k,full_collector=full_collector,initial=J,
                lengths=lengths,peak_states=peak,terminal_states=len(d),
                CWM=e.cw(expected),outcomes=[dict(code=c,CWM=e.cw(w)) for c,w in sorted(observed.items())])


def local_publication():
    rows=[]
    # Selective replay only: new publication interface, not the parent main.
    _,domain=e.catalog(a.SOURCE_H)
    for J in sorted(domain):
        if a.signed(J)<0:continue
        H,start,specs,_,_=setup(J,2);s=specs[0]
        # Probe both output routes after EVERY producer prefix.
        K=start;word=[]
        for op in s['W']:
            word += [p.add(s['pos']),p.add(s['neg']),op]
        word += [p.add(s['pos']),p.add(s['neg'])]
        z=run(K,word,H)
        check((s['pos'] in z['end']) == bool(a.signed(J)),'local signed publication')
        check((s['neg'] in z['end']) != bool(a.signed(J)),'local negative publication')
        check(s['plus'] in z['end'] if a.signed(J) else s['minus'] in z['end'],'tail retained')
        rows.append(z)
    return rows


def boundary_traces():
    rows={}
    # No guard: a query before any acquisition creates a fake positive message.
    H,J,S,WC,_=setup((a.HN,),2)
    s=S[0]
    K=m.canon(h for h in J if h!=s['guard'])
    z=run(K,[p.add(s['pos'])],H)
    check(s['pos'] in z['end'],'without guard premature positive publication succeeds')
    rows['missing_guard']=z
    # Wrong omission: acquired bridge is true but its private probe is missed.
    H,J,S,WC,_=setup((a.HN,),2);s=S[0]
    z=run(J,s['W']+[p.add(s['pos'])],H,omitted=(1,))
    check(s['pos'] in z['end'],'unprotected publication does not tolerate probe omission')
    rows['unprotected_omission']=z
    # Premature release of readiness, even by its valid private address.
    H,J,S,WC,_=setup((a.HN,),2);s=S[0]
    z=run(J,[p.one(s['guard'][1]),p.add(s['pos'])],H)
    check(s['pos'] in z['end'],'publication order is a real causal precondition')
    rows['premature_release']=z
    # Cleanup omission remains conservative: no published certificate.
    H,J,S,WC,_=setup((a.HP,),2);s=S[0]
    z=run(J,s['W']+[p.add(s['pos']),p.add(s['neg'])],H,omitted=(6,))
    check(s['pos'] not in z['end'] and s['neg'] not in z['end'],'unreleased guard withholds both signs')
    rows['withheld_publication']=z
    # A valid late negative does not erase an already valid positive.
    H,J,S,WC,_=setup((a.HP,),2)
    W=[S[0]['W'][0]]+S[1]['W']+S[0]['W'][1:]
    z=run(J,W+WC,H)
    check(code(z['end'])==(1,0),'one acquired and one unacquired is positive')
    rows['one_witness_is_enough']=z
    # Arbitrarily early full collection returns UNKNOWN, then polling resolves.
    for b in (0,1):
        source=p.reg(3,b)
        H,J,S,WC,_=setup(source,2)
        first=run(J,WC,H)
        check(code(first['end'])==(0,0),'early collection neither guesses zero nor corrupts workers')
        h,retry,_=collector(2,True)
        second=run(first['end'],S[0]['W']+S[1]['W']+retry,H|h)
        check(code(second['end'])==((1,0) if b else (0,1)),'same-workspace next round completes')
        rows[f'early_then_retry_{b}']={'early':first,'late':second}
    # Early valid YES while another worker has not executed a single command.
    H,J,S,WC,_=setup((a.HP,),2)
    z=run(J,S[0]['W']+WC,H)
    check(code(z['end'])==(1,0) and S[1]['guard'] in z['end'],'true result before all workers finish')
    rows['early_positive']=z
    # Negative partial data do not justify NO; last worker supplies the positive.
    # First hold worker0's bridge, let worker1 fail/finish, then query.
    H,J,S,WC,_=setup((a.HP,),2)
    z=run(J,[S[0]['W'][0]]+S[1]['W']+WC,H)
    check(code(z['end'])==(0,0),'negative subset cannot deny unfinished successful bridge')
    rows['negative_subset_unknown']=z
    return rows


def full_examples():
    rows=[]
    for k in (2,3,6):
        for b in (0,1):
            source=p.reg(3,b)
            H,J,S,WC,_=setup(source,k)
            # Producer bridge attempts first, then complete each private result.
            W=[s['W'][0] for s in S]+[op for s in S for op in s['W'][1:]]
            z=run(J,W+WC,H)
            check(code(z['end'])==((1,0) if b else (0,1)),'complete source-to-certified-answer path')
            check(len(W+WC)+1==62*k-42,'first full-round command formula includes source opening')
            check(old.protected(source,z['end']),'original source and residual preserved')
            rows.append(dict(workers=k,source=b,total_including_open=len(W+WC)+1,inventory=len(set().union(*(set(h) for h in H))),execution=z))
    return rows


def prefix_extensions():
    """Finite exact evidence algebra, not a new physical three-valued logic."""
    counts=[]
    for k in range(1,7):
        U=frozenset(range(k));n=0
        # Per channel: missing, positive, negative. No channel asserts both.
        for vals in product(range(3),repeat=k):
            P=frozenset(i for i,x in enumerate(vals) if x==1)
            N=frozenset(i for i,x in enumerate(vals) if x==2)
            decision=1 if P else 0 if N==U else None
            mass=ONE
            for vals2 in product(range(3),repeat=vals.count(0)):
                it=iter(vals2)
                ext=tuple(next(it) if x==0 else x for x in vals)
                P2=frozenset(i for i,x in enumerate(ext) if x==1)
                N2=frozenset(i for i,x in enumerate(ext) if x==2)
                d2=1 if P2 else 0 if N2==U else None
                check(decision is None or d2==decision,'truthful irreversible decisions monotone in compatible signed evidence')
                mass=r.merge(mass,ONE);n+=1
        counts.append(dict(channels=k,extensions=n))
    return counts


def protected_interleave(J,k,f):
    H,_,specs,WC,_=setup(J,k)
    rep=f+1
    gate_word=[p.add(s[key]) for key in ('pos','neg') for s in specs]
    words=[old.repeat(s['W'],rep) for s in specs]+[old.repeat(gate_word,rep)]
    lengths=tuple(map(len,words))
    initial=m.canon(J+p.reg(400,0)+tuple(s['guard'] for s in specs))
    d={((0,)*(k+1),initial,0,0):e.prep(initial)}
    for op in [p.one(4)]*rep:
        q={}
        for (pcs,K,wins,b),mass in d.items():
            L,_=step(K,op,H)
            put(q,(pcs,L,wins,b),r.serial(mass,ONE))
            if b<f:put(q,(pcs,K,wins,b+1),r.serial(mass,ONE))
        d=q
    peak=len(d)
    for _ in range(sum(lengths)):
        q={}
        for (pcs,K,wins,b),mass in d.items():
            for i,j in enumerate(pcs):
                if j==lengths[i]:continue
                np=list(pcs);np[i]+=1;np=tuple(np)
                L,ok=step(K,words[i][j],H)
                nw=wins|((1<<i) if i<k and j<rep and ok else 0)
                options=[(L,nw,b)]
                if b<f:options.append((K,wins,b+1))
                for M,mwins,mb in options:
                    check(old.protected(J,M),'protected source frame under global omissions')
                    for t,s in enumerate(specs):
                        published=s['guard'] not in M
                        if published:
                            check(np[t]>6*rep,'publication follows all protected preparation groups')
                            check((s['plus'] in M)==bool(mwins&(1<<t)), 'protected published result agrees with contact')
                            check((s['minus'] in M)!=bool(mwins&(1<<t)), 'protected published negative agrees with contact')
                        if s['pos'] in M:check(published and bool(mwins&(1<<t)), 'protected positive truthful')
                        if s['neg'] in M:check(published and not bool(mwins&(1<<t)), 'protected negative truthful')
                    put(q,(np,M,mwins,mb),r.serial(mass,ONE))
        d=q;peak=max(peak,len(d))
    layers={};outcomes={};terms={}
    for (pcs,K,wins,b),mass in d.items():
        val=(int(any(s['pos'] in K for s in specs)),int(all(s['neg'] in K for s in specs)))
        check(val in ((0,0),(1,0),(0,1)), 'protected full result encoding')
        check(val[0]!=1 or a.signed(J)==1,'protected positive safety')
        check(val[1]!=1 or a.signed(J)==0,'protected negative safety')
        put(layers,b,mass);put(outcomes,(b,val),mass);terms[K]=b
    check(layers==old.positional_mass(lengths,rep,f), 'omission and shuffle CWM conservation')
    h,retry,_=collector(k,False)
    # These post-completion passes add no new faults; the general protection
    # proof also covers remaining budget, not inferred from this regression.
    for K in terms:
        z=run(K,old.repeat(retry,rep),H|h,trace=False)
        check(code(z['end'])==((1,0) if a.signed(J) else (0,1)), 'protected polling recovery')
    return dict(workers=k,faults=f,source=a.signed(J),commands=rep+sum(lengths),scope='protected producers and guarded emissions, not full concurrent sampling',
                peak_states=peak,terminal_states=len(d),
                layers=[dict(faults=b,CWM=e.cw(v)) for b,v in sorted(layers.items())],
                outcomes=[dict(faults=b,code=val,CWM=e.cw(w)) for (b,val),w in sorted(outcomes.items())])


def protected_serial(J,k,f,early=False):
    H,_,S,WC,_=setup(J,k)
    rep=f+1
    start=m.canon(J+p.reg(400,0)+tuple(s['guard'] for s in S))
    prod=[s['W'][0] for s in S]+[op for s in S for op in s['W'][1:]]
    W=old.repeat([p.one(4)]+(WC+prod if early else prod+WC),rep)
    d={(start,0):e.prep(start)}
    for op in W:
        q={}
        for (K,b),mass in d.items():
            L,_=step(K,op,H)
            put(q,(L,b),r.serial(mass,ONE))
            if b<f:put(q,(K,b+1),r.serial(mass,ONE))
        d=q
    layers={}
    for (K,b),mass in d.items():
        expected=(0,0) if early else ((1,0) if a.signed(J) else (0,1))
        check(code(K)==expected,'protected end-to-end result has declared information content')
        check(old.protected(J,K),'protected end-to-end original residual preserved')
        put(layers,b,mass)
        if early:
            h,retry,_=collector(k,True)
            end=run(K,old.repeat(retry,rep),H|h,trace=False)['end']
            check(code(end)==((1,0) if a.signed(J) else (0,1)), 'retry resolves withheld protected result')
    check(layers==a.layers(len(W),f),'serial omission budget conserved in original CWM')
    return dict(workers=k,faults=f,early=early,commands=len(W),
                layers=[dict(omissions=b,CWM=e.cw(w)) for b,w in sorted(layers.items())])


def main():
    result={}
    result['local_publication']=local_publication()
    result['boundaries']=boundary_traces()
    result['full_examples']=full_examples()
    result['evidence_algebra']=prefix_extensions()
    result['shuffle_families']=[]
    for k in (2,3):
        for J in ((a.HP,),m.canon((a.P,a.HN))):
            result['shuffle_families'].append(interleave(J,k,False))
    for J in ((a.HP,),m.canon((a.P,a.HN))):
        result['shuffle_families'].append(interleave(J,2,True))
    result['protected_shuffle_families']=[protected_interleave(p.reg(3,b),2,1) for b in (0,1)]
    result['protected_full_families']=[protected_serial(p.reg(3,b),2,f,early) for b in (0,1) for f in (1,2) for early in (False,True)]
    result['metrics']=dict(checks=CHECKS,uncached_kernel_calls=CALLS,transition_uses=USES,
                           full_shuffle_families=len(result['shuffle_families']))
    out=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'results.json'
    out.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps(result['metrics'],ensure_ascii=False,sort_keys=True))
    print(json.dumps(result['shuffle_families'],ensure_ascii=False,sort_keys=True))

if __name__=='__main__':main()
