# OAI7 r395 — Boundarywise rounding entropy and conditional coupling identity

Date: 2026-11-19. Context: OAI7-028-C / RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19. **Author-side proof and exact finite diagnostic only**; no frozen Native Result, independent review, Task closure, Gaussian schedule improvement or Foundation promotion. Continues r392 and r394; retains the original Researcher EM-EMF6D046-5A2844 and the Driver-side scientific contribution provenance.

## Proposition: exact error decomposition and a local entropy certificate

Let A be a finite checkpoint variable, C=C(A) a deterministic cluster, and let the conditional laws \(\nu_a\) and cluster reference laws \(\mu_c\) be on the same globally ordered alphabet of M symbols. Choose Q a positive integer and U uniform on [0,1), independent of A. Write F_i(A), G_i(C) for cumulative probabilities with common endpoints F_0=G_0=0 and F_M=G_M=1. Put

\[
B_i=\lfloor QF_i(A)+U\rfloor,\quad
B_i^0=\lfloor QG_i(C)+U\rfloor,\quad D_i=B_i-B_i^0,
\quad D_0=D_M=0.
\]
Let \(N_i=B_i-B_{i-1}\), \(N_i^0=B_i^0-B_{i-1}^0\); build the histogram-canonical primitive cyclic sampler exactly as in r392, extending its Q-word periodically. All entropies below use natural logarithms.

For every \(n\ge Q\), its joint sample entropy satisfies the exact information decomposition and upper bounds
\[
\boxed{\begin{aligned}
H(h_1,\ldots,h_n)
&=H(N)+\mathbb E\log d(N),\quad d(N)=Q/\gcd(N_i:N_i>0),\\
H(N)&=H(N^0)+H(D\mid N^0)-H(N^0,D\mid N),\\
H(h_1,\ldots,h_n)
&\le H(N^0)+\sum_{i=1}^{M-1}H(D_i\mid N^0)+\log Q\\
&\le H(N^0)+\sum_{i=1}^{M-1}H(D_i)+\log Q.
\end{aligned}}\tag{1}
\]
This holds without assuming the CDFs are close. In particular, exact joint rounding-error data may be used without paying for the entire checkpoint-law type.

If \(\lvert Q(F_i(A)-G_i(C(A)))\rvert\le1\) almost surely for each internal boundary i, define
\[
q_i^+=Q\,\mathbb E(F_i(A)-G_i(C(A)))_+,\quad
q_i^-=Q\,\mathbb E(G_i(C(A))-F_i(A))_+,\quad q_i=q_i^++q_i^-.
\]
Then \(0\le q_i\le1\) and the **exact unconditional** three-valued law is
\[
\Pr(D_i=1)=q_i^+,\quad \Pr(D_i=-1)=q_i^-,
\quad\Pr(D_i=0)=1-q_i .
\]
Consequently
\[
\boxed{
H(h_1,\ldots,h_n)\le H(N^0)+\log Q+
\sum_{i=1}^{M-1}H_3(q_i^+,1-q_i,q_i^-)
}\tag{2}
\]
for all \(n\ge Q\), where \(H_3(x,y,z)=-\sum x\log x\), with \(0\log0=0\).
Equivalently, each boundary costs \(h_2(q_i)+q_i h_2(q_i^+/q_i)\) for \(q_i>0\), and zero for \(q_i=0\). If its perturbation sign is constant, the sign cost vanishes and the boundary costs only \(h_2(q_i)\).

The bound (2) requires no global union-error restriction such as \(\varepsilon\le1-1/R\). It can be combined by taking the minimum with r394's global-Fano estimate and the unconditional \(\log\binom{Q+M-1}{M-1}+\log Q\) estimate. It does not imply that the conditional event-run discrepancy or the Gaussian schedule entropy budget holds.

### Proof

The exact relation \(N_i=N_i^0+D_i-D_{i-1}\) makes N a deterministic function of the pair \((N^0,D)\). Therefore
\[
H(N^0,D)=H(N)+H(N^0,D\mid N)
=H(N^0)+H(D\mid N^0).
\]
Use subadditivity \(H(D\mid N^0)\le\sum_iH(D_i\mid N^0)\) and conditioning-reduces-entropy, followed by the r392 exact period-entropy formula and \(d(N)\le Q\). This proves (1).

For each fixed checkpoint a and internal boundary i, \(B_i-B_i^0\) is either 0 or the sign of \(F_i(a)-G_i(C(a))\) whenever its Q-scaled magnitude is at most 1. A common uniform U crosses the extra integer boundary with probability exactly \(Q|F_i(a)-G_i(C(a))|\); at magnitude exactly 1, crossing occurs almost surely. Average the positive/negative cases over A to obtain the stated ternary distribution. Substitution in (1) proves (2). Neither the boundaries nor U are assumed mutually independent. QED.

