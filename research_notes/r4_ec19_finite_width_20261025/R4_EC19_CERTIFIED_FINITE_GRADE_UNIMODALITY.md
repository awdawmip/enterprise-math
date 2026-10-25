# R4-EC19 — An exact 512-grade, infinite-depth unimodality theorem for the auxiliary BRC kernel

**2026-10-25 | Author-side computer-assisted exact proof | Not independently reviewed or admitted**

**Scope.** This is the positive ordered binary affine **auxiliary** BRC grade/clean-source observer. It is neither a P000-native X6/Heartbeat dynamic statement nor a result preserving every possible future input word. Residual provenance and full ports are not removed. Read-snapshot authority: GLOBAL_KNOWLEDGE_V1 main@b034e5f7f3f65b3086830e7e3f8d53b28a382be4; initial Enterprise Math Source main@22a83b434187eb4fad90bdec903d91e7417ff4fc. Exact antecedents: R4-EC17 21b4d804272b563191b46eaee6c436515781f077 and R4-EC18 79ccbf8c8ee6d4f79986bef0eb88c4ce6973df57 (their theorem/admission status is unchanged).

## Exact model

Let E[n,j] be the x^n u^j coefficient of the formal rational series

\[
 E(x,u) = \frac{1-u x^2}{1-(1+u)x+2u^2x^4-u^3x^6}.
\]

EC17 proves E[n,j]=E[n,n-j], E[n,j]>=0 and the source-reflection identity

\[
 D[n,k] := C[n,n-k]-C[n,k]
 = E[n-3,k-1]-E[n-3,k-2].
\]

EC18 proves a quadratic parabolic positivity wedge n>=4j^2. The present theorem supplies unbounded depth for 512 fixed grades, including substantial territory outside that earlier wedge.

## Theorem EC19-FW512

For ALL integers n>=10 and 1<=j<=min(floor(n/2),512),

\[
\boxed{E[n,j] \ge E[n,j-1].}
\]

Equality occurs **only** at (n,j)=(10,3) and (12,4); the inequality is otherwise strict throughout this infinite set.

**Corollary EC19-D513.** For 2<=k<=513 and n>=max(13,2k+1),

\[
 D[n,k]=C[n,n-k]-C[n,k]\ge0.
\]

Equality occurs exactly at (n,k)=(13,4),(15,5). In the separate k=1 case, EC16 gives D[n,1]=1 for n>=3.

## Proof: exact rational coefficient reduction

Define E_j(x)=[u^j]E(x,u). Extracting grade coefficients from the defining rational identity gives

\[
 E_j(x)=A_j(x)/(1-x)^{j+1},
\quad A_0=1,\quad A_1=x-x^2+x^3,
\]

and with A_{-1}=0, for every j>=2,

\[
 \boxed{A_j=x A_{j-1}-2x^4(1-x)A_{j-2}
                 +x^6(1-x)^2 A_{j-3}.} \tag{1}
\]

By induction deg A_j<=3j: each shifted summand has degree at most 3j-2, 3j-1, 3j-1 respectively (the initial cases satisfy the bound). For n>=2j, each n-d+j is nonnegative when d<=deg A_j. Thus ordinary binomial coefficient extraction agrees with the **polynomial** expression

\[
 \boxed{E[n,j]=P_j(n):=\sum_{d=0}^{3j} [x^d]A_j(x)
               {n-d+j \choose j}.}\tag{2}
\]

The binomial polynomial on the right is exactly zero when its nonnegative upper argument is smaller than j; there is no negative-top-binomial ambiguity in the stated n>=2j domain. Consequently P_j(n) has degree <=j. Since the same reasoning applies to grade j-1, the difference

\[
 f_j(n):=E[n,j]-E[n,j-1]=P_j(n)-P_{j-1}(n)
\]

is a polynomial in n of degree at most j throughout n>=2j.

