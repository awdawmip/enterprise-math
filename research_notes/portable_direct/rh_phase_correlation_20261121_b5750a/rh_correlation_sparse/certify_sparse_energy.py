#!/usr/bin/env python3
"""Strict positive-window certificates from sparse complete-road endpoints.

Only Python integer/Fraction arithmetic enters a certificate.  Logarithms use
an explicit atanh-series remainder.  Road endpoints and exact rational nodes
are imported from the same-author rational branch, with input hashes retained.
No earlier suite or complete-road coefficient population is recomputed here.
"""
from bisect import bisect_right
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, isqrt, prod
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
DIGITS = 70
S = 10**DIGITS
ZERO, ONE = (0, 0), (S, S)
LOG_TERMS = 80
CLIP_CAP = Q(1, 10**25)
COUNTS = {'log_evaluations': 0, 'log_series_terms': 0, 'positive_pieces': 0,
          'negative_pieces': 0, 'unresolved_tiny_pieces': 0,
          'integration_bisections': 0, 'maximum_integration_depth': 0,
          'new_coarse_cells_evaluated': 0}


def ceildiv(n, d):
    return -((-n)//d)


def iq(x):
    x = Q(x)
    return x.numerator*S//x.denominator, ceildiv(x.numerator*S, x.denominator)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def scale(x, q):
    q = Q(q)
    a, b = x if q >= 0 else (x[1], x[0])
    return a*q.numerator//q.denominator, ceildiv(b*q.numerator, q.denominator)


def mul(x, y):
    z = [a*b for a in x for b in y]
    return min(z)//S, ceildiv(max(z), S)


def square(x):
    a, b = x
    lo = 0 if a <= 0 <= b else min(a*a, b*b)
    hi = max(a*a, b*b)
    return lo//S, ceildiv(hi, S)


def power(x, n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n //= 2
    return out


def sqrt_interval(x):
    assert x[0] >= 0
    lo, hi = isqrt(x[0]*S), isqrt(x[1]*S)
    if hi*hi < x[1]*S:
        hi += 1
    return lo, hi


def intersect(x, y):
    z = max(x[0], y[0]), min(x[1], y[1])
    assert z[0] <= z[1]
    return z


def overlaps(x, y):
    return max(x[0], y[0]) <= min(x[1], y[1])


def from_json(x):
    return iq(Q(x['lower']))[0], iq(Q(x['upper']))[1]


def text_decimal(z, places):
    sign = '-' if z < 0 else ''
    s = str(abs(z)).rjust(places+1, '0')
    return sign+s[:-places]+'.'+s[-places:] if places else sign+s


def render(x, places=24):
    unit = 10**(DIGITS-places)
    return {'lower':text_decimal(x[0]//unit, places),
            'upper':text_decimal(ceildiv(x[1], unit), places),
            'internal_integer_bounds':[str(x[0]), str(x[1])],
            'denominator_power_of_10':DIGITS}


def atanh_log(z):
    assert Q(0) <= z <= Q(1, 3)
    zi = iq(z)
    zz = mul(zi, zi)
    term, total = zi, ZERO
    for k in range(LOG_TERMS):
        total = add(total, scale(term, Q(2, 2*k+1)))
        term = mul(term, zz)
    tail = Q(9, 4*(2*LOG_TERMS+1)*3**(2*LOG_TERMS+1))
    COUNTS['log_series_terms'] += LOG_TERMS
    return total[0], total[1]+iq(tail)[1]


LOG2 = atanh_log(Q(1, 3))


@lru_cache(None)
def logq(x):
    x = Q(x)
    assert x > 0
    if x == 1:
        return ZERO
    COUNTS['log_evaluations'] += 1
    k = x.numerator.bit_length()-x.denominator.bit_length()
    t = x/Q(2**k) if k >= 0 else x*2**(-k)
    while t < 1:
        t *= 2
        k -= 1
    while t >= 2:
        t /= 2
        k += 1
    return add(scale(LOG2, k), atanh_log((t-1)/(t+1)))


def primes_to(n):
    mark = bytearray(b'\1')*(n+1)
    mark[:2] = b'\0\0'
    for p in range(2, isqrt(n)+1):
        if mark[p]:
            start = p*p
            mark[start:n+1:p] = b'\0'*((n-start)//p+1)
    return [p for p in range(2, n+1) if mark[p]]


def reference_events(Y, Z):
    events = {}
    primes = primes_to(Z)
    for p in primes:
        n = p
        while n <= Z:
            if n > Y:
                events[n] = p
            n *= p
    return events, len(primes)


def value(d, b, x):
    return sub(scale(sub(d, logq(x)), x), b)


def primitive(d, b, x):
    # Integral of [y(d-log y)-b]^2/y^2.
    logx = logq(x)
    t = sub(d, logx)
    first = scale(add(add(square(t), scale(t, 2)), iq(2)), x)
    cross = scale(mul(mul(b, d), logx), -2)
    last = scale(square(b), -Q(1, x))
    return add(add(first, cross), add(mul(b, square(logx)), last))


def exact_positive_energy(d, b, left, right, depth=0):
    """Classify by concavity; enclose unresolved root pieces by a rational cap."""
    COUNTS['maximum_integration_depth'] = max(COUNTS['maximum_integration_depth'], depth)
    l, r = Q(left), Q(right)
    fl, fr = value(d, b, l), value(d, b, r)
    if fl[0] >= 0 and fr[0] >= 0:
        COUNTS['positive_pieces'] += 1
        out = sub(primitive(d, b, r), primitive(d, b, l))
        assert out[1] >= 0
        return (max(0, out[0]), out[1]), ZERO
    cap = max(Q(fl[1], S), Q(fr[1], S))+Q((r-l)**2, 8*l)
    if cap <= 0:
        COUNTS['negative_pieces'] += 1
        return ZERO, ZERO
    cap_energy = cap*cap*(1/l-1/r)
    if cap_energy <= CLIP_CAP or depth >= 70:
        COUNTS['unresolved_tiny_pieces'] += 1
        upper = iq(cap_energy)[1]
        return (0, upper), (0, upper)
    COUNTS['integration_bisections'] += 1
    middle = (l+r)/2
    first, rem1 = exact_positive_energy(d, b, l, middle, depth+1)
    second, rem2 = exact_positive_energy(d, b, middle, r, depth+1)
    return add(first, second), add(rem1, rem2)


def linear_positive_energy(a, b, u, v):
    a, b, l, r = Q(a), Q(b), Q(u), Q(v)
    if not a:
        return iq(max(b, 0)**2*(1/l-1/r))
    root = -b/a
    if a > 0:
        l = max(l, root)
    else:
        r = min(r, root)
    if l >= r:
        return ZERO
    return add(iq(a*a*(r-l)+b*b*(1/l-1/r)), scale(sub(logq(r), logq(l)), 2*a*b))


class Certificate:
    def __init__(self, source, additions):
        self.source = source
        self.Y, self.Z = source['window']['Y'], source['window']['Z']
        assert self.Y**3 == self.Z**2 and source['window']['theta'] in ('1/2', '0.5')
        self.m = source['m']
        c = source['node_certificate']
        nodes = [Q(x) for x in c['nodes']]
        weights = [Q(x) for x in c['weights']]
        assert len(nodes) == self.m and len(set(nodes)) == self.m and min(nodes) > 0
        assert sum(weights) == 1
        for k in range(1, self.m):
            assert sum(w*a**k for w, a in zip(weights, nodes)) == 0
        self.C = Q(c['derivative_error_coefficient_exact'])
        assert self.C == prod(nodes)/factorial(self.m+1)
        self.P = (sum(abs(w) for w in weights)+1)/2
        self.records = {e['N']:e for e in source['endpoints']}
        for j in additions:
            e = j['endpoint']
            self.records[e['N']] = e
        self.qhat, self.sigma = {}, {}
        gamma = from_json(source['gamma'])
        for n, e in self.records.items():
            f = from_json(e['F'])
            self.qhat[n] = Q(f[0]+f[1], 2*S)
            self.sigma[n] = Q(f[1]-f[0], 2*S)
            A = from_json(e['A_D_excluding_unit'])
            B = from_json(e['B_D_excluding_unit'])
            reconstructed = sub(scale(sub(add(add(A, ONE), gamma), logq(Q(n))), n), B)
            assert overlaps(reconstructed, f)
        self.events, self.prime_count = reference_events(self.Y, self.Z)
        self.event_points = sorted(self.events)
        self.cells = {}
        self.eta_cache = {}

    def eta(self, v):
        if v not in self.eta_cache:
            self.eta_cache[v] = Q(scale(power(logq(Q(v)), self.m+1), self.C)[1], S)
        return self.eta_cache[v]

    def lambda_interval(self, n):
        p = self.events.get(n)
        return logq(Q(p)) if p else ZERO

    def cell(self, u, v):
        key = u, v
        if key in self.cells:
            return self.cells[key]
        COUNTS['new_coarse_cells_evaluated'] += 1
        inside = self.event_points[bisect_right(self.event_points, u):bisect_right(self.event_points, v-1)]
        Atot, Btot = ZERO, ZERO
        for n in inside:
            lam = self.lambda_interval(n)
            Atot = add(Atot, scale(lam, Q(1, n)))
            Btot = add(Btot, lam)
        V = sub(scale(Atot, v), Btot)
        gap = v-u
        a = (self.qhat[v]-self.qhat[u])/gap
        b = self.qhat[u]-a*u
        ac = scale(sub(scale(logq(Q(v)), v), scale(logq(Q(u)), u)), Q(1, gap))
        bc = scale(sub(logq(Q(u)), logq(Q(v))), Q(u*v, gap))
        d0 = sub(add(iq(a), ac), scale(V, Q(1, gap)))
        b0 = sub(sub(iq(-b), bc), scale(V, Q(u, gap)))
        assert value(d0, b0, Q(u))[0] <= iq(self.qhat[u])[0] <= value(d0, b0, Q(u))[1]
        energy, clip_remainder = ZERO, ZERO
        Aloc, Bloc = ZERO, ZERO
        cuts = [u]+inside+[v]
        for left, right in zip(cuts, cuts[1:]):
            d, bb = add(d0, Aloc), add(b0, Bloc)
            e, rem = exact_positive_energy(d, bb, Q(left), Q(right))
            energy, clip_remainder = add(energy, e), add(clip_remainder, rem)
            if right < v:
                lam = self.lambda_interval(right)
                Aloc = add(Aloc, scale(lam, Q(1, right)))
                Bloc = add(Bloc, lam)
        last_value = value(add(d0, Aloc), add(b0, Bloc), Q(v))
        assert last_value[0] <= iq(self.qhat[v])[0] <= last_value[1]
        local_eta = self.eta(v)
        geometry = Q(gap**5, 120*u**4) if gap > 1 else Q(0)
        # Both source moments, including n=v (its Green kernel is zero).
        Aval, Bval = Atot, Btot
        if v in self.events:
            lv = self.lambda_interval(v)
            Aval, Bval = add(Aval, scale(lv, Q(1, v))), add(Bval, lv)
        r0 = sub(sub(from_json(self.records[v]['A_D_excluding_unit']),
                     from_json(self.records[u]['A_D_excluding_unit'])), Aval)
        r1 = sub(sub(from_json(self.records[v]['B_D_excluding_unit']),
                     from_json(self.records[u]['B_D_excluding_unit'])), Bval)
        out = {'u':u, 'v':v, 'event_count':len(inside), 'd0':d0, 'b0':b0,
               'energy':energy, 'clip_remainder':clip_remainder,
               'linear_energy':linear_positive_energy(a, b, u, v),
               'eta':local_eta, 'geometry':geometry,
               'budget_sq':local_eta*local_eta*geometry,
               'residual_moment_0':r0, 'residual_moment_1':r1}
        self.cells[key] = out
        return out

    def model_at(self, u, v, y):
        cell = self.cell(u, v)
        d, b = cell['d0'], cell['b0']
        for n in self.event_points[bisect_right(self.event_points, u):bisect_right(self.event_points, y)]:
            if n >= v:
                break
            lam = self.lambda_interval(n)
            d, b = add(d, scale(lam, Q(1, n))), add(b, lam)
        return value(d, b, Q(y))

    def stage(self, nodes, title):
        pieces = [self.cell(u, v) for u, v in zip(nodes, nodes[1:])]
        Emod, Elin, clip = ZERO, ZERO, ZERO
        for c in pieces:
            Emod, Elin, clip = add(Emod, c['energy']), add(Elin, c['linear_energy']), add(clip, c['clip_remainder'])
        r2 = sum((c['budget_sq'] for c in pieces), Q(0))
        geometry = sum((c['geometry'] for c in pieces), Q(0))
        sigma = max(self.sigma[n] for n in nodes)
        e_read = scale(sqrt_interval(iq(Q(1, self.Y)-Q(1, self.Z))), sigma)
        e_shape = sqrt_interval(iq(r2))
        eps = add(e_read, e_shape)
        norm = sqrt_interval(Emod)
        lower_norm = max(0, norm[0]-eps[1])
        upper_norm = norm[1]+eps[1]
        Fenergy = lower_norm*lower_norm//S, ceildiv(upper_norm*upper_norm, S)
        ranked = sorted(pieces, key=lambda c:c['budget_sq'], reverse=True)
        global_budget = scale(sqrt_interval(iq(geometry)), self.eta(self.Z))
        return {'name':title, 'nodes':nodes, 'road_readout_count':len(nodes),
                'model_positive_energy':render(Emod), 'linear_positive_energy':render(Elin),
                'full_road_positive_energy':render(Fenergy),
                'shape_error_norm':render(e_shape, 30), 'endpoint_error_norm':render(e_read, 45),
                'total_norm_error':render(eps, 30),
                'global_eta_shape_bound':render(global_budget, 30),
                'unresolved_root_energy_upper':render(clip, 35),
                'shape_error_squared_exact':str(r2), 'gamma_squared_exact':str(geometry),
                'largest_local_budget_cell':[ranked[0]['u'],ranked[0]['v']],
                'cells':[{'u':c['u'],'v':c['v'],'events':c['event_count'],
                          'eta_upper_exact':str(c['eta']), 'budget_squared_exact':str(c['budget_sq']),
                          'residual_moment_0':render(c['residual_moment_0'],30),
                          'residual_moment_1':render(c['residual_moment_1'],30)} for c in pieces],
                '_Fenergy':Fenergy}


def moment_obstruction():
    u, r = 100, 3
    h, v = 4*r+2, u+4*r+2
    eta = Q(1, 100)
    c = eta/v
    x = {}
    for j in range(1, r+1):
        x[u+j] = c
        x[v-j] = c
    for j in range(r+1, 2*r+1):
        x[u+j] = -c
        x[v-j] = -c
    x[u+2*r+1] = Q(0)
    assert sum(x.values()) == 0
    assert sum(n*a for n,a in x.items()) == 0
    assert all(abs(n*a) <= eta for n,a in x.items())
    mid = Q(u+v, 2)
    response = sum(a*max(mid-n, 0) for n,a in x.items())
    assert response == c*r*r > 0
    return {'evidence':'exact Fraction arithmetic', 'u':u, 'v':v, 'r':r,
            'eta':str(eta), 'zeroth_source_moment':'0', 'first_source_moment':'0',
            'midpoint_response':str(response), 'source_e_n':{str(n):str(n*a) for n,a in sorted(x.items())}}


def main():
    names = ['inputs_window.json', 'inputs_split_global.json', 'inputs_split_local.json']
    inputs = [json.loads((ROOT/name).read_text()) for name in names]
    source, extra1, extra2 = inputs
    cert = Certificate(source, [extra1, extra2])
    base_nodes = sorted(e['N'] for e in source['endpoints'])
    stages = []
    stage1 = cert.stage(base_nodes, 'TEN_ROAD_ENDPOINTS')
    stages.append(stage1)
    first = extra1['endpoint']['N']
    global_cells = [(Q((v-u)**5,120*u**4),u,v) for u,v in zip(base_nodes,base_nodes[1:])]
    _, gu, gv = max(global_cells)
    assert first == (gu+gv)//2
    model1 = cert.model_at(gu,gv,first)
    defect1 = sub(from_json(extra1['endpoint']['F']), model1)
    nodes2 = sorted(base_nodes+[first])
    stages.append(cert.stage(nodes2, 'ELEVEN_AFTER_GLOBAL_BUDGET_SPLIT'))
    second = extra2['endpoint']['N']
    lu, lv = stages[-1]['largest_local_budget_cell']
    assert second == (lu+lv)//2
    model2 = cert.model_at(lu,lv,second)
    defect2 = sub(from_json(extra2['endpoint']['F']), model2)
    nodes3 = sorted(nodes2+[second])
    stages.append(cert.stage(nodes3, 'TWELVE_AFTER_LOCAL_BUDGET_SPLIT'))
    energy_intersection = stages[0]['_Fenergy']
    for stage in stages:
        energy_intersection = intersect(energy_intersection, stage['_Fenergy'])
        del stage['_Fenergy']
    assert 20000*(energy_intersection[1]-energy_intersection[0]) < energy_intersection[0]
    refinement_checks = []
    for u, v, midpoint, defect in [(gu,gv,first,defect1),(lu,lv,second,defect2)]:
        parent = cert.cell(u,v)
        child_budget = cert.cell(u,midpoint)['budget_sq']+cert.cell(midpoint,v)['budget_sq']
        assert child_budget*81 <= parent['budget_sq']*11
        endpoint_radius = ((v-midpoint)*cert.sigma[u]+(midpoint-u)*cert.sigma[v])/(v-u)
        point_budget = endpoint_radius+parent['eta']*Q((midpoint-u)*(v-midpoint),2*u)
        assert max(abs(defect[0]),abs(defect[1])) <= iq(point_budget)[1]
        refinement_checks.append({'parent':[u,v], 'new_point':midpoint,
                                  'child_to_parent_budget_ratio_exact':str(child_budget/parent['budget_sq']),
                                  'ratio_is_at_most':'11/81',
                                  'point_error_envelope':render(iq(point_budget),30)})
    # Earlier coefficient-only quartic bound, evaluated on this same window.
    k = 1
    while (k+1)**4 <= cert.Y:
        k += 1
    bq = Q((k+1)**4-k**4,k**3)
    cq = bq*bq/8
    aq = add(ONE,scale(logq(Q(k+1,k)),4*cert.P))
    az, ay = add(aq,scale(logq(Q(cert.Z)),cert.P)), add(aq,scale(logq(Q(cert.Y)),cert.P))
    old_eps_sq = scale(sub(power(az,3),power(ay,3)),cq*cq/(3*cert.P))
    old_eps = sqrt_interval(old_eps_sq)
    def log_square_integral_primitive(x):
        lx = logq(Q(x))
        return scale(add(sub(square(lx),scale(lx,2)),iq(2)),x)
    full_history_budget = scale(sqrt_interval(sub(log_square_integral_primitive(cert.Z),
                                                 log_square_integral_primitive(cert.Y))),cert.eta(cert.Z))
    report = {'status':'EXACT_SPARSE_POSITIVE_WINDOW_CERTIFICATE_PASSED',
              'window':source['window'], 'm':cert.m,
              'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names},
              'reference':'Lambda events with full -y log y curvature; affine gamma cancels only inside the model construction',
              'model':'M=linear(sparse real-road midpoint values)+G-linear(G)',
              'global_eta_upper_rederived':render(iq(cert.eta(cert.Z)),30),
              'old_coefficient_only_quartic_norm_bound_same_window':render(old_eps,20),
              'global_F_minus_G_norm_bound_from_uniform_eta':render(full_history_budget,30),
              'stages':stages,
              'intersection_of_all_strict_energy_enclosures':render(energy_intersection),
              'relative_energy_interval_width_less_than':'1/20000',
              'refinement_checks':refinement_checks,
              'new_road_midpoint_defects':[{'N':first,'parent_cell':[gu,gv],'F_minus_parent_model':render(defect1,30)},
                                         {'N':second,'parent_cell':[lu,lv],'F_minus_parent_model':render(defect2,30)}],
              'moment_interface_obstruction':moment_obstruction(),
              'accounting':{'road_endpoint_queries_total':len(nodes3),
                            'additional_road_queries':2,'road_data_recomputed_in_this_script':False,
                            'road_producer_jobs':[{'input':name,'counts':j['counts']} for name,j in zip(names,inputs)],
                            'producer_prefix_rebuilds':3,
                            'reference_sieve_through':cert.Z,'reference_prime_count':cert.prime_count,
                            'reference_prime_power_events_in_window':len(cert.events),
                            'cached_reference_and_rational_logs':logq.cache_info().currsize,
                            **COUNTS},
              'arithmetic':{'type':'fixed-denominator integer intervals plus exact Fraction',
                            'decimal_places':DIGITS,'atanh_terms':LOG_TERMS,
                            'root_region_cap_per_leaf_exact':str(CLIP_CAP),
                            'floating_point_used_in_certificate':False},
              'scope':['All complete-road endpoints and per-thickness ports remain in input files.',
                       'One finite complete power window; no arbitrarily distant energy estimate is asserted.',
                       'Reference Lambda sieve/log cost is separate from sparse full-road query cost.',
                       'All sign-crossing intervals are certified or retained with explicit positive-energy caps.',
                       'The zero-moment obstruction applies to the coefficient interface, not claimed realization by a true thickness family.']}
    (ROOT/'sparse_energy_certificate.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','global_eta_upper_rederived','old_coefficient_only_quartic_norm_bound_same_window',
                      'intersection_of_all_strict_energy_enclosures','accounting']},ensure_ascii=False,indent=2))
    for stage in stages:
        print(json.dumps({k:stage[k] for k in ['name','road_readout_count','model_positive_energy',
                          'full_road_positive_energy','shape_error_norm','largest_local_budget_cell']},ensure_ascii=False))


if __name__ == '__main__':
    main()
