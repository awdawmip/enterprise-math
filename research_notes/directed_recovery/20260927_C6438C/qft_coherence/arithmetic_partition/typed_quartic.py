"""Gaussian quartic Jacobi observer from actual typed integer transducers.

Gaussian pairs are exact labels, not complex amplitudes or a state propagator.
Signs, coordinate permutations and loop counts are host wiring; all magnitude
arithmetic, divisions, rounded quotient choices and residue updates use the
frozen actual BRC full-adder composition and retain their complete receipts.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import sys

ROOT=Path(__file__).resolve().parent
PREVIOUS=ROOT.parents[1]/'sep26-shor-general'
JACOBI=ROOT.parents[1]/'sep27-qft-research/character_certificates'
for path in (PREVIOUS/'optimization/lazy_modular',JACOBI):
    sys.path.insert(0,str(path))
from lazy_modular import Arithmetic,require,sparse,digest,source_binding
from lazy_gcd import typed_gcd_trace
from typed_jacobi import typed_jacobi_trace,certify_program_final_bit

SYMBOL='ACTUAL_TYPED_GAUSSIAN_QUARTIC_JACOBI_V1'
CHARACTER='ACTUAL_TYPED_PRIMITIVE_NORM_QUARTIC_CHARACTER_V1'
PROGRAM='ACTUAL_NATIVE_QUARTIC_UNIFORM_TWO_BIT_SUFFIX_V1'
UNITS=((1,0),(0,1),(-1,0),(0,-1))


def source():
    return {'quartic_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic_source':source_binding(),
        'jacobi_source_sha256':hashlib.sha256((JACOBI/'typed_jacobi.py').read_bytes()).hexdigest(),
        'gcd_source_sha256':hashlib.sha256((PREVIOUS/'optimization/lazy_modular/lazy_gcd.py').read_bytes()).hexdigest(),
        'math_source':'https://arxiv.org/pdf/1807.07719#page=13',
        'math_source_scope':'Bach-Sandlund section 7, primary convention, reciprocity and two supplements',
        'project_snapshot':'e8c5726a22d78c8d3623611afd33f4fe76b46321',
        'GK_snapshot':'f44ed5959c92e6e088c61c102951d1ab2c5e98d4',
        'activity':'RA-CAAAC604CB513AEA8BBC1DFC',
        'tool_route':'REUSE_APPLIED actual typed full-adder arithmetic; EXTEND Gaussian integer observer',
        'admission':'AUTHOR_ACTUAL_SHARED_CONTEXT_NOT_INDEPENDENTLY_ADMITTED'}


def pair(value):
    require(type(value) in (tuple,list) and len(value)==2
        and all(sparse.integer(x) for x in value),'two non-boolean integer Gaussian coordinates required')
    return tuple(value)


class SignedGaussian:
    def __init__(self):
        self.arithmetic=Arithmetic()
        self.events=[]
        self.sign_coordinate_wiring=0

    def add(self,x,y):
        if (x<0)==(y<0):
            magnitude,op=self.arithmetic.add(abs(x),abs(y))
            value=-magnitude if x<0 else magnitude
            receipt={'addition':op}
        else:
            relation,difference,op=self.arithmetic.compare(abs(x),abs(y))
            if relation>=0:
                value=-difference if x<0 else difference
                receipt={'comparison':op}
            else:
                _,difference,op2=self.arithmetic.compare(abs(y),abs(x))
                value=-difference if y<0 else difference
                receipt={'comparison':op,'reverse_difference':op2}
        self.sign_coordinate_wiring+=3
        self.events.append({'op':'signed_add','inputs':[x,y],'output':value,'receipt':receipt})
        return value

    def subtract(self,x,y):
        self.sign_coordinate_wiring+=1
        return self.add(x,-y)

    def multiply(self,x,y):
        magnitude,op=self.arithmetic.multiply(abs(x),abs(y))
        value=-magnitude if (x<0)!=(y<0) else magnitude
        self.sign_coordinate_wiring+=3
        self.events.append({'op':'signed_multiply','inputs':[x,y],'output':value,'operation':op})
        return value

    def exact_divide(self,x,d):
        q,r,op=self.arithmetic.divide(abs(x),d)
        require(r==0,'signed exact division has nonzero remainder')
        value=-q if x<0 else q
        self.sign_coordinate_wiring+=2
        self.events.append({'op':'signed_exact_divide','input':x,'denominator':d,
                            'output':value,'operation':op})
        return value

    def residue(self,x,d):
        _,r,op=self.arithmetic.divide(abs(x),d)
        complement=None
        if x<0 and r:
            _,r,complement=self.arithmetic.compare(d,r)
        self.sign_coordinate_wiring+=1
        self.events.append({'op':'signed_nonnegative_residue','input':x,'modulus':d,
                            'output':r,'division':op,'negative_complement':complement})
        return r

    def nearest(self,x,d):
        q,r,op=self.arithmetic.divide(abs(x),d)
        twice,addition=self.arithmetic.add(r,r)
        relation,_,comparison=self.arithmetic.compare(twice,d)
        increment=None
        if relation>=0:
            q,increment=self.arithmetic.add(q,1)
        value=-q if x<0 else q
        self.sign_coordinate_wiring+=2
        self.events.append({'op':'nearest_integer_ties_away_from_zero','numerator':x,
            'denominator':d,'output':value,'division':op,'double_remainder':addition,
            'halfway_comparison':comparison,'increment':increment})
        return value

    def gadd(self,x,y):
        return self.add(x[0],y[0]),self.add(x[1],y[1])

    def gsubtract(self,x,y):
        return self.subtract(x[0],y[0]),self.subtract(x[1],y[1])

    def gmultiply(self,x,y):
        ac,bd=self.multiply(x[0],y[0]),self.multiply(x[1],y[1])
        ad,bc=self.multiply(x[0],y[1]),self.multiply(x[1],y[0])
        return self.subtract(ac,bd),self.add(ad,bc)

    def norm(self,x):
        return self.add(self.multiply(x[0],x[0]),self.multiply(x[1],x[1]))

    def primary(self,z):
        total=self.add(z[0],z[1])
        self.sign_coordinate_wiring+=1
        return not(z[1]&1) and self.residue(total,4)==1

    def normalize(self,z):
        # Candidate j is z/i^j. These are signed coordinate permutations.
        x,y=z
        candidates=((x,y),(y,-x),(-x,-y),(-y,x))
        self.sign_coordinate_wiring+=8
        for j,candidate in enumerate(candidates):
            if self.primary(candidate):
                return candidate,j
        raise ValueError('Gaussian element is not odd and has no primary associate')

    def remainder(self,alpha,beta):
        norm=self.norm(beta)
        require(norm>0,'zero Gaussian divisor')
        self.sign_coordinate_wiring+=1
        numerator=self.gmultiply(alpha,(beta[0],-beta[1]))
        quotient=(self.nearest(numerator[0],norm),self.nearest(numerator[1],norm))
        remainder=self.gsubtract(alpha,self.gmultiply(quotient,beta))
        remainder_norm=self.norm(remainder)
        twice=self.add(remainder_norm,remainder_norm)
        relation,_,comparison=self.arithmetic.compare(twice,norm)
        require(relation<=0,'Gaussian remainder norm exceeds half the divisor norm')
        return remainder,{'quotient':quotient,'remainder':remainder,'divisor_norm':norm,
            'remainder_norm':remainder_norm,'half_norm_comparison':comparison}

    def cost(self):
        return {**{k:v for k,v in self.arithmetic.stats.items() if k!='native_kernel_calls_delta'},
            'signed_coordinate_wiring_operations':self.sign_coordinate_wiring}


def quartic_symbol_trace(alpha,beta):
    """Return zero, or i^exponent for arbitrary Gaussian alpha and odd beta.

    The denominator denotes its principal ideal, so replacing it by a unit
    associate does not change this symbol. Numerator units do require their
    supplementary factors. The empty denominator ideal (a unit) returns one.
    """
    alpha,beta=pair(alpha),pair(beta)
    require((beta[0]&1)!=(beta[1]&1),'odd nonzero Gaussian denominator required')
    observed=SignedGaussian()
    initial_beta,associate=observed.normalize(beta)
    x,n=alpha,initial_beta
    exponent,steps=0,[]
    while True:
        denominator_norm=observed.norm(n)
        if denominator_norm==1:
            zero=False;terminal='unit_denominator';break
        gamma,division=observed.remainder(x,n)
        if gamma==(0,0):
            zero=True;terminal='nonunit_common_divisor';break
        before_gamma=gamma
        ramified=[]
        while (gamma[0]&1)==(gamma[1]&1):
            e,f=gamma
            gamma=(observed.exact_divide(observed.add(e,f),2),
                   observed.exact_divide(observed.subtract(f,e),2))
            ramified.append({'input':(e,f),'output':gamma})
            observed.sign_coordinate_wiring+=2
        delta,unit_power=observed.normalize(gamma)
        c,d=n
        half_c=observed.exact_divide(observed.subtract(c,1),2)
        supplement=observed.exact_divide(observed.subtract(
            observed.subtract(observed.subtract(c,d),observed.multiply(d,d)),1),4)
        half_e=observed.exact_divide(observed.subtract(delta[0],1),2)
        first=observed.multiply(len(ramified),supplement)
        second=observed.multiply(unit_power,half_c)
        third=observed.multiply(2,observed.multiply(half_e,half_c))
        correction=observed.add(observed.subtract(first,second),third)
        updated=observed.residue(observed.add(exponent,correction),4)
        steps.append({'numerator':x,'primary_denominator':n,'denominator_norm':denominator_norm,
            'division':division,'raw_remainder':before_gamma,'ramified_divisions':ramified,
            'odd_remainder':gamma,'unit_power':unit_power,'next_primary_denominator':delta,
            'one_plus_i_supplement_exponent':supplement,'half_c_minus_one':half_c,
            'reciprocity_half_e_minus_one':half_e,'correction':correction,
            'input_exponent':exponent,'output_exponent':updated})
        x,n,exponent=n,delta,updated
    return {'schema':SYMBOL,'alpha':alpha,'beta':beta,'initial_primary_denominator':initial_beta,
        'initial_denominator_unit_power':associate,'zero':zero,
        'exponent':None if zero else exponent,'unit_value':(0,0) if zero else UNITS[exponent],
        'steps':steps,'terminal':{'reason':terminal,'numerator':x,'denominator':n,
            'denominator_norm':denominator_norm},
        'arithmetic_operations':observed.arithmetic.operations,'signed_observer_events':observed.events,
        'cost':observed.cost(),'source':source(),
        'ordinary_complex_or_float_arithmetic_used':False,
        'ordinary_integer_remainder_or_pow_used':False,
        'factorization_or_order_search_performed':False,
        'observer_only_no_state_propagation':True}


def verify_quartic_symbol(certificate):
    require(isinstance(certificate,dict) and certificate.get('schema')==SYMBOL,'wrong quartic symbol schema')
    rebuilt=quartic_symbol_trace(certificate['alpha'],certificate['beta'])
    require(digest(rebuilt)==digest(certificate),'quartic symbol certificate does not replay')
    return {'verified':True,'zero':rebuilt['zero'],'exponent':rebuilt['exponent'],
            'certificate_sha256':digest(rebuilt)}


def certify_character(N,u,v):
    require(sparse.integer(N) and N>=3 and (N&1),'odd integer N>=3 required')
    require(sparse.integer(u) and sparse.integer(v) and u!=0 and v!=0,
            'nonzero signed integer norm coordinates required')
    require((u&1)!=(v&1),'opposite parity norm coordinates required')
    observed=SignedGaussian()
    norm=observed.norm((u,v))
    relation,_,comparison=observed.arithmetic.compare(norm,N)
    require(relation==0,'public Gaussian norm does not equal N')
    gcd=typed_gcd_trace(abs(u),abs(v))
    require(gcd['value']==1,'primitive norm witness required by this character interface')
    primary,j=observed.normalize((u,v))
    return {'schema':CHARACTER,'N':N,'u':u,'v':v,'primary_denominator':primary,
        'denominator_unit_power':j,'norm':norm,'norm_comparison':comparison,'primitive_gcd':gcd,
        'arithmetic_operations':observed.arithmetic.operations,'signed_observer_events':observed.events,
        'cost':observed.cost(),'source':source(),
        'domain':'rational units modulo N; nonunits are returned as zero, not a color',
        'color_law':'chi(x*y mod N)=chi(x)+chi(y) mod 4 on units',
        'square_law':'(-1)^chi(w)=Jacobi(w,N)',
        'bare_work_label_coloring_implemented':True,
        'factorization_or_order_input':False}


def verify_character(certificate):
    require(isinstance(certificate,dict) and certificate.get('schema')==CHARACTER,'wrong character schema')
    rebuilt=certify_character(*(certificate[k] for k in ('N','u','v')))
    require(digest(rebuilt)==digest(certificate),'quartic character does not replay')
    return {'verified':True,'certificate_sha256':digest(rebuilt)}


def color_trace(w,character):
    require(sparse.integer(w),'integer rational work label required')
    verify_character(character)
    symbol=quartic_symbol_trace((w,0),(character['u'],character['v']))
    return {'N':character['N'],'work_label':w,'character_sha256':digest(character),
        'color':symbol['exponent'],'is_unit':not symbol['zero'],'symbol':symbol}


def certify_program_two_bit_suffix(program,u,v):
    canonical=certify_program_final_bit(program)
    character=certify_character(program.N,u,v)
    base=color_trace(program.a,character)
    require(base['is_unit'],'program base must be a character unit')
    available=base['color'] in (1,3)
    require(available==(canonical['status']=='CERTIFIED_FINAL_BIT_FAIR'),
            'quartic square law disagrees with canonical typed Jacobi')
    return {'schema':PROGRAM,'status':'CERTIFIED_UNIFORM_TERMINAL_TWO_BITS' if available else 'UNAVAILABLE',
        'suffix_start_depth':program.t-2,'program_witness':canonical,'character':character,
        'base_color':base,'source':source(),'all_residual_coordinates_retained':True,
        'arbitrary_midrun_state_authorized':False,'complete_row_oracle_must_be_retained':True,
        'scope':'joint conditional uniform two-bit suffix on unchanged admitted canonical square program'}


def verify_program_two_bit_suffix(certificate,program):
    require(isinstance(certificate,dict) and certificate.get('schema')==PROGRAM,'wrong quartic program schema')
    character=certificate['character']
    rebuilt=certify_program_two_bit_suffix(program,character['u'],character['v'])
    require(digest(rebuilt)==digest(certificate),'quartic program certificate does not replay')
    return {'verified':True,'status':rebuilt['status'],'certificate_sha256':digest(rebuilt)}
