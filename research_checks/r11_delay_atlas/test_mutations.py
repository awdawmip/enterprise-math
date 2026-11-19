"""Negative controls on the production verification path, including forced collisions."""
import copy
import json
import sys

sys.dont_write_bytecode=True
from verify import HERE, Rejected, check_case, check_manifest, equal_field, full_field, baseline, parse


def expect(label,code,fn):
    try:
        fn()
    except Rejected as err:
        if err.code != code:
            raise AssertionError((label,code,err.code)) from err
        return {'control':label,'rejection':code}
    raise AssertionError('mutated certificate unexpectedly accepted: '+label)


def changed(obj):
    return copy.deepcopy(obj)


def main():
    manifest=parse((HERE/'INPUT_MANIFEST.json').read_text())
    check_manifest(manifest)
    rows=[parse(line) for line in (HERE/'CASES.jsonl').read_text().splitlines()]
    if len(rows)!=144:
        raise AssertionError('144 stored cases required')
    row=next(case for case in rows if case['classification']=='RECOVERED' and
             case['steps'][0]['patch'] and any(w['flow_delta'] for w in case['steps']))
    check_case(row,256)
    checks=[]
    no_slot=changed(row)
    no_slot['steps'][0]['patch'][0][2].pop()
    checks.append(expect('delete_one_positive_pending_slot','complete_field',
                         lambda:check_case(no_slot,256)))
    rem=changed(row)
    slots=rem['steps'][0]['patch'][0][2]
    for slot in slots:
        used={(x[0],x[1],x[2]) for x in slots}
        alternate=next((d for d in range(1,5) if (slot[0],slot[1],d) not in used),None)
        if alternate is not None:
            slot[2]=alternate
            break
    checks.append(expect('change_one_remaining_time','complete_field',lambda:check_case(rem,256)))
    exterior=changed(manifest)
    exterior['observer']['site_count']-=1
    checks.append(expect('omit_one_background_address','model_site_count',
                         lambda:check_manifest(exterior)))
    exact=full_field(baseline(0))
    if equal_field(exact,(*exact[:3],exact[3][1:]),lambda _:0):
        raise AssertionError('full b-field lost its first nonmaterial address')
    gate=changed(manifest)
    gate['observer']['gate']=[0,1]
    checks.append(expect('widen_gate','model_gate',lambda:check_manifest(gate)))
    phase=changed(row)
    phase['phase_shift']=(phase['phase_shift']+3)%6
    checks.append(expect('claim_other_background_permitted_phase','recovery_phase',
                         lambda:check_case(phase,256)))
    lost=changed(row)
    nonzero=next(step['flow_delta'] for step in lost['steps'] if step['flow_delta'])
    nonzero.pop(next(iter(nonzero)))
    checks.append(expect('lose_cumulative_labelled_flux','cumulative_flux',lambda:check_case(lost,256)))
    collision=changed(row)
    collision['steps'][0]['patch'][0][1][0]+=1
    checks.append(expect('different_full_states_same_locator','complete_field',
                         lambda:check_case(collision,256,locator=lambda _:0)))
    unrun=changed(row)
    unrun.update(ticks=0,steps=[])
    checks.append(expect('mark_unexecuted_case_recovered','executed_prefix',lambda:check_case(unrun,256)))
    print(json.dumps({'negative_controls':checks,'controls_rejected':len(checks)},indent=2))
    return 0


if __name__=='__main__':
    sys.exit(main())
