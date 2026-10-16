# Abstract four-Selmer lifting at the core (9,8), without a rank decision

Status: UNREVIEWED NEW AUTHOR PAPER, eleventh separate object. EM-DVR-F73673. This supplies abstract higher-descent information at the previously proved zero-form boundary. It constructs no explicit four-cover, runs no arithmetic program, parameter scan or point-search implementation, and produces no rational point. No new Task, registered Tool, Native Result or truth promotion is created. The stopped fixed-(233,119) certificate Task, its inputs and exhausted budget remain unchanged.

## 1. Exact inherited object and new information

Retain only the sixth paper's fixed primitive core (r,s)=(9,8):
A=17, B=144, P=161, Q=127, D=9792=24²·17,
E:y²=x(x−P²)(x−Q²), ordered roots (0,P²,Q²).

The separately reviewed sixth theorem proves that the full two-Selmer group is

W=Sel²(E/Q)={U_b : b∈<−1,2,3,17>},   dim_F2 W=4,

and that its entire full-descent Cassels form is zero. It also identifies the two independent rational two-torsion Kummer classes U_(−1),U_17. It does not determine the rational rank r, which satisfies r+dim Sha(E/Q)[2]=2.

The new claim is an abstract lifting and group-structure theorem:

Sel⁴(E/Q) → Sel²(E/Q) is surjective,
Sel⁴(E/Q) ≅ (Z/4)² ⊕ (Z/2)²,
Sha(E/Q)[4] ≅ (Z/4)^(2−r),   with r still UNKNOWN in {0,1,2}.

The Selmer map is induced by multiplication two E[4]→E[2]. These statements give an abstract order 64 for Sel⁴ and prove that every two-Selmer class has a four-Selmer lift. They do not give equations or coefficients for those lifts, decide which classes come from rational points, determine r, or identify the entire two-primary Sha subgroup.

All arithmetic objects retain external classical types. This static descent tower is not a native spatial or physical-time model. Heartbeat X6's six discrete spatial Cell axes, no native plane, and time-as-needed separate typing are unchanged, with no WT/Foundation assertion.

## 2. Exact additional classical theorem and its actual source

We explicitly import the standard Selmer-lifting property of the Cassels–Tate pairing: for an elliptic curve over a number field and n≥2, the natural map

s_n:Sel^(n²)(E/K) → Sel^n(E/K)

has image equal to the left/right kernel of the pulled-back Cassels–Tate pairing on Sel^n. This is stronger than bilinearity alone; no claim below derives it merely from a zero matrix. It is a declared classical theorem input, not a new theorem attributed to this author.

Actual source consumed for this use: Shukla–Stoll, arXiv:2302.01640v1, printed/PDF pages 1–2. Exact local PDF SHA256 f84fee9a3cd3e2e37aee1c0b41f08296e88988a5f1142c5911b4d16762e408ce, original URL https://arxiv.org/pdf/2302.01640v1. The full relevant introduction was personally read for this new argument. Page 1 defines the n-Selmer group by local Kummer conditions and gives equation (1.1). Page 2 separately describes finiteness of all Sha as a conjecture, defines s_n, states the kernel/image property, and refers to Poonen–Stoll [PS99] for the general pairing theory. No new download or independent reading of all of [PS99] is claimed here. This paper uses the exact stated standard theorem at the elliptic/number-field scope of that inspected primary exposition, without assuming the Sha-finiteness conjecture or an analytic rank bound.

The already inspected FSS0710.2079v1 Theorem 5.2 and Shukla–Stoll's full-descent comparison identify the sixth paper's Cassels form with this pulled-back Cassels–Tate pairing. The original root order and short-model translation, if used, preserve all Kummer classes. Thus the zero full form in the sixth theorem is the actual kernel condition in the lifting theorem, not an unrelated alternating compatibility matrix from the tenth paper.

At n=2, the kernel is all of W. Hence the map pi:Sel⁴→W is surjective. This establishes abstract existence of four-Selmer lifts; it is not an explicit covering-construction algorithm or an executed four-descent certificate.

## 3. Exact kernel of the Selmer map

Write delta_n for the global or local n-Kummer map, as appropriate. Consider the short exact sequence of Galois modules

0 → E[2] --i--> E[4] --[2]--> E[2] → 0.

Its connecting map from E[2](Q) into H¹(Q,E[2]) is exactly delta_2 restricted to E[2](Q): choose a half of the rational two-torsion point and use its Galois coboundary. Therefore

ker(i:H¹(Q,E[2])→H¹(Q,E[4]))=delta_2(E[2](Q)).

Let K0 denote this image. At the present core, the sixth paper's two independent classes U_(−1),U_17 show |K0|=4. In particular no nonzero rational two-torsion point is divisible by two over Q. This is reused concrete torsion information, not a new uniform no-four-torsion proof. The general primitive-core no-four-torsion/Fermat boundary was already in the old accepted return and is not repeated.

Kummer naturality gives, over Q and every completion,

i(delta_2(P))=delta_4(2P),
pi(delta_4(P))=delta_2(P).

Thus i maps W into Sel⁴, and pi maps Sel⁴ into W. We claim the kernel of this restricted pi is exactly i(W), not an image of a potentially larger unramified cohomology group.

Indeed, global cohomological exactness writes a class in ker pi as i(a) for a∈H¹(Q,E[2]). Suppose i(a) is four-Selmer. At every place v it equals delta_4(P_v) for some P_v∈E(Q_v). Applying pi gives delta_2(P_v)=0, so P_v=2Q_v. Then

i(a_v)=delta_4(2Q_v)=i(delta_2(Q_v)).

