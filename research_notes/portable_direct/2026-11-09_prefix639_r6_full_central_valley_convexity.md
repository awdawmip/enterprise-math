# PREFIX-639-R6 — Full central-slice strict convexity and sharper optimal BRC mean–variance bounds

Date: 2026-11-09 (Asia/Shanghai). Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Research mode: independent TASK_RESEARCH; no formal shared-task CLAIM.
Status: AUTHOR_PROVED / EXACT_RATIONAL_BERNSTEIN_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model and theorem

Use the fixed signed two-information-direction BRC first-passage statistical observer of PREFIX-621/622. Fix the second probability z=19/128, the first-parameter interval I=[3/20,1/6], and q in [12,24]. The q interval is an analytic interpolation; the actual slots are q=12,24. Let Y be the unit-rate informative Poisson stopping time, mu(p)=E[Y], W(p)=Var(Y), F_q(p)=W(p)-mu(p)/q.

**Theorem 639.1.** For every real p in I and real q in [12,24],

    274 < mu'(p) < 321,
    27100 < F_q''(p) < 48100.

Consequently each F_q is strictly convex throughout I, and the unique interior minimizer previously certified in PREFIX-635 on [4/25,161/1000] is also the unique global minimizer on I. In particular, this proves uniqueness throughout the full first-parameter valley interval bracketed by the derivative reversal of PREFIX-631 at this z.

## Exact rational Bernstein proof

Reconstruct the frozen dyadic stopping survivor recurrence with DEN=2^18 and n<=189. A sign-count k at layer n survives according to the strict-integer test

    40(n+1) binom(n,k) a^k (DEN-a)^(n-k) > DEN^n

in the dyadic width check from PREFIX-621. The certificate checks first stopping layer n=25 and complete extinction after layer n=189. The resulting finite row[n,k] yields

    s_n(p)= sum_k row[n,k] p^k (1-p)^(n-k)
          = sum_k [row[n,k]/binom(n,k)] B_(n,k)(p).

For fixed z=19/128 let w(n,m)=binom(n+m,n)/2^(n+m+1). The exact PREFIX-622/635 moment identities use

    alpha_n=1-sum_m w(n,m)s_m(z);
    beta_n=(n+1)-sum_m ((n+m+1)/2)w(n,m)s_m(z);
    mu(p)=sum_m s_m(z)+sum_n alpha_n s_n(p);
    H(p)=constant_in_p+sum_n beta_n s_n(p);
    W(p)=2H(p)-mu(p)^2.

Therefore F_q is, up to an additive constant, 2 sum_n beta_n s_n - mu^2 - mu/q. The coefficient program uses only exact integers and Fraction arithmetic: degree-elevate every survivor polynomial into degree-188 Bernstein mu and H; form the degree-376 Bernstein product mu^2; differentiate the degree-376 F_q twice to obtain degree-374 F_q''; and restrict its Bernstein coefficients to I with exact rational de Casteljau subdivision. Similarly form and restrict the degree-187 mu' coefficients.

The certificate compares **all 188** mu' Bernstein controls, with exact minimum coefficient floor 274 and maximum coefficient ceiling 321. For the **375** Bernstein coefficients of F_q'' on I, the computed floors of the minima and ceilings of the maxima are q=12: (27156,47941), q=24: (27260,48065). Every exact control lies strictly inside the stated envelopes. Bernstein convex-hull positivity proves the inequalities for every real p∈I. F_q'' is affine in t=1/q; endpoint q=12 and 24 thus imply the same strict envelope for every intermediate real q. PREFIX-635 already supplies a unique interior stationary minimum in the smaller interval inside I. Strict F_q convexity over I makes it the unique global minimum over I. QED.

## Theorem 639.2 — Improved optimal informative mean/variance curvature

For t in K=[1/24,1/12], let c(t)=argmin_{p∈I}(W(p)-t mu(p)), A(t)=mu(c(t)), B(t)=W(c(t)). The optimizer remains within the earlier PREFIX-635 small interval [4/25,161/1000], where 300<mu_p(c)<310 is already independently certified. Combining it with the new F_q'' envelope yields

    900/481 < dA/dt < 961/271.

For the two actual optimizer choices (q=12 and q=24), the new rigorous positive gaps are

    75/962 < A(1/12)-A(1/24) < 961/6504,
    75/15392 < B(1/12)-B(1/24) < 961/104064.

Moreover the exposed mean–variance arc b(a)=B(A^{-1}(a)) from PREFIX-638 has the improved strict curvature envelope

    271/961 < b''(a) < 481/900.

Proof. At the interior critical point W_p(c)=t mu_p(c) and F_pp>0, so c_t=mu_p/F_pp, A_t=mu_p^2/F_pp, B_t=t A_t, and b''=1/A_t. Insert 300<mu_p<310 and 27100<F_pp<48100. For the mean-gap bounds integrate dA/dt over K, of length 1/24. For the variance-gap bounds integrate t dA/dt, observing integral_K t dt=1/384. The script also checks every exact rational reduction and improvement over PREFIX-637/638. QED.

These gaps refer to the variance W and expectation mu of informative Poisson stopping time Y, as defined; they are not directly the q-thinned native variance q²W-q mu. The frozen original 96-port native graph is unchanged.

## Verification and continuation

The standalone companion Python standard-library exact certificate regenerates all 189 stopping layers and all 188+2×375 restricted Bernstein controls, then validates the rational implications. Actual local execution 2026-11-09: ALL_CHECKS_PASS 14720, with extrema listed above. This is an exhaustive finite algebraic proof of the stated universal-in-p inequalities within the fixed statistical observer, not a finite sample mesh. No independent mathematical review or Result/Review admission has occurred.

Predecessor references: PREFIX-631 (cab564fd9a112feed4a5a1fac0ee5556ebe7d7b6), PREFIX-635 (ec03483204af911eef75785bcdaf610d24519ab2), PREFIX-636 (c70457fde1d39265b126976bd92126731c31c23e), PREFIX-638 (2ebec8fa75126f8c2c3bc8c086a7add9ae5a0c2a).

Next exact challenge: extend the certificate in z from the central value 19/128 to all z∈[37/256,39/256] through two-variable Bernstein subdivision, checking mu_p, F_q'' and endpoint gradient signs. The full two-dimensional global sampling-variance maximum remains the mother objective.
