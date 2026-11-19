"""Exact finite shuffle checks. Python 3.9+, standard library."""
import json
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial, lcm, prod


def paired_triples(m):
    # Direct enumeration of full linear words in A^m,B,C,D,E.
    # The four entries are positions of the four private letters.
    size = m+4
    table = Counter()
    for pos in permutations(range(size),4):
        before_a = [u-sum(v<u for v in pos) for u in pos]
        k = before_a[1]-before_a[0]+m*(pos[0]>pos[1])
        j = before_a[3]-before_a[2]+m*(pos[2]>pos[3])
        table[k,j] += 1
    total = sum(table.values())
    assert total==factorial(size)//factorial(m)
    conditional_total = total//(m+1)
    denominator = (m+2)*(m+3)
    eigenvalue = F(2,denominator)
    excess = F()
    for i in range(m+1):
        assert sum(table[i,j] for j in range(m+1)) == conditional_total
        for j in range(m+1):
            numerator=m+4+(j==i)+(j==m-i)
            assert table[i,j]*denominator==numerator*conditional_total
            excess+=abs(F(table[i,j],total)-F(1,(m+1)**2))
    tv=excess/2
    assert tv==eigenvalue*(1-F(2,m+1)+F(int(m%2==0),(m+1)**2))
    return dict(m=m,full_words=total,positive_nonconstant_eigenvalue=str(eigenvalue) if m>=2 else None,
                exact_total_variation=str(tv)), table


def independent_functions(max_m):
    counts = []
    for m in range(1,max_m+1):
        denominator = (m+2)*(m+3)
        balanced = 0
        interior = 0
        for mask in range(1<<(m+1)):
            if mask in (0,(1<<(m+1))-1):
                continue
            bins = [j for j in range(m+1) if mask>>j&1]
            ok = all((m+1)*sum(m+4+(j==i)+(j==m-i) for j in bins)
                     ==len(bins)*denominator for i in range(m+1))
            if ok:
                balanced += 1
                interior += len(bins)
        expected=2**((m+1)//2) if m%2 else 0
        assert balanced==expected
        assert interior==balanced*(m+1)//2
        counts.append([m,balanced])
    return counts


def triangle(*indices):
    edges=Counter()
    for a,b in zip(indices,indices[1:]+indices[:1]):
        edges[min(a,b),max(a,b)] += 1 if a<b else -1
    return edges


def moments(stock,left,right):
    # Append the last letter. Coefficients of (X+dx)^u(Y+dy)^v give exact moments.
    n=len(stock)
    scale=lcm(*(2*stock[a]*stock[b] for a,b in left.keys() | right.keys()))
    def directed(edges):
        matrix=[[0]*n for _ in range(n)]
        for (a,b),value in edges.items():
            val=scale*value//(2*stock[a]*stock[b])
            matrix[a][b],matrix[b][a] = val,-val
        return matrix
    a,b=map(directed,(left,right))
    moment_keys=list(product(range(3),repeat=2))
    zero=(0,)*n
    states={zero:{key:int(key==(0,0)) for key in moment_keys}}
    for s in product(*(range(k+1) for k in stock)):
        if s==zero:
            continue
        totals={key:0 for key in moment_keys}
        for last,cnt in enumerate(s):
            if not cnt:
                continue
            prev=list(s)
            prev[last]-=1
            old=states[tuple(prev)]
            x=sum(prev[i]*a[i][last] for i in range(n))
            y=sum(prev[i]*b[i][last] for i in range(n))
            for u,v in moment_keys:
                totals[u,v]+=sum(comb(u,i)*comb(v,j)*x**(u-i)*y**(v-j)*old[i,j]
                                  for i in range(u+1) for j in range(v+1))
        states[s]=totals
    sums=states[tuple(stock)]
    count=sums[0,0]
    assert count==factorial(sum(stock))//prod(factorial(j) for j in stock)
    def mean(i,j):
        return F(sums[i,j],count*scale**(i+j))
    assert mean(1,0)==mean(0,1)==mean(1,1)==0
    return count,mean(2,2)-mean(2,0)*mean(0,2)


def incident(stock,edges):
    return sum(F(c**2,stock[b]) for (a,b),c in edges.items() if a==0)


def general_examples():
    result=[]
    first=triangle(0,1,2)
    other=triangle(0,4,5)
    form=triangle(0,1,2,3)
    for u in form:
        form[u]*=2
    form.update(triangle(0,2,3))
    for name,left,right,stock in [
        ('shared_singleton',form,other,[1,2,1,2,2,1]),
        ('equal_two',first,other,[2]*6),
        ('two_private_sizes',first,other,[4,1,3,2,1,2]),
        ('four_axis_and_three_axis',form,other,[3,2,1,2,2,1]),
        ('all_singleton_private',first,other,[5,1,1,2,1,1])
    ]:
        count,observed=moments(stock,left,right)
        m=stock[0]
        theory=F(m-1,360*m**3)*incident(stock,left)*incident(stock,right)
        assert theory==observed
        result.append(dict(case=name,stock=stock,word_count=count,unscaled_square_covariance=str(theory)))
    return result


def main():
    checks=[]
    example=None
    for m in range(1,19):
        row,table=paired_triples(m)
        checks.append(row)
        if m==4:
            example=[[table[i,j] for j in range(m+1)] for i in range(m+1)]
    print(json.dumps(dict(triples=checks,m4_full_word_joint_counts=example,
                          nonconstant_binary_events_independent_of_other_count=independent_functions(10),
                          general_single_intersection=general_examples()),indent=2))


if __name__=="__main__":
    main()
