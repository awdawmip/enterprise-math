# PREFIX-665-R6 — Signed curvature certifies an eightfold wider BRC variance strip

Date: 2026-11-10 (Asia/Shanghai). Researcher-ID: EM-DIRECT-07934C / TASK_RESEARCH.
Research-Activity-ID: RA-F54095C14AC6EC72A09CEB58.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem 665.1: Strict normal curvature and quantitative unique maximum

In the unchanged frozen 189-layer two-direction BRC first-stop observer, define
\[
\mu(p,z)=E[Y],\quad H(p,z)=E[Y^2]/2,\quad W(p,z)=2H(p,z)-\mu(p,z)^2,\quad V_q(p,z)=q^2W(p,z)-q\mu(p,z).
\]
Let
\[
\varepsilon=2^{-12}=1/4096,\quad J=[607/4096,609/4096],\quad R=[0,\varepsilon]\times J.
\]
For every real \((p,z)\in R\) and \(12\le q\le24\), the signed estimates
\[
\boxed{\mu_{pp}(p,z)>210,\qquad W_{pp}(p,z)<-12000}
\]
and therefore
\[
\boxed{(V_q)_{pp}(p,z)=q^2 W_{pp}-q\mu_{pp}<-12000q^2}
\]
hold strictly. The unique maximum of \(V_q\) on \(R\) remains \((0,z_*(q))\), with \(z_*(q)\) the unique edge maximum certified by PREFIX-660. Set \(M_q=V_q(0,z_*(q))\). Then
\[
\boxed{M_q-V_q(p,z)\ge76650p+6000q^2p^2+6400000(z-z_*(q))^2}
\]
with strict inequality away from the maximizer. The verified strip has eight times the area of PREFIX-664 (width \(2^{-15}\)) and 262144 times the area of PREFIX-661 (width \(2^{-30}\)), with the same \(z\)-band.

## Proof: signed moment curvature, not an absolute-variance perturbation

Let \(A_n(k)\) be the frozen survivor count after \(n\) branches and \(f_n(k)=A_n(k)/\binom nk\in[0,1]\). Its Bernstein survival polynomial is
\[
s_n(u)=\sum_{k=0}^n A_n(k)u^k(1-u)^{n-k},\qquad 0\le n\le188.
\]
Set \(t_m(z)=s_m(z)\) and
\[
w_{nm}=2^{-(n+m+1)}\binom{n+m}{n},\quad
a_n(z)=1-\sum_{m=0}^{188}w_{nm}t_m(z),\quad
b_n(z)=n+1-\sum_{m=0}^{188}\frac{n+m+1}{2}w_{nm}t_m(z).
\]
The two-clock Gamma/Poisson maximum identity (reused from PREFIX-659) gives
\[
\mu(p,z)=\sum_{n=0}^{188}a_n(z)s_n(p)+\sum_{m=0}^{188}t_m(z),
\quad H(p,z)=\sum_{n=0}^{188}b_n(z)s_n(p)+\sum_{m=0}^{188}(m+1)t_m(z).
\]
The negative-binomial weights sum to one; hence \(0\le a_n\le1\) and \(0\le b_n\le n+1\).

