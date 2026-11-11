#!/usr/bin/env python3
"""PREFIX-697-R6: exact 189-row BRC endpoint observer and maximal bridge parameter range.
Inherited exact integer-kernel replay plus a direct zero-jet computation at the two bridge endpoints; standard-library Fraction.
Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as Q
from math import comb, factorial
import json

N,DEN=189,1<<18
C,D,R=53,1000,6
SCIENCE_PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
FLOORA=[44000296,-168056589514,-6667624082229,39352687679231,3189837819999830,-36266294695911132]
FLOORB=[789752024,12845959424,-99127959112,-1326952329685,-14895243921676,-1960958310350017]
@lru_cache(None)
def fall(n,j):
    x=1
    for i in range(j): x*=n-i
    return x
@lru_cache(None)
def accept(n,k,p):
    return 40*(n+1)*comb(n,k)*p**k*(DEN-p)**(n-k)>DEN**n
@lru_cache(None)
def alive(n,k):
    if k>n//2: return alive(n,n-k)
    m=k*DEN//n
    assert accept(n,k,m)
    if k==0: lo=hi=0
    else:
        x,y=0,m
        while y-x>1:
            t=(x+y)//2
            if accept(n,k,t): y=t
            else: x=t
        lo,hi=x,y
    x,y=m,DEN
    while y-x>1:
        t=(x+y)//2
        if accept(n,k,t): x=t
        else: y=t
    if 4*(x-hi)>DEN: return True
    if 4*(y-lo)<DEN: return False
    raise ArithmeticError(("ambiguous frozen survivor",n,k))
def rows():
    row={0:1};out=[]
    for n in range(N):
        out.append(row.copy()); nxt=defaultdict(int)
        for k,v in row.items(): nxt[k]+=v;nxt[k+1]+=v
        row={k:v for k,v in nxt.items() if alive(n+1,k)}
    assert not row and len(out)==189
    assert sum(map(len,out))==9529
    assert all(0<=v<=comb(n,k) for n,h in enumerate(out) for k,v in h.items())
    return out
def jets(rs):
    ap=[C**i for i in range(N+1)]
    cp=[(D-C)**i for i in range(N+1)]
    dp=[D**i for i in range(N+1)]
    out=[[] for _ in range(R)]
    for n,row in enumerate(rs):
        for j in range(R):
            if j>n:
                out[j].append(Q(0));continue
            numerator=0
            for k,mult in row.items():
                for ell in range(j+1):
                    f=j-ell
                    if k<ell or n-k<f: continue
                    numerator+=mult*comb(j,ell)*(-1)**f*fall(k,ell)*fall(n-k,f)*ap[k-ell]*cp[n-k-f]
            out[j].append(Q(numerator,dp[n-j]))
    return out
def dot_pair(x, y, weights, common_den):
    """Compute exactly K and J bilinear moments with one integer sweep.
    x[n],y[n] are rational survivor derivatives; D**n*x[n] is integral.
    K[n,m] = binom(n+m,n)/2**(n+m+1), J=(n+m+1)*K/2.
    """
    ux = [int(v * D**i) for i, v in enumerate(x)]
    uy = [int(v * D**i) for i, v in enumerate(y)]
    sk = sj = 0
    for n, u in enumerate(ux):
        if not u:
            continue
        wrow = weights[n]
        for m, v in enumerate(uy):
            if not v:
                continue
            term = u * v * wrow[m]
            sk += term
            sj += (n + m + 1) * term
    return Q(sk, common_den), Q(sj, 2*common_den)

def full_check():
    rs=rows(); js=jets(rs)
    s0=[Q(h.get(0,0)) for h in rs]
    base=2*D
    powers=[base**i for i in range(2*(N-1)+1)]
    common_den=2*powers[2*(N-1)]
    weights=[[comb(n+m,n)*powers[2*(N-1)-n-m] for m in range(N)] for n in range(N)]
    md=[];me=[];hd=[];he=[]
    s0sum=sum(s0)
    s0h=sum((n+1)*s0[n] for n in range(N))
    for j in range(R):
        Kd=Jd=Q(0)
        for k in range(j+1):
            dk,dj=dot_pair(js[k],js[j-k],weights,common_den)
            Kd+=comb(j,k)*dk
            Jd+=comb(j,k)*dj
        sk,sj=dot_pair(s0,js[j],weights,common_den)
        me.append(sum(js[j])+(s0sum if j==0 else 0)-sk)
        md.append(2*sum(js[j])-Kd)
        he.append(sum((n+1)*js[j][n] for n in range(N))+(s0h if j==0 else 0)-sj)
        hd.append(2*sum((n+1)*js[j][n] for n in range(N))-Jd)
    A=[];B=[]
    for j in range(R):
        B.append(md[j]-me[j])
        A.append(2*(hd[j]-he[j])-sum(comb(j,k)*(md[k]*md[j-k]-me[k]*me[j-k]) for k in range(j+1)))
    fa=[(v*10**8).__floor__() for v in A]
    fb=[(v*10**8).__floor__() for v in B]
    assert fa==FLOORA and fb==FLOORB
    assert fa[5] == -36266294695911132 and fa[5] != -36266294695911140
    M=N-1
    dc=[1]+[2**(j-1)*fall(M,j) for j in range(1,7)]
    U=[3*N]+[N*(4*dc[j]+sum(comb(j,i)*dc[i]*dc[j-i] for i in range(1,j))) for j in range(1,7)]
    Ab=4*N*U[6]+2*sum(comb(6,i)*U[i]*U[6-i] for i in range(7))
    Bb=2*U[6]
    assert Ab==201273663850076722544640 and Bb==17896441402901698560
    A3=4*N*U[3]+2*sum(comb(3,i)*U[i]*U[3-i] for i in range(4))
    assert A3==218571424275456 and 2*U[3]==69527880576
    T=Q(647,5000000)
    enclosures={}
    for name,fl,bnd in (("A",fa,Ab),("B",fb,Bb)):
        eps=sum(Q(max(abs(fl[j]),abs(fl[j]+1)),10**8)*T**(j-1)/factorial(j-1) for j in range(2,6))+Q(bnd)*T**5/factorial(5)
        lower=Q(fl[1],10**8)-eps
        upper=Q(fl[1]+1,10**8)+eps
        if name=="A": assert -1751<lower<upper<-1611
        else: assert 128<lower<upper<129
        enclosures[name]={"lower_exact":str(lower),"upper_exact":str(upper),"deviation_exact":str(eps)}
    output={
        "title":"PREFIX-693-R6",
        "frozen_science_pin":SCIENCE_PIN,
        "levels":N,"survivor_cells":9529,
        "bridge":["264353/5000000","530659/10000000"],
        "q_band":["63055771/5256000","660614143/27500000"],
        "jets_floor_1e8":{"A":fa,"B":fb},
        "sixth_derivative_bounds":{"A":Ab,"B":Bb},
        "derivative_enclosures":enclosures,
        "proved":["all z in bridge: -1751<A'<-1611, 128<B'<129",
                  "all real q in band: exactly one transverse zero of qA-B in bridge",
                  "analytic increasing inverse q=B/A and two-sided slope envelope"],
        "method":"exact frozen survivor recurrence + joint kernels + rational global Taylor enclosure",
        "status":"AUTHOR_DERIVED / EXACT_FRACTION_REPLAY / UNREVIEWED / NOT_ADMITTED",
        "verification":"ALL_CHECKS_PASS PREFIX693-R6"
    }
    # Model-readout root certification: not a native BRC state update.
    q_lo,q_hi=Q(63055771,5256000),Q(660614143,27500000)
    left,right=Q(528706,10**7),Q(530659,10**7)
    d_lo=128+1611*q_lo
    d_hi=129+1751*q_hi
    m=2500000*q_hi+1500
    c=m/(2*d_lo)
    width=right-left
    contraction=c*width
    assert d_lo>0 and d_hi>d_lo and contraction<Q(31,100)
    e=width
    errors=[]
    for i in range(5):
        e=c*e*e
        errors.append(str(e))
    assert Q(errors[3])<Q(31,10**13)
    assert Q(errors[4])<Q(2,10**20)
    output.update({"title":"PREFIX-695-R6",
      "status":"AUTHOR_RECOMPUTED / FULL_189_ROW_EXACT_INTEGER_KERNEL / UNREVIEWED / NOT_ADMITTED",
      "verification":"ALL_CHECKS_PASS PREFIX695-R6",
      "independent_common_denominator_replay":True,
      "correction":{"old_RESULTS_A5":"-36266294695911140","exact_A5":str(fa[5]),"paper_checker_A5":str(FLOORA[5])},
      "newton_certified":{"q_band":[str(q_lo),str(q_hi)],"bridge":[str(left),str(right)],
        "d_lower":str(d_lo),"d_upper":str(d_hi),"second_derivative_bound":str(m),
        "quadratic_error_coefficient":str(c),"bridge_width":str(width),
        "contraction_factor_bound":str(contraction),"step_errors":errors,
        "five_step_lt":"2/100000000000000000000","mode":"safeguarded projected Newton readout solver only"}})
    print(json.dumps(output,ensure_ascii=False,indent=2))


def exact_endpoint_bridge():
    """Recompute full rational A,B,Q at both ends of PREFIX-696 bridge J.
    No interpolation or floating point is used for any logical comparison.
    The underlying survivor predicate, branch labels and K/J kernels come
    from frozen science. Uniform Q'>0, Q''>0 are PREFIX-696 dependencies.
    """
    global D
    D=25000  # exact common denominator for 1321/25000 and 1329/25000
    rs=rows()
    p=2*D
    pw=[p**i for i in range(2*(N-1)+1)]
    H=2*pw[2*(N-1)]
    weights=[[comb(n+m,n)*pw[2*(N-1)-n-m] for m in range(N)] for n in range(N)]
    s0=[Q(row.get(0,0)) for row in rs]
    s0sum=sum(s0); s0weighted=sum((n+1)*s0[n] for n in range(N))
    out={}
    ratios={}
    original_moments={}
    for label,t in (("left",1321),("right",1329)):
        x=[Q(sum(v*t**k*(D-t)**(n-k) for k,v in row.items()), D**n)
           for n,row in enumerate(rs)]
        kxx,jxx=dot_pair(x,x,weights,H)
        kyx,jyx=dot_pair(s0,x,weights,H)
        sd=sum(x); sh=sum((n+1)*x[n] for n in range(N))
        md=2*sd-kxx; me=sd+s0sum-kyx
        hd=2*sh-jxx; he=sh+s0weighted-jyx
        A=2*(hd-he)-(md*md-me*me)
        B=md-me
        assert A>0 and B>0
        ratio=B/A
        floor15=(ratio*10**15).__floor__()
        assert Q(floor15,10**15)<ratio<Q(floor15+1,10**15)
        out[label]={"z":f"{t}/25000","q_floor_15":str(floor15),
                    "A_approx":str(float(A)),"B_approx":str(float(B))}
        ratios[label]=ratio
        original_moments[label]=(A,B)
    ql,qr=ratios["left"],ratios["right"]
    assert Q(11125016126410650,10**15)<ql<Q(11125016126410651,10**15)
    assert Q(46505912169160542,10**15)<qr<Q(46505912169160543,10**15)
    assert 11<ql<12 and 46<qr<47 and ql<qr
    # PREFIX-696 Q'>0 throughout J; hence its complete interior crossing
    # parameter range is q in (Q(left),Q(right)).
    assert int(ql)+1==12 and int(qr)==46
    Al,Bl=original_moments["left"]; Ar,Br=original_moments["right"]
    assert 11*Al-Bl<0<12*Al-Bl
    assert 46*Ar-Br<0<47*Ar-Br
    # For q=46 use PREFIX-696 derivative bounds:
    # -(1870*46+129)<F'_46<-(1490*46+128).
    loss=Br-46*Ar
    assert loss>0
    minrate=1490*46+128
    maxrate=1870*46+129
    assert (minrate,maxrate)==(68668,86149)
    lo=Q(1329,25000)-loss/minrate
    hi=Q(1329,25000)-loss/maxrate
    assert Q(531587456,10**10)<lo<hi<Q(531590002,10**10)
    result={"id":"PREFIX-697-R6",
            "science_pin":SCIENCE_PIN,
            "survivor_levels":189,"survivor_cells":9529,
            "bridge_J":["1321/25000","1329/25000"],
            "exact_endpoint_parameter_interval":"(B(left)/A(left), B(right)/A(right))",
            "endpoints":out,
            "maximal_integer_parameters_with_a_unique_interior_J_root":[12,46],
            "q46_root_certified_bracket":["0.0531587456","0.0531590002"],
            "q46_slope_denominator_bounds":[68668,86149],
            "evidence_kind":"exact zero-jet rational recomputation; logical implication of PREFIX-696 Q'>0",
            "formal_admission":False,
            "status":"ALL_CHECKS_PASS PREFIX697-R6"}
    import sys
    if "--full-fractions" in sys.argv:
        for label in ("left","right"):
            A,B=original_moments[label]
            result["endpoints"][label].update({"A_exact":str(A),"B_exact":str(B),"Q_exact":str(ratios[label])})
    print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))
    return result

if __name__=="__main__":
    exact_endpoint_bridge()
