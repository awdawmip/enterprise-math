# Stages 214 and 215 — exact all-real optimal segments in the external ternary-IID N14 decision problem

**Research strength:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED, 2026-10-28. These finite-statistics results are not native P000-X6 theorems, independently accepted Source Results, Driver reviews or physical claims.

## Statement and preserved parent

Independently observe symbols 0,1,2 under P=(3,1,20)/24 or Q=(2,2,20)/24, stopping at any ordered-history-adapted randomized time τ in [0,14], then declaring P or Q. Put eP=P(declare Q), eQ=Q(declare P), tP=E_Pτ, tQ=E_Qτ, and V14(α)=inf max(tP,tQ) subject to eP,eQ≤α. The infimum ranges over **all** history-dependent randomized tests, not merely count-only procedures.

The author-side Stage213 left frontier (reused at that evidence strength) is
α213=3747353537341061245/10517860061584293888 and V213=2068074187667448833/219122084616339456. Input is the Stage213 immutable PR #1571 head 1b73435b389e43385b3329e281e25780fee8d2c2, including its exact Stage214 dual candidate.

## Theorem A — Stage214

Let K214=265549752/2687315 and H214=2351021677817497415171339/29442503241037913260032. For **every real** 0≤δ≤1679571875/285315214344192, including irrational δ,

\[
\boxed{V_{14}(\alpha_{213}+\delta)=V_{213}-\frac{531099504}{2687315}\delta}.
\]

The right endpoint and its value are
\[
\boxed{\alpha_{214}=\frac{3747415453078661245}{10517860061584293888}},\qquad
\boxed{V_{214}=\frac{2067819259905528833}{219122084616339456}}.
\]

At K214, there are exactly two Bellman ties: T214=(7,2,2), declare Q / continue, and Z=(14,0,0), declare P / Q. With u=P(declare Q at T214 rather than continue) and z=P(declare P at Z rather than Q), the exact error-equalizing coin arc is

\[
z(u)=\frac{306764674289301629}{819200000000000000}+
\frac{138881259}{320000000000}u,\quad 0\le u\le1.
\]

The endpoint z values are 306764674289301629/819200000000000000 and 307120210312341629/819200000000000000, both strictly between 0 and 1. Balanced common error increases strictly from α213 to α214. The tP−tQ endpoint gaps are 190811148216681473/219122084616339456 and 190941031954281473/219122084616339456, both positive.

## Theorem B — Stage215

Let K215=15508584/157345 and H215=137345358024509431139809/1723888220197896585216. For **every real** 0≤δ≤24093453125/855945643032576,

\[
\boxed{V_{14}(\alpha_{214}+\delta)=V_{214}-\frac{31017168}{157345}\delta}.
\]

Its right endpoint is
\[
\boxed{\alpha_{215}=\frac{3747711513430661245}{10517860061584293888}},\qquad
\boxed{V_{215}=\frac{2066603386919928833}{219122084616339456}}.
\]

At K215 the two ties are T215=(9,3,1), declare P / continue, and Z=(14,0,0), declare P / Q. Now u=P(declare P at T215 rather than continue); the error-equalizing arc is

\[
z(u)=\frac{307120210312341629}{819200000000000000}-
\frac{127887501}{64000000000}u,\quad 0\le u\le1.
\]

Both endpoint z values (307120210312341629/819200000000000000 and 305483250299541629/819200000000000000) are strictly within (0,1); the balanced error rises strictly from α214 to α215. The two tP−tQ gaps are 190941031954281473/219122084616339456 and 190531627781481473/219122084616339456, both positive.

## Load-bearing universal proof (both theorems)

An actual ordered history h has state s=(n,a,b), where a counts symbol 0, b symbol 1, n−a−b symbol 2. Since all IID branch probabilities are strictly positive, the *exact* likelihood ratio at every individual history is

\[
\rho(s)=Q(h)/P(h)=2^{a+b}/3^a.
\]

For each stated positive K, the P-normalized conditional optimal Lagrangian obeys the exact recursion

\[
B_K(s)=\min\left\{K\rho(s)\ {\rm[declare~P]},\
 K\ {\rm[declare~Q]},\
 1+\sum_{j=0}^2 P_j B_K(s+e_j)\ {\rm[continue]}\right\},
\]

