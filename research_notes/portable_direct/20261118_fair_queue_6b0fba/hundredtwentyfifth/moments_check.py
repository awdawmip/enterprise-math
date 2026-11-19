"""One fixed guarded Markov transition. Python 3.9+, standard library only."""
import json
from fractions import Fraction as Q
from math import gcd, lcm


def apply(M, f):
    return [x*f[min(x+1, M)]+(M-x)*f[M-x] for x in range(M+1)]


def push(M, law):
    answer = [0]*(M+1)
    for x, mass in enumerate(law):
        answer[min(x+1, M)] += x*mass
        answer[M-x] += (M-x)*mass
    return answer


def rank(rows):
    if not rows:
        return 0
    mat = [v[:] for v in rows]
    pos = 0
    for col in range(len(mat[0])):
        rows_left = range(pos, len(mat))
        pivot = next((i for i in rows_left if mat[i][col]), None)
        if pivot is None:
            continue
        mat[pos], mat[pivot] = mat[pivot], mat[pos]
        p = mat[pos][col]
        for i in range(pos+1, len(mat)):
            if mat[i][col]:
                t = mat[i][col]
                v = [p*a-t*b for a,b in zip(mat[i], mat[pos])]
                g = gcd(*v)
                mat[i] = [a//g for a in v] if g else v
        pos += 1
    return pos


def determinant(matrix):
    a = [v[:] for v in matrix]
    sign = old = 1
    for i in range(len(a)-1):
        j = next((j for j in range(i,len(a)) if a[j][i]), None)
        if j is None:
            return 0
        if j != i:
            a[i],a[j] = a[j],a[i]
            sign = -sign
        pivot = a[i][i]
        for h in range(i+1,len(a)):
            for j in range(i+1,len(a)):
                num = a[h][j]*pivot-a[h][i]*a[i][j]
                assert num%old == 0
                a[h][j] = num//old
        old = pivot
    return sign*a[-1][-1]


def char_formula(M,t):
    result = t*(t-M)*(t-1 if M%2==0 else 1)
    for j in range((M-1)//2):
        result *= t*t-(M-3-4*j)*t-M
    return result


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def solve(a,rhs):
    augmented = [list(map(Q,row))+[Q(y)] for row,y in zip(a,rhs)]
    n=len(augmented)
    for i in range(n):
        pivot=next(j for j in range(i,n) if augmented[j][i])
        augmented[i], augmented[pivot] = augmented[pivot],augmented[i]
        augmented[i]=[u/augmented[i][i] for u in augmented[i]]
        for j in range(n):
            if j!=i:
                h=augmented[j][i]
                augmented[j]=[u-h*v for u,v in zip(augmented[j],augmented[i])]
    return [row[-1] for row in augmented]


def run():
    ranks = 0
    chars = 0
    histories = 0
    rows_by_M = {}
    for M in range(2,21):
        f0 = [1]*(M+1); f1 = list(range(M+1)); f2=[x*x for x in f1]
        mean_rows=[]; both=[f0]; rank_list=[]
        for t in range(M+2):
            both.extend((f1,f2))
            mean_rows.append(f1)
            r=rank(both)
            assert r==min(M+1,t+3)
            assert rank(mean_rows)==min(M+1,t+1)
            assert rank([f0]+mean_rows)==min(M+1,t+2)
            rank_list.append(r)
            f1,f2=apply(M,f1),apply(M,f2)
            ranks+=1
        if M in (2,4,7,12,20):
            rows_by_M[M]=rank_list[:M]
        n=M+1
        p=[push(M,[int(x==i) for x in range(n)]) for i in range(n)]
        for t in range(-2,M+1):
            direct=determinant([[int(i==j)*t-p[i][j] for j in range(n)] for i in range(n)])
            assert direct==char_formula(M,t)
            chars+=1
        h=[x*x-(2*M+1)*x for x in range(n)]
        assert apply(M,h)==[-M*h[i]-M*(M+1)*(M+i) for i in range(n)]
        initial=[(2*x*x+1)%(M+2) for x in range(n)]
        ft1=list(range(n));ft2=[x*x for x in range(n)]
        law=initial[:]; surv=[int(0<x<M) for x in range(n)]; old=[]
        for t in range(M+6):
            assert dot(ft1,initial)==sum(x*u for x,u in enumerate(law))
            assert dot(ft2,initial)==sum(x*x*u for x,u in enumerate(law))
            st=sum(surv[1:-1])
            if t>=2: assert st==(M-3)*old[-1]+M*old[-2]
            old.append(st)
            ft1,ft2=apply(M,ft1),apply(M,ft2)
            law,surv=push(M,law),push(M,surv)
            histories+=1

    M=4
    one=[1]*5; x=list(range(5)); square=[y*y for y in x]
    a=[one,x,square,apply(4,x),apply(4,apply(4,x))]
    assert determinant(a)!=0
    witnesses=[]
    for i in range(5):
        v=solve(a,[int(j==i) for j in range(5)])
        den=lcm(*(u.denominator for u in v))
        diff=[int(den*u) for u in v]
        plus=[max(u,0) for u in diff]; minus=[max(-u,0) for u in diff]
        assert all(dot(row,plus)-dot(row,minus)==(den if i==j else 0) for j,row in enumerate(a))
        if i: assert sum(plus)==sum(minus)>0
        witnesses.append(dict(index=i,positive=plus,negative=minus,
                              unscaled_integer_row_difference=den))
    return {"M_tested":[2,20],"time_ranks_checked":ranks,"three_ranks_per_time":
            ["mass_mean_second","mean_alone","mass_and_mean"],"selected_triple_rank_curves":rows_by_M,
            "independent_characteristic_polynomial_evaluations":chars,
            "exact_forward_transcripts_and_interior_survival_steps":histories,
            "M4_first_full_time":2,"M4_rows_one_x_x2_Px_P2x":a,
            "M4_integer_determinant":determinant(a),"M4_deletion_witnesses":witnesses}


if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
