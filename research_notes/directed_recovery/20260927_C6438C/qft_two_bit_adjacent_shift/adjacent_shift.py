"""Code-only adjacent-bit shift reduction on frozen actual typed arithmetic.

No scientific execution occurs on import. A separately reviewed checker and
actual startup receipt must precede the first bounded run.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import sys

ROOT=Path(__file__).resolve().parent
DIRECT=ROOT.parent/'sep27-qft-gap-direct/direct_gap'
DIRECT_PIN='3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521'
ADJACENT_PROOF_PIN='96757c3624c69bf3ec1e313504f56bb6099d1a79e47032813084b19340c272ad'
SCHEMA='BRC_ADJACENT_BITS_SHIFTED_SINGLE_BIT_V1'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

if sha(DIRECT/'direct_signed_gap.py')!=DIRECT_PIN:
    raise ValueError('frozen direct observer changed')
sys.path.insert(0,str(DIRECT))
from direct_signed_gap import (DirectSignedGapObserver,typed_two_power,
    semantic_certificate,require,BASELINE_PIN,FLOOR_PIN,PROOF_PIN,DIRECT_PROOF_PIN)


def validate_adjacent_inputs(g,ell,k,R,r,stride):
    require(all(type(v) is int for v in (g,ell,k,R,r,stride)),
        'strict integer inputs required')
    require(g>=2 and 0<=ell and k==ell+1 and k<g,
        'adjacent selected bits 0<=ell,k=ell+1<g required')
    require(R>=1 and 0<=r<R and stride==1,
        'positive supplied R, canonical residue, unit stride required')


class AdjacentShiftObserver(DirectSignedGapObserver):
    def __init__(self):
        super().__init__()
        self._adjacent_source=sha(__file__)
        self.inflight=None
        self.failed=False

    def _check(self):
        require(not self.failed,'interrupted observer is terminal')
        require(sha(__file__)==self._adjacent_source,'adjacent source changed')
        require(sha(ROOT/'ADJACENT_SHIFT_REDUCTION.md')==ADJACENT_PROOF_PIN,
            'adjacent proof changed')
        require(sha(DIRECT/'direct_signed_gap.py')==DIRECT_PIN,'direct source changed')
        super()._check()

    def one_negative(self,*args,**kwargs):
        raise ValueError('use the two_adjacent contract for this observer')

    def _adjacent_progression(self,head,orientation,L,U,P,R,V,
            coefficients,correction_coefficients):
        runner=self.runner
        start=len(runner.signed_operations)
        base=super()._progression(head,orientation,L,U,P,R,coefficients)
        record={'orientation':orientation,'multiplicity':1,
            'single_bit_progression':base,'signed_operations_start':start,
            'empty':base['empty'],'n':base['n']}
        # Attach the completed base before beginning the correction, so any
        # later exception preserves its actual chronology in the snapshot.
        self.inflight['progressions'].append(record)
        if base['empty']:
            record.update(correction=None,value=base['value'],
                signed_operations_stop=len(runner.signed_operations))
            return record
        correction_start=len(runner.signed_operations)
        b,n=head['value'],base['n']
        threeV=correction_coefficients['threeV']['value']
        a_offset=self._computed(lambda:runner.add(b,threeV))
        a,a_record=self._table(n,P,R,a_offset['value'])
        b_offset=self._computed(lambda:runner.add(b,V))
        c,c_record=self._table(n,P,R,b_offset['value'])
        da=self._computed(lambda:runner.add(runner.mul(b,a[0,1]),runner.mul(R,a[1,1])))
        db=self._computed(lambda:runner.add(runner.mul(b,c[0,1]),runner.mul(R,c[1,1])))
        # Reuse the already paid single-bit displacement sum. This is a
        # reference to its exact saved output, not a free new evaluation.
        sum_d=base['weighted_sums']['d']['value']
        terms={
            'linear_d':self._computed(lambda:runner.mul(-2,sum_d)),
            'weighted_floor_difference':self._computed(lambda:runner.mul(4,
                runner.sub(da['value'],db['value']))),
            'floor_sum':self._computed(lambda:runner.mul(
                correction_coefficients['fourV']['value'],runner.add(a[0,1],c[0,1]))),
            'floor_square_difference':self._computed(lambda:runner.mul(
                correction_coefficients['eightV']['value'],runner.sub(c[0,2],a[0,2])))}
        correction=self._computed(lambda:runner.total(x['value'] for x in terms.values()))
        record['correction']={'offsets':[a_offset,b_offset],
            'table_calls':[a_record,c_record],'weighted_floors':[da,db],
            'reused_single_bit_displacement_sum':sum_d,'terms':terms,
            'sum':correction,'signed_operations_start':correction_start,
            'signed_operations_stop':len(runner.signed_operations)}
        combined=self._computed(lambda:runner.add(base['value'],correction['value']))
        record.update(combined=combined,value=combined['value'],
            signed_operations_stop=len(runner.signed_operations))
        return record

    def two_adjacent(self,g,ell,k,R,r,*,stride=1):
        validate_adjacent_inputs(g,ell,k,R,r,stride)
        self._check()
        require(self.inflight is None,'request already in progress')
        runner=self.runner
        start=len(runner.signed_operations)
        self.inflight={'inputs':{'g':g,'ell':ell,'k':k,'R':R,'r':r,'stride':stride},
            'signed_operations_start':start,'progressions':[],'complete':False}
        try:
            V=typed_two_power(runner,ell)
            U=runner.add(V,V)
            P=runner.add(U,U)
            H=typed_two_power(runner,g-k-1)
            L=runner.mul(H,P)
            scales_stop=len(runner.signed_operations)
            self.inflight.update(V=V,U=U,P=P,H=H,L=L,
                scales_operations_start=start,scales_operations_stop=scales_stop)
            coefficients,helpers=self._coefficients(H,P)
            correction_coefficients={
                'threeV':self._computed(lambda:runner.add(U,V)),
                'fourV':self._computed(lambda:runner.mul(4,V)),
                'eightV':self._computed(lambda:runner.mul(8,V))}
            self.inflight.update(coefficients=coefficients,
                coefficient_helpers=helpers,correction_coefficients=correction_coefficients)
            positive_head=self._computed(lambda:runner.add(r,0))
            positive=self._adjacent_progression(positive_head,'nonnegative_difference',
                L,U,P,R,V,coefficients,correction_coefficients)
            negative_head=self._computed(lambda:runner.sub(R,r))
            negative=self._adjacent_progression(negative_head,'negative_difference_magnitude',
                L,U,P,R,V,coefficients,correction_coefficients)
            final=self._computed(lambda:runner.add(positive['value'],negative['value']))
            self.inflight.update(final_addition=final,value=final['value'],
                raw_denominator_exponent=2*g,negative_values_are_valid=True,
                signed_operations_stop=len(runner.signed_operations),complete=True)
            record=deepcopy(self.inflight)
            self.requests.append(record)
            self.inflight=None
            return deepcopy(record)
        except BaseException:
            self.failed=True
            raise

    def export_certificate(self):
        self._check()
        require(self.inflight is None,'unfinished arithmetic is not a complete certificate')
        return deepcopy({'schema':SCHEMA,'source_sha256':self._adjacent_source,
            'direct_source_sha256':DIRECT_PIN,'baseline_helper_source_sha256':BASELINE_PIN,
            'floor_moment_source_sha256':FLOOR_PIN,'signed_gap_proof_sha256':PROOF_PIN,
            'direct_proof_sha256':DIRECT_PROOF_PIN,'adjacent_proof_sha256':ADJACENT_PROOF_PIN,
            'requests':self.requests,'actual_integer_evidence':self.runner.evidence(),
            'scope':'Supplied-R adjacent selected-bit scalar correlation, including non-top k',
            'host_wiring':'public indices; observed signs and routing; hashes and resource metadata',
            'admission':'AUTHOR_SHARED_CONTEXT_NOT_ADMITTED'})

    def incomplete_snapshot(self):
        snapshot=super().incomplete_snapshot()
        snapshot.update(schema='INCOMPLETE_'+SCHEMA,source_sha256=self._adjacent_source,
            direct_source_sha256=DIRECT_PIN,adjacent_proof_sha256=ADJACENT_PROOF_PIN,
            inflight=deepcopy(self.inflight),failed=self.failed)
        return snapshot


def verify_adjacent_certificate(certificate,*,replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list,'list replay capture required')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema')==SCHEMA,'wrong adjacent schema')
    pins={'source_sha256':sha(__file__),'direct_source_sha256':DIRECT_PIN,
        'baseline_helper_source_sha256':BASELINE_PIN,'floor_moment_source_sha256':FLOOR_PIN,
        'signed_gap_proof_sha256':PROOF_PIN,'direct_proof_sha256':DIRECT_PROOF_PIN,
        'adjacent_proof_sha256':ADJACENT_PROOF_PIN}
    require(all(certificate.get(k)==v for k,v in pins.items()),'adjacent dependency pin mismatch')
    requests=certificate.get('requests')
    require(type(requests) is list,'request list required')
    observer=AdjacentShiftObserver()
    try:
        for request in requests:
            require(type(request) is dict and type(request.get('inputs')) is dict,'malformed request')
            inputs=request['inputs']
            require(set(inputs)=={'g','ell','k','R','r','stride'},'wrong adjacent input fields')
            observer.two_adjacent(inputs['g'],inputs['ell'],inputs['k'],inputs['R'],inputs['r'],
                stride=inputs['stride'])
        replay=observer.export_certificate()
    except BaseException:
        if replay_capture is not None and observer.runner.arithmetic.operations:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate)==semantic_certificate(replay),'adjacent replay mismatch')
    return {'verified':True,'requests_replayed':len(requests),
        'replay_arithmetic_stats':deepcopy(observer.runner.arithmetic.stats),
        'replay_certificate':replay,
        'excluded_runtime_field':'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}
