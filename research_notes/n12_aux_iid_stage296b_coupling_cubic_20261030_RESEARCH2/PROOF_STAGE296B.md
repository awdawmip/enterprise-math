# Stage296-B | Coupling types and cubic observer residual for repeated Bernoulli ports

**Author/status (2026-10-30):** Research2 portable author continuation of Stage295-B.2, source commit c8948e1dfb4cf22af040350f2129e03012f7cf2b. PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. The results are internal to the explicit finite positive-probability BRC-style ordered-word model, **not** native P000/X6 dynamics or a formal Source Result.

## Frozen control and assumptions

Verified GLOBAL_KNOWLEDGE_V1 main@24ab8f17a3fc3ea961bd3552551c5ad1c148a051 and Enterprise Math main@b9d541db192cc2905adf3e600f2feb00f794ec28. Read canonical entry and operating manual, P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488, ACTIVE Heartbeat/X6 and joint-relation observer constraints, Task Researcher startup and current portable research protocol. The older global P000_STARTUP projection still points at original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; current project original governs, and P000/ACTIVE sources are not edited.

Predecessor: PROOF_STAGE295B_FULLMIX.md at immutable c8948e1d, PR #1736. Sources S=0,1 have prior 1/2 each. At labels A,B the uncompressed conditional independent rates are (a,1-a) and (1-a,a), respectively, with 0<=a<=1/2. Full ordered observer retains (S,Y_A,Y_B); compressed controller does not observe S. Let h=a(1-a), r=(1-a)^2, s=a^2. Source laws indexed (00,01,10,11) are P0=(h,r,s,h), P1=(h,s,r,h). All eight source-labelled words are strictly positive if 0<a<1/2.

## Theorem A: the exact coupling interface boundary

The unrestricted, source-blind **free visible-output kernel** has minimum mean source-TV risk R_free=1/2-a, attained by Q*=(h,1/2-h,1/2-h,h).

Class I (pre-mixed conditional IID): choose a single possibly real and source-correlated parameter Theta in [0,1], then draw both Y_A,Y_B independently conditional on (Theta,S), with success rate Theta. Its exact minimum mean source-TV is R_I=(1-a)^2-1/4, attained with Theta=1/2 independently of S. Thus R_I-R_free=(1/2-a)^2, strictly positive for a<1/2.

Proof: Triangle inequality gives 2 R_free>=TV(P0,P1)=1-2a; Q* attains equality. For each source the designated high-probability unequal word under the target has mass r; any Class I mixture has probability E[Theta(1-Theta)|S]<=1/4 for that word, giving per-source TV>=r-1/4. Uniform independent fair pair at Theta=1/2 attains this lower bound. The argument covers arbitrary real mixing laws, including source-correlated mixing. In particular at a=1/4, Q*=(3,5,5,3)/16, R_free=1/4, R_I=5/16, gap=1/16, and Cov_Q*(Y_A,Y_B)=3/16-1/4=-1/16, whereas Cov_ClassI=Var(Theta)>=0.

Class II (two **deterministic-parity coupling modes**, not conditionally IID): choose an unobserved fair bit U for the first visit. A shared mode Z is either E (set Y_B=U) or X (set Y_B=1-U), with P(Z=E)=2h and P(Z=X)=1-2h; Z is independent of U and S. Then both individual Bernoulli marginals equal 1/2 even conditional on either mode, and the ordered law is exactly Q*. In this precisely declared **primitive parity-mode class**, two modes are necessary for every 0<a<1/2: the target has strictly positive equal and unequal word probabilities, whereas a single deterministic parity mode supports just one type. At a=1/4 the mode probabilities are 3/8 (E) and 5/8 (X). **This is not an absolute minimum shared-seed cardinality:** a primitive class allowing one arbitrary stochastic correlated pair kernel already realizes Q* as a single mode. Nor is Class II permitted by Class I's conditional independence premise.

Class III (history-adaptively retuned Bernoulli port): draw Y_A~Bernoulli(1/2); after observing Y_A, use a freshly retuned independent Bernoulli draw for B with rates

    Pr(Y_B=1 | Y_A=0)=1-2h,
    Pr(Y_B=1 | Y_A=1)=2h.

Then Q* is reproduced exactly for all 0<=a<=1/2. If h!=1/4, the two rates are unequal. Therefore, within the class of a deterministic first rate followed by a fresh second Bernoulli draw **without any other shared seed**, knowledge of the preceding output distinguishes at least two histories and is necessary for this exact construction: without history-dependent rates, the two outputs are independent and cannot have Q*'s strictly negative covariance. At a=1/4 rates are 5/8 and 3/8. This minimum information claim is **specific to the no-extra-seed retuning class**, not to seed-correlated preprogrammed two-rate strategies.

