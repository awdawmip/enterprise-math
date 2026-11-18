"""Reproduce split-prime counts and a fixed, public positive-core phase observation."""
import argparse
from collections import Counter
from dataclasses import asdict
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
import sys

P = 5


def step(z):
    a, b = z
    return 2*a-b, a+2*b


def iterate(z, t):
    for _ in range(t):
        z = step(z)
    return z


def gaussian_order(z, sign):
    a,b = z
    if not (a or b):
        raise ValueError("zero has no finite pair of branch orders")
    order = 0
    while (2*a+sign*b) % 5 == (2*b-sign*a) % 5 == 0:
        a,b = (2*a+sign*b)//5,(2*b-sign*a)//5
        order += 1
    return order


def reduced_denominator(z):
    a,b = z
    d = a*a+b*b
    return d//gcd(d,gcd(a*a-b*b,2*a*b))


def arithmetic():
    cases = 0
    attaining = 0
    pairs = [(a,b) for a in range(-10,11) for b in range(-10,11) if (a,b)!=(0,0)]
    for z in pairs:
        u,v = gaussian_order(z,1),gaussian_order(z,-1)
        d = reduced_denominator(z)
        assert d%2 and (u>=0 and v>=0)
        a,b = z
        A = (a*a-b*b)*d//(a*a+b*b)
        if d>1:
            assert gcd(A,d)==1
            B = pow(2*A,-1,d)
            assert abs((2*B*A)%(2*d)-d)==1
            attaining += 1
        for t in range(7):
            w = iterate(z,t)
            diff = abs(u-v+t)-abs(u-v)
            assert reduced_denominator(w)*5**max(0,-diff)==d*5**max(0,diff)
            assert (gaussian_order(w,1),gaussian_order(w,-1))==(u+t,v)
            assert gcd(*w)==gcd(*z)*5**min(t,max(0,v-u))
            cases += 1
    return {"signed_pairs":len(pairs),"pair_time_cases":cases,"sharp_margin_cases":attaining}


def root_minus_two(h):
    r,power = 3,5
    for _ in range(1,h):
        r = next(r+j*power for j in range(5) if ((r+j*power)**2+1)%(5*power)==0)
        power *= 5
    return r


def classes(h):
    modulus = 5**h
    yield from ((x,1) for x in range(modulus))
    yield from ((1,y) for y in range(0,modulus,5))


def canonical(x,y,h):
    modulus = 5**h
    if y%5:
        return x*pow(y,-1,modulus)%modulus,1
    return 1,y*pow(x,-1,modulus)%modulus


def finite_fibers(h,t):
    # Enumerate in ordinary axes, perform G in Z[i], then convert output to split axes.
    L = h+t
    iota = root_minus_two(h)
    counts = Counter()
    carry = Counter()
    for z in classes(L):
        a,b = iterate(z,t)
        k = 0
        while a%5 == b%5 == 0:
            a,b = a//5,b//5
            k += 1
        carry[k] += 1
        counts[canonical(a+iota*b,a-iota*b,h)] += 1
    assert set(counts)==set(classes(h))
    for (x,y),n in counts.items():
        if x == 0:
            expected = 5**(2*t) if t<h else 6*5**(h+t-1)-5**(2*h-1)
        else:
            j = 0
            while x%5 == 0:
                x //= 5
                j += 1
            expected = 5**(2*min(j,t))
        assert n == expected
    assert sum(counts.values())==6*5**(L-1)
    for j in range(1,t+1):
        assert sum(n for k,n in carry.items() if k>=j)==5**(L-j)
    return {"h":h,"t":t,"inputs":sum(counts.values()),"outputs":len(counts),
            "attracting_cell_fiber":counts[0,1],"number_of_outputs_by_fiber_size":dict(sorted(Counter(counts.values()).items())),
            "inputs_by_integer_carry":dict(sorted(carry.items()))}


