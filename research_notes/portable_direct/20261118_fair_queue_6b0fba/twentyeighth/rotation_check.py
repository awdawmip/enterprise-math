"""Finite spectra by integer Krylov identities, raw signed frames, and sign-gauge posteriors."""
from array import array
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import json


AXES = tuple(range(6))
TRIPLES = tuple(combinations(AXES, 3))
EVEN = tuple(p for p in permutations(AXES) if
             sum(p[i] > p[j] for i,j in combinations(AXES,2)) % 2 == 0)
POSITION = {p:i for i,p in enumerate(EVEN)}
SEEDS = ((-8,-5,0,4,16,40),(-8,-6,-4,-3,0,5,6,10,24),
         (-8,-5,-4,-1,0,4,7,8,12,16),(-12,-9,-6,0,6,9,12))


def cycle(i,j,k):
    a=list(AXES)
    a[i],a[j],a[k]=j,k,i
    return tuple(a)


OPTIONS = [(cycle(i,x,y),(1<<i)|(1<<j)|(1<<k))
           for i,j,k in TRIPLES for x,y in ((j,k),(k,j))]
LEFT = [[POSITION[tuple(r[k] for k in p)] for p in EVEN] for r,_ in OPTIONS]


def linear_solution(columns, target):
    a = [[Fraction(c[i]) for c in columns]+[Fraction(y)] for i,y in enumerate(target)]
    n=len(columns)
    for j in range(n):
        pivot=next(i for i in range(j,len(a)) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        a[j]=[v/a[j][j] for v in a[j]]
        for i in range(len(a)):
            if i!=j and a[i][j]:
                a[i]=[v-a[i][j]*u for v,u in zip(a[i],a[j])]
    assert all(not any(row) for row in a[n:])
    result=[a[i][-1] for i in range(n)]
    assert all(x.denominator==1 and x>0 for x in result)
    return list(map(int,result))


def block(weight):
    """Verification uses guessed factors, without assuming any spectral multiplicity."""
    mask=(1<<weight)-1
    signs=[(-1)**(mask&T).bit_count() for _,T in OPTIONS]
    edges=list(zip(signs,LEFT))
    deltas=[[1]+[0]*359]
    factors=[[-x,1] for x in SEEDS[weight]]
    if weight==3:
        factors.append([-45,0,1])
    coeff=[1]
    for factor in factors:
        ans=[0]*(len(coeff)+len(factor)-1)
        for i,u in enumerate(coeff):
            for j,z in enumerate(factor):
                ans[i+j]+=u*z
        coeff=ans
    for _ in range(len(coeff)-1):
        v=deltas[-1]
        b=[0]*360
        for sg,perm in edges:
            for i,j in enumerate(perm):
                b[i]+=sg*v[j]
        deltas.append(b)
    assert all(sum(c*v[i] for c,v in zip(coeff,deltas))==0 for i in range(360))
    moments=[360*v[0] for v in deltas]
    cols=[[x**j for j in range(len(moments))] for x in SEEDS[weight]]
    if weight==3:
        cols.append([2*45**(j//2) if j%2==0 else 0 for j in range(len(moments))])
    mult=linear_solution(cols,moments)
    result={str(x):v for x,v in zip(SEEDS[weight],mult)}
    if weight==3:
        result.update({"+sqrt45":mult[-1],"-sqrt45":mult[-1]})
    assert sum(result.values())==360
    return result


def power_moment(label,k):
    if label.endswith("sqrt45"):
        assert k%2==0
        return 45**(k//2)
    return int(label)**k


def total_spectrum(blocks):
    total=Counter()
    for w in range(7):
        for label,mult in blocks[min(w,6-w)].items():
            if w>3:
                label=str(-int(label))
            total[label]+=comb(6,w)*mult
    for label,n in total.items():
        if not label.endswith("sqrt45"):
            assert total[str(-int(label))]==n
    assert sum(total.values())==23040
    return total


def raw_frames(total):
    identity=(1,2,3,4,5,6)
    moves=[tuple((1-2*((mask>>j)&1))*(r[j]+1) for j in AXES) for r,mask in OPTIONS]
    ids={identity:0}
    frames=[identity]; dist=[0]
    adj=array('H')
    for i,state in enumerate(frames):
        for g in moves:
            s=tuple((1 if x>0 else -1)*state[abs(x)-1] for x in g)
            j=ids.get(s)
            if j is None:
                j=len(frames); ids[s]=j; frames.append(s); dist.append(dist[i]+1)
            adj.append(j)
    assert len(frames)==23040
    balls=Counter(dist)
    assert [balls[i] for i in range(7)]==[1,40,1100,7390,10118,4090,301]
    par=[sum(x<0 for x in g)%2 for g in frames]
    F=[sum((1 if x>0 else -1) * (6*(abs(x)==i)-1) for i,x in enumerate(g,1))
       for g in frames]
    assert all(d%2==p for d,p in zip(dist,par))
    assert all(sum(F[j] for j in adj[40*i:40*i+40])==24*F[i] for i in range(len(frames)))
    constants=[Fraction(sum(abs(z) for p,z in zip(par,F) if p==b),2*11520) for b in (0,1)]
    word=[1]+[0]*(len(frames)-1); rows=[]
    for k in range(11):
        assert all((x>0)==(d<=k and d%2==k%2) for x,d in zip(word,dist))
        ret=sum(n*power_moment(label,k) for label,n in total.items())//23040 if k%2==0 else 0
        assert ret==word[0] and sum(word)==40**k
        pow_sum=sum(n*power_moment(label,2*k) for label,n in total.items())
        assert 23040*sum(x*x for x in word)==pow_sum
        rows.append({"n":k,"support":sum(x>0 for x in word),"identity_words":word[0]})
        word=[sum(word[j] for j in adj[40*i:40*i+40]) for i in range(len(frames))]
    return dict(shortest_length_counts=sorted(balls.items()),direct_words=rows,
                leading_TV_even_odd=list(map(str,constants)))


def shared_gauges():
    """Enumerate posterior sets by filtering the 32 sign frames modulo central reversal."""
    # Fix axis 5 positive to choose one representative per antipodal pair.
    gauges=tuple(range(32))
    masks=[]
    for triple in TRIPLES:
        i,j,k=triple
        patterns=Counter()
        for a in gauges:
            pattern=tuple(((a>>u)^(a>>v))&1 for u,v in ((i,j),(j,k),(k,i)))
            patterns[pattern] |= 1<<a
        assert len(patterns)==4
        masks.extend(patterns.values())
    all_g=(1<<32)-1
    seen={all_g}; todo=deque(seen)
    while todo:
        current=todo.popleft()
        for mask in masks:
            cand=current&mask
            if cand and cand not in seen:
                seen.add(cand); todo.append(cand)
    counts=Counter(s.bit_count() for s in seen)
    # One-step posterior laws are pairwise different; orientations have the same twist counts.
    laws={tuple(Fraction((s&m).bit_count(),s.bit_count()) for m in masks) for s in seen}
    assert len(laws)==len(seen)==489
    seen_moves = Counter()
    gauges_at_once = []
    for a in gauges:
        moves = [tuple((1-2*((T>>i)&1))*(1-2*(((a>>i)^(a>>r[i]))&1))*(r[i]+1)
                       for i in AXES) for r,T in OPTIONS]
        gauges_at_once.append(set(moves))
        seen_moves.update(moves)
    assert len(seen_moves)==160 and set(seen_moves.values())=={8}
    def inverse(g):
        h=[0]*6
        for i,axis in enumerate(g,1):
            h[abs(axis)-1]=i if axis>0 else -i
        return tuple(h)
    shared_return = Fraction(sum(inverse(g) in gs for gs in gauges_at_once for g in gs),
                             32*40**2)
    fresh_return = Fraction(sum(inverse(g) in seen_moves for g in seen_moves),160**2)
    assert shared_return==Fraction(1,40) and fresh_return==Fraction(1,160)
    counts_by_weight=[]
    for w in range(7):
        mask=(1<<w)-1
        effective=[sum((-1)**(mask&T&v).bit_count() for v in range(64)
                       if v&~T==0 and v.bit_count()%2==1)//4 for _,T in OPTIONS]
        # The denominator division is exact after summing the four twist characters.
        exact_weights=[1 if mask&T==0 else (-1 if mask&T==T else 0) for _,T in OPTIONS]
        assert effective==exact_weights
        counts_by_weight.append(sum(abs(z) for z in effective))
    assert counts_by_weight==[40,20,8,4,8,20,40]
    return {"four_twist_absolute_row_bounds_divided_by_four":counts_by_weight,
            "posterior_sizes_and_counts":sorted(counts.items()),
            "distinct_one_step_laws":len(laws), "unit_return_two_steps_shared":str(shared_return),
            "unit_return_two_steps_resampled":str(fresh_return)}


def main():
    blocks=[block(w) for w in range(4)]
    total=total_spectrum(blocks)
    print(json.dumps({"walsh_blocks":blocks,"full_spectrum":total,"frame_checks":raw_frames(total),
                      "sign_gauge_models":shared_gauges()},sort_keys=True,indent=2))


if __name__=="__main__":
    main()