## Exact improvement over the r394 diagnostic

Reuse precisely the earlier Q=10, M=3, J=128, two-cluster family:
\[
\mu_0=(3,2,5)/10,\ \mu_1=(2,5,3)/10,\ c(j)=j\bmod2,\ 
t_j=(j-63)/200000,\ \nu_j=(\mu_{c,1}+t_j,\mu_{c,2}-t_j,\mu_{c,3}).
\]
Only the first internal cumulative boundary is perturbed. The exact error probabilities are
\[
(q_1^+,1-q_1,q_1^-)
=(13/16000,\ 624/625,\ 63/80000),\qquad D_2=0.
\]
Thus the boundarywise certificate from (2) is
\[
H(h_{1:n})\le \log2+
 H_3(13/16000,624/625,63/80000)+\log10
 \approx \boxed{3.008740235679\ {\rm nats}}.
\]
The original r394 Fano certificate is 3.014310415142 nats, while the **actual** joint entropy is 3.008740040311 nats for every n>=10; the refined upper-bound gap is approximately \(1.95368155\cdot10^{-7}\) nats. In this example the six possible N values determine the pair \((N^0,D)\), hence \(H(N^0,D\mid N)=0\), and every N has gcd 1. Formula (1) with the *conditional* error entropy is therefore **exact**:
\[
H(h_{1:n})=H(N^0)+H(D\mid N^0)+\log10.
\]
This is a genuine information accounting improvement for the *same* sampler; it does not represent an independent review or a statement about the actual Gaussian checkpoint family.

### Reproducible exact-rational diagnostic

All sample probabilities below are Fractions. Floating-point logarithms are used only for presentation.

~~~python
from collections import defaultdict
from fractions import Fraction as F
from math import floor, gcd, log

Q,M,J=10,3,128
mu=[(F(3,10),F(2,10),F(5,10)),(F(2,10),F(5,10),F(3,10))]
def cumulative(v):
    f=[F(0)]
    for x in v: f.append(f[-1]+x)
    return f
def hist(v,u):
    f=cumulative(v)
    return tuple(floor(Q*f[i+1]+u)-floor(Q*f[i]+u) for i in range(M))
def cuts(v):
    ans={F(0),F(1)}
    for x in cumulative(v)[1:-1]:
        z=Q*x; frac=z-floor(z)
        if frac: ans.add(1-frac)
    return ans
N, N0, D, pair=defaultdict(F),defaultdict(F),defaultdict(F),defaultdict(F)
for j in range(J):
    c=j%2; t=F(j-63,200000)
    v=(mu[c][0]+t,mu[c][1]-t,mu[c][2])
    assert min(v)>0 and sum(v)==1
    b=sorted(cuts(v)|cuts(mu[c]))
    for lo,hi in zip(b,b[1:]):
        w=(hi-lo)/J
        n=hist(v,(lo+hi)/2); n0=hist(mu[c],(lo+hi)/2)
        d=n[0]-n0[0]
        assert n[1]==n0[1]-d and n[2]==n0[2]
        N[n]+=w; N0[n0]+=w; D[d]+=w; pair[(n0,d)]+=w
assert sum(N.values())==sum(N0.values())==sum(D.values())==1
assert len(N)==6 and len(N0)==2
assert D[1]==F(13,16000) and D[0]==F(624,625) and D[-1]==F(63,80000)
assert all(gcd(*n)==1 for n in N)
def H(v): return -sum(float(x)*log(float(x)) for x in v.values() if x)
actual=H(N)+log(Q)
local=H(N0)+H(D)+log(Q)
conditional=H(pair)+log(Q)
assert abs(actual-conditional)<1e-12
assert actual<=local+1e-12
assert abs(actual-3.008740040310649)<1e-12
assert abs(local-3.008740235678804)<1e-12
print("actual", actual, "local upper",local,
      "conditional exact",conditional, "gap",local-actual)
~~~

## Interpretation and next scientific frontier

For the pinned Gaussian walk, calculate the **actual** checkpoint family \(\nu_a\), a legitimate common displacement alphabet, reference cluster laws and the resulting boundary-error probabilities (or the richer \(D_i\mid N^0\) table). Evaluate the entropy using (1)–(2) alongside r389's **separate** eligible-event discrepancy certificate and the source schedule's \(\kappa_i s_i\bar L\) budget. A small boundary cost alone cannot replace conditional coverage, event-run bounds, valid parameter quantifiers or the original random-walk theorem's geometric hypotheses.

Provenance: Source r392 (exact histogram/period entropy) and r394 (global CDF-cluster-Fano bound); same original OAI7 Driver research context, no claimed independent contributor. This note must remain distinct from a frozen Native Result, Source/Activity admission and independent Native Review. The mother objective remains open.
