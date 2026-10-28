# EC49P — Reversible sensor order reduces exact external causal memory from two bits to one

Author-side portable research; AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED.
Author label: R4-LOCAL-EC49P-20261029T0128-AUTHOR (not a native session/claim).
Immutable inputs: GLOBAL_KNOWLEDGE_V1 main@520e9b3192da6bbd7be43f85867854b6d23a2671; Enterprise Math main@0f635378d6c1f5b133f7518c289e49b5a3cca8df; EC49O PR #1652 at 84cd9817f468e6c262c8dc455d0c9516fbbaeff0. P000/ACTIVE unchanged. Model: auxiliary positive rational two-source probabilities, NOT native signed BRC or six-axis X6 dynamics.

## 1. Model and quantifiers

All indices modulo three: W,X,Y ∈ {0,1,2}. For w,x,y define
\[
s_w(x,y)={\bf1}_{y=x+w}-{\bf1}_{y=x+w+1},\quad
Q(w,x,y)=1/27,\quad P(w,x,y)=(2+s_w(x,y))/54.
\]
All 27 atoms per source are strictly positive rationals; each measure normalizes to 1. The initial W and each single sensor separately are source-neutral: P(W=w,X=x)=Q(W=w,X=x)=1/9, and likewise Y. After both sensors P/Q=1+s/2 ∈ {1/2,1,3/2}.

The controller first observes W. It can accept/reject at cost 0 or purchase X (cost 1) or Y (cost 2); after observing the first, it may accept/reject or purchase the remaining sensor; after both, accept/reject. It always remembers its own purchase order and actually observed sensor values. Immediately after stage zero it forgets W except for m external memory bits D, causally set while W is visible. The unrestricted full controller retains W. All randomized choices are source-independent, real, fresh behavioral coins; no uncounted shared random seed, third free action tag, repeat purchase, or delay coding. Cost T is total sensor price (not physical time). Define raw observation region S_m through O=(alpha,beta,E_P T,E_Q T), with alpha=P(accept), beta=Q(accept). This is a statement about actual raw images under all real policies, not convex hulls.

## 2. Theorem: S_1=S_full exactly

**Theorem EC49P.1**. In this variable-order protocol, one external memory bit suffices and zero bits do not:
\[
\boxed{S_1=S_{\mathrm{full}},\quad S_0\subsetneq S_{\mathrm{full}}.}
\]
The complete common raw region equals the linear image of the following bounded rational polytope, with variables b,n,c_0,a_{-1},a_0,a_{+1}:
\[
\begin{gathered}
0\le b\le 1,\quad 0\le n\le1-b,\quad0\le c_0\le2(1-b),\\
0\le a_s\le b/3\quad(s=-1,0,+1),\\
\alpha=n+\tfrac12a_{-1}+a_0+\tfrac32a_{+1},\qquad
\beta=n+a_{-1}+a_0+a_{+1},\\
E_PT=E_QT=3b+c_0.
\end{gathered} \tag{1}
\]

**Outer bound, including adaptive order, early acceptance and real randomization.** Let B denote the event of purchasing both sensors. The decision to buy the second sensor is made after a prefix of W, one sensor, recorded order/actions and fresh coins. Each such observable prefix has exactly the same P and Q law, because each single-sensor W-conditioned marginal does. Thus b=P(B)=Q(B). Under Q, conditional on any such prefix, the second sensor is uniform, with exactly one of its three values falling into each s∈{-1,0,+1}. Hence
\[
Q(B\cap\{s=k\})=b/3,\quad
P(B\cap\{s=k\})=(1+k/2)b/3. \tag{2}
\]
Define a_k=Q(B∩{s=k}∩accept), 0≤a_k≤b/3. Since likelihood ratio is constant on each signed class, P's accepted complete mass is sum_k(1+k/2)a_k and Q's is sum_k a_k. Acceptance prior to purchase of the second sensor has identical P and Q mass n∈[0,1-b]. All completed paths pay 3; incomplete paths pay 0,1,2 with source-neutral probabilities, so E_P T=E_Q T=3b+c_0 with 0≤c_0≤2(1-b). This proves containment in (1) without reducing arbitrary full policies to pure strategies.

**Constructive inclusion using one external bit, not a convexification argument.** Given ANY real feasible parameters in (1), set p=c_0/2, q=1-b-p≥0, u=n/(1-b) if b<1 (else 0), and r_k=3a_k/b if b>0 (else 0). All are valid probabilities. On observing W, choose using a fresh coin:

- probability b: COMPLETE; encode W=0 as (first X,D=0), W=1 as (first X,D=1), W=2 as (first Y,D=0). Buy the other sensor after the first and accept after both with probability r_{s_W(X,Y)}. The own recorded first action plus one bit reveals W.
- probability p: PADDING; first Y,D=1 (disjoint from the three COMPLETE labels), then stop before buying the second sensor and accept with probability u.
- probability q: STOP immediately and accept with probability u.

No cross-stage shared random seed is used. The recorded pair (first-order,D) identifies each of three COMPLETE histories or the PADDING state, and the immediate STOP action is terminal. Completed accepted masses by sign are exactly a_k under Q and (1+k/2)a_k under P; incomplete accepted mass is (p+q)u=n under both. Both costs equal 3b+2p=3b+c_0. This realizes the exact prescribed RAW four-vector. Full memory trivially simulates all one-bit policies. Therefore S_1=S_full.

