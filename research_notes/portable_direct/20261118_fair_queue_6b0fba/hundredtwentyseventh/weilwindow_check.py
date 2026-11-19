"""Certified small matrices for the moving Li response head. Requires python-flint."""
import argparse
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx

ctx.prec = 128
LI_SHA = "ff635e2e070d442ba5b48b20a29a1a908942254887d46bacca77d9cd551f3e8d"
PI = arb.pi()


def enclosure(low, high=None, digits=6):
    """Integers are bounds after multiplication by 10**digits."""
    high = low if high is None else high
    scale = 10**digits
    lo = int((low.lower()*scale).lower().floor().unique_fmpz())
    hi = int((high.upper()*scale).upper().ceil().unique_fmpz())
    assert arb(lo) / scale <= low and arb(hi) / scale >= high
    return [lo, hi]


def positive_root_bounds(A):
    # Floats only suggest a positive vector. Arb alone certifies the inequalities.
    numeric = [[float(x.mid()) for x in row] for row in A]
    v = [1.0]*len(A)
    for _ in range(16):
        v = [sum(c*e for c,e in zip(row,v)) for row in numeric]
        peak = max(v)
        v = [x/peak for x in v]
    test = [max(1,round(x * 10**10)) for x in v]
    ratios = [sum(c*w for c,w in zip(row,test))/vi for row,vi in zip(A,test)]
    return min(x.lower() for x in ratios), max(x.upper() for x in ratios)


def triangle(diagonal, divided):
    n = len(diagonal)
    A = [[arb(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i] = diagonal[i]
        for j in range(i):
            A[i][j] = A[j][i] = divided(i,j)
    return A


def raw_head(L, eps, J, m):
    a = arb(J)+arb(1)/4
    k = [(arb(q)+(arb(1)/2 if eps<0 else 0))*PI/L for q in range(m)]
    b = [(arb(1 if q==0 and eps>0 else 2)/L).sqrt() for q in range(m)]
    U, diag = [], []
    for q,x in enumerate(k):
        z = acb(a,x/2)
        dp = z.digamma().imag
        U.append(x*dp/2)
        diag.append((z.polygamma(1).real/4 if q==0 and eps>0 else
                     dp/(4*x)+z.polygamma(1).real/8)*b[q]**2)
    A = triangle(diag,lambda i,j: b[i]*b[j]*(U[i]-U[j])/(k[i]**2-k[j]**2))
    mirror = (-2*L*(2*J+arb(1)/2)).exp()
    factors = ((1-mirror,arb(1)) if eps>0 else (arb(1),1+mirror))
    lo,hi = positive_root_bounds(A)
    trace = sum(diag)
    # Independently sum the ORIGINAL mirror-corrected responses. The infinite
    # positive tail uses the decreasing integral bounds on sum c_j^(-2).
    H = J+512
    cH = 2*H+arb(1)/2
    comparisons = 0
    for i,j in ((0,0),(0,m-1),(m-1,m-1)):
        total = arb(0)
        for e in range(J,H):
            c = 2*e+arb(1)/2
            total += (1-eps*(-2*L*c).exp())*c**2/((c*c+k[i]**2)*(c*c+k[j]**2))
        zH = (-2*L*cH).exp()
        tail_low = ((1-zH)/(2*cH)
                    /((1+(k[i]/cH)**2)*(1+(k[j]/cH)**2)))
        tail_high = (1+zH)*(1/(2*cH)+1/cH**2)
        direct_low = (total+tail_low)*b[i]*b[j]
        direct_high = (total+tail_high)*b[i]*b[j]
        assert direct_low <= A[i][j]*factors[0] and A[i][j]*factors[1] <= direct_high
        comparisons += 1
    B = PI*(m-(arb(1)/2 if eps>0 else 0))/(2*L*J)
    trace_cont = trace_kernel(B)
    return dict(J=J,m=m,parity="even" if eps>0 else "odd",B=enclosure(B),
                spectral_norm=enclosure(lo*factors[0],hi*factors[1]),
                trace=enclosure(trace*factors[0],trace*factors[1]),
                limit_trace_at_its_own_B=enclosure(trace_cont),
                trace_displacement=enclosure(trace*factors[0]-trace_cont,
                                              trace*factors[1]-trace_cont),
                source_dot_products_cross_checked=comparisons)


def trace_kernel(B):
    return (acb(0,B).polylog(2).imag+B.atan())/(2*PI)


def continuous(L, alpha_num, alpha_den, cells=128):
    B = PI*alpha_num/(2*L*alpha_den)
    width = B/cells
    norms, traces = [], []
    for side in (0,1):
        nodes = [(i+side)*width for i in range(cells)]
        v = [x*x.atan() for x in nodes]
        ds = [width/(2*PI)*((arb(1) if i==0 and side==0 else x.atan()/x)
                             + 1/(1+x*x)) for i,x in enumerate(nodes)]
        A = triangle(ds,lambda i,j: width/PI*(v[i]-v[j])/(nodes[i]**2-nodes[j]**2))
        norms.append(positive_root_bounds(A))
        traces.append(sum(ds))
    # The kernel decreases in each argument; positive Perron comparisons bound norm.
    integral = trace_kernel(B)
    assert traces[1] < integral < traces[0]
    return dict(m_over_J=[alpha_num,alpha_den], cells=cells, B=enclosure(B),
                norm=enclosure(norms[1][0],norms[0][1]), trace=enclosure(integral))


def origin_response_integral(L, eps, J, q, slices=2048):
    # Directly integrate Li (3.1) times the signed original trigonometric mode.
    # Each subinterval of x/L has an outward interval range, including end points.
    c = 2*J+arb(1)/2
    ell = arb(1)/slices
    k = (q+(arb(1)/2 if eps<0 else 0))*PI/L
    b = (arb(1 if q==0 and eps>0 else 2)/L).sqrt()
    s = arb(0)
    for w in range(slices):
        y=(arb(2*w+1,1)/(2*slices))
        arg = k*L*y
        shape = arg.cos() if eps>0 else arg.sin()
        s+= shape*((-c*L*(1-y)).exp()+eps*(-c*L*(1+y)).exp())
    det = 1-eps*(-2*c*L).exp()
    s *= b*L*ell/det.sqrt()
    exact = (-1)**q * b*det.sqrt()*c/(c*c+k*k)
    assert s.contains(exact)
    return enclosure(exact)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--li-source",type=Path)
    a=p.parse_args()
    if a.li_source:
        assert hashlib.sha256(a.li_source.read_bytes()).hexdigest()==LI_SHA
    result = {}
    for label,L in (("4/5",arb(4)/5),("log(5)/2",arb(5).log()/2)):
        result[label] = dict(
            continuous=[continuous(L,n,d) for n,d in ((1,8),(1,1),(4,1))],
            true_compressions=[raw_head(L,e,J,m) for J,m in
                               ((8,8),(8,32),(32,32),(32,128),(64,8))
                               for e in (1,-1)],
            source_quadratures=[dict(J=8,q=q,eps=e,exact_dot=origin_response_integral(L,e,8,q))
                                for q in (0,3) for e in (1,-1)])
    print(json.dumps(dict(source_v2_sha256=LI_SHA,endpoint_cases=result,
                  numerical_enclosures="pair of integers divided by 1000000",
                  factor_HS_error_times_J_at_most=5,
                  gram_operator_error_times_J_at_most=13,
                  trace_error_times_J_at_most=33,
                  numerical_backend="python-flint Arb, 128 bits"),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
