"""Fixed-count ordered upper/lower shears. All entries except the stated diagnostics are exact."""
from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, gcd, lcm, prod
import json

I=(1,0,0,1)
U=(1,1,0,1)
V=(1,0,1,1)


def times(x,y,m=0):
    a,b,c,d=x
    e,f,g,h=y
    z=(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
    return tuple(t%m for t in z) if m else z


def inv(x):
    a,b,c,d=x
    return d,-b,-c,a


def up(t): return 1,t,0,1


def lo(t): return 1,0,t,1


A,B=times(U,V),times(V,U)
C=times(A,inv(B))
D=times(times(U,C),inv(U))


def reduce_word(s):
    out=[]
    for char in s:
        if out and out[-1] == char.swapcase():
            out.pop()
        else:
            out.append(char)
    return ''.join(out)


def inverse_word(s): return s[::-1].swapcase()


def word(s):
    matrix=I
    for char in s:
        g={'C':C,'D':D,'c':inv(C),'d':inv(D)}[char]
        matrix=times(matrix,g)
    return matrix


def schreier():
    a,b='dC','cdC'
    u12=reduce_word((a+inverse_word(b)+inverse_word(a)+b)*2)
    assert word(u12)==up(12)
    ab=[reduce_word(b+inverse_word(u12))]
    x,y=a,b
    for i in range(11):
        ab.append(x)
        x,y=reduce_word(x+inverse_word(y)),x
    generators={}
    for i in range(12):
        for key,s,move,w in [('U',U,1,u12 if i==11 else ''),('V',V,-1,ab[i])]:
            target=times(times(up(i),s),up(-((i+move)%12)))
            assert word(w)==target
            generators[f'{i},{key}']=w
    assert max(map(len,generators.values()))==11
    assert times(inv(D),C)==A
    assert times(times(U,A),inv(U))==C and times(times(U,B),inv(U))==A
    triples=[times(times(U,U),V),times(times(U,V),U),times(times(V,U),U)]
    assert [times(triples[i],inv(triples[i+1])) for i in range(2)]==[D,C]
    return generators


def group_size(m):
    primitives=sum(gcd(x,y,m)==1 for x,y in product(range(m),repeat=2))
    return m*primitives


def diameter(m):
    generators=[C,D,inv(C),inv(D)]
    depth={I:0}
    queue=deque([I])
    while queue:
        x=queue.popleft()
        for g in generators:
            y=times(g,x,m)
            if y not in depth:
                depth[y]=depth[x]+1
                queue.append(y)
    h=group_size(m)//gcd(m,12)
    assert len(depth)==h
    return {'m':m, 'commutator_order':h, 'diameter':max(depth.values()), 'diameter_upper':50*lcm(12,m)}


def tv(hist,h):
    t=sum(hist.values())
    return 1-sum((min(F(n,t),F(1,h)) for n in hist.values()),F(0))


def weighted_law(odds_numerators,odds_denominators,a,m):
    h=group_size(m)//gcd(m,12)
    weights=list(zip(odds_numerators,odds_denominators))
    dp={0:Counter({I:1})}
    for wa,wb in weights:
        nxt={}
        for count,entries in dp.items():
            for mask,g,weight in ((1,U,wa),(0,V,wb)):
                if count+mask>a:
                    continue
                dest=nxt.setdefault(count+mask,Counter())
                for x,v in entries.items():
                    dest[times(g,x,m)] += v*weight
        dp=nxt
    exact=Counter()
    for selected in combinations(range(len(weights)),a):
        selected=set(selected)
        mat,mass=I,1
        for j,(wa,wb) in enumerate(weights):
            mat=times(U if j in selected else V,mat,m)
            mass*=wa if j in selected else wb
        exact[mat]+=mass
    assert exact==dp[a]
    return exact,tv(exact,h)


def conjugate(t):
    return 1+t,1,-t*t,1-t


def pair_matrix(i,j,m):
    return times(conjugate(j),conjugate(i),m)


def group_by_gaps(a,b,m):
    """Append letters by the source time order; each chosen time tuple has unit mass."""
    counts=Counter()
    if a==1:
        for i in range(b+1):
            x=times(lo(b-i),times(U,lo(i),m),m)
            counts[x]+=1
    else:
        for i in range(b+1):
            left=times(U,lo(i),m)
            for j in range(i,b+1):
                x=times(lo(b-j),times(U,times(lo(j-i),left,m),m),m)
                counts[x]+=1
    return counts


def rare_cases():
    totals=[0,0]
    diagnostics=[]
    for m in range(2,46):
        h=group_size(m)//gcd(m,12)
        orbits=Counter(pair_matrix(i,j,m) for i,j in product(range(m),repeat=2))
        size=sum(m//gcd(d,m) for d in range(m))
        assert len(orbits)==size
        for (a,top,c,d),freq in orbits.items():
            assert freq==gcd(top,m)
        limiting=tv(orbits,h)
        if 12%m:
            assert limiting==1-F(size,h)
        if m<=14:
            for b in range(0,3*m+1):
                first=group_by_gaps(1,b,m)
                assert tv(first,h)==1-F(min(m,b+1),h)
                second=group_by_gaps(2,b,m)
                formula=Counter()
                for delta in range(m):
                    period=m//gcd(m,delta+2)
                    for start in range(period):
                        n=b-delta-start
                        if n<0:
                            continue
                        last=n//m
                        count=(last+1)*(n//period+1)-(m//period)*last*(last+1)//2
                        formula[times(lo(b),pair_matrix(start,start+delta,m),m)] += count
                support=sum(min(m//gcd(m,d+2),max(0,b-d+1)) for d in range(m))
                assert len(second)==support
                assert (len(second)==size)==(b>=2*m-2)
                assert formula==second
                assert sum(second.values())==comb(b+2,2)
                if b>=2*m-2:
                    assert min(second.values())==comb((b+2)//m,2)
                totals[0]+=1
        totals[1] += m*m
        if m in (2,3,4,5,6,7,8,12,16,25,30,45):
            diagnostics.append({'m':m,'two_A_eventual_support':size,'commutator_order':h,
                                'two_A_limiting_TV':str(limiting)})
    return {'joint_one_two_word_laws_checked':totals[0], 'residue_pairs_checked':totals[1], 'examples':diagnostics}


def finite_plateau():
    m=24
    h=group_size(m)//gcd(12,m)
    plateau=1-F(sum(m//gcd(j,m) for j in range(m)),h)
    outcomes=[]
    for total in (239,240,263,264):
        hist=group_by_gaps(2,total-2,m)
        actual=tv(hist,h)
        assert min(hist.values())==comb(total//m,2)
        assert (actual==plateau)==(total!=239)
        outcomes.append({"total_length":total,"minimum_preimage_count":min(hist.values()),"actual_TV":str(actual)})
    weights=Counter()
    for i,delta in product(range(2),repeat=2):
        w=(2 if (1+i)%2 else 1)*(2 if (2+i+delta)%2 else 1)
        weights[pair_matrix(i,i+delta,2)] += w
    assert sorted(weights.values())==[1,4,4] and tv(weights,3)==F(2,9)
    return {"m":m,"commutator_order":h,"plateau_value":str(plateau),"finite_examples":outcomes,
            "alternating_odds_mod_2_limiting_weights":sorted(weights.values())}


def main():
    degrees=schreier()
    sample=[]
    for m in (3,4,5,7):
        for n in range(3,12):
            aa=[1+i%5 for i in range(n)]
            bb=[2+(i*i)%3 for i in range(n)]
            a=(n+1)//2
            x,d=weighted_law(aa,bb,a,m)
            tilt=5
            y,_=weighted_law([k*tilt for k in aa],bb,a,m)
            assert y==Counter({k:v*tilt**a for k,v in x.items()})
            if n==11:sample.append({'m':m,'n':n,'a':a,'positive_matrices':len(x),'conditional_TV':str(d)})
    return {'schreier_words_for_positive_generators':degrees,'finite_diameters':[diameter(m) for m in range(2,22)],
            'time_varying_tilt_tests':36,'time_varying_examples':sample,'rare_shear_tests':rare_cases(), 'plateau_boundary':finite_plateau()}


if __name__=='__main__': print(json.dumps(main(),indent=2))
