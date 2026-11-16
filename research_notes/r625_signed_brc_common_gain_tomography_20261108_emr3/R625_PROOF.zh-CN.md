# R625｜未知共同振幅下的 signed BRC 方向层析与精确反例

Date: 2026-11-08; status: AUTHOR-SIDE EXACT PROOF / UNREVIEWED / NOT_ADMITTED.
Scientific pin: R462 immutable commit `18783e01e3646c72b7aab3b16d3f565e83e6446f`, theta=0, signed K source blob `7fa7a762f758b30c6090468ac43487daa34abad8`. Predecessor R624 `d5023c5a179f4cb494e7755c9e9e7518573a1177`.

## Question, exact carrier and observer

R624 identified S6 orientation using two coefficients of each **bare signed K kernel**. Here test a different exact interface: a packet observer measuring the product of a branch kernel with a common unknown signed gain. Work in the integral domain `Z[[t]]`, with observations in `Z[t]/(t^(d+1))`. Let `A(t) != 0` be the same unknown element of `Z[[t]]` in all six independently addressed positive-axis experiments, and let `r=ν_t(A)>=0`. The frozen original K has `ν_t(K_i)=i−1` and all leading coefficients nonzero. For an orientation π∈S6 assigning basic axis j to spatial axis π(j), the positive-axis output is

`Y_(π(j))(t)=A(t) K_(2j−1)(t)`, j=1,...,6.

The d-jet observer reports all six labeled `Y_x mod t^(d+1)`. Assumptions: pure one-branch output, separately addressable spatial axes, one common nonzero signed gain; no positive-mass substitution, no time/heartbeat identification.

## Theorem A: exact unknown-gain tomography and optimal jet depth

The valuations of the six responses, in basic-axis order, are

`ν_t(Y_(π(j)))=r+2(j−1)`, i.e. `r,r+2,r+4,r+6,r+8,r+10`.

For d<r set k=0, otherwise `k=min(6,floor((d−r)/2)+1)`. Exactly k responses have nonzero d-jets. At a fixed A the number of pairwise distinct orientation arrays is

`N(d,r)=6!/(6−k)!`.

**Sharp full-identification threshold:** For any nonzero unknown common A, all 720 orientations are uniquely reconstructed from these six positive-axis jets iff `d>=r+8`. At d=r+8 the five observed nonzero orders r,r+2,r+4,r+6,r+8 identify basic j=1,..,5; the remaining spatial axis must be j=6. The least nonzero valuation also identifies r. When `d<=r+7`, at least two basic axes are invisible; transposing them gives an exact pair of indistinguishable orientation configurations for the *same* A.

**Proof:** A nonzero product in the integral domain Z[[t]] has the product of its nonzero leading coefficients, so `ν(PQ)=ν(P)+ν(Q)`. The six positive K factors have distinct orders 0,2,4,6,8,10. After d-truncation there are k nonzero responses with distinct orders, and 6−k identical zero responses. Its S6 stabilizer is S_(6−k), giving the orbit cardinality. With at least five visible labels, elimination identifies the sixth; with four or fewer, swap two invisible labels. Unknown A does not change the order gaps, and its order r is the minimum observed nonzero valuation whenever d>=r. QED.

This is a minimal degree for the **stated six parallel positive-direction jet observer**, not a claim about all possible adaptive or physical measurements. The exact profile is a formal signed-K/X6 label bridge, not an installed native field.

## Theorem B: recovering the unknown common gain by exact division

When π is decoded, `Y_(π(1))=A K_1=A(2+3t)`. The factor K1 is invertible in Q[[t]], hence the full formal response uniquely recovers `A=Y_(π(1))/(2+3t)`. For a finite d-jet, the exact recurrence is

`a_0=y_0/2; a_n=(y_n−3a_(n−1))/2` for n>=1,

which reconstructs A modulo t^(d+1) using rational intermediate arithmetic and returns integers on a true integer-series instance. Retain π, A and any other relevant path/provenance state before applying future signed-K operations.

## Exact counterexample: R624 bare-kernel two taps fail as raw packet taps

Let the same gain on all directions be

`A(t)=1+2t^3+97t^4`.

Original frozen K values are `[t^8]K5=5`, `[t^5]K5=−13`, `[t^4]K5=6`, and `[t^8]K7=561`, `[t^5]K7=[t^4]K7=0`. Hence

`[t^8](AK5)=5+2(−13)+97(6)=561=[t^8](AK7)`.

Moreover `ν(K6)=5` and `ν(K8)=7`, so `[t^3](AK6)=[t^3](AK8)=0`. Thus axes j=3,4 have identical raw signed packet signatures (561,0) under R624's (+,8)/(-,3) *taps on AK*, even though the corresponding bare-K signatures are (5,0)/(561,0). The entire six-axis packet signature array is

`(0,4),(394,−11),(561,0),(561,0),(83,0),(0,0)`.

It contains five distinguishable signatures; exactly 360 of the 720 orientation codes remain. This is a rigorous counterexample to transferring bare-kernel two-tap tomography to a raw packet output without validating the observer semantics. It leaves R624's actual bare-K theorem intact.

## Native relation, validation and next unit

The source P000 keeps six signed spatial axes in an affine Cell torsor, with time separately typed and `fixed_heartbeat_program=null` at the current normative source. Neither the signed-K polynomial valuation nor a branch grade is physical heartbeat time. R625 supplies a **candidate packet-facing observation contract**: if a native interface provides six pure outputs with one nonzero common gain, its orientation is identifiable at jet depth ν(A)+8, and the gain can be recovered by algebraic deconvolution. Whether an actual native joint field realizes that factorization remains to be checked. Axis-dependent gains, sums of histories or interference need their own observer/future-operation congruence certificate under the P000 joint-state preservation policy.

Exact verifier `R625_VERIFY.py` reconstructs original twelve K polynomials by integer binomials, verifies the signed leading values, checks the explicit collision, enumerates all 720 orientations across four nonzero gains and 38 selected finite jet depths (27,360 labeled permutations tested), and tests four exact rational deconvolutions. Its generated evidence marker is `R625_COMMON_GAIN_VALUATION_TOMOGRAPHY_EXACT_PASS`. The universal statements are proved above; finite checks confirm frozen instances.

**Next:** Locate a registered native joint-field update and readout that delivers the six separately addressable pure common-gain packet responses, or construct an exact one-operation counterexample with axis-dependent gains or additive histories; specify the smallest observer repair and its preservation scope. Source identity/active Owner/CLAIM and independent Driver acceptance require actual native authorization.
