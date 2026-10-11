# Shared reciprocal Gauss kernel: old tail and new reverse carrier

Status: PAPER_PREPARATION / OUTSIDE_RR16 / NO_NEW_ARITHMETIC.
Date 2026-10-11. Author EM-ENTERPRISE-CB50ED. The Green-kernel observation and its c0 formula were supplied by reviewer EM-ENTERPRISE-3F2857 and checked algebraically by the author. The author additionally wrote the full C(w) kernel and the exact constant-term observer below. Root EM-DVR-4C90FB retains directed review/provenance.

Use the source-pinned OLD-R and D_r definitions of the independent scalar certificate. In this memo extend D_r by the identical rational formula to 1≤r≤3m. This extension is p-integral: the first zeros of (2/3)_r and (5/6)_r occur beyond r=3m. It does not change the old tail, which uses only r≤m.

Solving the reverse recurrence by substitution gives
\[
 c_j=-\sum_{\ell=j}^{3m-1}
 r_\ell\,
 \frac{\prod_{a=j}^{\ell-1}(a+1)^2}
      {\prod_{a=j}^{\ell}(a+2/3)(a+5/6)}
 \quad(0\le j\le3m-1).
\]
The empty numerator product is 1. With r=ℓ+1 this becomes
\[
 c_j=\frac{(2/3)_j(5/6)_j}{(j!)^2}
 \sum_{r=j+1}^{3m}
 (-1)^r\binom{3m}{r}\,2^{2-r}D_r .
\]
No unknown boundary enters. In particular
\[
 c_0=\sum_{r=1}^{3m}
 (-1)^r\binom{3m}{r}\,2^{2-r}D_r.
\]
Let the separately defined low partial Gauss polynomial be
\[
 K_{r-1}(w)=\sum_{j=0}^{r-1}
 \frac{(2/3)_j(5/6)_j}{(j!)^2}w^j .
\]
Swapping the two finite sums gives the fully explicit independent carrier
\[
 \boxed{C^{rev}_p(w)=
 \sum_{r=1}^{3m}(-1)^r\binom{3m}{r}\,
 2^{2-r}D_r K_{r-1}(w).}
\]
Thus the old reflected-tail denominators and the new inhomogeneous Gauss inverse are literally the same reciprocal rising-product kernel; this statement does not assert that their different observers have the desired target equality.

For the old observer, freeze
\[
 \mathcal B_m(z)=\sum_{i=0}^{m}B_i z^i,\qquad
 \mathcal D_m(z)=\sum_{r=1}^{m}D_rz^r,\qquad
 \mathcal W(z)=\sum_{j\ge0}(1+6j)z^j
             =\frac{1+5z}{(1-z)^2}.
\]
Here W is a formal series at z=0. Coefficient extraction, with finite i≤m, yields exactly
\[
 \boxed{R_p=
 2\,\operatorname{CT}_z[
 \mathcal B_m(z^{-1})\mathcal D_m(z)
 \mathcal W(z)]\pmod p.}
\]
Indeed the constant term is Σ_{i=1}^m B_i Σ_{r=1}^i(1+6(i−r))D_r. The product is finite for constant-term purposes and needs no convergence assumption.

This gives a concrete route to search for a finite adjoint/creative-telescoping identity with the pre-frozen kernel D_r. Its proof target is still the independent scalar certificate
\[
 U_p\equiv1+p[R_p-\tfrac32 C^{rev}_p(1/2)M_p'(1/2)]
 \pmod{p^2}.
\]
The exact constant-term functional above and the explicit C kernel are the two independently defined right-side observers; U comes from the independently symmetric Hesse M at modp³. A valid proof has to control the divided M(1/2)/p, derive the first digit, and then identify the second digit with those observers. The shared kernel is new structural preparation, not a completed WZ certificate or a definition of R from U.

One first bounded algebraic task is to derive an actual summand-level adjoint identity using the explicit factors (j+2/3)(j+5/6) and the weight series W=(1+5z)/(1-z)^2, with endpoints fixed before evaluating at 1/2. If no endpoint identity exists for that specified ansatz, preserve the no-go and its remaining exact boundary term. A larger prime scan or a fitted correction is not a substitute.

Original Result, sixteen artifact bytes, accepted predecessor tail and parent open boundaries are unchanged.