where continue is excluded for n=14. There are exactly Σ_{n=0}^{14}(n+1)(n+2)/2=680 count states. The count reduction is justified by the stated IID suffix law and the Lagrangian observer, **not** assumed as an unrestricted compression of native X6 spatial states. Backward induction at *every actual ordered history*, followed by integrating its positive P mass, proves for any arbitrarily history-dependent randomized policy:

\[
t_P+K(e_P+e_Q)\ge B_K(0,0,0)=H_K,\quad
\max(t_P,t_Q)\ge H_K-2K\alpha
\quad\text{when } e_P,e_Q\le\alpha.
\]

Exact rational Bellman enumeration gives respectively H214/H215, exactly 1,238 strictly positive alternative-action gaps per stage, no negative gaps, minimum strict gaps 1026961/348276024 (Stage214) and 1026961/244702944 (Stage215), and exactly the two asserted tie states.

At either T, a>0 or b>0, whereas at Z both counts vanish. Symbol counts cannot decrease; a path passing T cannot reach Z, and Z is terminal so it cannot reach T. Thus the two independent random choices never both affect a single ordered path. The four observable coordinates O=(eP,eQ,tP,tQ) therefore obey an *exact* multilinear expansion

\[
O(u,z)=O(0,0)+uD_T+zD_Z+uzM,\qquad M=(0,0,0,0).
\]

The accompanying fraction certificates contain all four deterministic corners, D_T and D_Z. At each stage, the executable verifier independently obtains those four corners from a rational **IID suffix DP** and from a distinct, **unmerged full ordered-history integer positive P/Q mass DFS**: exactly 125,176 and 109,534 total ordered policy-tree visits respectively. These counts cover each deterministic policy tree with its actual stopping rule (they do not pretend to enumerate 3^14 leaves irrespective of stopping).

The specified affine z(u) is obtained by solving eP=eQ from these exact coefficients, and its two endpoint values certify 0≤z(u)≤1 for every **real** u∈[0,1]. The shared error is strictly increasing; the affine tP−tQ remains positive by both endpoint inequalities. Every selected action is a Bellman minimizer. Consequently
tP+K(eP+eQ)=H_K and max(tP,tQ)=tP=H_K−2Kα,
matching the universal lower bound for every real α in each full interval.

The successor duals touch at the right endpoints. At Stage214's endpoint, H215=H214+2α214(K215−K214); at Stage215's endpoint, H216=H215+2α215(K216−K215). As successive K decrease strictly, each successor dual bound is strictly above the **fixed preceding supporting line** to the right of that endpoint. This is only supporting-line strictness, not Stage216 primal optimality.

## Stage216 is only a first-switch dual candidate

A separate exact scan, based on the Stage215 high-error tie policy, finds

\[
K_{216}=\frac{908057789003279736}{9275758227422879},\quad
H_{216}=\frac{10060422269700525971327026167740407}{127032717449378935977323595300864}.
\]

The ties at K216 are T216=(1,0,1) (declare Q / continue) and Z=(14,0,0) (declare P / Q). All 680 states have no negative gap and 1,238 strictly positive gaps; minimum 3387232024158932057/432769775858641842624. The exact Stage215 right-contact identity holds. The right-side margin slope between these two fixed dual lines equals 1951045645915544864832/1459494178293852896255>0. **No Stage216 primal policy has yet been proved.**

## Evidence and typing

Full Fraction/BigInt-equivalent integer arithmetic is used; no floating grid. Original executed proofs, individual scripts, corner certificates, logs, SHA256 manifest and a compressed reproducibility pack were generated locally. The accompanying REPRO_STAGE214_215.py is a standalone test of both full-real claims: complete Bellman states/gaps, four exact corners by the two methods, mixed term, error arcs and endpoints. See EXECUTION_PROVENANCE.md for source pins, exact execution status and native authority limitation.

Typed BRC reuse is provenance-preserving ordered paths, separate positive rational P and Q branch masses, multiplicity and the precisely scoped IID suffix observer. No native six-dimensional discrete X6 Cell embedding, safe readout/future-operation certificate, time evolution or physical parameter bridge is supplied. P000/ACTIVE worldview is not replaced or empirically proved by this external example. Formal CLAIM, Source Result, independent Driver review and Lean proof remain separate admission work.
