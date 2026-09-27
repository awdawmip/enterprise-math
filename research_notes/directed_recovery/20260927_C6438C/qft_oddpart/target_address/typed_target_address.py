"""Paid cyclic-subgroup address recovery from a replayed small-odd-part order."""
from pathlib import Path
from copy import deepcopy
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent/'period_discovery'))
from typed_odd_part import verify_odd_part_certificate, canonical_scientific_bytes
from lazy_modular import Arithmetic, LazyModularFactory, verify_lazy_permutation, source_binding
from stage45.brc_loop_recheck import CALLS


def require(test, message):
    if not test:
        raise ValueError(message)


def source_hashes():
    import typed_odd_part, lazy_modular
    return {name: hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
        for name,module in (('typed_target_address.py',sys.modules[__name__]),
                            ('typed_odd_part.py',typed_odd_part),('lazy_modular.py',lazy_modular))}


class TargetAddressError(ValueError):
    def __init__(self, message, evidence):
        super().__init__(message)
        self.evidence = evidence


def recover_target_address(order_certificate, z):
    """MEMBER with canonical r, or a paid NONMEMBER certificate.

    Every call freshly verifies the order. PARTIAL is never consumed as an
    order. A canonical nonunit z returns NONMEMBER with a typed gcd trace.
    Invalid schemas and interrupted invariant failures raise with evidence.
    """
    first = len(CALLS)
    arithmetic, factory = Arithmetic(), LazyModularFactory()
    verified, verifications = set(), []
    record = {'schema':'BRC_PAID_TARGET_ADDRESS_V1','status':'RUNNING','r':None,
        'R':None,'q':None,'s':None,'inputs':{'N':None,'b':None,'z':z},
        'order_certificate':deepcopy(order_certificate),'order_replay':None,
        'evidence':{'source_sha256':source_hashes(),'unit_check':None,
            'power_chains':[],'odd_projection_search':[],'bit_lifts':[],
            'host_wiring':'integer loop indices, exponent bits, routing and equality only; CRT residues are typed',
            'scope':'paid group membership/address recovery; no ideal phase or amplitude propagation'}}
    evidence = record['evidence']
    stats = {'modular_column_actions':0,'power_chains':0,'odd_projection_tests':0,
             'binary_lift_bits':0}

    def finish(status, reason=None, r=None):
        record['status'],record['r'] = status,r
        if reason is not None: evidence['reason'] = reason
        tables = factory.export_certificate()
        evidence['table_instances'] = tables
        evidence['permutation_verifications'] = deepcopy(verifications)
        evidence['arithmetic_operations'] = deepcopy(arithmetic.operations)
        evidence['arithmetic_stats'] = dict(arithmetic.stats)
        evidence['native_source'] = source_binding() if tables else None
        metrics = dict(stats)
        metrics.update(table_instance_count=len(tables),
            setup_adder_digit_replays=sum(x['stats']['setup_adder_digit_replays'] for x in tables),
            column_adder_digit_replays=sum(x['stats']['column_adder_digit_replays'] for x in tables),
            verification_adder_digit_replays=sum(x['replayed_adder_digits'] for x in verifications),
            auxiliary_adder_digit_replays=arithmetic.stats['adder_digit_replays'],
            column_requests=sum(x['stats']['column_requests'] for x in tables),
            computed_columns=sum(x['stats']['computed_columns'] for x in tables),
            cache_hits=sum(x['stats']['cache_hits'] for x in tables),
            actual_native_core_calls_delta=len(CALLS)-first)
        metrics['address_only_adder_digit_replays'] = sum(metrics[k] for k in (
            'setup_adder_digit_replays','column_adder_digit_replays',
            'verification_adder_digit_replays','auxiliary_adder_digit_replays'))
        order = record['order_replay']
        metrics['order_replay_adder_digit_replays'] = order['metrics']['total_adder_digit_replays'] if order else 0
        metrics['total_adder_digit_replays'] = metrics['address_only_adder_digit_replays']+metrics['order_replay_adder_digit_replays']
        record['metrics'] = metrics
        return deepcopy(record)

    def table(modulus,multiplier):
        result = factory(modulus,multiplier)
        key = modulus,multiplier
        if key not in verified:
            verifications.append(verify_lazy_permutation(result))
            verified.add(key)
        return result

    def column(modulus,multiplier,source):
        action = table(modulus,multiplier)
        value = action[source]
        stats['modular_column_actions'] += 1
        return value,{'N':modulus,'multiplier':multiplier,'source':source,'target':value,
            'permutation_certificate_sha256':action.certificate_sha256}

    def power(base,exponent,purpose):
        require(type(exponent) is int and exponent>=0,'nonnegative exponent required')
        table(N,base)
        rest,value,factor,steps,bit = exponent,1,base,[],0
        while rest:
            selected = rest&1
            multiply_edge = None
            if selected: value,multiply_edge = column(N,factor,value)
            rest >>= 1
            square_edge = None
            if rest: factor,square_edge = column(N,factor,factor)
            steps.append({'bit':bit,'selected':selected,'value':value,
                          'multiply_edge':multiply_edge,'square_edge':square_edge})
            bit += 1
        evidence['power_chains'].append({'purpose':purpose,'base':base,'exponent':exponent,
                                        'value':value,'steps':steps})
        stats['power_chains'] += 1
        return value

    try:
        replay = verify_odd_part_certificate(order_certificate)['replay']
        record['order_replay'] = replay
        require(replay['status']=='CERTIFIED','PARTIAL discovery does not certify an order')
        N,b = replay['inputs']['N'],replay['inputs']['b']
        q,s,R = replay['q'],replay['s'],replay['R']
        record.update(q=q,s=s,R=R)
        record['inputs'].update(N=N,b=b)
        require(type(z) is int and 1<=z<N,'canonical integer target 1<=z<N required')
        left,right,divisions = N,z,[]
        while right:
            quotient,remainder,operation = arithmetic.divide(left,right)
            divisions.append({'left':left,'right':right,'quotient':quotient,
                              'remainder':remainder,'division_operation':operation})
            left,right = right,remainder
        evidence['unit_check'] = {'gcd':left,'divisions':divisions}
        if left!=1: return finish('NONMEMBER','target is not a unit')
        two_power = 1<<s
        gq = power(b,two_power,'odd_projection_generator')
        yq = power(z,two_power,'odd_projection_target')
        value,rq = 1,None
        for exponent in range(q):
            evidence['odd_projection_search'].append({'exponent':exponent,'value':value})
            stats['odd_projection_tests'] += 1
            if value==yq:
                rq = exponent
                break
            if exponent+1<q:
                value,edge = column(N,gq,value)
                evidence['odd_projection_search'][-1]['next_edge'] = edge
        evidence['odd_projection'] = {'gq':gq,'yq':yq,'rq':rq}
        if rq is None: return finish('NONMEMBER','odd projection is outside the certified q-cycle')
        g2 = power(b,q,'two_projection_generator')
        y2 = power(z,q,'two_projection_target')
        inverse_g2 = table(N,g2).inverse_multiplier
        eta = power(g2,1<<(s-1),'order_two_element') if s else None
        evidence['two_projection'] = {'g2':g2,'y2':y2,'inverse_g2':inverse_g2,'eta':eta}
        if not s and y2!=1: return finish('NONMEMBER','trivial two-part projection does not equal one')
        e = 0
        for j in range(s):
            inverse_prefix = power(inverse_g2,e,'inverse_lift_prefix_'+str(j))
            corrected,correct_edge = column(N,inverse_prefix,y2)
            residual = power(corrected,1<<(s-1-j),'lift_test_'+str(j))
            if residual==1: bit = 0
            elif residual==eta: bit = 1
            else: bit = None
            row = {'j':j,'prefix_e':e,'inverse_prefix':inverse_prefix,
                   'corrected':corrected,'correct_edge':correct_edge,
                   'test_value':residual,'bit':bit}
            evidence['bit_lifts'].append(row)
            stats['binary_lift_bits'] += 1
            if bit is None: return finish('NONMEMBER','two-part bit lift failed at j='+str(j))
            e,add_id = arithmetic.add(e,(1<<j) if bit else 0)
            row.update(next_e=e,prefix_add_operation=add_id)
        evidence['two_projection']['r2'] = e
        if q==1:
            k = 0
            r,add_id = arithmetic.add(e,0)
            crt = {'modulus_one_shortcut':True,'k':k,'r':r,'add_operation':add_id}
        else:
            _,e_mod,ereduce = arithmetic.divide(e,q)
            delta,delta_ops = arithmetic.modsubtract(rq,e_mod,q)
            _,two_mod,treduce = arithmetic.divide(two_power,q)
            inverse_two = table(q,two_mod).inverse_multiplier
            k,kedge = column(q,inverse_two,delta)
            scaled,mul_id = arithmetic.multiply(two_power,k)
            r,add_id = arithmetic.add(e,scaled)
            crt = {'modulus_one_shortcut':False,'e_mod_q':e_mod,'e_division_operation':ereduce,
                'delta':delta,'delta_operations':delta_ops,'two_mod_q':two_mod,
                'two_division_operation':treduce,'inverse_two':inverse_two,'k':k,
                'k_edge':kedge,'scale_operation':mul_id,'add_operation':add_id,'r':r}
        relation,_,compare_id = arithmetic.compare(r,R)
        require(relation<0,'CRT address must lie below the certified order')
        crt['range_comparison_operation'] = compare_id
        evidence['crt'] = crt
        final = power(b,r,'final_membership_check')
        evidence['final_check'] = {'b_to_r':final,'target':z,'equal':final==z}
        if final!=z: return finish('NONMEMBER','final actual b^r does not equal target')
        return finish('MEMBER',r=r)
    except ValueError as error:
        evidence['error'] = str(error)
        if getattr(error,'evidence',None) is not None:
            evidence['nested_failure_evidence'] = error.evidence
            # A rejected order may already have paid for a complete replay.
            # Preserve and count it even though the verifier did not return.
            nested = error.evidence
            candidate = nested.get('replay',nested) if isinstance(nested,dict) else None
            if (record['order_replay'] is None and isinstance(candidate,dict)
                    and candidate.get('schema')=='BRC_SMALL_ODD_PART_ORDER_V1'
                    and 'metrics' in candidate):
                record['order_replay'] = candidate
        failed = finish('REJECTED')
        raise TargetAddressError(str(error),failed) from error


def verify_target_address(record):
    require(type(record) is dict and record.get('schema')=='BRC_PAID_TARGET_ADDRESS_V1',
            'target-address certificate schema required')
    require(record.get('status') in ('MEMBER','NONMEMBER'),'completed target-address attempt required')
    canonical_scientific_bytes(record)
    replay = recover_target_address(record['order_certificate'],record['inputs']['z'])
    if canonical_scientific_bytes(record)!=canonical_scientific_bytes(replay):
        raise TargetAddressError('complete target-address certificate does not replay',
            {'attempted_certificate':deepcopy(record),'replay':replay})
    return {'verified':True,'replay':replay,
            'scope':'fresh order and target-address replay; process-native-cache deltas excluded'}
