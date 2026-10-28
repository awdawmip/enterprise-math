"""Domain-aware positive-contact compiler for the existing 20-code triad codec.

Compilation manipulates a finite specification and emits fixed reserve/release
words. Execution never selects a table row or a logical branch in Python.
All matching updates and positive history weights use the unchanged parent BRC.
"""
from __future__ import annotations
import argparse
import json
import sys
from itertools import combinations
from pathlib import Path
from functools import lru_cache

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_triad_origin as old
j,p,m,e,r,f=old.j,old.p,old.m,old.e,old.r,old.f
ONE,ZERO=old.ONE,old.ZERO
CHECKS=0


def ck(condition:bool, description:str)->None:
    global CHECKS
    CHECKS+=1
    if not condition: raise AssertionError(description)


def minimal_contacts(states, desired):
    """Finite compile-time supports, then deterministic greedy cover.

This is NOT an optimal set-cover claim and NOT a run-time oracle. A support is
accepted only if every allowed state containing it has the desired label.
All selected covers are checked again and physically executed in audit mode.
"""
    states=tuple(frozenset(s) for s in states);desired=frozenset(desired)
    candidates={}
    for U in states:
        elements=tuple(sorted(U))
        for size in range(len(elements)+1):
            for support in combinations(elements,size):
                if support not in candidates:
                    P=frozenset(support)
                    candidates[support]=frozenset(i for i,S in enumerate(states) if P<=S)
    good=sorted(((s,c) for s,c in candidates.items() if c and c<=desired),
                key=lambda item:(len(item[0]),item[0]))
    primes=[]
    for support,cover in good:
        if not any(frozenset(a)<=frozenset(support) for a,_ in primes):
            primes.append((support,cover))
    remaining=set(desired);chosen=[]
    while remaining:
        support,cover=min(primes,key=lambda item:(-len(item[1]&remaining),len(item[0]),item[0]))
        if not cover&remaining: raise ValueError('Observer not expressible by positive contacts')
        chosen.append((support,cover));remaining-=cover
    # Delete redundant selected terms, without claiming a minimum cover.
    for support,cover in tuple(reversed(chosen)):
        rest=set().union(*(c for s,c in chosen if s!=support))
        if desired<=rest: chosen=[item for item in chosen if item[0]!=support]
    actual=set().union(*(c for _,c in chosen))
    if actual!=desired: raise AssertionError('Incomplete or overbroad compiled cover')
    return tuple(chosen),len(primes)


@lru_cache(maxsize=1)
def compile_codec():
    base=old.codec();rows=base['rows'];inputs=base['inputs'];work=base['work']
    input_ports=[frozenset(old.literal_ports(row['bits'],inputs)) for row in rows]
    code_ports=[frozenset(base['weight_codes'][row['weight']]+row['residue']) for row in rows]
    sorted_ports=[frozenset(old.literal_ports((0,)*(6-w)+(1,)*w,inputs)) for w in range(7)]
    H=set().union(*(p.library(o) for o in range(0,48,6)))
    H.update(row['residue'] for row in rows);H.update(base['weight_codes'])
    F=[p.one(o+1) for o in inputs];forward_blocks=[]
    for target in sorted({row['residue'] for row in rows}):
        desired=frozenset(i for i,row in enumerate(rows) if row['residue']==target)
        cover,primes=minimal_contacts(input_ports,desired)
        for support,covered in cover:
            h,w=old.all_occupied_write(support,target,work);H|=h;F+=w
            forward_blocks.append(dict(support=support,target=target,covered=tuple(sorted(covered)),word=w))
    f_stages=[dict(name='captured_residue',end=len(F))]
    F += [p.add(p.reg(o,b)[0]) for o in inputs for b in (0,1)]
    f_stages.append(dict(name='restored_original_input',end=len(F)))
    # Preserve the original fixed sorting and packing suffix byte-for-byte.
    original_suffix=base['forward'][base['forward_stages'][2]['end']:]
    F+=original_suffix
    f_stages.append(dict(name='encoded',end=len(F)))

    G=[p.one(o+1) for o in inputs];weight_blocks=[]
    for weight,target in enumerate(base['weight_codes']):
        cover,primes=minimal_contacts(sorted_ports,frozenset((weight,)))
        for support,covered in cover:
            h,w=old.all_occupied_write(support,target,work);H|=h;G+=w
            weight_blocks.append(dict(support=support,target=target,covered=tuple(sorted(covered)),word=w))
    G += [p.one(o+5) for o in inputs]
    g_stages=[dict(name='weight_and_residue_only',end=len(G))]
    decoder_blocks=[]
    for bit,o in enumerate(inputs):
        desired=frozenset(i for i,row in enumerate(rows) if row['bits'][bit])
        cover,primes=minimal_contacts(code_ports,desired)
        bit_blocks=[]
        for support,covered in cover:
            target=p.reg(o,1)[1]
            h,w=old.all_occupied_write(support,target,work);H|=h;G+=w
            bit_blocks.append(dict(support=support,target=target,covered=tuple(sorted(covered)),word=w))
        decoder_blocks.append(dict(bit=bit,prime_supports=primes,blocks=bit_blocks))
    g_stages.append(dict(name='decoded_positive_tails',end=len(G)))
    for o in inputs:
        G += [p.add(p.reg(o,0)[1]),p.add(p.reg(o,0)[0]),p.add(p.reg(o,1)[0])]
    G += [p.one(v) for v in base['weight_members']+base['residue_members']]
    g_stages.append(dict(name='restored_and_clean',end=len(G)))
    for op in F+G:
        if op[0]=='reserve':H.add(op[1])
    return dict(base=base,rows=rows,inputs=inputs,work=work,H=H,forward=F,inverse=G,
                forward_stages=f_stages,inverse_stages=g_stages,
                forward_blocks=forward_blocks,weight_blocks=weight_blocks,decoder_blocks=decoder_blocks,
                input_ports=input_ports,code_ports=code_ports,sorted_ports=sorted_ports)


