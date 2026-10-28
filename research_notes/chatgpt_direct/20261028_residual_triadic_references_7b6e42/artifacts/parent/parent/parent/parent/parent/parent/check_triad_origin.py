"""Fixed triadic source codec: a single triple on six members, with executable inverse.

Finite lookup tables are compiled into *fixed* reserve/release sequences. No run
selects a row in Python. All scientific matching updates call the inherited,
unchanged kernel; history composition and merges use its positive CWM.
"""
from __future__ import annotations
import argparse
import json
import sys
from itertools import combinations, product
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_compact as old
j,p,m,e,r,f=old.j,old.p,old.m,old.e,old.r,old.f
ONE,ZERO=old.ONE,old.ZERO
CHECKS=0

def ck(x,label):
    global CHECKS
    CHECKS+=1
    if not x:raise AssertionError(label)


def triad(xs):return tuple(sorted(xs))


def all_occupied_write(ports,target,work):
    """Write target iff all ports occupied, for disjoint ports/target/work.

All probes compete for target[0] and work. At least one empty source port
blocks the target; a preoccupied target already blocks itself. Afterward the
source is unchanged and the one possible probe is cleaned via private work.
"""
    target=triad(target)
    if set(ports)&set(target) or work in set(ports)|set(target):
        raise ValueError('Probe/read ports must be disjoint from target and work')
    probes=[triad((v,target[0],work)) for v in ports]
    return set(probes)|{target},[p.add(q) for q in probes]+[p.add(target),p.one(work)]


def literal_ports(bits,offsets):
    # After the header is removed, tail0 occupies +4 and tail1 occupies +3.
    return [o+(3 if bit else 4) for bit,o in zip(bits,offsets)]


def rows_for_six():
    """A finite codebook specification, not a run-time rank oracle.

Within each weight w, enumerate subsets of {0..5} in tuple-lex order. The row
with ordinal j uses the jth 3-subset of residue members 49..54. All 64 rows
are compiled and executed for every input, in the same order.
"""
    triples=list(combinations(range(49,55),3))
    rows=[]
    for w in range(7):
        for ordinal,S in enumerate(combinations(range(6),w)):
            bits=tuple(int(i in S) for i in range(6))
            rows.append(dict(weight=w,ordinal=ordinal,ones=S,bits=bits,
                             sorted=(0,)*(6-w)+(1,)*w,residue=triples[ordinal]))
    return rows


def codec():
    inputs=[6*i for i in range(6)]
    residue=tuple(range(49,55));work=55
    rows=rows_for_six()
    H=set().union(*(p.library(o) for o in range(0,48,6)))
    F=[p.one(o+1) for o in inputs]
    f_stages=[dict(name='open_inputs',end=len(F))]
    for row in rows:
        h,w=all_occupied_write(literal_ports(row['bits'],inputs),row['residue'],work)
        H|=h;F+=w
    f_stages.append(dict(name='write_single_triad',end=len(F)))
    F += [p.add(p.reg(o,b)[0]) for o in inputs for b in (0,1)]
    f_stages.append(dict(name='restore_inputs',end=len(F)))
    h,sw,ss,wires,free=j.network(6);H|=h;F+=sw
    f_stages.append(dict(name='sort',end=len(F),wires=list(wires)))
    # Move the fixed final logical-wire layout back to the six fixed addresses.
    # The compile-time slot map depends ONLY on the fixed comparator network.
    wires=list(wires);free=set(free);moves=[]
    while wires!=inputs:
        candidates=[i for i in range(6) if wires[i]!=inputs[i] and inputs[i] in free]
        if candidates:
            i=candidates[0];src=wires[i];dst=inputs[i]
        else:
            i=next(i for i in range(6) if wires[i]!=inputs[i]);src=wires[i];dst=min(free)
        h,w=old.transfer(src,dst,work);H|=h;F+=w
        moves.append((src,dst));free.remove(dst);free.add(src);wires[i]=dst
    ck(free=={36,42},'fixed sort packing leaves the two scratch registers free')
    f_stages.append(dict(name='pack_sorted_addresses',end=len(F),moves=moves))

    # Decode side information into one of seven triples on five scratch members.
    # This frees the six full sorted registers before recreating original order.
    weight_members=tuple(range(37,42))
    weight_codes=list(combinations(weight_members,3))[:7]
    flag=(43,44,45)
    G=[p.one(o+1) for o in inputs]
    g_stages=[dict(name='open_sorted',end=len(G))]
    for weight,T in enumerate(weight_codes):
        pattern=(0,)*(6-weight)+(1,)*weight
        h,w=all_occupied_write(literal_ports(pattern,inputs),T,work)
        H|=h;G+=w
    G += [p.one(o+5) for o in inputs]
    g_stages.append(dict(name='weight_relation_and_consumed_sorted',end=len(G)))
    for idx,row in enumerate(rows):
        ports=tuple(weight_codes[row['weight']])+tuple(row['residue'])
        h,w=all_occupied_write(ports,flag,work);H|=h;G+=w
        # Only 1-tails are conditionally formed. Default 0 is filled AFTER all
        # 64 mutually exclusive rows. This is a compile-time constant choice.
        for bit,o in zip(row['bits'],inputs):
            if bit:
                target=p.reg(o,1)[1]
                h,w=all_occupied_write((flag[0],),target,work)
                H|=h;G+=w
        G.append(p.one(flag[1]))
    g_stages.append(dict(name='decoded_positive_tails',end=len(G)))
    for o in inputs:
        G += [p.add(p.reg(o,0)[1]),p.add(p.reg(o,0)[0]),p.add(p.reg(o,1)[0])]
    G += [p.one(v) for v in weight_members+residue]
    g_stages.append(dict(name='complete_and_clean',end=len(G)))
    return dict(H=H,forward=F,inverse=G,inputs=inputs,residue_members=residue,
                weight_members=weight_members,weight_codes=weight_codes,flag=flag,
                work=work,rows=rows,forward_stages=f_stages,inverse_stages=g_stages)


