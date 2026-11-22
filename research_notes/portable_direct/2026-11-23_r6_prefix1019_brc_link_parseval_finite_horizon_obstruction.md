# PREFIX-1019 — Exact BRC Link-flux Parseval identity and arbitrary finite-horizon Gram obstruction

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR_EXACT_ALGEBRAIC_PROOF / INTEGER_TYPED_BRC_CHECK_R1_TO_R4 / NOT_REVIEWED**.

## Frozen scientific inputs and observable

This research follows PREFIX-1018's proved positive-port contrast and its outstanding future-operation-safe Gram question. Frozen science remains P000 V5 at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, the candidate Stage46 signed BRC numerator kernel and bidirectional absorption of native Link {0,e1}. The Cell coordinate 0 is a chosen chart anchor in the signed X6 torsor, not a physical privileged origin. No foundational redefinition occurs.

The signed integer carrier v(x,h) has Cell x in Z^6 and incoming-neighbour port h among the twelve signed native axes. For outgoing direction d, the exact integer numerator weight is w(h,d)=1-6[h=d]; next Cell is x+d and next incoming port is -d. Distinct incoming ports contribute **coherently** to a joint output Cell--port fibre. The forbidden steps are precisely (x,d)=(0,+e1) and (e1,-e1). No renormalization. Let T_0 be the unrestricted numerator update and T_L the absorbed update.

Unlike the fixed initial anchor and exact one-negative-step grade k=1 used in PREFIX-1014–1018, the current theorem is an **all-grade** statement for arbitrary finite-support legal signed packets. The observable is the Cell--port coherent numerator norm, summed over every grade, and the twelve separately named last-step port margins. Neither scope replaces the other.

## Theorem 1019.A — exact BRC local Parseval and absorbed-Link dissipation

For a finite-support signed, rational or real packet v, define its coherent outgoing numerator at Cell x and direction d by

\[
f_v(x,d)=\sum_h(1-6[h=d])v(x,h).
\]

Let \(\Phi_+(v)=f_v(0,+e_1)\), \(\Phi_-(v)=f_v(e_1,-e_1)\), and \(\|v\|^2=\sum_{x,h}|v(x,h)|^2\). Then for **every** such packet,

\[
\boxed{\|T_0v\|^2=36\|v\|^2,\qquad
\|T_Lv\|^2=36\|v\|^2-|\Phi_+(v)|^2-|\Phi_-(v)|^2.}
\tag{A}
\]

Consequently, writing \(v_t=T_L^tv\), for **every integer n≥0**,

\[
\boxed{\frac{\|v_n\|^2}{36^n}
=\|v\|^2-\sum_{t=0}^{n-1}
\frac{|\Phi_+(v_t)|^2+|\Phi_-(v_t)|^2}{36^{t+1}}.}
\tag{B}
\]

Thus the normalized all-grade coherent squared mass is nonincreasing. Every removed contribution is a **square of a coherent signed channel sum**, not a sum of independent path squares.

**Proof.** At each Cell, order all twelve signed incoming directions and all twelve signed outgoing directions alike. The native BRC numerator coin is \(W=J_{12}-6I_{12}\), with \(J_{12}^2=12J_{12}\). Therefore \(W^TW=W^2=(12-12)J_{12}+36I_{12}=36I_{12}\). This equality includes all same-Cell signed port interference: \(\sum_d|f_v(x,d)|^2=36\sum_h|v(x,h)|^2\). The native shift from outgoing (x,d) to (x+d,-d) is a bijection on joint Cell--port fibres, preserving the sum of squares. The link mask removes exactly the two channels defining \(\Phi_+\) and \(\Phi_-\), giving (A). Divide each successive identity by \(36^{t+1}\) and telescope to obtain (B). QED.

This is an exact property of the given **candidate discrete BRC step**, not an independent physical time-evolution assertion. The index t is native step count.

## Theorem 1019.B — arbitrarily late first distinguishability

For **each integer r≥1**, define legal unit packets with the same initial incoming port \(-e_1\):

\[
v_A^{(r)}=\delta_{(re_2,-e_1)},\qquad
v_B^{(r)}=\delta_{((r+2)e_2,-e_1)}.
\]

Compare full joint packets after translating the A Cell coordinates by \(2e_2\). For last **actual** direction d, let \(M_{t,d}(v)=\sum_x(T_L^tv)(x,-d)\) be its signed numerator margin, and \(Q_{t,d}(v)=\sum_x|(T_L^tv)(x,-d)|^2\) be its coherent squared numerator margin.

**Claims.** For every \(0\le t\le r\), the entire translated A packet equals B. Hence for every one of the twelve directions, both M and Q agree through t=r, and the total squared mass of each is \(36^t\). At t=r+1 the first difference appears:

