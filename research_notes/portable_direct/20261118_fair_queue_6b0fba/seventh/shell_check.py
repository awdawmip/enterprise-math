"""Layer counts on the signed nearest-neighbour cubic lattice. Python standard library."""
from collections import deque
from itertools import product
from math import comb, factorial, prod


def steps(point):
    for j in range(len(point)):
        for sign in (-1, 1):
            dest = list(point)
            dest[j] += sign
            yield j, sign, tuple(dest)


def enumerate_layers(seed, radius):
    """Multi-source BFS on raw native charts. Retain start-labelled shortest words."""
    seed = set(seed)
    if not seed or radius < 0:
        raise ValueError("a nonempty seed and a nonnegative radius are required")
    d = len(next(iter(seed)))
    if d == 0 or not all(len(v) == d for v in seed):
        raise ValueError("seed dimensions must agree and be positive")
    distance = dict.fromkeys(seed, 0)
    paths = dict.fromkeys(seed, 1)
    queue = deque(seed)
    while queue:
        x = queue.popleft()
        r = distance[x]
        if r == radius + 1:
            continue
        for _, _, y in steps(x):
            if y not in distance:
                distance[y] = r+1
                paths[y] = 0
                queue.append(y)
            if distance[y] == r+1:
                paths[y] += paths[x]
    # Last-edge word counts belong to paths FROM r TO r+1.
    rows = [dict(vertices=0, words=0, out=[[0,0] for _ in range(d)],
                 flat=[0]*d, last=[[0,0] for _ in range(d)]) for _ in range(radius+1)]
    for x,r in distance.items():
        if r > radius:
            continue
        row = rows[r]
        row["vertices"] += 1
        row["words"] += paths[x]
        for j,sign,y in steps(x):
            k = int(sign == 1)
            if distance[y] == r+1:
                row["out"][j][k] += 1
                row["last"][j][k] += paths[x]
            elif distance[y] == r and sign == 1:
                row["flat"][j] += 1
    return rows, distance


def multiply(factors, radius, exponential=False):
    """Truncated coefficients. In exponential mode return n! times [t^n]."""
    result = [1]+[0]*radius
    for factor in factors:
        result = [sum(result[n-k]*factor[k]*(comb(n,k) if exponential else 1)
                      for k in range(n+1)) for n in range(radius+1)]
    return result


def box_series(widths, radius):
    d = len(widths)
    factors = [[width]+[2]*radius for width in widths]
    ones = [1]*(radius+1)
    vertices = multiply(factors,radius)
    words = multiply(factors,radius,True)
    out, flat, last = [],[],[]
    for j in range(d):
        rest = factors[:j]+factors[j+1:]
        out.append(multiply([ones]+rest,radius))
        flat.append([(widths[j]-1)*c for c in multiply(rest,radius)])
        last.append(multiply([ones]+rest,radius,True))
    return vertices, words, out, flat, last


def seeds(widths, notched=False):
    seed = set(product(*(range(m) for m in widths)))
    if notched:
        seed.remove(tuple(0 for _ in widths))
    return seed


def check_box(widths, radius):
    rows,_ = enumerate_layers(seeds(widths),radius)
    vertices,words,out,flat,last = box_series(widths,radius)
    for r,row in enumerate(rows):
        assert row["vertices"] == vertices[r] and row["words"] == words[r]
        for j in range(len(widths)):
            assert row["out"][j] == [out[j][r]]*2
            assert row["last"][j] == [last[j][r]]*2
            assert row["flat"][j] == flat[j][r]
    return rows


def check_notch(widths, active, radius):
    # Corner removed in the first m nondegenerate axes, other widths must be 1.
    assert 1 <= active <= len(widths)
    assert all(w>=2 for w in widths[:active]) and all(w==1 for w in widths[active:])
    d,m=len(widths),active
    rows,_=enumerate_layers(seeds(widths,True),radius)
    vertices,words,out,flat,last = box_series(widths,radius)
    unity=[1]*(radius+1)
    G=[1]+[2]*radius
    face=multiply([unity]*(m-1)+[G]*(d-m),radius)
    delta_w=[(m-1)*m**r-m*(m-1)**r for r in range(radius+1)]
    base_delta_w=delta_w
    delta_w=multiply([base_delta_w]+[G]*(d-m),radius,True)
    active_word_diff=[(m-1)*(m**r-(m-1)**r) for r in range(radius+1)]
    active_word_diff=multiply([active_word_diff]+[G]*(d-m),radius,True)
    for r,row in enumerate(rows):
        assert row["vertices"] == vertices[r]-face[r]
        assert row["words"] == words[r]+delta_w[r]
        for j in range(d):
            if j<m:
                assert row["out"][j] == [out[j][r]]*2
                assert row["flat"][j] == flat[j][r]-face[r]
                assert row["last"][j] == [last[j][r]+active_word_diff[r],last[j][r]]
            else:
                decrease=multiply([unity]*m+[G]*(d-m-1),radius)[r]
                assert row["out"][j] == [out[j][r]-decrease]*2
                assert row["flat"][j] == 0
                correction=multiply([base_delta_w,unity]+[G]*(d-m-1),radius,True)[r]
                assert row["last"][j] == [last[j][r]+correction]*2
    return rows


def run():
    for shape in ((1,), (2,), (1,1), (2,3),(2,3,1),(3,2,2),(1,1,1,1,1,1)):
        check_box(shape,4)
    for shape,m in (((3,),1),((2,2),2),((3,2,1),2),((2,2,2,1),3)):
        check_notch(shape,m,4)
    shape=(2,1,1,1,1,1)
    double=check_box(shape,5)
    elbow=check_notch((2,2,1,1,1,1),2,5)
    # Reflect the y-coordinate to match the frozen, marked elbow with its actual signs.
    source_elbow={(0,)*6,(1,0,0,0,0,0),(1,1,0,0,0,0)}
    original,_=enumerate_layers(source_elbow,5)
    for r,row in enumerate(original):
        assert row["last"][0] == elbow[r]["last"][0]
        assert row["last"][1] == elbow[r]["last"][1][::-1]
        assert all(row[k] == elbow[r][k] for k in ("vertices","words","out","flat"))
    for label,rows in (("adjacent pair",double),("three-cell elbow",original)):
        for r,row in enumerate(rows):
            print(label,r,row["vertices"],row["out"][0],row["out"][1],row["out"][2],
                  row["flat"][:3],row["words"],row["last"][:3])
    A=(0,)*6
    B=(1,0,0,0,0,0)
    _,da=enumerate_layers([A],5)
    _,db=enumerate_layers([B],5)
    _,ds=enumerate_layers([A,B],5)
    for r in range(6):
        ba={x for x,k in da.items() if k<=r}
        bb={x for x,k in db.items() if k<=r}
        assert ba & bb == {x for x,k in ds.items() if k<=r-1}
        assert not ({x for x,k in da.items() if k==r} & {x for x,k in db.items() if k==r})
    old=[x for x in product(range(-5,6),repeat=3) if sum(v*v for v in x)==25]
    old_words=sum(factorial(sum(map(abs,x)))//prod(factorial(abs(v)) for v in x) for x in old)
    assert len(old)==30 and old_words==846
    print("fixed-cell squared-radius 25:",len(old),old_words)


if __name__ == "__main__":
    run()
