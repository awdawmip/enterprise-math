# D25/LIFT — p=157 ordinary Hesse odd port survives a vanishing scalar second-digit tail

Date: 2026-11-10. Status: **AUTHOR_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. Parent task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific input `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. This author-portable note consumes the existing Hesse trace/norm identities and the already-proved p=157 scalar-tail cancellation; its new increment is an **exact cross-observer separation witness** for the same prime. It makes no native H0/B0 or Frobenius identification.

## Exact statement at p=157

Work in `R=(Z/157^3 Z)[T]/(T^2-2)`, where `157^3=3869893`, with tagged ports `u=(2-T)/4`, `ubar=(2+T)/4` and coefficient involution `sigma(T)=-T`. Let

\[
A_p(X)=\sum_{k=0}^{(p-1)/3}\frac{(3k)!}{27^k(k!)^3}X^k.
\]

Two independent exact algorithms, one based on the coefficient recurrence and binary ring powers and the other on direct factorial coefficients and the even/odd binomial expansion of `u^k`, give

\[
\boxed{A_{157}(u)=3454000+934778T\pmod{3869893}.}
\]

Both coordinates are divisible by 157. Consequently the **ordinary coefficient-ring** candidate and its norm are

\[
\boxed{\alpha=A_{157}(u)/157\equiv20+145T\pmod{157},}
\qquad
\boxed{N(\alpha)=20^2-2(145)^2\equiv112\ne0\pmod{157}.}
\]

The previously established exact symmetric/antisymmetric Hesse factorization at these ports is `A_p(u)=G+(pT/4) Phi`. It gives the **tagged odd observer**

\[
\boxed{\Phi_{157}(1/8)=4(934778/157)\equiv109\ne0\pmod{157},}
\]

and the quadratic port discriminant obeys

\[
\boxed{\bigl(\operatorname{Tr}(A)^2-4N(A)\bigr)/157^2
\equiv8(145)^2\equiv53\ne0\pmod{157}.}
\]

For the separately defined frozen scalar sequence `B_0=1, B_(k+1)/B_k=(6k+1)(3k+1)/(36(k+1)^2)`, evaluate `0<=k<157` exactly. Let `S2=sum_(k=53)^156 B_k` and `g=sum B_k, h=sum (12k+1)B_k, G_p=g/p`. Independent integer-product and modular-recurrence calculations give

\[
\boxed{S_2\equiv74\cdot157^3\pmod{157^4},\quad v_{157}(S_2)=3,}
\]

\[
h\equiv80\pmod{157},\quad
G_p\equiv13712\pmod{157^2},\quad
h\equiv13111\pmod{157^2},
\]

and hence

\[
\boxed{\Delta_{157}=(G_ph-1)/157\equiv82\pmod{157},
\qquad\Delta_{157}^{\le52}\equiv82\pmod{157}.}
\]

**Separation result.** At this exact prime, the scalar tail's contribution to the second p-adic digit is zero, whereas the independently tagged ordinary Hesse odd coordinate is nonzero: `109 mod 157`; its normalized ordinary norm is also nonzero: `112 mod 157`. Thus discarding the odd Hesse port because the scalar tail cancels would be a genuine information loss. The two observers have distinct source and operation types; this witness does not assert any universal algebraic independence theorem.

## Method, reproducibility and source boundary

All calculations are exact modular integer computations, with denominators invertible in the declared ranges. The Hesse polynomial was evaluated independently by (i) a recurrence with multiplication in `R` and (ii) the closed factorial coefficient with direct even/odd binomial expansion. Each scalar `B_k` for `k=0,...,156` was computed both by recurrence and by separate integer numerator/denominator products modulo `157^4`; agreement was asserted at every index. The exact observations are packaged with standalone `d25_p157_hesse_probe.py`, JSON certificate, and verification log in the conversation artifact `D25_P157_HESSE_ODD_TAIL_SEPARATION_AUTHOR_PORTABLE_20261110.zip` (SHA-256 `ec0286e180b85856220df2fb878653552bc43f69a0ada19309d27afa15ee8147`). The archive is a local conversation artifact, not a Source-published bundle.

The original native H0/B0 divided-power module, actual Frobenius direction, normalization eta and frozen definition of `R_157` remain to be authenticated before comparison with `Delta_157=82`. No native CM experiment or canonical task publication is claimed. This note preserves all predecessor Source progress and author contributions, and does not constitute an active CLAIM, official checkpoint, Result, or independent review. Next discriminating action: retrieve original-class H0/B0 and R_157 at the frozen Source, then test whether any port map is legitimate and compute `Delta_157-R_157` with the signed branch retained.