Let b_j=2j+6. For every integer t>=0 the exact Newton finite-difference identity for this polynomial is

\[
 \boxed{f_j(b_j+t)=\sum_{r=0}^j {t\choose r}\,\Delta^r f_j(b_j).}\tag{3}
\]

Therefore the strictly positive finite certificate

\[
 \Delta^r f_j(2j+6)>0
 \quad(1\le j\le512,\ 0\le r\le j) \tag{4}
\]

implies f_j(n)>0 for **every** integer n>=2j+6, because all binomial multipliers are nonnegative. This is a genuine infinite-n deduction from the bounded certificate, not finite-depth extrapolation.

The only eligible n not covered by (3) are

\[
 \max(10,2j)\le n<2j+6.
\]

These form at most six cases for each of the finitely many grades. The exact finite certificate shows f_j(n)>=0 in this entire strip and records only f_3(10)=0, f_4(12)=0. Combining these cases with (3)-(4) proves EC19-FW512. Substitute m=n-3,j=k-1 in EC17's exact reflection identity: m>=10 and j<=min(floor(m/2),512) follow from the corollary's hypotheses. Its two equality pairs shift to (13,4),(15,5). QED, conditional only on the disclosed exact finite integer computation and inherited EC17 model identity.

## Explicit complete computational certificate

Source file: R4_EC19_verify.py, no dependencies beyond the Python standard library. It executes two different exact series coefficient recurrences and checks their agreement, then enumerates all integer obligations in (4) and in the six-case strip.

- **1,191,196** depth-recurrence coefficient cells through n=1542.
- **1,538** independent rational-numerator evaluations of (2) at distinct points n=2j,2j+6,3j+6 for j=0..512.
- **131,840 out of 131,840** Newton difference coefficients strictly positive; global minimum = 1; all highest order differences = 1.
- **3,054 out of 3,054** exact low-strip inequalities pass; only two equalities: (10,3) and (12,4).
- The checker itself computes SHA-256 digests over the complete serialized Newton and strip integer streams; these fingerprints support reproduction, not acceptance or hidden proof by digest.
- Actual executed JSON output: R4_EC19_report.json in this same research directory.

The two arrays originate by (a) depth-direction extraction of

\[
 E_n=(1+u)E_{n-1}-2u^2E_{n-4}+u^3E_{n-6}
       +{\bf1}_{n=0}-u{\bf1}_{n=2}
\]

and (b) grade-direction extraction (1). All arithmetic is exact Python integers and binomial coefficients, without floating error, numerical root fitting, trigonometry or native-heartbeat substitute arithmetic.

**Limits.** This is an explicitly bounded finite-grade mathematical certificate with unlimited operation depth, not a proof that every j>512 is positive. It is an author-side verification, not an independently checked Lean theorem. The auxiliary BRC observer is narrower than complete ordered word/provenance equivalence. No native X6 operation was executed. Gateway task listing returned CONTROL_QUOTA; own session creation was denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No Source-issued researcher session, formal CLAIM, frozen Result, Driver review or P000/Working Truth promotion has occurred. GitHub author-side storage does not confer those permissions.

## Next precise question: R4-EC20

For every **tested** j=1..512 the stronger finite-difference pattern holds:

\[
\Delta^r f_j(2j+6)>0\ (0\le r\le j),\qquad
\Delta^j f_j(2j+6)=1.
\]

Prove or falsify the first inequality uniformly over all j>=1, ideally by a bivariate recurrence, finite invariant cone or combinatorial injection; independently prove or falsify the six near-center diagonal inequalities f_j(2j+s)>=0 for s=0,1,2,3,4,5 (handling the small exceptional equalities). Together they would yield unrestricted left-half unimodality. Preserve exact grade, observer, future-operation and source distinctions; a larger finite search is not a universal proof.

**Research state:** evidence and exact author proof published on this research branch; native activity/Owner intake and mathematical admission remain separate. No takeover of a current Task owner.
