# D25/LIFT GH-2 — S Clausen source conservation, true finite cutoff, and a W/S Gauss unit-gauge obstruction

2026-10-27 Asia/Hong_Kong · Independent TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923` (not CONTROL_PLANE_MAINTENANCE or on-hour Research). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; mother D25/LIFT/JT2 OPEN. **Frozen scientific Source** `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Status `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. No native session CLAIM/OPEN/checkpoint, Result, H0/B0 or independent review is asserted.

## Inputs and typed carriers

Consume, without recrediting: R23 genuine unchanged W/S upper-half source reduction and external proved S full/half truncation; R36's **different** PF Green operator; R47–R55 original two-source finite Green and precision; GH-1's W-side Gauss labelled source with its real finite cutoff. The existing companion `20261027_hourly_d25_s_clausen_port_filtration_gh2_check.py` is a prior author-side checker, not a new independent review. Here the genuinely new algebraic results are a **cutoff-aware S-port conservation identity** and a **unit-diagonal carrier-map obstruction for both frozen prime classes**.

Preserve the original S summand
\[
s_n=(8n+1)c_n,\qquad c_n=\frac{(4n)!}{(n!)^4\,2304^n}.
\]
Introduce an **auxiliary** S Gauss factor, not a native X6 or Hasse J/E source,
\[
u_k=\frac{(1/8)_k(3/8)_k}{(k!)^2\,9^k},\qquad
\frac{u_{k+1}}{u_k}=\frac{(8k+1)(8k+3)}{576(k+1)^2}.
\]
The classical Clausen identity
`2F1(1/8,3/8;1;z)^2=3F2(1/4,1/2,3/4;1,1;z)` gives an exact rational coefficient identity
\[
\boxed{c_n=\sum_{i+j=n}u_i u_j.}\tag{GH2.1}
\]
External proved input: V. J. W. Guo and W. Zudilin, *A q-microscope for supercongruences*, *Advances in Mathematics* 346 (2019), 329–358, DOI `10.1016/j.aim.2019.02.008`, arXiv `1803.01830`: `\sum_{n=0}^{p-1}s_n\equiv\sum_{n=0}^{(p-1)/2}s_n\pmod{p^3}` for all primes `p>3`. This is an S-only theorem, not a W/S equality.

## GH-2A: three true S Gauss valuation bands and terminal annihilator

For every prime `p\equiv19\bmod24` (so `p≥19`), set
\[
a=(p-3)/8,\quad b=(3p-1)/8,\quad h=(p-1)/2=a+b,\quad H=(3p-1)/4=2b.
\]
**All-prime theorem:** for all `0≤k<p`,
\[
v_p(u_k)=0\ (k≤a),\quad1\ (a<k≤b),\quad2\ (b<k<p).
\tag{GH2.2}
\]
Define labelled residues `α_j=u_j mod p` for `0≤j≤a`, `β_i=u_i/p mod p` for `a<i≤b`, `γ_k=u_k/p² mod p` for `b<k<p`; these are S-side, **not GH-1's W-side residues**. For `h<n<p` put
\[
M_n=\sum_{\substack{i+j=n\\a<i,j≤b}}\beta_i\beta_j,\qquad
B_n=\sum_{\substack{j+k=n\\0≤j≤a,\ b<k<p}}\alpha_j\gamma_k.
\]
Then for every such `n`
\[
\boxed{s_n/p^2\equiv(8n+1)(M_n+2B_n)\pmod p.}\tag{GH2.3}
\]
For `H<n<p`, `M_n=0` by support and `B_n=0 mod p` by the original factorial valuation `v_p(c_n)=\lfloor4n/p\rfloor=3`, hence
\[
\boxed{\gamma_n=-\sum_{j=1}^{a}\alpha_j\gamma_{n-j}\pmod p,\quad H<n<p.}\tag{GH2.4}
\]

**Proof.** In the exact recurrence `u_{k+1}/u_k`, steps `k=a` and `k=b` contribute precisely one `p` via `8a+3=p` and `8b+1=3p`; all denominators `576(k+1)^2` are p-units and no other numerator step below `p-1` contributes `p`. In (GH2.1), low-low and low-middle pairs have maximal degrees `2a` and `a+b=h`; at degree `n>h`, only middle-middle (valuation `1+1`) and both ordered low-high (valuation `0+2`) survive after dividing by `p²`. Above `H=2b` middle-middle is absent and the exact original factorial coefficient has valuation three, so the **aggregated** low-high coefficient vanishes. Since `α_0=1` and `n-a>b`, solving this coefficient equation yields GH2.4. Individual low-high terms have not been erased. QED.

## GH-2B: real cutoff and S-only conservation

Define the **distinct weighted S high ports**
\[
G_{MM}=\sum_{n=h+1}^{H}(8n+1)M_n,\qquad
G_{LH}=2\sum_{n=h+1}^{H}(8n+1)B_n,
\]
and the **separate lower-degree low-high port**
\[
G_{LH}^{low}=2\sum_{n=b+1}^{h}(8n+1)B_n.
\]
The source decomposition GH2.3, terminal gap GH2.4 and independently proved Guo–Zudilin half/full equality give the **all-prime summed constraint**
\[
\boxed{G_{MM}+G_{LH}=0\pmod p.}\tag{GH2.5}
\]
This does **not** prove either port is individually zero.

Write the S-source moments
\[
A=\sum_{j=0}^a\alpha_j,\quad J=\sum_{j=0}^a j\alpha_j,\quad
C=\sum_{k=b+1}^{p-1}\gamma_k,\quad C_1=\sum_{k=b+1}^{p-1}k\gamma_k,
\]
and retain the actual upper-cutoff correction
\[
E=\sum_{\substack{0≤j≤a,\ b<k<p\\j+k≥p}}
     (8(j+k)+1)\alpha_j\gamma_k.
\tag{GH2.6}
\]
**New exact finite rectangular identity**, all such primes:
\[
\boxed{2\{AC+8(JC+AC_1)-E\}=G_{LH}^{low}+G_{LH}\pmod p.}\tag{GH2.7}
\]
**Proof.** Expand the full ordered rectangular weighted product as
`2\sum_{j,k}(1+8j+8k)α_jγ_k=2\{AC+8(JC+AC_1)\}`. Excluding the genuine indices `j+k≥p` subtracts **exactly `2E`**. Group remaining degrees into `b+1..h`, `h+1..H`, and `H+1..p-1`; the last vanishes only as the complete degree sum by GH2.4. Thus GH2.7 holds. Combining GH2.5 and GH2.7 proves the new S-side cutoff conservation:
\[
\boxed{G_{MM}+2\{AC+8(JC+AC_1)-E\}-G_{LH}^{low}=0\pmod p.}\tag{GH2.8}
\]
If a separately pinned, accepted CM0 root yields `A=0` in the actual frozen scope, this condition may be specialized to `G_MM+16JC-2E-G_LH^low=0`; the theorem itself **does not require** that input or the open W/S lift.

## GH-2C: no rank-diagonal p-adic **unit** gauge between the W and S Gauss carriers

GH-1's **different** W Gauss factor is
\[
t_k=\frac{(1/6)_k(1/3)_k}{(k!)^2\,2^k},\qquad
v_p(t_k)=0,1,2
\]
in the consecutive intervals `k≤m`, `m<k≤2m`, `2m<k<p` for `p=6m+1`.

**Theorem (both frozen classes).** For every `p≡19 mod24`, take `i=(p+5)/8=a+1≤m`. Then `(v_p(t_i),v_p(u_i))=(0,1)`. For every `p≡13 mod24`, take `i=m+1`. The first S roots are `(5p-1)/8` and `(7p-3)/8`, strictly after `m`, and `(v_p(t_i),v_p(u_i))=(1,0)`. Thus **no** `u_k=g_kt_k` can hold for all `0≤k<p` with `g_k∈Z_p^×` everywhere, even allowing the unit multipliers to depend on `k` and `p`.

**Proof.** A p-adic unit preserves valuation. The explicit S- and W-factorial numerator zeros occur at the stated different integer ranks, giving the opposite valuation pairs; their existence contradicts a global unit-valued rank-diagonal gauge. This is an obstruction **only to that typed interface**, not to a valuation-shifting, nonlocal, rank-mixing, or native PF/Hasse WZ intertwiner. QED.

## Exact checking, boundary and next step

A new standalone Python-stdlib author checker was **actually executed** on all **77 frozen-target-class primes `p<2000`** (37 of the 19-class and 40 of the 13-class). For all 37 of the 19-class it checked original S factorial terms independently modulo `p³`, GH2.3, every terminal GH2.4 step, GH2.5, the **new finite cutoff** GH2.7 and GH2.8, and the two-carrier valuation mismatch. Every check passed. A previously published checker separately covered the classical S Clausen identity and the smaller prime set. This is not independent replication, formal checking, or native H0/B0.

**Finite conjectural observation, explicitly not a theorem:** in the tested 37 primes both `G_MM` and `G_LH` separately happened to be zero. Only their **sum** is proved for all primes here; separate zero identities remain `CONJECTURE / UNPROVED`.

BRC `COMPOSE_APPLIED`: labelled S source pair (middle-middle vs ordered low-high), exact valuation, cutoff and future W/S operator. An aggregate cancellation cannot delete the nonzero individual source terms. The Gauss auxiliary index is not a native X6 dimension; P000, six native spatial axes, one independent time axis and the three-dimensional slice rules are unchanged.

**Next smallest open science unit:** prove or refute the separate S-port zero conjecture; more importantly seek a **p-adic filtered rank-mixing** W-GH1 / S-GH2 / R23 low-half and R36 PF-Green intertwiner, respecting all six fixed `z=2` Hasse J/E channels, both finite endpoints, positive-direction infinity and source `η/κ`. GH2 does **not** prove the still open `L_p/p²+U_p=0 mod p`. Original H0/B0, `[X]U mod p²`, semilinear normalization, native `p=373` experiment and independent Driver review remain open.

**Control:** exact own-session recovery/read continuation previously returned SUCCEEDED through `awdawmip/kimi-query-bridge#6622/#6623` but `execution_authorized=false`, no active claim/open/run. Historical service session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94` / Researcher `EM-ENTERPRISE-5298BA`, 16 prior contributors and two **neutral** preserved staging manifests remain provenance, not current authorization. Read-only gateway `0.6.11` reports `research_authority_granted=false` and `executor_binding_configured=false`; Source checkpoint vs predecessor claim CAS conflict remains owned by `awdawmip/enterprise-math#1558`. No unauthorized native publication, claim, session close or Research-Activity semantic checkpoint is asserted. Reuse the same genuine logical lane; never borrow maintenance identity or alter the scientific frozen pin.
