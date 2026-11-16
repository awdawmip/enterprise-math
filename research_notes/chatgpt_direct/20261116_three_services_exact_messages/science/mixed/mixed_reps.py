"""Orbit representatives for large classes when the first two transformations are shared."""
from itertools import product

POINTS=list(product(range(5),repeat=3))


def index(point):
    x,y,z=point
    return 25*x+5*y+z


def orbit(mask):
    rows=[p for i,p in enumerate(POINTS) if mask >> i & 1]
    result=set()
    for swap,a,b,k,l in product(range(2),(-1,1),(-1,1),(1,2),range(1,5)):
        image=[(x[swap]*a*k, x[1-swap]*b*k, x[2]*l) for x in rows]
        for t in POINTS:
            result.add(sum(1<<index(tuple((v+w)%5 for v,w in zip(y,t))) for y in image))
    return result


def go(masks):
    universe=set(masks)
    used=set()
    representatives=[]
    for i,mask in enumerate(masks):
        if mask in used:continue
        images=orbit(mask)
        assert images<=universe and not images&used
        used.update(images)
        representatives.append(i)
    assert used==universe
    return representatives
