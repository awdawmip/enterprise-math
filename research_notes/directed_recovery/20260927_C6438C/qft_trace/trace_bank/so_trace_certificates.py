"""Immutable complete-native trace bounds; no policy or propagation change.

All scientific trace scalars are actual signed PositivePathObserver outputs.
Determinant parity is a structural theorem about the bound native alphabet.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]
OLD=BASE/'sep26-shor-general'
LEGACY=BASE/'sep27-qft-uniform/word_certificates'
PINS={
    LEGACY/'word_certificates.py':'c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3',
    OLD/'new_word_compiler/compiled_streaming.py':'d0f980b7ff5fb41438e9e0ad40af65a190bcd6f83660c821f8362643190a558c',
    OLD/'new_word_compiler/certified_word_compiler.py':'e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d',
    OLD/'optimization/carrier_codec/carrier_codec.py':'c25149e0ab4ce92a59d2ca40cb697fe6505cd1dc8d406e9c5a2d92cb2b28c953',
    OLD/'optimization/streaming/lazy_streaming.py':'635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257',
}
for path,expected in PINS.items():
    if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        raise ValueError('frozen native dependency changed: '+str(path))
sys.path.insert(0,str(LEGACY))
from word_certificates import (_program_view,SignedExpressions,CompleteNativeWord,
    replay_complete_word,restrict_word,restrict_bank,strict_bytes,digest,packed,
    sources as legacy_sources,CALLS)
from certified_word_compiler import fixed

NATIVE_PINS={
    Path(fixed.__file__):'d9981004a89c651f072ff88732c8b402baf83c16690a0cfacfa9c32199fde254',
    Path(sys.modules[fixed.native_quartet.__module__].__file__):
        'e5cb9c4871da2662bbf831cc7721730593be478ebbe238a58d95ba2917dda47c',
}

PROFILE='TRACE_BALANCED_DYADIC_V1'
SCHEMA='BRC_SO_TRACE_BANK_V1'


def sources():
    for path,expected in {**PINS,**NATIVE_PINS}.items():
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise ValueError('frozen native dependency changed: '+str(path))
    return {'trace_bank_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'legacy_native_dependencies':legacy_sources(),
            'native_orientation_files':{path.name:sha for path,sha in NATIVE_PINS.items()}}


def program_view(program):
    # Preserve all old view fields, but strict JSON now also distinguishes
    # bool/int in cached columns, counts and carrier indices.
    raw=_program_view(program)
    return strict_bytes({'native_fields':raw[:-2],
        'phase_bindings':json.loads(raw[-2]),'codec_binding':json.loads(raw[-1])})


def primitive_orientation():
    actual=fixed.primitives()
    expected=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1))
    if (actual['h']!=expected or actual['neg']!=-1
            or actual['swap']!=((F(0),F(1)),(F(1),F(0)))):
        raise ValueError('actual primitive columns do not match determinant proof')
    return json.loads(packed({'schema':'BRC_NATIVE_ORIENTATION_PROOF_V1',
        'actual_primitive_receipt':actual,'H4_denominator':2,
        'primitive_determinants':{'h4':1,'neg':-1,'swap':-1},
        'proof':'actual H4 symmetric orthogonal with trace zero has two +1/two -1; '
                'neg and transposition each have determinant -1; '
                'distinct-coordinate embedding is permutation conjugacy',
        'orthogonality_source':'actual orthogonal primitive product and complete word replay',
        'classification_is_structural_not_generic_determinant_execution':True}))


@dataclass(frozen=True)
class SOTraceRecord:
    phase_index:int
    s:F
    bound_valid:bool
    bound_method:str
    bound_is_exact:bool
    certificate_sha256:str


class TraceReplayError(ValueError):
    def __init__(self,message,evidence):
        super().__init__(message)
        self.evidence=evidence


def certify_word(m,full,codec,primitive):
    expr=SignedExpressions()
    word=full.inverse_phase_word
    negative_positions=[j for j,gate in enumerate(word) if gate[0] in ('neg','swap')]
    parity=len(negative_positions)&1
    determinant=-1 if parity else 1
    orientation={'primitive_sha256':digest(primitive),
        'normalized_word':word,'negative_determinant_letter_positions':negative_positions,
        'negative_letter_parity':parity,'determinant':determinant,
        'structural_parity_not_a_numeric_determinant_observer':True}
    nodes=[];diagonal=[];tree=[];trace=None;margin=None;clip=None
    if determinant==1:
        for j in range(61):
            actual_diagonal=F(full.columns[j][j],full.den)
            value,index=expr.evaluate(f'deficit[{j}]',((F(1),),(-F(1),actual_diagonal)))
            node=len(nodes)
            nodes.append({'kind':'diagonal_deficit','coordinate':j,
                'column_scalar':str(actual_diagonal),'value':str(value),'expression_index':index})
            diagonal.append(node)
        current=diagonal
        level=0
        while len(current)>1:
            following=[];layer=[]
            for offset in range(0,len(current),2):
                left=current[offset]
                if offset+1==len(current):
                    following.append(left);layer.append({'carry_node':left});continue
                right=current[offset+1]
                value,index=expr.evaluate(f'trace_sum[{level},{offset//2}]',
                    ((F(nodes[left]['value']),),(F(nodes[right]['value']),)))
                node=len(nodes)
                nodes.append({'kind':'sum','left':left,'right':right,
                    'value':str(value),'expression_index':index})
                following.append(node);layer.append({'sum_node':node})
            tree.append(layer);current=following;level+=1
        trace=F(nodes[current[0]]['value'])
        if trace<0:raise ValueError('actual complete orthogonal trace defect is negative')
        value,index=expr.evaluate('four_minus_trace',((F(4),),(-F(1),trace)))
        margin={'value':str(value),'expression_index':index}
        clip='TRACE' if value>=0 else 'UNIVERSAL_FOUR'
        s=trace if value>=0 else F(4)
        exact=trace==0
        method='SO_HALF_TRACE_BOUND'
    else:
        s=F(4);exact=True;method='DET_MINUS_ONE_EXACT'
    if not 0<=s<=4:raise ValueError('certificate scalar outside closed range')
    codec_record=None
    if codec is not None:
        restricted=restrict_word(full,codec)
        codec_record={'binding':restricted.binding_record(),
            'forward_columns':restricted.columns,'inverse_columns':restricted.inverse_columns,
            'full_forward_inverse_blocks_and_identity_complement_checked':True}
    record={'schema':'BRC_COMPLETE_NATIVE_TRACE_BOUND_V1','phase_index':m,
        'full_dimension':61,'native_binding':full.binding_record(),
        'complete_forward_columns':full.columns,'complete_inverse_columns':full.inverse_columns,
        'denominator':full.den,'orientation':orientation,'exact_codec':codec_record,
        'trace_profile':PROFILE,'trace_defect':None if trace is None else str(trace),
        'trace_nodes':nodes,'diagonal_node_indices':diagonal,'balanced_levels':tree,
        'clipping_margin':margin,'clipping_branch':clip,
        's':str(s),'bound_valid':True,'bound_method':method,'bound_is_exact':exact,
        'inverse_uses_same_bound':True,
        'inverse_justification':'actual complete inverse equals transpose; 2I-G-G^T is unchanged',
        'proof':'SO nonzero B eigenvalues paired; half trace bounds largest; '
                'det-minus-one orthogonal word has -1 eigenvalue and squared distance exactly 4',
        'observer_operations':expr.observer.operations,
        'expression_reference_count':expr.references,
        'zero_expression_reference_count':expr.zero_expression_references,
        'actual_unique_observer_expressions':len(expr.observer.operations),
        'all_scientific_trace_scalars_from_signed_native_observer':True,
        'generic_SO_bound_is_not_claimed_exact':True,
        'old_B_squared_witness_not_executed':True}
    encoded=json.loads(packed(record))
    return encoded,SOTraceRecord(m,s,True,method,exact,digest(encoded))


@dataclass(frozen=True,init=False)
class SOTraceBank:
    binding_sha256:str
    _view_bytes:bytes
    _records:tuple
    _evidence_bytes:bytes

    def __init__(self,program):
        first,t0=len(CALLS),perf_counter()
        view=program_view(program);source=sources()
        primitive_start=len(CALLS);primitive=primitive_orientation();primitive_end=len(CALLS)
        records=[];words={};setups=[];full_bank={}
        for m,gate in sorted(program.bank.items()):
            start,t1=len(CALLS),perf_counter()
            before=replay_complete_word.cache_info()._asdict()
            replay_complete_word.cache_clear()
            full=CompleteNativeWord(gate.inverse_phase_word,61);full_bank[m]=full
            after=replay_complete_word.cache_info()._asdict();replay_end=len(CALLS)
            expected=full if program.codec is None else restrict_word(full,program.codec)
            if strict_bytes(expected.binding_record())!=strict_bytes(gate.binding_record()):
                raise ValueError('program word binding differs from actual complete replay')
            if strict_bytes((gate.den,gate.columns,gate.inverse_columns))!=strict_bytes(
                    (expected.den,expected.columns,expected.inverse_columns)):
                raise ValueError('program columns differ from actual complete replay')
            for key in ('_forward_nonzero','_inverse_nonzero'):
                if strict_bytes(getattr(gate,key,None))!=strict_bytes(getattr(expected,key,None)):
                    raise ValueError('program sparse native cache differs from replay')
            if strict_bytes(program.phase_bindings[str(m)])!=strict_bytes(full.binding_record()):
                raise ValueError('program full phase source binding is stale')
            evidence,record=certify_word(m,full,program.codec,primitive)
            words[str(m)]=evidence;records.append(record)
            setups.append({'phase_index':m,'call_interval':[start,len(CALLS)],
                'complete_native_replay_call_interval':[start,replay_end],
                'native_cache_before':before,'native_cache_after_fresh_replay':after,
                'native_cache_cleared_for_fresh_replay':True,
                'forward_basis_columns':61,'inverse_basis_columns':61,
                'inverse_recovery_basis_columns':61,
                'actual_unique_observer_expressions':evidence['actual_unique_observer_expressions'],
                'expression_reference_count':evidence['expression_reference_count'],
                'elapsed_seconds':perf_counter()-t1})
        if program.codec is not None:
            codec,_,binding=restrict_bank(full_bank,indices=program.codec.indices,full_dim=61)
            if (codec!=program.codec or strict_bytes(binding)!=strict_bytes(program.codec_binding)):
                raise ValueError('program codec differs from complete word replay')
        if program_view(program)!=view or sources()!=source:
            raise ValueError('program or source changed during trace admission')
        logical=json.loads(packed({'schema':SCHEMA,'source':source,'full_dimension':61,
            'encoded_dimension':program.dim,'primitive_orientation':primitive,
            'phase_bindings':program.phase_bindings,'codec_binding':program.codec_binding,
            'words':words,'omitted_program_fields':['N','a','work_modular_powers','history'],
            'scope':'actual full native-word norm bounds; no state/target-accuracy assertion'}))
        binding=digest(logical)
        evidence={'logical':logical,'binding_sha256':binding,
            'setup':{'call_interval':[first,len(CALLS)],'actual_core_calls':CALLS[first:],
                'core_call_count':len(CALLS)-first,'word_setups':setups,
                'primitive_call_interval':[primitive_start,primitive_end],
                'elapsed_seconds':perf_counter()-t0,
                'stored_trace_nodes':sum(len(v['trace_nodes']) for v in words.values()),
                'stored_complete_column_scalar_entries':len(records)*2*61*61,
                'logical_serialized_bytes':len(strict_bytes(logical)),
                'native_program_admission_setup_included':False,
                'repeated_check_runs_scientific_observers':False}}
        object.__setattr__(self,'binding_sha256',binding)
        object.__setattr__(self,'_view_bytes',view)
        object.__setattr__(self,'_records',tuple(records))
        object.__setattr__(self,'_evidence_bytes',strict_bytes(evidence))

    def check(self,program):
        if program_view(program)!=self._view_bytes:
            raise ValueError('trace bank does not match exact native words and codec')

    def get(self,m,*,inverse=False):
        if type(m) is not int or type(inverse) is not bool:
            raise ValueError('strict integer phase and boolean direction required')
        for record in self._records:
            if record.phase_index==m:return record
        raise KeyError(m)

    def evidence(self):
        return json.loads(self._evidence_bytes)

    @classmethod
    def restore(cls,program,serialized):
        def pairs(items):
            out={}
            for key,value in items:
                if key in out:raise ValueError('duplicate JSON key')
                out[key]=value
            return out
        if isinstance(serialized,(str,bytes)):
            serialized=json.loads(serialized,object_pairs_hook=pairs)
        if type(serialized) is not dict or set(serialized)!={'logical','binding_sha256','setup'}:
            raise ValueError('canonical complete trace-bank evidence required')
        if type(serialized['logical']) is not dict or serialized['logical'].get('schema')!=SCHEMA:
            raise ValueError('versioned trace-bank schema required')
        if type(serialized['binding_sha256']) is not str or digest(serialized['logical'])!=serialized['binding_sha256']:
            raise ValueError('trace bank logical hash mismatch')
        fresh=cls(program)
        if (strict_bytes(fresh.evidence()['logical'])!=strict_bytes(serialized['logical'])
                or fresh.binding_sha256!=serialized['binding_sha256']):
            raise TraceReplayError('trace certificate differs from complete fresh replay',fresh.evidence())
        return fresh