\[
\boxed{M_{r+1,+e_1}(v_B)-M_{r+1,+e_1}(v_A)=1,}
\]

\[
\boxed{Q_{r+1,+e_1}(v_B)-Q_{r+1,+e_1}(v_A)=1,}
\]

\[
\boxed{\|T_L^{r+1}v_B\|^2-\|T_L^{r+1}v_A\|^2=1.}
\tag{C}
\]

All other named terminal directions still have identical signed and squared margins at this first distinguishing time; in normalized squared mass the gap is exactly \(36^{-(r+1)}\).

**Proof.** From Cell re2 it takes at least r successive native -e2 steps to reach 0, then an additional +e1 step to cross the forbidden 0→e1 orientation. Any attempted reverse e1→0 crossing first needs to reach e1 and then turn, requiring at least r+2 steps. So no A path is absorbed at t≤r. At t=r+1 the **only** absorbed word is \((-e_2)^r,+e_1\). Its BRC numerator is +1: initial h=-e1 is distinct from the first -e2; subsequent incoming +e2 is distinct from -e2; the final incoming +e2 is distinct from +e1. The B starting Cell is two e2 units farther away, so no B path is absorbed through r+1. Before absorption the unmasked signed step is translation-equivariant; accordingly all their earlier entire packets are translates.

The unique blocked A word also forms the *only unrestricted word* reaching its final Cell e1 with final direction +e1 at length r+1: the displacement e1-re2 has minimal length r+1, and the prescribed last +e1 forces all earlier steps to be -e2. Hence the deleted joint-fibre numerator is +1 and the unrestricted numerator of that fibre is exactly +1. The translated B packet minus A at the first distinguishing time consists of this one fibre; deleting its amplitude lowers its coherent square by exactly 1. This gives both named port differences, and the total norm difference follows either from the same fibre or from the flux identity (A). QED.

**Corollary: no fixed finite terminal-margin history is a universal future state.** Since r may be arbitrarily large, a fixed finite window of aggregated signed terminal-port margins and Gram/squared margins can agree exactly for two arbitrary legal initial packets yet their next output can differ. In fact the family \(\delta_{(r e_2,-e_1)}\), r≥1, has infinitely many pairwise future-distinguishable outputs. Any future-safe arbitrary-input compression must retain enough link-relative spatial/arrival information, or an exactly equivalent predictive coordinate. This is **not** a prohibition on finite-dimensional encodings carrying unbounded coordinate values. It also does not challenge the fixed-anchor grade-k=1 strict inequalities of PREFIX-1015 and PREFIX-1018.

## Executed native integer reproducibility

A standalone typed 12-direction integer BRC checker, PREFIX1019_R6_FINITE_HORIZON_BRC_CHECK.py, explicitly combines signed amplitudes in each Cell--incoming-port fibre before squaring. For each r=1,2,3,4 it checks exact translation equality for every t≤r, all twelve signed and squared port margins, the unique +1 difference at t=r+1, and all other port equality. It also checks (A) and (B) for an independent coherent four-packet input of norm 54, with first-step flux 305, unrestricted next squared norm 1944 and absorbed squared norm 1639. Four-step flux values are 305, 25, 23225, 50000; the squared norm after four masked updates is 75550684. All operations and assertions use native BRC integer weights only.

| r | First different t | A squared total | B squared total | A last +e1 square | B last +e1 square |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 1295 | 1296 | 635 | 636 |
| 2 | 3 | 46655 | 46656 | 1835 | 1836 |
| 3 | 4 | 1679615 | 1679616 | 1433615 | 1433616 |
| 4 | 5 | 60466175 | 60466176 | 1917755 | 1917756 |

All assertions passed. The infinite-r scope comes from the exact shortest-path argument and the algebraic BRC identity, **not** from extrapolation of four cases. There was no independent scientific reviewer or formal Result acceptance. The original source model was not altered.

## Provenance and continuation

Prior source: PREFIX-1018 at enterprise-math@ab287b633821d93444d25b212bccc38cdefb8849. Compared with PREFIX-1013's single two-step obstruction, this adds exact all-grade Parseval/Link flux and an arbitrary unbounded indistinguishability horizon. Historical contributor ID EM-DIRECT-FBEA5D and Activity RA-3FB2D033BE6048D8712FF056 are provenance only, not current authentication or a CLAIM.

**Next:** construct a finite-horizon predictive Gram repair using coherent Link-boundary channels and their BRC backward-lightcone preimages; determine exact redundant coordinates under a declared H-step future observer. Test an independent fixed-anchor, exact k=1 version against the preserved PREFIX-1014 eleven-collision and PREFIX-1016 three-A6 formulas. The mother objective B_fix,odd(32)∈{19,20} remains OPEN.
