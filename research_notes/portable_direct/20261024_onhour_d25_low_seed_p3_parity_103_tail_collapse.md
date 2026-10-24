# D25/LIFT — fixed-prime LOW-seed third-digit parity and exact two-tail collapse

2026-10-24 | ordinary TASK_RESEARCH, onhour logical Research lane | **AUTHOR-SIDE MATHEMATICS; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Not a Source checkpoint, formal Result, benchmark, native CM/divided-power comparison or independent review.

**Scope and provenance.** Mother objective RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen *scientific* source c47e13e4aba0e006366f989d6334d443f6333ae3. This note uses the original summand from the independently established exact WZ work at c7fb90fd7ec451a954b553b963dd85d4ec99fc96 and the upper-half p³ five-port theorem at 7724e73f2d15c92ce98520e6a55b8231d737fa03. It does not re-credit either. The distinct hourly lane's odd-product/source-residue theorem at the current portable note 20261024_hourly_d25_third_digit_odd_product_source_transfer.md concerns a different observable and is not imported as an identity with this fixed-endpoint LOW seed. Here conversation identity is chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance and hourly research.

## Original frozen arithmetic and target

For nonnegative integers r,n, set

\[
A_r=\frac{(6r)!}{3^{6r}((2r)!)^3},\quad
R_{r,0}=1,\quad
\frac{R_{r,n+1}}{R_{r,n}}=
\frac{(4r+2n+1)(3n+1)(3n+2)}
{36(n+1)(2r+n+1)(4r+n+1)},
\]
\[
T_{r,n}=A_r(6n+12r+1)R_{r,n},\qquad
S_r=\sum_{n=0}^{4r}T_{r,n}.
\]

The previously proved exact factorial identity is

\[
T_{r,n}=(6n+12r+1)
\frac{(6r)!(4r+2n)!(3n)!}
{3^{6r}(2r)!\,216^n(n!)^2((2r+n)!)^2(4r+n)!}. \tag{F}
\]

Fix p=6m+1 prime, m>=2, and r=ell=ceil(m/2). The scientific target remains S_m congruent to p(4/3)^{p-1} modulo p³ for p≡13,19 (mod 24). The inherited five-port formula states S_m≡S_r+p sum_{k=r}^{m-1}d_{p,k} (mod p³). This note works on the still-unproved original LOW seed S_r, not on another task or native experiment.

## Theorem 1 — exact valuation support of the LOW seed

For each integer n with 0<=n<=4r, *every term is p-integral*, and its exact p-adic valuation is:

- If m is even (r=m/2, p=12r+1), v_p(T_{r,0})=1 and v_p(T_{r,n})=0 for 1<=n<=4r.
- If m is odd (r=(m+1)/2, p=12r-5, p>=19), v_p(T_{r,n})=0 for 0<=n<=4r-3; v_p(T_{r,4r-2})=1; v_p(T_{r,4r-1})=v_p(T_{r,4r})=2.

**Proof.** When m is even, 12r=p-1. Every factorial argument in (F), including the largest numerator arguments 4r+2(4r)=3(4r)=12r=p-1, is below p. The separate scalar is 6n+12r+1=p+6n. It is p-divisible exactly at n=0, because 1<=n<=4r=2m<p.

When m is odd, 12r=p+5. Every denominator factorial argument in (F) is <p: n<=4r, 2r+n<=6r, 4r+n<=8r; for p>=19, 8r=2(p+5)/3<p. Also 6r<p. The scalar is 6n+12r+1=p+6(n+1), and 1<=n+1<=4r+1<p, so it is always a p-unit. For n<=4r-3, both 4r+2n and 3n are below p. At n=4r-2 those two arguments are respectively p+1 and p-1; at n=4r-1 they are p+3 and p+2; at n=4r they are both p+5. Each p<=t<2p factorial contributes exactly one factor p. This proves the asserted valuations without relying on cancellation between summands. QED.

In particular the two original hard-target classes have *different compulsory ports*: p≡13 (mod 24) has a valuation-one HEAD at n=0; p≡19 (mod 24) has a valuation-one terminal-predecessor at n=4r-2 and two valuation-two TAIL terms at n=4r-1,4r.

## Theorem 2 — exact tail-pair ratio and universal 103/1500 coefficient

Take m odd, r=(m+1)/2 and p=12r-5>=19. Let U=T_{r,4r-2}, V=T_{r,4r-1}, W=T_{r,4r}; all are original, unmodified terms. Direct substitution into the original consecutive-term ratio gives **exact rational equalities**

\[
\frac VU=
\frac{(3r-1)(12r-5)(36r-5)}
{3(6r-1)(8r-1)(36r-11)}, \tag{R1}
\]
\[
\frac WV=
\frac{(6r-1)(12r-1)^2(36r+1)}
{3456r^3(36r-5)}. \tag{R2}
\]

Therefore, after *exact* algebraic substitution r=(p+5)/12,

\[
\boxed{\frac{V+W}{U}=
p\frac{(p+1)(15p^4+269p^3+1796p^2+5284p+5768)}
{8(p+3)(p+5)^3(2p+7)(3p+4)}.} \tag{E}
\]

