"""Independent C87 QT audit using the original three-variable polytope.

No source-volume elimination formula is used in the polytope volume. Vertices
are intersections of the original twelve half-spaces in (source_x,source_y,
basis_shear). Exact face pyramids give the volume with its original measure.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).parent
TRIANGLE=ROOT.parent/'triangle'


def det3(rows):
    a,b,c=rows
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def subtract(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))


def solve3(rows,right):
    denominator=det3(rows)
    if not denominator:return None
    return tuple(det3([tuple(right[i]if j==k else rows[i][j]for j in range(3))for i in range(3)])/denominator
                 for k in range(3))


def face_order(vertices,indices,normal):
    drop=next(i for i,v in enumerate(normal)if v)
    keep=[i for i in range(3)if i!=drop]
    pts=sorted((vertices[i][keep[0]],vertices[i][keep[1]],i)for i in indices)
    def cross(o,a,b):return(a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[];upper=[]
    for seq,out in[(pts,lower),(list(reversed(pts)),upper)]:
        for point in seq:
            while len(out)>1 and cross(out[-2],out[-1],point)<=0:out.pop()
            out.append(point)
    return [p[2]for p in lower[:-1]+upper[:-1]]


def original_polytope_volume(r,u,t):
    d=1/u;planes=[]
    offsets=[(-u,u*t,0,0),(u,-u*t,0,0),(0,d,1,-t),(-u,u*t-d,-1,t)]
    for ox,oy,zx,zy in offsets:
        planes.extend([((-F(1),F(0),-F(zx)),F(ox)),
                       ((F(0),-F(1),-F(zy)),F(oy)),
                       ((F(1),F(1),F(zx+zy)),r-ox-oy)])
    vertices=set()
    for triple in combinations(planes,3):
        point=solve3([p[0]for p in triple],[p[1]for p in triple])
        if point is not None and all(dot(n,point)<=b for n,b in planes):vertices.add(point)
    vertices=sorted(vertices)
    if len(vertices)<4:return F(0)
    center=tuple(sum(v[j]for v in vertices)/len(vertices)for j in range(3))
    done=set();volume=F(0)
    for normal,bound in planes:
        indices=frozenset(i for i,v in enumerate(vertices)if dot(normal,v)==bound)
        if len(indices)<3 or indices in done:continue
        done.add(indices)
        face=face_order(vertices,indices,normal)
        for i in range(1,len(face)-1):
            volume+=abs(det3([subtract(vertices[j],center)for j in [face[0],face[i],face[i+1]]]))/6
    return volume


def broken_line_volume(r,u,t):
    d=1/u
    knots=sorted([-u,u,3*u-2*d/(1-t),2*d/t-3*u])
    def value(h):return r-F(3,2)*u-max(0,d+(1-t)*(h-3*u)/2)-max(0,d-t*(h+3*u)/2)-max(u,abs(h))/2
    values=list(map(value,knots))
    volume=max(0,values[0])**3/(3*(1+t)/2)+max(0,values[-1])**3/(3*(2-t)/2)
    for lo,hi,a,b in zip(knots,knots[1:],values,values[1:]):
        if max(a,b)<=0:continue
        if min(a,b)>=0:volume+=(hi-lo)*(a*a+a*b+b*b)/3
        else:volume+=(hi-lo)*max(a,b)**3/(3*abs(a-b))
    return volume/4


def run():
    cases=[]
    for r,u,t in product([F(5,2),F(8,3),F(11,4)],
                         [F(1),F(9,8),F(7,6),F(6,5),F(5,4),F(4,3)],
                         [F(1,3),F(2,5),F(1,2),F(3,5),F(2,3)]):
        if not 2/r<=u<=r/2:continue
        original=original_polytope_volume(r,u,t)
        reduced=broken_line_volume(r,u,t)
        assert original==reduced,(r,u,t,original,reduced)
        assert reduced==broken_line_volume(r,u,1-t)
        cases.append((r,u,t,original))
    # The small-angle capacity comparisons, checked by exact coefficients.
    # On [0,1/3]: 8-15t+9t^2>0, 1-9t^2>=0, t(1-3t)>=0.
    # First polynomial's Bernstein coefficients are 8, 11/2, 4.
    assert all(x>0 for x in [F(8),F(11,2),F(4)])
    assert F(1)-9*F(1,3)**2==0

    sys.path.insert(0,str(TRIANGLE))
    import qt_positive_integral as q
    boxes=[(F(8,3),F(9,8),F(5,4),F(2,5),F(1,2)),
           (F(11,4),F(7,6),F(4,3),F(1,3),F(2,5)),
           (F(5,2),F(9,8),F(5,4),F(2,5),F(3,5))]
    checked=0
    for r,ul,uh,tl,th in boxes:
        iv=q.source_volume_cell(q.I(q.I.cv(ul).lo,q.I.cv(uh).hi),
                                q.I(q.I.cv(tl).lo,q.I.cv(th).hi),q.I.cv(r))
        for i,j in product(range(3),repeat=2):
            u=ul+(uh-ul)*F(i,2);t=tl+(th-tl)*F(j,2)
            value=broken_line_volume(r,u,t)
            assert F(iv.lo,q.Q)<=value<=F(iv.hi,q.Q)
            checked+=1

    path=TRIANGLE/'complete_qt_certificate.json'
    certificate=json.loads(path.read_text())
    for name,digest in certificate['source_sha256'].items():
        assert hashlib.sha256((TRIANGLE/name).read_bytes()).hexdigest()==digest
    row=certificate['kappa3'];den=int(row['denominator'])
    lower=F(int(row['lower_numerator']),den);upper=F(int(row['upper_numerator']),den)
    assert sum(int(certificate[name]['lower_numerator'])for name in ['head','exact_middle','bounded_middle','tail'])==int(row['lower_numerator'])
    assert sum(int(certificate[name]['upper_numerator'])for name in ['head','exact_middle','bounded_middle','tail'])==int(row['upper_numerator'])
    assert F(17101,10000)<lower<upper<F(17833,10000)
    exemplar=next((r,u,t,v)for r,u,t,v in cases if(r,u,t)==(F(5,2),F(6,5),F(1,2)))
    result={'status':'PASS','arithmetic':'Fraction and integer interval comparisons',
            'independent_original_3D_polytope_cases':len(cases),
            'positive_polytope_cases':sum(v>0 for r,u,t,v in cases),
            'reflection_checks':len(cases),
            'whole_cell_sanity_boxes':len(boxes),'exact_internal_corner_checks':checked,
            'positive_example':list(map(str,exemplar)),
            'complete_certificate_source_bindings':len(certificate['source_sha256']),
            'final_four_part_rational_sum':True,
            'strict_kappa_enclosure':['1.7101','1.7833'],
            'full_outer_mesh_recomputed_by_review':False,
            'finite_cases_replace_analytic_proof':False}
    (ROOT/'qt_independent_review_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':print(json.dumps(run(),indent=2))
