"""Conditional incidence-gate certificate with the published positive CWM kernel."""
import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
import hashlib
from itertools import combinations, permutations, product
import json
from math import gcd
from pathlib import Path
import sys


PINS = {
    "research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md":
        "03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b",
    "src/enterprise_math/brc_weighted.py": "3f205696709e847909958a153f8fe10d3f6b70f0",
    "src/enterprise_math/brc_logarithm.py": "4732e5fc381ce613d240c4381ccbef03c27a69c7",
    "src/enterprise_math/exact_arithmetic.py": "35ea95b0916494b83a92386e3e313928362dd79e",
}


def load_kernel(root):
    for name, pin in PINS.items():
        data = (root / name).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if blob != pin:
            raise ValueError(f"version mismatch for {name}")
    sys.path.insert(0, str(root / "src"))
    from enterprise_math import brc_weighted
    return brc_weighted


def local_match(source_slot, reference_slot):
    return int(source_slot == reference_slot)


class Scan:
    def __init__(self, brc):
        self.brc = brc
        self.operations = Counter()
        self.unit = brc.cwm_edge(1)

    def step(self, weight, label):
        self.operations[label] += 1
        return self.brc.cwm_propagate(weight, self.unit)

    def run(self, m, state, direction=1, sheet=1, errors=(), weight=None):
        """Only the equality below controls a source-dependent microscopic action."""
        j, x, r, bit = state
        assert gcd(direction, m) == 1 and sheet in (-1, 1)
        weight = self.brc.CWM_ONE if weight is None else weight
        steps = []
        for i in range(m):
            bit ^= local_match(j, x) ^ int(i in errors)
            weight = self.step(weight, "local_xor")
            if bit:
                weight = self.step(weight, "receiver_hold")
            elif m == 3:
                # Quoted action P^sheet. These are candidate, positive CWM transitions;
                # we do not import the unavailable original world's contact routine.
                pushes = (direction * sheet) % 3
                for _ in range(pushes):
                    r = (r + sheet) % m
                    weight = self.step(weight, "quoted_three_channel_contact")
            else:
                r = (r + direction) % m
                weight = self.step(weight, "mod_m_receiver_turn")
            x = (x + direction) % m
            weight = self.step(weight, "scheduled_reference_turn")
            steps.append((x, r, bit))
        bit ^= 1
        weight = self.step(weight, "blind_final_not")
        return (j, x, r, bit), weight, steps

    def reverse(self, m, state, direction=1):
        j, x, r, bit = state
        weight = self.step(self.brc.CWM_ONE, "inverse_blind_not")
        bit ^= 1
        for _ in range(m):
            x = (x-direction)%m
            weight = self.step(weight, "inverse_reference_turn")
            if bit == 0:
                r = (r-direction)%m
            weight = self.step(weight, "inverse_receiver_or_hold")
            bit ^= local_match(j, x)
            weight = self.step(weight, "inverse_local_xor")
        return (j,x,r,bit), weight


def contact_certificate(scan):
    m = 3
    checks = 0
    equivariance = 0
    chart_rows = []
    for state in product(range(m), range(m), range(m), range(2)):
        j, a, r, b = state
        output, weight, history = scan.run(m, state)
        assert output == (j, a, (r+(-1)**b*(j-a))%m, b)
        assert weight == scan.brc.CWM_ONE
        assert scan.reverse(m,output) == (state,weight)
        for u, c, sheet in product((1,-1), range(m), (1,-1)):
            change = lambda t: (u*t+c)%m
            changed = (change(j), change(a),change(r),b)
            out, w, hist = scan.run(m, changed,u,sheet)
            assert out == (*map(change,output[:3]),output[3])
            assert hist == [(change(x),change(y),bit) for x,y,bit in history]
            assert w == weight
            equivariance += 1
        if b == 0:
            chart_rows.append({"input":[j,a,r],"output":list(output[:3])})
        checks += 1
    # A joint, non-product weighted input. Compare typed masses after recording.
    brc = scan.brc
    raw = [(s,1+s[0]+2*s[1]+3*s[2]+s[0]*s[2]+7*(s[1]==s[2])) for s in product(range(3),repeat=3)]
    normalizer = sum(w for _,w in raw)
    before,after={},{}
    for (j,a,r),n in raw:
        w = brc.cwm_edge(Fraction(n,normalizer))
        dest, w2, _ = scan.run(m,(j,a,r,0),weight=w)
        assert w == w2
        left,right=(r-a)%m,(dest[2]-j)%m
        before[left]=brc.cwm_recoalesce(before.get(left,brc.CWM_ZERO),w)
        after[right]=brc.cwm_recoalesce(after.get(right,brc.CWM_ZERO),w2)
    assert before == after
    return dict(original_channel_rows=chart_rows,full_inputs=checks,
                expanded_frame_and_sheet_tests=equivariance,
                difference_bins=[dict(count=after[i].count,total=str(after[i].total),
                                      dominant=str(after[i].dominant)) for i in range(3)])


def generic(scan):
    by_mod = {}
    for m in range(2,10):
        count = 0
        for u in range(1,m):
            if gcd(u,m)!=1:
                continue
            for j,a,r,b in product(range(m),range(m),range(m),(0,1)):
                out,w,_=scan.run(m,(j,a,r,b),u)
                assert out == (j,a,(r+(-1)**b*(j-a))%m,b) and w==scan.brc.CWM_ONE
                count += 1
        by_mod[m]=count
    return by_mod