All denominators in (E) are p-units for p>=19. Reduction of the remaining rational factor modulo p gives 5768/84000=103/1500. Since v_p(U)=1,

\[
\boxed{V+W\equiv \frac{103p}{1500}U\pmod{p^3}.} \tag{C}
\]

This is an honest third-digit readout: it retains the two original valuation-two ports *as a pair* and contracts them only after proving the precise observer equality at p³ precision.

Further, v_p(V+W)=2 for every eligible p except p=103, where v_103(V+W)=3. Indeed, the polynomial in (E) has constant term 5768=56·103, and no other prime p>=19 divides 5768. At p=103, its value divided by 103 is 56+5284≡87 (mod 103), not zero; all other numerator/denominator factors are units. For the target subclass p≡19 (mod 24), p≠103 because 103≡7 (mod 24), so **v_p(V+W)=2 for every target prime in that subclass**. Individually v_p(V)=v_p(W)=2 at p=103 as well; their cancellation to valuation 3 cannot be inferred by dropping provenance.

## Corollary — third-digit LOW-seed interface for both hard-target classes

For p≡13 (mod 24), r=m/2 and the first scalar is exactly p:

\[
\boxed{S_r=pA_r+\sum_{n=1}^{4r}T_{r,n}.} \tag{13}
\]

For p≡19 (mod 24), r=(m+1)/2 and the last two terms contract, modulo p³, to:

\[
\boxed{S_r\equiv
\sum_{n=0}^{4r-3}T_{r,n}
+T_{r,4r-2}\left(1+\frac{103p}{1500}\right)
\pmod{p^3}.} \tag{19}
\]

Combining (13)/(19) with the **inherited** fixed-p upper-half five-port d_{p,k} theorem yields two explicit equivalents of the original target. The missing obligation is to prove the resulting full LOW-seed-plus-five-port difference vanishes modulo p³ uniformly in each prescribed prime class (or produce a genuine original-endpoint counterexample). Neither the parity theorem nor equation (C) asserts that vanishing.

## Arithmetic observer and executed validation

BRC application: the initial observed carrier is the labelled list (n, original T_{r,n}, factorial numerator and denominator p-valuations, scalar-factor valuation, p-adic unit through the required precision). Allowed operation is the original *signed* sum and exact same-prime WZ rank transfer. We retain the HEAD / ordinary / predecessor / TAIL port provenance; the pair (V,W) is collapsed only under (C) at the specified modulus. No positive-mass or zero-cost branch erasure claim is made.

Independent exact-rational recurrence and p-free factorial modular paths were executed against primes 13<=p<=1000, p≡1 (mod 6): **79 primes** (36 even-m, 43 odd-m). The even/odd valuation-support assertions and, in odd cases, (C) passed all instances. For p<=211 the entire seed stream from the exact Fraction recurrence was compared termwise modulo p³ with factorial p-unit arithmetic; no mismatch. The p=103 pair has exact valuation 3 by independent Fraction evaluation (each member has valuation 2). Selected original residues:

| p | r | S_r (mod p³) | U/p (mod p) | (V+W)/p² (mod p) |
|---:|---:|---:|---:|---:|
| 13 | 1 | 2041 | not applicable | not applicable |
| 19 | 2 | 1102 | 5 | 17 |
| 37 | 3 | 45214 | not applicable | not applicable |
| 43 | 4 | 11137 | 24 | 13 |
| 103 | 9 | 763951 | 60 | 0 |
| 211 | 18 | 2938597 | 163 | 152 |

At p=211, the independent seed value S_18≡2938597 (mod 211³) agrees with the inherited upper-half transport input at 7724e73f2d15c92ce98520e6a55b8231d737fa03. No native benchmark was performed; 79 bounded samples do not establish the displayed theorems, which instead follow from the exact rational algebra above.

## Durable continuation

Parent and frozen evidence: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7, frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3. Already established and not to repeat: original WZ certificate c7fb90f, same-prime p³ upper-half five-port 7724e73, independent hourly source/odd-product transfer, D24 accepted Result. New unreviewed author unit: valuation-support theorem and exact 103/1500 terminal contraction, with exact p=103 cancellation exception. No native session, winning CLAIM, run, checkpoint, Result or review is asserted by this author note. Recent own bridge recovery reference: private kimi-query-bridge issue 6186, recovery-status-20261023-1704-onhour-01; its Source authority_verified=false, no own claim/run. Its dispatch issue 6188 later returned FAILED/TimeoutExpired; never replay it under another ID. The Site gateway currently has research_authority_granted=false; issue #1539 and current control responsible path must be consulted before role-bound writes.

**Next exact science unit:** determine the p-adic LOW-seed cancellation mechanism for (13) and (19), retaining the p≡19 universal nonvanishing p² pair; combine with each original d_{p,k} from 7724e73 rather than suppressing this port. A finite-field hypergeometric identity establishing S_r≡0 (mod p), followed by a valid second- and third-digit lift, would be a genuine route; this is proposed, not proved. Preserve the independent native obligations (same-class CM/divided-power normalization, exact original native benchmark and formal Source/Driver admission). Current output is not the accepted task frontier and must be evaluated for overlap and source permission before registration.
