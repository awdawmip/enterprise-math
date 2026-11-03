# PREFIX-469 — Closed rational series for full-history BRC observer states

Date: 2026-11-03 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Continuation: PREFIX-468 at Enterprise Math commit 621a2afb5a676bace3f83d79522ddb9158a762f0. Current rules are read independently from main.

## Typed native object and observer

Fix a chosen affine X6 chart of P000/ACTIVE Heartbeat World. Restrict the native signed primitive alphabet to the eleven symbols x=+E1, and ±E2,...,±E6. Put a=+E2 and b=+E3. Each of ten non-x letters is always legal. Initial x is legal; later x is legal exactly after the ordered two-letter suffix ab. Length n is an ordered-path parameter.

Retain the BRC base observation f=(s,y1,...,y5,A,C), where s=#x, yi=#(+E(i+1))−#(−E(i+1)), pi=min(#positive_i,#negative_i), A=p2+2p4+p5, C=p3+p5. For a fixed n, this exactly determines the individual positive rational weight of PREFIX-466/467; a separate integer coefficient records multiplicity. The history state q is 0 (suffix neither a nor ab), 1 (suffix a), or 2 (suffix ab, also the exceptional empty start). Write B_n=#{f} and F_n=#{(f,q)} among legal n-letter paths. By PREFIX-467, (f,q) is the exact observer quotient for all legal future endpoint/weight/count histograms up to horizon H≥2. This is an internal signed-path observation, not a final Cell address or a complete path-provenance readout.

## Theorem A: exact suffix-state occupancy for every n

Define Qj(n)=#{f : there exists a legal n-letter word with base f and q=j}. Then:

* n=0: (Q0,Q1,Q2)=(0,0,1).
* n=1: (Q0,Q1,Q2)=(10,1,0).
* Every integer n≥2: (Q0,Q1,Q2)=(B_n−3, B_(n−1), B_(n−2)).

Moreover, at n≥2 the exactly three base keys **without** any q=0 representative (listed as s,y1,...,y5,A,C) are
(0,n,0,0,0,0,0,0), (0,n−1,1,0,0,0,0,0), (1,n−1,0,0,0,0,0,0).

**Proof.** Appending the ordinary letter a sends every legal prefix of length n−1 to state q=1. At the base-key level this append map is injective: subtract the +E2 signed coordinate, and reverse its deterministic pair-cancellation/valuation update, recovering the previous key. Conversely any q=1 word ends with a, and deleting a yields a legal prefix. Hence Q1(n)=B_(n−1) for n≥1. Similarly, appending ab creates q=2 and is injective on the base-key population (reverse first +E3, then +E2). Every nonempty q=2 word ends in ab, so Q2(n)=B_(n−2) for n≥2. The empty start is counted separately.

To prove the q=0 count, fix a **complete unordered eleven-letter count vector** of length n, supported by at least one legal word. By the Parikh-support theorem of PREFIX-468, its x-count s satisfies s≤1+min(a_+,b_+). If any ordinary letter c distinct from a,b has positive count, a valid q=0 representative is constructed as follows: when s=0 arrange ordinary letters ending in c; when s≥1 begin with x, append all ordinary letters unused by the required s−1 ab blocks, keeping one c for the end, then append (abx)^(s−1), and finally append c. Every x after the first is immediately preceded by ab; the final c resets the suffix to 0.

If the count vector uses only x,a,b, inspect cases. When s=0, b_+≥2 permits a word ending bb, and a_+=0,b_+≥1 permits an all-b word ending b. The two remaining q=0-deficient vectors of length n≥2 are a^n and (n−1)a+1b: their final letters are respectively a, or a/b with an ab suffix when b ends the word. When s=1, a_+,b_+≥1 permits a word ending abx (place unused a,b before this suffix). If a_+=0,b_+≥1, use x followed by b's. The single x word is q=0. The only further q=0-deficient vector of length n≥2 is x+(n−1)a: x must be first, so the path ends a. For s≥2, legality forces a_+,b_+≥s−1 and the explicit word x + unused a,b + (abx)^(s−1) is valid and ends x, giving q=0.