def summary():
    C=compile_codec();B=C['base']
    return dict(forward_calls=len(C['forward']),inverse_calls=len(C['inverse']),
                roundtrip_calls=len(C['forward']+C['inverse']),members=len(set().union(*C['H'])),
                candidate_events=len(C['H']),parent_candidate_events=len(B['H']),
                forward_guard_calls=sum(len(b['word']) for b in C['forward_blocks']),
                forward_guard_terms=len(C['forward_blocks']),
                weight_guard_calls=sum(len(b['word']) for b in C['weight_blocks']),
                decoder_guard_calls=sum(len(b['word']) for d in C['decoder_blocks'] for b in d['blocks']),
                decoder_terms=sum(len(d['blocks']) for d in C['decoder_blocks']),
                decoder_per_bit=[dict(bit=d['bit'],terms=len(d['blocks']),calls=sum(len(b['word']) for b in d['blocks'])) for d in C['decoder_blocks']],
                code_format_changed=False,search_is_optimal=False)


def nominal(weight):
    C=compile_codec();B=C['base'];outs=[];mass=ZERO
    for index,row in enumerate(C['rows']):
        if row['weight']!=weight:continue
        I=j.init(row['bits'],C['inputs']);K=I;at=0;stages=[]
        for stage in C['forward_stages']:
            K=f.execute(K,C['forward'][at:stage['end']],C['H'])['end'];at=stage['end']
            if stage['name']=='captured_residue':
                tails=tuple(p.reg(o,bit)[1] for o,bit in zip(C['inputs'],row['bits']))
                ck(K==m.canon(tails+(row['residue'],)),'capture preserves all input tails and exact original-format triad')
            elif stage['name']=='restored_original_input':
                ck(K==m.canon(I+(row['residue'],)),'source restored without any hidden code-dependent state')
            else:ck(K==old.expected(row,B),'new forward has exactly the old code format')
            stages.append(dict(stage=stage['name'],matching=K))
        encoded=K;at=0
        for stage in C['inverse_stages']:
            K=f.execute(K,C['inverse'][at:stage['end']],C['H'])['end'];at=stage['end']
            if stage['name']=='weight_and_residue_only':
                ck(K==m.canon((B['weight_codes'][weight],row['residue'])),'side-information compression is exact')
            elif stage['name']=='decoded_positive_tails':
                expected=(B['weight_codes'][weight],row['residue'])+tuple(p.reg(o,1)[1] for o,bit in zip(C['inputs'],row['bits']) if bit)
                ck(K==m.canon(expected),'all six observer covers write exactly their true tails')
            else:ck(K==I,'new inverse restores original addresses and clears every scratch state')
            stages.append(dict(stage=stage['name'],matching=K))
        mass=r.merge(mass,e.prep(I))
        outs.append(dict(index=index,input=row['bits'],encoded=encoded,end=K,stages=stages))
    return dict(weight=weight,cases=len(outs),mass=e.cw(mass),rows=outs,**summary())


