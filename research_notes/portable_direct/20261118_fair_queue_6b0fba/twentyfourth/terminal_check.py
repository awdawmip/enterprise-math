"""Exact terminal masks for rational-integer branch tables, independent CRT regressions."""
import json
from collections import defaultdict
from itertools import product
from math import gcd, lcm, prod


def primary_agreement(n,left,right):
    g=gcd(n,*(a-b for a,b in zip(left,right,strict=True)))
    return n//gcd(n,pow(n//g,n.bit_length(),n))


def atoms(n,table,y):
    parts={():n}
    for h,row in enumerate(table):
        agrees=primary_agreement(n,row,y)
        refined={}
        for labels,value in parts.items():
            inside=gcd(value,agrees)
            outside=value//inside
            assert gcd(inside,outside)==1
            if inside>1: refined[labels+(h,)]=inside
            if outside>1: refined[labels]=outside
        parts=refined
    assert prod(parts.values())==n
    return parts


def idempotent_on(n,d):
    """1 mod the unitary divisor d, 0 on its complementary divisor."""
    if d==1: return 0
    c=n//d
    return c*pow(c,-1,d)%n


def choose_formal_representative(n,parts,h):
    if () in parts:
        return None
    selected=[1]*h
    for options,d in parts.items():
        selected[options[0]]*=d
    return [idempotent_on(n,d) for d in selected]


def code_output(n,table,idems):
    return tuple(sum(e*row[k] for row,e in zip(table,idems))%n for k in range(len(table[0])))


def primary_factors(n):
    """Independent finite verification only; unused by the mask construction."""
    parts=[]
    for d in range(2,n+1):
        q=1
        while n%d==0:
            n//=d
            q*=d
        if q>1: parts.append(q)
        if n==1: break
    return parts


def masks(n,table,updates):
    s=len(table)
    base=[[primary_agreement(n,x,y) for y in table] for x in table]
    history=[base]
    while True:
        values=history[-1]
        step=[[gcd(base[i][j],*(values[f[i]][f[j]] for f in updates))
               for j in range(s)] for i in range(s)]
        if step==values: return history
        history.append(step)
        assert len(history)-1<=max(0,s-2)


def brute_automaton(n,table,updates,hist):
    s=len(table)
    for q in primary_factors(n):
        classes=[tuple(x%q for x in row) for row in table]
        seen=set()
        for level,mat in enumerate(hist):
            relation=tuple(tuple(a==b for b in classes) for a in classes)
            assert all((mat[i][j]%q==0)==relation[i][j] for i,j in product(range(s),repeat=2))
            seen.add(relation)
            codes={value:index for index,value in enumerate(dict.fromkeys(classes))}
            classes=[(codes[x],*(codes[classes[f[i]]] for f in updates))
                     for i,x in enumerate(classes)]
        final=tuple(tuple(a==b for b in classes) for a in classes)
        assert final in seen


def perfect_powers():
    modulus_count=0
    tested=0
    for n in range(2,151):
        idem=[b for b in range(n) if b*b%n==b]
        for t in range(1,9):
            for exps in ((2,),(3,),(2,3),(4,6),(6,10,15)):
                g=gcd(*exps)
                gaps=[(t+1)**e-t**e for e in exps]
                assert gcd(*gaps)==(t+1)**g-t**g
                rows=[tuple(t**e for e in exps),tuple((t+1)**e for e in exps)]
                fibers=defaultdict(list)
                for b in idem:
                    y=tuple((base+gap*b)%n for base,gap in zip(rows[0],gaps))
                    fibers[y].append(b)
                    if exps==(2,3):
                        assert (4*(y[1]-t**3)-3*(2*t+1)*(y[0]-t**2))%n==b
                    tested+=1
                hidden=primary_agreement(n,*rows)
                assert all(len(v)==2**len(primary_factors(hidden)) for v in fibers.values())
                for y,choices in fibers.items():
                    partition=atoms(n,rows,y)
                    rep=choose_formal_representative(n,partition,2)
                    assert rep[1] in choices and code_output(n,rows,rep)==y
                modulus_count+=1
    return {"modulus_t_exponent_sets":modulus_count,"exact_idempotent_inputs":tested}


