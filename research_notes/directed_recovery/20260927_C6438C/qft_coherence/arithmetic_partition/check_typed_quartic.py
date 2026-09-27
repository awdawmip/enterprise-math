"""Bounded native arithmetic, quartic laws and complete actual suffix fields."""
from __future__ import annotations
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
import sys
from typed_quartic import (PREVIOUS,SignedGaussian,quartic_symbol_trace,verify_quartic_symbol,
    certify_character,verify_character,color_trace,certify_program_two_bit_suffix,
    verify_program_two_bit_suffix,Arithmetic,typed_jacobi_trace)
from lazy_modular import inverse_certificate,lazy_modular_power_trace
from stage45.brc_loop_recheck import CALLS,verify_vendor

ROOT=Path(__file__).resolve().parent
for path in (PREVIOUS/'optimization/collision_analysis',PREVIOUS/'optimization/streaming'):
    sys.path.insert(0,str(path))
from check_gram_sampler import load_bank
from lazy_streaming import LazyStreamingProgram
from stage80.fixed_phase import norm


def clean(x):
    if isinstance(x,F):return {'numerator':x.numerator,'denominator':x.denominator}
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [clean(v) for v in x]
    return x


def reject(name,action,results):
    try:action()
    except ValueError as error:results.append({'name':name,'rejected':True,'message':str(error)})
    else:raise AssertionError('accepted negative control '+name)


def pack(state,den):
    return {'denominator':den,'rows':[[key,row] for key,row in sorted(state.items())]}


