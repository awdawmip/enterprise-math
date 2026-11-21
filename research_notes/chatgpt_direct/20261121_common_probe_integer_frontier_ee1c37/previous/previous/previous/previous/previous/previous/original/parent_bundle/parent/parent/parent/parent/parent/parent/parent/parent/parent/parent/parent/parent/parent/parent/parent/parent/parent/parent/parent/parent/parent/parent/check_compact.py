"""Executable lossless origin compaction for the pinned triadic sorting model.

All scientific matching updates call the inherited, unchanged step kernel.
Positive path algebra is the inherited CWM. Expected bits are test oracles only;
compiled words never branch on an input or use a saved test input to restore it.
"""
from __future__ import annotations
import argparse
import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_lift as old
j, p, m, e, r, f = old.j, old.p, old.m, old.e, old.r, old.f
ONE, ZERO = old.ONE, old.ZERO
CHECKS = 0


def ck(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def xor_gate(x: int, y: int, out: int):
    """11 fixed calls, consume two full inputs, write a full XOR to empty out."""
    j.domains((x, y, out))
    H = set().union(*(p.library(o) for o in (x, y, out)))
    q01 = tuple(sorted((x + 3, y + 4, out + 4)))
    q10 = tuple(sorted((x + 4, y + 3, out + 4)))
    H.update((q01, q10))
    lh, lt = p.reg(out, 0)
    rh, rt = p.reg(out, 1)
    W = [p.one(x + 1), p.one(y + 1), p.add(q01), p.add(q10),
         p.add(lt), p.add(rt), p.one(x + 3), p.one(x + 4),
         p.one(y + 5), p.add(lh), p.add(rh)]
    return H, W


def transfer(src: int, dst: int, work: int):
    """Actual copy without source-head rebuilding, then consume source tail."""
    H, W = p.copy_program(src, dst, work)
    return H, [op for i, op in enumerate(W) if i not in (5, 6)] + [p.one(src + 5)]


def codec(n: int):
    """Fixed n<=6 allocator: first n-1 source bits + sorted output; parity inverse."""
    if not 2 <= n <= 6:
        raise ValueError('The executed address instances cover n=2..6.')
    H, sort_word, sort_stages, wires, free = j.network(n)
    inputs = [6 * i for i in range(n)]
    records = [6 * (n + 2 + i) for i in range(n - 1)]
    accs = [6 * (2 * n + 1), 6 * (2 * n + 2)]
    work = 6 * (2 * n + 3) + 1
    FW = []
    for src, rr in zip(inputs, records):
        h, w = p.copy_program(src, rr, work)
        H |= h
        FW += w
    FW += sort_word
    IW = []
    stages = []
    cur = wires[0]
    nxt = accs[0]
    for idx, src in enumerate(wires[1:], 1):
        h, w = xor_gate(cur, src, nxt)
        H |= h
        IW += w
        cur = nxt
        nxt = accs[1] if cur == accs[0] else accs[0]
        stages.append(dict(kind='sorted_parity', upto=idx + 1, end=len(IW), current=cur))
    # Sorted operands have now really been consumed. Original addresses are empty.
    for idx, (rr, dst) in enumerate(zip(records, inputs)):
        h, w = p.copy_program(rr, dst, work)
        H |= h
        IW += w
        h, w = xor_gate(cur, rr, nxt)
        H |= h
        IW += w
        cur = nxt
        nxt = accs[1] if cur == accs[0] else accs[0]
        stages.append(dict(kind='restore_prefix', upto=idx + 1, end=len(IW), current=cur))
    h, w = transfer(cur, inputs[-1], work)
    H |= h
    IW += w
    stages.append(dict(kind='finish', end=len(IW)))
    return dict(n=n, H=H, forward=FW, inverse=IW, inputs=inputs, records=records,
                wires=wires, free=free, accumulators=accs, work=work,
                stages=stages, sort_stages=sort_stages)


def endpoint(bits, C):
    return m.canon(j.init(tuple(sorted(bits)), C['wires']) + j.init(bits[:-1], C['records']))


def gate_cases():
    H, W = xor_gate(0, 6, 12)
    ck(len(W) == 11, 'eleven-call XOR')
    ck(len(set().union(*H)) == 18, 'XOR uses only three registers')
    rows = []
    for x, y in product((0, 1), repeat=2):
        J = j.init((x, y), (0, 6))
        z = f.execute(J, W, H, keep=True)
        ck(z['end'] == p.reg(12, x ^ y), 'exact XOR endpoint, both sources consumed')
        rows.append(dict(bits=(x, y), run=z))
    HT, WT = transfer(0, 6, 13)
    ck(len(WT) == 8, 'eight-call consuming transfer')
    for bit in (0, 1):
        z = f.execute(p.reg(0, bit), WT, HT, keep=True)
        ck(z['end'] == p.reg(6, bit), 'transfer really removes all old source events')
        rows.append(dict(transfer_bit=bit, run=z))
    return rows


def roundtrips():
    data = []
    for n in range(2, 7):
        C = codec(n)
        H, FW, IW = C['H'], C['forward'], C['inverse']
        q = n * (n - 1) // 2
        ck(len(FW) == 15*q + 9*(n-1), 'compact encoder command count')
        ck(len(IW) == 31*(n-1) + 8, 'compiled parity inverse command count')
        ck(len(set().union(*H)) == 12*n + 19, 'actual union of declared member addresses')
        rows, fine, coarse = [], {}, {}
        positions = [set() for _ in range(len(FW + IW) + 1)] if n == 6 else None
        for bits in product((0, 1), repeat=n):
            J = j.init(bits, C['inputs'])
            z = f.execute(J, FW, H)
            K = z['end']
            ck(K == endpoint(bits, C), 'forward retains only sorted values and first n-1 origin bits')
            ck(K not in fine, 'compact endpoints injective on ordered input words')
            fine[K] = bits
            observed = tuple(p.read(K, o) for o in C['wires'])
            ck(j.sq_observer(bits) == j.sq_observer(observed), 'actual BRC data-square observation')
            f.put(coarse, observed, e.prep(J))
            # Inspect inverse stage boundaries, with all model changes through the original kernel.
            at = 0
            for s in C['stages']:
                K = f.execute(K, IW[at:s['end']], H)['end']
                at = s['end']
                if s['kind'] == 'sorted_parity':
                    want = 0
                    for b in observed[:s['upto']]: want ^= b  # oracle, not program branch
                    ck(p.read(K, s['current']) == want, 'actual sorted-parity accumulator')
                elif s['kind'] == 'restore_prefix':
                    upto = s['upto']
                    ck(tuple(p.read(K,o) for o in C['inputs'][:upto]) == bits[:upto], 'restored ordered prefix')
                    ck(all(p.restrict(K,o) == () for o in C['records'][:upto]), 'consumed origin records empty')
            ck(K == J, 'exact original matching restored; all record/work slots blank')
            if positions is not None:
                K = J
                positions[0].add(K)
                for t, op in enumerate(FW + IW, 1):
                    K, _ = f.step(K, op, H)
                    positions[t].add(K)
                ck(K == J, 'six-bit prefix audit follows same fixed roundtrip')
            trace = None
            if n == 6 and bits == (0,1,0,1,0,1):
                trace = dict(forward=f.execute(J,FW,H,True), inverse=f.execute(z['end'],IW,H,True))
            rows.append(dict(input=bits, sorted=observed, record=bits[:-1], encoded=z['end'], restored=K, trace=trace))
        ck(f.total(coarse.values()) == f.total(ONE for _ in product((0,1),repeat=n)), 'all positive source histories preserved')
        if positions is not None:
            ck(all(len(v)==64 for v in positions), 'all 64 inputs distinct at all 434 common program positions')
        data.append(dict(n=n, record_bits=n-1, forward_calls=len(FW), inverse_calls=len(IW),
                         roundtrip_calls=len(FW+IW), members=len(set().union(*H)), distinct_endpoints=len(fine),
                         fibers=[dict(sorted=k,CWM=e.cw(v)) for k,v in sorted(coarse.items())],
                         common_position_distinct_counts=None if positions is None else list(map(len,positions)),runs=rows))
    return data


def image(weight: int):
    C=codec(6);H,FW,IW=C['H'],C['forward'],C['inverse']
    s=(0,)*(6-weight)+(1,)*weight
    rows=[];valid_count=0
    for record in product((0,1),repeat=5):
        K=m.canon(j.init(s,C['wires'])+j.init(record,C['records']))
        restored=f.execute(K,IW,H)['end']
        x=tuple(p.read(restored,o) for o in C['inputs'])
        rebuilt=f.execute(restored,FW,H)['end']
        valid=weight-sum(record) in (0,1)  # assertion only
        ck((rebuilt==K)==valid,'actual encode-after-decode recognizes exact valid image')
        ck(restored==j.init(x,C['inputs']),'decoder clean on every full canonical triple even out of domain')
        valid_count+=int(valid)
        rows.append(dict(record=record,valid_image=valid,restored=x,reencoded_equals_input=rebuilt==K))
    return dict(weight=weight,canonical_sorted=s,cases=len(rows),valid_count=valid_count,rows=rows)


def retained():
    data=[]
    for n in (2,3,6):
        C=codec(n);H=set(C['H']);work=C['work']
        # Leave the source work member isolated from all new output registers.
        outs=[6*(2*n+4+i) for i in range(n)];CW=[]
        for src,dst in zip(C['wires'],outs):
            h,w=p.copy_program(src,dst,work);H|=h;CW+=w
        W=C['forward']+CW+C['inverse'];rows=[]
        ck(len(W)==15*n*(n-1)//2+49*(n-1)+17,'retained sorted copy command count')
        ck(len(set().union(*H))==18*n+19,'inventory includes sorted copy')
        for bits in product((0,1),repeat=n):
            J=j.init(bits,C['inputs']);z=f.execute(J,W,H)
            expected=m.canon(J+j.init(tuple(sorted(bits)),outs))
            ck(z['end']==expected,'original ordered source plus sorted copy; no origin logs remain')
            rows.append(dict(input=bits,end=z['end']))
        data.append(dict(n=n,calls=len(W),members=len(set().union(*H)),runs=rows))
    return data


def migrate():
    """Convert ACTUAL old 15-record six-bit endpoints, without oracle input."""
    n=6;C=codec(n)
    OH,OF,OI,ostages,owires,ofree,orecords,owork=old.network(n)
    H=OH|C['H'];W=OI+C['forward'];rows=[]
    ck(owires==C['wires'],'old/new final sorted addresses agree')
    ck(C['records']==orecords[:5],'five retained records reuse first five emptied old record slots')
    ck(len(W)==555,'285 old inverse + 270 compact encoder')
    for bits in product((0,1),repeat=n):
        J=j.init(bits,C['inputs']);old_end=f.execute(J,OF,H)['end']
        new_end=f.execute(old_end,W,H)['end']
        ck(new_end==endpoint(bits,C),'15 genuine local origin records converted to exact compact endpoint')
        ck(all(p.restrict(new_end,o)==() for o in orecords[5:]),'ten retired old origin registers physically empty')
        recovered=f.execute(new_end,C['inverse'],H)['end']
        ck(recovered==J,'migrated compact record supports original matching restoration')
        rows.append(dict(input=bits,old_end=old_end,compact_end=new_end,restored=recovered))
    return dict(n=6,migration_calls=len(W),combined_inventory=len(set().union(*H)),runs=rows)


def boundaries():
    C=codec(6);H=C['H'];FW=C['forward'];IW=C['inverse']
    bits=(0,0,0,0,0,1);J=j.init(bits,C['inputs'])
    K=f.execute(J,FW,H)['end']
    rr=C['records'][0]
    mutate=p.clear_word(rr)+[p.add(h) for h in p.reg(rr,1)]
    change=f.execute(K,mutate,H,True)
    dec=f.execute(change['end'],IW,H,True)
    altered=(1,0,0,0,0,0)
    ck(dec['end']==j.init(altered,C['inputs']),'one altered record bit gives different same-weight source')
    enc=f.execute(dec['end'],FW,H)['end']
    ck(enc==change['end'],'tampered record still inside exact legal image')
    ck(j.sq_observer(bits)==j.sq_observer(altered),'data squares cannot detect valid-source substitution')
    # Four raw prefix records alone do not distinguish the two remaining positions.
    pairs=[]
    for b in (bits,(0,0,0,0,1,0)):
        kk=f.execute(j.init(b,C['inputs']),FW+p.clear_word(C['records'][4]),H)['end']
        pairs.append(kk)
    ck(pairs[0]==pairs[1],'actual deletion of fifth record creates ordered-source collision')
    # Two raw inputs with same first five but opposite sixth show record alone is insufficient.
    A=f.execute(j.init((0,0,0,0,0,0),C['inputs']),FW,H)['end']
    B=K
    clear_sorted=sum((p.clear_word(o) for o in C['wires']),[])
    aa=f.execute(A,clear_sorted,H)['end'];bb=f.execute(B,clear_sorted,H)['end']
    ck(aa==bb,'discarding sorted side information merges origins despite all five record bits')
    # Reversal of the command list is not the compiled inverse.
    reversed_result=f.execute(K,list(reversed(FW)),H)['end']
    ck(reversed_result!=J,'reverse command order not an inverse')
    return dict(corruption=dict(original=bits,mutation=change,decoded=dec),four_record_collision=pairs,
                missing_side_information=aa,reverse_word_endpoint=reversed_result)


def faults():
    H,W=xor_gate(0,6,12);out=[]
    for bits in product((0,1),repeat=2):
        start=j.init(bits,(0,6));expected=p.reg(12,bits[0]^bits[1])
        for budget in (1,2):
            word=j.d.a.rep(W,budget);states={(start,0):e.prep(start)}
            for op in word:
                nxt={}
                for (K,u),mass in states.items():
                    L,_=f.step(K,op,H)
                    f.put(nxt,(L,u),r.serial(mass,ONE))
                    if u<budget:f.put(nxt,(K,u+1),r.serial(mass,ONE))
                states=nxt
            layers={}
            for (K,u),mass in states.items():
                ck(K==expected,'protected XOR remains a complete consuming gate')
                f.put(layers,u,mass)
            ck(layers==j.d.a.layers(len(word),budget),'all omission positions counted by positive CWM')
            out.append(dict(input=bits,budget=budget,calls=len(word),layers=[dict(omitted=u,CWM=e.cw(v)) for u,v in sorted(layers.items())]))
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',required=True,choices=['gates','roundtrips','image','retained','migrate','boundaries','faults'])
    ap.add_argument('--weight',type=int);ap.add_argument('--output',required=True)
    args=ap.parse_args()
    if args.mode=='image':
        if args.weight is None or not 0<=args.weight<=6:ap.error('--weight must be 0..6 for image')
        data=image(args.weight)
    else:data={'gates':gate_cases,'roundtrips':roundtrips,'retained':retained,'migrate':migrate,'boundaries':boundaries,'faults':faults}[args.mode]()
    result=dict(mode=args.mode,new_checks=CHECKS,uncached_kernel_calls=f.CALLS,transition_uses=f.USES,data=data)
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='data'}))

if __name__=='__main__':main()
