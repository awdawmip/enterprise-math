"""Deterministic exact cross-checks; not Lean, independent review, or source CI."""
from __future__ import annotations
import hashlib, json, sys, time, random
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as F
import sympy as s
from vendor import atlas_brc as old
import six_axis as a
from ports import schur_ports,same_labeled_ports,FormalPortSignature

COUNTS={}
def bump(name,n=1): COUNTS[name]=COUNTS.get(name,0)+n

def require(condition,message='failed check'):
    if not condition: raise AssertionError(message)

def rejects(fn,*args,**kwargs):
    try: fn(*args,**kwargs)
    except (ValueError,TypeError): bump('negative_input_checks'); return
    raise AssertionError('invalid input accepted: '+repr(fn))

def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))

def matvec(A,v): return tuple(sum(x*y for x,y in zip(row,v)) for row in A)

def test_group():
    actual=set(old.edge_action(g) for g in old.GROUP)
    observed=set()
    stars={frozenset(st) for st in old.STARS}
    for p in permutations(range(6)):
        if {frozenset(p[e] for e in st) for st in old.STARS}==stars: observed.add(p)
        bump('six_label_permutations_examined')
    require(actual==observed and len(actual)==24)
    mats={g:a.rotation_matrix(g) for g in old.GROUP}
    independent=set()
    for p in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            M=tuple(tuple(signs[i] if j==p[i] else 0 for j in range(3)) for i in range(3))
            if s.Matrix(M).det()==1: independent.add(M)
    require(set(mats.values())==independent and len(independent)==24)
    require(len({a.flag_ray(v,e) for v,e in a.FLAGS})==12)
    for g in old.GROUP:
        require(s.Matrix(mats[g]).det()==1)
        for h in old.GROUP:
            require(matmul(mats[g],mats[h])==mats[old.compose(g,h)])
            bump('carrier_group_compositions')
        for v,e in a.FLAGS:
            require(matvec(mats[g],a.flag_ray(v,e))==a.flag_ray(*a.rotate_flag(v,e,g)))
            bump('flag_equivariance_checks')
    for v in range(4):
        rays=[a.flag_ray(v,e) for e in old.STARS[v]]
        require(tuple(sum(ray[i] for ray in rays) for i in range(3))==(0,0,0))
        require(all(sum(x*x for x in ray)==2 for ray in rays))
        require(all(sum(x*y for x,y in zip(r,t))==-1 for r,t in combinations(rays,2)))
    for e,(u,v) in enumerate(old.EDGES):
        require(a.flag_ray(u,e)==tuple(-x for x in a.flag_ray(v,e)))
    con=a.ChartSignConnection()
    for eps in product((-1,1),repeat=4):
        gauge=con.gauge(eps)
        require(gauge.signs!=(1,)*6)
        for u,v,w in combinations(range(4),3):
            require(gauge.walk_product((u,v,w,u))==-1)
            bump('gauge_triangle_checks')
    vertices,edges=con.double_cover()
    cube={state:tuple(state[1]*x for x in a.TETRA[state[0]]) for state in vertices}
    require(len(set(cube.values()))==8 and len(edges)==12)
    for x,y in combinations(vertices,2):
        require((frozenset((x,y)) in edges)==(sum(i!=j for i,j in zip(cube[x],cube[y]))==1))
        bump('double_cover_pair_checks')


def test_glue():
    independent={}
    for n in product(range(3),repeat=6):
        if min(n)==0: independent[old_charts(n)]=n
    for n in product(range(4),repeat=6):
        enc=a.CountAtlas.encode(n)
        require(enc.decode()==n)
        require(enc.charts==old_charts(n))
        bump('six_count_roundtrips')
        for omitted in range(4):
            require(a.reconstruct({v:enc.charts[v] for v in range(4) if v!=omitted})
                    ==tuple(x-min(n) for x in n))
            bump('three_chart_reconstructions')
        for g in old.GROUP:
            require(enc.rotate(g)==a.CountAtlas.encode(old.rotate_axes(n,g)))
            bump('count_atlas_rotation_checks')
    local=[x for x in product(range(2),repeat=3) if min(x)==0]
    accepted=0
    for charts in product(local,repeat=4):
        possible=charts in independent
        try: n=a.reconstruct(dict(enumerate(charts)))
        except ValueError:
            require(not possible)
        else:
            require(possible and n==independent[charts])
            accepted+=1
        bump('all_binary_local_chart_packets')
    COUNTS['compatible_binary_local_chart_packets']=accepted
    n=(0,2,4,3,1,5)
    require(a.local_charts(n)==a.local_charts(tuple(x+12345678901234567890 for x in n)))
    require(a.CountAtlas.encode(n)!=a.CountAtlas.encode(tuple(x+1 for x in n)))
    require(old_charts((0,0,0,0,0,1))[:2]==old_charts((0,)*6)[:2])
    # Root-normalization is an algorithmic choice; all 4 roots yield same result.
    bad=((0,0,0),(0,0,0),(0,1,0),(0,0,0))
    rejects(a.reconstruct,dict(enumerate(bad)))


