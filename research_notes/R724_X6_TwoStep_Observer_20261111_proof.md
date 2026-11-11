# R724 — X6 two-step signed paths: exact observer fibers and future-safe residual

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000). Scientific predecessor: R722 author PR #2093 at abd3541990c952919782f89336fa567e3c2fdd62.

## Typed setting

Let V={0,...,5}, U={+e_a,-e_a: a in V}; every ordered length-two native **Cell-coordinate** path P=(u1,u2) is in U^2 (144 paths). Its signed displacement v(P)=u1+u2 belongs to Z^6. For each 3-axis S, O_S(z)=can3(z|S), subtracting the minimum of its three coordinates. Define b_S(v)=1[O_S(z+v)!=O_S(z)], independently of z. The R722 identity gives b_S(v)=1[the three components of v on S are not all equal].

These are typed spatial observer changes. An admissible physical TRIADIC_CLOSURE_E, a V29 PASS/TRANSFER event, and a V39 j event have *not* been inferred from a Cell coordinate step. Each path step is an ordered discrete spatial adjacency, not a heartbeat interval.

## Theorem 1: 22 terminal observers, maximum ordered-path fiber 12

There are three exhaustive cases:

1. u2=-u1: 12 paths, v=0, one zero terminal mask b(v), fiber size 12.
2. u2=u1: 12 paths, v=+-2e_a; the six masks select exactly those 10 triples containing axis a, each mask has 2 paths (+,+ and -,-).
3. The axes differ: 120 paths, v=s e_a+t e_b with a!=b and s,t in {+-1}; the fifteen masks select exactly the 16 triples not wholly inside V\\{a,b}, each mask has 8 paths (two orders x four sign choices).

Therefore exactly 22 masks exist. Ordered-path fiber multiplicities are 1 fiber of size 12, 6 of size 2, 15 of size 8. Given the terminal mask, a fixed-length auxiliary code to recover the complete *ordered and signed* path needs at least ceil(log2 12)=4 bits; deterministic within-fiber indexing attains 4.

## Theorem 2: retaining the midpoint observer reduces worst-case path repair to 2 bits

Define the observer trace T(P)=(b(u1),b(v(P))). The first mask reveals the axis of the first step, but not its sign. Cancellations give 6 traces of size 2; same-axis doubles give 6 traces of size 2; different axes give 30 traces of size 4 (ordered axes known; four sign pairs remain). Hence exactly 42 trace signatures, with 12 size-2 fibers and 30 size-4 fibers. The optimum fixed-length auxiliary trace repair is exactly ceil(log2 4)=2 bits. This is a local path-provenance representation using an actual intermediate observation, not an assumption that endpoints determine the ordered history.

## Theorem 3: future observation classes at horizons 0, 1, 2 are 22, 67, 73

The 144 paths produce 73 distinct net displacements
W2={0} union {+-2e_a} union {s e_a+t e_b: a<b, s,t in {+-1}}.

Let Q_h be all net displacements of at most h appended signed unit steps (including 0). Define F_h(v)=(b(v+q))_{q in Q_h}; this is a *family of hypothetical allowed future readouts*, not an executed physical trajectory or a claim about the number of practical queries.

- h=0: |Q0|=1. F0 has 22 classes: 1 singleton, 6 doubletons, 15 fourtons (these are *net* displacements, not 144 paths).
- h=1: |Q1|=13. For v=s e_a+t e_b, adding +e_a produces a 10-triple observer iff s=-1 and a 16-triple observer iff s=+1; +e_b likewise reveals t. All four sign pairs for a!=b are distinguished. For v=+2e_a and v=-2e_a, any single appended unit step produces the same observer in the two cases: step on a leaves the same 10-triple mask, step outside a gives the same 16-triple mask. Thus 67 classes: 61 singletons and 6 doubletons.
- h=2: |Q2|=85. Appending -2e_a distinguishes +2e_a (observer zero) from -2e_a (observer on a). All 73 displacements are distinguished.

This gives exact finite-future observer-safe quotients for W2: sizes 22/67/73.

## Theorem 4: 2 bits are necessary and sufficient for arbitrary-future *endpoint* preservation

For each terminal mask b(v), at most four distinct net vectors in W2 are compatible: one for zero, two for a single selected axis, four for a selected axis pair. A two-bit within-fiber index determines v; then any future signed native coordinate increment q can be evaluated through b(v+q). Four different sign pairs under one chosen axis pair have distinct future readouts already at horizon 1. Consequently exactly 2 fixed additional bits are necessary and sufficient for terminal-mask-to-future-safe-net-vector reconstruction on W2.

**Do not conflate the three reconstruction targets:** (i) terminal mask -> ordered signed path: 4 bits; (ii) trace of two observed points -> ordered signed path: 2 bits; (iii) terminal mask -> arbitrary-future-safe *net displacement*: 2 bits. An event reading ordered branch identities or multiplicities continues to require the relevant provenance, even if its endpoint observer factors through v.

### Distinguishing witnesses

(+e0,+e1) and (+e1,+e0) have identical net v and all future endpoint observers, but different native order and different midpoint observations. (+e0,+e1) and (+e0,-e1) have identical terminal and midpoint masks, but appending +e1 gives respectively 16 and 10 changing triples. (+e0,+e0) and (-e0,-e0) remain identical under every single-step future observation, yet -2e0 separates them.

## Evidence, source and next question

A standalone stdlib Python verifier enumerates all 12² ordered paths, independently evaluates can3 before/after from three signed initial Cells, checks 720 S6 coordinate-permutation covariances for 73 net vectors, builds Q0/Q1/Q2, and asserts all stated exact fiber distributions. JSON evidence records coverage and results. This is finite exact native *coordinate combinatorics*, not BRC propagation, external classical pi/trigonometry, an implemented force closure, or a native-residual numerical attribution.

Applicable sources: pinned P000 foundation, pinned X6 native spatial Cell torsor, pinned P000 triadic force definition and joint-relation observer preservation; current EM continuation + portable protocol and current global math/output policies. Proof and code are author-side scientific artifacts; no formal Result or Driver acceptance is implied.

**Next unresolved unit:** select an actual admissible frozen X6 Cell/Link/Port + V29 PASS/TRANSFER + V39 j update; determine its typed relation to an ordered pair of Cell-coordinate steps; test whether triadic closure is sensitive to sign/order when b(v) is not. If sensitive, provide the smallest BRC branch/provenance repair; otherwise prove a safety certificate for the exact event subclass.