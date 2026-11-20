# R762HB — Four-counter additive Link repair of signed X6 STAR candidates

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS. **Date:** 2026-11-20, Asia/Shanghai. **Source:** frozen taskbook enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8; P000 scientific input pinned by taskbook to enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Prior:** R762GU (integer STAR lattice) and R762HA (#2857@47701f9c54f37b95070bd426d1d4abca86c98267). **Status:** AUTHOR-PROVED_CANDIDATE_MODEL, integer checker PASS, independent review NOT_REVIEWED.

## Question and model boundary

Four auxiliary STAR labels v=0,1,2,3 select triples among six *native* X6 axes 01,02,03,12,13,23. These four labels are **not four extra spatial dimensions**. In a chosen signed relative Cell chart, let H_v have value 1 on the three edges incident to v, zero otherwise. A is the 6-by-4 incidence matrix with columns H_v. A signed **candidate composite** event (v,σ), σ=±1, has proposed raw Cell increment σH_v. Its actual primitive-force incidence, TRIADIC_CLOSURE_E admission, Port/Link gate, and time law are *not yet specified by P000*. The claim below is deliberately about typing this candidate without silently declaring a native stable interaction.

## HB1. Primitive straight-line typing and exactly six shortest local refinements

P000's spatial primitive steps have support on one signed native axis. Each H_v has support on three distinct native axes and L1 step distance exactly 3. Therefore σH_v **cannot itself be a primitive straight spatial step**. If represented by a shortest sequential native-axis path, it needs exactly three steps with signs σ, and these have 3!=6 distinct ordered realizations.

An event-boundary- and provenance-preserving composite word of length m has exactly 6^m *decorated shortest-path refinements* if all six local orders are permitted. This is not a claim that flattened, undecorated words are distinct, nor that an unestablished native Link/time gate admits all six orders. A separately typed simultaneous three-force interaction may have an independent Cell readout; three-axis spatial translation alone does not establish triadic balance.

## HB2. Conservative additive Link candidate and its precise minimum rank

Introduce relational Link state ℓ∈Z⁴, explicitly not extra spatial axes. For the abstract STAR candidate define

    (C,ℓ) --(v,σ)--> (C+σH_v, ℓ−σe_v),
    K(C,ℓ)=C+Aℓ.

Then K∈Z⁶ is invariant **at every event**. Event ordinal advances separately; Port, chirality and BRC event provenance stay independently typed. Conservation of K does not mean full (Cell,Link,Port,time,history) state has returned or that the force configuration is primitively stable.

This Link rank is minimal **among free abelian additive Link carriers** L′≈Z^r with fixed event increments d_v and a Z-linear decoder D:L′→Z⁶ satisfying D(d_v)=H_v for *all four candidate STAR types*. Since A has rank 4 (HB3), rank(D)≥4 and r≥4; the explicit choice L=Z⁴, d_v=e_v, D=A attains equality. If only a subset S of these types is legal, the corresponding minimum is |S|, because every subset of A's columns is independent.

The rank bound is not a minimum bit count and does not forbid nonlinear, variable-length or restricted-history encodings. It is the exact minimal additive linear **unrestricted-branch** repair interface.

## HB3. Exact integral image and inherited parity obstruction

In row order 01,02,03,12,13,23,

    A = [[1,1,0,0],[1,0,1,0],[1,0,0,1],
         [0,1,1,0],[0,1,0,1],[0,0,1,1]].

The GCDs of all integer minors of order 1,2,3,4 are (1,1,1,2). Hence its Smith invariant factors are (1,1,1,2), so coker(A)≈Z²⊕Z/2Z. If y=(a,b,c,d,e,f), it has an integral STAR lift precisely when

    e=c+d−b,   f=c+d−a,   a+b+d ≡ 0 (mod 2).

The unique lift is z0=(a+b−d)/2, z1=(a−b+d)/2, z2=(−a+b+d)/2, z3=c−z0.

The lattice and parity criterion reuse the R762GU result; they are included here as exact certificates for the new Link minimization/decoding theorem, not claimed as novel lattice discoveries.

## HB4. Positive BRC refinements and a sharp history-loss witness

For unrestricted signed candidate events there are 8 choices per composite event. Exact integer BRC DP gives raw-six-axis zero returns at lengths m=0..4 equal to (1,0,8,0,168), consistent with R762GU. When six native primitive-path orders per composite event are all admitted **and event boundaries retained**, the corresponding decorated zero-return counts are 8×6²=288 at m=2 and 168×6⁴=217728 at m=4. These values are *not* the original signed composite-source counts: observer scope differs.

For fixed v, (+v,−v) and (−v,+v) have identical final raw Cell C and additive Link ℓ, but different intermediate states and ordered BRC provenance. Therefore even this exact additive repair does not certify erasure of historical path identities when future Link permission or observers can inspect them.

## Checker / limitations / next experiment

R762HB_CHECK.js runs without dependencies; exact integer tests cover all minor GCDs, 625 inventory lifts, eight signed step conservation checks, shortest-path permutations for all four columns, and source DP through m=4. An independent local SymPy calculation of Smith form also returned diagonal (1,1,1,2). R762HB_EVIDENCE.json records exact results. There is no formal or independent mathematical review.

**Still open:** an actual frozen-P000-admissible primitive triadic force-event predicate; a native Link/Port transition; joint incidence and physical-time calibration. These cannot be declared legal merely because K is conserved. Next test: obtain one explicit typed native TRIADIC_CLOSURE_E incidence and its Link/time permission, and either show it factors through a STAR column with a legal update or preserve an exact failure witness. If actual admissible labels form a subset, recompute the minimal additive Link rank of its selected columns and retain path provenance whenever future operations require it.