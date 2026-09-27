"""Saved-record-only audit; stdlib, no scientific import or answer oracle."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import ast
import gzip
import hashlib
import json

ROOT=Path(__file__).resolve().parent
FREE=ROOT.parent/'sep27-brc-hbw-free-trace'
ELLIPTIC=ROOT.parent/'sep27-brc-elliptic-mark'
OLD=ROOT.parent/'sep27-brc-native-tool-discovery'
PINS={
 'source':'d1b0d497ecf8c028e6f4cec8b8322f47d30fa2437c2828825bd79f727d3dda87',
 'plan':'590b59350b55e38121c3517cd8c94dd842fd562c0c36aaa619d1b44f4fb9c050',
 'native_reader':'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825',
 'hbw_reader':'6dda7b6c995c457c24334507adfc44574e197f120d41f7d0775fdf3815f26b98',
 'free_reader':'5c4bb5ab416376d922dc15bbc05f553686011ef89f7ca4060d138a870785533d',
 'elliptic_reader':'055609ee97e8e910dd343d0972fda8e152b039135cdf44d21095ae427b0d885c',
 'raw':'21eefcdd65c06eff0ef932eee3b0c80a0d62345273ef3c810daa8937b621b216',
 'gzip':'3d14f0eb84432a1f0b7b6a5ea3e7637b147c2acfa08519d7d482ed2fe177111f',
 'old_raw':'bd9ccd13f75e41b44edcfd294990ce1bd5673011fe906b4780c05662dfe70158',
 'old_gzip':'2b714edc7cd51728377ef5269451724feb96a8896af3037fcb60101ef09e37c5'}
METRICS=('adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
CATEGORIES=('setup','power','expressions','joint','single','quotient','validation')
SPECIAL={'common_coordinate_gcd','free_trace_setup','validation_matrix_power'}
sha=lambda raw:hashlib.sha256(raw).hexdigest()


def select(path,pin,names,rename=None):
    raw=path.read_bytes(); assert sha(raw)==pin
    nodes=[n for n in ast.parse(raw).body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in names]
    assert {n.name for n in nodes}==names
    for n in nodes: n.name=(rename or {}).get(n.name,n.name)
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path)+'::<record-only>','exec'),globals())


def links_for(step,route):
    return Links(dict(step,route=route))


def visit(index):
    global position
    node=wiring[index]; kind=node['kind']
    if kind in SPECIAL:
        if kind=='common_coordinate_gcd':
            counts['common_gcd_coordinates']+=len(node['coordinate_steps'])
            counts['common_gcd_euclid_divisions']+=sum(len(s['euclid']) for s in node['coordinate_steps'])
        return free_visit(index)
    if kind in ('addmod','submod','modmul','gcd_of_difference','matrix_product'):
        return hbw_visit(index)
    assert index==position and node['id']==index and node['status']=='COMPLETE'
    position+=1; r=cursors[node['route']]
    assert r.pos==node['direct_start']; counts['wiring_'+kind]+=1
    op=Links(node) if 'links' in node else None
    prefix=node['route'].rsplit('_',1)[0]; params=setups[prefix]
    if kind=='public_clock_relation_check':
        assert node['addition_operation']==r.pos
        ad=r.op('add'); assert (ad['left'],ad['right'])==(node['E'],2)
        assert ad['low']==node['actual_Eplus2']==node['declared_Eplus2']; result=True
    elif kind=='ordered_adjacent_trace_power':
        bits=format(node['E'],'b'); pair=[params['two'],params['k']]
        assert node['initial']==pair and node['k']==params['k'] and node['public_exponent_bits']==bits
        for i,(bit,step) in enumerate(zip(bits,node['steps'],strict=True)):
            assert step['bit_index']==i and step['bit']==bit and step['before']==pair and step['status']=='COMPLETE'
            sop=links_for(step,node['route'])
            product=sop.mul('adjacent_product',pair[0],pair[1]); odd=sop.sub('odd_trace',product,params['k'])
            selected=pair[0] if bit=='0' else pair[1]
            square=sop.mul('selected_square',selected,selected); even=sop.sub('selected_even_trace',square,params['two'])
            pair=[even,odd] if bit=='0' else [odd,even]
            assert step['after']==pair; sop.close(); counts['adjacent_bits']+=1
        assert node['public_bit_control']=={'bits_read':len(bits),'multiplications_per_bit':2,'subtractions_per_bit':2,'orientation':'(V_E,V_(E+1)); never folded'}
        result=pair
    elif kind=='both_signed_translated_expressions':
        pair=node['pair']; result={}
        for label,step in zip(('identity','antipodal'),node['signs'],strict=True):
            assert step['label']==label and step['status']=='COMPLETE'; sop=links_for(step,node['route'])
            if label=='identity':
                tau=sop.sub('tau',pair[0],params['two']); w=sop.sub('w',pair[1],params['k']); target=1
            else:
                tau=sop.add('tau',pair[0],params['two']); w=sop.add('w',pair[1],params['k']); target=params['negative_one']
            result[label]={'target':target,'tau':tau,'w':w}; assert step['output']==result[label]; sop.close()
    elif kind=='exact_two_clock_quotient':
        assert node['numerator']>0 and node['denominator']>0 and node['division_operation']==r.pos
        div=r.op('divide')
        assert (div['value'],div['modulus'])==(node['numerator'],node['denominator'])
        assert div['remainder']==node['remainder']==0 and div['quotient']==node['quotient']>=1
        assert node['factor_check_key']==saved_factor_check(r,div['quotient'])
        result={'value':div['quotient'],'class':classify(div['quotient'],r.r['N']),'remainder':0}
    elif kind=='full_matrix_signed_residual_ideal':
        m=node['matrix']; target=node['target']
        a=op.sub('residual_00',m[0][0],target); d=op.sub('residual_11',m[1][1],target)
        entries=[a,m[0][1],m[1][0],d]; g=op.common('all_four_entries_gcd',entries)
        result={'entries':entries,'common_gcd':g}
    elif kind=='independent_two_clock_full_matrix_validation':
        case=cases_by_prefix[prefix]; pair=case['terminal_pair']; E=case['inputs']['E']; E2=case['inputs']['Eplus2']; M=params['M']
        assert node['E']==E and node['Eplus2']==E2 and node['pair']==pair
        assert child(node['inverse_check_link'],'matrix_product',left=M,right=params['Minv'])==[[1,0],[0,1]]
        full=child(node['E_power_link'],'validation_matrix_power',matrix=M,E=E)
        full2=child(node['Eplus2_power_link'],'validation_matrix_power',matrix=M,E=E2)
        next_full=child(node['Eplus1_link'],'matrix_product',left=full,right=M)
        second_full=child(node['Eplus2_from_adjacency_link'],'matrix_product',left=next_full,right=M)
        assert full2==second_full==node['full_Eplus2'] and full==node['full_E'] and next_full==node['full_Eplus1']
        trace0=op.add('trace_E',full[0][0],full[1][1]); trace1=op.add('trace_Eplus1',next_full[0][0],next_full[1][1])
        assert pair==[trace0,trace1]
        dets=[]
        for label,m in (('E',full),('Eplus2',full2)):
            ad=op.mul(label+'_det_ad',m[0][0],m[1][1]); bc=op.mul(label+'_det_bc',m[0][1],m[1][0]); det=op.sub(label+'_det',ad,bc)
            assert det==1; dets.append({'clock':label,'value':det})
        assert dets==node['determinants']
        for label,check in zip(('identity','antipodal'),node['signed_checks'],strict=True):
            ex=case['expressions'][label]; observed=case['readouts'][label]
            assert check['label']==label and check['target']==ex['target'] and check['status']=='COMPLETE'
            sop=links_for(check,node['route'])
            first=child(check['E_ideal_link'],'full_matrix_signed_residual_ideal',matrix=full,target=ex['target'])
            second=child(check['Eplus2_ideal_link'],'full_matrix_signed_residual_ideal',matrix=full2,target=ex['target'])
            assert first['common_gcd']==observed['dE']==check['first_clock_gcd']
            assert second['common_gcd']==observed['dEplus2']['value']==check['second_clock_gcd']
            x,y=first['entries'][1],first['entries'][3]
            kx=sop.mul('k_x',params['k'],x); residual00=sop.sub('cyclic_residual_00',y,kx); neg=sop.sub('negative_x',0,x)
            assert first['entries']==[residual00,x,neg,y]
            dy=sop.add('two_y',y,y); tau=sop.sub('tau_from_cyclic_mark',dy,kx)
            ky=sop.mul('k_y',params['k'],y); dx=sop.add('two_x',x,x); w=sop.sub('w_from_cyclic_mark',ky,dx)
            assert tau==ex['tau']==check['tau'] and w==ex['w']==check['w']
            coprime=sop.common('clock_divisors_coprime',[first['common_gcd'],second['common_gcd']]); assert coprime==check['coprime']==1
            assert check['exact_product_operation']==r.pos; mul=r.op('multiply')
            assert (mul['left'],mul['right'])==(first['common_gcd'],second['common_gcd'])
            assert mul['value']==observed['dUnion']==check['product']; sop.close()
            counts['signed_full_two_clock_checks']+=1
        result={'both_adjacent_traces_equal':True,'full_E':full,'full_Eplus2':full2,'signed_checks':node['signed_checks']}
    else: raise AssertionError(kind)
    if op: op.close()
    assert result==node['output'] and r.pos==node['direct_stop'],(index,kind,r.pos)
    return result


def main():
    global data,catalog,counts,payload,routes,cursors,wiring,position,setups,cases_by_prefix
    destination=ROOT/'ADJACENT_TRACE_RECORD_REVIEW.json'; assert not destination.exists(),'refuse overwrite'
    packed=(ROOT/'ADJACENT_TRACE_RESULTS.json.gz').read_bytes(); raw=gzip.decompress(packed)
    assert (sha(raw),sha(packed),len(raw),len(packed))==(PINS['raw'],PINS['gzip'],3598285,192274)
    payload=json.loads(raw); summary=json.loads((ROOT/'ADJACENT_TRACE_SUMMARY.json').read_bytes()); binding=payload['binding']
    assert payload['schema']==summary['schema']=='BRC_ADJACENT_TRACE_TWO_CLOCK_V1'
    assert payload['status']==summary['status']=='PASS_FINITE_ADJACENT_TRACE_NOT_ADMITTED'
    assert sha((ROOT/'adjacent_trace.py').read_bytes())==binding['source_sha256']==summary['source_sha256']==PINS['source']
    assert sha((ROOT/'PLAN.md').read_bytes())==binding['plan_sha256']==summary['plan_sha256']==PINS['plan']
    assert (summary['raw_sha256'],summary['gzip_sha256'],summary['raw_bytes'],summary['gzip_bytes'])==(sha(raw),sha(packed),len(raw),len(packed))
    assert json.loads((ROOT/'STARTED.json').read_bytes())=={k:v for k,v in binding.items() if k!='reused_interfaces'}
    assert not (ROOT/'FAILED_EXECUTION.json.gz').exists() and not (ROOT/'FAILED_SERIALIZATION.txt').exists()
    guardraw=Path(binding['guard_path']).read_bytes(); guard=json.loads(guardraw)
    assert sha(guardraw)==binding['guard_sha256'] and guard==binding['guard']
    assert guard['record_sha256']==binding['expected_guard_record_sha256']=='d7f69e8e5666d281583eb01711b8fa99c8443fb6be99efab8485282c8989eaaf'
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    for root,key in ((FREE,'free_dependencies'),(ELLIPTIC,'elliptic_dependencies'),(OLD,'old_dependencies'),(ROOT,'local_dependencies')):
        for name,pin in binding[key].items(): assert sha((root/name).read_bytes())==pin
    data={'binding':binding['reused_interfaces']}; catalog=data['binding']['native_arithmetic']['native_adder']['columns']; counts=Counter()
    select(OLD/'read_native_port_review.py',PINS['native_reader'],{'trace','stream','inverse','gcd','audit_route','Records'})
    select(OLD/'hbw_marked_section/read_hbw_marked_records.py',PINS['hbw_reader'],{'child','visit'},{'visit':'hbw_visit'})
    select(FREE/'native_probe/read_free_trace_records.py',PINS['free_reader'],{'classify','saved_factor_check','visit'},{'visit':'free_visit'})
    select(ELLIPTIC/'read_elliptic_records.py',PINS['elliptic_reader'],{'Links'})
    for path,pin in data['binding']['files'].items(): assert sha(Path(path).read_bytes())==pin
    assert sha((OLD/'native_relative_port.py').read_bytes())==data['binding']['new_source_sha256']
    assert sha((OLD/'EXPERIMENT_PLAN.md').read_bytes())==data['binding']['plan_sha256']
    for name,path in {'sparse_modular':'D:/em/TEMP/sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'D:/em/TEMP/sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert sha(Path(path).read_bytes())==data['binding']['native_arithmetic']['files_sha256'][name]
    hist=Path('D:/em/TEMP/sep26-local-takeover/activity_closeout/src/enterprise_math/brc_histogram.py').read_bytes()
    assert hashlib.sha1(b'blob '+str(len(hist)).encode()+b'\0'+hist).hexdigest()==data['binding']['histogram_blob']
    vendor=Path('D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py').read_bytes()
    assert sha(vendor)==data['binding']['native_arithmetic']['native_adder']['vendor']['sha256']
    assert len(payload['all_native_records'])==summary['total_native_calls']==payload['native_catalog_calls_after_source_admission']==summary['native_catalog_calls_after_source_admission']==1
    native=payload['all_native_records'][0]; assert (native['entrypoint'],native['states'],native['depth'])==('recurrent_mass_power',12,1)
    routes=payload['routes']; audits={name:audit_route(route) for name,route in routes.items()}; cursors={name:Records(route) for name,route in routes.items()}
    total=sum((Counter(row['total']) for row in audits.values()),Counter())
    for name,audit in audits.items():
        cost=payload['costs'][name]
        assert {k:audit['total'][k] for k in METRICS}=={k:cost[k] for k in METRICS}
        assert cost['direct_typed_operations']==len(routes[name]['arithmetic_operations']) and cost['route_invocations']==routes[name]['calls']
        assert not routes[name]['tables'] and not routes[name]['inverses']
    assert {k:total[k] for k in METRICS}==summary['total_cost']
    wiring=payload['wiring']; position=0; setups={}; cases_by_prefix={'case'+str(i):c for i,c in enumerate(payload['cases'])}
    grid=((77,3,4,6),(77,3,8,10),(49,3,8,10),(77,3,6,8)); reports=[]
    assert binding['inputs']==[{'N':N,'k':k,'E':E,'Eplus2':E2} for N,k,E,E2 in grid]
    for i,(case,small,(N,k,E,E2)) in enumerate(zip(payload['cases'],summary['cases'],grid,strict=True)):
        prefix='case'+str(i); names={c:prefix+'_'+c for c in CATEGORIES}
        assert case['inputs']==small['inputs']=={'N':N,'k':k,'E':E,'Eplus2':E2} and case['route_names']==names
        parameters=child(case['setup_link'],'free_trace_setup',N=N,k=k,route=names['setup']); assert parameters==case['setup']==small['setup'] and parameters['status']=='REGULAR'
        assert child(case['clock_relation_link'],'public_clock_relation_check',E=E,declared_Eplus2=E2,route=names['setup']) is True
        pair=child(case['power_link'],'ordered_adjacent_trace_power',E=E,k=k,route=names['power']); assert pair==case['terminal_pair']==small['terminal_pair']
        ex=child(case['expressions_link'],'both_signed_translated_expressions',pair=pair,route=names['expressions']); assert ex==case['expressions']==small['expressions']
        assert set(case['readouts'])=={'identity','antipodal'}
        for label in ('identity','antipodal'):
            row=case['readouts'][label]; assert row==small['readouts'][label] and row['target']==ex[label]['target']
            dE=child(row['joint_link'],'common_coordinate_gcd',values=[ex[label]['tau'],ex[label]['w']],route=names['joint'])
            assert dE==row['dE'] and classify(dE,N)==row['dE_class']
            union=child(row['single_link'],'gcd_of_difference',inputs=[ex[label]['w'],0],route=names['single'])
            assert union==row['dUnion'] and classify(union,N)==row['dUnion_class']
            second=child(row['quotient_link'],'exact_two_clock_quotient',numerator=union,denominator=dE,route=names['quotient']); assert second==row['dEplus2']
        validation=child(case['validation_link'],'independent_two_clock_full_matrix_validation',E=E,Eplus2=E2,pair=pair,route=names['validation'])
        assert validation==case['validation']==small['validation']
        assert case['status']==small['status']=='COMPLETE_FINITE_TWO_CLOCK_OBSERVATION_NOT_SUCCESS_RATE'
        assert small['costs']=={category:payload['costs'][name] for category,name in names.items()}
        reports.append({'inputs':case['inputs'],'terminal_pair':pair,'expressions':ex,'readouts':case['readouts'],
             'category_digits':{c:audits[names[c]]['total']['adder_digit_replays'] for c in CATEGORIES},
             'production_digits_all_requested_probes':sum(audits[names[c]]['total']['adder_digit_replays'] for c in CATEGORIES if c!='validation'),
             'paired_case':i<3})
    assert position==len(wiring)
    for cursor in cursors.values(): cursor.close()
    assert total['adder_digit_replays']==counts['checked_native_digit_cells'] and total['typed_operations']==counts['checked_top_level_operations']
    assert set(routes)=={name for c in payload['cases'] for name in c['route_names'].values()}
    categories={c:{key:sum(audits[case['route_names'][c]]['total'][key] for case in payload['cases']) for key in METRICS} for c in CATEGORIES}
    assert categories==summary['category_totals']
    old_packed=(FREE/'native_probe/FREE_TRACE_RESULTS.json.gz').read_bytes(); old_raw=gzip.decompress(old_packed)
    assert (sha(old_packed),sha(old_raw),len(old_packed),len(old_raw))==(PINS['old_gzip'],PINS['old_raw'],109481,1822824)
    old=json.loads(old_raw); comparison=payload['saved_baseline_comparison']; assert comparison==summary['saved_baseline_comparison']
    assert comparison['compressed_sha256']==sha(old_packed) and comparison['raw_sha256']==sha(old_raw)
    assert comparison['compressed_bytes']==len(old_packed) and comparison['raw_bytes']==len(old_raw)
    assert comparison['unpaired_case_index']==3 and comparison['new_scientific_execution_of_old_program'] is False and comparison['equal_output_end_to_end_ratio_claimed'] is False
    for i,(match,oc,nc) in enumerate(zip(comparison['matched'],old['cases'],payload['cases'][:3],strict=True)):
        inp={k:nc['inputs'][k] for k in ('N','k','E')}; assert match['case_index']==i and match['inputs']==oc['inputs']==inp and match['common_outputs_equal'] is True
        assert oc['setup']==nc['setup'] and oc['probes']['trace']==nc['terminal_pair'][0]
        for label in ('identity','antipodal'):
            assert oc['probes']['signed'][label]['joint_gcd']==nc['readouts'][label]['dE']
            assert oc['probes']['signed'][label]['joint_class']==nc['readouts'][label]['dE_class']
        assert match['historical_probes_with_extra_outputs_preserved']==oc['probes']
        assert match['historical_costs']=={c:old['costs'][name] for c,name in oc['route_names'].items()}
        reports[i]['historical_component_digits']={c:v['adder_digit_replays'] for c,v in match['historical_costs'].items()}
    receipt_raw=(ROOT/'ACTUAL_EXECUTION_TOOL_RESULT.json').read_bytes(); receipt=json.loads(receipt_raw)
    assert receipt['tool_name']=='exec_command' and receipt['result']['chunk_id']=='c117ac' and receipt['result']['exit_code']==0
    assert json.loads(receipt['result']['output'])==summary
    report={'status':'PASS_STDLIB_ADJACENT_TRACE_SAVED_RECORD_REVIEW_NOT_ADMISSION','reader_sha256':sha(Path(__file__).read_bytes()),
      'source_pins':PINS,'binding':binding,'raw_sha256':sha(raw),'gzip_sha256':sha(packed),'raw_bytes':len(raw),'gzip_bytes':len(packed),
      'summary_sha256':sha((ROOT/'ADJACENT_TRACE_SUMMARY.json').read_bytes()),'counts':dict(counts),'wiring_nodes':len(wiring),
      'route_audits':audits,'total_cost':dict(total),'category_totals':categories,'native_records':payload['all_native_records'],'cases':reports,
      'actual_tool_receipt_sha256':sha(receipt_raw),'actual_tool_chunk_id':'c117ac',
      'scope':['Every saved native digit cell, typed operation and chronological outer link consumed.',
       'All eight exact quotient divisions, proper-factor certificates and full-matrix two-clock checks consumed.',
       'No scientific imports, rerun, host gcd/pow or modular answer recomputation.',
       'Old saved baseline is equality/cost data only; fourth case excluded from matched comparisons.',
       'Standard-library administrative counts and comparisons; shared-context audit, not admission.']}
    with destination.open('x',encoding='utf-8') as f:f.write(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:report[k] for k in ('status','counts','wiring_nodes','total_cost','category_totals','cases')},indent=2))


if __name__=='__main__': main()
