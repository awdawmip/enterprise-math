"""Contention is missing local evidence, not a negative source observation.

All model transitions use the pinned original three-member reservation kernel.
CWM handles path composition/recoalescence. No parent main is executed.
The model is conditional: stable signed source, private worker markers, faithful
atomic primitive calls, and a join before reducing stable, complete flags.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import parent_adapter as a
p, e, m, r = a.p, a.e, a.m, a.r
ONE, ZERO = a.ONE, a.ZERO
CHECKS = CALLS = USES = 0
CACHE = {}


def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


def step(J, op, H):
    global CALLS, USES
    USES += 1
    key = (J, op)
    if op[0] == 'reserve' and op[1] not in H:
        raise ValueError('operation not in the declared event library')
    if key not in CACHE:
        K, _, ok = e.step(J, op, H)
        CALLS += 1
        CACHE[key] = K, ok
    return CACHE[key]


def put(d, key, mass):
    d[key] = r.merge(d.get(key, ZERO), mass)


def total(d):
    mass = ZERO
    for value in d.values():
        mass = r.merge(mass, value)
    return mass


def repeat(word, count):
    return [op for op in word for _ in range(count)]


def flag(i):
    return 30 + 20*i


def worker(i, faults=0, contacts=1):
    o = flag(i)
    bridge = (7, o+8, o+9)
    H, read_word, probe = a.reader(o+9, o, o+7)
    H |= {bridge}
    word = [p.add(bridge)] * contacts
    word += repeat(read_word + [p.one(o+8)], faults+1)
    return H, word, bridge, probe


def protected(J, K):
    return all((h in J) == (h in K) for h in (a.E, a.P, a.HP, a.HN))


def execute(J, word, H, omitted=(), keep=True):
    start = J
    omitted = frozenset(omitted)
    mass = e.prep(J)
    rows = []
    for index, op in enumerate(word):
        old = J
        J, ok = (J, None) if index in omitted else step(J, op, H)
        mass = r.serial(mass, ONE)
        if keep:
            rows.append(dict(slot=index+1, operation=op, invoked=index not in omitted,
                             success=ok, before=old, after=J))
    return dict(start=start, end=J, commands=len(word), CWM=e.cw(mass), trace=rows)


def positional_mass(lengths, opening, faults):
    """Separate CWM on positions only: same shuffles and omission alternatives."""
    d = {(tuple(0 for _ in lengths), 0): ONE}
    for _ in range(opening):
        q = {}
        for (pcs, b), mass in d.items():
            put(q, (pcs, b), r.serial(mass, ONE))
            if b < faults:
                put(q, (pcs, b+1), r.serial(mass, ONE))
        d = q
    for _ in range(sum(lengths)):
        q = {}
        for (pcs, b), mass in d.items():
            for i, j in enumerate(pcs):
                if j == lengths[i]:
                    continue
                np = list(pcs); np[i] += 1; np = tuple(np)
                put(q, (np, b), r.serial(mass, ONE))
                if b < faults:
                    put(q, (np, b+1), r.serial(mass, ONE))
        d = q
    out = {}
    for (pcs, b), mass in d.items():
        put(out, b, mass)
    return out


def shuffles(J, k, faults=0, contacts=None):
    contacts = tuple(contacts or [1]*k)
    specs = [worker(i, faults, contacts[i]) for i in range(k)]
    H = a.SOURCE_H | set().union(*(x[0] for x in specs))
    words = [x[1] for x in specs]
    lengths = tuple(map(len, words))
    opening = faults+1
    d = {((0,)*k, J, 0, 0): e.prep(J)}
    for op in [p.one(4)] * opening:
        q = {}
        for (pcs, K, b, wins), mass in d.items():
            L, _ = step(K, op, H)
            put(q, (pcs, L, b, wins), r.serial(mass, ONE))
            if b < faults:
                put(q, (pcs, K, b+1, wins), r.serial(mass, ONE))
        d = q
    peak = len(d)
    for _ in range(sum(lengths)):
        q = {}
        for (pcs, K, b, wins), mass in d.items():
            for i, j in enumerate(pcs):
                if j == lengths[i]:
                    continue
                np = list(pcs); np[i] += 1; np = tuple(np)
                L, ok = step(K, words[i][j], H)
                check(protected(J, L), 'original evidence and P stay unchanged')
                nw = wins | ((1 << i) if j < contacts[i] and ok else 0)
                put(q, (np, L, b, nw), r.serial(mass, ONE))
                if b < faults:
                    put(q, (np, K, b+1, wins), r.serial(mass, ONE))
        d = q
        peak = max(peak, len(d))
    law = {}; layers = {}; terminals = {}
    for (pcs, K, b, wins), mass in d.items():
        bits = tuple(p.read(K, flag(i)) for i in range(k))
        check(bits == tuple(int(bool(wins & (1 << i))) for i in range(k)),
              'private complete flag equals actual own bridge success')
        expected = m.canon(a.norm(J) + tuple(h for i, bit in enumerate(bits) for h in p.reg(flag(i), bit)))
        check(K == expected, 'exact final state: normalized source, flags, no work probes')
        if a.signed(J) == 0:
            check(not any(bits), 'negative tail blocks all source contacts')
        elif faults < sum(contacts):
            check(any(bits), 'first unomitted contact succeeds on positive source')
        put(law, (b, bits), mass); put(layers, b, mass); terminals[bits] = K
    check(layers == positional_mass(lengths, opening, faults),
          'full CWM history mass matches independent position-and-omission transport')
    return dict(initial=J, workers=k, faults=faults, contacts=contacts,
                commands=opening+sum(lengths), peak_states=peak,
                layers=[dict(omissions=b, CWM=e.cw(w)) for b, w in sorted(layers.items())],
                outcomes=[dict(omissions=b, flags=bits, CWM=e.cw(w)) for (b,bits),w in sorted(law.items())]), terminals


def majority(inputs, output, scratch=(1000,1010,1020), ancilla=1030):
    H0, W0, _ = p.majority_program()
    addresses = {}
    for old, new in zip((0,6,12,18,24,30,36), (*inputs, *scratch, output)):
        addresses.update({old+i: new+i for i in range(1,7)})
    addresses[43] = ancilla
    H = {tuple(sorted(addresses[x] for x in h)) for h in H0}
    W = [(kind, addresses[arg]) if kind == 'release' else
         p.add(addresses[x] for x in arg) for kind,arg in W0]
    return H, W


def reducer(k, faults=0):
    if k < 2:
        H, W = p.copy_program(flag(0), 400, 1030)
        return H | p.library(300), repeat(W, faults+1)
    H = set(p.library(300)); W = []; current = flag(0); intermediates=[]
    for i in range(1,k):
        output = 400 if i == k-1 else 500+10*(i-1)
        h,w = majority((current, flag(i), 300), output)
        H |= h; W += w
        if output != 400:
            intermediates.append(output)
        current = output
    for o in intermediates:
        W += p.clear_word(o)
    return H, repeat(W, faults+1)


def reduce_trace(J, k, keep=True):
    H,W = reducer(k)
    H |= a.SOURCE_H | set().union(*(worker(i)[0] for i in range(k)))
    start = m.canon(J+p.reg(300,1))
    z = execute(start, W, H, keep=keep)
    expected_bit = int(any(p.read(J, flag(i)) for i in range(k)))
    check(z['end'] == m.canon(start+p.reg(400,expected_bit)), 'original OR gates reduce flags and clear scratch')
    return z


def join_words(k, faults=0, contacts=None, schedule='overlap'):
    contacts = tuple(contacts or [1]*k)
    specs = [worker(i, faults, contacts[i]) for i in range(k)]
    H = a.SOURCE_H | set().union(*(x[0] for x in specs))
    prefix=[p.one(4)]*(faults+1)
    # Each process contacts first, then locally completes; no source-dependent choice.
    if schedule == 'overlap':
        W = prefix + [op for i in range(k) for op in specs[i][1][:contacts[i]]]
        W += [op for i in range(k) for op in specs[i][1][contacts[i]:]]
    else:
        W = prefix + [op for spec in specs for op in spec[1]]
    h,reduce_word = reducer(k,faults); H |= h
    return H, W+reduce_word, len(W)


def serial_omissions(J,k,faults,schedule):
    H,W,cut = join_words(k,faults,schedule=schedule)
    start = m.canon(J+p.reg(300,1))
    d={(start,0):e.prep(start)}
    for op in W:
        q={}
        for (K,b),mass in d.items():
            L,_=step(K,op,H)
            check(protected(J,L),'protected source throughout complete reduction')
            put(q,(L,b),r.serial(mass,ONE))
            if b<faults:put(q,(K,b+1),r.serial(mass,ONE))
        d=q
    layers={};law={}
    for (K,b),mass in d.items():
        value=p.read(K,400)
        check(value==a.signed(J),'shared global omission budget preserves final reduced value')
        bits=tuple(p.read(K,flag(i)) for i in range(k))
        expected=m.canon(a.norm(J)+p.reg(300,1)+p.reg(400,value)+tuple(h for i,v in enumerate(bits) for h in p.reg(flag(i),v)))
        check(K==expected,'joined result preserves all flags and original residual, clears all other work')
        put(layers,b,mass);put(law,(b,bits),mass)
    check(layers==a.layers(len(W),faults),'end-to-end omission histories are all retained')
    return dict(initial=J,k=k,faults=faults,schedule=schedule,commands=len(W),
                layers=[dict(omissions=b,CWM=e.cw(w)) for b,w in sorted(layers.items())],
                law=[dict(omissions=b,flags=bits,CWM=e.cw(w)) for (b,bits),w in sorted(law.items())])


def examples():
    out={}
    for k in (2,3,6):
        H,W,cut=join_words(k)
        for name,J in [('positive',(a.HP,)),('dirty_negative',m.canon((a.HN,a.P)))]:
            z=execute(m.canon(J+p.reg(300,1)),W,H)
            check(p.read(z['end'],400)==a.signed(J),'arbitrary-overlap representative reduces to correct source')
            check(tuple(p.read(z['end'],flag(i)) for i in range(k)) == ((1,)+(0,)*(k-1) if name=='positive' else (0,)*k),
                  'overlap produces one real winner, not k source-value measurements')
            out[f'{k}_{name}']=z
    # Every nonzero flag vector is feasible on the same positive source.
    realizations=[]
    for k in range(1,7):
        specs=[worker(i) for i in range(k)]
        HH=a.SOURCE_H|set().union(*(x[0] for x in specs))
        for mask in range(1,1<<k):
            winners=[i for i in range(k) if mask&(1<<i)]
            losers=[i for i in range(k) if not mask&(1<<i)]
            leader=winners[0]
            word=[p.one(4),specs[leader][1][0]]
            word += [op for i in losers for op in specs[i][1]]
            word += specs[leader][1][1:]
            word += [op for i in winners[1:] for op in specs[i][1]]
            zz=execute((a.HP,),word,HH,keep=False)
            bits=tuple(p.read(zz['end'],flag(i)) for i in range(k))
            check(bits==tuple(int(bool(mask&(1<<i))) for i in range(k)),
                  'every nonzero flag vector is realizable by a legal finite shuffle')
            realizations.append(dict(k=k,flags=bits,commands=word,end=zz['end']))
    out['all_nonzero_realizations']=realizations
    # Restore a known-full source only after every private bridge has been cleared.
    restored=[]
    for k in (2,3,6):
        HH,word,cut=join_words(k)
        for bit in (0,1):
            J=p.reg(3,bit)
            start=m.canon(J+p.reg(300,1))
            zz=execute(start,word[:cut]+[p.add(a.A),p.add(a.B)]+word[cut:],HH)
            check(a.source(zz['end'])==J and p.read(zz['end'],400)==bit,
                  'source restoration after join commutes with later private reduction')
            idle=[len(set(range(4,10))-m.used(row['after'])) for row in zz['trace']]
            check(max(idle)==3,'original six-member source exposure stays three')
            restored.append(dict(k=k,source_bit=bit,source_exposure_peak=max(idle),run=zz))
    out['restored_source']=restored
    # All contacts omitted: no record-only decoder can distinguish normalized +/- sources.
    k=2;H,W,cut=join_words(k,2);omitted=(3,4)
    fail=execute(m.canon((a.HP,)+p.reg(300,1)),W,H,omitted)
    check(p.read(fail['end'],400)==0,'two omitted acquisition attempts defeat two workers')
    out['omission_boundary']=fail
    paired=execute(m.canon((a.HN,)+p.reg(300,1)),W,H,omitted,keep=False)
    check(m.canon(h for h in fail['end'] if h not in a.SOURCE_H)==m.canon(h for h in paired['end'] if h not in a.SOURCE_H),
          'all-contact omission has identical auxiliary outputs for opposite signed sources')
    out['omission_boundary_negative_control']=paired
    # Source-to-marker contact does NOT use e.step success as a control input.
    # Failing to protect the private physical reader itself reintroduces false evidence.
    H,W,cut=join_words(2)
    z=execute(m.canon((a.HN,)+p.reg(300,1)),W,H,(3,))
    check(p.read(z['end'],400)==1,'omitting private marker probe creates a false positive when unprotected')
    out['unprotected_private_reader']=z
    # A foreign occupant on the private marker looks like a won bridge.
    alien=(39,801,802)
    z=execute(m.canon((a.HN,alien)+p.reg(300,1)),W,H|{alien})
    check(p.read(z['end'],400)==1,'foreign private marker occupancy lies outside contract')
    out['foreign_marker']=z
    # Empty source is outside the signed-tail input contract.
    z=execute(p.reg(300,1),W,H)
    check(p.read(z['end'],400)==1,'unknown evidence cannot be substituted for negative source')
    out['unsigned_input']=z
    # A completely missing worker has no flag; it cannot be treated as a reliable zero.
    h0,w0,_,_=worker(0);h1,w1,_,_=worker(1)
    hred,wred=reducer(2)
    # A real positive witness is still in worker 0's bridge, not yet copied into its flag.
    z=execute(m.canon((a.HP,)+p.reg(300,1)),[p.one(4),w0[0]]+w1+wred,a.SOURCE_H|h0|h1|hred)
    check(p.read(z['end'],400)==0, 'early reduction misses an outstanding real positive witness')
    out['missing_join_prerequisite']=z
    return out


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='results.json');parser.add_argument('--quick',action='store_true')
    args=parser.parse_args()
    _,cat=e.catalog(a.SOURCE_H)
    dom=tuple(sorted(J for J in cat if a.signed(J)>=0))
    check(len(dom)==9,'reuse original signed-tail input domain')
    out={'scope':'CONDITIONAL_TYPED_BRC_NOT_NATIVE_PHYSICS','examples':examples(),'shuffles':[],'reductions':[],'end_to_end':[]}
    for J in dom:
        record,terminals=shuffles(J,2)
        out['shuffles'].append(record)
        for bits,K in terminals.items():
            out['reductions'].append({'input_flags':bits,'run':reduce_trace(K,2,False)})
    if not args.quick:
        for J in ((a.HP,),m.canon((a.HN,a.P))):
            for k,f in ((3,0),(2,1),(3,1),(3,2)):
                print('shuffle',k,f,J,flush=True)
                record,terminals=shuffles(J,k,f)
                out['shuffles'].append(record)
                for bits,K in terminals.items():
                    out['reductions'].append({'input_flags':bits,'run':reduce_trace(K,k,False)})
        for k,f in ((2,1),(3,2),(6,2)):
            for J in (p.reg(3,1),m.canon((a.HN,a.P))):
                for schedule in ('overlap','serial'):
                    print('joined',k,f,J,schedule,flush=True)
                    out['end_to_end'].append(serial_omissions(J,k,f,schedule))
    out['verification']={'assertions':CHECKS,'uncached_kernel_calls':CALLS,'transition_uses':USES,
                         'shuffle_families':len(out['shuffles']),'joined_families':len(out['end_to_end']),
                         'parent_main_executed':False,'independent_review':False}
    dest=Path(args.output);dest.write_text(json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')
    summary={**out['verification'], 'shuffle_counts':[{'k':v['workers'],'f':v['faults'],'layers':v['layers'],'outcomes':v['outcomes']} for v in out['shuffles']],
             'joined_lengths':[{'k':v['k'],'f':v['faults'],'commands':v['commands'],'layers':v['layers']} for v in out['end_to_end']]}
    dest.with_name('summary_'+dest.name).write_text(json.dumps(summary,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(out['verification'],flush=True)

if __name__=='__main__': main()
