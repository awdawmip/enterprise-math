# Stage295-B.2｜全局预随机化仍不能消除的双标签共享端口 LP 缺口

**Scientific status (2026-10-30):** `PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_REPLAY / UNREVIEWED / NOT_ADMITTED`. This is a precise **external finite positive-weight BRC-style ordered-word model**. It is neither a native P000/X6 dynamics theorem nor an admitted Source Result. The exact predecessor is Stage294-B / Stage295-B source residual in Draft PR #1736, immutable `18d06d646d79febdabb12ff112f474cb66b4f6ee`. This note settles its *fully pre-randomized shared-parameter strict-gap question for one declared two-label family*; it does not characterize every possible shared-port/coupling architecture.

## Frozen control and scientific inputs

- Verified `GLOBAL_KNOWLEDGE_V1` canonical `main@13c260412ff71512277f01b1de8beb92403c5924` (verified by identical GitHub compare against `main`); Enterprise Math canonical `main@dcfa196433e9b0dfe501e41345817aa4a91e5a77`.
- The global P000 startup projection blob `c6d4d2d79b09537bdae55253baef9c28583e44dc` was verified against its original global P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. The actual Enterprise Math P000 V5 blob at the project pin is `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`; ACTIVE Heartbeat/X6, joint-relation observer preservation and portable research protocols were read separately. The external two-bit observer is not asserted to embed into the six-axis Cell space.
- Source: `PROOF_STAGE294B.md`, `PROOF_STAGE295B_SOURCE_RESIDUAL.md`, `NEXT_TASK_PACKET_295B.md` at the predecessor commit above. The Stage294 deterministic-only `1/48` gap vanishes upon one valid two-atom pre-randomization. That result is retained and not reused as a mixed-strategy obstruction.

## Precisely declared two-label BRC experiment

Let `S∈{0,1}` be an upstream *provenance source tag*, each with mass `1/2`. On every realization visit **two distinct labeled stages A then B**, observing the complete ordered output `(Y_A,Y_B)∈{00,01,10,11}`. The observer also retains `S` for source-conditioned risk, but the compressed control cannot read S. No physical retuning of a shared port between A and B is permitted. The exact future operation is the second use of that same port; no further intervention, hidden seed readout or unbounded horizon is claimed.

The original uncompressed model has two distinct Bernoulli ports. Given S=0, A uses success parameter `a`, B uses `1-a`; given S=1, they are interchanged. Conditional on S the visits are independent. Restrict `0≤a≤1/2`; when `0<a<1/2`, **all eight source-labeled ordered leaf masses are strictly positive**. With `h=a(1-a)`, `r=(1-a)^2`, `s=a^2`, the four ordered leaves have laws

```
        00    01    10    11
P_0      h     r     s     h
P_1      h     s     r     h
```

The **free output-kernel LP** may use any source-blind distribution `Q` over these four ordered leaves (equivalently, a rational first-step kernel and a second-step history-adapted kernel). Its objective is

`R_free(Q) = [TV(P_0,Q)+TV(P_1,Q)]/2`.

The **physical compressed shared-port class** draws one global parameter `Theta∈[0,1]` before the two visits; conditional on `(S,Theta)`, the two Bernoulli outputs are **independent with the same parameter Theta**. Theta may have *any* mixing law, including an arbitrary S-correlated conditional law `mu_s` (an enlargement of source-oblivious pre-randomization). Thus every physical conditional output law has form

`Q_s(00)=E[(1-Theta)^2|s]`, `Q_s(01)=Q_s(10)=E[Theta(1-Theta)|s]`, `Q_s(11)=E[Theta^2|s]`.

The source-retaining physical risk is `R_phys(mu_0,mu_1)=[TV(P_0,Q_0)+TV(P_1,Q_1)]/2`. Requiring a single common mixing law `mu_0=mu_1` gives a subclass; the theorem solves **both** it and the larger source-correlated class. The setting may be an arbitrary real probability law, so this is not a finite setting grid or a deterministic parameter shortcut. The laws are positive BRC branch masses and serial conditional products, with exact `S,A,B,word` provenance; they are not signed amplitudes.

## Theorem 295.B.2 (sharp mixed shared-port gap, all a)

For every real `a∈[0,1/2]`, the exact optimal risks are

`inf_Q R_free(Q) = 1/2-a`,

`inf_(mu_0,mu_1) R_phys(mu_0,mu_1) = (1-a)^2-1/4`,

and the second infimum is unchanged if `mu_0=mu_1` is imposed. Therefore

`G(a) := min R_phys - min R_free = (1/2-a)^2`.

The gap is **strictly positive for every 0≤a<1/2**, including strictly positive leaf systems `0<a<1/2`. In particular at `a=1/4`,

`min R_free=1/4`, `min R_phys=5/16`, `G=1/16`.

### Proof: unrestricted LP optimum

The total variation triangle inequality gives for every Q:

`TV(P_0,Q)+TV(P_1,Q) ≥ TV(P_0,P_1) = |r-s| = 1-2a`.

Equality holds for the midpoint `Q*=(P_0+P_1)/2=(h,1/2-h,1/2-h,h)`. Thus `min R_free=(1-2a)/2=1/2-a`. The midpoint is genuinely implementable by a rational visible-history-adapted output kernel when a is rational: first choose `Y_A=0/1` equiprobably, then use `Pr(Y_B=1|Y_A=0)=1-2h`, `Pr(Y_B=1|Y_A=1)=2h`. Both conditional Bernoulli rates are in `[0,1]`; for `a=1/4` they are `5/8` and `3/8`. There is no dependence on hidden S.

### Proof: global lower bound over **all** pre-randomizations and source correlations

