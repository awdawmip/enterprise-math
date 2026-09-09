"""Finite local-type audit and one exact auxiliary counterexample.

Reuse the existing BRC exact-DIV, T6 partition-refinement predicate, and the
archived task-local integer polynomial ring. No blind checker, old assignment
enumeration, global map search, RR system or period computation is executed.
"""
from pathlib import Path
from dataclasses import asdict
from itertools import product
from collections import Counter
import hashlib, importlib.util, json, sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.exact_arithmetic import division, brc_integer_value, brc_is_integral
from enterprise_math.operation_quotient import refines

POLY_PATH=ROOT/'research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/check_squareclass_rr.py'
spec=importlib.util.spec_from_file_location('rb_existing_integer_polynomial_ring',POLY_PATH)
p=importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

cache={}
def exact_div(n,d):
    key=(n,d)
    if key not in cache:
        value,trace=brc_integer_value(division(n,d))
        assert trace.reconstruct()==n
        cache[key]=(value,asdict(trace))
    return cache[key][0]

def main():
    local=[]
    for name,epi,ef,ex in [('B_SPECIAL',2,1,2),('Q_ORDINARY',1,2,1),('Q_SPECIAL',1,2,2),('OTHER_SPECIAL',1,1,2),('OTHER_ORDINARY',1,1,1)]:
        value=exact_div(ef*ex,epi)
        local.append({'type':name,'e_pi':epi,'e_f':ef,'e_target_x':ex,'e_X':value})
    integral,bad_trace=brc_is_integral(division(1,2))
    assert integral is False
    try:
        brc_integer_value(division(1,2))
    except ValueError:
        strict_rejected=True
    else:
        raise AssertionError('Impossible B_ORDINARY degree ratio was not rejected')

    patterns={'6+0+0+0':(6,0,0,0),'4+2+0+0':(4,2,0,0),'2+2+2+0':(2,2,2,0)}
    states=[]; histograms={}; rejected={}
    for name,m in patterns.items():
        histogram=Counter(); bad=0
        for targets in product((-1,0,1,2,3),repeat=3):
            q_at=tuple(targets.count(v) for v in range(4))
            remainder=tuple(6-m[v]-4*q_at[v] for v in range(4))
            if any(x<0 for x in remainder):
                bad+=1; continue
            doubles=tuple(exact_div(x,2) for x in remainder)
            special_q=sum(q_at)
            ram_special=sum(3*q_at[v]+doubles[v] for v in range(4))
            ram_ordinary=3-special_q
            assert ram_special==9+special_q
            assert ram_special+ram_ordinary==12
            assert sum(doubles)==9-2*special_q
            assert all(m[v]+4*q_at[v]+2*doubles[v]==6 for v in range(4))
            histogram[special_q]+=1
            states.append({'pattern':name,'B_occupancies':m,'q_target_labels':targets,
                'q_special_per_fiber':q_at,'ordinary_double_points_per_special_fiber':doubles,
                'q_local_degrees':tuple(2 if v==-1 else 4 for v in targets),
                'q_local_parameter_valuations':tuple({'coordinate':'X-X(Q)','order':2} if v==-1 else
                    {'coordinate':'X' if v==3 else 'X-target_special_value','order':-4 if v==3 else 4} for v in targets),
                'special_ramification':ram_special,'ordinary_q_ramification':ram_ordinary,
                'total_ramification':12,'global_map_constructed':False})
        histograms[name]={str(s):histogram[s] for s in range(4)}
        rejected[name]=bad
    assert histograms['6+0+0+0']=={'0':1,'1':9,'2':18,'3':6}
    assert histograms['4+2+0+0']=={'0':1,'1':9,'2':18,'3':6}
    assert histograms['2+2+2+0']=={'0':1,'1':12,'2':36,'3':24}
    assert len(states)==141

    domain=tuple(range(len(states)))
    coarse={i:(6,6,states[i]['total_ramification']) for i in domain}
    fine={i:(states[i]['B_occupancies'],states[i]['q_target_labels'],states[i]['q_local_degrees'],
        states[i]['ordinary_double_points_per_special_fiber']) for i in domain}
    assert refines(domain,fine,coarse) is True
    assert refines(domain,coarse,fine) is False
    witness0=next(i for i,s in enumerate(states) if s['pattern']=='4+2+0+0' and s['q_target_labels']==(-1,-1,-1))
    witness1=next(i for i,s in enumerate(states) if s['pattern']=='4+2+0+0' and s['q_target_labels']==(1,-1,-1))
    assert coarse[witness0]==coarse[witness1] and fine[witness0]!=fine[witness1]

    R=p.variable(p.NAMES.index('R')); t=p.variable(p.NAMES.index('t'))
    R2=p.multiply(R,R); R3=p.multiply(R2,R)
    U=p.add(R3,p.scale(p.multiply(R,t),2),R2,p.constant(-3))
    numerator=p.add(R2,t)
    residual=p.add(p.multiply(numerator,numerator),p.scale(p.multiply(R,U),-1))
    assert residual=={}
    changed=p.add(U,p.constant(1))
    tampered_residual=p.add(p.multiply(numerator,numerator),p.scale(p.multiply(R,changed),-1))
    assert tampered_residual==p.scale(R,-1)
    assert any(row['powers']['t']==1 and row['coefficient']!=0 for row in p.polynomial_rows(U))

    source_paths=['src/enterprise_math/exact_arithmetic.py','src/enterprise_math/operation_quotient.py',
        'research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/check_squareclass_rr.py']
    result={'schema':'RB_LOCAL_BRANCH_AND_EVEN_DIVISOR_AUDIT_V1',
        'classification':'FINITE_LOCAL_TYPES_AND_EXACT_AUXILIARY_IDENTITY_ONLY',
        'source_scope':'Current source-exposed Driver audit; not a clean blind reconstruction and not a global map construction.',
        'interfaces_reused':{'T0_BRC':'REUSE_EXECUTED: exact integer degree ratios and residual pair counts',
            'T6_OPERATION_SAFE_QUOTIENT':'REUSE_EXECUTED: refines checks that total-only observations do not determine the needed local type',
            'ARCHIVED_TASK_LOCAL_INTEGER_RING':'REUSE_EXECUTED: polynomial identity and exact tamper residual'},
        'source_modules':{path:{'git_blob_sha1':git_blob(ROOT.joinpath(path).read_bytes()),
            'sha256':hashlib.sha256(ROOT.joinpath(path).read_bytes()).hexdigest()} for path in source_paths},
        'local_degree_law':'e_X*e_pi=e_target_x*e_f; Q has e_f=2 and B has e_f=1',
        'local_types':local,'rejected_B_ordinary':{'integral':integral,'trace':asdict(bad_trace),'strict_integer_readout_rejected':strict_rejected},
        'brc_exact_input_cache':[{'numerator':n,'denominator':d,'value':v,'trace':trace} for (n,d),(v,trace) in sorted(cache.items())],
        'native_division_calls':len(cache)+2,
        'population':{'three_named_q_points':True,'target_labels':{'-1':'ordinary','0':'0','1':'1','2':'lambda','3':'infinity'},
            'raw_placements_per_occupancy':125,'valid_local_placements':len(states),'histograms_by_number_special_q':histograms,
            'rejected_degree_overflow':rejected,'six_block_globally_excluded_here':False,
            'old_180_360_assignment_search_reexecuted':False,'counts_are_global_maps_or_irreducible_components':False},
        'observer_check':{'fine_refines_total':True,'total_refines_fine':False,
            'same_total_different_local_type':[states[witness0],states[witness1]],
            'boundary':'Only the declared finite observation relation was tested; no undeclared future operation or infinite/global equivalence is certified.'},
        'states':states,
        'even_divisor_witness':{'curve':'t^2=R^3-3R','U':'R^3+2*R*t+R^2-3','identity':'R*U=(R^2+t)^2',
            'identity_residual':p.polynomial_rows(residual),'tamper_U_plus_1_residual':p.polynomial_rows(tampered_residual),
            'polynomial':p.polynomial_rows(U),'t_coefficient':'2*R',
            'paper_arguments_separate':['U=R*(R+t/R)^2 as a function-field identity.',
                'div(R)=2[T0]-2[O], and T0 is nonzero two-torsion, so [R] is geometrically nontrivial.',
                'U is regular at finite points and has pole order exactly 6 at O.',
                'Thus U has even divisor, lies in L(6O), and has nontrivial square class [R], but it has a nonzero t term.',
                'The half-section R+t/R lies in L(2O+T0), not L(2O); the zero of R cancels its pole at T0.'],
            'status':'Auxiliary classification counterexample with exact polynomial check; geometric/divisor proof is a separately stated paper argument pending independent review.',
            'global_six_block_map_constructed':False,'frozen_lambda_six_block_existence_or_nonexistence_decided':False}}
    target=Path(__file__).with_name('local_branch_and_even_divisor_certificate.json')
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'status':'PASS','certificate':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
        'valid_local_placements':len(states),'histograms':histograms,'native_division_calls':len(cache)+2,
        'total_observer_insufficient':True,'U_identity_checked':True,'U_tamper_detected':True,'global_map_constructed':False},indent=2))

if __name__=='__main__':
    main()
