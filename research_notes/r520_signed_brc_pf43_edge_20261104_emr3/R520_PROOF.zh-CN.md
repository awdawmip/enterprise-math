# R520 — signed BRC auxiliary scalar: all-positive-integer signs for the 43rd right-edge Toeplitz minor

Date: 2026-11-04. Scientific pin: R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f (R452/R462 fixed-t polynomial identity). Direct predecessor: R519 commit 0b0d9dfde3ba9406f716ccec2243011580fc6036. Status: AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED. The statement is internal to the original signed-BRC auxiliary scalar model.

## Exact statement and assumptions

For integer k>=1, put r=2k+1, C_k=binom(2k,k)/(k+1)>0. For integer 2<=t<=r define

    H_k(t)=binom(r+t,2t)*[x^r](1-x)*(1+x)^(2t)*(1+x^2)^(r-t),

with H_k(t)=0 outside that range. Define D_m(k)=det(H_k(3+i-j)) for 0<=i,j<m, D_0(k)=1.

**Conditional theorem, assuming the frozen R452/R462 fixed-t polynomial lemma:**

    D_43(k)>0 for 1<=k<=4 and for 9<=k<=38;
    D_43(k)<0 for 5<=k<=8 and for all integers k>=39.

There are no integer zeros. In r-coordinates, the strictly negative finite segment is r=11,13,15,17; positive segments are r=3,5,7,9 and odd r=19,21,...,77; the infinite negative tail starts at r=79. With the R519 result, D_42(k)>0>D_43(k) for k=5 and all k>=39, while D_42(k)<0<D_43(k) for k=9,10.

## Polynomial reduction

The frozen lemma states p_t(k)=H_k(t)/C_k belongs to Q[k], with deg p_t<=2t for each fixed t>=2. Toeplitz–Hessenberg expansion gives for f_m(k)=D_m(k)/C_k^m:

    f_0=1;
    f_m(k)=sum_{a=1}^m (-1)^(a-1)*p_(a+2)(k)*p_2(k)^(a-1)*f_(m-a)(k).

Induction bounds deg f_m<=6m: an a-th summand has degree <=2(a+2)+4(a-1)+6(m-a)=6m. Hence deg f_43<=258.

Put G_43(k)=[k(k+1)(2k+1)(2k+3)]^43*(k+2), strictly positive for all integers k>=1, degree 173. For k=1,...,86, compute the reduced rational values f_43(k)/G_43(k); L is the positive lcm of all their denominators. Let delta_j=Delta^j (L*f_43/G_43)(1), 0<=j<=85, and

    S_43(k)=sum_{j=0}^85 delta_j*binom(k-1,j).

The degree of G_43*S_43 is at most 173+85=258. The precise arbitrary-precision integer program checks for all 259 distinct integers k=1,...,259:

    L*D_43(k) = C_k^43*G_43(k)*S_43(k).

Both sides divided by C_k^43 represent polynomials of degree <=258; equality at 259 distinct points proves L*f_43=G_43*S_43 identically as polynomials in Q[k]. This is an exact finite proof of the interpolation identity under the frozen lemma, rather than an interpolation guess at the untested tail.

## Signs for the full infinite integer domain

The complete evidence R520_EVIDENCE.json records L, all 86 integer delta_j, the 259-point identity check, the pre-tail values, and the shifted coefficients. Exact pre-tail checks k=1,...,38 give sign blocks + on 1..4, - on 5..8, and + on 9..38.

Let epsilon_j=Delta^j S_43(39) for j=0,...,85. The exact certificate finds **all 86 epsilon_j strictly negative**. For every integer u>=0, binom(u,j)>=0 and binom(u,0)=1, so

    S_43(39+u)=sum_{j=0}^85 epsilon_j*binom(u,j)<0.

Since L, C_k and G_43(k) are strictly positive for k>=1, D_43(k)<0 for every integer k>=39. In particular there is no zero in the classified domain.

## Independent implementation checks

R520_VERIFY.js uses exact BigInt operations and verifies all 259 interpolation identities, 20 direct original-signed 43x43 determinants via Bareiss elimination against the Hessenberg recurrence, and 860 raw-signed-convolution versus ballot–Catalan identities (k=1,...,20; t=2,...,44). Run: node R520_VERIFY.js > R520_EVIDENCE.json. The source emits R520_EXACT_JS_PASS.

R520_INDEPENDENT.py uses a separately written signed coefficient formula, SymPy's exact Berkowitz determinant method on 18 direct 43x43 integer matrices for k=1,2,3,4,5,6,7,8,9,10,11,12,14,15,37,38,39,40; it checks the recursive ballot expression and separately verifies 860 signed/ballot coefficient identities. Its actually executed output is R520_INDEPENDENT_PASS; the captured output is R520_INDEPENDENT_EVIDENCE.json. These checks are author-side cross-implementation evidence, not an independent mathematical admission.

## Research frontier

P000, the ACTIVE worldview, and the scientific pin were unchanged. Native Task Owner cannot be confirmed: em_control_tasks returned CONTROL_QUOTA. em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No native Researcher-ID, CLAIM, Result or independent Driver review was created. The PR branch records a reproducible, unreviewed author-side theorem candidate.

Next smallest uncompleted unit: s=3,m=44, with degree bound <=264, 88 Newton coefficients and 265 distinct exact identity points. A structurally distinct route fixes k=4,5,8,9,38,39 and studies the denominator and dominant roots of the rational order-generating function derived from the recurrence. Its exact denominator is

    1 - sum_{a=1}^{2k-1} (-1)^(a-1) H_k(a+2)H_k(2)^(a-1) z^a.

Use root isolation or algebraic factorization to investigate the sign-transition mechanism while retaining the original signed auxiliary scalar scope.
