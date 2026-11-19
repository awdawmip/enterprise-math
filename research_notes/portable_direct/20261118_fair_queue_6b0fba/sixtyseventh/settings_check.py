"""A finite setting protocol. Original labelled M2 replay is optional and hash-pinned."""
import argparse
import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
from tempfile import TemporaryDirectory

M2_HASH = '3aa56d0509634fd70f4ca6ef7aa787705462c0f3ef343073d117954706a15016'
CORE_HASH = '7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def position(role, t):
    h, r = divmod(t, 3)
    xyz = [0] * 6
    xyz[role] = (2*h + (r >= 1)) % 3
    xyz[(role+1) % 3] = (h + (r == 2)) % 3
    return tuple(xyz)


def source_receipt(path):
    assert digest(path) == M2_HASH and digest(path.parent/'vendor/brc_weighted_recurrent.py') == CORE_HASH
    spec = importlib.util.spec_from_file_location('m2_settings_replay', path)
    m2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m2)
    archive_rows = []
    all_pairs = set()
    for j in range(3):
        seed = (j, j, (j+1) % 3)
        b, c = m2.BRC(), m2.Checks()
        with TemporaryDirectory() as folder:
            where = Path(folder)
            m2.simulate(b,c,where,'FREE_CYCLIC',seed,steps=9,polarity=1)
            ep, sp = next(where.glob('*EVENTS.json')), next(where.glob('*STATES.json'))
            events, snapshots = json.loads(ep.read_text()), json.loads(sp.read_text())
            moves = [e for e in events if e['kind']=='residual_driven_activation_transfer']
            assert len(events)==6588 and len(moves)==27 and len(b.ledger)==27 and len(c.rows)==28
            cells = list(product(range(3), repeat=6))
            pairs = set()
            for e in moves:
                t = e['heartbeat_from']
                slot = int(e['slot'].split(':')[1])
                role = seed[slot]
                c0 = t % 3
                before = (role + t*(t-1)//2) % 3
                axis = (before+c0) % 3
                assert e['contact_before']==[c0,0] and e['role_before']==before
                assert e['role_after']==e['axis']==axis and e['sign']==e['weight']==1
                assert cells[e['source_cell']]==position(role,t)
                assert cells[e['target_cell']]==position(role,t+1)
                pairs.add((c0,before))
            for t, state in enumerate(snapshots):
                assert len(state['cells'])==729 and all(v['contact_frame']==[t%3,0] for v in state['cells'])
                assert len(state['all_live_obligations'])==3 and not state['closed_obligations']
                for tok in state['all_live_obligations']:
                    slot = int(tok['id'].split(':')[1])
                    assert tok['source']=='lambda' and len(tok['history'])==t
                    assert cells[tok['cell']]==position(seed[slot],t)
            if j==0:
                assert digest(ep)=='181a935292fc851e53ee6c4f50961e77bca4b4daba1f8029a638805990568bfd'
                assert digest(sp)=='2372ee25cf2c8d619c7827db48d51659445d2cfb4c8aac1e7315897d85786a6a'
            all_pairs.update(pairs)
            archive_rows.append(dict(seed=list(seed),events_sha256=digest(ep),states_sha256=digest(sp),
                transfers=len(moves),background_events=len(events)-len(moves),brc_units=len(b.ledger),
                original_checks=len(c.rows),contact_role_pairs=len(pairs)))
    assert len(all_pairs)==9
    return dict(source_sha256=M2_HASH,core_sha256=CORE_HASH,original_simulate_rows=archive_rows,
                union_contact_role_pairs=len(all_pairs),post_axis_decoder_exact=True)


def convolution(a,b):
    n=len(a)
    return [sum(a[j]*b[(i-j)%n] for j in range(n)) for i in range(n)]


def kernel(m,d,t):
    k,u=divmod(t % (m*d),d)
    weights=[0]*m
    weights[k],weights[(k+1)%m]=d-u,u
    return weights


def defects():
    # Integer weights with common denominator d^2. Full mesh pairs include all inverse pairs.
    out=[]
    for m,d in [(2,16),(3,20),(5,12),(8,8)]:
        group_max=inverse_max=0
        all_rows=[kernel(m,d,t) for t in range(m*d)]
        for s,a in enumerate(all_rows):
            for t,b in enumerate(all_rows):
                c=convolution(a,b)
                target=all_rows[(s+t)%(m*d)]
                diff=[x-d*y for x,y in zip(c,target)]
                u,v=s%d,t%d
                factor=u*v if u+v<=d else (d-u)*(d-v)
                index=(s//d+t//d)%m
                expected=[0]*m
                for j,w in enumerate((1,-2,1)):
                    expected[(index+j)%m]+=factor*w
                assert diff==expected
                twice_tv=sum(map(abs,diff))
                group_max=max(group_max,twice_tv)
                if (s+t)%(m*d)==0:
                    inverse_max=max(inverse_max,twice_tv)
        assert group_max==inverse_max==d*d
        out.append(dict(states=m,subdivisions=d,all_pairs=(m*d)**2,
                        max_group_tv=str(F(group_max,2*d*d)),max_inverse_tv=str(F(inverse_max,2*d*d))))
    return out


def min_states(m,a):
    surviving=a
    while gcd(m,surviving)>1:
        surviving//=gcd(m,surviving)
    return m*(a//surviving)


def discrete_tests():
    pairs=0
    for m,a in product(range(2,27),range(1,101)):
        actual=next(l for l in range(m,m*a+1) if l//gcd(l,a)==m)
        assert min_states(m,a)==actual and (m*a)%actual==0
        pairs+=1
    assert min_states(3,6000)==9
    return dict(checked_pairs=pairs,N=18000,anchor_stride=6000,anchor_order=3,
                minimum_states=9,witness=[(6000*j)%9 for j in range(3)])


def observed_tests():
    visible=[]
    for t in range(361):
        # Independent single-slot walk followed by a coordinate reading.
        for j in range(3):
            xyz=[0]*6
            role=j
            for n in range(t):
                role=(role+n%3)%3
                xyz[role]=(xyz[role]+1)%3
            assert tuple(xyz)==position(j,t)
        outputs={position(j,t) for j in range(3)}
        assert len(outputs)==(1 if t%9==0 else 3)
        if 1<=t<=9:
            visible.append(len(outputs))
    # Push midpoint forward through the genuine endpoint observer. Its baseline is j=0.
    readouts=[Counter(),Counter()]
    for t in range(1,10):
        for j,mass in enumerate((F(1,2),F(1,4),F(1,4))):
            readouts[0][t,position(j,t)]+=mass/9
        readouts[1][t,position(0,t)]+=F(1,9)
    tv=sum(abs(readouts[0][key]-readouts[1][key]) for key in readouts[0].keys()|readouts[1].keys())/2
    assert tv==F(4,9)
    return dict(closed_formula_times_checked=361,position_classes_t1_to_t9=visible,
                midpoint_position_tv_known_uniform_tick=str(tv),midpoint_position_tv_t9='0',
                midpoint_port_tv='1/2')


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--m2',type=Path,help='Optional original native_candidates.py beside its vendor directory.')
    ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    answer=dict(source_replay=source_receipt(args.m2) if args.m2 else None,external_mesh=defects(),
                labelled_observer=observed_tests(),finite_cycle=discrete_tests())
    data=json.dumps(answer,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(data)
    else:
        print(data,end='')
