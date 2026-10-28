# P11/AP endpoint dictionary and the unpaid terminal value

Author: EM-ANALYSIS-1E507F; RA-9C879FA5E6538D45DD9AE10F.
Date: 2026-10-28. Frozen direct paper scope; awaiting nonauthor review.
Classification: **REUSE / SCOPE_CLARIFICATION**, not a new mathematical
discovery, formal Task execution, Task acceptance, or all-m nonvanishing result.

## 1. Why the originally proposed unit was not executed

The proposed all-m nondegeneracy of the actual outer matrix at t=1 lies
inside the existing formal determinant task. It is also expressly required
in section 4, “Endpoint closure if positivity succeeds”, of the residual
Möbius–Bernstein coefficient task. A lightweight RA has no claim authority.
The live claim state is UNKNOWN here; historical READY text is not treated
as current claimability or absence of another owner. No such core execution,
claim, task amendment, coefficient-sign search or finite-m scan was made.

The owner instead authorized this bounded paper clarification: distinguish
the endpoint variables, record reversible algebra, and specify exactly which
future assertion would pay t=1. The prior endpoint author/review bytes remain
unchanged. Student/Parity is resting this round. Core98/fixed233 and m7
fixed-certificate NO_INVOKE boundaries are preserved.

The source model is external classical real polynomial/Cauchy algebra.
Heartbeat World remains the signed six-axis Cell torsor with no native plane;
there is no native-space or physical claim about any parameter below.

## 2. Exact sources and inherited data

All three source pins below are in awdawmip/enterprise-math at commit
`1a553d4d28a105230ecebd5a555dc8adbab8ee28`:

- `research_returns/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_RETURN_20260901.md`,
  blob `340a17c17156e633f0c107023507ceb5498a3763`, SHA256
  `8d189093d0381743c734698e0dd47b4977d799ade23f268047f067f74eb504ee`.
  Sections 3–4 give the full signed outer reduction; sections 6–7 give the
  first order, degree, and two-Cauchy-endpoint transform.
- `research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md`,
  blob `19a0bcf5eee3c6100443d66ed9a53d2979a5ace0`, SHA256
  `617b34abac20d524023933a09777b85aa4220e1962283586c1c2121d3031b28d`.
  Sections 5–6 already prove termwise endpoint division and the signed
  secant coefficient representation; section 11 explicitly leaves t=1 open.
- `research_tasks/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_20260902.md`,
  blob `290e507c7bf7a651b2f3608ced64ff09de47bed5`, SHA256
  `33acc5309db4e610e23e9dfdeb42b88a57c19c503197c5be7192fd9f8d0bc8ab`.
  Its endpoint requirement is scope evidence, not current execution authority.

The original outer task scope was separately read at the same commit:
`research_tasks/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DETERMINANT_20260901.md`,
blob `c2e573692fe13edb3c81df4b581759dd19033f5f`, SHA256
`f1e6be2f2ef1caff836f44f8da86912366833e271f38b08189ab1b7a31a296f6`.
Full connector bytes and Git blob hashes of the three new reads were checked.

Fix m>=2, n=m-1, b=m^2 and d=n(2m-3). Use the exact source polynomials

    tau_m(t)=t^n q_m(t),        deg tau_m=2n^2,     deg q_m=d,
    Bhat_m(x)=(1+x)^d q_m(x/(1+x)).                         (1)

The degree statements, nonzero q_m(0), and the crossing theorem are inherited
results, not proved again. In particular q_m is not the zero polynomial.
The transformed cofactor is exactly

    det Ltilde_x[hat(2m),hat(2m)]=x^n(1+x)^n Bhat_m(x).       (2)

The full outer relation, without any loss of signed layers, is

    tau_m(t)=kappa_m(t) det S_m(t),
    kappa_m(t)=product_(j=0)^n[w_j d_j(t)] / V_m^2,
    V_m=product_(k=1)^n k!,
    d_j(t)=integral_0^1 u^(mj)(1-u)^n(1-t u^b)^n du.          (3)

Here d_j(1)>0 and every w_j=(-1)^j binom(n,j) is nonzero. Thus kappa_m is
nonzero at 1, and every entry of S_m is rational and analytic near 1. No
sign of kappa_m, q_m(1), or det S_m(1) is being silently replaced by positivity.

## 3. The three distinct endpoints

The rational coordinate relation is t=x/(1+x), x=t/(1-t). On the physical
parameter interval of this external problem, 0<=t<1 corresponds to x>=0.
Outside it, the identities remain polynomial/rational identities only.

| Original parameter | Möbius coordinate | Inherited or exact meaning |
| --- | --- | --- |
| t=0 | x=0 | Initial Cauchy layer; ord tau=n and Bhat(0)=q(0)!=0. |
| t=infinity | x=-1 | Highest Cauchy layer after reversing/scaling; controls the leading t coefficient, not tau(1). |
| t=1 | x=infinity | Actual beta-kernel endpoint; its value is the nominal top coefficient of Bhat. |

To verify the middle row, expand q(t)=sum_(j=0)^d a_j t^j in (1):

    Bhat(x)=sum_(j=0)^d a_j x^j(1+x)^(d-j),
    Bhat(-1)=(-1)^d a_d != 0.                              (4)

The source's terminal-layer degree loss is equivalently

    ord_(u=0) [u^(n(2m-1)) tau_m(1/u)] = n,

because deg tau_m=n(2m-1)-n=2n^2. It concerns t=infinity. This is the
second Cauchy endpoint in the inherited degree calculation. The finite
admissible endpoint t=1 is a different point.