Consequently a_v−delta_2(Q_v) belongs to the local kernel of i, which is delta_2(E[2](Q_v)), and hence to the local two-Kummer image. Therefore a_v is in that local Kummer image at every place. The defining all-place Selmer criterion gives a∈W. Conversely i(W) is in the kernel because pi composed with i is zero on E[2]. This proves the claim, including every local place without a cutoff or a good-reduction assumption.

We have therefore proved the exact sequence

0 → W/K0 --i--> Sel⁴(E/Q) --pi--> W → 0.

The right surjectivity uses the additional classical lifting theorem and the sixth zero form. The left/middle exactness was derived explicitly above from global/local Kummer naturality. None of these steps requires a rational point representing an arbitrary element of W.

## 4. The abstract Sel⁴ group

Since |W|=16 and |K0|=4, the left kernel has order 4. The exact sequence gives

|Sel⁴(E/Q)|=4·16=64.

The cohomology group H¹(Q,E[4]), and hence its Selmer subgroup, is killed by four. On E[4] the composition i followed after pi is multiplication two, so the same holds on cohomology and its Selmer subgroups. Since pi is surjective onto W,

2 Sel⁴(E/Q)=i(W),   |2 Sel⁴(E/Q)|=4.

Every finite abelian group killed by four is a sum of Z/4 and Z/2 groups. If it is (Z/4)^a⊕(Z/2)^b, its doubled subgroup has order 2^a and its total order is 2^(2a+b). The two proved orders force a=2 and b=2. Therefore

Sel⁴(E/Q) ≅ (Z/4)² ⊕ (Z/2)².

This is an abstract group-structure determination by exact theorems and the known full two-Selmer form. No named generators, rational four-cover equations, local four-cover witnesses, matrix enumeration or executed four-descent are supplied. The extension has not been split by a claimed explicit choice of lifts.

## 5. The precise consequence for Sha[4]

The n-Kummer exact sequence gives

0 → E(Q)/nE(Q) → Sel^n(E/Q) → Sha(E/Q)[n] → 0

for n=2,4. Naturality for pi makes the left map the reduction E(Q)/4E(Q)→E(Q)/2E(Q), and the right map multiplication two on Sha[4]. For any Sha[2] class, choose a lift in W and then a preimage under the proved surjective pi. Its image in Sha[4] is a double-preimage of the original class. Thus multiplication two Sha[4]→Sha[2] is surjective, with kernel exactly Sha[2].

Writing t=dim_F2 Sha[2]=2−r, we obtain

0 → Sha[2] → Sha[4] --[2]--> Sha[2] → 0,
|Sha[4]|=2^(2t),   |2 Sha[4]|=2^t.

The same finite exponent-four classification now forces Sha[4]≅(Z/4)^t, with no additional Z/2 summands. This proves the claimed conditional-in-r description without deciding r:

r=2 would give Sha[4]=0;
r=1 would give Sha[4]≅Z/4;
r=0 would give Sha[4]≅(Z/4)².

These are cases of an exact formula, not three asserted arithmetic possibilities realized by curves, and not a determination of the present r. In particular the argument does not import a finiteness or parity conjecture to delete the r=1 case.

Every Sha[2] class is now proved divisible by two in Sha[4]. This supplies genuine divisibility information beyond the previous zero first-form boundary. It still says nothing about a further division to order eight, higher Selmer lifts, odd-primary Sha or the finiteness of all Sha. If r<2, the full two-primary subgroup cannot have exponent two, but its structure beyond its four-torsion is unresolved.

## 6. Scientific frontier and dependency boundaries

The sixth author theorem is exact Source4090e063926e770103afc4628ea40c8a8949cedb, research_notes/owner_goal_20261016/p11_uniform_u2_and_zero_form/P11_CORE_9_8_ZERO_CASSELS_FORM_OBSTRUCTION_PAPER.md,4621B SHA256af50660fc21b773a5b42231a8e6de62e87a28689dce19ec14d940f806a0789da. Its true nonauthor paper assessment is a separate 9100B report SHA256535f5cfeed0add40c4355729f42b7322d049928d0628d8bdb09400db3c1ad907. That old PASS does not review the new lifting theorem application, Sel⁴ kernel calculation or group classifications here.

Its exact full-local and full-pairing dependencies remain those of that paper, including Stoll2001, FSS0710.2079v1 and Shukla–Stoll2302.01640v1 in their retained models. The new use of the last primary's pages 1–2 is explicit in Section 2; no complete Git publication of its PDF or independent proof of general Cassels–Tate duality is fabricated. The tenth M/K compatibility form is not a dependency or a substitute for the zero **Cassels** form.

The old accepted return already excludes rational four-torsion on primitive cores using the Fermat boundary. The current narrower K0 input is also directly visible in the sixth theorem. Reusing it avoids a duplicate mathematical unit. This paper's genuinely additional deliverable is the exact two-to-four Selmer sequence and its abstract group/divisibility consequences on one fixed previously unresolved core.

The next missing information is explicit four-cover data or a genuinely new higher pairing/rational-point input capable of distinguishing r. No such information is supplied. A theorem that a four-Selmer lift exists is not a certificate giving that lift's equations; neither kind of lift is a rational point on the two-cover. The new order-64 statement is not an execution receipt or a claim that a scientific four-descent program ran. The core-(6,1)/(5,4) rank-zero and old fixed-core rank-one papers keep their own scopes.

Failure/kill conditions include an incomplete full W computation, a merely restricted rather than full zero Cassels form, a missing full Cassels–Tate bridge, an unjustified kernel/image lifting theorem, a mistaken global/local Kummer exactness argument, or loss of the actual K0 cardinality. Any such failure invalidates the corresponding abstract conclusion. No old closed Task is reopened, no fixed-(233,119) preparation is resumed, no exhausted budget is changed, and no Native acceptance or parent closure is inferred. This new paper requires its own genuine nonauthor review.
