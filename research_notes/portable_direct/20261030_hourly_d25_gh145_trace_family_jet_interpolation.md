# D25/LIFT GH-145 — Exact trace-family jet interpolation and marked first moment

Date: 2026-10-30 (Asia/Hong_Kong); lane TASK_RESEARCH, chatgpt-research-hourly-enterprise-math-20260923. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## General theorem

Let p≥5 be prime, K=F_(p²), q=p², e=(q−1)/2, χ quadratic character χ(0)=0. With f_B(x)=x³+x²+Bx define the finite-field polynomial (not an integer trace function):

  T_p(B)=Σ_(x∈K) f_B(x)^e ∈F_p[B]⊂K[B], degree at most e<q.

It evaluates at every B∈K to Σ_x χ(f_B(x)). For smooth E_B:y²=f_B(x) (B≠0,1/4), T_p(B)=−a_q(E_B) mod p, a_q=q+1−#E_B(K). Singular supports are T_p(0)=T_p(1/4)=−1; direct factorization x²(x+1) and x(x+1/2)² proves these values.

**Marked jet identity.** Define S_1(B)=Σ_(x,f_B(x)≠0)χ(f_B(x))x/f_B(x). Differentiate the *polynomial* T_p(B): since e≡−1/2 mod p and χ(f)=f^e on K,

  T_p'(B)=e S_1(B); hence S_1(B)=−2T_p'(B).

This is not the invalid derivative of an integer-valued point count.

**Exact full trace-family resolvent.** All polynomials over K of degree <q have interpolation using 1−(X−v)^(q−1), for v∈K: this is one at X=v and zero at other field points. In particular

  T_p(X)=Σ_(v∈K)T_p(v)[1−(X−v)^(q−1)].

Differentiate and evaluate at B. Since −(q−1)=1 in K, the v=B derivative is zero, and at v≠B the derivative is (B−v)^(q−2)=1/(B−v). Therefore

  S_1(B)=−2Σ_(v∈K,v≠B)T_p(v)/(B−v).

For B≠0,1/4 use the elliptic trace and singular supports to obtain

  S_1(B)
    =2Σ_(v∈K\{0,1/4,B})[a_q(E_v) mod p]/(B−v)
     +2(1/B+1/(B−1/4)).

These are exact identities at all parameters in their declared range, including the first identity at singular parameters. They show why one unmarked CM/Frobenius trace cannot determine the marked derivative: the resolvent consumes the *entire parameter-labelled family*. This is a new-to-this-project explicit finite-field interface, not a source-independent analytic evaluation of S_1(B0), nor a proof of GH-3/GH-83 or native p² lift. The O(q) trace-family sum makes no computational complexity improvement claim.

BRC carrier: (p,K,{v,T_p(v)},B,source labels,singular supports). Observer: marked S_1(B); operation: formal polynomial derivative followed by labelled field interpolation. Removing parameter labels loses the resolvent weight. The theorem is auxiliary finite-field algebra, not a P000-native six-dimensional proof.

## Actually executed verification

The Python standard-library verifier d25_gh145_trace_polynomial_jet_check.py independently constructs every T_p(v) by exhaustive cubic quadratic-character sums, computes marked S_1(B) directly using x/f_B(x), then computes the whole-family resolvent at every B∈K. For p=5,7,11,13,19 there are 25+49+121+169+361=725 independent parameter instances. All passed, including singular T_p(0)=T_p(1/4)=−1 for each p. Terminal marker: PASS_GH145_TRACE_POLYNOMIAL_JET_INTERPOLATION. The general result follows from the proof, not the samples.

No separate new native p=373 experiment, independent p3347 special-value computation, native authorized OPEN, Source checkpoint, review or admission is claimed. This supplements but does not repeat GH-124's Hasse identity; the new step is the exact whole-trace-family Lagrange jet reconstruction.

## Remaining proof obligation

Seek an independent CM/Jacobi/Gauss or p-adic reduction of the *labelled trace resolvent* at B0=(1+2√2/3)/8, or an independent evaluation of central blind-band moments, genuinely predicting S_1(B0) and R_3347(9)=0 without using GH-124/GH-145 as circular input. Native D25 H0/B0 divided-power, [X]U mod p², Frobenius, η and p=373; GH-3/GH-83 remain OPEN. Source/native control support is tracked in #1558; published portable work does not enter Source completed_units. P000 and frozen science pin unchanged.