Differentiating the finite Bernstein polynomials exactly, at \(p=0\):
\[
s_n''(0)=n(n-1)\Delta^2 f_n(0),\quad
s_n'''(0)=n(n-1)(n-2)\Delta^3 f_n(0).
\]
A fresh full 189-layer exact integer recurrence at \(Q=19/128\) gives strict rational brackets:
\[
89.455<\mu(0,Q)<89.456,\;
231<\mu_{pp}(0,Q)<232,\;
10472<H_{pp}(0,Q)<10474,
\]
\[
8308<\mu_{ppp}(0,Q)<8310,\quad 526257<H_{ppp}(0,Q)<526260,
\]
\[
-7322<\mu_{ppz}(0,Q)<-7320,\quad
-330968<H_{ppz}(0,Q)<-330964.
\]
Every comparison is made with Fraction, not rounded floating point.

Write \(\delta=1/4096\). The signed center values are extended in \(z\) using the exact negative-binomial moments
\[
E[(m)_2]=(n+1)(n+2),\quad
E[\tfrac{n+m+1}{2}(m)_2]=(n+1)(n+2)(n+3)
\]
and the Bernstein bound \(|t_m''(z)|\le2m(m-1)\). On \(J\), the score bound \(|t_m'(z)|<21\) holds for \(m\le188\). The resulting exact integer budgets are
\[
Z_{\mu,2}=35752800,\quad Z_{H,2}=1373274000,\quad
Z_{\mu,3}=22503600,\quad Z_{H,3}=911030400.
\]
In the \(p\) direction, put \(e_{n,0}=\Delta^4 f_n(0)\) and \(e_{n,1}=\Delta^4 f_n(1)\). Since \(f_n(k)\in[0,1]\), \(|\Delta^4f_n(k)|\le8\), and
\[
|s_n^{(4)}(p)|\le n^{\underline4}
\left(|e_{n,0}|+(n-4)\varepsilon|e_{n,1}|+
8\binom{n-4}{2}\varepsilon^2\right)\quad(0\le p\le\varepsilon).
\]
The certificate sums this cap with weights 1 and \(n+1\) to obtain \(C_{\mu,4}\) and \(C_{H,4}\). Taylor's theorem in \(z\), then \(p\), yields
\[
|\mu_{pp}(p,z)-\mu_{pp}(0,Q)|\le E_\mu
=7322\delta+\tfrac12 Z_{\mu,2}\delta^2+
\varepsilon(8310+Z_{\mu,3}\delta)+\tfrac12\varepsilon^2 C_{\mu,4},
\]
\[
|H_{pp}(p,z)-H_{pp}(0,Q)|\le E_H
=330968\delta+\tfrac12Z_{H,2}\delta^2+
\varepsilon(526260+Z_{H,3}\delta)+\tfrac12\varepsilon^2C_{H,4}.
\]
Exact verification gives
\[
E_\mu=\frac{37547206677619}{2199023255552},\qquad
E_H=\frac{15323198055973819}{8796093022208}.
\]
The previously established k=1 Bernstein integration budget, evaluated at \(\varepsilon\), implies \(|\mu_p|<229\). Using \(|\mu_z(0,z)|<3969\) (PREFIX-659), we get
\[
\mu(p,z)>\frac{4527621}{51200}>88,\quad
\mu_{pp}(p,z)>231-E_\mu>210,\quad H_{pp}(p,z)<10474+E_H<12217.
\]
Now
\[
W_{pp}=2H_{pp}-2\mu_p^2-2\mu\mu_{pp}
<2(10474+E_H)-2\frac{4527621}{51200}(231-E_\mu)
=\frac{-754511415287856738753}{56294995342131200}<-12000.
\]
This proves uniform strictly negative \(V_{q,pp}\).

Finally PREFIX-661 establishes \(V_{q,p}(0,z)<-76650\) for every real \(12\le q\le24\), and PREFIX-660 gives the boundary gap \(V_q(0,z_*)-V_q(0,z)\ge6400000(z-z_*)^2\) for \(z\in J\). Integrate the strict normal curvature in \(p\), add this edge gap and obtain the stated stability and uniqueness.

## Evidence, reuse and next discriminating unit

Companion Python certificate recomputes all 189 integer-survivor layers, the Q-centered \(a_n,b_n\) moments and their mixed derivatives; all claimed inequalities use exact Fraction arithmetic. Result JSON contains the full rational envelopes; local run: ALL_CHECKS_PASS 4920. Source is the immutable frozen statistical observer pin, not a claim about all native Heartbeat dynamics. BRC observer resolution: REUSE_EXECUTED / COMPOSE_APPLIED, preserving count multiplicity and path state through the recurrence before Bernstein readout.

The next test is the same signed-curvature mechanism at \(\varepsilon=2^{-11}\): investigate tighter k=2/k=3 Bernstein tails or two-dimensional interval subdivision; the present coarse fourth-derivative envelope loses the sign there. Separately, certify triangle-wise variance upper bounds against the boundary winner to advance the full \([0,1]^2\) global maximum objective. Formal Result and independent review remain pending.
