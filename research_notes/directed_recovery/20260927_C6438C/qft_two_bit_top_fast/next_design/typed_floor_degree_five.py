"""Code-only fixed degree-five single-floor moments on the actual typed runner.

No scientific run occurs on import. This successor requires a separately
reviewed checker and actual startup guard before execution.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import sys

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'sep27-qft-adaptive/nonzero_structure'
BASE_PIN='633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2'
PROOF_PIN='1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

if sha(BASE/'typed_floor_moments.py')!=BASE_PIN:
    raise ValueError('frozen floor arithmetic changed')
sys.path.insert(0,str(BASE))
from typed_floor_moments import TypedFloorMoments,require

DEGREES=tuple((p,e) for e in range(6) for p in range(6-e))
BINOMIAL=((1,),(1,1),(1,2,1),(1,3,3,1),(1,4,6,4,1),(1,5,10,10,5,1))
# Numerator coefficients are (power, integer coefficient), no zero terms.
POWER_SUMS=((1,((1,1),)),(2,((2,1),(1,-1))),
    (6,((3,2),(2,-3),(1,1))),(4,((4,1),(3,-2),(2,1))),
    (30,((5,6),(4,-15),(3,10),(1,-1))),
    (12,((6,2),(5,-6),(4,5),(2,-1))))


class FloorDegreeFiveRunner(TypedFloorMoments):
    def __init__(self):
        super().__init__()
        self._extension_source=sha(__file__)

    def _check(self):
        require(sha(__file__)==self._extension_source,'degree-five source changed')
        require(sha(BASE/'typed_floor_moments.py')==BASE_PIN,'base floor source changed')
        require(sha(ROOT/'DEGREE_FIVE_RECIPROCITY.md')==PROOF_PIN,'degree-five proof changed')
        # The inherited source field still binds the unchanged arithmetic base.
        super()._check()

    def small_power(self,value,exponent):
        require(type(exponent) is int and 0<=exponent<=6,'fixed exponent 0..6 required')
        answer=1
        for _ in range(exponent):
            answer=self.mul(answer,value)
        return answer

    def power_sums(self,n):
        require(type(n) is int and n>=0,'nonnegative integer length required')
        if not n:
            return (0,0,0,0,0,0)
        powers=[1,n]
        for _ in range(2,7):
            powers.append(self.mul(powers[-1],n))
        result=[]
        for denominator,terms in POWER_SUMS:
            numerator=self.total(self.mul(coefficient,powers[exponent])
                for exponent,coefficient in terms)
            result.append(self.exact_div(numerator,denominator))
        return tuple(result)

    def moments(self,n,m,a,b,_depth=0):
        self._check()
        require(all(type(x) is int for x in (n,m,a,b)) and n>=0 and m>=1,
            'strict integer n>=0,m>=1 and signed a,b required')
        self.stats['moment_requests']+=1
        self.stats['max_recursion_depth']=max(self.stats['max_recursion_depth'],_depth)
        key=n,m,a,b
        if key in self.cache:
            self.stats['cache_hits']+=1
            return dict(self.cache[key])
        start=len(self.signed_operations)
        sums=self.power_sums(n)
        output={(p,e):sums[p] if e==0 else 0 for p,e in DEGREES}
        branch,child='empty',None
        details={'maximum_total_degree':5,'normalization':None,'height':None,
            'zero_coefficient_omissions':[],'reconstruction':[]}
        if n:
            normalization_start=len(self.signed_operations)
            A,a0=self.floor_div(a,m)
            B,b0=self.floor_div(b,m)
            details['normalization']={'A':A,'a0':a0,'B':B,'b0':b0,
                'signed_operations_start':normalization_start,'signed_operations_stop':len(self.signed_operations)}
            if A or B:
                branch,child='normalize_signed_coefficients',(n,m,a0,b0)
                g=self.moments(*child,_depth=_depth+1)
                for p,e in DEGREES:
                    if not e:
                        continue
                    operation_start=len(self.signed_operations)
                    terms=[]
                    for k in range(e+1):
                        for l in range(e-k+1):
                            if (A==0 and l>0) or (B==0 and e-k-l>0):
                                details['zero_coefficient_omissions'].append(
                                    {'p':p,'e':e,'k':k,'l':l,'A_zero':A==0,'B_zero':B==0})
                                continue
                            coefficient=self.mul(BINOMIAL[e][k],BINOMIAL[e-k][l])
                            coefficient=self.mul(coefficient,self.small_power(A,l))
                            coefficient=self.mul(coefficient,self.small_power(B,e-k-l))
                            terms.append(self.mul(coefficient,g[p+l,k]))
                    output[p,e]=self.total(terms)
                    details['reconstruction'].append({'p':p,'e':e,'value':output[p,e],
                        'signed_operations_start':operation_start,'signed_operations_stop':len(self.signed_operations)})
            elif not a:
                branch='normalized_constant_zero'
            else:
                height_start=len(self.signed_operations)
                Y,remainder=self.floor_div(self.add(self.mul(a,self.sub(n,1)),b),m)
                details['height']={'Y':Y,'remainder':remainder,'signed_operations_start':height_start,
                    'signed_operations_stop':len(self.signed_operations)}
                if not Y:
                    branch='normalized_zero_height'
                else:
                    offset=self.sub(self.add(self.sub(m,b),a),1)
                    branch,child='transpose_lattice',(Y,a,m,offset)
                    g=self.moments(*child,_depth=_depth+1)
                    for p,e in DEGREES:
                        if not e:
                            continue
                        operation_start=len(self.signed_operations)
                        denominator,numerator_coefficients=POWER_SUMS[p]
                        endpoint=self.mul(self.mul(denominator,self.small_power(Y,e)),sums[p])
                        terms=[]
                        for v in range(e):
                            for h,c in numerator_coefficients:
                                # p+e<=5 and e>=1 imply v+h<=5.
                                coefficient=self.mul(BINOMIAL[e][v],c)
                                terms.append(self.mul(coefficient,g[v,h]))
                        numerator=self.sub(endpoint,self.total(terms))
                        output[p,e]=self.exact_div(numerator,denominator)
                        details['reconstruction'].append({'p':p,'e':e,'denominator':denominator,
                            'numerator':numerator,'value':output[p,e],'signed_operations_start':operation_start,
                            'signed_operations_stop':len(self.signed_operations)})
        self.cache[key]=dict(output)
        self.nodes.append({'parameters':key,'branch':branch,'child':child,
            'signed_operations_start':start,'signed_operations_stop':len(self.signed_operations),
            'moments':{f'{p},{e}':output[p,e] for p,e in DEGREES},'degree_five_details':details})
        return dict(output)

    def evidence(self):
        result=super().evidence()
        result.update(schema='BRC_DEGREE_FIVE_SINGLE_FLOOR_MOMENTS_V1',
            source_sha256=self._extension_source,base_arithmetic_source_sha256=BASE_PIN,
            proof_sha256=PROOF_PIN,maximum_total_degree=5,
            scope='Fixed degree-five single-floor integer moments; no mixed-floor or order oracle')
        return deepcopy(result)