def pinned_core(repo):
    base = repo/'src'/'enterprise_math'
    pins = {"brc_weighted_recurrent.py":"7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26",
            "exact_arithmetic.py":"f4f8feead82dc53a35e5fec495b31e46e64820f7b115c9efd6034063e68f8ad6",
            "core.py":"d2814d1d31eb195905f05136f250fcac2232b8cfc7dc6c9797000733ddebe636",
            "division.py":"4421c6dc9acfaa61492137951e543973c010c6a127655126152cc18763cc35e9"}
    for path,digest in pins.items():
        assert sha256((base/path).read_bytes()).hexdigest()==digest
    sys.path.insert(0,str(base.parent))
    from enterprise_math.brc_weighted_recurrent import recurrent_mass_power
    from enterprise_math.exact_arithmetic import division, brc_evaluate_division, compare_divisions
    powers = []
    def mass_power(name,matrix,t):
        mat = recurrent_mass_power(matrix,t)
        size = len(matrix)
        steps = t.bit_length()+t.bit_count()
        powers.append({"name":name,"order":size,"exponent":t,"matrix_products":steps,
                       "rational_multiplies":size**3*steps,"rational_accumulations":size**3*steps,
                       "max_output_entry_bits":max(x.numerator.bit_length() for row in mat for x in row)})
        return mat

    raw = (-2,1)
    matrix = [[2,0,1,0],[0,2,0,1],[0,1,2,0],[1,0,0,2]]
    signed_sources = [0,2,1,0]
    out = mass_power("G^2",matrix,2)
    rows = [[int(source*x) for x in row] for source,row in zip(signed_sources,out)]
    totals = list(map(sum,zip(*rows)))
    z = (totals[0]-totals[1],totals[2]-totals[3])
    assert z==iterate(raw,2)==(-10,-5)
    assert sum(totals)==3**2*sum(signed_sources)
    bilinear_receipts = []
    def observation(label,terms):
        d = len(terms)+3
        mat = [[0]*d for _ in range(d)]
        for j,(left,right,weight) in enumerate(terms,1):
            mat[0][j] = abs(left)
            negative = (left<0) ^ (right<0) ^ (weight<0)
            mat[j][d-1 if negative else d-2] = abs(right)*abs(weight)
        row = mass_power(label,mat,2)[0]
        endpoints = int(row[-2]),int(row[-1])
        value = endpoints[0]-endpoints[1]
        assert value==sum(l*r*w for l,r,w in terms)
        bilinear_receipts.append({"observer":label,"labeled_terms":terms,"endpoint_positive_negative":endpoints})
        return value
    a,b = z
    d = observation("norm",[(a,a,1),(b,b,1)])
    X = observation("real phase numerator",[(a,a,1),(b,b,-1)])
    Y = observation("imag phase numerator",[(a,b,2)])
    w = (1,1)
    delta = observation("oriented determinant",[(a,w[1],1),(b,w[0],-1)])
    d_other = observation("comparison norm",[(1,1,1),(1,1,1)])
    delta_square = observation("four determinant squares",[(delta,delta,4)])
    error_expr = division(delta_square,d*d_other)
    comparison = compare_divisions(error_expr,division(1,2))
    assert comparison==-1 and (X,Y,d)==(75,100,125)
    traces = []
    def half_open_bin(n,den):
        trace = brc_evaluate_division(division(abs(n),den))
        traces.append({"input_sign":(n>0)-(n<0),"trace":asdict(trace)})
        return trace.quotient if n>=0 else -trace.quotient-int(trace.remainder!=0)
    # A translated grid with boundary at 3/5; a nearby phase uses the left cell.
    exact_bin = half_open_bin(5*X-3*d,5*d)
    near = (19,10)
    D = near[0]**2+near[1]**2
    XX = near[0]**2-near[1]**2
    near_bin = half_open_bin(5*XX-3*D,5*D)
    assert (exact_bin,near_bin)==(0,-1)
    reference = (2,1)
    near_det = observation("nearby determinant",[(reference[0],near[1],1),(reference[1],near[0],-1)])
    eps = division(4*near_det**2,5*D)
    safe = compare_divisions(eps,division(1,400)) < 0
    grid_cases = [half_open_bin(4*X+d,2*d),half_open_bin(4*XX+D,2*D)]
    assert safe and grid_cases==[1,1]
    return {"public_source_sha256":pins,"origin":"synthetic signed integer pair (-2,1)",
            "G_edge_weights_in_order_a_plus_a_minus_b_plus_b_minus":matrix,
            "input_port_masses":signed_sources,"horizon":2,"origin_by_endpoint_masses":rows,
            "signed_output":z,"squared_amplitude":d,"unreduced_phase_observer":[X,Y,d],
            "comparison_input":w,"error_squared_literal":[delta_square,d*d_other],
            "comparison_to_half":comparison,"bilinear_witnesses":bilinear_receipts,
            "half_open_floors":[exact_bin,near_bin],"centered_mesh_checks":{"B":2,"cells":grid_cases,
            "chord_error_sq":[eps.numerator,eps.denominator],"strict_enough_for_margin_1_over_20":safe},
            "division_receipts":traces,
            "power_receipts":powers,"power_calls":len(powers),"cached_power_results_reused":0,
            "core_fraction_multiplications":sum(p["rational_multiplies"] for p in powers),
            "raw_bitlengths":{"source":max(abs(x).bit_length() for x in raw),
                              "signed_result":max(abs(x).bit_length() for x in z),
                              "phase_components_and_denominator":[x.bit_length() for x in (X,Y,d)]}}


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path)
    args = parser.parse_args()
    repos = [Path.cwd(),*Path(__file__).resolve().parents,Path('/workspace/enterprise-math')]
    repo = args.repo or next((p for p in repos if (p/'src/enterprise_math/exact_arithmetic.py').is_file()),None)
    if repo is None:
        parser.error("provide --repo pointing to the pinned public source checkout")
    report = {"gaussian_checks":arithmetic(),"fiber_checks":[finite_fibers(h,t) for h in range(1,5)
              for t in range(5) if h+t<=6],"public_api_replay":pinned_core(repo)}
    print(json.dumps(report,indent=2,ensure_ascii=False))
