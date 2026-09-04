"""Deterministic exact checks. Run without Python -O. No floats in proofs."""
from __future__ import annotations
import argparse, hashlib, json, math, random, time
from dataclasses import replace
from fractions import Fraction as Q
from functools import reduce
from itertools import combinations, permutations, product
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
import atlas_brc as a
import generic_atoms as ga
import factor_atoms as old

if not __debug__:
    raise RuntimeError('verification assertions require Python without -O')


def require_refusal(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('invalid input was not refused')


def brute(n):
    bounds = [min(n[e] for e in star) for star in a.STARS]
    ks = [k for k in product(*(range(u+1) for u in bounds))
          if all(k[u]+k[v]<=n[j] for j,(u,v) in enumerate(a.EDGES))]
    m = max(map(sum,ks))
    return m,tuple(k for k in ks if sum(k)==m)


def rational_poly(p):
    return tuple(Q(int(q.p),int(q.q)) for q in reversed(p.all_coeffs()))


def compare_old(factors,cert):
    fs = [rational_poly(p) for p in factors]
    prev = old.compile_atoms(fs)
    assert old.verify_certificate(fs,prev)
    assert tuple((z.profile,z.polynomial) for z in prev.atoms) == tuple(
        (z.profile,rational_poly(z.polynomial)) for z in cert.atoms)
    return prev


def run():
    start=time.monotonic(); out={}; rng=random.Random(0xB6C42A1)
    old.select_backend('pinned')
    count=rotcount=0
    for n in product(range(4),repeat=6):
        m,ks=brute(n); f=a.compile_fibre(n)
        assert f.optimum==m and set(f.enumerate())==set(ks)
        if f.exceptional is not None:
            b=f.exceptional
            assert set(ks)=={tuple(b[j]+int(i==j) for j in range(4)) for i in range(4)}
        for k in ks:
            assert a.decode(a.residual(n,k),k)==n
            assert all(min(a.residual(n,k)[e] for e in st)==0 for st in a.STARS)
        for g in a.GROUP:
            fg=a.compile_fibre(a.rotate_axes(n,g))
            assert fg.optimum==m
            # Check membership rather than duplicate the whole enumeration.
            for k in ks:
                assert fg.contains(a.rotate_slices(k,g))
            rotcount+=1
        count+=1
    out['exhaustive_capacity_inputs_0_to_3']=count
    out['capacity_rotation_checks']=rotcount
    for _ in range(350):
        n=tuple(rng.randrange(10) for _ in range(6))
        assert a.compile_fibre(n).optimum==brute(n)[0]
    out['additional_bruteforce_capacity_inputs']=350

    # Local min-zero in every chart is necessary but not enough for optimum.
    trap=(1,1,1,1,1,2); greedy=(1,0,0,0)
    assert all(min(a.residual(trap,greedy)[e] for e in st)==0 for st in a.STARS)
    assert sum(greedy)==1 and a.compile_fibre(trap).optimum==2
    assert a.compile_fibre(trap).enumerate()==((0,0,1,1),)
    out['local_min_zero_greedy_trap_certified']=True

    # Independent exact LP active-basis audit, including very large integers.
    rows=[[int(v in e) for v in range(4)] for e in a.EDGES]+[
          [-int(i==v) for v in range(4)] for i in range(4)]
    bases=[]
    for ix in combinations(range(10),4):
        mat=s.Matrix([rows[i] for i in ix])
        if mat.det()!=0: bases.append((ix,mat.inv()))
    assert len(bases)==141
    large=0
    for _ in range(25):
        n=tuple(rng.randrange(10**60,10**61) for _ in range(6))
        rhs=(*n,0,0,0,0); vertices=[]
        for ix,inv in bases:
            k=tuple(inv*s.Matrix([rhs[i] for i in ix]))
            if min(k)>=0 and all(k[u]+k[v]<=n[j] for j,(u,v) in enumerate(a.EDGES)):
                vertices.append(k)
        lp=max(map(sum,vertices)); assert lp==min(a.seven_bounds(n))
        m=a.compile_fibre(n).optimum
        witnessed=False
        for k in vertices:
            if sum(k)!=lp:continue
            lows=tuple(int(s.floor(t)) for t in k)
            for bits in product((0,1),repeat=4):
                kk=tuple(v+b for v,b in zip(lows,bits))
                if sum(kk)==m and all(kk[u]+kk[v]<=n[j] for j,(u,v) in enumerate(a.EDGES)):
                    witnessed=True
        assert witnessed
        large+=1
    # Guaranteed exceptional big family, no enumeration needed.
    b=tuple(10**120+i*7 for i in range(4))
    n=tuple(b[u]+b[v]+1 for u,v in a.EDGES)
    assert a.compile_fibre(n).optimum==sum(b)+1
    out['independent_lp_bases']=len(bases);out['large_integer_lp_checks']=large
    out['exceptional_121_digit_case']=True

    stars={frozenset(t) for t in a.STARS}
    automorphisms={p for p in permutations(range(6))
                   if {frozenset(p[e] for e in st) for st in a.STARS}==stars}
    assert automorphisms=={a.edge_action(g) for g in a.GROUP}
    # Independent 3x3 proper signed-permutation FCC carrier realization.
    L=((1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1))
    aligned=[L[int(label[1:])-1] for label in a.LINE_ORDER]
    signed_actions=set()
    for perm in permutations(range(3)):
        invs=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in product((-1,1),repeat=3):
            if (-1)**invs*math.prod(signs)!=1:continue
            action=[]
            for v in aligned:
                image=tuple(signs[i]*v[perm[i]] for i in range(3))
                action.append(next(j for j,w in enumerate(aligned) if image==w or image==tuple(-t for t in w)))
            signed_actions.add(tuple(action))
    assert signed_actions==automorphisms and len(automorphisms)==24
    out['atlas_automorphisms']=24;out['proper_fcc_carrier_rotations']=24
    one=a.compile_fibre((1,)*6); assert len(one.enumerate())==4
    assert not any(all(a.rotate_slices(k,g)==k for g in a.GROUP) for k in one.enumerate())
    out['symmetric_optimal_fibre_size']=4;out['equivariant_single_choice_exists']=False

    B=s.Matrix([[int(v in e) for v in range(4)] for e in a.EDGES])
    D=smith_normal_form(B,domain=s.ZZ)
    assert [abs(D[i,i]) for i in range(4)]==[1,1,1,2]
    assert B*s.ones(4,1)==2*s.ones(6,1)
    assert B.gauss_jordan_solve(s.ones(6,1))[0]==s.ones(4,1)/2
    out['lossy_laurent_quotient_smith_diagonal']=[1,1,1,2]

    def key():
        return a.BranchKey(Q(rng.randrange(1,8),rng.randrange(1,8)),
                           tuple(rng.randrange(3) for _ in range(6)),rng.choice(a.GROUP),rng.randrange(5))
    def hist():
        return a.add({key():rng.randrange(1,4)},{key():rng.randrange(1,4)})
    for _ in range(250):
        x,y,z=hist(),hist(),hist();g=rng.choice(a.GROUP)
        assert a.multiply(a.multiply(x,y),z)==a.multiply(x,a.multiply(y,z))
        assert a.multiply(x,a.add(y,z))==a.add(a.multiply(x,y),a.multiply(x,z))
        assert a.relabel(a.multiply(x,y),g)==a.multiply(a.relabel(x,g),a.relabel(y,g))
        for m in (0,1,2,3):
            assert a.moment(a.multiply(x,y),m)==a.moment(x,m)*a.moment(y,m)
    out['histogram_semiring_and_equivariance_cases']=250
    for _ in range(500):
        u,v,w=key(),key(),key(); g=rng.choice(a.GROUP)
        carry=a.compression_carry(u,v)
        assert carry>=0
        assert carry==a.compression_carry(u.relabel(g),v.relabel(g))
        assert carry+a.compression_carry(u.then(v),w)==(
            a.compression_carry(v,w)+a.compression_carry(u,v.then(w)))
    N=10**100
    u=a.BranchKey(axes=(N,0,0,0,0,0))
    v=a.BranchKey(axes=(0,N,N,0,0,0))
    assert a.compile_fibre(u.axes).optimum==a.compile_fibre(v.axes).optimum==0
    assert a.compression_carry(u,v)==N
    assert a.compression_carry(a.BranchKey(),v)==0
    out['framed_carry_nonnegative_covariance_cocycle_cases']=500
    out['unbounded_carry_101_digit_case']=True
    out['scalar_compression_quotient_future_unsafe']=True
    out['moment_multiplication_checks']=1000
    trace=(3,4,0,0,0,0)
    for g in a.GROUP:
        assert a.sector_norm_squared(a.rotate_axes(trace,g),g[0])==25
    require_refusal(lambda:a.sector_norm_squared((1,1,1,0,0,0),0))
    out['sector_345_covariance_checks']=24

    # Rotation cycling the three edges at slice A; step and turn do not commute.
    turn=(0,2,3,1);frames=(a.IDENTITY,turn,a.compose(turn,turn))
    step=a.BranchKey(Q(1,10),(1,0,0,0,0,0),a.IDENTITY,1)
    rotate=a.BranchKey(Q(1,10),a.ZERO,turn,1)
    assert step.then(rotate)!=rotate.then(step)
    assert rotate.then(rotate).then(rotate).frame==a.IDENTITY
    assert rotate.then(rotate).then(rotate).length==3
    H={a.BranchKey():1}
    for n in range(1,7):
        H=a.multiply(H,{step:1,rotate:1})
        raw={}
        for word in product((step,rotate),repeat=n):
            k=reduce(lambda b,c:b.then(c),word,a.BranchKey())
            raw[k]=raw.get(k,0)+1
        assert H==raw and sum(H.values())==2**n
    out['ordered_word_replay_lengths']=6

    X=s.symbols('Xab Xac Xad Xbc Xbd Xcd');z,y,t=s.symbols('z y t')
    T,index=a.frame_lift(1,[(0,0,step,1),(0,0,rotate,1)],X,z,frames=frames)
    det=s.expand((s.eye(3)-T).det())
    expected=s.expand(s.prod(1-z*X[j]/10 for j in a.STARS[0])-(z/10)**3)
    assert det==expected
    out['cyclic_frame_determinant']=str(det)
    out['cyclic_frame_determinant_exact']=True
    # Coefficientwise transfer agreement, before algebraic root selection.
    for n in range(1,6):
        P=(T.subs(z,1)**n).applyfunc(s.expand)
        h={a.BranchKey():1}
        for _ in range(n):h=a.multiply(h,{step:1,rotate:1})
        for g in frames:
            expr=sum(s.Rational(k.weight.numerator,k.weight.denominator)*c*
                     s.prod(xx**e for xx,e in zip(X,k.axes)) for k,c in h.items() if k.frame==g)
            assert s.expand(P[index[0,a.IDENTITY],index[0,g]]-expr)==0
    out['frame_transfer_prefix_checks']=15
    full,ix=a.frame_lift(1,[(0,0,step,1),(0,0,rotate,1)],X,z)
    for r in a.GROUP:
        subs={X[i]:X[j] for i,j in enumerate(a.edge_action(r))}
        for g in a.GROUP:
            for h in a.GROUP:
                assert full[ix[0,a.compose(r,g)],ix[0,a.compose(r,h)]]==full[ix[0,g],ix[0,h]].subs(subs,simultaneous=True)
    out['full_24_frame_covariance_entries']=24**3

    # Automatically close the predecessor's Q(t) compiler frontier.
    factors=((y-t)*(y-1),(y-t)*(y+1))
    cert=ga.compile_atoms(factors,y,(t,));assert ga.verify_certificate(factors,cert)
    guard=ga.regular_guard(cert,(-2,2))
    assert s.expand(guard.polynomial.as_expr()-(t*t-1)*(t*t-4))==0
    specs=root_queries=0
    for value in (s.Rational(j,3) for j in range(-12,13)):
        if guard.at({t:value})==0:
            require_refusal(lambda:ga.specialize(cert,guard,{t:value}));continue
        cc=ga.specialize(cert,guard,{t:value})
        fs=tuple(s.Poly(f.subs(t,value),y,domain=s.QQ) for f in factors)
        fresh=ga.compile_atoms(fs,y)
        assert ga.signature(cc)==ga.signature(fresh)
        previous=compare_old(fs,cc);counts=old.atom_counts(previous,Q(-2),Q(2))
        for w in product(range(3),repeat=2):
            safety,N,M=old.observe(previous,counts,w)
            realroots={value:s.Integer(w[0]+w[1]),s.Integer(1):s.Integer(w[0]),s.Integer(-1):s.Integer(w[1])}
            expectedN=sum(int(bool(e>0)) for r,e in realroots.items() if -2<r<2)
            expectedM=sum(int(e) for r,e in realroots.items() if -2<r<2)
            assert (safety,N,M)==(expectedN==0,expectedN,expectedM)
            root_queries+=1
        specs+=1
    out['automatic_predecessor_guard']='(t^2-1)(t^2-4)'
    out['predecessor_regular_specializations']=specs;out['inherited_root_observer_queries']=root_queries

    # Rational coefficients, scalars, squarefree layers, and special guards.
    rational_fs=((t+1)/(t-2)*(y-1/(t-3))**2*(y+2),
                 (y-1/(t-3))*(y+2)**3)
    rc=ga.compile_atoms(rational_fs,y,(t,));assert ga.verify_certificate(rational_fs,rc)
    rg=ga.regular_guard(rc,(-4,4))
    rcount=0
    for value in map(s.Rational,range(-6,9)):
        if rg.at({t:value})==0:continue
        cc=ga.specialize(rc,rg,{t:value})
        fs=tuple(s.Poly(f.subs(t,value),y,domain=s.QQ) for f in rational_fs)
        compare_old(fs,cc);rcount+=1
    for value in (-1,2,3):assert rg.at({t:s.Rational(value)})==0
    out['rational_coefficient_regular_specializations']=rcount

    # All six parameters: four overlapping triad atoms plus a shared atom.
    q=tuple(s.prod(X[e] for e in star) for star in a.STARS)
    af=tuple((y-qq)*(y-2) for qq in q)
    ac=ga.compile_atoms(af,y,X);assert ga.verify_certificate(af,ac) and len(ac.atoms)==5
    ag=ga.regular_guard(ac)  # sparse conjunction, never expand the big product
    for g in a.GROUP:
        sub={X[i]:X[j] for i,j in enumerate(a.edge_action(g))}
        tr=ga.transform_parameters(ac,sub)
        fr=ga.compile_atoms(tuple(f.subs(sub,simultaneous=True) for f in af),y,X)
        assert ga.signature(tr)==ga.signature(fr)
    for values in ((2,3,5,7,11,13),(3,5,7,11,13,17),(5,7,11,13,17,19)):
        sub=dict(zip(X,map(s.Integer,values)))
        cc=ga.specialize(ac,ag,sub)
        fs=tuple(s.Poly(f.subs(sub,simultaneous=True),y,domain=s.QQ) for f in af)
        compare_old(fs,cc)
    onevalues={x:s.Integer(1) for x in X}
    assert ag.at(onevalues)==0
    require_refusal(lambda:ga.specialize(ac,ag,onevalues))
    collided=ga.compile_atoms(tuple(f.subs(onevalues) for f in af),y)
    assert len(collided.atoms)==1 and collided.atoms[0].profile==(1,1,1,1)
    assert collided.atoms[0].polynomial==s.Poly((y-1)*(y-2),y,domain=s.QQ)
    out['six_parameter_atoms']=5;out['six_parameter_covariance_checks']=24
    out['six_parameter_regular_specializations']=3
    out['six_parameter_sparse_guard_factors']=len(ag.factors)
    out['coarse_all_one_collision_refused']=True

    # Algebraic contact with the rotation determinant.
    df=((1-z/5)*det,(1-z/7)*det)
    dc=ga.compile_atoms(df,z,X[:3]);assert ga.verify_certificate(df,dc) and len(dc.atoms)==3
    dg=ga.regular_guard(dc)
    dcount=0
    for values in ((1,2,3),(2,3,5),(3,4,7),(1,1,1)):
        sub=dict(zip(X[:3],map(s.Integer,values)))
        if dg.at(sub)==0:continue
        cc=ga.specialize(dc,dg,sub)
        fs=tuple(s.Poly(f.subs(sub,simultaneous=True),z,domain=s.QQ) for f in df)
        compare_old(fs,cc);dcount+=1
    out['cyclic_determinant_regular_specializations']=dcount

    # Typed refusals and deliberately corrupted certificate rejection.
    refuses=[lambda:a.compile_fibre((1,)*5),lambda:a.compile_fibre((True,)*6),
      lambda:a.residual((0,)*6,(1,0,0,0)),lambda:a.BranchKey(0),lambda:a.BranchKey(0.5),
      lambda:a.BranchKey(frame=(0,0,2,3)),lambda:a.moment({},-1),
      lambda:ga.compile_atoms((0,),y,(t,)),lambda:ga.compile_atoms((y+0.2,),y,(t,)),
      lambda:ga.regular_guard(ga.compile_atoms((y-1,),y,(t,)),(1,2)),
      lambda:ga.specialize(cert,guard,{t:0.3}),lambda:ga.transform_parameters(cert,{t:s.Integer(1)})]
    for fn in refuses:require_refusal(fn)
    corrupted=replace(cert,atoms=(replace(cert.atoms[0],profile=(0,0)),*cert.atoms[1:]))
    assert not ga.verify_certificate(factors,corrupted)
    out['invalid_input_refusals']=len(refuses);out['corrupted_certificate_rejected']=True
    out['status']='PASS_EXACT_REFERENCE_CHECKS_NOT_REPOSITORY_CI_OR_LEAN'
    out['sympy_version']=s.__version__;out['elapsed_seconds']=round(time.monotonic()-start,3)
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='verification.json');args=parser.parse_args()
    result=run()
    text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    Path(args.output).write_text(text,encoding='utf-8');print(text)
