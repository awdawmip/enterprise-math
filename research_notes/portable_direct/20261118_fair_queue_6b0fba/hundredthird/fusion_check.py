"""Replay or audit the C2 integration on the two complete S15 workload policies."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

from fusion_reverse import check as reverse_windows

HERE=Path(__file__).resolve().parent
S15='4514051d6564462eb24610e63040a35742344dd4c77aca76b271151de2c244d4'
C2='b0eb513d6fbee51cbb1e0cb13a62c229ea2123ab377d8d52da669657f49d3e14'
POLICIES=('s15_65','s15_195')
FIELDS=('copied_terms','coefficient_visits','shifted_terms','merge_row_visits','transform_row_visits')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def restore(source, root):
    root.mkdir(parents=True, exist_ok=False)
    with ZipFile(source) as z:
        nested='BRC_Shor_Online_Calibration_S14_9EB73CFB_20260930.zip'
        names=[n for n in z.namelist() if n.startswith('s15/') and n.count('/')==1
               and (n.endswith('.py') or n in ('s15/PROTOCOL.json','s15/README.md'))]
        for n in [nested,*names]:
            dest=root/n
            assert dest.resolve().is_relative_to(root.resolve())
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(z.read(n))
    subprocess.run([sys.executable,str(root/'s15'/'prepare_source.py'),'--archive',str(root/nested),
                    '--destination',str(root/'s14_source')],check=True,stdout=sys.stderr)
    for policy in POLICIES:
        subprocess.run([sys.executable,str(HERE/'fusion_worker.py'),'--intake',str(root),
                        '--out',str(root/('final'+policy.split('_')[1])),'--policy',policy],
                       check=True,stdout=sys.stderr)


def differences(a,b,key=()):
    if isinstance(a,dict) and isinstance(b,dict) and a.keys()==b.keys():
        for k in a:
            yield from differences(a[k],b[k],key+(k,))
    elif isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
        for i,(u,v) in enumerate(zip(a,b)):
            yield from differences(u,v,key+(i,))
    elif a!=b:
        yield key


def compare_evidence(root,archive,policy,reverse):
    work=root/('final'+policy.split('_')[1])
    log=json.loads((work/'C2_INTEGRATION.json').read_text())
    prefix='s15/formal/run1/'+policy+'/'
    archive_rows=json.loads(archive.read(prefix+'DETERMINISTIC.json'))['steps']
    assert len(log['selected'])==len(archive_rows)==48
    output_hashes=[]
    output_bytes=0
    for i,r in enumerate(archive_rows):
        blob=(work/'outputs'/f'{i:03d}.json').read_bytes()
        wanted=r['output_sha256']
        assert blob==gzip.decompress(archive.read('s15/formal/output_pool/'+wanted+'.json.gz'))
        assert digest(blob)==wanted and len(blob)==r['output_bytes']
        assert log['selected'][i]==[i,r['plan']['method']]
        output_bytes+=len(blob)
        output_hashes.append(wanted)
    active=reverse['schedules'][policy]['work11_selected_full_steps']
    assert [x['step'] for x in log['cones']]==active and len(active)==47
    from_support=sum(reverse['steps'][i]['copy_saving_from_input'] for i in active)
    assert from_support==log['counts']['saved_copied_entries']
    for c in log['cones']:
        r=reverse['steps'][c['step']]
        assert c['local_window_sha256']==r['local_window_sha256']
        assert c['four_leaf_sizes']==r['four_leaf_support_sizes']

    exact_files=('CHECKS.json','CACHE_EVENTS.json','OPERATIONS.json')
    for name in exact_files:
        assert json.loads((work/name).read_bytes())==json.loads(archive.read(prefix+name))
    # Object-size calibration may differ across Python builds, as do hashes that include it.
    # Accept each permitted field by exact path and preserve difference counts separately.
    profiles={
      'PREDICTIONS.jsonl':{('row','learner_digest_before'),('row','candidates','row','decision_tie_key','first')},
      'PREDICTION_HASHES.json':{('row','sha256')},
      'TRAINING_EVENTS.json':{('row','selected_receipt_sha256'),('row','prediction_sha256')},
      'CALIBRATION_ONLINE.json':{('row','learner_after'),('row','learner_before'),('row','selected_receipt_sha256'),('row','prediction_sha256')},
      'CALIBRATION_PAIRS.json':{('row','prediction_sha256')},
      'DETERMINISTIC.json':{('steps','row','cache',k) for k in ('peak_sum_entry_reachable_bytes','sum_entry_reachable_bytes','summary_peak_bytes')},
      'CALIBRATION_STATE.json':{('reachable_bytes',),('digest',)},
    }
    observed={}
    for name,allowed in profiles.items():
        parse=(lambda blob:[json.loads(x) for x in blob.splitlines()]) if name.endswith('.jsonl') else json.loads
        diff=Counter()
        for path in differences(parse((work/name).read_bytes()),parse(archive.read(prefix+name))):
            clean=tuple(('first' if i==len(path)-1 and k==0 and i and path[i-1]=='decision_tie_key' else 'row')
                        if isinstance(k,int) else k for i,k in enumerate(path))
            assert clean in allowed,(name,path)
            diff['/'.join(clean)]+=1
        observed[name]=dict(diff)
    online=json.loads((work/'OPERATIONS.json').read_bytes())['online']['ring']
    baseline=[online[k] for k in FIELDS]
    replacement=baseline.copy()
    replacement[0]-=log['counts']['saved_copied_entries']
    assert log['counts']['actual_copied_entries']+log['counts']['saved_copied_entries']==log['counts']['baseline_copied_entries']
    deterministic=dict(policy=policy,full_steps=active,tree_steps=[i for i in range(48) if i not in active],
      exact_checks=len(json.loads((work/'CHECKS.json').read_bytes())),equal_complete_output_files=48,output_bytes=output_bytes,
      aggregate_output_sha256=digest(''.join(output_hashes).encode()),
      aggregate_true_window_sha256=digest(''.join(x['local_window_sha256'] for x in log['cones']).encode()),
      active_window_sizes_at_step6=next(x['four_leaf_sizes'] for x in log['cones'] if x['step']==6),
      counts=log['counts'], actual_ordered_ledger_sha256=log['ordered_ledger_sha256'],
      independent_input_support_copy_saving=from_support,
      exact_archive_ledger_families=list(exact_files),checked_semantic_files=list(profiles),
      online_FIVE_logical=baseline,online_one_coordinate_replacement=replacement)
    timing=json.loads((work/'TIMING.json').read_bytes())
    return deterministic,dict(process=log['measured'],reference_phase_seconds=timing['total_cost_seconds'],
                              platform_metadata_differences=observed)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--s15',required=True,type=Path)
    parser.add_argument('--c2',required=True,type=Path)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--workdir',type=Path,help='new directory for two fresh, serial scientific processes')
    mode.add_argument('--audit-dir',type=Path,help='existing intake containing completed final65, final195')
    parser.add_argument('--measure',type=Path,help='write environment-specific costs and metadata divergence')
    args=parser.parse_args()
    assert digest(args.s15.read_bytes())==S15 and digest(args.c2.read_bytes())==C2
    if args.workdir:
        restore(args.s15,args.workdir.resolve())
    root=(args.workdir or args.audit_dir).resolve()
    reverse=reverse_windows(args.s15,args.c2)
    output=[]
    machine={}
    with ZipFile(args.s15) as archive:
        for policy in POLICIES:
            result,measure=compare_evidence(root,archive,policy,reverse)
            output.append(result)
            machine[policy]=measure
    if args.measure:
        args.measure.write_text(json.dumps(machine,sort_keys=True,indent=2)+'\n')
    result=dict(task='RS-BRC-FUSION-C2-OWNERSHIP-REFERENCE-INTEGRATION-20261005',
                source_archive_sha256=dict(s15=S15,four_leaf=C2),
                policy='selected online full FFT work 11, level 6 butterfly 129 followed by level 7 butterflies 129 and 161',
                coordinate_order=list(FIELDS),terminal_slots_for_inverse=list(range(1,512,32)),budgets=output)
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
