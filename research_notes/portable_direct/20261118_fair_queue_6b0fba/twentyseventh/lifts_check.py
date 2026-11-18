"""Check cyclic face-label lifts on actual simplicial boundary matrices, in Python 3."""
import json
from collections import Counter
from itertools import product
from math import gcd


def edge(u, v):
    return (min(u, v), max(u, v))


def boundary(face):
    return [(u, v) for u, v in zip(face, face[1:] + face[:1])]


def complex_data(stages, prime=2):
    """Two triangles per pair, a 3p-gon between them, and an integral edge cochain."""
    length = 3*prime
    triangles = [(0, 1, 2)]
    faces = []
    values = {}

    def assign(u, v, x):
        key = edge(u, v)
        signed = x if u < v else -x
        assert u != v and values.get(key, signed) == signed
        values[key] = signed

    for i in range(stages + 1):
        if i:
            first = 3 + (length+3)*(i-1)
            middle = list(range(first, first+length))
            triangles.append(tuple(range(first+length, first+length+3)))
        cycle = triangles[i]
        for j in range(3):
            assign(cycle[j], cycle[(j+1)%3], prime**i if j==2 else 0)
        if not i:
            continue
        small = [int(j%3==2) * prime**(i-1) for j in range(length)]
        for j in range(length):
            assign(middle[j], middle[(j+1)%length], small[j])
        for target, index, weight in (
            (triangles[i-1], [j%3 for j in range(length)], prime**(i-1)),
            (triangles[i], [j//prime for j in range(length)], prime**i),
        ):
            # A square with one collapsed target edge contributes one triangle.
            radial = 0
            for j in range(length):
                n = (j+1)%length
                u, v = middle[j], middle[n]
                left, right = index[j], index[n]
                x, y = target[left], target[right]
                delta = weight if left==2 and right==0 else 0
                assign(u, x, radial)
                faces.append((u,v,y))
                if x != y:
                    faces.append((u,x,y))
                    assign(u, y, radial + delta)
                radial += delta-small[j]
            assert radial == 0
    assert len(set(tuple(sorted(f)) for f in faces)) == len(faces)
    assert all(len(set(f))==3 for f in faces)
    face_edges = {edge(u,v) for f in faces for u,v in boundary(f)}
    assert face_edges == values.keys()
    return triangles, faces, values


def period(values, face):
    return sum((1 if u<v else -1)*values[edge(u,v)] for u,v in boundary(face))


def chord_matrix(edges, faces):
    n = max(v for _,v in edges)+1
    parent = list(range(n))

    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v

    chords = []
    for u,v in sorted(edges):
        a,b = find(u),find(v)
        if a==b:
            chords.append((u,v))
        else:
            parent[a] = b
    assert all(find(u)==find(0) for u in range(n))
    cols = {e:i for i,e in enumerate(chords)}
    rows = []
    for f in faces:
        row = {}
        for u,v in boundary(f):
            if edge(u,v) in cols:
                row[cols[edge(u,v)]] = 1 if u<v else -1
        rows.append(row)
    return rows, len(chords)


def unit_core(rows, ncols):
    """Eliminate unit pivots by integral row and column operations."""
    rows = [r.copy() for r in rows]
    active = set(range(ncols))
    pivots = 0
    while True:
        candidates = ((len(r), i, j) for i,r in enumerate(rows)
                      for j,c in r.items() if abs(c)==1)
        best = min(candidates,default=None)
        if best is None:
            break
        _, index, j = best
        pivot = rows.pop(index)
        unit = pivot[j]
        active.remove(j)
        for r in rows:
            multiple = r.get(j,0)*unit
            if multiple:
                for q,c in pivot.items():
                    value = r.get(q,0)-multiple*c
                    if value:
                        r[q] = value
                    else:
                        r.pop(q,None)
        pivots += 1
    return pivots, [[r.get(j,0) for j in sorted(active)] for r in rows], len(active)


def smooth_witnesses():
    census = []
    for t in range(1,9):
        stages = t+1
        rings, faces, values = complex_data(stages)
        v,e,f = 3+9*stages,len(values),len(faces)
        assert (e,f)==(3+30*stages,21*stages)
        assert all(period(values,z)==0 for z in faces)
        assert [period(values,z) for z in rings] == [2**i for i in range(stages+1)]
        cores = []
        for cap in (t,t+1):
            rows, chords = chord_matrix(values, faces+[rings[cap]])
            pivots, core, width = unit_core(rows,chords)
            assert width==1 and len(core)==1 and abs(core[0][0])==2**cap
            cores.append(abs(core[0][0]))
        for j in range(1,t+1):
            assert all(period(values,z)%(2**j)==0 for z in faces+[rings[t],rings[t+1]])
        assert period(values,rings[t])%(2**(t+1))==2**t
        assert period(values,rings[t+1])%(2**(t+1))==0
        coarse_modulus = 2**t
        fine_modulus = 2*coarse_modulus
        profiles = []
        for d in cores:
            lifts = Counter(y%coarse_modulus for y in range(fine_modulus) if d*y%fine_modulus==0)
            profiles.append(dict(Counter(lifts[x] for x in range(coarse_modulus))))
        assert profiles == [{0:coarse_modulus//2,2:coarse_modulus//2},{2:coarse_modulus}]
        census.append({"t":t,"vertices":v,"edges":e,"triangles_each_with_cap":f+1,
                       "normalized_chords":chords,"unit_pivots_each":pivots,
                       "integral_residuals_early_late":cores,
                       "coarse_states_by_number_of_fine_lifts_early_late":profiles})
    return census


def mixed(m):
    return [x for x in product(range(m),repeat=3)
            if 2*(x[0]+x[1])%m==0 and 12*(x[1]+x[2])%m==0]


def fiber_tests():
    data = []
    total = 0
    for m,n in [(2,2),(2,4),(4,2),(4,4),(3,3),(6,2),(6,3),(4,3),(3,4)]:
        coarse, fine = mixed(m), mixed(m*n)
        fibres = Counter(tuple(z%m for z in x) for x in fine)
        predictions = {x for x in coarse
                       if (2*(x[0]+x[1])//m) % gcd(2,n) == 0
                       and (12*(x[1]+x[2])//m) % gcd(12,n) == 0}
        # In Smith coordinates a one-step correction can cancel exactly gcd(d,n) multiples.
        assert predictions == set(fibres)
        fixed = n*gcd(2,n)*gcd(12,n)
        image = m*gcd(2,m*n)//gcd(2,n)*gcd(12,m*n)//gcd(12,n)
        assert len(fibres)==image and set(fibres.values())=={fixed}
        data.append({"m":m,"n":n,"coarse":len(coarse),"fine":len(fine),
                     "image":image,"fibres_per_liftable_class":fixed})
        total += (m*n)**3
    return data,total


def main():
    data = smooth_witnesses()
    other = []
    for p,t in [(3,1),(3,2),(3,3),(5,2),(7,2)]:
        stages = t+1
        rings, fs, values = complex_data(stages,p)
        assert len(values)==3+(12*p+6)*stages and len(fs)==(9*p+3)*stages
        assert all(period(values,f)==0 for f in fs)
        cores = []
        for i in (t,t+1):
            matrix, ncols = chord_matrix(values,fs+[rings[i]])
            _, end, width = unit_core(matrix,ncols)
            assert width==1 and abs(end[0][0])==p**i and period(values,rings[i])==p**i
            cores.append(abs(end[0][0]))
        other.append({"p":p,"t":t,"integral_residuals":cores})
    mixed_rows,total = fiber_tests()
    marked = {}
    for modulus in (2,4,8,16):
        groups = [{(x,y) for x,y in product(range(modulus),repeat=2)
                   if (2*(x+sign*y))%modulus==0} for sign in (1,-1)]
        reductions = [{(x%(modulus//2),y%(modulus//2)) for x,y in grp} for grp in groups]
        marked[modulus] = {"cardinals":list(map(len,groups)),
                          "named_solutions_equal":groups[0]==groups[1],
                          "image_cardinals":list(map(len,reductions)),
                          "above_1_1": [sum((x%(modulus//2),y%(modulus//2))==(1,1)
                                           for x,y in grp) for grp in groups]}
    assert marked[4]["named_solutions_equal"] and marked[8]["above_1_1"]==[0,4]
    print(json.dumps({"simple_triangle_pairs":data,"odd_prime_pairs":other,"mixed_smith_census":mixed_rows,
                      "directly_examined_fine_vectors":total,"marked_rank_one_pair":marked},
                     indent=2,sort_keys=True))


if __name__=="__main__":
    main()
