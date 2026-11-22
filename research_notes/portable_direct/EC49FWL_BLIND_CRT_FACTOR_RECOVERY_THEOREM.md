# EC49FWL — Blind CRT single-hole factor identification from indexed reflection defects

Date: 2026-11-22 (Asia/Shanghai).
Scientific lineage: frozen BRC16943; EC49FWK at d2e7c3f5d120a0eb87ae1a24ed443e2eb3ba4a56; source-dependent auxiliary CRT certificate, **not** native Farey evolution.
Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. Portable research; no authenticated Task CLAIM or current Activity association asserted.

## Problem

EC49FWK's sharp physical-observer budgets assume the mod-11 CRT factor V is known. We remove this knowledge assumption: let n,q be coprime positive integers with q odd and q>=3. Let U be any subset of Z/n, w=|U|, and V either Z/q or Z/q minus a single **unknown** element z. Identify what the complete indexed reflection-defect spectrum of W=U x V in Z/(nq) determines, before reading any physical membership probe.

For S subset Z/m, write Delta_S(c)=|S triangle (c-S)|, and K_U(a)=|U intersect (a-U)|. Define the row total R(b)=sum_{c mod nq : c mod q=b} Delta_W(c). All these are exact finite integer objects.

## Theorem 1 (blind one-hole inverse; all coprime n and odd q)

If V=Z/q minus {z}, then for c=(a,b) under CRT,

Delta_W(a,b) = (q-1) Delta_U(a) if b=2z,
and Delta_W(a,b) = (q-2) Delta_U(a)+2w otherwise.

Consequently, R(b) has a unique minimum at b0=2z mod q whenever w>0, and for each b!=b0,

**R(b)-R(b0)=2w^2**, independent of n,q,z and the geometry of U.

Therefore the *unknown* hole is uniquely determined by z=2^{-1} b0 (mod q); the support size by w=sqrt((max R-min R)/2), an exact positive integer; and the full indexed ten-cycle (or n-cycle) spectrum by

Delta_U(a)=Delta_W(a,b0)/(q-1).

All three are recovered from the indexed full spectrum without an a priori V or w. The formula does not assert recovery of U itself.

Proof: let k=|U intersect (a-U)|. The product identity for intersections under CRT gives |W intersect ((a,b)-W)|=k times |V intersect (b-V)|. For the q−1-element V, the latter is q−1 for b=2z and q−2 elsewhere. As |W|=(q−1)w and Delta=2(|W|-intersection), the formula follows. Subtract the exceptional row value from an ordinary row: 2w−Delta_U(a)=2K_U(a). Summing over a, sum_a K_U(a)=w^2 since each ordered (x,y) in U^2 contributes once to a=x+y. Thus the gap is 2w². For w>0 the gap is positive, and odd q makes multiplication by 2 invertible.

## Theorem 2 (factor-type classification and exact degeneracy)

For V=Z/q, Delta_W(a,b)=q Delta_U(a), so all R(b) coincide. For one-hole V with w>0, exactly one row sum is smaller. Thus **every nonzero indexed spectrum** identifies whether V is full or one-hole; in the latter case Theorem 1 reconstructs z,w,Delta_U. In the full case Delta_U=Delta_W/q, but w need not be determined by the spectrum.

The zero spectrum is genuinely ambiguous. Every reflection fixes W if and only if W is empty or full (compose reflections to generate all translations). Within the stated product family, this is W=empty (U=empty with arbitrary V) or W=Z/(nq) (U=Z/n and V=Z/q). No defect-only observer distinguishes those two words.

## Sharp limit: recovery of factors is not recovery of U

Even with z and w recovered, two supports can have identical full indexed spectrum. For n=10, U_A={0,2,3,4,7}, U_B={0,1,3,4,6}, each has w=5 and exactly the same Delta_U; with z=3 both produce the same 110-entry Delta_W. Their unknown one-hole factor is recovered as z=3 and row gap 50, but the original signed positions are not recovered. This preserves EC49FWI/EC49FWJ's separate membership-probe obligations.

The known-factor premise for the EC49FWK sampling counts is therefore derivable from a **complete indexed exact 110-center spectrum**, except in its explicitly identified all-zero case. This is a conditional interface improvement: if only a partial or noisy spectrum is observed, the inference needs separate robustness analysis. It does not prove any corresponding improvement for the frozen moving-Farey F_native/Y_native; those maps remain to be located, typed and checked.

## Exact computation and scope

The attached standalone Python standard-library verifier tests all 2^10=1,024 subsets U; all eleven possible one-hole locations (11,264 formula/decoding instances); all 1,024 full-factor 110-cycle cases by *direct* cyclic computation; and 3,584 directly computed one-hole cases (all U at z=0 plus every fourth U at z=1,...,10). It asserts the explicit indistinguishability witness. Output is ALL PASS.

The universal (n,q) theorem follows from the displayed combinatorial proof; numeric execution covers the stated n=10,q=11 case, not every coprime pair. This is an auxiliary residual-observer result. Frozen BRC16943 scientific input, P000 six-axis semantics, ACTIVE residual-fidelity worldview, provenance and previous non-reviewed status are unchanged.

Next discriminating unit: obtain the actual frozen moving-Farey state transition F_native and successor observer Y_native. On exact same-spectrum support doubletons, test whether the first successor observer factors through (Delta_U,w,z) or separates the supports. A novel native state transfer requires a declared X6/slice embedding and complete relation-preservation evidence; do not invent F_native from this CRT abstraction.
