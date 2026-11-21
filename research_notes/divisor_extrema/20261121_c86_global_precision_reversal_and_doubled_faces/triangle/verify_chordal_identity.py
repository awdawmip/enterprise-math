"""Exact finite checks for C86's universally proved Farey face identity."""
from itertools import combinations
from math import gcd
from fractions import Fraction as F
from pathlib import Path
import json,hashlib

def det(v,w):return v[0]*w[1]-v[1]*w[0]
def neg(v):return(-v[0],-v[1])
def add(v,w):return(v[0]+w[0],v[1]+w[1])
def counts(points,source):
    S={(x-source[0],y-source[1])for x,y in points
       if gcd(abs(x-source[0]),abs(y-source[1]))==1}
    V={min(v,neg(v))for v in S};D=len(V)
    E={frozenset((v,w))for v,w in combinations(V,2)if abs(det(v,w))==1}
    faces=[(v,w,z)for v,w,z in combinations(V,3)
           if all(frozenset((a,b))in E for a,b in [(v,w),(w,z),(z,v)])]
    assert int(D==0)==1-D+len(E)-len(faces)
    doubled={v for v in V if v in S and neg(v)in S}
    if len(doubled)>1:return False
    B=sum(abs(det(v,w))==1 for v,w in combinations(S,2))
    C=sum(det(v,w)==1 and neg(v)in S for v in S for w in S)
    T=sum(det(v,w)==1 and neg(add(v,w))in S for v in S for w in S)//3
    P=sum(abs(det(v,w))==1 and add(v,w)in S for v,w in combinations(S,2))
    QP=sum(det(v,w)==1 and neg(v)in S and add(v,w)in S for v in S for w in S)
    QT=sum(det(v,w)==1 and neg(v)in S and neg(add(v,w))in S for v in S for w in S)
    Qfaces=sum(any(v in doubled for v in face)for face in faces)
    assert B-C==len(E)
    assert QP+QT==Qfaces
    assert T+P==len(faces)+Qfaces
    assert int(D==0)==1-D+B-C-T-P+QP+QT
    return True

def run():
    all_cases=single_double=0
    for n in range(1,13):
        for d in range(1,n+1):
            if n%d:continue
            h=n//d
            for r in range(h):
                points=[(x,y)for x in range(max(d,r)+1)for y in range(h+1)
                        if 0<=x*h-r*y and x*h-r*y+d*y<=d*h]
                for source in points:
                    all_cases+=1;single_double+=counts(points,source)
    assert counts([(0,0)],(0,0))
    path=Path(__file__).with_name('chordal_lower_certificate.json')
    cert=json.loads(path.read_text());b=cert['kappa3'];den=int(b['denominator'])
    low,high=F(int(b['lower_numerator']),den),F(int(b['upper_numerator']),den)
    assert F(17088,10000)<low<high<F(979,500)
    for name,digest in cert['source_sha256'].items():
        assert hashlib.sha256(path.with_name(name).read_bytes()).hexdigest()==digest
    result={'status':'PASS','triangle_hull_twice_area_max':12,
            'exact_source_cases_general_farey_identity':all_cases+1,
            'exact_source_cases_at_most_one_doubled_direction':single_double+1,
            'strict_kappa_bounds':['17088/10000','979/500'],
            'finite_checks_are_universal_proof':False,
            'proof':'CHORDAL_CORRECTION.md',
            'integral_meshes_recomputed_by_this_verifier':False}
    path.with_name('chordal_identity_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
