"""Exact six-moment ternary cap, with positive and negative controls for pivot recovery."""
from hashlib import sha256
import json
from math import factorial, prod
from pathlib import Path
from subprocess import check_output, run
from tempfile import TemporaryDirectory

BUDGET = 2331
PRIMES = (19, 17, 13, 11, 7)
ORDERS = range(1, 7)


def valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def column(d, p):
    # Called only for v_p(d)=1 (or d=27*u for p=3 after removing 27).
    u = d // p**valuation(d,p)
    return [prod(pow(u,-1,m) - k*p for k in range(j)) % m
            for j,m in zip(ORDERS,moduli(p))]


def moduli(p):
    return [p**(j+valuation(factorial(j),p)) for j in ORDERS]


def invoke(program, header, mods, atoms, vectors, queries=()):
    rows = [header, mods, *([d,*v] for d,v in zip(atoms,vectors)), *queries]
    data = ''.join(' '.join(map(str,row))+'\n' for row in rows)
    return [list(map(int,row.split())) for row in
            check_output([program],input=data,text=True).splitlines()]


def count_lists(atoms, B):
    ways = [1]+[0]*B
    for d in atoms:
        for n in range(d-1,B+1):
            ways[n] += ways[n-d+1]
    return sum(ways)


def cross_prime(program, p, omitted, den, queries):
    """Queries (id, budget_left, budget_right, target residue vector), with left-right=target."""
    den = list(den)
    mods = moduli(p)
    vectors = [column(d,p) for d in den]
    offsets = [list(v) for _,_,_,v in queries]
    for t in range(omitted):
        row = 5-t
        # Pivot must be a unit in its coordinate of largest remaining modulus.
        pivot = next(a for a in range(t,len(den)) if vectors[a][row] % p)
        den[t],den[pivot] = den[pivot],den[t]
        vectors[t],vectors[pivot] = vectors[pivot],vectors[t]
        lead = vectors[t][:row]
        inv = pow(vectors[t][row],-1,mods[row])
        for v in vectors+offsets:
            c = v[row]*inv % mods[row]
            for j,w in enumerate(lead):
                v[j] = (v[j]-c*w) % mods[j]
            v[row] = c
    indices = [*range(omitted),*sorted(range(omitted,len(den)),key=den.__getitem__)]
    atoms = [den[i] for i in indices]
    vectors = [vectors[i] for i in indices]
    assert prod(mods[:6-omitted]) <= 2**64 and 2*max(mods) < 2**32
    bound = max(max(r,s) for _,r,s,_ in queries)
    # The DFS also carries a byte digit counter for the separate top-layer mode.
    assert bound//(atoms[omitted]-1) < 256
    prepared = [(i,r,s,*z) for (i,r,s,_),z in zip(queries,offsets)]
    output = invoke(program,[1,len(atoms),bound,omitted,len(queries)],mods,atoms,vectors,prepared)
    [total],*answers = output
    assert count_lists(atoms[omitted:],bound) == total
    assert [i for i,_ in answers] == [i for i,*_ in queries]
    return dict(pivots=atoms[:omitted],budget=bound,tail_multisets=total), dict(answers)


def smoke_test(program):
    # Oracle uses direct raw signatures and both budgets independently of the quotient search.
    p = 7
    den = [7,14,21,28,35,42,56,63]
    mods = moduli(p)
    vectors = [column(d,p) for d in den]
    levels = []
    def walk(i,c,v):
        levels.append((c,v))
        for t in range(i,len(den)):
            money=c+den[t]-1
            if money>57:
                break
            walk(t,money,tuple((a+b)%m for a,b,m in zip(v,vectors[t],mods)))
    walk(0,0,(0,)*6)
    queries = []
    wanted = {}
    for r,s in [(17,46),(40,23),(51,57)]:
        differences = {tuple((a-b)%m for a,b,m in zip(x,y,mods))
                       for c,x in levels if c<=r for e,y in levels if e<=s}
        samples = sorted(differences)
        for v in samples[::max(1,len(samples)//36)]:
            for delta in [v,((v[0]+1)%p,*v[1:])]:
                i=len(queries)
                queries.append((i,r,s,delta))
                wanted[i]=int(delta in differences)
    for omitted in [2,3]:
        _,answers=cross_prime(program,p,omitted,den,queries)
        assert answers==wanted
    return dict(queries_per_pivot_choice=len(queries),yes=sum(wanted.values()),
                no=len(wanted)-sum(wanted.values()),pivot_choices=[2,3])


def main():
    multiple = 2**5*3**3*5*7*11*13*17*19
    den = [d for d in range(2,BUDGET+2) if multiple%d==0]
    top = [d for d in den if d%27==0]
    low = [d for d in den if d%27!=0]
    mods = moduli(3)
    assert prod(mods)<2**64 and BUDGET//(min(top)-1)<256
    with TemporaryDirectory() as workspace:
        program=Path(workspace)/'ternary'
        run(['c++','-std=c++17','-O3',str(Path(__file__).with_name('ternary_solver.cpp')),
             '-o',str(program)],check=True)
        controls = smoke_test(program)
        head,*middle,last=invoke(program,[0,len(top),BUDGET,0,0],mods,top,
                                 [column(d,3) for d in top])
        n,distinct,repeated=head
        raw,npairs=last
        assert n==count_lists(top,BUDGET) and npairs==len(middle)
        cases=[]
        for row in middle:
            r,s,*digits=row
            a,b=digits[:len(top)],digits[len(top):]
            assert len(a)==len(b)==len(top) and not any(x*y for x,y in zip(a,b))
            assert BUDGET-r==sum(x*(d-1) for x,d in zip(a,top))
            assert BUDGET-s==sum(x*(d-1) for x,d in zip(b,top))
            cases.append((r,s,dict((d,x) for d,x in zip(top,a) if x),
                               dict((d,x) for d,x in zip(top,b) if x)))
        alive=set(range(npairs))
        stages=[]
        for p in PRIMES:
            qmods=moduli(p)
            queries=[]
            for i in sorted(alive):
                r,s,a,b=cases[i]
                offset=[0]*6
                for d in a.keys() | b.keys():
                    if d%p:continue
                    for j,x in enumerate(column(d,p)):
                        offset[j]=(offset[j]+(b.get(d,0)-a.get(d,0))*x)%qmods[j]
                if any(offset):
                    queries.append((i,r,s,offset))
            helpers=[d for d in low if d%p==0]
            data,answers=cross_prime(program,p,3 if p==7 else 2,helpers,queries)
            rejected=sorted(i for i,yes in answers.items() if not yes)
            alive.difference_update(rejected)
            stages.append(dict(p=p,available_atoms=len(helpers),queries=len(queries),
                               **data,rejected=rejected,remaining=len(alive)))
        assert not alive
    r,s,a,b=cases[139]
    example=dict(index=139,budgets=[r,s],left=a,right=b)
    digest=sha256(('\n'.join(' '.join(map(str,row)) for row in middle)+'\n').encode()).hexdigest()
    return dict(budget=BUDGET,allowed_multiple=multiple,allowed_count=len(den),top=top,
                ternary_moduli=mods,top_multisets=n,distinct_signatures=distinct,
                repeated_signatures=repeated,equal_pairs=raw,disjoint_pairs=npairs,
                disjoint_rows_sha256=digest,positive_negative_controls=controls,
                stages=stages,example=example)


if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
