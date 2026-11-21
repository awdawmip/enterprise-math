"""Executable fail-closed decoding of the inherited 20-state origin code.

All scientific state updates use the unchanged inherited triadic/BRC kernel.
The static compiler emits one word for every input. Expected Boolean predicates
are used only to audit the word, never to choose runtime instructions.
"""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
from functools import lru_cache
from itertools import combinations,product
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_observer_cover as prior
old=prior.old
j,p,m,e,r,f=prior.j,prior.p,prior.m,prior.e,prior.r,prior.f
reader=f.a.reader
ONE,ZERO=prior.ONE,prior.ZERO
CHECKS=0

def ck(test,label):
    global CHECKS
    CHECKS+=1
    if not test: raise AssertionError(label)

@lru_cache(None)
def residue_domain():
    _,d=e.catalog(list(combinations(range(49,55),3)))
    return tuple(sorted(d))

def finite_cover(states,desired,seeds):
    """Exact ON/OFF support audit; deterministic greedy, not minimum cover."""
    states=tuple(frozenset(s) for s in states)
    allmask=(1<<len(states))-1
    want=sum(1<<i for i in desired)
    inverted={v:sum(1<<i for i,s in enumerate(states) if v in s)
              for v in set().union(*states)}
    good={}
    for seed in seeds:
        xs=tuple(sorted(seed))
        for n in range(len(xs)+1):
            for q in combinations(xs,n):
                if q in good:continue
                mask=allmask
                for v in q:mask &= inverted[v]
                if mask and mask & ~want == 0:good[q]=mask
    primes={}
    for q in sorted(good,key=lambda q:(len(q),q)):
        if not any(s in primes for n in range(len(q)) for s in combinations(q,n)):
            primes[q]=good[q]
    remaining=want; chosen=[]
    while remaining:
        q=min(primes,key=lambda q:(-(primes[q]&remaining).bit_count(),len(q),q))
        if not primes[q]&remaining:raise ValueError('No positive cover')
        chosen.append(q);remaining &= ~primes[q]
    for q in tuple(reversed(chosen)):
        union=0
        for other in chosen:
            if other!=q:union |= primes[other]
        if union==want:chosen.remove(q)
    union=0
    for q in chosen:union |= primes[q]
    if union!=want:raise AssertionError('cover exactness')
    return [(q,tuple(i for i in range(len(states)) if primes[q]>>i&1)) for q in chosen],len(primes)

