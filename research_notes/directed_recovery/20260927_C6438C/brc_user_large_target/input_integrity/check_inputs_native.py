"""One native input-consistency run; supplied p/q never enter a factoring runner."""
from pathlib import Path
import argparse
import gzip
import hashlib
import importlib.util
import json
import traceback

ROOT=Path(__file__).resolve().parent
ADJ=ROOT.parents[1]/'sep27-brc-adjacent-trace'
ADJ_SHA='d1b0d497ecf8c028e6f4cec8b8322f47d30fa2437c2828825bd79f727d3dda87'
ACTIVITY='RA-CAAAC604CB513AEA8BBC1DFC'
INPUTS={'N_complete':505246541734676269885345827299505246541734676269885345827299,
        'displayed_block':505246541734676269885345827299,
        'supplied_p':670915268711887,'supplied_q':753070566876077}


def sha(raw): return hashlib.sha256(raw).hexdigest()


def require(value,message):
    if not value: raise ValueError(message)


def write_json(path,value):
    with path.open('x',encoding='utf-8') as f:
        f.write(json.dumps(value,indent=2,sort_keys=True)+'\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--guard-file',required=True)
    parser.add_argument('--guard-record-sha256',required=True)
    parser.add_argument('--global-knowledge-sha',required=True)
    args=parser.parse_args()
    require(len(args.global_knowledge_sha)==40 and all(c in '0123456789abcdef' for c in args.global_knowledge_sha),'knowledge SHA format')
    for name in ('STARTED.json','INPUT_RESULTS.json.gz','INPUT_SUMMARY.json','FAILED.json.gz'):
        require(not (ROOT/name).exists(),'refuse rerun/overwrite '+name)
    guardraw=Path(args.guard_file).read_bytes(); guard=json.loads(guardraw)
    require(guard['activity_id']==ACTIVITY,'wrong activity')
    require(guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[],'guard not clear')
    require(guard['record_sha256']==args.guard_record_sha256,'guard record mismatch')
    helperpath=ADJ/'adjacent_trace.py'
    require(sha(helperpath.read_bytes())==ADJ_SHA,'frozen helper mismatch')
    spec=importlib.util.spec_from_file_location('input_check_adjacent_helper',helperpath)
    helper=importlib.util.module_from_spec(spec); spec.loader.exec_module(helper)
    helper.check_dependencies()
    binding={'source_sha256':sha(Path(__file__).read_bytes()),'plan_sha256':sha((ROOT/'PLAN.md').read_bytes()),
        'adjacent_helper_sha256':ADJ_SHA,'guard_path':str(Path(args.guard_file)),
        'guard_sha256':sha(guardraw),'guard':guard,'inputs':INPUTS,
        'coordinator_actual_global_knowledge_read_sha':args.global_knowledge_sha}
    write_json(ROOT/'STARTED.json',binding)
    payload={'schema':'BRC_USER_INPUT_INTEGRITY_V1','binding':binding,'stage':'IMPORT_FROZEN_WRAPPERS'}
    arithmetic=None; old=None
    try:
        free,hbw=helper.load_frozen(); old=hbw.old
        payload['stage']='SOURCE_ADMISSION'
        payload['native_source']=old.source_check()
        arithmetic=old.lm.Arithmetic()
        payload['stage']='MULTIPLY_SUPPLIED_LABELS'
        product,mul_id=arithmetic.multiply(INPUTS['supplied_p'],INPUTS['supplied_q'])
        payload['product']=product; payload['product_operation']=mul_id
        payload['stage']='COMPARE_COMPLETE'
        complete_relation,complete_difference,complete_id=arithmetic.compare(product,INPUTS['N_complete'])
        payload['complete_comparison']={'relation':complete_relation,'low_difference':complete_difference,'operation':complete_id}
        payload['stage']='COMPARE_DISPLAYED_BLOCK'
        block_relation,block_difference,block_id=arithmetic.compare(product,INPUTS['displayed_block'])
        payload['block_comparison']={'relation':block_relation,'low_difference':block_difference,'operation':block_id}
        payload['stage']='DIVIDE_COMPLETE_BY_PRODUCT'
        quotient,remainder,div_id=arithmetic.divide(INPUTS['N_complete'],product)
        payload['complete_division']={'quotient':quotient,'remainder':remainder,'operation':div_id}
        helper.check_dependencies()
        require(sha(helperpath.read_bytes())==ADJ_SHA,'helper changed during run')
        require(sha(Path(__file__).read_bytes())==binding['source_sha256'],'source changed during run')
        require(sha((ROOT/'PLAN.md').read_bytes())==binding['plan_sha256'],'plan changed during run')
        require(sha(Path(args.guard_file).read_bytes())==binding['guard_sha256'],'guard changed during run')
        payload.update(status='COMPLETE_NATIVE_INPUT_CONSISTENCY_NOT_FACTORING',stage='COMPLETE',
            product_equals_complete=complete_relation==0,product_equals_block=block_relation==0,
            complete_divisible_by_product=remainder==0,arithmetic_operations=arithmetic.operations,
            arithmetic_cost=arithmetic.stats,all_native_records=old.CALLS)
        raw=json.dumps(payload,sort_keys=True,separators=(',',':'),default=old.plain).encode()
        packed=gzip.compress(raw,mtime=0)
        with (ROOT/'INPUT_RESULTS.json.gz').open('xb') as f:f.write(packed)
        summary={k:payload[k] for k in ('schema','status','product','product_equals_complete','product_equals_block','complete_divisible_by_product','complete_division','arithmetic_cost')}
        summary.update(inputs=INPUTS,source_sha256=binding['source_sha256'],plan_sha256=binding['plan_sha256'],
            raw_bytes=len(raw),raw_sha256=sha(raw),gzip_bytes=len(packed),gzip_sha256=sha(packed),
            actual_native_calls=len(old.CALLS),scope='Input consistency only; p/q not admitted to blind search; no primality proof')
        write_json(ROOT/'INPUT_SUMMARY.json',summary)
        print(json.dumps(summary,indent=2))
    except BaseException as error:
        payload.update(status='FAILED_NOT_RESUMABLE',error_type=type(error).__name__,error=str(error),traceback=traceback.format_exc())
        if arithmetic is not None:payload.update(arithmetic_operations=arithmetic.operations,arithmetic_cost=arithmetic.stats)
        if old is not None:payload['all_native_records']=old.CALLS
        raw=json.dumps(payload,sort_keys=True,default=old.plain if old else None).encode()
        with (ROOT/'FAILED.json.gz').open('xb') as f:f.write(gzip.compress(raw,mtime=0))
        raise


if __name__=='__main__':main()
