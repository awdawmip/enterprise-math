"""Integer checks for the finite exceptional component and uniform exterior bound."""
from collections import Counter
from math import gcd, isqrt
import json

CARD = ((1,0),(-1,0),(0,1),(0,-1))
KING = CARD + ((1,1),(1,-1),(-1,1),(-1,-1))
REPS = ((1,1),(2,1),(3,0),(3,2),(4,1),(5,2),(6,1),(7,0),(7,2),
        (8,3),(8,5),(9,4),(10,3),(11,4))
EXCEPTION_REPS = ((1,1),(2,1),(3,0),(3,2))


def orbit(z):
    x,y=z
    return {(a*i,b*j) for a in (1,-1) for b in (1,-1) for i,j in ((x,y),(y,x))}


def near(z, steps):
    x,y=z
    for dx,dy in steps:
        yield x+dx,y+dy


def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def gaussian_prime(z):
    x,y=z
    if x*y:
        return prime(x*x+y*y)
    v=max(abs(x),abs(y))
    return prime(v) and v%4==3


def avoiding(z,q):
    x,y=z
    return gcd(x*x+y*y,q)==1


def walk(r, steps, eligible, guard=None):
    seen={r}
    todo=[r]
    for z in todo:
        for w in near(z,steps):
            if w not in seen and eligible(w):
                seen.add(w)
                todo.append(w)
                if guard is not None and len(todo)>guard:
                    raise AssertionError('claimed finite component exceeded certificate bound')
    return seen


def quotient(q):
    points={(x,y) for x in range(q) for y in range(q) if avoiding((x,y),q)}
    pos={}
    h=Counter()
    edges=0
    for start in sorted(points):
        if start in pos: continue
        pos[start]=start
        todo=[start]
        for u in todo:
            x,y=pos[u]
            for dx,dy in CARD:
                a,b=x+dx,y+dy
                v=a%q,b%q
                if v not in points: continue
                edges+=1
                if v in pos:
                    assert pos[v]==(a,b)
                else:
                    pos[v]=(a,b)
                    todo.append(v)
        h[len(todo)]+=1
    return len(points),edges//2,h


def lifted_65_then_remove_3():
    # Explore literal integer points and their neighbours. No modulo-195 edges
    # or displacement labels are used in this calculation.
    unvisited={(x,y) for x in range(65) for y in range(65) if avoiding((x,y),65)}
    counts=Counter()
    while unvisited:
        r=min(unvisited)
        S=walk(r,CARD,lambda u:avoiding(u,65),65**2)
        residues={(x%65,y%65) for x,y in S}
        assert len(residues)==len(S) and residues<=unvisited
        unvisited-=residues
        for a in range(3):
            for b in range(3):
                # Each phase removes one point residue (a,b) modulo 3.
                part={u for u in S if (u[0]%3,u[1]%3)!=(a,b)}
                while part:
                    C=walk(next(iter(part)),CARD,part.__contains__)
                    part-=C
                    counts[len(C)]+=1
    return counts


def report():
    P=set().union(*(orbit(z) for z in REPS))
    E=set().union(*(orbit(z) for z in EXCEPTION_REPS))
    assert E<=P and len(E)==24 and all(map(gaussian_prime,P))
    assert P==walk((1,1),KING,gaussian_prime,100)
    assert len(P)==100
    boundary={v for z in P for v in near(z,KING)}-P
    assert not any(map(gaussian_prime,boundary))
    odd=sorted({x*x+y*y for x,y in boundary if (x+y)%2})
    assert odd==[1,25,45,65,85,117,125,153,169]
    for t in orbit((1,1)):
        assert len(walk(t,CARD,gaussian_prime,3))==3
    count,edges,h=quotient(195)
    assert h==lifted_65_then_remove_3()
    assert count==18432 and edges==15246 and sum(h.values())==3618 and max(h)==71
    return {'exterior_period':195,'exterior_residues':count,'exterior_undirected_edges':edges,
            'exterior_component_histogram':dict(sorted(h.items())),
            'exterior_number_of_components':sum(h.values()),'exterior_max':max(h),
            'exception_count':len(E),'prime_core_size':len(P),'core_orbit_representatives':REPS,
            'core_external_boundary_size':len(boundary),'boundary_odd_norms':odd,
            'core_axis_prime_coordinates':sorted({max(abs(x),abs(y)) for x,y in P if x*y==0}),
            'max_prime_component_D_lt_1':1,'max_prime_component_1_to_sqrt2_excluded':3,
            'max_prime_component_sqrt2_to_2_excluded':100}


if __name__=='__main__':
    print(json.dumps(report(),indent=2))