For every `theta∈[0,1]`, `theta(1-theta)≤1/4`, with equality exactly at `theta=1/2`. Integrating against **any** source-dependent mixing distribution yields `Q_0(01)≤1/4` and `Q_1(10)≤1/4`. Since event probabilities differ by at most TV,

`TV(P_0,Q_0) ≥ P_0(01)-Q_0(01) ≥ r-1/4`,

`TV(P_1,Q_1) ≥ P_1(10)-Q_1(10) ≥ r-1/4`.

Here `r=(1-a)^2≥1/4`, so no absolute-value ambiguity arises. Averaging gives `R_phys≥r-1/4` for **every real or rational mixing law**, even with source-dependent mixing and arbitrary correlations of the parameter with upstream S. Choose the same deterministic `theta=1/2` for each S. Its physical output distribution is uniform `(1/4,1/4,1/4,1/4)`. Because `r≥1/4` and `h,s≤1/4`, the only positive coordinate of `P_0-uniform` is word `01`, and for `P_1-uniform` it is word `10`; both TVs equal `r-1/4`. This attains the universal lower bound. Finally,

`(r-1/4)-(1/2-a) = a^2-a+1/4 = (1/2-a)^2`. QED.

This argument is a **complete continuum certificate**, not a rational-grid extrapolation. It proves the mixed gap persists under arbitrary source-parameter correlation only while the two draws remain conditionally IID given the one reused parameter.

## Structural characterization and explicit information loss

For a normalized exchangeable two-bit law `q=(A,T,T,B)` with nonnegative entries, a shared-parameter conditional-IID mixture exists iff

`A B >= T^2` (equivalently `Cov(Y_A,Y_B) >= 0`).

Necessity: writing `m=E[Theta]`, `d=E[Theta^2]`, we have `B=d`, `T=m-d`, `A=1-2m+d`; hence `AB-T^2=d-m^2=Var(Theta)≥0`. Sufficiency: for `m=T+B>0`, `d=B>0` and `d≥m²`, use parameter `p=d/m∈(0,1]` with probability `w=m²/d∈(0,1]`, and parameter `0` with probability `1-w`. This reproduces the first two moments and thus exactly q. For `m=0` use `Theta=0` with certainty. If q is rational, the certificate is entirely rational. This is the order-2 Hausdorff moment interface already used in Stage285–288, not a claimed new de Finetti theorem.

For the `a=1/4` free optimum `Q*=(3/16,5/16,5/16,3/16)`, `AB-T²=(9-25)/256=-1/16`: the free kernel contains a **negative joint correlation**, while the shared port forces a nonnegative one. Although the two single-visit marginals are both `1/2`, they do not certify safe collapse of the two-port interaction. This is the precise BRC observer-residual obstruction.

## Scope boundary: weakening conditional independence changes the answer

If one keeps merely the *same Bernoulli marginal rate* `1/2` at A and B but permits a shared hidden random seed to couple the two draws, the midpoint Q* becomes realizable: choose with probability `2h` a perfectly equal fair pair `(00 or 11, equiprobably)` and with probability `1-2h` a perfectly unequal fair pair `(01 or 10, equiprobably)`. Its ordered distribution is exactly `(h,1/2-h,1/2-h,h)`, the free LP midpoint, and the `G(a)` gap disappears. This is **not** conditional-IID repeated-port sampling and requires an enlarged coupling capability. Thus the sharp gap is a statement about an exact typed interface, not about every notion of reusing the same marginal port.

## Reproducibility, verification level, and current control boundary

`REPRO_STAGE295B_FULLMIX.py` (Python standard-library `Fraction`) independently checks five rational parameter cases, including the strict-positive `a=1/4` witness; exhausts 969 free 4-word probability kernels on denominator-16 grids and 70 five-node weight-denominator-4 mixed physical settings; checks the event inequality for each source separately, the rational two-atom positive-covariance reconstruction, and the negative covariance `-1/16`. Recorded stdout: `REPRO_STAGE295B_FULLMIX_EXECUTED_STDOUT.txt`, ending in `STAGE295B_FULLMIX_TWO_LABEL_EXACT_PASS`. The grids are **finite crosschecks**; all-real mixed optimality and the two-moment characterization are justified by the algebraic arguments above.

BRC reuse resolution: **REUSE_APPLIED**, using the positive-rational ordered-branch sum/product law and the truncated second-moment carrier; no native typed BRC executor was run. Novel general method/tool or physical prior-art priority is not claimed. Classical external reference context: Persi Diaconis, *Approximate exchangeability and de Finetti priors in 2022*, Scandinavian Journal of Statistics 50 (2023), 38–53, DOI `10.1111/sjos.12609`; Rina Foygel Barber et al., *De Finetti's theorem and related results for infinite weighted exchangeable sequences*, arXiv:2304.03927. These concern exchangeability representation and related extensions; the finite two-label risk calculation above is independently proved here.

Current Sites status observed 2026-10-30: `research_authority_granted=false`, `write_relay_enabled=false`, `registered_session_count=0`; native job quota reports `active_jobs=5`, `new_job_allowed_by_quota=false`; backend control indicates `UPSTREAM_CODE_REVIEW_REQUIRED`. The current active Task Owner could not be authenticated from this site. No native session, CLAIM, Result, review, Driver acceptance or X6 correspondence is asserted. Source storage and activity bookkeeping are separate from native research-role authority.

## Next executable problem

Stage296-B should quantify the least **admissible joint-coupling capability** needed to realize Q* and characterize whether an X6-native BRC interface permits conditional independence, source-sensitive seed transfer or adaptive port retuning. In the same two-label model, extend from two to three visits and find an exact hierarchy of order-2 versus order-3 observable residues under common-setting mixing. Keep Stage278-A N=12 Bellman frontier separate.
