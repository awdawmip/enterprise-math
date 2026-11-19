"""Account for structural work, recorded full source runs, certification and output."""
import argparse
from collections import Counter
import json
import resource
import sys
from tempfile import TemporaryFile
import time

sys.dont_write_bytecode=True
from verify import HERE, check_manifest, parse, require, verify


def structural_cost(rows):
    local=0
    stored_steps=0
    by_length=Counter()
    for row in rows:
        by_length[row['ticks']]+=1
        stored_steps+=len(row['steps'])
        for step in row['steps'][:-1]:
            support={node[0] for node in step['patch']}
            local+=len(support | {v ^ (4>>j) for v in support for j in range(3)})
    return {'cases':len(rows),'reference_transitions':sum(r['full_checks'] for r in rows),
            'reference_material_node_evaluations':8*sum(r['full_checks'] for r in rows),
            'local_material_node_evaluations':local,'explicit_prefix_states':stored_steps,
            'first_recovery_tick_histogram':dict(sorted(by_length.items()))}


def structural_check(record,structure):
    for name in ('reference','repair'):
        part=record[name]
        operations=part.get('operations',part)
        require(operations['exact_full_fields_and_all_labelled_increments']
                ==structure['reference_transitions'], 'paid_full_comparisons',name)
        key='literal_ticks' if name=='reference' else 'recomputed_material_nodes'
        amount=(structure['reference_transitions'] if name=='reference'
                else structure['local_material_node_evaluations'])
        require(operations[key]==amount,'source_operation_total',key)
        for k in ('cpu_seconds','wall_seconds','peak_rss_kib'):
            require(isinstance(part[k],(int,float)) and part[k]>0,'source_measured_'+k,name)
        require(part['cpu_seconds']<=1800 and part['peak_rss_kib']<=1048576,
                'recorded_budget_limit',name)
        require(isinstance(part['brc_counts'],dict) and bool(part['brc_counts']) and
                all(isinstance(v,int) and v>=0 for v in part['brc_counts'].values()),
                'source_brc_operations',name)
        require(isinstance(part['brc_max_bits'],dict) and max(part['brc_max_bits'].values())>0,
                'source_brc_max_bits',name)


def report(directory):
    manifest=parse((directory/'INPUT_MANIFEST.json').read_text())
    check_manifest(manifest)
    costs=parse((directory/manifest['cost']).read_text())
    casebytes=(directory/manifest['certificate']).read_bytes()
    rows=[parse(line) for line in casebytes.splitlines()]
    structure=structural_cost(rows)
    structural_check(costs,structure)
    before=time.perf_counter()
    cpu=time.process_time()
    checks=verify(directory/'INPUT_MANIFEST.json',144,256,True)
    measured={'wall_seconds':time.perf_counter()-before,'cpu_seconds':time.process_time()-cpu,
              'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    before=time.perf_counter()
    cpu=time.process_time()
    # Serialize all certificate rows with the producer's contract and write the bytes.
    reproduced=b''.join((json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
                        for r in rows)
    require(reproduced==casebytes,'case_output_byte_accounting')
    with TemporaryFile() as output:
        written=output.write(reproduced)
        output.flush()
    paid={'bytes_written':written,'wall_seconds':time.perf_counter()-before,
          'cpu_seconds':time.process_time()-cpu}
    return {'structural_recount':structure,'frozen_source_benchmark':costs,
            'fresh_checker':{'result':checks,'resources':measured},
            'fresh_certificate_serialization_and_write':paid}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--include-certification',action='store_true',required=True)
    p.add_argument('--include-output',action='store_true',required=True)
    p.parse_args()
    try:
        result=report(HERE)
    except (OSError,KeyError,TypeError,ValueError) as e:
        print(f'REJECTED {e}',file=sys.stderr)
        return 1
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
