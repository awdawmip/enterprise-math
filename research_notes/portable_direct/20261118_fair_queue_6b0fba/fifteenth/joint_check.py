"""Finite Eisenstein-row verification. The ring of values is Z[z]/(z^4-z^2+1), z=exp(pi*i/6)."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import prod
import json

ZERO=(0,0,0,0)
ONE=(1,0,0,0)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))
def scale(n,a):
    return tuple(n*x for x in a)
def mul(a,b):
    c=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    for i in range(6,3,-1):
        c[i-2]+=c[i]
        c[i-4]-=c[i]
    return tuple(c[:4])
def times(xs):
    out=ONE
    for x in xs:
        out=mul(out,x)
    return out
ROOTS=[ONE]
for k in range(11):
    ROOTS.append(mul(ROOTS[-1],(0,1,0,0)))
def conj(a):
    out=ZERO
    for j,b in enumerate(a):
        out=add(out,scale(b,ROOTS[(-j)%12]))
    return out
def sq(a):
    return mul(a,conj(a))
def scalar(x):
    assert x[1:]==(0,0,0)
    return x[0]
def total(values):
    out=ZERO
    for x in values:
        out=add(out,x)
    return out

# q_p=7,7,25,13. For split ideals, omega maps to 2,4 (mod 7) or 3 (mod 13).
NORMS=(7,7,25,13)
def residue_mul5(a,b):
    x,y=a
    v,w=b
    return ((x*v-y*w)%5,(x*w+y*v-y*w)%5)
def prime_logs(a,b):
    logs=[]
    for p,omega in [(7,2),(7,4)]:
        v=(a+omega*b)%p
        lookup={pow(1+omega,j,p):j for j in range(6)}
        logs.append(lookup[v] if v else None)
    v=(a%5,b%5)
    w=residue_mul5(v,v)
    w=residue_mul5(w,w)
    roots={(1,0):0}
    x=(1,0)
    for j in range(1,6):
        x=residue_mul5(x,(1,1))
        roots[x]=j
    logs.append(roots[w] if v!=(0,0) else None)
    v=(a+3*b)%13
    logs.append({pow(4,j,13):j for j in range(6)}[v*v%13] if v else None)
    return tuple(logs)

def chi(exp,logs):
    if any(e and k is None for e,k in zip(exp,logs)):
        return ZERO
    return ROOTS[2*sum(e*(k or 0) for e,k in zip(exp,logs))%12]

def classify(a,b):
    conductor=[q for x,y,q in zip(a,b,NORMS) if (x-y)%6]
    mask=[q for x,y,q in zip(a,b,NORMS) if (x or y) and (x-y)%6==0]
    return prod(conductor),prod(mask),prod((Fraction(q-1,q) for q in mask),start=Fraction(1))

def complete_rows():
    # Use the nonzero representative (35,0) of the all-zero residue.
    return [prime_logs(a if a or b else 35,b) for a,b in product(range(35),repeat=2)]

def gram(rows):
    indices=[(i,j,k) for i,j,k in product(range(3),range(3),range(2))]
    indices += [(6,0,0),(0,6,0),(1,6,0),(7,0,0),(0,0,6),(6,6,6)]
    # Bucket equal vectors of character values per row; zero masks are tested before reduction mod 6.
    hist=defaultdict(int)
    for vals in rows:
        hist[vals[:3]]+=1
    def local_product(a,b,k):
        if any((x or y) and v is None for x,y,v in zip(a,b,k)):
            return ZERO
        return ROOTS[2*sum((x-y)*(v or 0) for x,y,v in zip(a,b,k))%12]
    count=0
    resonant=0
    for a,b in product(indices,repeat=2):
        f,mask,mass=classify(a,b)
        value=total(scale(n,local_product(a,b,v)) for v,n in hist.items())
        assert Fraction(scalar(value),len(rows))==(mass if f==1 else 0)
        count+=1
        resonant+=(f==1)
    f, _, alias=classify((6,0,0),(0,6,0))
    assert f==1 and alias==Fraction(36,49)
    return {"norms":[7,7,25],"modulus_norm":len(rows),"columns":len(indices),
            "gram_entries":count,"resonant_entries":resonant,"norm_equal_split_alias":str(alias)}

def geometric():
    units=0
    stats=[]
    for shift in [0,-1]:  # t=0 or pi/(6 log 25); phases are z^shift for one norm 25.
        M=S=joint=ZERO
        for a,b in product(range(5),repeat=2):
            k=prime_logs(a,b)[2]
            if k is None:
                continue
            x=ROOTS[(2*k+shift)%12]
            inv=add(ONE,scale(-1,x))
            plain=total(ROOTS[(j*(2*k+shift))%12] for j in range(6))
            marked=mul(x,mul(inv,plain))
            # Individual |M|^2 may lie in Q(sqrt(3)); accumulate in the full number ring.
            M=add(M,sq(inv))
            S=add(S,sq(plain))
            joint=add(joint,sq(marked))
            if shift==0: units+=1
        stats.append({"phase_shift_twelfths":shift,"unit_average_inverse_squared":scalar(M)//24,
                      "unit_average_plain_squared":scalar(S)//24,"unit_average_joint_squared":scalar(joint)//24,
                      "all_residues_average_joint_squared":str(Fraction(scalar(joint),25))})
    assert units==24 and [o["unit_average_joint_squared"] for o in stats]==[0,4]
    return stats

def evec(i):
    return tuple(int(j==i) for j in range(4))
def plus(*indices):
    return tuple(map(sum,zip(*indices)))
def evalpoly(terms,v):
    return total(scale(c,chi(exp,v)) for exp,c in terms.items())

def overlaps():
    zero_exp=(0,0,0,0)
    # Möbius on all squarefree divisors of three good primes (finite coefficient check);
    # plain columns include squareful and sixth-power terms.
    inv={(*x,0):(-1)**sum(x) for x in product(range(2),repeat=3)}
    plain={zero_exp:1,evec(0):1,(2,0,0,0):1,(0,6,0,0):1,(0,0,2,0):1}
    slots=({0:1,1:-1},{2:1,3:1})
    merged=defaultdict(int)
    for (n,a),(l,b),i,j in product(inv.items(),plain.items(),slots[0],slots[1]):
        merged[plus(n,l,evec(i),evec(j))]+=a*b*slots[0][i]*slots[1][j]
    rows=[(a,b) for a in range(-11,12) for b in range(-11,12) if (a,b)!=(0,0) and a*a-a*b+b*b<=81]
    masks=[0]*4
    for a,b in rows:
        v=prime_logs(a,b)
        base=mul(evalpoly(inv,v),evalpoly(plain,v))
        choices={ij:times([scale(slot[i],chi(evec(i),v)) for slot,i in zip(slots,ij)])
                 for ij in product(*slots)}
        assert mul(base,total(choices.values()))==evalpoly(merged,v)
        actual=[ZERO]*4
        for x,y in product(choices,repeat=2):
            mask=sum((i==j)<<k for k,(i,j) in enumerate(zip(x,y)))
            actual[mask]=add(actual[mask],mul(choices[x],conj(choices[y])))
        factors=[]
        for slot in slots:
            vals=[scale(c,chi(evec(i),v)) for i,c in slot.items()]
            diag=sum(scalar(sq(z)) for z in vals)
            assert diag==sum(c*c for i,c in slot.items() if v[i] is not None)
            factors.append([add(sq(total(vals)),scale(-diag,ONE)),scale(diag,ONE)])
        for mask in range(4):
            assert actual[mask]==times(factors[k][(mask>>k)&1] for k in range(2))
            masks[mask]+=scalar(mul(sq(base),actual[mask]))
    assert sum(masks)==sum(scalar(sq(evalpoly(merged,prime_logs(*row)))) for row in rows)
    return {"nonzero_element_rows_N_le_81":len(rows),"norms":list(NORMS),"mask_order":"bits for equal first/second slots",
            "integer_joint_sums_by_exact_equality_pattern":masks,"joint_total":sum(masks),
            "raw_column_tuples":len(inv)*len(plain)*4,"combined_columns":len(merged),
            "nonzero_combined_columns":sum(c!=0 for c in merged.values())}

if __name__=="__main__":
    rows=complete_rows()
    print(json.dumps({"complete_residue_gram":gram(rows),"genuine_inert_prime_probe":geometric(),
                      "two_slot_disk_test":overlaps()},indent=2))