@lru_cache(1)
def build():
    parent=prior.compile_codec();B=parent['base']
    inputs=tuple(B['inputs']);Q=(49,50,51,52)
    samples=(60,66,72,78);valid=(85,86,87)
    outputs=tuple(range(90,126,6));status=126;work=55
    weights=tuple(B['weight_codes']);R=residue_domain()
    H=set().union(*(p.library(o) for o in inputs+samples+outputs+(status,)))
    H |= set(combinations(range(49,55),3))|set(weights)|{valid}
    W=[];stages=[];reads=[]
    # Exact sorted-word recognizer, not the parent's sorted-domain shortcut.
    W += [p.one(o+1) for o in inputs]
    for weight,T in enumerate(weights):
        ports=old.literal_ports((0,)*(6-weight)+(1,)*weight,inputs)
        h,w=old.all_occupied_write(ports,T,work);H|=h;W+=w
    W += [p.add(p.reg(o,b)[0]) for o in inputs for b in (0,1)]
    stages.append(dict(name='exact_weight_source_restored',end=len(W)))
    for v,o in zip(Q,samples):
        h,w,_=reader(v,o,work);H|=h
        reads.append(dict(port=v,offset=o,start=len(W),word=w))
        W+=w+[p.one(o+1)]
    stages.append(dict(name='signed_occupancy_snapshot',end=len(W)))
    # Eight possible recognized weights: none for every unsorted complete word.
    rows=B['rows'];admissible={(x['weight'],x['residue']) for x in rows}
    signals=[];background=[];desired=[];seeds=[]
    for weight in (-1,0,1,2,3,4,5,6):
        for T in R:
            used=set(m.used(T))
            literal={o+(3 if v in used else 4) for v,o in zip(Q,samples)}
            s=set(weights[weight]) if weight>=0 else set()
            s |= used|literal
            index=len(signals);signals.append(frozenset(s))
            good=weight>=0 and len(T)==1 and (weight,T[0]) in admissible
            background.append(dict(weight=weight,residue=T,occupied=tuple(sorted(s)),valid=good))
            if good:desired.append(index);seeds.append(s)
    cover,nprime=finite_cover(signals,desired,seeds)
    guards=[]
    for support,covers in cover:
        h,w=old.all_occupied_write(support,valid,work);H|=h;W+=w
        guards.append(dict(support=support,covered=covers,word=w))
    stages.append(dict(name='domain_certified',end=len(W)))
    # Reuse all 70 parent observer supports. Only add a guard port and move
    # targets, so no invalid input can publish even one output tail.
    decoder=[]
    for item in parent['decoder_blocks']:
        bit=item['bit'];o=outputs[bit]
        for block in item['blocks']:
            target=p.reg(o,1)[1];support=tuple(sorted(set(block['support'])|{valid[0]}))
            h,w=old.all_occupied_write(support,target,work);H|=h;W+=w
            decoder.append(dict(bit=bit,support=support,target=target,word=w))
    stages.append(dict(name='guarded_positive_tails',end=len(W)))
    for o in outputs:
        for target in (p.reg(o,0)[1],p.reg(o,0)[0],p.reg(o,1)[0]):
            h,w=old.all_occupied_write((valid[0],),target,work);H|=h;W+=w
    stages.append(dict(name='guarded_complete_output',end=len(W)))
    h,w,_=reader(valid[0],status,work);H|=h;W+=w
    W += [p.one(o+5) for o in samples]
    W += [p.one(v) for v in B['weight_members']]
    W += [p.one(valid[0])]
    stages.append(dict(name='clean_result',end=len(W)))
    return dict(H=H,word=W,stages=stages,inputs=inputs,outputs=outputs,status=status,
                samples=samples,Q=Q,valid=valid,work=work,weights=weights,
                reads=reads,guards=guards,background=background,decoder=decoder,
                rows=rows,prime_count=nprime,parent=parent)

def summary(C):
    return dict(commands=len(C['word']),members=len(set().union(*C['H'])),
        candidate_events=len(C['H']),fixed_occupancy_queries=len(C['Q']),
        validity_terms=len(C['guards']),validity_calls=sum(len(b['word']) for b in C['guards']),
        prime_supports=C['prime_count'],parent_decoder_terms=len(C['decoder']),
        guarded_decoder_calls=sum(len(b['word']) for b in C['decoder']),
        stages=C['stages'],source_preserved=True,invalid_outputs='all six data slots empty; complete status zero',
        minimum_program_claim=False)

def case_domain(first:int,last:int):
    C=build();rows=[];mass=ZERO;valid_count=0
    source_map={(tuple(x['sorted']),(x['residue'],)):tuple(x['bits']) for x in C['rows']}
    for value in range(first,last):
        bits=tuple((value>>(5-i))&1 for i in range(6))
        for T in residue_domain():
            initial=m.canon(j.init(bits,C['inputs'])+T)
            expected_bits=source_map.get((bits,T));good=expected_bits is not None
            Z=f.execute(initial,C['word'],C['H'])['end']
            expected=m.canon(initial+p.reg(C['status'],int(good))+
                             (j.init(expected_bits,C['outputs']) if good else ()))
            ck(Z==expected,'exact source-preserving accepted decode or fail-closed rejection')
            valid_count+=int(good);mass=r.merge(mass,e.prep(initial))
            rows.append(dict(input=bits,residue=T,accepted=good,
                decoded=tuple(p.read(Z,o) for o in C['outputs']),source_unchanged=True))
    return dict(first=first,last=last,cases=len(rows),accepted=valid_count,
                CWM=e.cw(mass),rows=rows,**summary(C))

