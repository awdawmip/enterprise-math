# D25: a nonzero transverse Dixon digit and a safe parameter-derivative interface

The 15 newly preserved source messages are now at enterprise-math@9bba3d56193d4ba55bfc1a42cc38f2d2dbf416ee under research_notes/directed_recovery/20260926_13C1B7/sources (publication/readback reported by root; this agent retains its own local exact message-byte checks).

Status: AUTHOR_LOCAL_PROVED_ALGEBRA / FINITE_COUNTEREXAMPLE_TO_A_SHORTCUT / UNREVIEWED / NOT_ADMITTED.
This is a directed-research contribution within root EM-DIRECT-13C1B7 / RA-BC9CF141D000E1FE25AF22EA after its successful registration (Source 029e62a1a31a0b9e65e7e915db724efdd8311836). This subagent shares root context and does not claim independent review. It does not use CM24 task ownership to research LIFT.

## Question and useful result

The new hourly D25 frontier asks for one- and two-parameter derivatives of terminating families connecting the LOW/Beta observer to the already closed B11 moment. Before differentiating that B11 simplification, one must retain its normal parameter direction.

We prove an all-m algebraic formula for that normal derivative, and exhibit an exact p=13 witness showing that the mod-p Dixon replacement loses a nonzero next digit. Thus “differentiate/use the closed B11 value as though it were an equality through p²” is an invalid shortcut. This does not refute B11 or LIFT. It identifies a concrete correction that any successful LOW-to-B11 transport must preserve or explicitly cancel.

## Exact family

For m>=1 define the finite rational function
\[
 F_m(a,d)=\sum_{j=0}^{m}\frac{(-m)_j}{(d)_j}\frac{a}{a+j}.
\]
Work away from displayed poles; identities are rational-function identities and extend at removable singularities. This is the terminating family
\[
{}_3F_2(-m,1,a;d,a+1;1).
\]

On the contiguous-Dixon line d=m+a+1, the already-used finite identity has the rational form
\[
 C_m(a):=F_m(a,m+a+1)
 =1+a\sum_{r=0}^{m-1}\left(\frac1{a+2r+2}-\frac1{a+2r+1}\right).
 \tag{1}
\]
This is the parameter version of B11's exact Dixon node; it is not a new proof of the B11 mod-p congruence.

For completeness its parameter domain can be checked without analytic continuation:
put \(A_{m,j}=(-m)_j/(a+m+1)_j\). Direct cancellation gives
\[
 A_{m,j}-A_{m-1,j}
 =A_{m,j}\frac{j(a+j)}{m(a+m)}
\]
with \(A_{m-1,m}=0\). An elementary finite telescoping certificate (so no external summation theorem is needed) is
\[
 T_j=\frac{(j+a+m)A_{m,j}[m-j(a+2m)]}{(a+2m-1)(a+2m)}.
\]
Direct multiplication by A_{m,j+1}/A_{m,j}=(j-m)/(j+a+m+1) verifies T_{j+1}-T_j=j A_{m,j}. Since T_{m+1}=0 and T_0=m(a+m)/[(a+2m-1)(a+2m)], summation yields
\[
 \sum_{j=0}^m jA_{m,j}
 =-\frac{m(a+m)}{(a+2m-1)(a+2m)}.
\]
Consequently \(C_m-C_{m-1}=a[(a+2m)^{-1}-(a+2m-1)^{-1}]\), and \(C_0=1\), proving (1) as an exact finite rational identity. No prime scan or p-adic approximation enters this step.

## Tangent and normal derivatives are different