def matching_certificates():
    # All perfect matchings on 2m states are exactly the conjugates of a bit toggle.
    def match(rest):
        if not rest:
            yield []
            return
        for i in range(1,len(rest)):
            pair=(rest[0],rest[i])
            for rest_pairs in match(rest[1:i]+rest[i+1:]):
                yield [pair]+rest_pairs
    result={}
    for m in range(2,6):
        count=0
        allowed=set()
        for pairs in match(tuple(range(2*m))):
            action = {x:y for i,j in pairs for x,y in [(i,j),(j,i)]}
            if all(action[x]<m for x in range(m)):
                diffs={(action[x]-x)%m for x in range(m)}
                if len(diffs)==1:
                    allowed.update(diffs)
            count+=1
        assert all(2*t%m==0 for t in allowed)
        assert 1 not in allowed or m==2
        result[m]=dict(involutions=count,clean_cyclic_translations=sorted(allowed))
    return result


def blindness():
    checks=0
    examples={}
    for m in range(2,14):
        for allowed in combinations(range(m),2):
            subgroup_size=m//reduce(gcd,allowed,m)
            reached={0}
            while True:
                enlarged=reached|{(x+t)%m for x in reached for t in allowed}
                if enlarged==reached:
                    break
                reached=enlarged
            assert len(reached)==subgroup_size
            for first in range(m):
                offsets=reached|{(first+x)%m for x in reached}
                cells=Counter(tuple(t==d for t in sorted(offsets)) for d in range(m))
                assert len(cells)==len(offsets)+int(len(offsets)<m)
                assert max(cells.values())==max(1,m-len(offsets))
                checks+=1
    for m,h in [(3,1),(6,2),(12,4)]:
        u=m//h
        offsets=list(range(0,m,u))
        examples[f"m{m}_step{u}"]=dict(reachable=offsets,blind=[d for d in range(m) if d not in offsets])
    return dict(two_start_windows_checked=checks,examples=examples)


def blind_spot(scan):
    result={}
    for m in range(3,11):
        cases=0
        for baseline in range(m):
            for d,r in product(range(m),range(m)):
                a = (baseline**2+1)%m
                source_slot = (a+d)%m
                for halfcode in (False,True):
                    y=(r+baseline)%m
                    bit=0
                    tests=0
                    w=scan.step(scan.brc.CWM_ONE,"blind_spot_known_initial_turn")
                    for t in range(m):
                        if t==baseline:
                            continue
                        shift=(t-baseline)%m
                        reference_slot=(a+t)%m
                        if halfcode and 2*shift==m:
                            h=m//2
                            low=y%h
                            y,bit=low+h*bit,y//h
                            w=scan.step(w,"swap_receiver_half_with_bit")
                            bit ^= local_match(source_slot,reference_slot)
                            w=scan.step(w,"blind_spot_xor")
                            y,bit=low+h*bit,y//h
                            w=scan.step(w,"swap_receiver_half_with_bit")
                            tests+=1
                        else:
                            bit ^= local_match(source_slot,reference_slot)
                            w=scan.step(w,"blind_spot_xor")
                            y=(y+bit*shift)%m
                            w=scan.step(w,"blind_spot_known_controlled_turn")
                            bit ^= local_match(source_slot,reference_slot)
                            w=scan.step(w,"blind_spot_xor")
                            tests+=2
                    assert (y,bit,w)==((r+d)%m,0,scan.brc.CWM_ONE)
                    assert tests==2*(m-1)-int(halfcode and m%2==0)
                    cases+=1
        result[m]=dict(tested_ready_inputs_across_both_gate_sets=cases,
                       tests_with_receiver_recoding=2*(m-1)-int(m%2==0),
                       tests_with_write_only_receiver=2*(m-1))
    return result


def fault_certificate(scan):
    result={}
    for m in range(2,12):
        one,two,correct=0,0,0
        for k in range(m):
            for a in range(m):
                out,_,_=scan.run(m,(k,0,0,0),errors=(a,))
                assert out[-1]==1
                one+=1
            for s,t in combinations(range(m),2):
                out,_,_=scan.run(m,(k,0,0,0),errors=(s,t))
                drift=t-s-2*min(max(k-s,0),t-s)
                assert out[-1]==0 and (out[2]-k-drift)%m==0
                midpoint=(2*k==s+t)
                assert (out[2]==k)==midpoint
                correct+=int(midpoint)
                two+=1
        assert correct==(m-1)**2//4
        result[m]=dict(one_flip_flagged=one,two_flip_trials=two,
                       two_flip_clean_flag=two,correct_records_after_two=correct,
                       conditional_success=str(Fraction(correct,two)))
    return result


def optimal_reads():
    out={}
    for m in range(2,8):
        weights=[k+1 for k in range(m)]
        costs=[]
        for order in permutations(range(m)):
            costs.append(sum(weights[k]*min(i+1,m-1) for i,k in enumerate(order)))
        denom=sum(weights)
        expect=sum(sorted(weights,reverse=True)[i]*min(i+1,m-1) for i in range(m))
        assert min(costs)==expect
        out[m]=dict(prior_weights=weights,orders=len(costs),optimal_mean=str(Fraction(expect,denom)),
                    uniform_mean=str(Fraction((m-1)*(m+2),2*m)))
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-checkout',required=True,type=Path)
    root=parser.parse_args().source_checkout.resolve()
    scan=Scan(load_kernel(root))
    result=dict(source_pins=PINS,original_recorder_package_replayed=False,
                target="conditional local equality at a scheduled, movable reference",
                three_channel=contact_certificate(scan),all_unit_frames=generic(scan),
                involution_conjugacy=matching_certificates(),movement=blindness(),
                unavailable_single_offset=blind_spot(scan),
                read_only=optimal_reads(),faults=fault_certificate(scan),
                actual_unit_cwm_propagations=dict(scan.operations))
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
