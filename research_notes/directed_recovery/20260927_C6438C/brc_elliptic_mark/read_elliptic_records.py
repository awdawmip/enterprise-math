"""Stdlib-only saved-record audit. No scientific import or answer recomputation."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import ast
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent/'sep27-brc-native-tool-discovery'
PROOFS = ROOT.parent/'sep27-brc-hbw-free-trace'
PINS = {
 'source':'a0186eb10a02f7ad3ed4106cd1395d495379e18e12f03b82b212db7c90fb60da',
 'plan':'8f8660262c7b60fc20def4ddc58164757aa908b9c1854d948bd0093fcb0599fc',
 'native_reader':'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825',
 'hbw_reader':'6dda7b6c995c457c24334507adfc44574e197f120d41f7d0775fdf3815f26b98',
 'free_reader':'5c4bb5ab416376d922dc15bbc05f553686011ef89f7ca4060d138a870785533d',
 'raw':'6a2d9b2243f14c73faa5352af041e850b4fcb3d0cb63215ea31277143f7d46da',
 'gzip':'3f381e2603b9a512f0aea2dd9eb3c8087e36487a7651b742ff2ab49408550c9b'}
METRICS = ('adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
sha = lambda raw: hashlib.sha256(raw).hexdigest()


def selected(path, pin, names, rename=None):
    raw = path.read_bytes(); assert sha(raw) == pin
    nodes = [n for n in ast.parse(raw).body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in names]
    assert {n.name for n in nodes} == names
    for n in nodes:
        n.name = (rename or {}).get(n.name,n.name)
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path)+'::<record-only>', 'exec'),globals())


class Links:
    def __init__(self,node):
        self.node,self.pos = node,0
    def get(self,role,kind,**expected):
        saved = self.node['links'][self.pos]; self.pos += 1
        assert saved['role'] == role
        assert wiring[saved['wiring_id']]['route'] == self.node['route']
        return child(saved['wiring_id'],kind,**expected)
    def calc(self,role,kind,x,y):
        return self.get(role,kind,inputs=[x,y])
    def add(self,role,x,y): return self.calc(role,'addmod',x,y)
    def sub(self,role,x,y): return self.calc(role,'submod',x,y)
    def mul(self,role,x,y): return self.calc(role,'modmul',x,y)
    def gcd(self,role,x): return self.calc(role,'gcd_of_difference',x,0)
    def common(self,role,values): return self.get(role,'common_coordinate_gcd',values=values)
    def close(self): assert self.pos == len(self.node['links'])


def visit(index):
    global position
    node = wiring[index]; kind = node['kind']
    if kind in ('addmod','submod','modmul','gcd_of_difference'):
        return base_visit(index)
    assert index == position and node['id'] == index and node['status'] == 'COMPLETE'
    position += 1
    r = cursors[node['route']]
    assert r.pos == node['direct_start']
    counts['wiring_'+kind] += 1
    op = Links(node) if 'links' in node else None
    if kind == 'common_coordinate_gcd':
        assert node['N'] == r.r['N']
        r.calls['common_gcd_requests'] += 1
        current = r.r['N']
        for value,step in zip(node['values'],node['coordinate_steps'],strict=True):
            assert (step['left'],step['right']) == (current,value)
            left,right = current,value
            for item in step['euclid']:
                assert right != 0 and (item['left'],item['right']) == (left,right)
                assert item['division_operation'] == r.pos
                division = r.op('divide')
                assert (division['value'],division['modulus']) == (left,right)
                assert (division['quotient'],division['remainder']) == (item['quotient'],item['remainder'])
                assert 0 <= division['remainder'] < right
                left,right = right,division['remainder']
                counts['common_gcd_euclid_divisions'] += 1
            assert right == 0 and step['gcd'] == left
            current = left
            counts['common_gcd_coordinates'] += 1
        assert node['factor_check_key'] == saved_factor_check(r,current)
        result = current
    elif kind == 'montgomery_setup':
        N,A = node['N'],node['A']; assert N == r.r['N']
        assert node['odd_modulus_operation'] == r.pos
        d = r.op('divide')
        assert (d['value'],d['modulus'],d['remainder'],d['quotient']) == (N,2,1,node['odd_modulus_quotient'])
        two = op.add('two',1,1); three = op.add('three',two,1)
        four = op.add('four',two,two); eight = op.add('eight',four,four)
        ten = op.add('ten',eight,two); fourA = op.mul('four_A',four,A)
        B = op.add('B',ten,fourA); A2 = op.mul('A_square',A,A)
        disc = op.sub('discriminant',A2,four); product = op.mul('smoothness_product',B,disc)
        gs = [op.gcd('B_gcd',B),op.gcd('discriminant_gcd',disc),op.gcd('smoothness_gcd',product),op.gcd('base_x_gcd',two)]
        x2 = op.mul('base_x_square',two,two); x3 = op.mul('base_x_cube',x2,two)
        ax2 = op.mul('A_base_x_square',A,x2)
        partial = op.add('base_rhs_partial',x3,ax2); rhs = op.add('base_rhs',partial,two)
        assert B == rhs and gs == [1,1,1,1]
        result = {'N':N,'A':A,'B':B,'discriminant':disc,'smoothness_product':product,
                  'setup_gcds':gs,'status':'REGULAR','proper_setup_factors':[],
                  'P_affine':[two,1],'P_xz':[two,1],
                  'constants':{'two':two,'three':three,'four':four,'eight':eight},
                  'membership_lhs':B,'membership_rhs':rhs}
        setups[node['route'].removesuffix('_setup')] = result
    elif kind == 'kummer_double':
        X,Z = node['point']; A = node['A']; params = setups[node['route'].removesuffix('_ladder')]
        assert A == params['A']
        x2=op.mul('X_square',X,X); z2=op.mul('Z_square',Z,Z)
        difference=op.sub('square_difference',x2,z2); nx=op.mul('new_X',difference,difference)
        xz=op.mul('XZ',X,Z); axz=op.mul('A_XZ',A,xz)
        partial=op.add('quadratic_partial',x2,axz); quad=op.add('quadratic',partial,z2)
        fourxz=op.mul('four_XZ',params['constants']['four'],xz)
        nz=op.mul('new_Z',fourxz,quad); result=[nx,nz]
    elif kind == 'fixed_difference_add':
        left,right,difference=node['left'],node['right'],node['difference']
        params=setups[node['route'].removesuffix('_ladder')]
        assert difference == params['P_xz'] and node['relation']=='left-right=+-fixed_P'
        xx=op.mul('X_left_X_right',left[0],right[0]); zz=op.mul('Z_left_Z_right',left[1],right[1])
        first=op.sub('first_factor',xx,zz); first2=op.mul('first_factor_square',first,first)
        nx=op.mul('new_X',difference[1],first2)
        xz=op.mul('X_left_Z_right',left[0],right[1]); zx=op.mul('Z_left_X_right',left[1],right[0])
        second=op.sub('second_factor',xz,zx); second2=op.mul('second_factor_square',second,second)
        nz=op.mul('new_Z',difference[0],second2); result=[nx,nz]
    elif kind == 'montgomery_ladder':
        params=setups[node['route'].removesuffix('_ladder')]
        bits=format(node['E'],'b'); R0,R1=[1,0],params['P_xz']
        assert node['public_exponent_bits']==bits and node['initial']==[R0,R1]
        assert node['chart_certificate']=='GEOMETRIC_NEXT_TOOL fixed unit difference'
        for i,(bit,step) in enumerate(zip(bits,node['steps'],strict=True)):
            assert step['bit_index']==i and step['bit']==bit and step['before']==[R0,R1] and step['status']=='COMPLETE'
            added=child(step['addition_link'],'fixed_difference_add',left=R0,right=R1,difference=params['P_xz'])
            doubled=child(step['doubling_link'],'kummer_double',point=R0 if bit=='0' else R1,A=params['A'])
            R0,R1=(doubled,added) if bit=='0' else (added,doubled)
            assert step['after']==[R0,R1]
        assert node['public_bit_control']=={'bits_read':len(bits),'add_dispatches':len(bits),'double_dispatches':len(bits)}
        result=[R0,R1]
    elif kind == 'translated_mark_expression':
        params=setups[node['route'].removesuffix('_mark_expression')]
        assert node['a']==params['P_affine'][0]
        az=op.mul('a_Z1',node['a'],node['pair'][1][1])
        result=op.sub('W',node['pair'][1][0],az)
    elif kind == 'scalar_factor_readout':
        g=op.gcd('gcd',node['value']); result={'value':g,'class':classify(g,r.r['N'])}
    elif kind == 'marked_common_readout':
        g=op.common('common_gcd',node['values']); result={'value':g,'class':classify(g,r.r['N'])}
    elif kind == 'jacobian_double_validation':
        X,Y,Z=node['point']; a2,a4=node['a2'],node['a4']
        constants=setups[node['route'].removesuffix('_validation')]['constants']
        x2=op.mul('X_square',X,X); y2=op.mul('Y_square',Y,Y); z2=op.mul('Z_square',Z,Z)
        z4=op.mul('Z_fourth',z2,z2); y4=op.mul('Y_fourth',y2,y2)
        yz=op.mul('YZ',Y,Z); nz=op.mul('new_Z',constants['two'],yz)
        m0=op.mul('three_X_square',constants['three'],x2); xz2=op.mul('X_Z_square',X,z2)
        a2xz2=op.mul('a2_X_Z_square',a2,xz2); m1=op.mul('two_a2_X_Z_square',constants['two'],a2xz2)
        m2=op.mul('a4_Z_fourth',a4,z4); partial=op.add('M_partial',m0,m1); M=op.add('M',partial,m2)
        xy2=op.mul('X_Y_square',X,y2); S=op.mul('S',constants['four'],xy2)
        ms=op.mul('M_square',M,M); ts=op.mul('two_S',constants['two'],S)
        nz2=op.mul('new_Z_square',nz,nz); a2nz2=op.mul('a2_new_Z_square',a2,nz2)
        xp=op.sub('new_X_partial',ms,ts); nx=op.sub('new_X',xp,a2nz2)
        diff=op.sub('S_minus_new_X',S,nx); yp=op.mul('M_times_difference',M,diff)
        ey4=op.mul('eight_Y_fourth',constants['eight'],y4); ny=op.sub('new_Y',yp,ey4)
        result=[nx,ny,nz]
    elif kind == 'jacobian_curve_and_primitive_check':
        X,Y,Z=node['point']; a2,a4=node['a2'],node['a4']
        lhs=op.mul('Y_square',Y,Y); x2=op.mul('X_square',X,X); x3=op.mul('X_cube',x2,X)
        z2=op.mul('Z_square',Z,Z); z4=op.mul('Z_fourth',z2,z2)
        x2z2=op.mul('X_square_Z_square',x2,z2); t2=op.mul('a2_term',a2,x2z2)
        xz4=op.mul('X_Z_fourth',X,z4); t4=op.mul('a4_term',a4,xz4)
        partial=op.add('rhs_partial',x3,t2); rhs=op.add('rhs',partial,t4)
        primitive=op.common('primitive_gcd',node['point'])
        assert lhs==rhs==node['lhs']==node['rhs'] and primitive==node['primitive_gcd']==1
        result={'lhs':lhs,'rhs':rhs,'primitive_gcd':primitive}
    elif kind == 'independent_full_point_validation':
        prefix=node['route'].removesuffix('_validation'); case=cases_by_prefix[prefix]; params=setups[prefix]
        pair=case['terminal_pair']; E=case['inputs']['E']; bits=format(E,'b')
        assert node['pair']==pair and node['E']==E and node['public_exponent_bits']==bits and bits.count('1')==1
        ladder=wiring[case['ladder_link']]
        saved=[('initial',ladder['initial'])]+[('after_bit_'+str(s['bit_index']),s['after']) for s in ladder['steps']]
        expected_checks=[]
        for label,points in saved:
            for i,point in enumerate(points):
                g=op.common('pair_primitive_'+label+'_'+str(i),point); assert g==1
                expected_checks.append({'label':label,'pair_index':i,'point':point,'gcd':g})
        assert node['primitive_pair_checks']==expected_checks
        a2=op.mul('a2',params['A'],params['B']); a4=op.mul('a4',params['B'],params['B'])
        ix=op.mul('initial_X',params['constants']['two'],params['B']); point=[ix,a4,1]
        assert node['a2']==a2 and node['a4']==a4 and node['initial']==point
        states=[point]
        child(node['initial_check_link'],'jacobian_curve_and_primitive_check',point=point,a2=a2,a4=a4)
        assert len(node['doubling_steps'])==len(bits)-1
        for i,step in enumerate(node['doubling_steps']):
            assert step['doubling_index']==i and step['before']==point and step['status']=='COMPLETE'
            point=child(step['double_link'],'jacobian_double_validation',point=point,a2=a2,a4=a4)
            assert step['after']==point; states.append(point)
            child(step['check_link'],'jacobian_curve_and_primitive_check',point=point,a2=a2,a4=a4)
        assert node['full_point_states']==states
        z2=op.mul('terminal_Z_square',point[2],point[2]); bz2=op.mul('terminal_B_Z_square',params['B'],z2)
        left=op.mul('cross_left',pair[0][0],bz2); right=op.mul('cross_right',pair[0][1],point[0]); assert left==right
        gp=op.gcd('primitive_return_gcd',point[2]); assert gp==case['readouts']['marked']['value']
        gs=op.mul('return_gcd_square',gp,gp); gg=op.gcd('squared_return_gcd',gs)
        assert gg==case['readouts']['ordinary']['value']
        result={'full_point':point,'full_point_return_gcd':gp,'cross_left':left,'cross_right':right,
                'Kummer_square_gcd':gg,'marked_gcd_equal':True,'public_doublings':len(bits)-1,
                'scope':'terminal E point; adjacent R1 certified by production ladder induction'}
    else:
        raise AssertionError(kind)
    if op: op.close()
    assert node['output']==result and r.pos==node['direct_stop'],(index,kind,r.pos)
    return result


def main():
    global data,catalog,counts,payload,routes,cursors,wiring,position,setups,cases_by_prefix
    destination=ROOT/'ELLIPTIC_RECORD_REVIEW.json'; assert not destination.exists(),'refuse overwrite'
    packed=(ROOT/'ELLIPTIC_MARK_RESULTS.json.gz').read_bytes(); raw=gzip.decompress(packed)
    assert (sha(raw),sha(packed),len(raw),len(packed))==(PINS['raw'],PINS['gzip'],2295574,119267)
    payload=json.loads(raw); summary=json.loads((ROOT/'ELLIPTIC_MARK_SUMMARY.json').read_bytes()); binding=payload['binding']
    assert payload['schema']==summary['schema']=='BRC_ELLIPTIC_TRANSLATED_MARK_V1'
    assert payload['status']==summary['status']=='PASS_FINITE_ELLIPTIC_MARK_NOT_ADMITTED'
    assert sha((ROOT/'elliptic_mark.py').read_bytes())==binding['source_sha256']==summary['source_sha256']==PINS['source']
    assert sha((ROOT/'PLAN.md').read_bytes())==binding['plan_sha256']==summary['plan_sha256']==PINS['plan']
    assert (summary['raw_sha256'],summary['gzip_sha256'],summary['raw_bytes'],summary['gzip_bytes'])==(sha(raw),sha(packed),len(raw),len(packed))
    assert json.loads((ROOT/'STARTED.json').read_bytes())=={k:v for k,v in binding.items() if k!='reused_interfaces'}
    assert not (ROOT/'FAILED_EXECUTION.json.gz').exists() and not (ROOT/'FAILED_SERIALIZATION.txt').exists()
    guardraw=Path(binding['guard_path']).read_bytes(); guard=json.loads(guardraw)
    assert sha(guardraw)==binding['guard_sha256'] and guard==binding['guard']
    assert guard['record_sha256']==binding['expected_guard_record_sha256']
    assert guard['record_sha256'].startswith('b5abe25e')
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    for root,key in ((PROOFS,'proof_dependencies'),(ROOT,'local_dependencies'),(OLD,'old_dependencies')):
        for name,pin in binding[key].items(): assert sha((root/name).read_bytes())==pin
    data={'binding':binding['reused_interfaces']}; catalog=data['binding']['native_arithmetic']['native_adder']['columns']; counts=Counter()
    selected(OLD/'read_native_port_review.py',PINS['native_reader'],{'trace','stream','inverse','gcd','audit_route','Records'})
    selected(OLD/'hbw_marked_section/read_hbw_marked_records.py',PINS['hbw_reader'],{'child','visit'},{'visit':'base_visit'})
    selected(PROOFS/'native_probe/read_free_trace_records.py',PINS['free_reader'],{'classify','saved_factor_check'})
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
    routes=payload['routes']; audits={name:audit_route(route) for name,route in routes.items()}
    cursors={name:Records(route) for name,route in routes.items()}
    total=sum((Counter(row['total']) for row in audits.values()),Counter())
    for name,audit in audits.items():
        cost=payload['costs'][name]
        assert {k:audit['total'][k] for k in METRICS}=={k:cost[k] for k in METRICS}
        assert cost['direct_typed_operations']==len(routes[name]['arithmetic_operations']) and cost['route_invocations']==routes[name]['calls']
        assert not routes[name]['tables'] and not routes[name]['inverses']
    assert {k:total[k] for k in METRICS}==summary['total_cost']
    wiring=payload['wiring']; position=0; setups={}; cases_by_prefix={'case'+str(i):c for i,c in enumerate(payload['cases'])}
    grid=((9,0,4),(35,4,8),(19,0,4)); reports=[]
    assert binding['inputs']==[{'N':N,'A':A,'E':E} for N,A,E in grid]
    categories=('setup','ladder','ordinary','mark_expression','marked','single_W','validation')
    for i,(case,small,(N,A,E)) in enumerate(zip(payload['cases'],summary['cases'],grid,strict=True)):
        prefix='case'+str(i); names={c:prefix+'_'+c for c in categories}
        assert case['inputs']==small['inputs']=={'N':N,'A':A,'E':E} and case['route_names']==names
        parameters=child(case['setup_link'],'montgomery_setup',N=N,A=A); assert parameters==case['setup']==small['setup']
        pair=child(case['ladder_link'],'montgomery_ladder',E=E); assert pair==case['terminal_pair']==small['terminal_pair']
        ordinary=child(case['ordinary_link'],'scalar_factor_readout',value=pair[0][1],label='Kummer_Z0')
        W=child(case['mark_expression_link'],'translated_mark_expression',pair=pair,a=parameters['P_affine'][0]); assert W==case['W']==small['W']
        marked=child(case['marked_link'],'marked_common_readout',values=[pair[0][1],W])
        single=child(case['single_W_link'],'scalar_factor_readout',value=W,label='single_W')
        assert {'ordinary':ordinary,'marked':marked,'single_W':single}==case['readouts']==small['readouts']
        validation=child(case['validation_link'],'independent_full_point_validation',E=E,pair=pair)
        assert validation==case['validation']==small['validation']
        assert case['status']==small['status']=='COMPLETE_FINITE_OBSERVER_COMPARISON_NOT_SUCCESS_RATE'
        assert small['costs']=={category:payload['costs'][name] for category,name in names.items()}
        reports.append({'inputs':case['inputs'],'terminal_pair':pair,'W':W,'readouts':case['readouts'],'validation':validation,
            'category_digits':{c:audits[names[c]]['total']['adder_digit_replays'] for c in categories},
            'production_digits_including_all_three_probes':sum(audits[names[c]]['total']['adder_digit_replays'] for c in categories if c!='validation')})
    assert position==len(wiring)
    for cursor in cursors.values(): cursor.close()
    assert total['adder_digit_replays']==counts['checked_native_digit_cells'] and total['typed_operations']==counts['checked_top_level_operations']
    assert set(routes)=={name for c in payload['cases'] for name in c['route_names'].values()}
    report={'status':'PASS_STDLIB_ELLIPTIC_SAVED_RECORD_REVIEW_NOT_ADMISSION','reader_sha256':sha(Path(__file__).read_bytes()),
        'source_pins':PINS,'binding':binding,'raw_sha256':sha(raw),'gzip_sha256':sha(packed),'raw_bytes':len(raw),'gzip_bytes':len(packed),
        'summary_sha256':sha((ROOT/'ELLIPTIC_MARK_SUMMARY.json').read_bytes()),'counts':dict(counts),'wiring_nodes':len(wiring),
        'route_audits':audits,'total_cost':dict(total),'native_records':payload['all_native_records'],'cases':reports,
        'scope':['Full saved native digit cells, typed operations and outer ladder/readout/Jacobian validation links consumed.',
                 'All joint-gcd Euclidean divisions and proper-factor division links checked.',
                 'No scientific imports, rerun, host modular answer computation, gcd, pow or curve arithmetic.',
                 'Only administrative counts, equality comparisons and recorded-output routing; not independent admission.']}
    with destination.open('x',encoding='utf-8') as f: f.write(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:report[k] for k in ('status','counts','wiring_nodes','total_cost','cases')},indent=2))


if __name__=='__main__': main()
