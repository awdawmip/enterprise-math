"""Typed, labelled P07 contact extensions on a replayable period-three graph."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import importlib.util
from itertools import combinations, permutations, product
import json
from math import comb, factorial, prod
from pathlib import Path
import sys
from tempfile import TemporaryDirectory

CORE_HASH = '7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'
M2_HASH = '3aa56d0509634fd70f4ca6ef7aa787705462c0f3ef343073d117954706a15016'
N1_HASH = '09eae3e08308e3041416daaca5a951b7c632104bbe7fa21200b11d57b6b568e9'
SOURCE_HASHES = [
    '181a935292fc851e53ee6c4f50961e77bca4b4daba1f8029a638805990568bfd',
    '2372ee25cf2c8d619c7827db48d51659445d2cfb4c8aac1e7315897d85786a6a',
]
CELLS = list(product(range(3), repeat=6))
INDEX = {x:i for i,x in enumerate(CELLS)}


def load_checked(path, digest, name):
    if sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError(f'source digest mismatch for {name}')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class Accounts:
    def __init__(self, core):
        self.core = core
        self.operations = []

    def evaluate(self, label, weights, power):
        value = self.core.recurrent_mass_power(weights, power)[0][-1]
        assert value.denominator == 1
        self.operations.append((label, weights, power, value.numerator))
        return value.numerator

    def event(self, label):
        return self.evaluate(label, [[0,1],[0,0]], 1)

    def plus(self, a, b, label):
        return self.evaluate(label, [[0,a,b,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]], 2)

    def aggregate(self, values, label):
        total = 0
        for value in values:
            total = self.plus(total,value,label)
        return total

    def debit(self, balance, bills):
        charge = self.aggregate(bills, 'joint_bill')
        if charge > balance:
            return None
        new = balance-charge
        assert self.plus(new,charge,'one_account_reconciliation') == balance
        return new


def neighbor(cell, axis, sign):
    coords = list(CELLS[cell])
    coords[axis] = (coords[axis]+sign)%3
    return INDEX[tuple(coords)]


def token(identity, source, role, sign):
    return dict(id=identity, source=source, role=role, sign=sign, cell=0, path=[])


def transfer(B, old, tick):
    c = tick%3
    role = (old['role']+c)%3
    dst = neighbor(old['cell'],role,old['sign'])
    event = [tick,old['cell'],dst,old['role'],role,role,old['sign'],c,0]
    B.event(f"edge:{tick}:{old['id']}:{old['cell']}:{dst}")
    return dict(old,cell=dst,role=role,path=old['path']+[event])


def selections(groups):
    """No arbitrary pairing: role-0 subset anchors the unordered triples."""
    for k in range(min(map(len,groups))+1):
        for x in combinations(groups[0], k):
            for y in permutations(groups[1], k):
                for z in permutations(groups[2], k):
                    yield tuple(zip(x,y,z))


def original_check(path, tape):
    model = load_checked(path,M2_HASH,'original_p07_m2')
    assert sha256((path.parent/'vendor/brc_weighted_recurrent.py').read_bytes()).hexdigest()==CORE_HASH
    B,checks = model.BRC(),model.Checks()
    with TemporaryDirectory() as tmp:
        target=Path(tmp)
        result=model.simulate(B,checks,target,'FREE_CYCLIC',(0,0,1),steps=9)
        sf=next(target.glob('*STATES.json'))
        ef=next(target.glob('*EVENTS.json'))
        assert [sha256(f.read_bytes()).hexdigest() for f in (ef,sf)]==SOURCE_HASHES
        assert (result['background_action_events'],result['activation_transfer_events'],len(B.ledger))==(6561,27,27)
        for i,row in enumerate(json.loads(sf.read_text())):
            assert len(row['cells'])==729 and not row['closed_obligations']
            expected={f"lambda:{v['id'][1:]}":v for v in tape[i]}
            for cell in row['cells']:
                v=cell['cell']
                assert cell['identity']==list(CELLS[v]) and cell['contact_frame']==[i%3,0]
                assert cell['background_triad']==[f'bg:{v}:{r}' for r in range(3)]
                assert sorted(cell['active_source_slots'])==sorted(s for s,a in expected.items() if a['cell']==v)
            for old in row['all_live_obligations']:
                v=expected[old['id']]
                assert (old['source'],old['cell'],old['role'],old['sign'])==('lambda',v['cell'],v['role'],v['sign'])
                assert [[e['heartbeat_from'],e['source_cell'],e['target_cell'],e['role_before'],
                         e['role_after'],e['axis'],e['sign'],*e['contact_before']]
                        for e in old['history']]==v['path']


def budget_source(path):
    mod=load_checked(path,N1_HASH,'original_p07_n1')
    ar=mod.TraceArithmetic()
    ar.stage='joint_account'
    receipt=mod.SharedBudget(5,ar)
    alias=receipt
    try:
        receipt.spend_batch([4,4])
    except ValueError:
        assert alias.amount==5
    else:
        raise AssertionError('overspending accepted')
    alias.spend_batch([2,3])
    assert receipt.amount==0


def histogram(triads):
    return tuple(sorted(Counter(''.join(s[0] for s in triple) for triple in triads).items()))


def multinomial_audit():
    checked=Counter()
    for counts in product(range(3),repeat=6):
        a,b=counts[:3],counts[3:]
        groups=[[f'{s}{r}:{i}' for s,ls in [('A',a),('B',b)] for i in range(ls[r])] for r in range(3)]
        by_type=Counter((len(m),histogram(m)) for m in selections(groups))
        mixed=defaultdict(set)
        total=Counter()
        for (qty,h),n in by_type.items():
            uses=Counter()
            for labels,x in h:
                for r,s in enumerate(labels): uses[r,s]+=x
            predicted=prod(factorial(ls[r])//factorial(ls[r]-uses[r,s])
                           for s,ls in [('A',a),('B',b)] for r in range(3))//prod(factorial(x) for _,x in h)
            assert predicted==n
            total[qty]+=n
            mixed[qty].add(sum(x for labels,x in h if len(set(labels))>1))
        for h,n in total.items():
            assert n==factorial(h)**2*prod(comb(len(g),h) for g in groups)
            u=min(min(map(len,groups)),sum(a),sum(b))
            assert min(mixed[h])==max(0,h-min(a)-min(b)) and max(mixed[h])==min(h,u)
            spectrum=set()
            for d in range(h+1):
                lo=max(0,h-d-min(b),(3*h-2*d-sum(b)+2)//3)
                hi=min(h-d,min(a),(sum(a)-d)//3)
                if lo<=hi:
                    spectrum.add(d)
            assert spectrum==mixed[h]
            if a[0]==a[1]==a[2] and b[0]==b[1]==b[2] and h==a[0]+b[0]:
                assert spectrum=={0}.union(range(2,u+1))
        if counts==(1,)*6:
            assert mixed[2]=={0,2} and total[2]==4
        checked.update(inventories=1,tensor_histograms=len(by_type),labelled_matchings=sum(total.values()))
    return dict(checked)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--core',type=Path,help='pinned public brc_weighted_recurrent.py')
    ap.add_argument('--m2',type=Path,help='optional original native_candidates.py with its vendor directory')
    ap.add_argument('--n1',type=Path,help='optional original test_native_pointer.py with its dependencies')
    ap.add_argument('--expand',type=Path,help='write full integer checker data, every cell and branch, to this file')
    args=ap.parse_args()
    if args.core is None:
        roots=(Path.cwd(),*Path(__file__).resolve().parents)
        args.core=next((f for r in roots for f in [r/'src/enterprise_math/brc_weighted_recurrent.py'] if f.is_file()),None)
    if args.core is None: ap.error('supply --core or run from a checkout with src/enterprise_math/')
    B=Accounts(load_checked(args.core,CORE_HASH,'public_p07_brc'))
    all_edges={(v,r,s):neighbor(v,r,s) for v in range(729) for r in range(6) for s in (1,-1)}
    assert all(all_edges[y,r,-s]==v for (v,r,s),y in all_edges.items())
    first=[token(f'A{i}','A',r,1) for i,r in enumerate((0,0,1))]
    tape=[first]
    for h in range(9):
        tape.append([transfer(B,v,h) for v in tape[-1]])
    meets=[i for i,row in enumerate(tape) if len({v['cell'] for v in row})==1]
    assert meets==[0,9]
    roles=[v['role'] for v in tape[-1]]
    assert roles==[0,0,1] and all(v['cell']==0 for v in tape[-1])
    if args.m2: original_check(args.m2,tape)
    if args.n1: budget_source(args.n1)
    start=tape[-1]+[token(f'B{r}','B',r,-1) for r in range(3)]
    ids={v['id']:v for v in start}
    groups=[[v['id'] for v in start if v['role']==r] for r in range(3)]
    rows=[]
    branch_live=[]
    for m in selections(groups):
        removed={i for tri in m for i in tri}
        pending=[v for v in start if v['id'] not in removed]
        balance=B.debit(4,[1]*len(m)+[1]*len(pending))
        if balance is None:
            assert m==()
            continue
        tri,=m
        contact=B.event('joint_contact:'+','.join(tri))
        assert contact==1
        out=[transfer(B,v,9) for v in pending]
        assert set(tri).isdisjoint(v['id'] for v in out)
        assert set(tri)|{v['id'] for v in out}==set(ids)
        for s in ('A','B'):
            assert B.plus(sum(ids[i]['source']==s for i in tri),sum(v['source']==s for v in out),'source_partition')==3
        branch_live.append(out)
        topup=B.plus(balance,3,'identical_later_input')
        after=B.debit(topup,[1,1,1])
        assert after==0 and all(v['role'] in (0,1) for v in out)
        later=[transfer(B,v,10) for v in out]
        rows.append(dict(held=list(tri),common_followup_targets=[[v['id'],v['cell']] for v in later],same=len({ids[i]['source'] for i in tri})==1,
                         balance=balance,live_targets=[[v['id'],v['cell']] for v in out],
                         active_cells=len({v['cell'] for v in out})))
    assert len(rows)==6 and sum(row['same'] for row in rows)==1
    pure=next(row for row in rows if row['same'])
    reads=[Counter(v for _,v in row['live_targets']) for row in rows]
    pure_read=Counter(v for _,v in pure['live_targets'])
    assert all(any((not row['same']) and cnt[site]==pure_read[site] for row,cnt in zip(rows,reads))
               for site in range(729))
    assert all((cnt[162]==cnt[486]==0)==row['same'] for row,cnt in zip(rows,reads))
    assert B.debit(5,[4,4]) is None and B.debit(5,[2,3])==0
    ledger=json.dumps(B.operations,separators=(',',':')).encode()
    if args.expand:
        expanded=[]
        for row,live in zip(rows,branch_live):
            closed=[dict(ids[i],closed_tick=10,joint=row['held']) for i in row['held']]
            cells=[dict(address=x,background_ids=[[v,j] for j in range(3)],frame=[1,0],
                        live=[a['id'] for a in live if a['cell']==v],
                        held=[a['id'] for a in closed if a['cell']==v]) for v,x in enumerate(CELLS)]
            expanded.append(dict(cells=cells,adjacency='axis signs mod 3',live=live,closed=closed,
                                 relation=dict(source_members={'A':['A0','A1','A2'],'B':['B0','B1','B2']},
                                 account_initial=4,account_final=row['balance'],contact=row['held'],
                                 receipt_edges=[v['path'][-1] for v in live])))
        args.expand.write_text(json.dumps(expanded,separators=(',',':'))+'\n')
    proof=dict(core=CORE_HASH,original_source_fingerprints={'M2':M2_HASH,'N1':N1_HASH},
               independent_source_replay_hashes=SOURCE_HASHES,
               cells=len(CELLS),signed_edges=len(all_edges),triple_meeting_steps=meets,
               prefix_states=[[(v['cell'],v['role']) for v in step] for step in tape],
               prefix_cost={'background_sites':9*729,'slot_transfers':27},
               window={'raw_role_triples':6,'minimum_single_cell_reads_for_realized_purity':2,'witness_read_cells':[162,486],'candidate_partial_matchings':7,'debit_rejections':1,
                       'funded_source_pure':1,'funded_unrestricted':6,
                       'per_branch':{'background_sites':729,'joint_records':1,'custody_memberships':3,'signed_edge_transfers':3}},
               outputs=rows,six_count_grid=multinomial_audit(),
               audited_brc_calls=len(json.loads(ledger)),ledger_sha256=sha256(ledger).hexdigest())
    print(json.dumps(proof,indent=2,sort_keys=True))


if __name__=='__main__': main()
