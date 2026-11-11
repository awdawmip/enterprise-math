"""Positive rational schedule mixtures and the two-preparation decoder."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import cache
from itertools import combinations
from math import comb, lcm
from pathlib import Path
import json
import sys


def responses(r,c,word,brc=None):
    tails=('557','575','755')
    updates=''.join('5'*m+'23' for m in word[:-1])+'5'*word[-1]
    rates=(Q(1,4),Q(1),Q(4))
    rows=[]
    raw_counts=0
    for initial in range(3):
        for_hist=brc is not None
        def forward(symbol,previous,stock):
            j='2357'.index(symbol)
            result=[brc.weight_histogram([]) if for_hist else Q(0) for _ in range(3)]
            for i,mass in enumerate(previous):
                empty=mass.is_zero if for_hist else mass==0
                if empty: continue
                total=stock[0]+stock[1]+rates[i]*stock[2]+stock[3]
                p=stock[j]*(rates[i] if j==2 else 1)/total
                transitions=[(0,Q(7,8)),(i,Q(1,8))] if symbol=='3' else [(min(2,i+1) if symbol=='2' else i,Q(1))]
                for dest,weight in transitions:
                    if for_hist:
                        new=brc.histogram_serial(mass,brc.weight_histogram([p*weight]))
                        result[dest]=brc.histogram_recoalesce(result[dest],new)
                    else:
                        result[dest]+=p*weight*mass
            stock[j]-=1
            return result
        if for_hist:
            masses=[brc.weight_histogram([1] if i==initial else []) for i in range(3)]
        else:
            masses=[Q(i==initial) for i in range(3)]
        stock=[r,r,c,1]
        for sym in updates: masses=forward(sym,masses,stock)
        assert stock==[0,0,2,1]
        tails_out=[]
        for tail in tails:
            now=list(masses);remaining=list(stock)
            for sym in tail: now=forward(sym,now,remaining)
            if for_hist:
                n=sum(h.count for h in now)
                assert n==2**r
                raw_counts+=n
                tails_out.append(sum(h.total_mass for h in now))
            else:
                tails_out.append(sum(now))
        states=[h.total_mass for h in masses] if for_hist else masses
        assert sum(states)==sum(tails_out)
        rows.append(states+tails_out)
    return rows,raw_counts


def solve(matrix,vector):
    """Exact nonsingular square linear system."""
    rows=[[*row,v] for row,v in zip(matrix,vector)]
    for i in range(len(rows)):
        j=next(j for j in range(i,len(rows)) if rows[j][i])
        rows[i],rows[j]=rows[j],rows[i]
        t=rows[i][i]
        rows[i]=[x/t for x in rows[i]]
        for j in range(len(rows)):
            if i!=j:
                t=rows[j][i]
                rows[j]=[x-t*y for x,y in zip(rows[j],rows[i])]
    return [row[-1] for row in rows]


def simplex_rows(matrix,lam):
    return [[(lam*x+y)/(lam+1) for x,y in zip(matrix[0],matrix[i])] for i in (2,1)]


def vector4(matrix):
    return [row[i] for row in simplex_rows(matrix,7) for i in (0,1)]


def determinant(matrix):
    """Bareiss algorithm with exact divisions over integers."""
    a=[row.copy() for row in matrix]
    prev=1
    sign=1
    for i in range(len(a)-1):
        j=next((j for j in range(i,len(a)) if a[j][i]),None)
        if j is None:return 0
        if j!=i:
            a[j],a[i]=a[i],a[j]
            sign=-sign
        p=a[i][i]
        for j in range(i+1,len(a)):
            for u in range(i+1,len(a)):
                n=p*a[j][u]-a[j][i]*a[i][u]
                assert n%prev==0
                a[j][u]=n//prev
        prev=p
    return sign*a[-1][-1]


def rho(r,c,m):
    k=2*r+1
    value=Q(1,4**m)
    for n in range(c-m,c+1): value*=Q(k+4*n,k+n)
    return value


def recover_slopes(endpoints):
    a,b=[row[3:] for row in endpoints]
    def H(t):
        quot=[(x*(1-t)+y*t)/x for x,y in zip(a,b)]
        return max(quot)/min(quot)
    hhalf,hfull=H(Q(1,2)),H(Q(1))
    low=(2*hhalf-hfull-1)/(hfull-hhalf)
    return hfull-1+hfull*low,low


def main(native):
    sys.path.insert(0,str(native.resolve()))
    from enterprise_math import brc_histogram as brc
    goal=(1,3,0,0,0)
    words=[(0,0,4,0,0),(0,1,2,1,0),(0,2,2,0,0),(0,3,0,1,0),(0,3,1,0,0)]
    def all_first_zero():
        for i in range(5):
            for j in range(5-i):
                yield (0,i,j,4-i-j,0)
    matrix=cache(lambda w:responses(4,6,w)[0])
    columns=[vector4(matrix(w))+[Q(1)] for w in words]
    target=vector4(matrix(goal))+[Q(1)]
    weights=solve(list(zip(*columns)),target)
    assert min(weights)>0 and sum(weights)==1
    mix=[[sum(p*matrix(w)[i][j] for p,w in zip(weights,words)) for j in range(6)] for i in range(3)]
    assert simplex_rows(mix,7)==simplex_rows(matrix(goal),7)
    diff=[x-y for x,y in zip(mix[0],matrix(goal)[0])]
    assert any(diff)
    assert all([x-y for x,y in zip(mix[i],matrix(goal)[i])]==[-7*v for v in diff] for i in (1,2))
    paths=list(all_first_zero())
    scaled=[]
    for w in paths:
        deltas=[v-t for v,t in zip(vector4(matrix(w)),target[:4])]
        denominator=lcm(*(v.denominator for v in deltas))
        scaled.append([int(v*denominator) for v in deltas])
    # Nonzero for every four proves no affine/positive representation on <=4.
    determinants=[determinant([scaled[i] for i in inds]) for inds in combinations(range(len(scaled)),4)]
    assert len(determinants)==comb(15,4) and all(determinants)
    branches=0
    for w in [goal]+words:
        raw,n=responses(4,6,w,brc)
        assert raw==matrix(w)
        branches+=n
    def check_lines(surface,expected):
        g7=recover_slopes(simplex_rows(surface,7))
        g1=recover_slopes(simplex_rows(surface,1))
        observed=[]
        for lam,extremes in ((7,g7),(1,g1)):
            a,b=simplex_rows(surface,lam)
            slopes=[b[j]/a[j]-1 for j in (3,4,5)]
            assert (max(slopes),min(slopes))==extremes
            ranks=tuple(tuple(j for j,g in enumerate(slopes) if g==extreme) for extreme in extremes)
            observed.append(ranks)
        assert observed[0]==observed[1]
        assert all(1+6/(7/a-1/b)==expected for a,b in zip(g1,g7))
        assert all(surface[1][j]/surface[2][j]==expected for j in (3,4,5))
        return observed[0]

    goal_ranks=check_lines(matrix(goal),rho(4,6,1))
    mix_ranks=check_lines(mix,rho(4,6,0))
    assert recover_slopes(simplex_rows(matrix(goal),1))!=recover_slopes(simplex_rows(mix,1))
    assert recover_slopes(simplex_rows(matrix(goal),7))==recover_slopes(simplex_rows(mix,7))

    def schedules(r,n):
        if r==0:
            yield (n,)
        else:
            for i in range(n+1):
                for sub in schedules(r-1,n-i):
                    yield (i,)+sub

    all_tests=0
    for r in range(1,5):
        for c in range(2,9):
            for word in schedules(r,c-2):
                check_lines(responses(r,c,word)[0],rho(r,c,word[0]))
                all_tests+=1
    tests=[]
    for r in range(1,5):
        for c in range(2,10):
            for m in range(c-1):
                w=(m,)+(0,)*(r-1)+(c-2-m,)
                surface=responses(r,c,w)[0]
                tests.append(check_lines(surface,rho(r,c,m)))
    return dict(cut=[4,6],deterministic=goal,randomized=[dict(gaps=w,weight=str(p)) for w,p in zip(words,weights)],
                raw_common_endpoints=[[str(v) for v in row] for row in simplex_rows(mix,7)],
                off_line_difference_at_pure_zero=[str(x) for x in diff],positive_branches_with_multiplicity=branches,
                pure_state_and_tail_checks=6*3*6,minimum_support=5,lower_support_determinants=len(determinants),
                two_preparation_decodes=len(tests),all_schedule_alignment_and_decodes=all_tests,
                example_extreme_tail_indices=dict(pure=goal_ranks,mixture=mix_ranks),first_gap_rhos=[str(rho(4,6,m)) for m in (0,1)])


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--native-root',type=Path,required=True)
    print(json.dumps(main(p.parse_args().native_root),indent=2))
