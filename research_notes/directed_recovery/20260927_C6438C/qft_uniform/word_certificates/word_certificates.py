"""Immutable full-native-word scalar certificates, with paid fresh replay.

No prefix covariance, ideal target angle, or work-label dynamics is used.
Identical signed expressions share actual PositivePathObserver receipts;
every full-carrier entry retains its expression address, including zero.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
OLD = BASE/'sep26-shor-general'
for directory in (OLD/'new_word_compiler', OLD/'optimization/streaming',
                  OLD/'optimization/carrier_codec'):
    sys.path.insert(0,str(directory))
from compiled_streaming import CompleteNativeWord, replay_complete_word
from certified_word_compiler import PositivePathObserver, packed, source_binding
from carrier_codec import ExactCarrierCodec, RestrictedNativeWord, restrict_word, restrict_bank
from lazy_streaming import LazyStreamingProgram
from stage45.brc_loop_recheck import CALLS


def strict_bytes(value):
    return json.dumps(value,sort_keys=True,separators=(',', ':'),
                      ensure_ascii=False,allow_nan=False).encode('utf-8')


def digest(value):
    return hashlib.sha256(strict_bytes(value)).hexdigest()


def sources():
    paths = {'word_certificates':Path(__file__),
             'compiled_streaming':OLD/'new_word_compiler/compiled_streaming.py',
             'carrier_codec':OLD/'optimization/carrier_codec/carrier_codec.py',
             'lazy_streaming':OLD/'optimization/streaming/lazy_streaming.py'}
    return {'native':source_binding(),'files_sha256':{
        key:hashlib.sha256(path.read_bytes()).hexdigest() for key,path in paths.items()}}


def _program_view(program):
    if not isinstance(program,LazyStreamingProgram) or program.full_dim != 61:
        raise ValueError('admitted complete 61-carrier lazy program required')
    if type(program.bank) is not dict or any(type(m) is not int for m in program.bank):
        raise ValueError('canonical integer phase keys required')
    if set(program.bank) != set(range(2,program.t+1)):
        raise ValueError('complete bank required')
    codec = program.codec
    if codec is None:
        if program.dim != 61 or program.codec_binding is not None:
            raise ValueError('invalid complete carrier binding')
        codec_view = None
    else:
        if type(codec) is not ExactCarrierCodec or codec.full_dim != 61 or program.dim != codec.dim:
            raise ValueError('actual exact carrier codec required')
        codec_view = (codec.full_dim,codec.indices)
    rows = []
    for m,gate in sorted(program.bank.items()):
        expected_type = CompleteNativeWord if codec is None else RestrictedNativeWord
        if type(gate) is not expected_type or gate.dim != program.dim:
            raise ValueError('wrong complete/restricted native object type')
        rows.append((m,gate.dim,gate.den,gate.inverse_phase_word,
            gate.columns,gate.inverse_columns,gate.h4_count,gate.sign_count,gate.swap_count,
            getattr(gate,'columns_sha256',None),
            getattr(gate,'source_columns_sha256',None),
            getattr(gate,'_forward_nonzero',None),getattr(gate,'_inverse_nonzero',None)))
    return (program.full_dim,program.dim,codec_view,tuple(rows),
            strict_bytes(program.phase_bindings),strict_bytes(program.codec_binding))


class SignedExpressions:
    def __init__(self):
        self.observer = PositivePathObserver()
        self.cache = {}
        self.references = 0
        self.zero_expression_references = 0

    def evaluate(self,label,terms):
        # A zero factor contributes no path. Empty sums are still bound to one
        # actual observed zero expression, reused with a full entry index map.
        terms = tuple(tuple(F(v) for v in term) for term in terms)
        terms = tuple(term for term in terms if all(v != 0 for v in term)) or ((F(0),),)
        self.references += 1
        if terms == ((F(0),),):
            self.zero_expression_references += 1
        if terms not in self.cache:
            index = len(self.observer.operations)
            value = self.observer.evaluate(f'{index}:{label}',terms)
            self.cache[terms] = (value,index)
        return self.cache[terms]


@dataclass(frozen=True)
class WordCertificate:
    phase_index: int
    s: F
    accepted: bool
    certificate_sha256: str


class CertificateReplayError(ValueError):
    def __init__(self,message,evidence):
        super().__init__(message)
        self.evidence = evidence


def _certify_word(m,full,codec):
    expr = SignedExpressions()
    dim = 61
    G = tuple(tuple(F(full.columns[j][i],full.den) for j in range(dim)) for i in range(dim))
    matrices,indices = {},{}
    def matrix(name,terms):
        observed = tuple(tuple(expr.evaluate(f'{name}[{i},{j}]',terms(i,j))
                               for j in range(dim)) for i in range(dim))
        value = tuple(tuple(x[0] for x in row) for row in observed)
        matrices[name] = [[str(v) for v in row] for row in value]
        indices[name] = [[x[1] for x in row] for row in observed]
        return value
    gram = matrix('orthogonality_residual',lambda i,j:
        tuple((G[k][i],G[k][j]) for k in range(dim)) + ((-F(int(i==j)),),))
    if any(v for row in gram for v in row):
        raise ValueError('full-carrier signed orthogonality observation failed')
    D = matrix('I_minus_G',lambda i,j:((F(int(i==j)),),(-F(1),G[i][j])))
    B = matrix('B',lambda i,j:tuple((D[k][i],D[k][j]) for k in range(dim)))
    s,s_index = expr.evaluate('half_full_trace_B',tuple((B[i][i],F(1,2)) for i in range(dim)))
    residual = matrix('B_squared_minus_sB',lambda i,j:
        tuple((B[i][k],B[k][j]) for k in range(dim)) + ((-F(1),s,B[i][j]),))
    failed = [[i,j,str(v)] for i,row in enumerate(residual) for j,v in enumerate(row) if v]
    accepted = 0 <= s <= 4 and not failed
    nonzero_B = any(v for row in B for v in row)
    codec_record = None
    if codec is not None:
        restricted = restrict_word(full,codec)
        codec_record = {'binding':restricted.binding_record(),
            'forward_columns':restricted.columns,'inverse_columns':restricted.inverse_columns,
            'full_forward_inverse_cross_blocks_zero_and_complement_identity':True,
            'certificate_was_computed_on_full_dimension':61}
    record = {'schema':'BRC_FULL_WORD_SCALAR_WITNESS_V1','phase_index':m,
        'full_dimension':61,'native_binding':full.binding_record(),
        'complete_forward_columns':full.columns,'complete_inverse_columns':full.inverse_columns,
        'denominator':full.den,'exact_codec':codec_record,
        's':str(s),'witness_rule':'HALF_FULL_TRACE_B_AND_FULL_B_SQUARED_EQUALS_sB',
        'accepted':accepted,'nonzero_B':nonzero_B,
        'norm_squared_equals_s_if_accepted':accepted,
        'failed_entries':failed,'s_in_closed_interval_0_4':0 <= s <= 4,
        'full_matrices':matrices,'entry_expression_indices':indices,
        's_expression_index':s_index,'observer_operations':expr.observer.operations,
        'expression_reference_count':expr.references,
        'zero_expression_reference_count':expr.zero_expression_references,
        'actual_unique_observer_expressions':len(expr.observer.operations),
        'all_full_entries_bound_to_actual_signed_observer':True,
        'not_an_ideal_target_angle_certificate':True}
    encoded = json.loads(packed(record))
    return encoded,WordCertificate(m,s,accepted,digest(encoded))


@dataclass(frozen=True,init=False)
class WordCertificateBank:
    """Immutable certificates; only exact native-bank/codec identity is shared.

    check() compares source-derived immutable columns/words, not N/a/history.
    A fresh constructor always replays complete words outside the inherited
    replay cache. restore() pays the same cold setup, never trusts JSON claims.
    Python monkeypatches or object.__setattr__ attacks are outside this API.
    """
    binding_sha256: str
    _view: tuple
    _records: tuple
    _evidence_bytes: bytes

    def __init__(self,program):
        first,t0 = len(CALLS),perf_counter()
        view = _program_view(program)
        source = sources()
        words,records,setup,full_bank = {},[],[],{}
        for m,gate in sorted(program.bank.items()):
            start,t1 = len(CALLS),perf_counter()
            before = replay_complete_word.cache_info()._asdict()
            replay_complete_word.cache_clear()
            full = CompleteNativeWord(gate.inverse_phase_word,61)
            full_bank[m] = full
            after = replay_complete_word.cache_info()._asdict()
            complete_end = len(CALLS)
            if program.codec is None:
                expected = full
            else:
                expected = restrict_word(full,program.codec)
            if strict_bytes(expected.binding_record()) != strict_bytes(gate.binding_record()):
                raise ValueError('program native word binding differs from fresh replay')
            if (gate.den,gate.columns,gate.inverse_columns) != (expected.den,expected.columns,expected.inverse_columns):
                raise ValueError('program cached columns differ from fresh native replay')
            if any(getattr(gate,key,None) != getattr(expected,key,None)
                   for key in ('_forward_nonzero','_inverse_nonzero')):
                raise ValueError('program sparse application cache differs from fresh native replay')
            if strict_bytes(program.phase_bindings[str(m)]) != strict_bytes(full.binding_record()):
                raise ValueError('program full-word source binding is stale')
            evidence,record = _certify_word(m,full,program.codec)
            words[str(m)] = evidence
            records.append(record)
            setup.append({'phase_index':m,'call_interval':[start,len(CALLS)],
                'complete_native_replay_call_interval':[start,complete_end],
                'native_cache_before':before,'native_cache_after_fresh_replay':after,
                'native_cache_cleared_for_fresh_replay':True,
                'forward_basis_columns':61,'inverse_basis_columns':61,
                'inverse_recovery_basis_columns':61,
                'actual_unique_observer_expressions':evidence['actual_unique_observer_expressions'],
                'elapsed_seconds':perf_counter()-t1})
        if program.codec is not None:
            codec,_,codec_binding = restrict_bank(full_bank,indices=program.codec.indices,full_dim=61)
            if codec != program.codec or strict_bytes(codec_binding) != strict_bytes(program.codec_binding):
                raise ValueError('program codec certificate differs from complete native replay')
        if _program_view(program) != view:
            raise ValueError('program changed while certificates were constructed')
        logical = {'schema':'BRC_IMMUTABLE_WORD_CERTIFICATE_BANK_V1','source':source,
            'full_dimension':61,'encoded_dimension':program.dim,
            'phase_bindings':program.phase_bindings,'codec_binding':program.codec_binding,
            'words':words,'omitted_program_fields':['N','a','work_modular_powers','history'],
            'scope':'complete admitted native words and exact codec only; no state or probability assertion'}
        logical = json.loads(packed(logical))
        binding = digest(logical)
        evidence = {'logical':logical,'binding_sha256':binding,
            'setup':{'call_interval':[first,len(CALLS)],'actual_core_calls':CALLS[first:],
                'core_call_count':len(CALLS)-first,'word_setups':setup,
                'elapsed_seconds':perf_counter()-t0,
                'stored_full_matrix_scalar_entries':len(records)*4*61*61,
                'stored_complete_column_scalar_entries':len(records)*2*61*61,
                'logical_serialized_bytes':len(strict_bytes(logical)),
                'native_program_admission_setup_included':False,
                'repeated_check_runs_scientific_observers':False}}
        object.__setattr__(self,'binding_sha256',binding)
        object.__setattr__(self,'_view',view)
        object.__setattr__(self,'_records',tuple(records))
        object.__setattr__(self,'_evidence_bytes',strict_bytes(evidence))

    def check(self,program):
        if _program_view(program) != self._view:
            raise ValueError('certificate bank does not match exact native words and codec')

    def get(self,m):
        if type(m) is not int:
            raise ValueError('integer phase index required')
        for record in self._records:
            if record.phase_index == m:
                return record
        raise KeyError(m)

    def evidence(self):
        return json.loads(self._evidence_bytes)

    @classmethod
    def restore(cls,program,serialized):
        if isinstance(serialized,(str,bytes)):
            serialized = json.loads(serialized)
        if type(serialized) is not dict or set(serialized) != {'logical','binding_sha256','setup'}:
            raise ValueError('complete canonical bank evidence required')
        if digest(serialized['logical']) != serialized['binding_sha256']:
            raise ValueError('serialized logical hash mismatch')
        fresh = cls(program)
        if (strict_bytes(fresh.evidence()['logical']) != strict_bytes(serialized['logical'])
                or fresh.binding_sha256 != serialized['binding_sha256']):
            raise CertificateReplayError('serialized witness differs from fresh complete replay',fresh.evidence())
        # Dynamic old setup timings/call indices are provenance only. Returned
        # evidence always contains this invocation's real fresh setup receipts.
        return fresh