For completeness, the actual t=1 matrix entry has the elementary exact form

    H_1(i,j)=integral_0^1 u^(i+mj)(1-u^b)^n du
            =(1/b) Beta((i+mj+1)/b,n+1)
            =n! b^n / product_(s=0)^n(i+mj+1+bs).           (5)

Indeed v=u^b gives the beta integral and its usual integer second-argument
product. Put a=i+mj+1. The terminal unweighted Cauchy layer has entry
1/(a+bn). The ratio of (5) to this entry is

    n! b^n / product_(s=0)^(n-1)(a+bs),

which is strictly decreasing for a>0. Thus these endpoint matrices are not
the same matrix up to a common scalar. This statement does not rule out
some other proved relation; it only rules out that literal substitution.
Positive entries in (5) do not determine the signed gauge cofactor.

## 4. Complete reversible jet dictionary at t=1

For this section q is any nonzero polynomial of degree at most d and
B(x)=(1+x)^d q(x/(1+x)); the AP case is an immediate substitution.
Always retain the nominal length d+1, including any zero top coefficients.
Write

    b_j=[x^j]B(x),     J_r=q^(r)(1)/r!,       0<=j,r<=d.

Then for 0<=k<=d,

    b_(d-k)=sum_(r=0)^k (-1)^r binom(d-r,k-r) J_r,          (6)
    J_k=sum_(r=0)^k (-1)^r binom(d-r,k-r) b_(d-r).          (7)

Proof of (6). Reversing at infinity gives the polynomial identity

    y^d B(1/y)=(1+y)^d q(1/(1+y))
               =sum_(r=0)^d (-1)^r J_r y^r(1+y)^(d-r).

Read its coefficient of y^k. For (7), use the inverse identity

    q(1+z)=sum_(r=0)^d (-1)^r b_(d-r) z^r(1+z)^(d-r)

and read z^k. Both are finite identities; no limiting sign or convergence
assumption is needed. This retains all endpoint jets, rather than dropping
them to a single positive mass or a scalar fit.

If r=ord_(t=1)q(t), the first nonzero reversed coefficient is

    b_(d-r)=(-1)^r J_r !=0,
    deg B=d-r.                                             (8)

Conversely, that degree determines the same r. In particular, substituting
the actual AP q_m and using t^n and kappa_m(t) nonzero near 1 yields

    [x^d]Bhat_m=q_m(1)=tau_m(1)=kappa_m(1)det S_m(1),        (9)
    ord_(t=1) det S_m(t)=d-deg Bhat_m.                       (10)

Equation (10) uses order zero for a nonzero value. It is an exact
restatement of the unpaid endpoint obligation, not a proof that the order
is zero and not a smaller sign problem. The known degree of q_m does not
imply degree d of Bhat_m: a Möbius transform can lose top degree precisely
when q_m(1)=0.

## 5. What does and does not pay the endpoint

The following are equivalent for each exact m:

    det S_m(1)!=0;
    tau_m(1)!=0;
    [x^d]Bhat_m!=0;
    deg Bhat_m=d.                                           (11)

If a future correctly authorized proof establishes strict positivity of
the complete nominal coefficient row [x^k]Bhat_m for 0<=k<=d, its k=d
case together with (9) pays the endpoint. This gives the separate exact
endpoint implication requested by the taskbook. There is no further
independent endpoint conjecture after that complete row is proved.

In contrast, positivity of Bhat_m(x) for every finite x>=0, or positivity
of all coefficients only up to its unknown actual degree, is insufficient.
Neither statement determines [x^d]Bhat_m.

A purely polynomial logical witness makes the distinction exact. For any
n>=1 and d=n(2n-1), let

    q_star(t)=(1-t)(1+t)^(d-1),
    tau_star(t)=t^n q_star(t),
    B_star(x)=(1+2x)^(d-1).                                 (12)

Then q_star(0)=1, deg q_star=d, deg tau_star=2n^2,
B_star(-1)=(-1)^(d-1)!=0, and B_star has strictly positive coefficients
through its actual degree d-1 and is positive at every finite x>=0.
Nevertheless tau_star(1)=0 and its order there is exactly one. For d=1
the same statements hold with B_star=1. This witness is not an actual AP
cofactor, not a matrix counterexample, and not an HCM0 counterexample.
It only disproves the logical inference from these generic endpoint/degree
facts to a nonzero value at t=1. No AP source result is refuted.

## 6. Deduplication, reuse and remaining action

The exact source already provides (1)–(3), first/terminal Cauchy data, and
a stronger signed secant representation. Its later section 11 explicitly
does not claim t=1 closure. This note does not replace or improve those
results. Equations (4)–(12) extract elementary consequences into a scoped
endpoint dictionary. The jet transform is standard finite polynomial
algebra; no claim that it is absent elsewhere or a new tool family is made.

Tool-coverage lookup was completed before this composition. Resolution:
COMPOSE_APPLIED to the existing Cauchy/cofactor/Möbius interfaces plus
ordinary Taylor coefficients and the beta integral. Lexical registry hits
do not constitute invocation. Zero scientific programs, finite AP cases,
coefficient scans, original checker runs or formal-task searches were executed.

The actual all-m endpoint remains OPEN. Its continuation requires the
existing task lineage and current exact execution authority, preserving
all prior accepted negative boundaries. The appropriate next action from
this direct delegation is nonauthor paper review and Source capture of
this clarification; no same-line constant variant or sign search follows
automatically. In the portfolio ledger this is source/routing clarification,
not a new P11 theorem or a fresh research-unit success count.

Review focus: variable endpoints; nominal versus actual degree; both jet
transform signs; analytic nonzero factor in (3); no positivity assumption
on the signed outer matrix; and the strictly non-AP scope of (12).