def audit(which):
    """Physically execute every selected guard on its complete admissible domain."""
    C=compile_codec();B=C['base'];cases=[];mass=ZERO
    if which=='forward':
        blocks=C['forward_blocks']
        states=[m.canon(p.reg(o,bit)[1] for o,bit in zip(C['inputs'],row['bits'])) for row in C['rows']]
    elif which=='weight':
        blocks=C['weight_blocks']
        states=[m.canon(p.reg(o,bit)[1] for o,bit in zip(C['inputs'],(0,)*(6-w)+(1,)*w)) for w in range(7)]
    else:
        bit=int(which);blocks=C['decoder_blocks'][bit]['blocks']
        states=[m.canon((B['weight_codes'][row['weight']],row['residue'])) for row in C['rows']]
    for number,block in enumerate(blocks):
        observed=[]
        for index,J in enumerate(states):
            Z=f.execute(J,block['word'],C['H'])['end']
            active=index in block['covered']
            expected=m.canon(J+((block['target'],) if active else ()))
            ck(Z==expected,'actual conditional write agrees with finite contact certificate and preserves source')
            if block['target'] in Z: observed.append(index)
            mass=r.merge(mass,e.prep(J))
        ck(tuple(observed)==block['covered'],'complete physical cover matches the compile-time specification')
        cases.append(dict(number=number,support=block['support'],target=block['target'],positive_states=observed))
    return dict(which=which,guard_count=len(blocks),state_count=len(states),mass=e.cw(mass),guards=cases)


def image(weight):
    C=compile_codec();B=C['base'];_,carriers=e.catalog(list(combinations(B['residue_members'],3)))
    valid={row['residue'] for row in C['rows'] if row['weight']==weight};outs=[]
    for T in sorted(carriers):
        I=m.canon(j.init((0,)*(6-weight)+(1,)*weight,C['inputs'])+T)
        D=f.execute(I,C['inverse'],C['H'])['end'];bits=tuple(p.read(D,o) for o in C['inputs'])
        ck(all(v in(0,1) for v in bits) and D==j.init(bits,C['inputs']),'every enumerated carrier yields complete data and no scratch residue')
        R=f.execute(D,C['forward'],C['H'])['end']
        admissible=len(T)==1 and T[0] in valid
        ck((R==I)==admissible,'decode-encode fixed points equal the original code image')
        outs.append(dict(residue=T,admissible=admissible,decoded=bits,code_restored=R==I))
    return dict(weight=weight,cases=len(outs),valid=sum(z['admissible'] for z in outs),rows=outs)


def boundaries():
    C=compile_codec();B=C['base'];out={}
    # A two-contact predicate is sufficient for bit 6 over the exact 64-code domain.
    term=next(b for b in C['decoder_blocks'][5]['blocks'] if b['support']==(52,54))
    out['two_contact_rule']=dict(support=term['support'],covered_sources=[C['rows'][i] for i in term['covered']],word=term['word'])
    ck(len(term['covered'])==8,'two source members cover eight different legal code/source pairs')
    witnesses=[]
    for removed in term['support']:
        shortened=tuple(x for x in term['support'] if x!=removed)
        idx=next(i for i,row in enumerate(C['rows']) if not row['bits'][5] and set(shortened)<=C['code_ports'][i])
        row=C['rows'][idx];I=m.canon((B['weight_codes'][row['weight']],row['residue']))
        h,w=old.all_occupied_write(shortened,term['target'],C['work']);z=f.execute(I,w,C['H']|h,keep=True)
        ck(term['target'] in z['end'],'arbitrary removal of another contact causes a false positive')
        witnesses.append(dict(removed=removed,source=row,trace=z))
    out['necessary_contact_witnesses']=witnesses
    # A valid-domain optimization is not a total error detector.
    invalid=m.canon((B['weight_codes'][0],(49,52,54)))
    z=f.execute(invalid,term['word'],C['H'],keep=True)
    ck(term['target'] in z['end'],'invalid rank at weight zero is not rejected by positive observer terms')
    out['invalid_domain_shortcut']=z
    # Sorting is a premise of the short boundary recognizer.
    unsorted_bits=(1,0,0,0,0,0)
    I=j.init(unsorted_bits,C['inputs'])
    cut=C['inverse_stages'][0]['end']
    a=f.execute(I,C['inverse'][:cut],C['H'],keep=True)
    ck(a['end']!=m.canon((B['weight_codes'][1],)),'boundary weight reader is not a general Hamming weight counter')
    out['unsorted_input']=a
    # Actual old/new interchange in both directions, on four representative inputs.
    compat=[]
    for bits in ((0,)*6,(1,)*6,(1,0,1,0,1,0),(0,0,0,0,0,1)):
        I=j.init(bits,C['inputs']);row=next(x for x in C['rows'] if x['bits']==bits)
        old_code=f.execute(I,B['forward'],B['H'])['end']
        back=f.execute(old_code,C['inverse'],C['H'])['end']
        new_code=f.execute(I,C['forward'],C['H'])['end']
        old_back=f.execute(new_code,B['inverse'],B['H'])['end']
        ck(old_code==new_code==old.expected(row,B) and back==old_back==I,'old and new fixed programs are code-compatible')
        compat.append(dict(input=bits,code=new_code,new_decodes_old=back,old_decodes_new=old_back))
    out['compatibility']=compat
    # Nonintersecting frame is genuinely preserved.
    row=C['rows'][27];frame=(90,91,92);I=m.canon(j.init(row['bits'],C['inputs'])+(frame,))
    framed=f.execute(I,C['forward']+C['inverse'],C['H']|{frame})['end']
    ck(framed==I,'disjoint frame preserved through the complete round trip')
    out['frame']=dict(input=row['bits'],frame=frame,end=framed)
    # A valid code can still be replaced by another valid one without being detected.
    row=next(x for x in C['rows'] if x['bits']==(1,0,1,0,1,0))
    other=next(x for x in C['rows'] if x['weight']==row['weight'] and x['residue']!=row['residue'])
    encoded=f.execute(j.init(row['bits'],C['inputs']),C['forward'],C['H'])['end']
    flip=[p.one(row['residue'][0]),p.add(other['residue'])]
    changed=f.execute(encoded,flip,C['H'])['end'];decoded=f.execute(changed,C['inverse'],C['H'])['end']
    ck(decoded==j.init(other['bits'],C['inputs']),'legal code replacement still changes historical origin')
    out['valid_substitution']=dict(original=row['bits'],replacement=other['bits'],changed_code=changed,decoded=decoded)
    # Positive occupied-contact observers cannot reject every extension of a true state.
    J=((1,2,3),);K=m.canon(J+((4,5,6),));target=(10,11,12);pairs=[]
    for size in range(4):
        for support in combinations((1,2,3),size):
            h,w=old.all_occupied_write(support,target,13)
            x=f.execute(J,w,h|set(J))['end'];y=f.execute(K,w,h|set(K))['end']
            ck(target in x and target in y,'positive-contact predicate stays true under source occupancy extension')
            pairs.append(dict(support=support,on_J=target in x,on_K=target in y))
    out['monotone_boundary']=pairs
    # Arbitrary new occupied ports may impersonate the asserted source.
    foreign=m.canon(((52,90,91),(54,92,93)))
    z=f.execute(foreign,term['word'],C['H']|set(foreign),keep=True)
    ck(term['target'] in z['end'],'occupancy predicate is not evidence provenance authentication')
    out['foreign_occupancy']=z
    return out