def old_charts(n):
    # Independent direct formula; does not call new encoder.
    return tuple(tuple(n[e]-min(n[f] for f in st) for e in st) for st in old.STARS)


def test_composition():
    rng=random.Random(60120905)
    for _ in range(600):
        n,m,k=[tuple(rng.randrange(10**30) for _ in range(6)) for j in range(3)]
        g,h,t=[rng.choice(old.GROUP) for j in range(3)]
        x,y,z=[old.BranchKey(F(j+1,j+2),v,q,j+1) for j,(v,q) in enumerate(((n,g),(m,h),(k,t)))]
        require(x.then(y).then(z)==x.then(y.then(z)))
        require(a.CountAtlas.encode(n).add_in_frame(a.CountAtlas.encode(m),g).decode()==x.then(y).axes)
        r,u,v=[a.normalize_counts(p)[0] for p in (n,m,k)]
        ru=a.normalize_counts(tuple(i+j for i,j in zip(r,old.rotate_axes(u,g))))[0]
        uv=a.normalize_counts(tuple(i+j for i,j in zip(u,old.rotate_axes(v,h))))[0]
        require(a.depth_carry(r,u,g)+a.depth_carry(ru,v,old.compose(g,h))
                ==a.depth_carry(u,v,h)+a.depth_carry(r,uv,g))
        require(old.compression_carry(x,y)>=0)
        # Cross-check existing K-carry separately; it is NOT depth carry.
        require(old.compression_carry(x,y)+old.compression_carry(x.then(y),z)
                ==old.compression_carry(y,z)+old.compression_carry(x,y.then(z)))
        bump('large_integer_composition_and_two_cocycle_cases')
    N=10**100
    require(a.depth_carry((N,0,0,0,0,0),(0,N,N,N,N,N))==N)
    for _ in range(120):
        keys=[old.BranchKey(F(rng.randrange(1,6),7),tuple(rng.randrange(5) for _ in range(6)),
                            rng.choice(old.GROUP),rng.randrange(4)) for j in range(3)]
        arrows=[a.TypedArrow(str(i),str(i+1),key) for i,key in enumerate(keys)]
        A,B,C=({arrows[0]:2},{arrows[1]:3},{arrows[2]:5})
        require(a.arrow_product(a.arrow_product(A,B),C)==a.arrow_product(A,a.arrow_product(B,C)))
        require(sum(a.arrow_product(a.arrow_product(A,B),C).values())==30)
        require(a.arrow_product(C,A)=={})
        bump('typed_brc_category_cases')
    rejects(a.TypedArrow('a','b',keys[0]).then,a.TypedArrow('c','d',keys[1]))
    fibre=old.compile_fibre((1,)*6)
    require(fibre.optimum==1 and set(fibre.enumerate())==set(product((0,1),repeat=4)) &
            {tuple(int(i==j) for i in range(4)) for j in range(4)})
    require(old.compile_fibre((1,1,1,1,1,2)).optimum==2)
    COUNTS['pinned_optimal_fibre_examples']=2


