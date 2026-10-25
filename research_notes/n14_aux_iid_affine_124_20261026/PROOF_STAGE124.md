# R1 / N14 — Stage124: exact full-real affine optimum and sharpness

**Claim class:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF, no native CLAIM/Result or independent Research Driver mathematical acceptance. External finite ternary iid model **only**, not the P000 native X6 Cell-space model.

## 1. Exact theorem

For P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), and at most N=14 iid observations, consider all randomized stopping/decision rules depending on *literal full ordered histories*. Put eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau); minimize V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

From author-proved Stage123:
alpha123=2573845365525582162925/7411551152237344456704,
V123=377878052586265662571445/29646204608949377826816.

Let K124=1245231873/1658336, L124=36440256/51823, S124=2411320065/1658336, and eta124=8596140125/8578184203978407936.

**Theorem:** For *every real* 0<=delta<=eta124,
V14(alpha123+delta) = V123 - S124*delta.
The exact new endpoint is
alpha124=2573845372952647230925/7411551152237344456704,
V124=377878009388672358128945/29646204608949377826816.

This **same supporting affine line is right-sharp**: equality to it cannot hold at any alpha>alpha124. We do not assert that larger alpha is infeasible or that the next support is known.

## 2. Universal Bellman support for arbitrary ordered strategies

At count state s=(n,a,b), where a,b count symbol 0,1, the prefix likelihood ratio is Q(word)/P(word)=2^(a+b)/3^a. Let H(s) minimize the costs:
* declare P: K124*2^(a+b)/3^a;
* declare Q: L124;
* continue if n<14: 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b).

Exact rational backwards enumeration covers all 680 count states, 1,238 *strictly positive* alternatives, no negative gaps, and only two ties: A=(9,3,0) P/continue and T=(14,7,4) terminal P/Q. The least positive gap is 294166217221/39614118100992. At the root,

H(0)=5878829162353591081475135/11355563791072559628288
    =V123+S124*alpha123.

For each **literal ordered prefix**, its likelihood ratio and conditional iid suffix depend only on that count state. Backward Bellman induction is therefore valid without restricting full-history strategies to count-measurable policies:

H(0)<=tP+L124*eP+K124*eQ<=max(tP,tQ)+S124*alpha.

Consequently V14(alpha)>=H(0)-S124*alpha for all admissible policies.

## 3. Literal BRC positive-mass first hits and exact affine moments

Retain each actual ordered word, its multiplicity, first-hit depth and separate positive P and Q integer-numerator weights (P symbols have numerators (3,1,20)/24, Q symbols (1,1,10)/12). Exact full-tree enumeration under unique Bellman minimizers elsewhere yields

| Tie state | Ordered first-hit words | P mass | Q mass |
|---|---:|---:|---:|
| A=(9,3,0) | 84 | 109375/1990656 | 109375/6718464 |
| T=(14,7,4) | 7962 | 165875/25048249270272 | 165875/26748301344768 |

A cannot be an ancestor of T because going from depth9 counts (3,0) to depth14 (7,4) needs eight symbol-0/1 increases in only five draws. T cannot precede A by depth. These literal positive-mass path cones are disjoint, so there is **no mixed probability term**.

Let y be the probability of immediately declaring P at A (otherwise continue); z the probability of declaring Q at terminal T (otherwise P). All other states use the unique minimizing action. Then with M=(eP,eQ,tP,tQ),

M(y,z)=M00+y*dA+z*dT,

where the exact four-vectors are

M00=(608919691844004011/1752976676930715648,
55715890510475/160489808068608,
2798007941169380921/219122084616339456,
161747615623729/13374150672384);

dA=(-1921609375/7925422620672,
259765625/835884417024,
-20758609375/330225942528,
-1476453125/69657034752);

dT=(165875/25048249270272,
-165875/26748301344768,
0,0).

The T switch is between two decisions **at the same terminal depth**, so it contributes no time change. Exact four-corner recurrence and separately written integer literal-word DFS agree on all four observers, including the identity M11=M00+dA+dT.

The only compressed quotient used is justified by the iid likelihood ratio and suffix moment equality *for these four observers*. No arbitrary future observer or native X6 state correspondence is inferred.

## 4. Exact primal family, every real point

The equation eP=eQ is exactly equivalent to

y(z)=151539326395319/415627392000000
     +(160567/6927123200)*z.

For all real z in [0,1],

0<y(0)<y(1)=151548960415319/415627392000000<1,

so both randomizations are legal. Exactly,

eP=eQ=alpha123+eta124*z,
tP=V123-S124*eta124*z.

The endpoint margins tP-tQ are respectively

19564551641189828171621/29646204608949377826816 > 0,
19564523009155753489121/29646204608949377826816 > 0.

The time difference is affine, hence tP>tQ on the entire real interval. Every action used minimizes its Bellman cost; therefore H(0)=tP+L124*eP+K124*eQ. Since the errors equal the allowed alpha and max(tP,tQ)=tP, the constructed policies attain the universal Bellman bound throughout the interval.

## 5. Right-sharpness of this support

The finite randomized full-history policy space is compact. If the same affine support were attained at alpha>alpha124, positivity of K124,L124 would force both errors to equal alpha and all positively reached actions to minimize Bellman costs. Only A/T have tied actions; all others have strictly positive gaps. Prefix-specific randomizations within an iid count fiber can be weighted-averaged for the declared four observables because its likelihood ratio and suffix observer laws coincide. The two ordered first-hit cones are disjoint. Thus any equality-attaining policy has the *same four observables* as some legal (y,z) in [0,1]^2 satisfying the unique balance equation above. Its balanced alpha=alpha123+eta124*z strictly increases with z; z<=1 implies alpha<=alpha124, contradiction. This proves the support cannot extend rightward.

## 6. Execution, authority, exact provenance and next question

Two **author implementations** executed locally with exact stdlib Fraction arithmetic, no floating point: a bottom-up all-680-state Bellman/four-corner checker and a separate top-down memoized Bellman plus literal ordered-prefix integer DFS. The independent implementation visited 815542 / 815542 / 810502 / 810502 nodes at corners (y,z)=(0,0)/(0,1)/(1,0)/(1,1), recovered first-hit counts/PQ masses, all four root moments, zero mixed finite difference and exact endpoint equalities. Source, machine-readable certificate, run evidence and bounded next unit accompany this proof. GitHub source readback is storage validation, **not remote execution**.

BRC reuse status REUSE_APPLIED to positive rational ordered path identity, multiplicity, provenance, separate P/Q masses and an expressly restricted four-observer quotient; adapted existing N14 exact-checker family. No P000 six-axis observer/update-preserving mapping or physical applicability has been proved. Independent Research Driver review pending.

Fixed GLOBAL_KNOWLEDGE_V1 research read main@e8d65b2492cf35be071c32b0c9852487f100be07, P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Initial EM research source main@520517d398d10a46c55d6f106cee1db5a0e82a69, subsequently consumed immutable concurrent Stage123 author source at 0300f93ab4f4e4a0daa2fd214704f80ad14a6ae6. GitHub account awdawmip. Native inventory returned CONTROL_QUOTA and session_start STATIC_READONLY_SCOPE_DENIED (operation_sent=false); no verified active Owner, native CLAIM/Result or review. This is ordinary versioned **author** evidence only.

Stage125 currently DUAL_CANDIDATE_ONLY at K125=3579845625/4855672, L125=416181048/606959, with new tie U=(12,7,5) Q/continue. Stage125 primal optimum is unproved; see NEXT_TASK_PACKET_125.md.
