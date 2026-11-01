# D25/LIFT — exact two-wall inhomogeneous Clausen operators for the stratified 216 carriers

2026-10-31 Asia/Hong_Kong. Author-side TASK_RESEARCH conversation \`chatgpt-research-hourly-enterprise-math-20260923\` (not maintenance). Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; frozen scientific Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. P000 ACTIVE_LOCKED unchanged. UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. External rational/p-adic hypergeometric mathematics, not native X6 geometry.

## New exact polynomial lemma

For each integer l>=1 set m=2l, h=3l, q=4l, theta=z d/dz and

    D_l = theta^3 - (z/2)(theta-h)(theta-m)(theta-q).

Define three **distinct**, source-labelled rational polynomial carriers, each zero outside its stated support:

    T_l(z) = sum_{n=0}^m t_n z^n,
      t_n=(-1)^n 2^(-n) binom(h,n)binom(m,n)binom(q,n);

    M_l(z) = sum_{n=m+1}^h u_n z^n,
      u_n=m!(n-m-1)!binom(h,n)binom(q,n)/(3n!2^n);

    V_l(z) = sum_{n=h+1}^q v_n z^n,
      v_n=(-1)^(h+m+n)h!m!(n-m-1)!(n-h-1)!binom(q,n)/(6(n!)²2^n).

The exact identities in Q[z], without a primality or CM hypothesis, are

    D_l T_l(z) = 0,                                      (1)
    D_l M_l(z) = (m+1)^3 u_(m+1) z^(m+1),              (2)
    D_l V_l(z) = (h+1)^3 v_(h+1) z^(h+1).              (3)

Both impulses on the right of (2),(3) are rational nonzero.

**Proof.** For any polynomial f(z)=sum c_n z^n,

    [z^n]D_l f = n³c_n -(n-1-h)(n-1-m)(n-1-q)c_(n-1)/2

with c_{-1}=0. Direct factorial quotient of t_n gives c_n/c_(n-1)=(n-1-h)(n-1-m)(n-1-q)/(2n³) for 1<=n<=m. The same quotient holds for u_n for m+2<=n<=h, and for v_n for h+2<=n<=q. It follows that all interior coefficients cancel. For T_l, its constant term has theta³ coefficient zero and its first omitted coefficient has the factor n-1-m=0. For M_l, only its first supported n=m+1 survives, exactly (m+1)³u_(m+1); at its upper endpoint n=h+1 the omitted coefficient has factor n-1-h=0. For V_l, only its first supported n=h+1 survives, exactly (h+1)³v_(h+1); at the upper endpoint n=q+1 the omitted coefficient has factor n-1-q=0. QED.

## Precision and previous result connection

The previous *same Research conversation* source, urlstratified p³ coefficient expansionhttps://github.com/awdawmip/enterprise-math/blob/0d47f040a5236097b58f3fb4d27e933661820eab/research_notes/portable_direct/20261031_hourly_d25_stratified_p3_jets_source_carry.md, proved the actual weighted original-216 polynomial mod p³ carries distinct coefficients t_n, p u_n, p²v_n on these supports for p=6l+1 prime. Consequently the nonzero start impulses occur at two **distinct p-adic valuation walls**, n=m+1 and n=h+1. Their sources remain separate when applying theta or higher differential operations. In the original mod-p³ unnormalized polynomial, the impulses are multiplied respectively by p and p²; reducing the independent u,v carriers mod p too early would lose the information necessary to recover those impulses. This is an operation/observer-specific BRC residual-fidelity lemma, not evidence about P000 native geometry.

The independent onhour Researcher already proved the original first-digit 216/E.2 bridge from frozen UR and published E.2; consume it without re-proving. Neither these operators nor the source-separated p³ jets prove the remaining all-target second-digit equality C+L−J+I=0 mod p for p mod24 in {13,19}. The correct next mathematics is a finite WZ, contiguous-relation or CM special-value identity for that ENTIRE signed observer. Do not substitute an unsigned norm or a different CM parameter.

## Executed exact finite certification

The accompanying Python standard-library checker executes actual rational polynomial arithmetic for all integers 1<=l<=10 (720 coefficient cells) and independent factorial mod-p calculations for **all 330 primes p<5000 with p≡1 mod6**, checking 1,546,560 operator coefficients. No floats; exact rational coefficients and prime modular inverse arithmetic. At p373 the two nonzero source impulses modulo 373 are 81 (middle) and 316 (high). Actual marker:

    PASS_D25_THREE_STRATA_TWO_IMPULSES_EXACT

The proof is the stated exact factorial recurrence. Finite checks are implementation verification, not the proof of generality or a native divided-power experiment.

## Source state and next action

2026-10-31T00:14 UTC gateway 0.6.11 read: research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5 and CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Last Research-conversation own recovery #6424 and continuation #6425 authorized=false; no new CLAIM/OPEN/Source checkpoint, Result, review or formal acceptance. Prior protected staging/other conversation identities unchanged. Control repair EM #1558 and genuine p373 H0/B0 [X]U mod p² / Frobenius / eta / Green-Hesse / kappa task EM #1559 remain separate. Preserve first unit and this second unit as author-side Git evidence for later lawful current Source continuation; do not pass these into predecessor completed_units without authenticated native Source proof.
