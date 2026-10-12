"""Independent arithmetic prepared before the new family Source delivery.

This module imports no producer/consumer code and accepts no result by itself.
Its caller must first verify the immutable Source/RR and complete custody.
No scientific case is executed by loading this module or invoking its CLI.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

P=17
N=16
SIDE_CAP=2331
PORTABLE_SHA='7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce'
PROBLEM_SHA='a16356adfd5c1763ed0c0426b381d89f70f0c51736335687578f1b9a5c63db0d'

def check(value,message):
    if not value: raise AssertionError(message)

def reject_float(value):
    raise ValueError('floating mathematical JSON value')

def unique_keys(items):
    result={}
    for key,value in items:
        check(key not in result,'duplicate JSON key')
        result[key]=value
    return result

def read_json(path,expected_sha=None):
    raw=Path(path).read_bytes()
    check(expected_sha is None or hashlib.sha256(raw).hexdigest()==expected_sha,
          'immutable byte SHA256')
    return json.loads(raw,parse_float=reject_float,object_pairs_hook=unique_keys)

def rational(value):
    check(type(value) is list and len(value)==2,'rational pair')
    check(all(type(x) is str for x in value),'rational decimal strings')
    check(int(value[1])>0,'positive rational denominator')
    return F(int(value[0]),int(value[1]))

def pair(value):
    value=F(value)
    return [str(value.numerator),str(value.denominator)]

def dot(left,right):
    check(len(left)==len(right),'dot dimensions')
    return sum((a*b for a,b in zip(left,right)),F())

def determinant(matrix):
    rows=[[F(v) for v in row] for row in matrix]
    n=len(rows)
    check(all(len(row)==n for row in rows),'square determinant')
    result=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if rows[i][k]),None)
        if pivot is None: return F()
        if pivot!=k:
            rows[k],rows[pivot]=rows[pivot],rows[k]
            result=-result
        value=rows[k][k]
        result*=value
        for i in range(k+1,n):
            quotient=rows[i][k]/value
            rows[i]=[a-quotient*b for a,b in zip(rows[i],rows[k])]
    return result

def residues(vector):
    check(len(vector)==N,'mixed vector dimension')
    return [sum(vector[j-1]*pow(j,-k,P**k) for j in range(1,N+1))%(P**k)
            for k in range(1,7)]

def gram_schmidt(rows):
    stars=[]
    norms=[]
    mu=[]
    for row in rows:
        row=list(map(F,row))
        coefficients=[dot(row,v)/d for v,d in zip(stars,norms)]
        remainder=[row[j]-sum(c*v[j] for c,v in zip(coefficients,stars))
                   for j in range(N)]
        norm=dot(remainder,remainder)
        check(norm>0,'full-rank exact Gram factors')
        for prior in stars: check(dot(remainder,prior)==0,'GS orthogonality')
        stars.append(remainder)
        norms.append(norm)
        mu.append(coefficients)
    return stars,norms,mu

def verify_common(portable):
    check(portable['dimension']==N and portable['degree']==6,'common dimensions')
    basis=[[int(v) for v in row] for row in portable['unweighted_basis']]
    weighted=[[int(v) for v in row] for row in portable['weighted_basis']]
    weights=[P*j-1 for j in range(1,N+1)]
    check(len(basis)==N and all(len(row)==N for row in basis),'basis16x16')
    check(list(map(int,portable['weights']))==weights,'q0 weights')
    check(weighted==[[v*w for v,w in zip(row,weights)] for row in basis],
          'weighted basis identity')
    check(all(residues(row)==[0]*6 for row in basis),'every kernel row')
    det=determinant(basis)
    check(abs(det)==P**21,'exact kernel determinant17^21')
    minors={}
    for columns in (range(1,7),range(11,17)):
        minor=determinant([[pow(j,-k,P) for j in columns] for k in range(1,7)])
        check(minor.denominator==1 and int(minor)%P!=0,'unit inverse-power minor')
        minors[str(list(columns))]=str(minor)
    # A unit minor modulo17 is invertible modulo17^6. Hence the mixed map
    # onto product Z/(17^k) is surjective, its kernel has index17^21,
    # and the contained lattice of that determinant is the full kernel.
    stars,norms,mu=gram_schmidt(weighted)
    check(norms==[rational(v) for v in portable['gram_schmidt_squared']],
          'all exact GS squared norms')
    encoded=portable['mu']
    check(len(encoded)==N,'mu row count')
    for i in range(N):
        check(len(encoded[i])==N,'mu row width')
        check([rational(encoded[i][j]) for j in range(i)]==mu[i],'every GS mu')
        check(rational(encoded[i][i])==1,'mu diagonal')
        check(all(rational(encoded[i][j])==0 for j in range(i+1,N)),'mu padding')
    return {'basis':basis,'weighted':weighted,'weights':weights,'stars':stars,
            'norms':norms,'mu':mu,'determinant':det,'unit_minors':minors}

def prime_factors(value):
    value=int(value)
    check(value>0,'positive cofactor')
    result=[]
    prime=2
    while prime*prime<=value:
        while value%prime==0:
            result.append(prime)
            value//=prime
        prime+=1
    if value>1: result.append(value)
    return result

def exact_case(case):
    positive=[tuple(map(int,atom)) for atom in case['positive_atoms']]
    negative=[tuple(map(int,atom)) for atom in case['negative_atoms']]
    atoms=positive+negative
    check(all(q in (1,2) and 1<=r<=16 for q,r in atoms),'exact atom domain')
    positive_budget=SIDE_CAP-sum(P*(P*q+r)-1 for q,r in positive)
    negative_budget=SIDE_CAP-sum(P*(P*q+r)-1 for q,r in negative)
    check(min(positive_budget,negative_budget)>=0,'nonnegative separate side budgets')
    targets=[(-sum(pow(P*q+r,-k,P**k) for q,r in positive)
               +sum(pow(P*q+r,-k,P**k) for q,r in negative))%(P**k)
             for k in range(1,7)]
    radius=positive_budget**2+negative_budget**2
    check(int(case['q0_positive_budget'])==positive_budget,'positive atom mass budget')
    check(int(case['q0_negative_budget'])==negative_budget,'negative atom mass budget')
    check(list(map(int,case['mixed_targets']))==targets,'all six original targets')
    check(int(case['radius_squared'])==radius,'necessary sphere radius')
    factors=[prime_factors(P*q+r) for q,r in atoms]
    outside=any(any(v>P for v in row) for row in factors)
    return {'id':case['id'],'positive_atoms':positive,'negative_atoms':negative,
            'positive_budget':positive_budget,'negative_budget':negative_budget,
            'targets':targets,'radius_squared':radius,'cofactor_factorizations':factors,
            'maximal_p17_domain':'OUTSIDE' if outside else 'ADMISSIBLE'}

def verify_family_descriptors(problem):
    expected=[]
    for r in range(1,17): expected.append((f'q2-{r}',[(2,r)],[]))
    for r in range(1,17):
        for s in range(r,17): expected.append((f'same-q1-{r}-{s}',[(1,r),(1,s)],[]))
    for r in range(1,17):
        for s in range(r+1,17): expected.append((f'opposite-q1-{r}-{s}',[(1,r)],[(1,s)]))
    cases=problem['cases']
    check(len(cases)==272 and len({c['id'] for c in cases})==272,'272 distinct descriptors')
    check([(c['id'],[tuple(map(int,x)) for x in c['positive_atoms']],
             [tuple(map(int,x)) for x in c['negative_atoms']]) for c in cases]==expected,
          'complete primitive family, including repeated and mixed-sign atoms')
    check(problem['common_basis_sha256']==PORTABLE_SHA,'case-common pin')
    check(list(map(int,problem['moduli']))==[P**k for k in range(1,7)],'mixed moduli')
    check([[int(v) for v in row] for row in problem['coefficients']]
          ==[[pow(j,-k,P**k) for j in range(1,N+1)] for k in range(1,7)],
          'all original mixed coefficients')
    return [exact_case(case) for case in cases]

def alternate_representative(targets):
    modulus=P**6
    rows=[[pow(j,-k,modulus) for j in range(11,17)]+[targets[k-1]%modulus]
          for k in range(1,7)]
    for k in range(6):
        pivot=next(i for i in range(k,6) if rows[i][k]%P)
        rows[k],rows[pivot]=rows[pivot],rows[k]
        inverse=pow(rows[k][k],-1,modulus)
        rows[k]=[(v*inverse)%modulus for v in rows[k]]
        for i in range(6):
            if i!=k:
                multiplier=rows[i][k]
                rows[i]=[(a-multiplier*b)%modulus for a,b in zip(rows[i],rows[k])]
    representative=[0]*10+[row[-1] for row in rows]
    check(residues(representative)==targets,'alternate original mixed representative')
    return representative

def alternate_full_sphere(exact,common):
    """Post-custody independent review recursion, never called by module CLI."""
    radius=exact['radius_squared']
    norms=common['norms']
    check(all(d>radius for d in norms),'adjacent-integer completeness premise')
    rep=alternate_representative(exact['targets'])
    offset=[v*w for v,w in zip(rep,common['weights'])]
    centers=[dot(offset,star)/d for star,d in zip(common['stars'],norms)]
    check(sum(d*h*h for d,h in zip(norms,centers))==dot(offset,offset),
          'alternate affine GS identity')
    z=[0]*N
    trace=[]
    leaves=[]
    def descend(i,spent):
        if i<0:
            vector=[rep[j]+sum(z[s]*common['basis'][s][j] for s in range(N))
                    for j in range(N)]
            weighted=[w*v for w,v in zip(common['weights'],vector)]
            check(residues(vector)==exact['targets'] and dot(weighted,weighted)==spent,
                  'alternate full sphere leaf reconstruction')
            positive=sum(w*v for w,v in zip(common['weights'],vector) if v>0)
            negative=sum(-w*v for w,v in zip(common['weights'],vector) if v<0)
            leaves.append({'q0':[str(v) for v in vector],'norm':pair(spent),
                           'positive_total':str(positive),'negative_total':str(negative),
                           'both_signed_budgets_valid':positive<=exact['positive_budget']
                              and negative<=exact['negative_budget']})
            return
        center=centers[i]+sum(common['mu'][j][i]*z[j] for j in range(i+1,N))
        target=-center
        lower=target.numerator//target.denominator
        choices=[lower] if target.denominator==1 else [lower,lower+1]
        # Integers outside this list are at distance at least1, so their
        # coordinate contribution already exceeds D_i>R^2. Equality stays.
        for value in choices:
            norm=spent+norms[i]*(F(value)+center)**2
            admitted=norm<=radius
            trace.append({'index':i,'higher_z':[str(v) for v in z[i+1:]],
                          'center':pair(center),'all_possible_choices':[str(v) for v in choices],
                          'chosen':str(value),'prior_norm':pair(spent),'norm':pair(norm),
                          'admitted':admitted})
            if admitted:
                z[i]=value
                descend(i-1,norm)
    descend(N-1,F())
    return {'case_id':exact['id'],'alternate_q0':[str(v) for v in rep],
            'affine_centers':[pair(v) for v in centers],'trace':trace,'leaves':leaves,
            'choice_count':len(trace),'strict_prune_count':sum(not e['admitted'] for e in trace)}

if __name__=='__main__':
    print('PREPARED_INDEPENDENT_ARITHMETIC_ONLY; no case executed or accepted')
