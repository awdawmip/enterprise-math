# R1/N14 — Likelihood-ratio fiber constancy is not sufficient for a coarse observer at N=3

**Evidence class:** author mathematical proof plus exact rational verifier; not an independent Driver review or Foundation theorem. 2026-10-27.

## Question and predecessor

The existing R1/N14 result at `research_notes/r1_n14_brc_coarse_lr_necessity_20261027_r1t11/PROOF.md` proves that, for universal simultaneous P/Q terminal-law preservation, the ratio Q(h)/P(h) must be constant on each recursively updatable compressed-state fiber. For horizon N=1 this is also sufficient. The follow-up asks for a criterion at N>=2. **The present construction proves that LR fiber constancy is not sufficient at N=3, even for a constant terminal observer.**

Here the same randomized policy, without knowing whether P or Q is true, must reproduce both joint terminal distributions (T,o(x(H_T)),D). The compressed policy's entire decision state is x, with no hidden persistent history or private policy-selection state.

## Strictly positive three-stage process

Alphabet A={0,1,2}; N=3. For every prefix h of length t<=2, P(h)=Q(h)=3^{-t}. After two observations, the third conditional distribution under P is

- at h=(0,0): p_hi=(1/4,1/4,1/2);
- at each of the other eight two-symbol histories: p_lo=(1/12,3/4,1/6).

Define r=(2,1,1/2), and set Q(a|h)=r_a P(a|h). Both P conditionals and their r-weighted versions sum to exactly 1: q_hi=(1/2,1/4,1/4) and q_lo=(1/6,3/4,1/12). Each cylinder has positive mass and P is not Q.

The deterministic compression is x(h)=(|h|,*) for t<=2, and x((i,j,a))=(3,a) for t=3. Its update is deterministic from the current x and next symbol: before the last step it discards the symbol; on the last step it retains a. Let the terminal observer o(x)=0 for every x (no state information is revealed in the required terminal report).

**LR property.** For t<=2, Q(h)/P(h)=1 in every fiber. For t=3, Q(i,j,a)/P(i,j,a)=r_a, and x(i,j,a)=(3,a). Therefore the ratio is constant on *every* compressed fiber at *every* observation time. The time-two state is not strongly lumpable, because its next-symbol distribution depends on the hidden ordered prefix.

## History-dependent stopping/decision policy

Continue at t=0,1. At t=2, continue only after h=(0,0); otherwise stop and output D=0. At t=3, output D=1 exactly when the last observed symbol is a=0 (otherwise D=0).

Both laws give the selected prefix probability 1/9, so

P(T=3)=Q(T=3)=1/9,

P(T=3,D=1)=(1/9)(1/4)=1/36,

Q(T=3,D=1)=(1/9)(1/2)=1/18.

Consequently the observed contrast is Delta_full=Q(T=3,D=1)-P(T=3,D=1)=1/36.

## Exact linear separating certificate

Assume an x-only stochastic policy matches these terminal laws. Since neither law stops before t=2 under the original policy, the matching policy must have probability 1 of continuing at t=0,1. All nine two-symbol histories are in the same state x_2=(2,*). Its chance of continuing must be a common number u. Matching P(T=3)=1/9 forces u=1/9.

Because the same u is used on all nine equally likely prefixes, their conditional distribution among the compressed continuers remains uniform. Their pooled next-symbol probabilities are

p_bar(0)=[1/4+8(1/12)]/9=11/108,

p_bar(1)=[1/4+8(3/4)]/9=25/36,

p_bar(2)=[1/2+8(1/6)]/9=11/54.

For Q, q_bar(a)=r_a p_bar(a), so q_bar-p_bar=(11/108,0,-11/108).

Let d_a in [0,1] be the compressed policy's chance of declaring D=1 in state x_3=(3,a). For **every single P/Q-common compressed strategy**,

Delta_x := Q(T=3,D=1)-P(T=3,D=1)
= u*(11/108)*(d_0-d_2)
<= (11/108)*P(T=3).

This is a universal *linear inequality in the declared terminal observables*, not a test against one guessed compressed policy. The original policy violates it:

Delta_full - (11/108)P(T=3)
= 1/36 - (11/108)(1/9)
= 27/972 - 11/972
= **4/243 > 0**.

Hence no x-only law-independent randomized stopping/decision policy preserves both terminal laws. This completes a universal nonpreservation proof within the specified finite model. In particular, the LR condition established as necessary by the predecessor result fails to be sufficient already at horizon 3.

## Reusable mechanism

The full-history policy selects the high-contrast prefix 00, where the third-symbol event {a=0} has positive Q-P contrast 1/4. A compressed policy whose time-two state erases the prefix can select only a uniform fraction and inherits the pooled contrast 11/108. **Future-selection-relevant residual information may therefore survive even when the current likelihood ratio is entirely determined by the compressed state.**

More generally in a single merged state with P=Q on all currently surviving histories, a history-specific one-step continuation may extract contrast mass P(h*) Σ_a [Q(a|h*)-P(a|h*)]_+. A compressed common continuation selecting the same total time mass achieves at most P(h*) Σ_a [q_bar(a)-p_bar(a)]_+, with the pool induced by current survivors. A strict difference is a sufficient obstruction. This is a *scoped one-step obstruction*, not the sought general N-stage iff.

## Exact check, scope, source and status

The accompanying verifier uses Python Fraction to check all 40 prefixes (1+3+9+27), both positive normalized probability laws, LR-fiber constancy for t=0,1,2,3, and the exact 4/243 separating gap. A finite check supplements the explicit all-policy inequality above; the program is not itself an independent proof review.

This is an **external finite ordered-path probability model**, not a native P000 six-dimensional Cell result, a physical model, a phase-cancellation claim, a Lean proof, or a new Foundation theorem. BRC reuse: positive rational branch masses, ordered provenance until the stated observer quotient, and exact observer contrast.

Frozen account control input: awdawmip/chatgpt-global-knowledge@e2d38ad0f2c3726cfad2c66d90c515e96f3ee36e; project source input: awdawmip/enterprise-math@d57652fae00d148c7e22bbdf18762d3cb0f9e52e. P000 startup's original blob pin 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc was matched to the canonical original metadata. GitHub login awdawmip was verified. Native control dispatch/owner check returned CONTROL_QUOTA; native session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Source persistence here is an **author activity checkpoint**, not a formal CLAIM, Source-native session, independent review, or admission.

**Next discriminating task:** characterize finite P/Q-coupled terminal-law attainability for recursively updated x-only strategies; decide whether the set is convex without a persistent hidden selector, then find an exact iff or a finite separating-certificate algorithm which respects survivor-mixture dynamics. See NEXT_TASK.md.