Differentiate (1) along its line, not at fixed d:
\[
 C_m'(a)=\partial_aF_m(a,d)+\partial_dF_m(a,d)
 \quad (d=m+a+1).
\]
At fixed d, direct finite differentiation gives
\[
 \partial_aF_m(a,d)
 =\sum_{j=1}^{m}\frac{(-m)_j}{(d)_j}\frac{j}{(a+j)^2}.
\]
Therefore the normal derivative is exactly
\[
 \boxed{
 N_m(a):=\partial_dF_m(a,m+a+1)
 =C_m'(a)-
 \sum_{j=1}^{m}\frac{(-m)_j}{(m+a+1)_j}\frac{j}{(a+j)^2}.
 }\tag{2}
\]
Here \(C_m'\) is completely explicit:
\[
 C_m'(a)=\sum_{r=0}^{m-1}
 \left[
 \frac1{a+2r+2}-\frac1{a+2r+1}
 +a\left(-\frac1{(a+2r+2)^2}
         +\frac1{(a+2r+1)^2}\right)
 \right].
\]
The sole unevaluated piece in (2) is a finite **double-pole moment**. A closed value of \(C_m\), or its derivative tangent to the Dixon line, does not delete that moment.

An equivalent direct normal formula is
\[
 N_m(a)=-\sum_{j=1}^{m}
 \frac{(-m)_j}{(m+a+1)_j}\frac{a}{a+j}
 \sum_{\ell=0}^{j-1}\frac1{m+a+1+\ell}.
 \tag{3}
\]
Equations (2) and (3) describe the same port; the checker compares them exactly.

## The parameter offset in B11 is precisely non-tangent

For p=6m+1 prime set \(a_0=-1/3\), \(d_0=m+2/3\). The original B11 sum is
\[
 S_m=F_m(a_0,3m+1)=F_m(a_0,d_0+p/3),
\]
whereas its closed Dixon replacement is \(S_m^*=C_m(a_0)\).

All denominators in this finite family and its first two derivatives are p-units: j<=m, the d factors are (3m+2+3l)/3 with maximum 6m-1=p-2, and a+j=(3j-1)/3 never vanishes modp. Thus Taylor expansion in the normal direction is legitimate:
\[
 \boxed{
 S_m-S_m^*\equiv\frac p3N_m(-1/3)\pmod{p^2},
 \qquad
 \frac{S_m-S_m^*}{p}\equiv\frac13N_m(-1/3)\pmod p.
 }\tag{4}
\]
The B11 proof correctly retained only mod-p equality. Equation (4) is the additional datum required for a next-digit transport.

This is already visible at an actual target prime, p=13 (m=2):
\[
 S_2=\frac{159}{140},\qquad
 S_2^*=\frac{587}{440},\qquad
 \frac{S_2-S_2^*}{13}=-\frac{47}{3080}\equiv8\pmod{13}.
\]
Equivalently,
\[
 S_2-S_2^*\equiv104=13\cdot8\not\equiv0\pmod{169}.
\]
The direct normal derivative is \(N_2(-1/3)\equiv11\pmod{13}\), so (4) gives \(11/3=8\pmod{13}\), independently agreeing with the exact rational difference.

Hence the conjectural shortcut \(S_m\equiv S_m^*\pmod{p^2}\) is refuted. The valid all-m identity (2) supplies the repair port rather than discarding the residual.

## Relation to LOW, and limits

Input portable messages:
- new hourly fb9aba8a-6fb9-411b-920b-9bb376d16cd5: complete L_n/M_n/J_r and two-band endpoint definition;
- new hourly f48dfe9d-4144-4e56-9948-00a764fb3035: LOW, IX and IZ;
- archived B11 at enterprise-math@95caf384ffb7248deb8c519a65c5bffef3c002e4, blob 641e5584bc258786bb898c938440a7a34b6e244e.

No equality between the remaining LOW residual and N_m alone has been proved here. That would be an unsupported promotion. The result is a rigorous constraint on any next LOW-to-B11 derivative map: distinguish the tangent Dixon derivative from the normal derivative (2), then demonstrate cancellation or explicitly carry the double-pole moment. Do not re-prove B11, reopen UR, or assert endpoint closure from finite agreement.

BRC typing:
population = finite indices j=0..m;
retained carrier = exact rational coefficients, normal/tangent parameter labels, and p-adic precision through the divided p digit;
unsafe quotient = replace a normal displacement by its mod-p Dixon value/tangent-only derivative;
separation witness = p=13 above;
safe repair = N_m or its equivalent explicit double-pole moment;
allowed future operation = differentiation/Taylor evaluation through p², with source parameter direction preserved.

## Executed checks

1. prepared_d25_beta_parameter_checker.py:
   203 exact parameter-jet/Beta basis checks for m=1..7;
   independent positive-parameter endpoint reconstruction and LOW residual for p=7,13,19,31,37,43,61,67;
   zero failures. This only verifies finite cases of the preceding author formulas.

2. d25_dixon_normal_defect.py:
   32 exact rational identities across m=1..8 and a=-1/3,2/7,3/2,2;
   equations (2)-(4) checked at the same 8 primes;
   explicit p=13 counterexample above reproduced.
   The proof of (2) and (4) is the finite algebra/Taylor argument, not these scans.

Files: PREPARED_CHECKER_RESULT.json and D25_DIXON_NORMAL_DEFECT_RESULT.json contain full exact evidence. LIFT/JT2 remains OPEN / NOT_ADMITTED. No remote write or operational task-state change was made by this subagent.

## Reuse disposition

REUSE_APPLIED (mathematical interface): reuse the existing finite terminating-hypergeometric carrier F_m and B11's contiguous-Dixon specialization, together with the project's typed BRC rule that parameter direction, valuation and provenance must survive a quotient. Equations (2)-(4) extend this existing local family by retaining its normal derivative; they are not a new general toolbox, and no method novelty is claimed.

Exact scientific sources actually read are the archived B11 source blob 641e5584bc258786bb898c938440a7a34b6e244e and the two complete portable hourly messages identified above. The current global BRC priority/use policy was read. This agent did not perform an exact toolbox-registry lookup and does not claim a registry match or execution of a pre-existing packaged checker. The new local scripts are transparent validation artifacts for these equations, not registrations of a new tool family.

The next mathematical action is to write the LOW Beta-to-B11 transport as a parameter-direction map and track the coefficient of this normal derivative. Prove that coefficient cancels against the remaining low/high jet terms, or retain the explicit double-pole moment as part of the final adjoint defect. A formula using only the tangent C'_m is now known to be insufficient for the original B11 normal displacement.