**Rational realization corollary.** The parameter polytope and four-vector map in (1) have rational coefficients. Any rational point in the image has a nonempty rational polytope fiber; such a fiber has a rational vertex. Choose rational parameters at that vertex, and the formulas above produce a one-bit fresh-behavioral controller with all probabilities rational (the zero-denominator endpoint conventions are rational). The conclusion concerns this exact protocol, not arbitrary imperfect-recall models.

## 3. Zero-bit strict obstruction and exact sharp gap

**Theorem EC49P.2.** For L(O)=alpha-beta,
\[
\max_{S_0}L=1/9,\quad \max_{S_1}L=\max_{S_{\rm full}}L=1/6.
\]
The one-bit/full witness is O*=(1/2,1/3,3,3); the best zero-bit full-cost witness is (4/9,1/3,3,3). Consequently O* lies outside even conv(S_0), separated by the sharp 1/18 gap.

**All-real upper bound.** At stage zero, W can determine real probabilities q_{w,X},q_{w,Y} of starting in each order, with q_{w,X}+q_{w,Y}≤1. With zero extra memory, after the first sensor value z and recalled order o, the probability k_{o,z} of buying the other sensor cannot depend on W; terminal acceptance r_{o,x,y} likewise cannot depend on W. Stopping early and accepting before buying the second sensor contribute zero P-Q difference because the relevant prefix is source-neutral. Thus
\[
L=\frac1{54}\sum_{o,x,y}r_{o,x,y}k_{o,z(o,x,y)}
       \sum_w q_{w,o}s_w(x,y).
\]
Maximizing acceptance for positive coefficients and dropping each k≤1 gives
\[
L\le \frac1{54}\sum_{o,z}\sum_{v\in\{0,1,2\}}
       [\sum_w q_{w,o}s_w(z,v)]_+,
\]
where for Y-first, z is the y value and v is the missing x (rather than reversing arguments of s). The right side is convex in the three initial simplex vectors (q_{w,X},q_{w,Y}); its maximum is attained at a deterministic vertex where each W selects STOP, X-first or Y-first. For any one order and fixed first reading, selecting a nonempty proper subset of the three W signed rows gives a permutation of (1,-1,0) over the missing-sensor values, positive-part sum exactly 1; selecting none or all three gives 0. Thus at most two order tags each contribute 1 per first reading. There are three readings and each coefficient is 1/54. Therefore L≤6/54=1/9.

Attainment: send W0,W1→X-first and W2→Y-first, always buy both. For X-first accept iff y=x; for Y-first accept iff y=x+2 mod3. Exact direct mass sums yield (alpha,beta,C,C)=(4/9,1/3,3,3). A one-bit controller instead uses (X,0),(X,1),(Y,0) to encode all W, always buys both, accepts iff s_W(x,y)=+1; direct sum gives (1/2,1/3,3,3). Bounds and equality follow, for all real policies (not solely enumerated rational policies).

## 4. Exact sensor-cost versus distinguishability frontier

**Theorem EC49P.3.** For every exact common sensor-cost C∈[0,3],
\[
\max_{S_0,\ E_PT=C}L=\min(C/18,1/9),\qquad
\max_{S_1,\ E_PT=C}L=C/18.
\]
Proof: from (1) L=(a_{+1}-a_{-1})/2≤b/6≤C/18, and previous zero-bit inequality supplies ≤1/9. The one-bit compiler realizes C/18 by choosing b=C/3, a_{+1}=b/3, n=c_0=a_0=a_{-1}=0.

For zero bits and 0≤C≤2, buy both for W0 with probability min(1,C) in order X,Y and for W1 with probability max(0,C−1) in order Y,X; reject otherwise. Accept on W0's X-first tag iff y=x and on W1's Y-first tag iff y=x+1. Both purchase paths each cost 3 on their chosen initial W, which has probability 1/3, so expected cost C and support C/18.

For 2≤C≤3, buy both for W0 in order X,Y and W1 in order Y,X; buy both for W2 in order X,Y with probability C−2. X-first terminal acceptance iff y=x OR y=x+2; Y-first iff y=x+1. The X-first signed-mass coefficients are (1−(C−2),−1,C−2), so positive sum stays 1, and Y-first contributes another 1. Support stays 2/18=1/9 while expected cost rises to C. This proves sharpness for every real C. It also shows why transfer of EC49O's fixed-order lower bound is invalid when sensor order becomes a causal action-history channel.

## 5. Executed verification, reproducibility, and limits

The companion standard-library Python Fraction checker VERIFY.py actually tested 27 strictly positive rational source atoms for each P/Q and normalized/source-neutral individual marginals; checked both four-vector witnesses; enumerated all 1,728 deterministic zero-bit plans (initial W→STOP/X/Y and six post-first BUY-OTHER/STOP bits) with exact optimal terminal accept/reject; verified seven rational C samples of both sharp frontier families; and compared 128 seeded rational full-history behavioral policies, first via direct source atom sums, then independent likelihood-class decomposition and explicit one-bit compiled policy sums. EXACT_REPORT.json is the actual emitted report. Universal real-policy claims are analytic theorems above and do not rely on finite sampling.

Signed s and P-Q differences are auxiliary finite-probability contrast, not the project's native signed/amplitude BRC algebra or native X6 displacement. W labels are finite hidden-history indices, not indigenous spatial axes; T is sensor cost, not heartbeat time. P000 and ACTIVE global worldview remain immutable. Native BRC/X6/time translation requires a distinct typed morphism, observer/future-operation commutation theorem, and independent review.

Next EC49Q: classify action-history label coding capacity and cost-neutral padding in general finite observer trees, and test whether rational attainable four-targets still always admit rational fresh behavioral implementations when conditional source kernels or resource laws vary. See NEXT_TASK.md.