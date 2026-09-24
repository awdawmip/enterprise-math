# D25 LIFT — absolute zero mode collapses to a terminating/unit-core second-digit certificate

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24
Consumed canonical Source frontier: awdawmip/enterprise-math@5ce312f8bdcb145f5a20cf39ffec73523b8f731c

## 0. Consumed frontier and de-duplication

Consume the canonical first-digit-fiber tangent/torus checkpoint. Also consume the independently persisted Driver finite-Green calculation on issue #1516 only as cross-flow evidence to avoid repeating its endpoint telescope. That Driver note shows that the complete nonzero-mode Green pairing of the existing u=1 synchronized path is already determined and leaves exactly one absolute zero mode

    Z_C = Q^C_0
        = Delta_p - Gbar A_0 - hbar Y_0                    (mod p),

where A_0 is the full valuation-one weighted middle aggregate and Y_0 is the terminal reflected valuation-two aggregate. This Researcher unit independently returns to the original B_k source and identifies that zero mode with a strictly smaller terminating/unit-core carrier. No Driver authority or mathematical acceptance is imported.

Fix p=6m+1 with p congruent 13 or 19 mod 24 and retain

    B_0=1,
    B_{k+1}/B_k=(6k+1)(3k+1)/(36(k+1)^2),
    g=sum_{k=0}^{p-1} B_k,
    h=sum_{k=0}^{p-1}(12k+1)B_k,
    G=g/p.

The accepted first digit gives G h == 1 (mod p). The exact source valuation strata are

    v_p(B_k)=0, 0<=k<=m;
    v_p(B_k)=1, m<k<=2m;
    v_p(B_k)=2, 2m<k<p.

## 1. Four source coordinates that survive the JT2 observer

Define the truncated/unweighted low+middle sum

    S := sum_{k=0}^{2m} B_k.

Because g-S is p^2-divisible and p|g, also p|S. Hence

    G_T := S/p

is p-integral. Define the weighted unit-band sum

    H_0 := sum_{k=0}^{m}(12k+1)B_k.

For the valuation-one middle band write

    x_r := B_{m+r}/p  (mod p),  1<=r<=m,

and define its weighted first digit

    A := sum_{r=1}^m (12r-1)x_r  (mod p).

Finally define the complete valuation-two unweighted mass

    Y := sum_{k=2m+1}^{p-1} B_k/p^2  (mod p).

All four coordinates retain their source range and valuation provenance; no unsigned mass or fitted recurrence is introduced.

## 2. Exact source decomposition through the second digit

Since every high-band B_k is p^2-divisible,

    g = S + p^2 Y                              (mod p^3),

and therefore

    BOXED: G = G_T + p Y                       (mod p^2).      (G)

For the weighted sum, put k=m+r in the middle band. Since p=6m+1,

    12(m+r)+1 = 2p + 12r - 1.

Thus modulo p^2,

    (12(m+r)+1)B_{m+r}
      = p(12r-1)x_r                            (mod p^2).

Every k>2m term is already p^2-divisible and is invisible in h modulo p^2. Hence

    BOXED: h = H_0 + p A                       (mod p^2).      (H)

In particular

    G_T == Gbar  (mod p),
    H_0 == hbar  (mod p),

so accepted UR implies G_T H_0 == 1 (mod p). The following absolute unit-core second digit is therefore well-defined:

    BOXED:
    Z_T := (G_T H_0 - 1)/p                     (mod p).        (Z0)

## 3. Exact zero-mode decomposition of Delta_p

Multiply (G) and (H) modulo p^2:

    G h
      = G_T H_0
        + p(G_T A + Y H_0)                     (mod p^2).

Divide the difference from 1 by p and reduce modulo p. This gives the exact all-target identity

    BOXED:
    Delta_p
      = Z_T + Gbar A + hbar Y                  (mod p).        (D)

No finite-prime inference enters this formula. It is the direct source decomposition of the live divided second digit by valuation band.

Therefore LIFT is exactly equivalent to the smaller absolute certificate

    BOXED:
    Z_T
      = R_m - Gbar A - hbar Y                  (mod p).        (L)

The Green/curvature chain no longer appears in the live scalar certificate. All of its u=1 nonzero-mode content has been compressed to the two typed source aggregates Gbar A and hbar Y; the only remaining absolute coordinate is Z_T, built from the terminating ranges k<=2m in g and k<=m in h.

## 4. Relation to the Driver zero mode

Let

    Y_0 := sum_{r=1}^m B_{p-r}/p^2             (mod p)

be the terminal reflected aggregate used by the synchronized path, and let

    Y_c := sum_{k=2m+1}^{5m} B_k/p^2           (mod p).

Then Y=Y_c+Y_0. At s=0 the synchronized source pair is

    g_C = g - sum_{r=1}^m B_{p-r},
    h_C = h - M^h_0 - T^h_0.

Modulo the JT2 observer, h_C has the same weighted unit core H_0, while

    g_C/p = G_T + p Y_c                        (mod p^2).

Hence its absolute zero mode is

    BOXED:
    Z_C = Z_T + hbar Y_c                       (mod p).        (B)

Substituting (B) into the independently obtained Green decomposition

    Delta_p = Z_C + Gbar A + hbar Y_0

recovers (D) exactly. Thus the Driver Green result is independently reconciled with the original source, but the present reduction is stronger as a source interface: the abstract zero mode has been replaced by one terminating/unit-core second digit plus the complete labelled valuation-two mass.

## 5. BRC information audit

Observer:
    Delta_p=(Gh-1)/p mod p, equivalently LIFT Delta_p=R_m.

Population/source:
    B_k with source index k, valuation band 0/1/2, and weighted/unweighted role retained.

Safe compression:
    - all valuation-one weighted ports may be compressed to A only after (H);
    - all valuation-two unweighted ports may be compressed to Y only after (G);
    - the entire u=1 Green difference/curvature carrier may be dropped for this scalar observer after the exact finite-Green endpoint identity and (D) identify its endpoint contribution.

Forbidden compression:
    - do not reduce G_T or H_0 to only their mod-p values before Z_T is formed; Z_T is precisely their live second digit;
    - do not erase the distinction between A and Y, because they enter with different accepted unit coefficients Gbar and hbar;
    - do not infer (L) from finite regression;
    - do not identify Z_T with the previously defined supersingular Frobenius repair scalar without a source bridge.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 6. Exact regression

A deterministic modular checker reconstructs B_k modulo p^3 for every target prime p<5000 and verifies:

1. p|S and p|(G_T H_0-1);
2. G=G_T+pY mod p^2;
3. h=H_0+pA mod p^2;
4. Delta_p=Z_T+Gbar A+hbar Y mod p;
5. the already-observed Delta_p=R_m for all 166 targets, only as regression/falsification.

Counts: 166 target primes, 83 in each residue class, zero failures.

The proof of (D) and (L) is Sections 1-3; the finite checker is not substituted for it.

## 7. Narrow next action

Do not sum the u=1 local defect stream again. The live all-target problem is now the absolute terminating/unit-core certificate (L).

The next information-gain unit should work directly with

    G_T = (1/p) sum_{k=0}^{2m} B_k,
    H_0 = sum_{k=0}^{m}(12k+1)B_k,

and determine Z_T=(G_T H_0-1)/p modulo p from a terminating contiguous/WZ, parameter, or degree-p Frobenius deformation, while separately retaining the explicit correction Gbar A+hbar Y. If a Frobenius route is used, prove its source bridge to Z_T rather than identifying coordinates by analogy. A lawful u!=1 residue-torus deformation remains an alternative only if it carries a genuinely new source coordinate.