The three exceptional count vectors have no signed cancelling pairs, since n=s+Σ|yi|. For fixed n their base keys therefore admit no alternative Parikh realization: any alternative cancelling pair would add two steps. Thus precisely the three base keys listed above lack q=0, and every other base key admits q=0. At n=1 only a lacks q=0, and at n=0 the empty path has q=2 by convention. This proves the table. QED.

## Theorem B: rational generating function and asymptotic

For every integer n≥2,

    F_n = B_n + B_(n−1) + B_(n−2) − 3,

with F_0=1 and F_1=11. Set G(z)=Σ_(n≥0)B_n z^n. PREFIX-468 proved

    G(z)=(1+2z²)(1+z)²(1+z−z³)/((1−z)^8(1−z³)).

Then, as a formal power-series identity over Q,

    F(z)=Σ_(n≥0)F_n z^n=(1+z+z²)G(z)−z−3z²/(1−z).

**Proof.** Every distinct reachable pair (f,q) contributes once, hence F_n=Q0(n)+Q1(n)+Q2(n). Insert Theorem A and sum, adjusting n=1 by −z and subtracting 3 for every n≥2. The rational function is exact for every n. Its denominator may be chosen as D(z)=(1−z)^8(1−z³), the same integer denominator as G, since (1−z) divides D. Thus F_n obeys the corresponding constant-coefficient integer recurrence after finitely many initial coefficients. Since G_n=n^8/10080+O(n^7) by PREFIX-468, the stated convolution yields

    F_n=n^8/3360+O(n^7) as n→∞.

For H≥2, the exact minimal fixed-width dense code on the declared states needs ceil(log2 F_n) bits at fixed n, with the dictionary known; for H=0 it needs ceil(log2 B_n) bits and the H=1 population is B_n+B_(n−2) for n≥2. Dictionary creation, weight recovery, and overall storage are separate implementation costs. QED.

## Exact executed verification and numerical results

The accompanying Python standard-library program uses arbitrary-precision integers only. At every length 0≤n≤8 it independently enumerates every reachable (11-letter Parikh count, suffix-state) pair using exact deterministic gate transitions, projects to the base valuation key, and compares all three Qj populations, their exceptional sets, B_n, and F_n to the analytic formulas. It separately exhausts all nonnegative 11-vectors of total n and checks the PREFIX-468 legality criterion elementwise against the transition-derived support. At n=8 there are exactly binomial(18,10)=43,758 such full inputs, of which 36,475 are legal. A second, literal ordered-word enumeration at n=0,...,5 compares the full (f,q) set plus exact path count/positive integer mass with the PREFIX-466 recurrence.

New exact row at n=8: B8=33797, Q0=33794, Q1=15863, Q2=6869, F8=56526. Additional checked finite rows: F2=74, F4=1270, F6=10493. Analytic recurrence outputs (no independent large-n enumeration): F9=117013, F10=228060, F12=747822, F16=5230846, F20=24834662. Actual execution log ends ALL_CHECKS_PASS. Theorems A/B supply the all-n analytic proof; program verifies the specified finite input universe.

## Reuse, authority and next question

Frozen science: Enterprise Math commit f42f2906d77f24085c123f3ccfe9667d41caa96d; P000/ACTIVE X6 Heartbeat World, joint observer preservation, typed positive BRC. Reused: PREFIX-465 exact valuation key, PREFIX-466 gate automaton, PREFIX-467 future quotient and PREFIX-468 closed G. Relative signed coordinates and weighted histograms retain their declared observer scope; the full history remains richer provenance.

Next PREFIX-470: repeat the explicit reachable-history analysis for the overlapping gate pattern aba (or aa); calculate the base-fiber occupancy of its minimal suffix automaton and determine the resulting generating series, with an exact finite certificate and attention to future-horizon observer equivalence. Independently retain the arbitrary-degree X6 moment rank question beyond the finite-degree PREFIX-459/460 certificates.

Native control check: GitHub authenticated as awdawmip with admin/push; native task listing returned CONTROL_QUOTA and researcher session start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Actual native owner is unconfirmed. This is persisted author-side scientific Source, not a CLAIM, official Result/Review or Admission.