**Observer safety:** Class II's joint law equals the free Q* only for declared observers of (S,Y_A,Y_B) and downstream operations factoring through this observed history. If future operations can inspect Z or U separately, or the actual chosen Theta or port-setting history, equality of the projected pair law is insufficient. Retain these labels or separately prove a state/future-kernel descent certificate. Source S remains visible to risk even though Q* ignores S in control; there is no unconditional native quotient claim.

## Theorem B: a sharp third-moment observer hierarchy

Let Theta be drawn once from a probability measure mu on [0,1], with three Bernoulli visits conditionally IID given Theta. Set m_j=E[Theta^j], with m_0=1. Fix m_1=1/2 and m_2=3/8. The **complete attainable interval** for m_3 is

    9/32 <= m_3 <= 11/32.

Proof: Cauchy-Schwarz for sqrt(Theta) and Theta^(3/2) gives m_2^2<=m_1*m_3, hence m_3>=9/32. Cauchy-Schwarz for sqrt(1-Theta) and Theta*sqrt(1-Theta) gives (m_1-m_2)^2 <= (1-m_1)(m_2-m_3), hence m_3<=11/32. The endpoints have exact rational atomic witnesses

    mu_L=(1/3)delta_0+(2/3)delta_(3/4),  m_3=9/32;
    mu_U=(2/3)delta_(1/4)+(1/3)delta_1,  m_3=11/32.

Both have m_1=1/2,m_2=3/8. Every intermediate m_3 is achieved by their convex mixture, proving no missing feasibility constraint.

For any fixed (m_1,m_2), ordered three-bit word probabilities by number k of successes are

    k=0: 1-3*m_1+3*m_2-m_3 (one word)
    k=1: m_1-2*m_2+m_3 (three ordered words)
    k=2: m_2-m_3 (three ordered words)
    k=3: m_3 (one word).

Thus if two mixing laws have identical first two moments and third-moment difference d, **TV of complete ordered three-bit laws = 4|d|**, while the two-visit ordered laws agree exactly. If the observer instead stops at the first success, with at most three visits, its four terminal masses are m_1, m_1-m_2, m_1-2*m_2+m_3, 1-3*m_1+3*m_2-m_3, so **TV of first-success stopping laws = |d|**.

Consequently over this entire fixed-first-two-moment fibre, the sharp ordered-three-bit TV diameter is 1/4, and the sharp first-success stopping diameter is 1/16. The optimal minimax reconstruction radii (allowing a valid common representative mu) are respectively **1/8** and **1/32**. Triangle inequality supplies the radius lower bound as half the endpoint diameter. The midpoint measure (mu_L+mu_U)/2 attains both radii, because each declared law is affine in m_3 and the midpoint is feasible.

With two equally likely source tags whose conditional mixing laws are mu_L and mu_U, a source-blind compressed common mixer equal to their midpoint realizes mean conditional risks 1/8 (complete three-bit) and 1/32 (stopping). Those are exact minima over common source-blind mixers, by the triangle inequality. This source-blind loss differs from Class I's two-visit **unrealizability** loss: both three-visit endpoint sources individually belong to the physical shared-port class.

## Provenance, verification, and literature boundary

REPRO_STAGE296B.py executes only Python standard-library Fraction and exact finite word enumeration. Its recorded output ends STAGE296B_COUPLING_AND_CUBIC_MOMENT_EXACT_PASS. Tested six rational values of a, both three-moment endpoint measures, nine rational convex mixtures, and their complete 8-word and first-success stopping distributions. Universal real-parameter claims follow the displayed algebra and Cauchy-Schwarz, **not** the finite checks. No native BRC executor, native X6 projection, native heartbeat experiment, full formal proof assistant or independent mathematical review was performed. A valid signed/phase cancellation law is not asserted.

External related work (background, not claimed proof of our numerical constants): Potaptchik, Roy & Schrittesser, *de Finetti's theorem and the existence of regular conditional distributions and strong laws on exchangeable algebras* (2023), https://arxiv.org/abs/2312.16349 ; Polson & Zantedeschi, *Predictive Coherence and the Moment Hierarchy: Martingale Posteriors for Exchangeable Bernoulli Sequences* (2026), https://arxiv.org/abs/2603.00661 . The latter studies predictive dependence on posterior moment hierarchy, consistent with why order-two information alone cannot determine three-step predictions; our fixed finite arithmetic constants and typed observer distinction are proved independently here.

Current native gateway direct status on 2026-10-30 reports research_authority_granted=false, registered_session_count=0, source-control code review required and new-job quota full (5/5). No active owner/CLAIM was authenticated; no native Result/Review/Driver acceptance is claimed. Source storage on an existing Draft PR is a portable author checkpoint, not formal task ownership or admission.

## Next executable unit

Stage297-B: classify finite parity/memory seed readout under **all declared future kernels** and derive a quantitative TV penalty when the seed label is erased but later exposed; separately determine the fourth-moment interval and observation-dependent diameter after three moments (four IID visits). In parallel identify what native X6 typed packet/port operations would be needed for a genuine observer-preserving correspondence proof, without inventing an embedding.
