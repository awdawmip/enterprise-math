"""Signed, source-indexed BRC branch jets for one intrinsic shortest triadic cycle."""
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys


KERNEL_SHA = "4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f"
CUBE = tuple(product((0, 1), repeat=6))
AXES = (1, 2, 3)
COORDINATES = tuple(product(AXES, repeat=3))
PANEL = ((1,2,1), (1,3,1), (1,2,3), (2,2,3))
MINOR = ((1,1,2), (1,1,3), (1,2,1), (1,2,3), (1,3,1), (2,2,3))


def path(bits, axes=AXES, chirality=1):
    i, j, k = axes
    if chirality == -1:
        j, k = k, j
    orbit = (i, -j, k, -i, j, -k, i)
    return tuple(s for a,b,outer in zip(orbit, orbit[1:], bits)
                 for s in ((b,-a) if outer else (-a,b)))


def jet(kernel, steps, degree=3):
    # Every primitive position makes a skip/take choice. Retain word AND product sign.
    lanes = {((),1):kernel.CWM_ONE}
    for step in steps:
        updated = dict(lanes)
        for (word,sign), count in lanes.items():
            if len(word) == degree:
                continue
            key = (word+(abs(step),), sign * (1 if step > 0 else -1))
            take = kernel.cwm_propagate(count, kernel.CWM_ONE)
            updated[key] = kernel.cwm_recoalesce(updated.get(key,kernel.CWM_ZERO), take)
        lanes = updated
    assert all(s.count == s.total and s.dominant == 1 for s in lanes.values())
    words = {word for word,sign in lanes}
    observed = {w:lanes.get((w,1),kernel.CWM_ZERO).count-lanes.get((w,-1),kernel.CWM_ZERO).count
                for w in words}
    return {w:n for w,n in observed.items() if n}


def multiply(left, right, degree):
    out = Counter()
    for u,x in left.items():
        for v,y in right.items():
            if len(u) + len(v) <= degree:
                out[u+v] += x*y
    return {w:n for w,n in out.items() if n}


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1)**j * v * determinant([row[:j]+row[j+1:] for row in matrix[1:]])
               for j,v in enumerate(matrix[0]) if v)


def rank_mod2(rows):
    basis = {}
    for row in rows:
        vector = sum((x%2)<<i for i,x in enumerate(row))
        while vector:
            pivot = vector.bit_length()-1
            if pivot not in basis:
                basis[pivot] = vector
                break
            vector ^= basis[pivot]
    return len(basis)


def local_panel(rows, modulus):
    project = (lambda x:x%modulus) if modulus else (lambda x:x)
    counts, sizes = [], []
    for i in range(3):
        labels = [key for key,row in rows.items() if row[i] or row[i+3]]
        for size in range(1, len(labels)+1):
            ways = 0
            for panel in combinations(labels, size):
                values = {tuple(project(rows[k][i]*a + rows[k][i+3]*b) for k in panel)
                          for a,b in product((0,1),repeat=2)}
                if len(values) == 4:
                    ways += 1
            if ways:
                counts.append(ways)
                sizes.append(size)
                break
    if len(counts) < 3:
        return None
    return dict(per_pair=sizes, minimum=sum(sizes), panels=counts[0]*counts[1]*counts[2])