def expected(row,C):return m.canon(j.init(row['sorted'],C['inputs'])+(row['residue'],))


def roundtrip_chunk(weight:int):
    C=codec();H,F,G=C['H'],C['forward'],C['inverse'];rows=[];mass=ZERO
    ck(len(set().union(*H))==55,'actual total declared member inventory is 55')
    for row in C['rows']:
        if row['weight']!=weight:continue
        initial=j.init(row['bits'],C['inputs']);K=initial;at=0
        forward_boundaries=[]
        for s in C['forward_stages']:
            z=f.execute(K,F[at:s['end']],H);K=z['end'];at=s['end']
            if s['name']=='write_single_triad':
                ck(tuple(h for h in K if set(h)<=set(C['residue_members']))==(row['residue'],),
                   'all 64 row programs leave exactly the correct one triple')
            if s['name']=='restore_inputs':
                ck(K==m.canon(initial+(row['residue'],)),'residual capture restores all six original inputs')
            forward_boundaries.append(dict(stage=s['name'],matching=K))
        ck(K==expected(row,C),'full forward endpoint is fixed sorted registers plus one triad only')
        ck(j.sq_observer(row['bits'])==j.sq_observer(row['sorted']),'data-square CWM preserved at boundary')
        encoded=K;at=0;inverse_boundaries=[]
        for s in C['inverse_stages']:
            z=f.execute(K,G[at:s['end']],H);K=z['end'];at=s['end']
            if s['name']=='weight_relation_and_consumed_sorted':
                want=m.canon((row['residue'],C['weight_codes'][weight]))
                ck(K==want,'sorted side information becomes one weight triple; no hidden registers remain')
            if s['name']=='decoded_positive_tails':
                want=m.canon((row['residue'],C['weight_codes'][weight])+
                     tuple(p.reg(o,1)[1] for bit,o in zip(row['bits'],C['inputs']) if bit))
                ck(K==want,'only the matching row writes actual positive tails')
            inverse_boundaries.append(dict(stage=s['name'],matching=K))
        ck(K==initial,'exact original values and addresses recovered; all scratch and residue blank')
        mass=r.merge(mass,e.prep(initial))
        rows.append(dict(input=row['bits'],ordinal=row['ordinal'],residue=row['residue'],encoded=encoded,
                         restored=K,forward=forward_boundaries,inverse=inverse_boundaries))
    return dict(weight=weight,cases=len(rows),CWM=e.cw(mass),forward_calls=len(F),inverse_calls=len(G),
                roundtrip_calls=len(F+G),candidate_events=len(H),members=55,rows=rows)