def audit():
    C=build();out=[];mass=ZERO
    for bi,b in enumerate(C['guards']):
        active=[]
        for i,row in enumerate(C['background']):
            raw=row['residue'];U=set(m.used(raw))
            I=m.canon(raw+(() if row['weight']<0 else (C['weights'][row['weight']],))+
                      tuple(p.reg(o,int(v in U))[1] for v,o in zip(C['Q'],C['samples'])))
            Z=f.execute(I,b['word'],C['H'])['end'];wanted=i in b['covered']
            ck(Z==m.canon(I+((C['valid'],) if wanted else ())),
                'guard physically realizes exact finite support and preserves source')
            if C['valid'] in Z:active.append(i)
            mass=r.merge(mass,e.prep(I))
        ck(tuple(active)==b['covered'],'audited support cover is exact')
        out.append(dict(index=bi,support=b['support'],positive_rows=active))
    return dict(guards=len(out),background=len(C['background']),CWM=e.cw(mass),guards_result=out,**summary(C))

def four_query_boundary():
    """Sharp only for fixed individual occupancy reads plus positive tests."""
    V=tuple(range(1,7));full=m.canon(((1,2,3),(4,5,6)))
    witnesses=[]
    for n in range(4):
        for Q in combinations(V,n):
            T=tuple(sorted(set(Q)|set(v for v in V if v not in Q) )) # choose completion below
            T=tuple(sorted(Q+tuple(v for v in V if v not in Q)[:3-len(Q)]))
            single=(T,);H=set(full)|{T};word=[];S=[]
            for i,v in enumerate(Q):
                o=20+6*i;h,w,_=reader(v,o,60);H|=h;word+=w;S.append(o)
            A=f.execute(single,word,H)['end'];B=f.execute(full,word,H)['end']
            ck(tuple(p.read(A,o) for o in S)==tuple(p.read(B,o) for o in S),
               'at most three fixed queries can be hidden inside an accepted single triad')
            ck(set(m.used(A))<=set(m.used(B)),
               'positive subsequent templates cannot accept single yet reject full extension')
            witnesses.append(dict(queries=Q,single=T,decoded=tuple(p.read(A,o) for o in S)))
    sufficient=[]
    for Q in combinations(V,4):
        patterns=[]
        for T in combinations(V,3):
            H={T};W=[];S=[]
            for i,v in enumerate(Q):
                o=20+6*i;h,w,_=reader(v,o,60);H|=h;W+=w;S.append(o)
            Z=f.execute((T,),W,H)['end'];obs=tuple(p.read(Z,o) for o in S)
            ck(0 in obs,'every isolated single triad leaves a queried vacancy among four fixed ports')
            patterns.append(obs)
        sufficient.append(dict(queries=Q,accepted_patterns=sorted(set(patterns))))
    return dict(necessity_cases=len(witnesses),sufficiency_cases=15*20,witnesses=witnesses,four_sets=sufficient)