def test_metric_and_native_contract():
    c=s.Symbol('c')
    P=s.zeros(6)
    for i,j in ((0,5),(1,4),(2,3)): P[i,j]=P[j,i]=1
    Q=s.eye(6)+c*P
    lam=s.Symbol('lambda')
    require(s.expand(Q.charpoly(lam).as_expr()-(lam-c-1)**3*(lam+c-1)**3)==0)
    orbits={}
    for i in range(6):
        for j in range(i,6):
            orbit=frozenset(tuple(sorted((old.edge_action(g)[i],old.edge_action(g)[j]))) for g in old.GROUP)
            orbits[orbit]=1
    require(sorted(map(len,orbits))==[3,6,12])
    for g in old.GROUP:
        for n in product(range(2),repeat=6):
            require(a.quadratic_extension(n,F(1,3))==a.quadratic_extension(old.rotate_axes(n,g),F(1,3)))
            bump('quadratic_covariance_checks')
    for v,star in enumerate(old.STARS):
        for i,j in combinations(star,2):
            n=[0]*6;n[i]=3;n[j]=4
            for coeff in (F(-1,2),F(0),F(2,3)):
                require(a.quadratic_extension(n,coeff)==old.sector_norm_squared(n,v)==25)
                bump('local_metric_restrictions')
    n=(1,0,0,0,0,1)
    require(a.quadratic_extension(n,F(0))==2 and a.quadratic_extension(n,F(1,2))==3)
    # Small declared derived model: 0 plus six terminal unit-operation states.
    acts={g:(0,)+tuple(j+1 for j in old.edge_action(g)) for g in old.GROUP}
    transitions={(0,e,e+1) for e in range(6)}
    COUNTS.update(a.verify_finite_axis_lift(7,transitions,acts))
    rejects(a.verify_finite_axis_lift,7,transitions-{(0,0,1)},acts)
    corrupted=dict(acts);corrupted[old.GROUP[1]]=tuple(range(7))
    rejects(a.verify_finite_axis_lift,7,transitions,corrupted)
    branches={f'{layer}:{e}':(0,e,e+1,F(1,layer+1)) for layer in range(2) for e in range(6)}
    bact={g:tuple(layer*6+old.edge_action(g)[e] for layer in range(2) for e in range(6)) for g in old.GROUP}
    stats=a.verify_finite_brc_lift(7,branches,acts,bact)
    COUNTS['branch_group_checks']=stats['branch_group_checks']
    COUNTS['branch_covariance_checks']=stats['branch_covariance_checks']
    # A thirteenth copy leaves support unchanged, but breaks branch covariance.
    more=dict(branches);more['unpaired']=(0,0,1,F(1))
    a.verify_finite_axis_lift(7,[record[:3] for record in more.values()],acts)
    fake={g:bact[g]+(12,) for g in old.GROUP}
    rejects(a.verify_finite_brc_lift,7,more,acts,fake)
    bump('support_vs_branch_multiplicity_counterexample')


def test_invalid():
    for n in ((True,0,0,0,0,0),(0,)*5,(-1,0,0,0,0,0),(F(1,2),0,0,0,0,0)):
        rejects(a.CountAtlas.encode,n)
    rejects(a.CountAtlas,((0,0,0),)*4,True)
    rejects(a.CountAtlas,((1,1,1),)*4,0)
    rejects(a.reconstruct,{0:(0,0,0),1:(0,0,0)})
    rejects(a.ChartSignConnection,(0,)*6)
    rejects(a.flag_ray,0,5)
    rejects(a.rotation_matrix,(0,1,2,True))
    rejects(a.depth_carry,(1,)*6,(0,)*6)
    rejects(a.quadratic_extension,(0,)*6,1)
    rejects(a.quadratic_extension,(0,)*6,-1)
    rejects(a.quadratic_extension,(0,)*6,0.5)


def main():
    started=time.time()
    data=Path(__file__).with_name('vendor').joinpath('atlas_brc.py').read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(blob=='881a34d1919da64a85e6e06902ec3f23654a147e','pinned source bytes drifted')
    for fn in (test_group,test_glue,test_composition,test_metric_and_native_contract,test_invalid):
        fn();print(fn.__name__,'PASS',flush=True)
    result={'status':'PASS_EXACT_SELF_CHECKS_NOT_LEAN_OR_INDEPENDENT_REVIEW',
            'counts':COUNTS,'vendor_git_blob':blob,'python':sys.version.split()[0],
            'sympy':s.__version__,'seconds':round(time.time()-started,3)}
    Path(__file__).with_name('verification_core.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