def image_chunk(weight:int):
    C=codec();H,F,G=C['H'],C['forward'],C['inverse'];outs=[]
    source_rows=[x for x in C['rows'] if x['weight']==weight]
    valid_triples={row['residue'] for row in source_rows}
    S=(0,)*(6-weight)+(1,)*weight
    _,domain=e.catalog(list(combinations(C['residue_members'],3)))
    for R in sorted(domain):
        K=m.canon(j.init(S,C['inputs'])+R);rest=f.execute(K,G,H)['end']
        bits=tuple(p.read(rest,o) for o in C['inputs'])
        ck(all(v in(0,1) for v in bits),'decoder returns complete Boolean output on the entire matching carrier')
        rebuilt=f.execute(rest,F,H)['end']
        valid=len(R)==1 and R[0] in valid_triples
        ck((rebuilt==K)==valid,'exact image on every sorted word times every carrier matching')
        ck(rest==j.init(bits,C['inputs']),'decoder fully cleans all examined valid/invalid prepared codes')
        outs.append(dict(residue=R,valid=valid,decoded=bits,roundtrip_equal=rebuilt==K))
    return dict(weight=weight,cases=len(outs),valid=len(source_rows),rows=outs)


def local_tests():
    # Exhaustive clean predicate: each port occupied by its own stable event or empty.
    ports=(1,4,7);target=(11,12,13);work=14
    H,W=all_occupied_write(ports,target,work)
    markers=((1,2,3),(4,5,6),(7,8,9));H|=set(markers)
    test=[]
    for bits in product((0,1),repeat=3):
        J=m.canon(h for bit,h in zip(bits,markers) if bit)
        z=f.execute(J,W,H,keep=True)
        expected_state=m.canon(J+((target,) if all(bits) else ()))
        ck(z['end']==expected_state,'all-occupied conditional write is exact and source preserving')
        test.append(dict(bits=bits,trace=z))
    # Exhaustive catalog: on <=5 members all possible partial triple matchings.
    inventories=[]
    for size in range(3,7):
        triples=list(combinations(range(1,size+1),3));_,domain=e.catalog(triples)
        ck(len(domain)==({3:2,4:5,5:11,6:31}[size]),'exact carrier matching-state capacity')
        inventories.append(dict(members=size,matching_states=len(domain),
                                CWM=e.cw(f.total(domain.values()))))
    C=codec();j3=[x for x in C['rows'] if x['weight']==3]
    ck(len({x['residue'] for x in j3})==20,'all 20 one-triple states needed in the largest fiber')
    residue_squares=[]
    for T in combinations(C['residue_members'],3):
        observed=tuple(int(v in T) for v in C['residue_members'])
        q=j.sq_observer(observed)
        ck(q==f.total((ONE,ONE,ONE)),'all twenty residue configurations have the same BRC square statistic')
        residue_squares.append(dict(triad=T,occupancy=observed,square_CWM=e.cw(q)))
    # Fails if a port is independently occupied by an undeclared-as-signal event.
    I=m.canon(((1,2,3),(4,5,6),(7,20,21)))
    h=H|{(7,20,21)};z=f.execute(I,W,h,keep=True)
    ck(target in z['end'],'occupancy provenance cannot be inferred from the predicate alone')
    # A query involving one candidate port: omission of the probe yields false write.
    h,w=all_occupied_write((1,),(11,12,13),14)
    bad=f.execute((),w,h,keep=True,omitted=(0,))
    ck(target in bad['end'],'unprotected missed probe can create false row match')
    return dict(predicate_cases=test,carrier_capacities=inventories,residue_squares=residue_squares,omission=bad,
                unrelated_occupancy=z,program_lengths=dict(forward=len(C['forward']),inverse=len(C['inverse'])),
                stages=C['forward_stages'],members=len(set().union(*C['H'])))


