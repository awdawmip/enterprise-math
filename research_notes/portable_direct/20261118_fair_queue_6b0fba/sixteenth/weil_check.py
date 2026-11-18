"""Exact finite certificate for the prime shifts on the log(5) Weil window."""
import argparse
import ast
from fractions import Fraction as F
from hashlib import sha256
from io import BytesIO
import json
from math import isqrt, prod
from pathlib import Path
import re
from urllib.request import urlopen
from zipfile import ZipFile


RBASE = "https://rstation.ai/api/v1/papers/riemann_hypothesis_"
LIU = ("https://raw.githubusercontent.com/luciferyu666/certified-weil-positivity/"
       "b6cd2183c1e79c6c27a34267812a7b2d73ed1b59/frozen-source/publication/manuscript.tex")
SOURCES = {
    "li1.md": (RBASE+"45/versions/1/download", "220c504b57107d4c40f7df854ab33c6c2649458bb712225648f02f8cb4f02413"),
    "li2.md": (RBASE+"45/versions/2/download", "ff635e2e070d442ba5b48b20a29a1a908942254887d46bacca77d9cd551f3e8d"),
    "lsupp1": (RBASE+"45/versions/1/supplement", "87d85c8cb1c9c6d004cd9b9944b761190941504f2205b371d33b4758b70cbe0b"),
    "lsupp2": (RBASE+"45/versions/2/supplement", "b96175b4db3d491ab4b57da77f4b4f054a5c1e8c96436b218f31c053ab997ac0"),
    "liu.tex": (LIU, "f8b0576c9321b00edf2c939b9ee0bad0f49624e1ec963fe94d1c4e572951eded"),
    "zhu": ("https://arxiv.org/pdf/2608.24827v2", "70332e428dd7ab82a352131787ac3db4b321459f0e12a6765a8ab1e6fbc22026"),
    "rst60.md": (RBASE+"60/versions/1/download", "e00cfeb7c50db39b88bbdc385b133061355ff3a13270df277cb9ef9467e0e19a"),
}


def log_bounds(q, terms=90):
    u = (q-1)/(q+1)
    assert 0 < u < 1
    lo = 2*sum(u**(2*j+1)/(2*j+1) for j in range(terms))
    return lo, lo+2*u**(2*terms+1)/((2*terms+1)*(1-u*u))


def sqrt_bounds(n):
    scale = 10**23
    low = isqrt(n*scale**2)
    return F(low,scale), F(low+1,scale)


def weight_intervals():
    weights = {}
    for n,p in ((2,2),(3,3),(4,2)):
        l,h = log_bounds(F(p))
        lo,hi = sqrt_bounds(n)
        weights[n] = (l/hi,h/lo)
    return weights


def discover(left, right, base=F(1), vertices=()):
    dividers = {left,right}
    for change in (F(5,4),F(4,3),F(5,3)):
        if left < change/base < right:
            dividers.add(change/base)
    ordered = sorted(dividers)
    for lo,hi in zip(ordered,ordered[1:]):
        y = base*(lo+hi)/2
        count = 3 if y<F(5,4) else 2
        new_points = vertices+tuple(base*2**j for j in range(count))
        if y>F(5,3):
            yield lo,hi,new_points
        else:
            k = 1 if 3*y<4 else 2
            yield from discover(lo,hi,3*base/2**k,new_points)


def edges(vertices):
    return [(i,j,int(r)) for i,x in enumerate(vertices)
            for j,y in enumerate(vertices[:i])
            if (r:=max(x/y,y/x)) in (2,3,4)]