def mixed_mod4_check(tensors, base):
    outputs = set()
    for bits,t in tensors.items():
        def coeff(word):
            return t.get(word,0) - base.get(word,0)
        sums = (coeff((2,1,1)), coeff((1,2,3)), -coeff((1,1,3)))
        differences = (coeff((2,1,2)), coeff((2,2,3)), coeff((3,1,3)))
        doubled_right = tuple(a-b for a,b in zip(sums,differences))
        encoded = tuple((a+b)%4 for a,b in zip((*sums,0),(0,*doubled_right)))
        right = [0,0,encoded[3]//2]
        left = [0]*3
        for i in (2,1,0):
            left[i] = (encoded[i]-right[i])%2
            if i:
                right[i-1] = (encoded[i]-left[i]-right[i])%4//2
        assert tuple(left+right)==bits
        outputs.add(encoded)
    assert len(outputs)==64
    # Normalize the column-parity matrix U to I. Test the integer-proof minor condition over F_2.
    for code in range(2**9):
        v = [[(code>>(3*i+j))%2 for j in range(3)] for i in range(3)]
        dets = [determinant([[v[i][j]^(p[i] if i==j else 0) for j in range(3)] for i in range(3)])%2
                for p in product((0,1),repeat=3)]
        assert sum(dets)%2==1 and 0 in dets
    return dict(mixed_mod4_channels=4, words=len(outputs), normalized_obstructions=512)


def covariant(table, axes, chirality):
    i,j,k = axes
    mapping = {1:i, 2:j if chirality == 1 else k, 3:k if chirality == 1 else j}
    return {tuple(mapping[x] for x in w):v for w,v in table.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    source = args.repo / "src/enterprise_math/brc_weighted.py"
    assert sha256(source.read_bytes()).hexdigest() == KERNEL_SHA
    sys.path.insert(0, str(args.repo/"src"))
    from enterprise_math import brc_weighted as kernel

    tensors = {bits:jet(kernel,path(bits)) for bits in CUBE}
    zero = (0,)*6
    singles = [tuple(int(i==j) for i in range(6)) for j in range(6)]
    base = tensors[zero]
    rows = {k:tuple(tensors[b].get(k,0)-base.get(k,0) for b in singles) for k in COORDINATES}
    for key,row in rows.items():
        assert len({i%3 for i,c in enumerate(row) if c}) <= 1
    for bits,tensor in tensors.items():
        for k,row in rows.items():
            assert tensor.get(k,0) == base.get(k,0) + sum(a*b for a,b in zip(row,bits))
        x,y,n,d = [tensor.get(k,0)-base.get(k,0) for k in PANEL]
        assert (-x%3, (n+d)//2, y//3, -x//3, (n-d)//2, y%3) == bits
        steps = path(bits)
        assert multiply(jet(kernel,steps[:6]),jet(kernel,steps[6:]),3) == tensor
        reverse = jet(kernel, tuple(-v for v in reversed(steps)))
        assert reverse == {w[::-1]:(-1)**len(w)*v for w,v in tensor.items()}

    all_counts = []
    for d in (1,2,3):
        keys = tuple(w for length in range(1,d+1) for w in product(AXES,repeat=length))
        classes = Counter(tuple(t.get(w,0) for w in keys) for t in tensors.values())
        all_counts.append(dict(classes=len(classes), fibre_sizes=sorted(Counter(classes.values()).items())))
    assert [r['classes'] for r in all_counts] == [1,27,64]
    assert all_counts[1]['fibre_sizes'] == [(1,8),(2,12),(4,6),(8,1)]
    minor = [list(rows[k]) for k in MINOR]
    det = determinant(minor)
    assert abs(det)==8 and rank_mod2(rows.values())==3
    for r in rows.values():
        assert all((r[i]-r[i+3])%2 == 0 for i in range(3))

    channels={}
    for modulus in (0,2,3,4,5,6,7,8,9,10,11):
        classes = Counter(tuple(t.get(k,0)%modulus if modulus else t.get(k,0) for k in COORDINATES)
                          for t in tensors.values())
        panels = local_panel(rows,modulus)
        assert len(classes) == (8 if modulus==2 else 64)
        if modulus==2:
            assert set(classes.values()) == {8} and panels is None
        else:
            assert panels["minimum"] == (6 if modulus in (3,4) else 4)
        channels[str(modulus)] = dict(classes=len(classes), raw_panel=panels)

    callbacks=0
    for axes in combinations(range(1,7),3):
        for chirality in (1,-1):
            for bits in CUBE:
                source_steps = path(bits)
                mapped_steps = tuple(next(iter(covariant({(abs(x),):1},axes,chirality)))[0]
                                     * (1 if x>0 else -1) for x in source_steps)
                assert mapped_steps == path(bits,axes,chirality)
                callbacks+=1
            b = (1,0,1,1,0,0)
            assert jet(kernel,path(b,axes,chirality)) == covariant(tensors[b],axes,chirality)

    mixed = mixed_mod4_check(tensors,base)
    output=dict(mixed=mixed, kernel_sha256=KERNEL_SHA, integer_jet=all_counts, determinant=det, rank_mod2=3,
                smith=[1,1,1,2,2,2], signed_tensor_rows={"".join(map(str,k)):r for k,r in rows.items()
                                                        if any(r)}, channels=channels,
                canonical_composition_and_dagger_words=len(tensors), transported_primitive_words=callbacks,
                directly_replayed_transported_jets=40)
    data=json.dumps(output,ensure_ascii=True,sort_keys=True,indent=2)+"\n"
    if args.json:
        args.json.write_text(data)
    print("1/27/64; Smith 1,1,1,2,2,2; primitive words",callbacks,"sha256",sha256(data.encode()).hexdigest())


if __name__=="__main__":
    main()