def main():
    first=len(CALLS)
    vendor=verify_vendor()
    files=(Path(__file__),ROOT/'typed_quartic.py')
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    arithmetic=Arithmetic()
    observers=[]
    # Prime Euler comparisons are finite-field typed observers of the definition,
    # never an ideal quantum propagator or a factoring oracle.
    euler=[]
    for p,u,v in ((5,1,2),(13,3,2),(17,1,4)):
        inverse=inverse_certificate(p,v)
        negative_u,negative_ops=arithmetic.modsubtract(0,u,p)
        root_i,root_ops=arithmetic.modmul(negative_u,inverse['inverse_multiplier'],p)
        _,pminus,_=arithmetic.compare(p,1)
        exp,rem,exp_op=arithmetic.divide(pminus,4)
        assert rem==0
        for w in range(p):
            symbol=quartic_symbol_trace((w,0),(u,v))
            replay=verify_quartic_symbol(symbol)
            if w==0:
                assert symbol['zero'];power=encoding=None
            else:
                power=lazy_modular_power_trace(p,w,exp)
                encoding=lazy_modular_power_trace(p,root_i,symbol['exponent'])
                assert power['value']==encoding['value']
            euler.append({'p':p,'u':u,'v':v,'w':w,'root_i':root_i,'root_inverse':inverse,
                'root_minus_u_operations':negative_ops,'root_modmul':root_ops,
                'exponent_operation':exp_op,'symbol':symbol,'replay':replay,
                'typed_euler_power':power,'typed_character_encoding':encoding})
    # Units, even/negative/complex numerators, inert and composite denominators.
    generic=[]
    for alpha,beta in [((0,0),(1,0)),((0,0),(3,0)),((0,1),(1,2)),((-1,0),(1,2)),
        ((2,0),(3,0)),((3,0),(3,0)),((4,-6),(1,8)),((-9,12),(2,9)),
        ((-3,-2),(-7,2)),((6,4),(3,6)),((2,0),(1,-2)),((2,0),(2,-1))]:
        symbol=quartic_symbol_trace(alpha,beta)
        generic.append({'symbol':symbol,'replay':verify_quartic_symbol(symbol)})
    characters,laws=[],[]
    for N,u,v,a in ((25,3,4,2),(65,1,8,3),(85,2,9,2)):
        character=certify_character(N,u,v)
        verify_character(character)
        values={}
        for w in range(N):
            color=color_trace(w,character)
            jacobi=typed_jacobi_trace(w,N)
            assert (0 if not color['is_unit'] else (-1 if color['color']&1 else 1))==jacobi['value']
            values[w]=color
            laws.append({'N':N,'w':w,'color':color,'jacobi':jacobi,'square_law':True})
        base=values[a]
        transport=[]
        for w,record in values.items():
            target,ops=arithmetic.modmul(a,w,N)
            actual=values[target]
            if record['is_unit']:
                summed,addop=arithmetic.add(base['color'],record['color'])
                _,expected,reduceop=arithmetic.divide(summed,4)
                assert actual['color']==expected
            else:addop=reduceop=None;assert not actual['is_unit']
            transport.append({'w':w,'target':target,'modmul_operations':ops,
                'color_addition':addop,'color_reduction':reduceop})
        characters.append({'character':character,'base':a,'transport':transport,
            'all_residue_colors':values})
    # Explicit known Gaussian factors are used only for this isolated definition
    # fixture. They are not inputs to the generic symbol/character algorithm.
    g=SignedGaussian()
    assert g.gmultiply((-1,2),(3,-2))==(1,8)
    product=[]
    for w in (0,1,2,3,5,7,11,13,17,64):
        whole=quartic_symbol_trace((w,0),(1,8))
        left=quartic_symbol_trace((w,0),(-1,2))
        right=quartic_symbol_trace((w,0),(3,-2))
        if left['zero'] or right['zero']:assert whole['zero']
        else:
            total,op=arithmetic.add(left['exponent'],right['exponent'])
            _,expected,red=arithmetic.divide(total,4)
            assert whole['exponent']==expected
        product.append({'w':w,'whole':whole,'left':left,'right':right})
    observers.append({'purpose':'explicit composite denominator fixture',
                     'arithmetic':g.arithmetic.operations,'events':g.events})

    bank,bank_source=load_bank()
    native=[]
    for N,a,u,v in ((65,3,1,8),(85,2,2,9)):
        program=LazyStreamingProgram(N,a,4,bank,61)
        certificate=certify_program_two_bit_suffix(program,u,v)
        assert certificate['status']=='CERTIFIED_UNIFORM_TERMINAL_TWO_BITS'
        replay=verify_program_two_bit_suffix(certificate,program)
        character=certificate['character'];cache={}
        def color(w):
            if w not in cache:cache[w]=color_trace(w,character)
            assert cache[w]['is_unit']
            return cache[w]['color']
        state,den=program.initial()
        frontier={(): (state,den)};records=[];fair=0;total=F(0)
        for depth in range(program.t):
            following={}
            for history,(state,den) in frontier.items():
                labels={key[1] for key,row in state.items() if any(row)}
                before={color(w) for w in labels}
                translated={color(program.tables[depth][w]) for w in labels}
                children=program.branches(state,den,history)
                parent=norm(state,den);masses=tuple(norm(s,d) for s,d in children)
                assert sum(masses)==parent
                if depth>=program.t-2:
                    assert before.isdisjoint(translated)
                    assert masses==(parent/2,parent/2);fair+=2
                records.append({'history':history,'parent':pack(state,den),
                    'children':[pack(s,d) for s,d in children],
                    'source_colors':sorted(before),'translated_colors':sorted(translated),
                    'child_masses':masses,'color_disjoint':before.isdisjoint(translated)})
                for bit,child in enumerate(children):
                    if masses[bit]:
                        if depth+1==program.t:total+=masses[bit]
                        else:following[history+(bit,)]=child
            frontier=following
        assert total==1
        native.append({'N':N,'a':a,'certificate':certificate,'replay':replay,
            'full_prefixes':records,'computed_bare_label_colors':cache,
            'certified_fair_child_edges':fair,'terminal_mass':total})
    negatives=[]
    for name,action in [
        ('even Gaussian denominator',lambda:quartic_symbol_trace((1,0),(1,1))),
        ('zero denominator',lambda:quartic_symbol_trace((1,0),(0,0))),
        ('boolean coordinate',lambda:quartic_symbol_trace((True,0),(1,2))),
        ('false norm witness',lambda:certify_character(65,1,6)),
        ('nonprimitive witness',lambda:certify_character(45,3,6)),
        ('even modulus',lambda:certify_character(10,1,3))]:reject(name,action,negatives)
    altered=deepcopy(euler[2]['symbol']);altered['exponent']=0
    if altered['exponent']==euler[2]['symbol']['exponent']:altered['exponent']=1
    reject('changed color',lambda:verify_quartic_symbol(altered),negatives)
    changed=deepcopy(characters[0]['character']);changed['source']['quartic_source_sha256']='0'*64
    reject('changed source',lambda:verify_character(changed),negatives)
    altered_program=deepcopy(native[0]['certificate']);altered_program['suffix_start_depth']+=1
    p=LazyStreamingProgram(65,3,4,bank,61)
    reject('changed suffix boundary',lambda:verify_program_two_bit_suffix(altered_program,p),negatives)
    p.initial=lambda: ({(0,3,0):(1,)+(0,)*60},1)
    reject('injected initial work',lambda:certify_program_two_bit_suffix(p,1,8),negatives)
    del p.initial
    unavailable=certify_program_two_bit_suffix(LazyStreamingProgram(65,2,4,bank,61),1,8)
    assert unavailable['status']=='UNAVAILABLE'
    assert hashes=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    result={'status':'AUTHOR_ACTUAL_SHARED_CONTEXT_NOT_INDEPENDENTLY_ADMITTED',
        'source_hashes':hashes,'kernel_verification':vendor,'prime_euler_observers':euler,
        'general_gaussian_cases':generic,'rational_square_laws':laws,'characters':characters,
        'composite_denominator_product_cases':product,'auxiliary_observers':observers,
        'actual_full_program_cases':native,'phase_bank_source':bank_source,
        'negative_controls':negatives,'unavailable_program':unavailable,
        'arithmetic_operations':arithmetic.operations,'native_core_calls':CALLS[first:],
        'classical_quantum_reference_run':False,'all_61_residual_coordinates_retained':True,
        'native_state_propagator_changed':False}
    raw=json.dumps(clean(result),sort_keys=True,separators=(',',':')).encode()
    (ROOT/'QUARTIC_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    summary={'status':result['status'],'prime_euler_cases':len(euler),'generic_gaussian_cases':len(generic),
        'rational_square_law_cases':len(laws),'full_residue_transport_moduli':[25,65,85],
        'composite_denominator_product_cases':len(product),
        'actual_full_program_cases':len(native),'positive_native_prefixes':sum(len(x['full_prefixes']) for x in native),
        'fair_child_edges':sum(x['certified_fair_child_edges'] for x in native),
        'negative_controls':len(negatives),'unavailable_status_preserved':True,
        'native_core_calls':len(CALLS)-first,'source_hashes':hashes,
        'payload_sha256':hashlib.sha256(raw).hexdigest()}
    (ROOT/'QUARTIC_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary))


if __name__=='__main__':main()