def format_fixed(v, digits, upper):
    scale = 10**digits
    i = int(-(-v*scale//1) if upper else v*scale//1)
    return f"{i//scale}.{i%scale:0{digits}d}"


def spectral_bracket(vertices, weights):
    graph = edges(vertices)
    size = len(vertices)
    scale = 10**17
    mid = {n:int(scale*(lo+hi)/2) for n,(lo,hi) in weights.items()}
    vec = [scale]*size
    for _ in range(330):
        new = [v*scale for v in vec]  # A+I removes any bipartite oscillation.
        for i,j,n in graph:
            new[i] += mid[n]*vec[j]
            new[j] += mid[n]*vec[i]
        peak = max(new)
        vec = [max(1,scale*t//peak) for t in new]
    lower = [F(0) for _ in vec]
    upper = [F(0) for _ in vec]
    for i,j,n in graph:
        lo,hi = weights[n]
        lower[i] += lo*vec[j]
        lower[j] += lo*vec[i]
        upper[i] += hi*vec[j]
        upper[j] += hi*vec[i]
    a = min(v/t for v,t in zip(lower,vec))
    b = max(v/t for v,t in zip(upper,vec))
    return [format_fixed(a,10,False),format_fixed(b,10,True)]


def finite_certificate():
    weights = weight_intervals()
    components = list(discover(F(5,4),F(3,2)))
    tiles = sorted((l*x,r*x) for l,r,v in components for x in v)
    assert tiles[0][0] == 1 and tiles[-1][1] == 5
    assert all(t[1] == u[0] for t,u in zip(tiles,tiles[1:]))
    assert prod((r/l)**len(v) for l,r,v in components)==5
    result = []
    for l,r,vertices in components:
        # Every neighbour lies in the same fibre or is wholly outside (1,5).
        for x in vertices:
            for h in (F(2),F(3),F(4),F(1,2),F(1,3),F(1,4)):
                v=x*h
                assert v in vertices or v*r<=1 or v*l>=5
        result.append(dict(interval=[str(l),str(r)],labels=list(map(str,vertices)),
                           dimension=len(vertices),rho_bounds=spectral_bracket(vertices,weights)))
    largest = max(result,key=lambda row:F(row['rho_bounds'][1]))
    assert largest['dimension']==12
    assert F(largest['rho_bounds'][1]) < F(121914,100000)
    biggest_labels = list(map(F,largest['labels']))
    assert max(biggest_labels)/min(biggest_labels)==F(9,2)
    l5 = tuple(x/2 for x in log_bounds(F(5)))
    assert F(4,5)<l5[0]<l5[1]<F(81,100)
    assert log_bounds(F(9,2))[1] < F(8,5)
    odd_pole_max = 4/sqrt_bounds(5)[0]-log_bounds(F(5))[0]
    assert odd_pole_max < F(18,100)
    diag_floor = log_bounds(F(400,81))[0]-F(81,2400)
    even_floor = diag_floor-F(largest['rho_bounds'][1])
    odd_floor = even_floor-odd_pole_max
    assert even_floor>F(1,3) and odd_floor>F(1,8)
    return dict(components=result,exact_endpoint_tile_count=len(tiles),
                plateau_Y="9/2 < Y <= 5",
                orthogonal_tail=dict(first_omitted_mode=8,even_lower="1/3",odd_lower="1/8",
                                     even_lower_numeric_down=format_fixed(even_floor,8,False),
                                     odd_lower_numeric_down=format_fixed(odd_floor,8,False)))


def unicode_npy(data):
    assert data[:8] == b"\x93NUMPY\x01\x00"
    start = 10+int.from_bytes(data[8:10],"little")
    info = ast.literal_eval(data[10:start].decode("ascii").strip())
    assert not info["fortran_order"] and info["descr"].startswith("<U")
    n=4*int(info["descr"][2:])
    return [data[i:i+n].decode("utf-32-le").rstrip("\0") for i in range(start,len(data),n)]


def ball_lower(text):
    m = re.fullmatch(r"\[([^ ]+) \+/- ([^ ]+)\]", text)
    return F(m[1])-F(m[2]) if m else F(text)


def source_check(directory, fetch):
    directory.mkdir(exist_ok=True,parents=True)
    for name,(url,digest) in SOURCES.items():
        path=directory/name
        if fetch and not path.exists():
            with urlopen(url,timeout=90) as response:
                data=response.read()
            assert sha256(data).hexdigest()==digest
            path.write_bytes(data)
        assert sha256(path.read_bytes()).hexdigest()==digest, name
    with ZipFile(directory/"lsupp2") as archive:
        files=archive.read("CONTENTS.sha256").decode().splitlines()
        for line in files:
            digest,path=line.split(maxsplit=1)
            assert sha256(archive.read(path.strip())).hexdigest()==digest
        dimensions=[]
        for item in archive.namelist():
            if not item.endswith(".npz"):
                continue
            with ZipFile(BytesIO(archive.read(item))) as arrays:
                pivots=unicode_npy(arrays.read("pivots.npy"))
                assert all(ball_lower(v)>0 for v in pivots)
                assert all(ball_lower(v)>0 for k in ("t400.npy","tqf.npy","Hmin.npy")
                           for v in unicode_npy(arrays.read(k)))
                dimensions.append(len(pivots))
        assert sorted(dimensions)==[6,7]
    return dict(v2_manifest_entries=len(files),v2_positive_frozen_pivots=sorted(dimensions))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json",type=Path)
    parser.add_argument("--sources",type=Path,
                        help="verify downloaded primary files and the v2 supplement")
    parser.add_argument("--fetch",action="store_true",help="download absent sources to --sources")
    args=parser.parse_args()
    if args.fetch and not args.sources:
        parser.error("--fetch requires --sources")
    out=finite_certificate()
    out["sources"]={k:{"url":url,"sha256":h} for k,(url,h) in SOURCES.items()}
    if args.sources:
        out["source_checks"]=source_check(args.sources,args.fetch)
    data=json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if args.json: args.json.write_text(data)
    else: print(data,end="")


if __name__=="__main__":
    main()
