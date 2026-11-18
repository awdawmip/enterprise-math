"""Independent two-grid residue/conditioning certificate at the frozen point.

Python 3.9+, standard library. Prints deterministic JSON, takes no inputs.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import accumulate, combinations
from math import comb, factorial, lcm, prod
import json


# Frozen data only for comparison at the end, never used in the kernel.
REFERENCE = F(
    100454427319989359659675407249135963526743900641273413214381415517253467584636104454350195238109256121339236245579864218040465440626509530269928562560758777677250236910281952986607655841943587052450086298496138478525112520994988083,
    13140271679761329808693806198578520565468656355215406498553427120699472323920753431915927405790028294878383495815200372403970181275238295968486314565597441855882972350550271674440611120068911346780150169600000000000000,
)


def value_derivative(roots, x):
    value, derivative = 1, 0
    for root in roots:
        derivative = derivative * (x - root) + value
        value *= x - root
    return value, derivative


def choose_precision(kappa):
    bits = 0
    while 2**bits <= kappa:
        bits += 1
    return bits


def trace_kernel(m, r, nodes):
    theta = tuple(F(i, m) for i in range(1, m + 1))

    @lru_cache(maxsize=None)
    def samples(t, x):
        v, dv = value_derivative(theta, x)
        p, dp = value_derivative(range(-t-m+1, -t+1), x)
        return v, dv, p-v, dp-dv

    def bezout(t, x, y):
        vx, dv, rx, dr = samples(t, x)
        vy, _, ry, _ = samples(t, y)
        numerator = (vx*ry-rx*vy)/(x-y) if x != y else dv*rx-dr*vx
        lead = F(2*m*t+m*m+1, 2)
        return numerator - rx*ry/lead

    step = [(-1)**j * sum(F(comb(k, j), 2**k) for k in range(j, m-1))
            for j in range(m-1)]
    # The transfer is inverse to averaging f(x) and f(x+m) on degrees <=m-2.
    assert all(sum(c*((j*m)**d+((j+1)*m)**d) for j,c in enumerate(step))
               == 2*int(d == 0) for d in range(m-1))
    values = []
    for x in nodes:
        shifted = [x+m*j for j in range(m-1)]
        late = sum((1 if j == k else 2)*step[j]*step[k]*bezout(r+m, shifted[j], shifted[k])
                   for j in range(m-1) for k in range(j+1))
        values.append(late-bezout(r, x, x))
    return values


def exact_norm(m, nodes, weights):
    # Common integer abscissae and integer mass numerators speed up the finite LP.
    scale = lcm(*(z.denominator for z in nodes))
    x = [int(z*scale) for z in nodes]
    target = [int(i<m) for i in range(2*m)]
    denominator = lcm(*(w.denominator for w in weights))
    w = [int(a*denominator) for a in weights]
    best_cost = sum(w[:m])
    best_den = 1
    best_labels = [m, m+1, m+2]
    vertices = {0, 1}
    best_coeff = (0,0,0,1)
    for triple in combinations(range(2*m), 3):
        g = [i for i in triple if target[i] == 1]
        h = [i for i in triple if target[i] == 0]
        if not g or not h:
            continue
        a,b = g if len(g) == 2 else h
        c = (h if len(g) == 2 else g)[0]
        s,t = target[a],target[c]
        d = (x[c]-x[a])*(x[c]-x[b])
        # H(X) = -s + (s-t)(X-Xa)(X-Xb)/d, with X the scaled abscissa.
        cost = sum(ww*abs((f-s)*d+(s-t)*(xx-x[a])*(xx-x[b]))
                   for ww,f,xx in zip(w,target,x))
        vertices.add(triple)
        if cost*best_den < best_cost*abs(d):
            best_cost,best_den = cost,abs(d)
            best_labels = list(triple)
            best_coeff = ((s-t)*x[a]*x[b]-s*d,-(s-t)*(x[a]+x[b]),s-t,d)
    # The other plateau vertex H=-1 may be optimal.
    if sum(w[m:])*best_den < best_cost:
        best_cost,best_den = sum(w[m:]),1
        best_labels = [0,1,2]
        best_coeff = (-1,0,0,1)
    h0,h1,h2,hd = best_coeff
    return (F(best_cost, best_den*denominator), best_labels, len(vertices),
            [F(h0,hd), F(scale*h1,hd), F(scale*scale*h2,hd)])


def derivative_certificate(m, r, poles, ordinates):
    n = m-1
    gamma = [(-1)**(k+n)*z/(factorial(k)*factorial(n-k))
             for k,z in enumerate(ordinates)]
    left,right = F(1,m),F(1)
    def summands(order, x):
        return [c/(x-y)**(m+order) for c,y in zip(gamma,poles)]
    def sign(v):
        return int(v>0)-int(v<0)
    def signs_at(x):
        return [sign(sum(summands(order,x))) for order in range(48)]
    def ranges(signs):
        out = []
        for j, v in enumerate(signs):
            if not out or v!=out[-1][2]:
                out.append([j,j,v])
            else:
                out[-1][1]=j
        return out
    left_sign,right_sign = signs_at(left),signs_at(right)
    assert left_sign == [1]*36+[-1]*12
    assert right_sign == [1]*40+[-1]*8
    limit47 = list(accumulate(summands(47,right)))
    limit46 = list(accumulate(summands(46,right)))
    assert all(x<0 for x in limit47)
    assert [k for k,x in enumerate(limit46) if x>=0] == [1]
    roots = {}
    for order in range(36,40):
        low,high = 66,1000
        while high-low>1:
            mid = (low+high)//2
            if sum(summands(order,F(mid,1000)))>0:
                high = mid
            else:
                low = mid
        a,b = F(low,1000),F(high,1000)
        assert left<a<b<=right
        assert sum(summands(order,a))<0<sum(summands(order,b))
        roots[str(order)] = [str(a),str(b)]
    # A uniform lower bound for F0 is F0(1), since F1 is positive by descent.
    return {"definition":"F_q=(-1)^q f^(14+q)/(14+q)!",
            "left_endpoint_sign_runs_through_47":ranges(left_sign),
            "right_endpoint_sign_runs_through_47":ranges(right_sign),
            "Abel_prefix_signs_at_right_q47":[sign(v) for v in limit47],
            "Abel_q46_nonnegative_prefix_last_zero_based":[k for k,x in enumerate(limit46) if x>=0],
            "simple_zero_intervals":roots,
            "F0_left":str(sum(summands(0,left))),"F0_right":str(sum(summands(0,right))),
            "integer_bounds_for_F0":[int(sum(summands(0,right))),int(-(-sum(summands(0,left))//1))]}


def certificate():
    m,r = 15,15
    nodes = [F(i,m) for i in range(1,m+1)] + [F(-r-i) for i in range(m)]
    values = trace_kernel(m, r, nodes)
    deriv = [prod(x-y for y in nodes if x!=y) for x in nodes]
    n = 2*m
    # Lagrange duality, first nonzero degree, plus all three actual parity checks.
    combined = lambda ys: sum(y/d for y,d in zip(ys,deriv))
    assert all(combined([x**j for x in nodes]) == int(j == n-1) for j in range(n))
    assert all(combined([v*x**j for v,x in zip(values,nodes)]) == 0 for j in range(3))
    theta_trace = sum(v/d for v,d in zip(values[:m],deriv[:m]))
    pole_trace = -sum(v/d for v,d in zip(values[m:],deriv[m:]))
    assert theta_trace == pole_trace == REFERENCE
    assert all(v != 0 for v in values)
    weights = [abs(v/d) for v,d in zip(values,deriv)]
    optimum,labels,nvertices,poly = exact_norm(m,nodes,weights)
    h = [sum(a*x**j for j,a in enumerate(poly)) for x in nodes]
    observer = [(int(i<m)+hh)/d for i,(hh,d) in enumerate(zip(h,deriv))]
    assert sum(c*v for c,v in zip(observer,values)) == theta_trace
    assert sum(abs(c*v) for c,v in zip(observer,values)) == optimum
    assert all(observer[i] == 0 for i in labels)
    # A primal witness proves the lower bound even without the exhaustive vertex check.
    # At poles the signs maximize the pole observer. Three theta entries cancel
    # its three syndromes; other theta entries are zero. Lagrange degree two.
    assert poly == [-1, 0, 0]
    correction = [0, (m-1)//2, m-1]
    extreme = [F(0)]*m + [(1 if d<0 else -1)*abs(z) for d,z in zip(deriv[m:],values[m:])]
    for i in correction:
        mass = -sum(extreme[j]/deriv[j] * prod((nodes[j]-nodes[k])/(nodes[i]-nodes[k])
                        for k in correction if k!=i) for j in range(m,n))
        extreme[i] = deriv[i] * mass
    assert all(abs(e) <= abs(v) for e,v in zip(extreme,values))
    assert all(combined([e*x**j for e,x in zip(extreme,nodes)]) == 0 for j in range(3))
    assert sum(v/d for v,d in zip(extreme[:m],deriv[:m])) == optimum
    def pack(value):
        k = value/abs(theta_trace)
        return {"relative_condition": str(k), "condition_approx": format(float(k),".10g"),
                "strict_positive_bits": choose_precision(k)}
    actual_bits = choose_precision(optimum/abs(theta_trace))
    margin = 1-optimum/(abs(theta_trace)*2**actual_bits)
    return {"m":m,"S":0,"a":1,"c":1,"trace_minus_14":str(theta_trace),
            "alternate_derivatives":derivative_certificate(m,r,nodes[m:],values[m:]),
            "degrees_checked": [0,n-1], "kernel_checksums_vanish_for_powers": [0,1,2],
            "separate_theta":pack(sum(weights[:m])), "separate_poles":pack(sum(weights[m:])),
            "combined":pack(optimum),"distinct_quadratic_vertices":nvertices,
            "observer_vanishes_at":[str(nodes[i]) for i,c in enumerate(observer) if c == 0],
            "optimal_H_ascending":[str(p) for p in poly],
            "primal_witness_theta_nonzero_ratios":{str(nodes[i]):str(extreme[i]/abs(values[i])) for i in correction},
            "relative_positive_margin_at_optimal_bits":str(margin),
            "residue_summands_by_sign":{
                "theta_positive":sum(v/d>0 for v,d in zip(values[:m],deriv[:m])),
                "pole_positive":sum(-v/d>0 for v,d in zip(values[m:],deriv[m:]))}}


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2, ensure_ascii=False))
