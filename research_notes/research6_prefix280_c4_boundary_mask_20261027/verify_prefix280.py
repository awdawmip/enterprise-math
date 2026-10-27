"""PREFIX-280: exact C4 ordered-path-pair BRC, boundary-mask reconstruction.
This is an independent checker for the declared Stage50 path-pair semantics,
NOT an execution of the original Stage50 Source or a physical heartbeat step.
"""
from fractions import Fraction as Q
from itertools import product
import json

V = ((Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1)))
R = (1, 0, -1, 0)
Z0 = (Q(0), Q(0))

def add(x, y): return x[0]+y[0], x[1]+y[1]
def sub(x, y): return x[0]-y[0], x[1]-y[1]
def conj(x): return x[0], -x[1]
def mul(x, y): return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]
def by(x, k): return x[0]/k, x[1]/k

def divide(x, y):
    d = y[0]*y[0] + y[1]*y[1]
    assert d > 0
    return by(mul(x, conj(y)), d)

def packet(weights, phases):
    return {j: (Q(w), p % 4) for j, (w, p) in enumerate(zip(weights, phases)) if w}

def mass(f): return sum((w*w for w, _ in f.values()), Q(0))

def corr(f, r):
    val = Z0
    for j, (w, p) in f.items():
        if j+r in f:
            v, q = f[j+r]
            val = add(val, by(V[(p-q) % 4], 1/(w*v)))
    return val

def brc_external(f, r, p):
    """Ten external Stage50 ports: ordered path pairs at every SOURCE LABEL."""
    total = Q(0)
    for j in set(f) | {k+r for k in f}:
        paths = []
        if j in f: paths.append(f[j])
        if j-r in f:
            w, q = f[j-r]
            paths.append((w, (q+p+2) % 4))
        for w, q in paths:
            for v, t in paths:
                total += w*v*R[(t-q) % 4]
    return Q(10,36)*total/(2*mass(f))

def read_c(f, r):
    e0, e1 = brc_external(f, r, 0), brc_external(f, r, 1)
    c = (Q(1) - Q(18,5)*e0, Q(18,5)*e1 - Q(1))
    assert c == by(corr(f, r), mass(f))
    return c

def flip_zero(f):
    out = f.copy()
    if 0 in out:
        w,p = out[0]
        out[0] = (w,(p+2)%4)
    return out

def reconstruct(f, n):
    flipped = flip_zero(f)
    baseline = {r: read_c(f,r) for r in range(1,n)}
    changed = {r: read_c(flipped,r) for r in range(1,n)}
    u = {r: by(sub(baseline[r], changed[r]), Q(2)) for r in range(1,n)}
    d = sub(baseline[n-2],u[n-2])
    s = divide(mul(conj(u[1]),u[n-1]),d)
    assert s[1] == 0 and s[0] > 0
    assert s == (f[0][0]**2/mass(f),Q(0))
    ratios = {r: divide(conj(u[r]),s) for r in range(1,n)}
    w0,p0 = f[0]
    for r in range(1,n):
        wr,pr=f[r]
        expected=by(V[(pr-p0)%4], w0/wr)
        assert ratios[r] == expected, (r,ratios[r],expected)
    return s, ratios

def normdata(f,n):
    return [read_c(f,r) for r in range(1,n)]

def scan():
    packets = 0; readouts=0
    cohorts = {}
    for n, weights in ((3,(1,2,3)),(4,(1,2)),(5,(1,))):
        k=0
        for ws in product(weights, repeat=n):
            for ps in product(range(4),repeat=n):
                f=packet(ws,ps)
                reconstruct(f,n)
                packets+=1; k+=1
                readouts+=4*(n-1)
        cohorts[str(n)]={'packets':k,'stage50_brc_external_readouts':4*(n-1)*k}
    f = packet((1,4,4),(0,0,0)); g=packet((2,5,2),(0,0,0))
    assert normdata(f,3)==normdata(g,3)
    assert normdata(flip_zero(f),3) != normdata(flip_zero(g),3)
    sf,rf = reconstruct(f,3); sg,rg = reconstruct(g,3)
    assert sf[0]==Q(1,33) and sg[0]==Q(4,33)
    assert rf=={1:(Q(4),Q(0)),2:(Q(4),Q(0))}
    assert rg=={1:(Q(5,2),Q(0)),2:(Q(1),Q(0))}
    assert (brc_external(flip_zero(f),1,0),brc_external(flip_zero(g),1,0)) == (Q(35,198),Q(5,18))
    # Sharp n=2 failure even after the same boundary source flip.
    p = packet((1,2),(0,0)); q = packet((2,1),(0,0))
    assert normdata(p,2)==normdata(q,2)
    assert normdata(flip_zero(p),2)==normdata(flip_zero(q),2)
    # Sharp zero-interior failure for n=3.
    p=packet((1,0,2),(0,0,0)); q=packet((2,0,1),(0,0,0))
    assert normdata(p,3)==normdata(q,3)
    assert normdata(flip_zero(p),3)==normdata(flip_zero(q),3)
    result={
        'id':'PREFIX-280',
        'status':'EXACT_INDEPENDENT_C4_ORDERED_PATH_PAIR_CHECK_PASS',
        'source_kind':'independent verifier reproducing the declared Stage50 10-port BRC ordered source-pair observer; original Stage50 not imported here',
        'total_nonzero_packets':packets,
        'total_stage50_external_brc_readouts':readouts,
        'cohorts':cohorts,
        'prefix279_witness':{
            'f_ratios':['1','4','4'], 'g_ratios':['1','5/2','1'],
            'f_first_source_mass_fraction':'1/33',
            'g_first_source_mass_fraction':'4/33',
            'post_gate_E_1_0_f':'35/198', 'post_gate_E_1_0_g':'5/18',
            'post_gate_gap':'10/99'
        },
        'sharp_boundary':{'two_sources_nonunique':True,'zero_interior_three_sources_nonunique':True},
        'native_gate_legality':'UNVERIFIED',
        'physical_heartbeat_evolution':'UNVERIFIED'
    }
    print('PREFIX280_INDEPENDENT_C4_BRC_BOUNDARY_MASK_PASS',packets,readouts)
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
    return result

if __name__ == '__main__': scan()
