# PREFIX-615-R6 — Exact geometric time change for BRC sign-adaptive stopping

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scientific dependency: PREFIX-610 signed-label law, PREFIX-611 Blackwell tag order, PREFIX-613 anytime confidence sequences, PREFIX-614 exact coverage waiting-time moments. Original native source: PREFIX-565 blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
No new native PREFIX-565 96-port graph execution or physical-time claim is made.

## The precise observable and model

For 1 <= k <= 6, d=2k <=12, and |theta_l|<1/48, independent one-step native BRC observations of terminal phase jointly with the Boolean action-slot tag induce the following *restricted-family* signed-label readout:

    P_q(Y=(l,s)) = (1+48*s*theta_l)/(2*q),  l=1,...,d, s in {-1,+1}
    P_q(Y=neutral)=1-d/q.

Here q=12 for slot 0; q=24 for slots 1 or 2. In particular conditional sign probabilities remain (1+48*theta_l)/2 under either tag. The raw terminal-phase, branch/provenance and slot observation stays available; the signed-label projection is used only for this declared family and for stopping/inference functions of the resulting labels. A single trial is a fresh independent *one-step* native action; N trials do not constitute one native N-step trajectory.

A stopping decision is **neutral-invariant** if inserting or deleting neutral labels leaves the decision at an informative event unchanged; the rule stops only at such a marked event, not at a fixed calendar deadline or on a run of neutral observations. It may depend on all previously observed informative direction labels AND their signs, on data-dependent confidence bounds, and on independent auxiliary randomization. Assume its number S of q_a trials until stopping is a.s. finite; moment conclusions require the corresponding finite moments.

## Theorem A: full stopping-time law, not only its first two moments

Let q_b >= q_a >=d, put p=q_a/q_b in (0,1], and use the same theta and marked alphabet. Then the complete experiment laws obey the exact mixture identity

    P_{q_b} = p P_{q_a} + (1-p) delta_neutral.

Let S=T_{q_a} be any neutral-invariant stopping time as above. There exists a coupling with independent G_1,G_2,... ~ Geometric(p), supported on {1,2,...}, such that

    T_{q_b} = G_1+...+G_S  almost surely.

The G_i are independent of the entire q_a observation stream, hence independent of S. Consequently, for 0<=z<=1,

    E[z^T_{q_b}] = E[(p*z/(1-(1-p)*z))^S].

For n>=1 the exact point mass and CDF transforms are

    Pr(T_{q_b}=n) =
      sum_{m=1}^n Pr(S=m) * binom(n-1,m-1) p^m (1-p)^(n-m),

    Pr(T_{q_b}<=n) =
      sum_{j=0}^n binom(n,j) p^j (1-p)^(n-j) Pr(S<=j).

In the second formula Pr(S<=0)=0. The coupling shows T_{q_b}>=T_{q_a} pathwise. The domination is strict in distribution for p<1 and S>=1 a.s.

**Proof.** Independently draw an i.i.d. q_a mark stream Y_1,Y_2,... and Bernoulli(p) gates for successive global trials. On a successful gate emit the next Y_i; on failure emit neutral. At each global trial the emission distribution is p P_{q_a}+(1-p)delta_neutral=P_{q_b}, and emissions are independent. The waiting time G_i between consecutive successful gates is geometric(p), independent of the entire mark stream. A neutral-invariant stopping rule reaches the same terminal informative mark in either stream; every inserted neutral is ignored. Hence the q_b global stopping index is the sum of the first S geometric gaps. Conditional on S=m this is the negative-binomial time to m gate successes, giving the point-mass formula and PGF. At global time n the number of successful gates is an independent Binomial(n,p) count B_n, and stopping has occurred precisely when S<=B_n. Averaging yields the CDF transform. The coupled inequality is immediate. QED.

## Theorem B: exact all-order moment transport; explicit third cumulant

Write mu_a=E S, v_a=Var S and c3_a=E[(S-mu_a)^3]. Under finite third moments:

    E T_b = mu_a/p
    Var(T_b) = [v_a+(1-p)*mu_a]/p^2
    c3_b = [c3_a + 3(1-p)*v_a+(1-p)(2-p)*mu_a]/p^3.

**Proof.** For a geometric(p) waiting time supported on positive integers, its first three cumulants are 1/p, (1-p)/p^2, and (1-p)(2-p)/p^3. Conditional on S, the cumulant generating function of the random sum is S times that of G. Expanding the composition K_S(K_G(t)) through order three gives the formulas. The exact PGF proves analogous transforms for all factorial moments for which they exist. QED.

For the native q_a=12, q_b=24, p=1/2:

    E T_24=2 E T_12
    Var T_24=4 Var T_12 + 2 E T_12
    c3(T_24)=8 c3(T_12)+12 Var T_12+6 E T_12.

PREFIX-614's mean and variance statements are special cases. The present result identifies the *whole law* and also works for sign-adaptive stopping.

## Theorem C: informative-time confidence paths are identical under the coupling

The PREFIX-613 anytime e-process and its rectangular confidence sequence depend on the trial history only through informative direction/sign counts (M_l,K_l). Inserted neutral labels leave these counts unchanged. Therefore in the construction of Theorem A, at each successive retained informative mark the confidence region is exactly identical for q_a and q_b, sample-path by sample-path. A decision such as "stop at the first informative observation when all confidence interval diameters are <=epsilon" (if it terminates almost surely) obeys the same geometric time-change distribution, even though its stopping decision uses observed signs. Any Ville guarantee derived for the original confidence sequence survives this stopping rule; the success/precision claim is about the declared signed-label experiment.

This gives an exact separation: **statistical inference as a function of informative data is identical** while the global native-action budget differs by a random geometric clock. A stopping rule using calendar time, neutral-run lengths, or additional raw observables requires its own analysis.

## New exact sign-dependent example

Take d=2, theta_1=0, theta_2=1/96 (inside the stipulated open domain). Stop at the first trial where both direction IDs have appeared and at least one direction has been observed with *both* signs. A four-bit state records the seen positive/negative signs separately for both directions; self-loops and transitions are solved by exact rational Markov recurrences. Unlike pure coupon coverage, this decision depends essentially on signs.

For q=12:

    E T_12=198/7,
    Var T_12=14090/49,
    c3(T_12)=2492850/343.

For q=24, an independent rational-state computation gives

    E T_24=396/7,
    Var T_24=59132/49,
    c3(T_24)=21184572/343.

These values satisfy all three transforms exactly. They also validate that the statement covers a rule beyond index-count-only stopping.

## Verification, boundaries and next question

Executable standard-library exact certificate: PREFIX615_R6_geometric_time_change_certificate.py. Companion literal result: PREFIX615_R6_RESULTS.json. The certificate independently enumerates finite capped-occupancy CDFs for d=2,4,6, thresholds r=1,2 and horizons n<=16 for each q, verifies the binomial CDF transform, then independently enumerates the sign-dependent four-bit stopping rule through n=24 and solves its first three raw moments. Exact Fraction/integers only, with 374 assertions: ALL_CHECKS_PASS.

This proves a general structural theorem directly from the inherited PREFIX-610 law and a standard elementary coupling. It does not recompute the original 48-phase/96-port BRC evidence, certify statistical novelty relative to all literature, confer formal task Result/Review authority, or replace future-use observer-preservation checks.

Next: characterize the smallest native terminal-phase/tag readout that reconstructs the entire signed-label marked sequence for all nine frozen roots; separately compare count-only versus sign-adaptive confidence-diameter stopping for fixed theta, with exact finite-state or bounded-error expectation calculations. Reuse the geometric clock instead of independently recomputing q=24 experiments.