def failures_and_migration():
    C=codec();H,F,G=C['H'],C['forward'],C['inverse'];rows=C['rows'];d=[]
    row=next(x for x in rows if x['bits']==(1,0,1,0,1,0))
    K=f.execute(j.init(row['bits'],C['inputs']),F,H)['end']
    # Two distinct legitimate single-triad codes at the same sorted side information.
    alt=next(x for x in rows if x['weight']==3 and x['residue']!=row['residue'])
    change=[p.one(row['residue'][0]),p.add(alt['residue'])]
    altered=f.execute(K,change,H,True)
    restored=f.execute(altered['end'],G,H)['end']
    ck(restored==j.init(alt['bits'],C['inputs']),'legal triad substitution changes recovered origin')
    ck(j.sq_observer(row['bits'])==j.sq_observer(alt['bits']),'same square statistic does not authenticate source')
    d.append(dict(kind='legal_origin_substitution',original=row['bits'],replacement=alt['bits'],change=altered,recovered=restored))
    # One additional legal disjoint triple breaks the ONE-triple code type.
    complement=triad(set(C['residue_members'])-set(row['residue']))
    double=f.execute(K,[p.add(complement)],H,True)
    doubled_result=f.execute(double['end'],G,H)['end']
    ck(doubled_result==j.init((1,1,1,1,1,1),C['inputs']),
       'two-triple corrupted carrier makes every middle-weight row look matched')
    d.append(dict(kind='two_triples_are_not_one_code',original=row['bits'],added=complement,
                  change=double,recovered=doubled_result))
    # Missing source side-information: weights 0 and 6 reuse ordinal-0 residue.
    R0=next(x for x in rows if x['weight']==0);R6=next(x for x in rows if x['weight']==6)
    A=expected(R0,C);B=expected(R6,C);clear=sum((p.clear_word(o) for o in C['inputs']),[])
    aa=f.execute(A,clear,H)['end'];bb=f.execute(B,clear,H)['end']
    ck(aa==bb,'residue alone is not a six-bit source code')
    d.append(dict(kind='side_information_required',after_zero=aa,after_one=bb))
    # Preserve an extra disjoint frame throughout one nontrivial roundtrip.
    frame=(1001,1002,1003);J=m.canon(j.init(row['bits'],C['inputs'])+(frame,))
    keep=f.execute(J,F+G,H|{frame})
    ck(keep['end']==J,'unrelated disjoint frame preserved')
    # Migration from prior actual 5-bit code -> actual prior inverse -> new forward.
    P=old.codec(6);migration=[]
    for bits in ((0,0,0,0,0,0),(1,0,1,0,1,0),(0,0,0,0,0,1),(1,1,1,1,1,1)):
        J=j.init(bits,C['inputs']);prev=f.execute(J,P['forward'],P['H'])['end']
        recovered=f.execute(prev,P['inverse'],P['H'])['end'];ck(recovered==J,'actual parent inverse before migration')
        encoded=f.execute(recovered,F,H)['end'];again=f.execute(encoded,G,H)['end'];ck(again==J,'migration keeps source')
        migration.append(dict(bits=bits,parent_endpoint=prev,new_endpoint=encoded,restored=again))
    return dict(failures=d,disjoint_frame=keep,migration=migration,
                migration_calls=len(P['inverse'])+len(F))


def protected_predicate():
    ports=(1,4,7);target=(11,12,13);work=14
    markers=((1,2,3),(4,5,6),(7,8,9))
    H,W=all_occupied_write(ports,target,work);H|=set(markers);families=[]
    for bits in product((0,1),repeat=3):
        J=m.canon(h for bit,h in zip(bits,markers) if bit)
        expected=m.canon(J+((target,) if all(bits) else ()))
        for budget in (1,2):
            word=[op for op in W for _ in range(budget+1)]
            states={(J,0):e.prep(J)}
            for op in word:
                nxt={}
                for (K,used),mass in states.items():
                    L,_=f.step(K,op,H)
                    f.put(nxt,(L,used),r.serial(mass,ONE))
                    if used<budget:f.put(nxt,(K,used+1),r.serial(mass,ONE))
                states=nxt
            layers={}
            for (K,used),mass in states.items():
                ck(K==expected,'protected conditional writer has exact source-preserving result')
                f.put(layers,used,mass)
            # Independent original-CWM layer count, without any matching state.
            positional={0:ONE}
            for _ in word:
                nxt={}
                for used,mass in positional.items():
                    f.put(nxt,used,r.serial(mass,ONE))
                    if used<budget:f.put(nxt,used+1,r.serial(mass,ONE))
                positional=nxt
            ck(layers==positional,'every retained/omitted history counted with original positive CWM')
            families.append(dict(bits=bits,budget=budget,commands=len(word),
                layers=[dict(omitted=u,CWM=e.cw(v)) for u,v in sorted(layers.items())]))
    return dict(families=families,whole_codec_fault_claim=False)


def clean_programs(C):
    return {k:(sorted(v) if k=='H' else v) for k,v in C.items()}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=('local','roundtrip','image','boundaries','faults','programs'))
    parser.add_argument('--weight',type=int,default=3);parser.add_argument('--output',required=True)
    args=parser.parse_args()
    if args.mode=='local':out=local_tests()
    elif args.mode=='roundtrip':out=roundtrip_chunk(args.weight)
    elif args.mode=='image':out=image_chunk(args.weight)
    elif args.mode=='boundaries':out=failures_and_migration()
    elif args.mode=='faults':out=protected_predicate()
    else:out=clean_programs(codec())
    if args.mode!='programs':
        out=dict(mode=args.mode,checks=CHECKS,uncached_kernel_calls=f.CALLS,
                 transition_uses=f.USES,result=out)
    Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('result','H','forward','inverse','rows')},ensure_ascii=False)[:1800])

if __name__=='__main__':main()
