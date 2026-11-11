# R725 — Three-step X6 Cell observers: permanent diagonal fibers and sharp future horizon

Author-side mathematics, 2026-11-11. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS (TP2-8B7E13C5904A2D6F1142). Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor R724 Draft PR #2097. Researcher EM-X6-8D905C, activity RA-FCCEA18E331FD60455AF367E; registration does not establish a CLAIM.

## Typed setting

This model concerns signed native **Cell-coordinate steps**, not actual three-force closure. Let U={+e_a,-e_a:0<=a<6}. The 1,728 length-three ordered paths are P=U^3. For a path (u1,u2,u3) put v_k=sum_{i<=k}u_i and v=v_3. For any three-axis S, the native coordinate readout O_S(z)=can_3(z|S) subtracts the minimum coordinate. Define

    b_S(v)=1[O_S(z+v)!=O_S(z)]
          =1[the three components of v on S are not all equal].

The equivalence is exact: two canonical triples coincide exactly when their source coordinates differ by a common scalar. The starting Cell cancels. Terminal observation b(v) has 20 bits. Full three-prefix trace is (b(v1),b(v2),b(v3)). A future horizon h observes (b(v+q)) for all net q realizable by at most h appended signed unit Cell steps, including zero. Future here is hypothetical spatial coordinate continuation, not physical time.

## Theorem 1: 51 endpoint masks and optimal path residuals

Exactly 51 distinct terminal masks occur among 1,728 paths. Their path-fiber histogram is 68:6, 24:25, 36:20; terminal mask weights are 10:6, 16:15, 18:10, 19:20.

Exhaustive symbolic case split supplies the count.

1. One active axis a: four net vectors ±e_a, ±3e_a. Each ±3e_a has one ordered path. Each ±e_a has three one-axis sign orderings plus 5 choices for a second axis with a cancelling signed pair, 2 choices of that pair's first sign and 3 positions for the lone a-step: 3+5*2*3=33 paths. Thus six masks, each with 2*33+2*1=68 ordered paths.
2. Two active axes {a,b}: a net has coefficients ±2 on one axis and ±1 on the other. There are 2 choices for the doubled axis and 2^2 sign assignments, each with three orders, giving 24 paths for each of C(6,2)=15 masks.
3. Three active axes, same sign: for each three-subset H there are two net signs and six orders. The mask detects the two size-three equality classes but cannot distinguish H from its complement Hc. Therefore 10 masks, each containing four net vectors and 24 ordered paths.
4. Three active axes, mixed signs: for a fixed triple H, the other three coordinates equal zero, giving exactly one all-equal triple (the complement Hc). The six assignments (choose one odd-sign axis in H and reverse all signs), each with six orders, produce one of 20 masks with 36 paths.

Check 6*68+15*24+10*24+20*36=1728. A fixed auxiliary code recovering the entire signed ordered path from the terminal mask requires ceil(log2 68)=7 bits, and an index within each fiber achieves that bound. Full-prefix traces have exactly 402 masks with fiber histogram 2:120, 4:132, 6:120, 8:30, established by exhaustive finite integer enumeration. Thus prefix trace requires exactly 3 auxiliary bits in the worst case.

## Theorem 2: 304 net states but only 284 future-safe classes

The distinct net vectors W3 consist of 24 single-axis states (±e_a,±3e_a), 120 doubled/single two-axis states (±2e_a±e_b, a!=b), and 160 triple-axis states (±e_a±e_b±e_c, a<b<c).

For arbitrary integer v,w∈Z^6, b(v+q)=b(w+q) for every integer q iff v-w belongs to Z(1,1,1,1,1,1). The forward direction for a diagonal difference follows from the three-axis relative-readout definition. For the converse, choose q=-v. Since b(0)=0, equality implies b(w-v)=0, which forces all six components of w-v equal.

For v,w∈W3, a nonzero diagonal difference c*1 obeys 6|c|=||v-w||_1<=||v||_1+||w||_1<=6. Thus |c|=1. Equality forces each vector to have exactly three nonzero unit entries, on complementary supports, all + in one and all - in the other. For every 3-subset H there is exactly one pair

    v=sum_{i∈H} e_i,
    w=-sum_{j∉H} e_j,
    v-w=(1,1,1,1,1,1).

This yields exactly C(6,3)=20 permanent two-state classes and 304-40=264 singleton classes. The future-safe quotient has 284 classes. Example: v=(1,1,1,0,0,0) and w=(0,0,0,-1,-1,-1). All future three-axis coordinate observations agree, although their signs, net displacements and ordered source paths differ.

## Theorem 3: h=3 is necessary and sufficient for the complete future-safe quotient

For n>=3 and any length L, let W_L be signed-axis-step net displacements and Q_L all nets of at most L appended signed steps. For every v∈W_L, the continuation q=-v lies in Q_L (reverse its primitive steps). Hence b(v-v)=0, whereas b(w-v)!=0 if w-v is not diagonal. Thus horizon L distinguishes all different diagonal-equivalence classes in W_L.

For L=3 the horizon bound is sharp. Take v=+3e_0 and w=-3e_0. If ||q||_1<=2, for every j!=0 we have |q_0-q_j|<=2. Hence the distinguished coordinate 0 of each v+q and w+q is never equal to any other coordinate, while equality relations among coordinates other than 0 are identical. Their b masks coincide. But q=-3e_0 yields b(v+q)=b(0)=0 and b(w+q)=b(-6e_0)!=0. Therefore h=3 is optimal.

Exact finite integer enumeration gives the horizon partition of all 304 net vectors:

| h | distinct future net increments | observable classes | fiber sizes |
|---|---:|---:|---|
| 0 | 1 | 51 | 4:16, 6:20, 8:15 |
| 1 | 13 | 218 | 1:132, 2:86 |
| 2 | 85 | 278 | 1:252, 2:26 |
| 3 | 377 | 284 | 1:264, 2:20 |

The remaining 20 pairs at h=3 exactly equal the algebraically classified permanent diagonal pairs. Six additional h=2 pairs are ±3e_a (a=0,...,5). The largest terminal fiber of net states has eight vectors and they are future-distinct for any given two-axis mask; hence 3 fixed auxiliary bits are necessary and sufficient to reconstruct the future-safe net class from the terminal mask.

## Verification and mathematical interface

The companion stdlib Python program enumerates all 12^3 ordered paths, all 304 distinct nets, 377 future-net increments, 720 axis permutations and three starting Cells to independently validate min-normalized can3 readouts; it verifies the observed h=3 partition against the mathematically identified diagonal quotient and exports JSON. Exact integer and bitwise arithmetic only. Run: python3 research_notes/R725_X6_ThreeStep_Observer_20261111_verify.py ; expected R725_X6_THREE_STEP_OBSERVER_EXACT_PASS.

P000's triadic balance and native six-space axioms remain unchanged. A Cell-step coordinate path has not been identified with a legal TRIADIC_CLOSURE_E event, V29 PASS/TRANSFER or V39 loop flow j. This result gives a concrete 20-pair provenance stress test: feed both alternatives through a genuinely typed native event interface; if an event can distinguish them, record its extra carrier/residual. If the selected event subclass treats them identically, prove that its update and all permitted continuations factor through the 284-class quotient. Author proof/finite computation does not imply independent Driver review or formal Source Result.