def table_checks():
    regressions=0
    for n in range(2,81):
        factors=primary_factors(n)
        for rows,actions in [
            ([(4,),(4,),(4,),(9,)],[(1,2,3,3)]),
            ([(0,0),(3,6),(6,1),(2,3)],[(1,0,3,2),(0,2,1,3)]),
            ([(-1,1,0),(0,1,-1)],[(1,0)])]:
            sizes=defaultdict(int)
            for assignment in product(range(len(rows)),repeat=len(factors)):
                onehot=[sum(idempotent_on(n,q) for q,b in zip(factors,assignment) if b==h)%n
                        for h in range(len(rows))]
                sizes[code_output(n,rows,onehot)]+=1
            for y,size in sizes.items():
                partition=atoms(n,rows,y)
                assert () not in partition
                predicted=prod(len(options)**len(primary_factors(q)) for options,q in partition.items())
                assert predicted==size
                rep=choose_formal_representative(n,partition,len(rows))
                assert code_output(n,rows,rep)==y
            if len(rows[0])==1:
                for t in range(n):
                    assert ((t,) in sizes)==(() not in atoms(n,rows,(t,)))
            hist=masks(n,rows,actions)
            brute_automaton(n,rows,actions,hist)
            regressions+=1
    return regressions


def square_product(x,y,n):
    a,b,c,d=x
    e,f,g,h=y
    return ((a*e+b*g)%n,(a*f+b*h)%n,(c*e+d*g)%n,(c*f+d*h)%n)


def lift_idempotent(n,m,residues):
    t=tuple(a%m for a in residues)
    precision=1
    while precision<(n-1).bit_length():
        ts=square_product(t,t,n)
        tc=square_product(ts,t,n)
        t=tuple((3*a-2*b)%n for a,b in zip(ts,tc))
        precision*=2
    assert square_product(t,t,n)==t
    return t


def rank_mod(x,p):
    a,b,c,d=x
    if (a*d-b*c)%p:
        return 2
    return int(any(z%p for z in x))


def matrix_checks():
    checked=0
    matrix_inputs=0
    for n in range(2,17):
        primes=[p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,p))]
        ids=[x for x in product(range(n),repeat=4) if square_product(x,x,n)==x]
        for g in range(1,n+1):
            m=n//gcd(n,g)
            strong=weak=True
            seen={}
            for x in ids:
                y=tuple(g*a%n for a in x)
                ranks=tuple(rank_mod(x,p) for p in primes)
                if y in seen:
                    old,old_ranks=seen[y]
                    strong=strong and old==x
                    weak=weak and old_ranks==ranks
                else:
                    seen[y]=(x,ranks)
                if all(m%p==0 for p in primes):
                    divisor=gcd(n,g)
                    inverse=pow(g//divisor,-1,m)
                    reduced=tuple((a//divisor)*inverse % m for a in y)
                    assert all(a%m==b for a,b in zip(x,reduced))
                    rep=lift_idempotent(n,m,reduced)
                    assert tuple(rank_mod(rep,p) for p in primes)==ranks
                matrix_inputs+=1
            assert strong==(gcd(n,g)==1)
            assert weak==all(m%p==0 for p in primes)
            checked+=1
    assert lift_idempotent(12,6,(3,0,0,0))==(9,0,0,0)
    return {"2x2_modulus_gap_pairs":checked,"2x2_terminal_inputs":matrix_inputs,
            "N12_mod6_representative":[3,0,0,0],"idempotent_lift":[9,0,0,0]}


def details():
    a=atoms(35,[(4,1),(9,-4)],(4,1))
    b=atoms(45,[(1,),(4,)],(31,))
    assert a=={(0,1):5,(0,):7} and b=={(0,):5,(1,):9}
    assert choose_formal_representative(45,b,2)[1]==10
    table=[(4,),(4,),(4,),(9,)]
    hist=masks(35,table,[(1,2,3,3)])
    assert len(hist)==3 and [m[0][1] for m in hist]==[35,35,5]
    sharp=[]
    for s in range(2,15):
        rows=[(0,)]*(s-1)+[(1,)]
        h=masks(35,rows,[tuple(min(i+1,s-1) for i in range(s))])
        assert len(h)-1==s-2
        assert h[-1][0][1]==1
        sharp.append([s,len(h)-1])
    return {"N35_signed_residue_collision":{"b":[0,21],"endpoint_and_residue":[4,1],
                    "candidate_atoms":[[list(h),q] for h,q in a.items()]},
            "N45_nonunit_gap_unique":{"endpoint":31,"b":10,
                    "candidate_atoms":[[list(h),q] for h,q in b.items()]},
            "N35_future_pair_0_1_masks":[m[0][1] for m in hist],
            "sharp_depth_states_and_words":sharp}


if __name__=="__main__":
    print(json.dumps({"perfect_power_checks":perfect_powers(),"finite_table_moduli":table_checks(),
                      "matrix_scope_checks":matrix_checks(),"examples":details()},indent=2))