def local_faults():
    # New two-contact block: replay exact inherited primitives, global omission budget.
    C=compile_codec();target=p.reg(30,1)[1];support=(52,54)
    h,w=old.all_occupied_write(support,target,55)
    markers=((52,80,81),(54,82,83));H=h|set(markers)
    results=[]
    for bits in ((0,0),(0,1),(1,0),(1,1)):
        I=m.canon(marker for b,marker in zip(bits,markers) if b)
        expected=m.canon(I+((target,) if all(bits) else ()))
        for budget in (1,2):
            protected=[op for op in w for _ in range(budget+1)];mass=ZERO;histories=0
            for missing in range(budget+1):
                for omitted in combinations(range(len(protected)),missing):
                    z=f.execute(I,protected,H,omitted=omitted)
                    ck(z['end']==expected,'protected local block has exact full endpoint after budgeted omissions')
                    mass=r.merge(mass,e.prep(z['end']));histories+=1
            results.append(dict(bits=bits,budget=budget,calls=len(protected),histories=histories,mass=e.cw(mass)))
    # No full-codec fault guarantee follows from this local result.
    bad=f.execute((),w,H,keep=True,omitted=(0,1))
    ck(target in bad['end'],'omitting all source contacts can falsely write a positive tail')
    return dict(families=results,unprotected=bad)


def main():
    q=argparse.ArgumentParser();q.add_argument('mode');q.add_argument('--part',default='0');q.add_argument('--out',required=True)
    a=q.parse_args();before=f.CALLS;uses=f.USES
    if a.mode=='nominal':ans=nominal(int(a.part))
    elif a.mode=='audit':ans=audit(a.part)
    elif a.mode=='image':ans=image(int(a.part))
    elif a.mode=='boundaries':ans=boundaries()
    elif a.mode=='faults':ans=local_faults()
    elif a.mode=='programs':
        C=compile_codec();ans=dict(summary=summary(),forward=C['forward'],inverse=C['inverse'],candidates=sorted(C['H']),
         forward_blocks=C['forward_blocks'],weight_blocks=C['weight_blocks'],decoder_blocks=C['decoder_blocks'],
         forward_stages=C['forward_stages'],inverse_stages=C['inverse_stages'])
    else:raise ValueError(a.mode)
    output=dict(mode=a.mode,part=a.part,checks=CHECKS,uncached_kernel_calls=f.CALLS-before,
                transition_uses=f.USES-uses,result=ans)
    Path(a.out).write_text(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ('mode','part','checks','uncached_kernel_calls','transition_uses')},ensure_ascii=False))

if __name__=='__main__':main()