def boundaries():
    C=build();B=C['parent']['base'];rows=[]
    # Fix the exact false positive from the parent: added complementary event.
    row=next(x for x in C['rows'] if tuple(x['bits'])==(1,0,1,0,1,0))
    T=row['residue'];comp=tuple(v for v in range(49,55) if v not in T)
    code=m.canon(j.init(row['sorted'],C['inputs'])+(T,))
    invalid=m.canon(code+(comp,))
    old_result=f.execute(invalid,C['parent']['inverse'],C['parent']['H'])['end']
    guarded=f.execute(invalid,C['word'],C['H'],keep=True)
    ck(p.read(guarded['end'],C['status'])==0 and guarded['end']==m.canon(invalid+p.reg(C['status'],0)),
       'old double-triad false decoding is rejected without consuming source')
    rows.append(dict(name='complementary_extra_event',original=row,old_decoded=tuple(p.read(old_result,o) for o in C['inputs']),new=guarded))
    # Source-shape assumptions: six unary occupied events can spoof the same ports.
    spoof=m.canon(j.init(row['sorted'],C['inputs'])+
                  tuple((v,200+2*v,201+2*v) for v in T))
    H=C['H']|set(spoof)
    z=f.execute(spoof,C['word'],H,keep=True)
    ck(p.read(z['end'],C['status'])==1,'occupancy equality does not establish internal incidence')
    rows.append(dict(name='outside_domain_external_incidence',trace=z))
    # Authenticity is separate: another valid residue means another valid source.
    replacement=next(x for x in C['rows'] if x['weight']==row['weight'] and x['residue']!=T)
    change=[p.one(T[0]),p.add(replacement['residue'])]
    changed=f.execute(code,change,C['H'])['end']
    z=f.execute(changed,C['word'],C['H'],keep=True)
    ck(p.read(z['end'],C['status'])==1 and tuple(p.read(z['end'],o) for o in C['outputs'])==tuple(replacement['bits']),
       'structural validity does not authenticate historical code')
    rows.append(dict(name='valid_code_substitution',original_bits=row['bits'],restored_bits=replacement['bits'],trace=z))
    # Validate/use race: after certification, replace the one triad with another
    # whose raw supports lie outside the old recognized weight; no fault of gate.
    # Use weight 0, only T0 legal. Substitute a last-rank triple after validation.
    row0=next(x for x in C['rows'] if x['weight']==0)
    I=m.canon(j.init(row0['sorted'],C['inputs'])+(row0['residue'],))
    cut=next(s['end'] for s in C['stages'] if s['name']=='domain_certified')
    middle=f.execute(I,C['word'][:cut],C['H'])['end']
    target=(52,53,54)
    changed=f.execute(middle,[p.one(row0['residue'][0]),p.add(target)],C['H'])['end']
    z=f.execute(changed,C['word'][cut:],C['H'],keep=True)
    ck(p.read(z['end'],C['status'])==1,'stale validity can outlive its premises if source mutates')
    rows.append(dict(name='post_validation_mutation',cut=cut,input_bits=row0['sorted'],new_residue=target,
                     decoded=tuple(p.read(z['end'],o) for o in C['outputs']),trace=z))
    # A truly disjoint frame is preserved on an accepted case.
    frame=(301,302,303);H=C['H']|{frame}
    out=f.execute(m.canon(code+(frame,)),C['word'],H)['end']
    ck(frame in out and p.read(out,C['status'])==1,'disjoint frame retained')
    return dict(witnesses=rows,**summary(C))

def programs():
    C=build()
    return dict(summary=summary(C),word=C['word'],candidates=sorted(C['H']),guards=C['guards'],
                background=C['background'],decoder=C['decoder'],reads=C['reads'])

def main():
    q=argparse.ArgumentParser();q.add_argument('mode');q.add_argument('--part',type=int,default=0);q.add_argument('--out',required=True)
    args=q.parse_args();before=f.CALLS;uses=f.USES
    if args.mode=='programs':ans=programs()
    elif args.mode=='cases':ans=case_domain(4*args.part,4*args.part+4)
    elif args.mode=='audit':ans=audit()
    elif args.mode=='queries':ans=four_query_boundary()
    elif args.mode=='boundaries':ans=boundaries()
    else:raise ValueError(args.mode)
    result=dict(mode=args.mode,part=args.part,checks=CHECKS,uncached_kernel_calls=f.CALLS-before,
                transition_uses=f.USES-uses,result=ans)
    Path(args.out).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('mode','part','checks','uncached_kernel_calls','transition_uses')},ensure_ascii=False))
    if args.mode=='programs':print(json.dumps(ans['summary'],ensure_ascii=False))
if __name__=='__main__':main()
