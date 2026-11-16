# PREFIX-839 — Two adjacent late Q histograms exactly reconstruct the unmarked source-weight multiset

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

**Scientific input pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Continuation:** PREFIX-827 future trace symmetric-coordinate formula, PREFIX-832 full-time bin difference, PREFIX-833 temporary recollision, PREFIX-834..838 exact resource constructions. This is the positive integer named-source BRC **Q-only auxiliary model**. Its time index is a formal iteration count; no X6 physical duration, native Cell/Link/Port permission or signed cancellation is asserted.

## Model

Fix p=q>=1. There are p initially present, individually named **unmarked** sources with positive integer removal weights w_1,...,w_p; one initially absent marked source has positive integer addition weight a and removal weight b. The capacity is p. At every step, Q=R+A sums all legal removal alternatives, weighted by the removed source's weight, and the legal marked-source addition alternative, weighted by a. Let Y_l(t) be the resulting **unnormalized integer count/mass** in occupancy bin l (0<=l<=p) after t operations. Outputs forget which named sources remain. The weights a,b,p and time t are known, and the unknown is the weight multiset {w_1,...,w_p}.

Set e_d=e_d(w_1,...,w_p), e_0=1, e_{p+1}=0, lambda=ab>0.

## Theorem 839.1 (constructive global reconstruction from two adjacent observations)

**For every p>=1, every choice of positive integers a,b,w_i, and every integer t>=p-1**, the two complete occupancy histograms (Y(t),Y(t+1)) determine e_1,...,e_p uniquely, by the following exact, integer-divisible triangular inverse.

For d=p,p-1,...,1 choose tau_d as the unique member of {t,t+1} having the same parity as d. Then tau_d>=d, and define

```
alpha_d = d! * binom(tau_d-1,d-1) * (ab)^((tau_d-d)/2) > 0.
beta_d = 0                                        if d=p or tau_d<d+2;
         (d+1)! * binom(tau_d-1,d) * a
           * (ab)^((tau_d-d-2)/2)                  otherwise.
e_d = (Y_{p-d}(tau_d) - beta_d * e_{d+1}) / alpha_d.
```

All divisions are exact in the stated integer model. The unordered multiset is then the multiset of roots of the monic integer polynomial

```
P(X) = X^p - e_1 X^(p-1) + e_2 X^(p-2) - ... + (-1)^p e_p.
```

Only **p scalar bins**, one Y_{p-d}(tau_d) for each d=1,...,p, are needed across the two frames. The corresponding p-by-p linear observation matrix, ordered by d=p down to 1 in both rows and columns, is triangular, with nonzero diagonal alpha_d, so its determinant is product_{d=1}^p alpha_d (with that ordering).

**Proof.** By the full exact named-source trace formula established in PREFIX-827/832, any positive-time path removes d>=1 distinct unmarked sources and ends with marked-presence bit m in {0,1}. With r=(tau-d-m)/2>=0 an integer, the total contribution to occupancy l=p-d+m is

```
d! * binom(tau-1,d-1) * e_d * a^(r+m) * b^r.
```

At occupancy l=p-d, the only possible terms have (number removed, marked bit) equal to (d,0) or (d+1,1). Thus at tau_d the bin is exactly `Y_{p-d}(tau_d)=alpha_d e_d+beta_d e_{d+1}`. The second term is absent at d=p or tau_d<d+2. Since tau_d>=d, lambda>0 and binomial(tau_d-1,d-1)>0, alpha_d is strictly positive. Starting from e_{p+1}=0, backward substitution gives the formula and uniqueness. The genuine source weights make all divisions integer-exact. The polynomial identity follows from Vieta's formula. QED.

The condition t>=p-1 is sufficient for this uniform triangular reconstruction, since it guarantees tau_d>=d even for d=p. At earlier two-frame horizons t<=p-2, the observation times are both below p, so no trace term contains e_p; the full coefficient vector is not identifiable as a general symbolic-coordinate problem from those frames.

## Theorem 839.2 (exact irreducible provenance fiber)

The entire count-only Q history is invariant under permuting the **names** attached to the initial weights. Two named assignments differing only by a label permutation have the same Y_l(t) for every t and l. Conversely, the two adjacent histograms in Theorem 839.1 separate any two **different weight multisets**.

Therefore, for a multiset containing distinct values v with multiplicities m_v, the count observer has an exact unresolvable name-assignment fiber of size

```
p! / product_v(m_v!).
```

If downstream operations or outputs distinguish name/port provenance, those labels must be retained or supplemented; they are not reconstructible from Q occupancy counts alone.

**Proof.** The Q transition commutes with every permutation of unmarked names, and occupancy summation is invariant under that permutation. Orbit-stabilizer gives the stated fiber cardinality; Theorem 839.1 proves no different multiset lies in the common two-frame fiber for t>=p-1. QED.

## Exact regression and deliberate re-alias witnesses

The accompanying standalone Node.js BigInt checker implements the named-subset-plus-marked-bit state machine independently of the closed-form expression, checks **every** histogram bin against the PREFIX-827/832 formula, and reconstructs all e_d from two consecutive frames:

- p=1..5, every nondecreasing multiset of p weights from {1,2,3,4};
- a in {1,2,3}, b in {1,2,4};
- t=p-1,...,p+5 for every configuration;
- for p>=2 also reverse the name-to-weight assignment and check all output frames;
- exact recollision witnesses: p=2, T=3 with (1,7) vs (2,4); p=3, T=4 with (1,4,10) vs (2,2,11); p=3, T=34 with (1,16,16) vs (2,5,26). For each, Y_A(T)=Y_B(T) but Y_A(T+1) differs, and the reconstructed elementary-symmetric vectors differ.

Program and stored result: `PREFIX839_R6_TWO_FRAME_RECONSTRUCTION_CHECK.js`, `PREFIX839_R6_TWO_FRAME_RECONSTRUCTION_RESULTS.json`. All arithmetic is native BigInt and exact divisibility is asserted. The finite regression corroborates the all-p proof; it is not a replacement for it. Inverse arithmetic at unbounded t may require large integers, and no complexity improvement over full simulation is claimed without bit-cost accounting.

## Research relationship and next work

Theorem 839.1 strengthens the observer treatment in PREFIX-833: a *fixed pair of adjacent late-time frames* recovers the complete symmetric source state, despite any possible one-frame re-alias. Theorem 839.2 identifies the exact named-provenance residual that this count observer cannot recover. These statements are internal to the typed Q-only BRC count observer; an independent typed interface is needed before transfer to native X6 time/Cell/Link/Port or physically meaningful durations.

**Open:** (i) smallest labeled observation augmentation that also recovers all name assignments without full raw trajectory; (ii) exact bit complexity of reconstructing e_d from large t, compared with one-step state updates; (iii) whether the general q>=5 nonnegative integer carrier lower bound from PREFIX-825 can be attained by constructive positive matrices; (iv) uniform even-T growth of M(T) beyond the verified finite window and Pell subsequence.

Author-only proof/check; independent mathematical review and Source theorem admission remain pending.
