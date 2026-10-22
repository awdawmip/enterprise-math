# 数论／CRT补卷：公式、前提、修正及证据边界

固定 Source：`56f5938da3f707c1d9db1b39afde124eac4634e3`；2026-10-01至2026-10-22的既有文献采收。14个文献单元不代表14个新定理；没有新证明、数学票、科学程序执行或Tool注册。

与既有 number57 卷按精确path、member SHA及科学标题去重：复用既有generic CRT与ordinary QR结果，补取其后应用。来源是共享workspace中与固定tree blob一致的真实字节；不虚构本轮Connector调用。

机器可读：[supplement_number_theory.json](supplement_number_theory.json)；逐路径/成员：[supplement_number_theory_coverage.json](supplement_number_theory_coverage.json)。

Gaussian wedge全Newton证书及J1r61–64全ZIP未在所读Source提供；adaptive第三congruence只有短checkpoint。对应作者claim和proof gaps逐条保留，不能当独立已核验定理。

## NT-SUP-CRT-AFFINE

仿射 shifted-quadratic 共用集合与付费 cyclic rank

同一固定仿射子类可共享二次预像集合，行差异是已知循环平移；不与普通QR集合或Hart非线性候选混同。

状态：`EXISTING_DIRECTED_NONBLIND_NONAUTHOR_PAPER_PASS_NOT_NATIVE_ACCEPTANCE`。

原贡献与归属：历史Root在delegated draft容量错误后写本稿；original CRT owner EM-DIRECT-FB83AB保留；本轮curator无数学贡献。

Source：[research_notes/ROOT_CRT_AFFINE_QUADRATIC_AND_FINAL_CONTROL_PATH_20261014_FBF223.json](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/ROOT_CRT_AFFINE_QUADRATIC_AND_FINAL_CONTROL_PATH_20261014_FBF223.json)。

原capsule成员：`/workspace/em-owner-resume-20261011/new-round-20261011/CRT_SHIFTED_QUADRATIC_ROW_TRANSLATION_AND_RANK_20261014.md`；此成员路径是归档标签，不能伪装成独立GitHub路径。

- x=a+c+ut; s_a=(a+c)/u,D=4N/u²; V_D={z:χ_v(z²−D)≥0}; T_a=V_D−s_a.
- 物理模坐标b=x modv有W_N=uV_D；域乘法后取canonical residue一般不保持整数排序。
- I_D(z)=(1+χ_v(z²−D)+1_(z²=D))/2；D≠0时|V_D|=(v+χ_v(D))/2；D=0时|V_D|=v。
- R_D(j)=#{z∈V_D:0≤z<j}; 半开[ell,h),n=h−ell,b=(ell+s_a) modv，count=R_D(b+n)−R_D(b)若b+n≤v，否则R_D(v)−R_D(b)+R_D(b+n−v)。完整period另计。

前提：固定整数N,c,u，v已证明为odd prime，gcd(u,v)=1；候选实际为x=a+c+ut，保留每行合法区间及carry。

边界：不覆盖general coupled predicates、任意行变系数二次式、composite Jacobi替代、Hart ceil√(4Nk)字典。；普通QR的旧复杂度不能直接抄作该新predicate的成本；prime/input reduction/inverse/扫描/排序/保存均付费。；与number57 NT-CRT-CHARACTER-STREAM为前驱依赖，非同一定理；仅paper specification，不注册新Tool。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# CRT shifted-quadratic rows: one translated survivor set, with paid rank queries

2026-10-14. One bounded paper unit, authored by Root after the delegated
drafting turn returned a model-capacity error. The original CRT mathematical
owner EM-DIRECT-FB83AB is preserved; no new owner, Task, claim, run, sample,
prime test, old checker, or scientific execution is created. Separate
source-exposed nonauthor review is requested. No external novelty claim.

## 1. Exact new interface and dependencies

The corrected existing prime-QR adapter accepts the complete ordinary QR set
independently of the U rows. It explicitly does not establish an interface
for a shifted-square survivor or general coupled predicate. Its cyclic-rank
formulas, empty-U cost correction, prime requirement and counterexamples are
completed inputs, not repeated work here. See
[corrected V2 contract](/workspace/em-owner-resume-20261011/new-round-20261011/crt-rank-only-interface-20261013/correction-v2/PRIME_QR_LEGENDRE_STREAM_RANK_SPACE_TRADEOFF_CORRECTED_V2.md).

This note handles one independently specified subclass. Fix integers N,c,u,
a proved odd prime v, and gcd(u,v)=1. For a retained row a, the actual
candidate coordinate in this subclass is

    x = a+c+u*t,             t an integer in its retained legal row interval.

The public modular survivor predicate is: x^2-4N is a quadratic residue
modulo v, with zero retained. This is a necessary modular square filter;
it is not a claim of an integer-square hit or a proper factor.

Let chi denote the Legendre symbol, taking ordinary integer values -1,0,1.
All divisions in definitions below are in F_v. Define

    s_a = (a+c)/u,   D = 4N/u^2,
    V_D = {z in F_v : chi(z^2-D) >= 0}.

The affine x assumption is part of the contract. It is not inferred for
Hart's ceil(sqrt(4Nk)) or for a generic coupled delta(a,b).

## 2. Translation theorem

For every row a and every integer t,

    x^2-4N = u^2((t+s_a)^2-D) in F_v.

Since u is nonzero, u^2 is a nonzero square. Multiplicativity of chi,
including its zero value, gives

    chi(x^2-4N) = chi((t+s_a)^2-D).

Consequently the legal survivor residues of t in row a are exactly

    T_a = V_D - s_a.                                      (1)

Thus a common base set does exist in this particular shifted-quadratic
subclass. The row dependence is a known cyclic translation. It would be
incorrect to infer from the old adapter's inapplicability that every
shifted-square predicate forbids a common set. It is equally incorrect to
replace V_D by the ordinary QR set: it is a quadratic preimage, and needs
its own paid indicator and rank construction.

In the physical residue coordinate b=x mod v, the same predicate has the
common row-independent set

    W_N={b in F_v: chi(b^2-4N)>=0}=u*V_D.                 (2)

Equation (2) follows by putting b=u*z, and using chi(u^2)=1. Scaling by u
is a permutation of field residues, but not in general a permutation
preserving their integer sorted order. A stored or streamed rank table
for one set cannot be silently treated as the sorted table for the other.
The selected coordinate and its actual row carry/cut must be retained.

## 3. Exact full-period count, including zeros

For q_z=z^2-D, the zero-inclusive survivor indicator as an ordinary integer
is

    I_D(z)=(1+chi(q_z)+1_{q_z=0})/2.                    (3)

Its three cases are 0 for a nonresidue, 1 for a nonzero residue, and 1 for
zero. This is an integer count, not a field sum interpreted as a count.

If D!=0, count pairs (z,y) with y^2=z^2-D. The map

    r=z-y, h=z+y,       r*h=D

is a bijection with v-1 pairs (r,h) in (F_v^*)^2 satisfying h=D/r,
since 2 is invertible. On the other hand the number of pairs is
sum_z(1+chi(z^2-D)). Therefore

    sum_z chi(z^2-D)=-1.

The number of zeros is 1+chi(D). Summing (3) yields the exact integer count

    |V_D|=(v+chi(D))/2,              D!=0.              (4)

If D=0, every z^2 is a square or zero, so V_D=F_v and |V_D|=v. One must
not substitute chi(0)=0 into the nonzero-D formula. All rows have the same
full-period count by (1), even though a partial row interval can have a
different count. These are all-prime identities under the stated inputs,
not prime/sample evaluations.

## 4. Exact cyclic rank contract

Represent field residues by 0,...,v-1 and let

    R_D(j)=#{z in V_D: 0<=z<j},    0<=j<=v.

For a row interval [ell,h) with 0<=ell<=h<=v, put n=h-ell and
b=(ell+s_a) mod v, in canonical integer representatives. Then its exact
survivor count is

    R_D(b+n)-R_D(b),                       b+n<=v;
    R_D(v)-R_D(b)+R_D(b+n-v),              b+n>v.        (5)

The formula rotates the interval by s_a and splits it only at the actual
cyclic wrap. It handles empty intervals and a full period without changing
endpoint conventions. A longer integer interval is decomposed into its
complete periods plus a remainder before using (5); every complete period
contributes (4), or v when D=0.

This is a row-specific rank contract, not permission to discard the row.
For a CRT-prefix application retain the original row a, c,u,v,N, the
selected coordinate convention, s_a, and the exact legal interval/carry
that the prefix induces. Aggregate cardinalities or independent marginals
do not recover those translated cuts. Conversely, in physical b coordinates
one can apply the already proved general CRT product-set rank identities
to a legitimately constructed complete W_N, while retaining their original
carry and finite-prefix rules. No new complete-prefix cost theorem is
asserted by changing notation.

## 5. Positive costs and streaming fallback

The prime certificate, reading/reducing N,c,u,a, computing u inverse and D,
all field arithmetic, zero comparisons, interval endpoints, counters,
sorting, memory and evidence preservation have costs. They are not supplied
for free by (1). In particular large N has its actual input/reduction cost;
the bit width of v alone is not a bound on the cost of reading N.

A direct honest implementation scans z=0,...,v-1 once for a shared V_D
table, evaluates (3), and accumulates R_D. It costs v quadratic-predicate
evaluations plus setup and rank bookkeeping, and a full prefix table uses
v+1 integer counters. For a previously proved prime, Euler exponentiation
is one possible Legendre evaluator, with positive modular-operation costs;
this note does not make a prime proof or exponentiation free.

Alternatively, collect the finitely many requested R_D cutpoints from (5),
sort them, scan the same shared predicate stream, and retain only requested
prefix counts. Pay for every row setup/shift, cut sorting, predicate read,
counter and repeated scan if queries arrive later. The common base can
avoid an unnecessary independent full scan per row; this is a structural
sharing opportunity, not a measured or asymptotic advantage over every
alternative. If there are no queries, no stream need be constructed; any
setup actually performed is still paid. The special D=0 branch can use its
proved all-survive formula, with its own setup and query costs retained.

No numerical scan, new N, old certificate, checker, solver or benchmark was
executed. A future implementation needs a typed cost contract and review;
the old ordinary-QR cost formula cannot simply be copied as measured cost
of this different predicate.

## 6. Exact boundary and next mathematical obligation

The result applies when the actual public predicate is exactly the affine
shifted square in section 1, with one fixed N,c,u,v and a proved odd prime.
It does not establish a common base for arbitrary row-dependent quadratic
coefficients, arbitrary delta(a,b), additional coupled filters, composite
Jacobi surrogates, or Hart's nonlinear root/candidate map. An actual
application must prove its coordinate dictionary first.

The completed accepted CRT child remains completed; no child or parent is
reopened here. This paper advances only the newly identified applicability
interface. General factorization gain, full parent objectives, actual
runtime and formal Native acceptance remain unproved. The next usable
step is to match a real saved public sieve predicate to this exact affine
contract, including its carry descriptor and all costs, rather than call
the ordinary-QR adapter on an unproved replacement set.

````

</details>

## NT-SUP-CRT-DICTIONARY

真实保存 shifted-square sieve 的坐标翻倍、半开前缀及两种carry字典

保存代码的实际(c0+k)²−N筛选精确匹配仿射接口，必须翻倍候选坐标；新的rank描述不代表旧代码已实现它。

状态：`EXISTING_DIRECTED_NONBLIND_NONAUTHOR_PAPER_PASS_NOT_NATIVE_ACCEPTANCE`。

原贡献与归属：原local helper native identity UNKNOWN，DIRECTED_NONBLIND；original owner EM-DIRECT-FB83AB保留。

Source：[research_notes/OWNER_PARALLEL_CM24_CRT_AND_MCP_REPAIR_20261014_FBF223.json](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/OWNER_PARALLEL_CM24_CRT_AND_MCP_REPAIR_20261014_FBF223.json)。

原capsule成员：`new-mathematics/CRT_ACTUAL_SAVED_SIEVE_DICTIONARY_20261014.md`；此成员路径是归档标签，不能伪装成独立GitHub路径。

- c0=ceil√N，B_v={b:(c0+b)²−N为零inclusive square modv}；t=((b−a)/u) modv,k=a+ut为A×B_v与period survivors的双射。
- x=2(c0+k),a_new=2a,c_new=2c0,u_new=2u；x²−4N=4((c0+k)²−N)，故D=N/u²，s_a=(a+c0)/u，|B_v|=(v+χ_v(N))/2。
- 整数0≤h≤uv，n_a(h)=min(v,max(0,1+floor((h−1−a)/u)))；这是k<h的精确行长，inclusive K需h=K+1。
- L=qM+h ⇒ C(L)=q|A||B_v|+Σ_a translated_row_rank_a(h)。
- ω_a=v(v^−1 mod u)a modM,ν_b=u(u^−1 modv)b modM；(ω+ν) modM=k，k<h iff ω+ν∈[0,h)∪[M,M+h)。

前提：N odd，固定c0；old squarefree modulus u及完整canonical A，old selected primes皆coprime N；下一v为proved odd prime，明确gcd(u,v)=gcd(N,v)=1；u=1虚singleton单列，无inverse mod1。

边界：canonical row、local offset b、加权ν、physical x modv是不同排序坐标；不可将translated cuts直接传旧self.V。；保留实际保存代码身份a5d4a5…作为原文静态阅读报告，本轮未重读/执行该科学代码。；not integer-square/proper-factor certification；额外coupling、prime powers、composite second group与Hart不由该最小stage字典覆盖。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Exact dictionary for one saved shifted-square CRT sieve

2026-10-14. One directed NONBLIND paper application of the reviewed
shifted-quadratic row contract. Original mathematical owner
EM-DIRECT-FB83AB and every existing formal owner are preserved. This local
helper has UNKNOWN native identity. No old program, sample, checker or
benchmark was executed; no new scientific script, Task, claim, Run, branch
or remote mutation was created. The accepted complete-list CRT child and
the completed ordinary-QR adapter remain completed inputs.

**Result.** The saved `QRWheelIndex` local predicate and one-prime
`_partial_crt` extension fit the new contract exactly, after a necessary
doubling of the candidate coordinate. The dictionary preserves the
half-open offset prefix and both kinds of CRT carry. It does not establish
a faster implementation or integer-square/factor certification.

## 1. Selected saved code, without an inferred solver model

The selected source is
[implicit_crt_qr_index.py](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py).
Its current local SHA256 is
`a5d4a53431d020b40787197aa68ccf3aa1703708b7716c6c4ebeba4318c37820`,
matching the previously frozen entry in
[IMPLICIT_CRT_INTERFACE_FROZEN_PINS.json](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/IMPLICIT_CRT_INTERFACE_FROZEN_PINS.json).
This is verification of saved bytes, not a fresh remote Source read.

The relevant actual definitions are:

- [Lines24–30](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py:24):
  `_local_allowed(N,c,p)` marks every square `y*y % p`, including zero,
  and returns precisely those offset residues `t` for which
  `((c+t)**2-N) % p` is marked.
- [Lines50–65](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py:50):
  the constructor validates distinct odd primes and coprimality to N,
  computes `c=ceil(sqrt(N))` once, and constructs these local predicates.
- [Lines33–44](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py:33):
  one incremental CRT step is exactly
  `r + modulus * (((a-r)*inverse(modulus,p)) % p)`.
- [Lines96–114](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py:96):
  count queries use `[0,length)`, split ordinary weighted sums at M,
  and use `divmod(length,M)` for complete periods.

The saved formal return independently fixes this same public predicate
and endpoint convention at
[lines19–29](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/formal-author-unit-20261013/QR_CRT_PREFIX_INDEX_PAID_COST_RESEARCH_RETURN.md:19).
Its incremental CRT and wrapped-sum rules appear at
[lines33–56](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/formal-author-unit-20261013/QR_CRT_PREFIX_INDEX_PAID_COST_RESEARCH_RETURN.md:33).
Their proof and old checks are consumed, not repeated as new results.

Write `c0` for this saved integer `ceil(sqrt(N))`. It is fixed for the
whole instance. The saved candidate is `c0+k` for an offset k; it is not
Hart's candidate obtained by recomputing a ceiling root as a function of
another search index.

## 2. One actual incremental CRT stage

Select one step of `_partial_crt`. Let u be the old `modulus`, A its
complete list `residues` in `[0,u)`, and v the next proved odd prime p.
Since the code uses distinct primes, gcd(u,v)=1; u=1 is allowed. Define

    B_v={b in [0,v): (c0+b)^2-N is a square modulo v, including zero}.

This is exactly the saved `allowed` list for v, not the ordinary set of
squares modulo v. In the following dictionary the old residue `r` is a,
and the newly chosen local residue named `a` in the code is b. The code
sets

    t=((b-a)*u^(-1)) mod v, chosen in {0,...,v-1},
    k=a+u*t.                                                (1)

For 0<=a<u, this gives 0<=k<uv, k=a modulo u, and k=b modulo v.
Conversely those two congruences determine exactly this t. Thus the step
is a bijection between A x B_v and all survivors of the old group plus
this one prime, in one period M=uv. Earlier local predicates depend only
on k modulo their primes and are preserved by k=a modulo u.

This is the selected minimal saved application. The new paper supplies a
rank description for the same one-prime extension; the old implementation
does not already implement that new rank description. No assumption is
made that the constructor's heuristic group partition always has a prime
as an entire second group. A composite group must be extended prime by
prime, or keep its separately proved composite-group interface.

## 3. Necessary coordinate doubling and the common translated set

The reviewed new paper uses `x^2-4N`, whereas the saved code uses
`(c0+k)^2-N`. Keep the same integer N and set

    x=2(c0+k),  a_new=2a,  c_new=2c0,  u_new=2u.

Then (1) gives the exact integer affine coordinate

    x=a_new+c_new+u_new*t,
    x^2-4N=4*((c0+k)^2-N).                                  (2)

Because v is odd,4 is a nonzero square. Both residuals are simultaneously
zero, a nonzero square, or a nonsquare modulo v. Also gcd(2u,v)=1.
Consequently all hypotheses needed for the new translation contract hold.

Its two field parameters become

    s_a=(a_new+c_new)/u_new=(a+c0)/u,
    D=4N/u_new^2=N/u^2.                                     (3)

Division in (3) is in F_v. There is no requirement that a field shift
s_a be represented by an unreduced integer quotient. With canonical
residue representatives define

    V_D={z in F_v: chi(z^2-D)>=0}.

For every t,

    (c0+a+u*t)^2-N=u^2*((t+s_a)^2-D) in F_v.

Hence the actual legal row residues are precisely

    T_a={t in [0,v): t+s_a mod v belongs to V_D}
       =V_D-s_a.                                          (4)

This also follows directly from the code's local b-coordinate:
`b=a+u*t mod v` lies in B_v iff (4) holds. Thus this common base set is
proved for an actual saved public predicate. It was not obtained by
substituting an ordinary QR set for a different predicate.

The saved coprime condition gcd(N,v)=1 implies D!=0. Its existing exact
cardinality therefore agrees with the new contract:

    |B_v|=|V_D|=(v+chi(N))/2,

since D differs from N by a nonzero square factor. The new contract's
D=0 all-survive branch is not needed to extend the saved coprime model.

The doubling is a dictionary on the retained candidates, not permission
to count every integer x in a doubled interval. Only the even coordinates
x=2(c0+k) are represented. Retain k and the original offset prefix.

## 4. Exact half-open prefix and translated carry

First let h be an integer prefix length with 0<=h<=M=uv in one period.
Fix a in A.
The exact saved condition on its canonical row is

    0<=k=a+u*t<h,  0<=t<v.

It is equivalent to `0<=t<n_a(h)`, where

    n_a(h)=min(v,max(0,1+floor((h-1-a)/u))).                 (5)

This is the clipped integer ceiling of `(h-a)/u`. Formula (5) is valid
also at h=0: each row is empty. At h=M each row has v candidate positions.
No equality at k=h is counted. The old formal inclusive rank at endpoint
K uses h=K+1 (and zero for K<0); this is the explicit conversion, not a
changed endpoint convention.

Let

    R_D(j)=#{z in V_D: 0<=z<j}, 0<=j<=v,
    b_a=s_a mod v in {0,...,v-1}, n=n_a(h).

By (4), this row contributes exactly

    R_D(b_a+n)-R_D(b_a),                    b_a+n<=v;
    R_D(v)-R_D(b_a)+R_D(b_a+n-v),            b_a+n>v.        (6)

The first interval of t begins at0 because a was kept canonical in
`[0,u)`. The only cut in (6) is the genuine wrap of `t+s_a` at v.
The formula counts both the empty row and a complete v-row correctly.

The total one-period count is the sum of (6) over a in A. For an arbitrary
nonnegative integer offset prefix length L=qM+h, with integers q,h and
0<=h<M, periodicity gives

    C(L)=q*|A|*|B_v|+sum_(a in A) row_count_a(h).            (7)

Translation by a complete period changes the candidate coordinate but
not any modular predicate or s_a. Formula (7) therefore agrees with the
saved `divmod(length,self.M)` convention. It concerns this selected stage's
prime product M; extra primes require their own retained conditions.

## 5. Agreement with the saved weighted-pair carry

The code's final `self.U` and `self.V` at
[lines78–82](/workspace/em-owner-resume-20261011/new-round-20261011/factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py:78)
are CRT-weighted residues modulo M. They are not respectively the
canonical a in `[0,u)` and local b in `[0,v)`. The `u` loop variable in
`_count_remainder` is a weighted residue, not the modulus u in this note.
Those different coordinates must not be silently exchanged.

For u>1, the same pair (a,b) has weighted representatives

    omega_a=v*(v^(-1) mod u)*a mod M,
    nu_b=u*(u^(-1) mod v)*b mod M.

The u=1 contribution is0 without an inverse modulo1, as in the saved
code. CRT uniqueness gives

    (omega_a+nu_b) mod M=a+u*t=k.

Since both weights lie in `[0,M)`, their ordinary sum is k+epsilon*M,
with epsilon in {0,1}. Thus `k<h` is exactly the disjoint condition

    omega_a+nu_b in [0,h) union [M,M+h).                     (8)

For fixed omega_a, (8) produces exactly the two old intervals
`[0,h-omega_a)` when omega_a<h and
`[M-omega_a,min(M,M+h-omega_a))` in the sorted weighted nu array.
These are precisely the comparisons in saved lines100–106.

Equations (5)–(6) and (8) count the same pairs by a bijection, while using
different order coordinates. Multiplication/scaling by CRT weights or2,
followed by reduction to canonical modular residues, does not preserve
the original canonical-residue sort order in general. Ordinary integer
multiplication by2 itself is increasing; the ordering warning concerns
the reduction modulo the relevant modulus. In particular one
must not pass cutpoints of (6) directly to the old sorted `self.V` array.
The new R_D table/stream and its translated cuts need their own descriptor
and paid construction. This proves carry agreement without rerunning the
old rank code or its samples.

## 6. Scope, costs and actual progress

The paid state needed by this application includes N,c0, the prime proof,
u,v, the complete retained A and its predicate provenance, inverse u,
D, each canonical a and s_a, the original offset prefix L, its M-period
decomposition, the row lengths (5), and whichever R_D cutpoints/table are
actually constructed. Local square bitsets, A construction, input/root
work, ranks, sorting, arithmetic and outputs retain positive costs.
Sharing one V_D stream is an available exact representation; no measured
gain or new complexity improvement follows from this dictionary.

The new work here is the factor-of-two coordinate match, the precise
prefix induced in each real saved CRT row, and the equivalence of the
translated and weighted-pair carry conventions. The underlying CRT
bijection, shifted-square translation theorem and old complete-list cost
result are inherited. No claim is made that any saved old code already
omits B_v, implements R_D, or executes a new solver.

Additional pair conditions, prime powers, composite Jacobi substitution,
unproved-prime inputs and nonlinear Hart candidate coordinates are outside
this application. Surviving a modular square filter is still only a
necessary condition for an integer-square hit; the final exact square
and proper-factor checks remain separate. General factoring gain, Native
acceptance, and all mathematical parent targets remain unproved.

Main new-contract dependency:
[CRT_SHIFTED_QUADRATIC_ROW_TRANSLATION_AND_RANK_20261014.md](/workspace/em-owner-resume-20261011/new-round-20261011/CRT_SHIFTED_QUADRATIC_ROW_TRANSLATION_AND_RANK_20261014.md),
saved SHA256
`ab79cfd196328145c2c04166433faf86f16564238c1d37418974539281b9dd81`.
No existing file was modified by this paper unit.

````

</details>

## NT-SUP-CRT-CARRY

真实CRT前缀摘要碰撞与有理线性联合修复维数

真实全乘积筛的少量局部摘要可能碰撞；另行声明的coupled payload模型即使保留全marginals与aggregate carry仍缺joint interaction，两种scope分列。

状态：`EXISTING_DIRECTED_NONBLIND_NONAUTHOR_PAPER_PASS_NOT_NATIVE_ACCEPTANCE`。

原贡献与归属：EM-CRTJC-5F30D8A2 / RA-CRT-JOINT-CARRY-20261014-A1；original owner EM-DIRECT-FB83AB。

Source：[research_notes/OWNER_PARALLEL_CM24_CRT_AND_MCP_REPAIR_20261014_FBF223.json](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/OWNER_PARALLEL_CM24_CRT_AND_MCP_REPAIR_20261014_FBF223.json)。

原capsule成员：`new-support/crt-joint-carry/ACTUAL_SHIFTED_SQUARE_CARRY_INTERACTION_MINIMALITY.md`；此成员路径是归档标签，不能伪装成独立GitHub路径。

- N1=871=13·67,N2=889=7·127,c0=30,p=3,q=5；A={1,2},B1={0,1,4},B2={0,2,3}。h5两local counts均3，但joint counts为2与1；摘要不保留N residue/完整predicate时失败。
- 固定N871的canonical k表((10,1,4),(5,11,14))，carry表((0,1,1),(0,0,0))；X={(1,1),(2,4)},Y={(1,4),(2,1)}同全marginals与carry1，但C_X(3)=1,C_Y(3)=0。
- A,B非空，sizes r,c；W=span_Q{row,col,ε}，δ=0当ε_ab=f_a+g_b，否则δ=1。全integer cuts与任意rational payload所需最少额外rational-linear统计d=(r−1)(c−1)−δ。
- G_(k+1)−G_k=该cell indicator；对nonnegative integer payload与任意decoder，rational-coefficient保留统计的同一necessity成立。有限cut H时d=dim(W+span G_H)−dimW。
- 六cell r2,c3,δ1故d1；t=C_x(3)=x_(1,1)。恢复x11=t,x14=e−t,x10=ρ1−e,x21=γ1−t,x24=γ4−e+t,x20=γ0−ρ1+e。
- m组coprime support S=∏r_i,marginal span dimension1+Σ(r_i−1)；加声明interaction后的额外维数为S−dimW。

前提：固定coprime CRT support与distinct canonical k；arbitrary payload是明确扩大输入，旧QRWheelIndex只支持all-ones全product。

边界：维数不是bit/space/operation下界；无限精度任意real系数+非线性decoder在范围外。；不把coupled payload碰撞说成旧unweighted product index错误；保留N可付费重建，少量summary witness不否定全部rank查询。；exact repair scalar t需实际付费获得；不主张廉价factor scalar、exponential wheel storage lower bound、速度或完成parent。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Actual shifted-square CRT prefixes: marginal summaries, carry and the remaining interaction

2026-10-14. Bounded directed NONBLIND paper unit by local agent
`/root/crt_joint_carry`, Researcher-ID `EM-CRTJC-5F30D8A2`.
Lightweight activity `RA-CRT-JOINT-CARRY-20261014-A1` is on EM main at
`cc25783a78d5d5778a5ef34356a32a172abf300c`; its locally assigned stable
session key is `local-agent-root-crt-joint-carry-20261014`, not a
platform-attested chat identity. Original mathematical owner
`EM-DIRECT-FB83AB`, formal Task/claim/epoch and all earlier authorships are
unchanged. No new Task, claim, Run, branch, old-code execution, Hart sample,
scientific script, prime search or measured gain is created here.

**New bounded result.** Two actual odd-semiprime shifted-square instances
have identical local cardinalities and identical local counts at the
requested prefix, but different joint prefix counts. On one of these
actual legal CRT supports, even full row/column marginals plus an aggregate
carry statistic fail for a declared *additional* coupled-payload observer.
For that additional observer the exact number of rational linear repair
statistics is proved, and is one in the displayed example. The saved
full-product algorithm does not support arbitrary coupled payloads, and
the latter theorem is not a lower bound for its static unweighted rank.

## 1. Exact inherited interface and nonduplication boundary

The complete input application is
`CRT_ACTUAL_SAVED_SIEVE_DICTIONARY_20261014.md`, 12152 bytes, SHA256
`281b4a057f420eb9fb45af86d69f9ff5164551badf85155b6d6237abd8f14f79`,
and its final nonauthor review. Its saved code is
`factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py`,
SHA256 `a5d4a53431d020b40787197aa68ccf3aa1703708b7716c6c4ebeba4318c37820`.
All three paths are under
`/workspace/em-owner-resume-20261011/new-round-20261011/`.
I read the code statically, especially lines 24–44, 50–82 and 96–114;
I did not import or execute it.

For odd N and fixed c0=ceil(sqrt(N)), its actual prime-p survivor set is

    A_p(N)={a in [0,p): (c0+a)^2-N is a square mod p, including zero}.

For two coprime groups u,v, complete legal lists A,B and M=uv, retain
the exact Cartesian-product relation A x B. The inherited weighted maps
are

    omega_a=v*(v^(-1) mod u)*a mod M,
    nu_b=u*(u^(-1) mod v)*b mod M,
    s_ab=omega_a+nu_b,  k_ab=s_ab mod M,
    epsilon_ab=floor(s_ab/M) in {0,1}.

For u=1 the first weight is zero without an inverse modulo 1. The
one-period prefix observer is G_h(a,b)=1_{k_ab<h}, 0<=h<=M integer.
The saved rank already counts the two intervals s<h and M<=s<M+h.
That formula, cyclic row splitting, CRT injectivity, full-list paid
obstruction, sorted rank/select and the translation x=2(c0+k),
D=N/u^2 are inherited, not newly proved or benchmarked here.

I also read the corrected ordinary-prime-QR character-stream rank
tradeoff at
`crt-rank-only-interface-20261013/correction-v2/PRIME_QR_LEGENDRE_STREAM_RANK_SPACE_TRADEOFF_CORRECTED_V2.md`.
It already contains a two-coupled-relation/marginal counterexample for
ordinary QR sets. The present contribution uses the *actual saved
shifted-square predicate*, separates full-product from extra coupled
states, keeps aggregate carry equal, and gives a sharp linear repair
dimension. It is not a new generic CRT or marginal-collision mechanism.

Current connected-main toolbox/method coverage was read before writing
this mechanism: toolbox Git blob
`3889506451091ebcfbf7a58cda6517c4af8c3597`, method inventory Git blob
`9289039bc689c638fbef10f9f4489e3793e999f0`. Resolution is
**COMPOSE_APPLIED**: T6 operation-safe quotient/fiber-constancy and
coarsest repair, the existing mixed finite-difference separability
diagnostic, and the inherited CRT rank interface. No new general tool
family, executable coverage gap, global literature novelty or Native
acceptance is claimed.

## 2. A failure wholly within the saved full-product input model

Take the fixed proved primes p=3,q=5, M=15, and the two odd semiprimes

    N1=871=13*67,    N2=889=7*127.

The displayed factors certify the example class; no hidden factors are
used by the index or used as a query oracle. Both numbers lie strictly
between 29^2=841 and 30^2=900, so both have c0=30. Both are coprime to
15, and both are 1 mod 3. Modulo 5 they are respectively 1 and 4.
The only prime square sets used in this hand calculation are {0,1}
mod 3 and {0,1,4} mod 5.

For N1 and N2 the p=3 allowed offset set is {1,2}: at a=0 the residual
is -1=2 mod 3, whereas at a=1,2 it is zero. For q=5, directly evaluating
b^2-N_i (c0=0 mod 5) gives

    B1={0,1,4},     B2={0,2,3}.

Thus the complete local cardinalities are (2,3) in both instances.
At integer prefix h=5, the standalone p-filter accepts offsets {1,2,4}
and has count 3. Each q-filter has completed one whole q-period and
also has count 3. Nevertheless their actual *conjunctions* on [0,5) are

    N1: {1,4},      N2: {2},

so their joint counts are 2 and 1. These are the unweighted full-product
predicates that the saved code actually accepts; no extra coupled
condition has been added for this witness.

Consequently no function of just (p,q,c0,h, the two complete local
cardinalities, the two standalone prefix-count values at h) computes
all such joint prefix counts. It is essential that the *summary* here
omits N's residue/predicate descriptor and the complete local rank
functions. Keeping N and paying to recompute its actual predicates, or
keeping both full local sets/rank functions and their CRT relation,
can recover the joint answer. This witness does not deny that fact and
does not show that all local rank queries are insufficient. It forbids
replacing the actual joint-cut prescription by these few independent
numbers alone.

## 3. A second observer, explicitly outside current saved-code scope

Now fix only N1=871 and retain the same legal A={1,2}, B={0,1,4}.
The CRT weights are omega=(10,5) in row order a=(1,2) and
nu=(0,6,9) in column order b=(0,1,4). The actual tables are

| a / b | 0 | 1 | 4 |
|---|---:|---:|---:|
| 1: canonical k | 10 | 1 | 4 |
| 2: canonical k | 5 | 11 | 14 |
| 1: epsilon | 0 | 1 | 1 |
| 2: epsilon | 0 | 0 | 0 |

Each cell is a real survivor of *both* saved shifted-square local
predicates. The six k values are distinct. This is direct small paper
arithmetic, not a new run of the saved code.

For this section only, declare an enriched support state x_ab: a
nonnegative integer multiplicity on these already legal pairs. Such a
state can describe a later extra pair filter, a provenance-selected
candidate stream or retained repeated occurrences. The observer is

    C_x(h)=sum_ab x_ab*G_h(a,b).

Allowed readouts are all integer cuts h=0,...,M on the *same* fixed
support and arbitrary permitted multiplicities. No time evolution,
nonlinear candidate map, or change of N/moduli is introduced. The
current QRWheelIndex has x_ab=1 for every legal cell and does not expose
this enriched input. These extra states are a proposed future interface,
not a previously implemented capability and not evidence of a bug in
the saved full-product code.

Consider two such selected-pair states, each containing two candidates:

    X: (a,b)=(1,1),(2,4),      canonical k={1,14};
    Y: (a,b)=(1,4),(2,1),      canonical k={4,11}.

Both have row counts (1,1), column counts (0,1,1), total mass 2 and
one pair of each carry value. Thus *complete* row/column marginal
histograms, every marginal rank derived from those histograms, and the
aggregate carry count are identical. But C_X(3)=1 and C_Y(3)=0.
Carry without its association to the relevant thresholds does not repair
these marginal summaries. Total mass and the full binary carry histogram
add nothing further in this example: total mass is already a marginal
sum and carry=0 count is total mass minus carry=1 count.

Equivalently, on the 2-by-2 rectangle with columns b=1,4, the mixed
difference of epsilon is zero while that of G_3 is nonzero. Hence G_3
is not a rational linear combination of row indicators, column
indicators and epsilon. This is an exact allowed-observer span test,
not the invalid assertion that CRT labels cannot reconstruct a number.

## 4. Sharp number of rational linear repairs for that enriched observer

**Theorem.** Let A,B be nonempty finite complete CRT support lists of
sizes r,c>=1, with gcd(u,v)=1 and distinct canonical CRT residues on
A x B. Work over Q. Let W be the span of all row indicators, all column
indicators and the one carry function epsilon. Define delta=0 when
epsilon is additively separable, epsilon_ab=f_a+g_b, and delta=1
otherwise. If all one-period integer prefix readouts C_x(h), 0<=h<=M,
must be recovered for arbitrary rational payloads x, the minimum number
of additional rational linear statistics, with linear decoding, is

    d=rc-(r+c-1+delta)=(r-1)(c-1)-delta.                (1)

The same necessity applies to arbitrary nonnegative integer
multiplicities and *any* decoder when every retained statistic has
rational coefficients. The sufficiency is still by linear decoding.
This counts statistics; it is not a bit, space or operation lower bound.

**Proof.** The row/column indicator span consists exactly of f_a+g_b
and has dimension r+c-1: the only coefficient redundancy is adding a
common constant to f and subtracting it from g. Adding epsilon changes
this dimension by delta, proving dim W=r+c-1+delta. Additive
separability is equivalent to vanishing of every rectangular mixed
difference: fixing one anchor row and column supplies f,g when they all
vanish.

For every legal cell (a,b) with canonical k=k_ab,

    G_(k+1)-G_k = 1_{that cell}.

This uses integer half-open cuts and CRT injectivity, so the difference
does not combine several legal cells. Hence all prefix indicators span
the full rc-dimensional vector space Q^(A x B). Additional linear
statistics must extend W to that full space; at least rc-dim W are
necessary and any choice completing a basis suffices. This proves (1).

For the nonnegative integer necessity, if the retained rational
statistics have rank less than rc, their common kernel contains a
nonzero rational vector z. Clear denominators to make z integral and
write z=z_plus-z_minus with disjoint nonnegative integer parts. Because
row marginals are among the retained statistics, z has total sum zero;
both parts are valid equal-total support multiplicities with identical
retained statistics. Some cell coefficient is nonzero, so the complete
family of prefix differences distinguishes them. No decoder can then
produce all prefixes for both. This is not an unrestricted encoding
bound: arbitrary real coefficients with infinite precision and
nonlinear decoding, or a restricted payload family, are outside the
claim. QED.

For a finite selected cut set H instead of all integer cuts, the exact
number is

    dim(W+span{G_h:h in H})-dim W.                     (2)

The dimension proof is identical. A fixed empty or full-period query
can need zero repairs; no positive lower bound is inferred for every
individual cut. For the prefix family alone, the coarsest per-pair
observation signature is its bucket relative to H; with every cut
retained this identifies k. If the row/column/carry observations in W
must also be preserved per pair, their signatures must be retained as
well. This is a scoped use of the existing T6 quotient mechanism, not
a new universal compression theorem.

## 5. Explicit minimal repair for the actual six-cell example

In the table above r=2,c=3. Carry is not additive: using columns 0,1,
its mixed difference is 0-1-0+0=-1. Thus delta=1 and d=1.
The nonzero G_3 mixed difference on columns 1,4 shows that G_3 is a
valid additional basis direction. Write row totals as rho_1,rho_2,
column totals as gamma_0,gamma_1,gamma_4, total carry as e, and store
the one new statistic t=C_x(3)=x_(1,1). All six cells are recovered by

    x_(1,1)=t;                  x_(1,4)=e-t;
    x_(1,0)=rho_1-e;            x_(2,1)=gamma_1-t;
    x_(2,4)=gamma_4-e+t;         x_(2,0)=gamma_0-rho_1+e.

Each identity follows directly from the displayed carry support and
row/column sums. Therefore every prefix is the sum of the recovered
cells whose displayed k is below h. If nonnegative payloads are the
declared input, the recovered entries must also be checked nonnegative;
inconsistent summaries are a typed error, not clipped to a guessed
state. Keeping t is only useful after paying to obtain it from the
original joint state; it is not a free oracle for a difficult rank.

Deleting the aggregate carry statistic while keeping only marginals
raises (1) from one to two extra rational linear directions on this
support. Conversely, storing every pair's exact omega,nu or k makes
epsilon arithmetic-reconstructible; floor((omega+nu)/M) then has its
paid comparison/division cost. The saved _count_remainder already
stores no separate epsilon array and computes the two carry intervals
inline. There is no stored carry-bit table here to delete as a new
memory optimization. Replacing that joint-cut prescription by marginal
counts would erase a necessary relation; replacing it by the previously
proved translated-rank interface preserves it and requires its own
paid rank descriptor. No new faster descriptor is proved by this note.

## 6. Multiple moduli and the precise retained relation

For m coprime groups, complete local lists of sizes r_i, and their
Cartesian support of size S=product r_i, CRT still maps each tuple to
a unique canonical k in [0,M). The independent marginal span has
dimension 1+sum_i(r_i-1). With any declared additional interaction
statistics E_1,...,E_j let W be their span with the marginals. The same
prefix-difference proof gives exactly

    d=S-dim W

additional rational linear statistics for arbitrary rational joint
payloads and all integer cuts. The ordinary sum of m canonical CRT
weights has a carry in {0,...,m-1}. Retaining its mean is one statistic;
retaining its full histogram gives at most m-1 additional independent
statistics after total mass. Neither is automatically all joint
interaction data. This is a theorem for the *declared payload and
linear-observer contract*. It does not imply exponential storage for
the full-product all-ones wheel, which retains the exact independent
product law and can evaluate prefixes by paid reconstruction/rank.

The distinction is useful for accepting a future delta(a,b) filter:
unchanged local marginals plus an aggregate carry number cannot in
general justify reuse of the unweighted product rank. The missing
interaction must remain in an exact pair/row descriptor or an explicitly
proved sufficient quotient. Factor reconstruction of k, by itself,
neither supplies a linear callable observer nor pays its computation.

## 7. Paid cost, native bridge, outcomes and next unfinished obligation

All old costs remain: input N and c0, proved-prime validation, gcds,
inverses, local predicate construction, canonical and weighted residue
preparation, sorting, ranks, row cuts, counters, certificate/output
writes and final integer-square/proper-factor certification. For a
new coupled stream of T explicitly listed occurrences with B-bit
weights/coordinates, accumulating its marginals/carry/t requires
reading all T occurrences, forming or validating their association and
performing the relevant modular/threshold arithmetic. A simple
schoolbook bound charges O(T*B^2) work for coordinate arithmetic plus
the actual payload bit arithmetic and O((r+c+j)*B) counter storage
when counters fit B bits; enlarge B for longer/rational payloads.
Nothing proves this is optimal or beats a direct paid prefix scan.
Arbitrary rational payloads have numerator/denominator bit growth;
dimension (1) does not bound that growth or the preparation cost.

Constructing a repair basis for a general support also costs work:
at least the inspected support description and the exact arithmetic
used by linear algebra. This note supplies a six-cell paper basis, not
a compressed implementation that can avoid reading a large support.
Its one-scalar repair cannot be promoted to a cheap scalar evaluation
algorithm. All prior full-list/full-traversal lower boundaries retain
their original premises and remain unchanged.

Basis is HEARTBEAT_WORLD_NATIVE_X6. The explicit restricted readout
bridge is: a retained native-state/provenance object at a Cell carries
the typed integer descriptor (N,c0,moduli,local predicates,CRT relation)
and, only in sections 3–6, typed joint occurrence multiplicities over
that descriptor. The arithmetic observation reads C_x(h); it is not a
full Cell address or a claim that these residue fields are spatial
axes. Equal marginal readouts do not identify native states. The
counterexample retains their joint relation; the linear repair is
certified only for all cuts on the same fixed support and payload
family. Changing the support, predicates or allowed future operations
requires a new preservation check. No spatial dimension is removed,
no native propagation law is inferred and no separately typed time is
needed for these static observations.

Discriminating outcomes for this bounded unit were: (A) a valid formula
using only the declared numerical local summaries; (B) an actual saved-
predicate counterexample; (C) carry is a sufficient universal repair;
(D) carry leaves an exact additional interaction. Sections 2 and 3
establish B and D in their respective scopes. Kill conditions are now
explicit: abandon a summary-only full-prefix proposal when these two
actual instances collide; abandon an aggregate-carry-only coupled
proposal when the X/Y witness is in its input language. Do not apply
either kill to an interface that retains a sufficient paid descriptor.

**Next unfinished useful lemma.** For the unchanged saved full-product
model, choose a precise shared shifted-square rank descriptor that
avoids one required complete nontrivial group list; prove construction,
all translated cut queries and total paid bit cost under a stated
within-instance query workload. Compare against the already optimized
two-pointer/sorted-rank wheel and the paid shared-predicate streaming
fallback. Required outcomes are an actual total-cost inequality or an
honest space-versus-recomputation tradeoff; a renamed carry or a scalar
oracle is a kill, not progress. No new Hart sample or extra coupled
filter is needed to pursue that original interface question.

This is new scoped mathematical support with review pending. It grants
no Native Task acceptance, complete factoring result, measured speedup,
global novelty, Working Truth or closure of the mathematical parent.

Researcher-ID: EM-CRTJC-5F30D8A2 / TASK_RESEARCH

````

</details>

## NT-SUP-CRT-BATCH-CORRECTED

真实one-prime CRT的offline batch rank：去第二list及比较位宽勘误

已知Q个prefix查询用去重cut树、一次付费predicate stream和二次row/query pass，避免第二完整survivor及weighted list；位宽比较采用已公开勘误。

状态：`REVIEWED_CORRECTION_DIRECTED_NONBLIND_PAPER_ONLY_NOT_NATIVE_ACCEPTANCE`。

原贡献与归属：EM-CRTJC-5F30D8A2；nonauthor EM-NONAUTHOR-5DF3A9B6，均DIRECTED_NONBLIND；original owner EM-DIRECT-FB83AB。

Source：[research_notes/CRT_BATCH_WIDTH_CORRECTION_AND_FAIR_REVIEW_DEDUP_20261014_FBF223.json](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/CRT_BATCH_WIDTH_CORRECTION_AND_FAIR_REVIEW_DEDUP_20261014_FBF223.json)。

原capsule成员：`crt-joint-carry/ACTUAL_SHIFTED_SQUARE_OFFLINE_BATCH_RANK_PAID_CONTRACT.md`；此成员路径是归档标签，不能伪装成独立GitHub路径。

- r=|A|,D=N/u²,b_a=(a+c0)/u modv,s=(v+χ(D))/2；L=qM+h，n_a(h)=min(v,max(0,1+floor((h−1−a)/u)))。
- e=(b_a+n) modv,w=floor((b_a+n)/v)；row=R(e)−R(b_a)+ws；C(L)=qrs+Σrow。
- Jset=({b_a}∪{e_a(h_i)}) minus {0}，J≤min(v−1,r(Q+1))；动态distinct-key tree不保存Q*r request-tags。
- Q,r≥1时work C_A+P_v+O((j_max+1)B³+QrB²)，另计实际certificate/provenance/output；rank-phase space O((r+J+Q+1)B)。
- 普通local second list Θ(v logv)bits；CRT-weighted list Θ(v logM)bits；uniform B-slot layout才是Θ(vB)。省第二weighted list的充分额外space条件为(J+Q+1)B=o(v logM)，共同A与provenance另计。

前提：同一固定实际one-prime extension、完整A、proved odd v、N odd≥3、c0=ceil√N，明确gcd(u,v)=gcd(N,v)=1，old selected primes皆coprime N；Q查询预先offline且与隐藏factor/真hit无关。；B至少覆盖N,M,queries,Q,r真实bit宽；r0/Q0/J0分支单列，做过的setup仍收费。

边界：原85fd旧paper/720c旧review已正式保存，不能改说未发布；仅Θ(vB)与J+Q=o(v)无条件比较被替换，算法/端点/J/work bound保留。；whole-instance peak仍含A构造与primeproof；较小rank-phase可更慢，不是strict total-work advantage。；未知online cuts、adaptive select、composite next group、coupled payload、Hart nonlinear candidates另需合同；modular survivor不是proper factor。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# One actual shifted-square CRT stage: offline batch ranks without its second complete list

2026-10-14. Bounded directed NONBLIND paper companion by
`/root/crt_joint_carry`, Researcher-ID `EM-CRTJC-5F30D8A2`,
activity `RA-CRT-JOINT-CARRY-20261014-A1`. Original mathematical owner
`EM-DIRECT-FB83AB`, formal Task/claim/epoch, earlier authors and completed
units are unchanged. Root requested this same-unit paid contract after
the carry-interaction paper identified the unchanged full-product
retrieval question. No new Task, claim, Run, old sample, source program
execution, scientific script or benchmark was created.

**Result.** For Q integer prefix queries known in advance on one fixed
actual one-prime CRT extension, at most

    J<=min(v-1, r*(Q+1))

distinct nontrivial base-set cutpoints suffice, where r=|A|. They can be
generated and deduplicated without storing Q*r request tags. One paid
Legendre-predicate stream fills those J prefix counts; a second
row/query pass reconstructs every answer. This omits the complete local
second survivor list and its CRT-weighted list. It establishes an exact
space-versus-recomputation contract, not a speedup or a new factoring
algorithm.

## 1. Actual input and inherited mathematics

Use the final saved-predicate dictionary under
`/workspace/em-owner-resume-20261011/new-round-20261011/`:
`CRT_ACTUAL_SAVED_SIEVE_DICTIONARY_20261014.md`, 12152 bytes, SHA256
`281b4a057f420eb9fb45af86d69f9ff5164551badf85155b6d6237abd8f14f79`,
with its nonauthor review. The underlying saved program is
`factorblind-implicit-crt-interface-20261013/implicit_crt_qr_index.py`,
SHA256 `a5d4a53431d020b40787197aa68ccf3aa1703708b7716c6c4ebeba4318c37820`.
It was read statically, not executed. The shifted-quadratic translation
paper and corrected ordinary-QR rank tradeoff are inherited inputs,
not fresh results or timings.

Fix odd N>=3, c0=ceil(sqrt(N)), an old squarefree product u of distinct
odd primes, and a complete distinct canonical survivor list A in [0,u)
for its saved shifted-square predicates. Every selected prime is proved
and coprime to N. The empty old group u=1 has its declared virtual
singleton A={0}; no array entry or inverse modulo 1 need be allocated.
Let v be one next proved odd prime, gcd(u,v)=gcd(N,v)=1, and M=u*v.
Only this one-prime extension is in scope. A composite second group or
Hart's nonlinear ceiling-root candidates require another contract.

The actual new local set is

    B_v={b mod v : (c0+b)^2-N is a square mod v, including zero}.

The mathematical support is exactly A x B_v under CRT, with every
legal pair counted once. No extra coupled payload/filter is admitted
by this interface. Retain its exact product relation, the A provenance
and all modulus/predicate pins; numerical marginal summaries alone
are not a replacement for these data.

Write inv=u^(-1) mod v and, in F_v, set

    D=N*inv^2,    b_a=(a+c0)*inv mod v,
    V_D={z in F_v : chi(z^2-D)>=0},
    R(j)=#{z in V_D : 0<=z<j}, 0<=j<=v.

This is precisely the inherited actual dictionary x=2(c0+k),
D=N/u^2, not the incorrect undoubled use of 4N/u^2. Its canonical row
k=a+u*t, 0<=t<v, survives iff (t+b_a) mod v is in V_D. Since D!=0,

    s=|B_v|=|V_D|=(v+chi(D))/2.

Primality and all character evaluations are paid; s is an exact integer
cardinality, not an average density. The endpoint values R(0)=0 and
R(v)=s are available after this paid setup, without a complete list.

## 2. Exact query endpoints and one-cut-per-row reduction

The Q queries are public nonnegative integers L_1,...,L_Q. They are
known before this batch begins, may repeat, and are independent of
hidden factors or the true successful factoring offset. The output is

    C(L_i)=#{0<=k<L_i : k passes the retained u predicates and v}.

All intervals are half-open integer intervals. For a query write
L=q*M+h with integer q>=0 and 0<=h<M. For every canonical a in A set

    n_a(h)=min(v,max(0,1+floor((h-1-a)/u))).

Then the row's legal prefix is exactly 0<=t<n_a(h). In particular
h=0 gives n=0. This is the inherited integer-prefix dictionary; no
inclusive endpoint has been silently substituted. Put

    e_a(h)=(b_a+n_a(h)) mod v,
    w_a(h)=floor((b_a+n_a(h))/v) in {0,1}.

The inherited two-interval cyclic rank now has the single uniform form

    row_a(h)=R(e_a(h))-R(b_a)+w_a(h)*s.                (1)

Indeed b_a in [0,v), n in [0,v], and translating [0,n) by b_a wraps
at most once. If b_a+n<v the ordinary rank difference applies. If
b_a+n>=v the interval is [b_a,v) followed by [0,e), giving (1).
At equality b_a+n=v, e=0 and w=1, so the endpoint at v is counted
correctly without requiring a stored R(v). Empty rows give e=b,w=0;
complete rows give e=b,w=1. The only carry used is this exact declared
row wrap, not a guessed mean or a sorted weighted-residue cut.

Consequently

    C(L)=q*r*s + sum_(a in A) row_a(h).               (2)

This sums the actual CRT bijection and charges every previous complete
period. R cutpoints are in the canonical z coordinate. They must not
be looked up in the saved code's differently sorted weighted nu array.

## 3. Offline cut set, without a hidden Q*r tag array

For Q>=1 and r>=1, define the set of *nontrivial* required cuts

    Jset=({b_a:a in A} union {e_a(h_i):a in A,1<=i<=Q}) minus {0}.

All cuts lie in {1,...,v-1}, so J=|Jset| obeys the displayed bound.
R(v) is not requested by (1); s is already the paid endpoint identity.
Duplicates do not create new counters. If J=0, no predicate stream is
needed. If A is empty, every answer is zero. If Q=0, return an empty
answer list; no character stream is necessary. Any setup actually
performed on these branches is still charged.

One concrete deterministic implementation uses a balanced search tree
of distinct integer cut keys, with one eventual count slot per node.
It retains A, optionally its r shifts b_a, the Q input queries and the
tree. It does *not* first append all Q*r tagged requests to an array.

1. Insert nonzero b_a into the tree while computing the r row shifts.
2. Scan each query and every retained row, recompute h_i,n,e, and insert
   a nonzero e only if absent. An attempted duplicate still has its paid
   search cost. No query/row tag is retained.
3. Traverse the tree in increasing-key order, or extract its J keys in
   sorted order. Let j_max be the largest key, or 0 when J=0. Starting
   with z=0 and count=0, scan z<j_max once. Before storing R(j), the
   count has accumulated the indicators for exactly 0<=z<j. Use

       I_D(z)=(1+chi(z^2-D)+1_{z^2=D})/2

   as the exact zero-inclusive integer predicate. Store only counts at
   the J requested keys. No B_v,V_D,weighted-nu list, v-bit square table
   or full R array is constructed by this algorithm.
4. Scan queries and rows a second time. Recompute e and w, look up
   R(e),R(b_a) in the J-key structure (zero uses its known value), apply
   (1), then (2). No saved Q*r lookup map is used. All recomputation
   and both lookups are paid.

The stream loop is a new abstract implementation contract, not a claim
that the saved QRWheelIndex already implements it. Since j_max<=v-1,
there are at most v-1 stream predicate visits, plus setup character
work. The worst-case bound v visits remains a harmless conservative
bound. Output answers can be returned as a Q-vector or streamed in
input-query order after the second pass; streaming pays each write.

Correctness follows from the exact stream prefix invariant, (1), (2)
and complete retention of the input product relation. Dynamic
deduplication affects only repeated requested cut keys, not survivor
multiplicity or pair association. It never quotients a native state or
turns factor reconstruction into a free callable observer.

## 4. Complete cost contract and actual workspace

Use schoolbook B-bit arithmetic, where B is at least 2 plus the bit
length of max(2,N,M,1+max_i L_i,Q+1,r+1), taking the empty-query
maximum as zero when Q=0. O(B)-bit words therefore hold
residues, all loop indices, prefix counts and answers. Larger supplied
certificate/provenance payloads retain their actual separate read and
storage costs. B includes large N, not merely log v. Integer division
and multiplication cost O(B^2); additions/comparisons O(B); Euclidean
inverse/gcd and a concrete binary-search integer root use conservative
O(B^3) work and O(B) arithmetic scratch.

Let P_v and S_v^cert denote actual prime-certificate verification work
and workspace. A fully explicit fallback trial-divides through
floor(sqrt(v)), at O(sqrt(v)*B^2) conservative work and O(B) scratch.
This is paid; a fast certificate cannot be presumed for free. Reading
N and deriving c0, gcd(u,v), gcd(N,v), inv, D and chi(D) have their
own O(B^3) conservative setup in addition to verification/input costs.
For a proved prime, Euler exponentiation computes each nonzero
Legendre value by at most O(B) modular multiplications, costing
O(B^3) work and O(B) scratch; zero is a charged comparison branch.
No character oracle or zero-cost modular square root is assumed.

Let C_A be the full already-incurred or newly required work constructing
and verifying the complete A with its old prime/predicate provenance;
let S_A^construction be that process's peak space. These quantities are
not waived. Reading r entries is O(rB); range/distinctness checks, if
not already certificate-bound, can use a balanced tree with
O(r*log(r+1)*B)<=O(rB^2) work and O(rB) space. Completeness requires
the declared exact construction/certificate, not just these checks.

For r,Q>=1, a concrete paid rank phase has:

| Operation | Work, excluding already separately named certificate/provenance costs |
|---|---|
| Query/input scan and period divisions | O((r+Q)B+QB^2) |
| r shifts and base-cut inserts | O(rB^2+rB*log(J+1)) |
| First query/row pass, cut generation and dynamic duplicate checks | O(QrB^2+QrB*log(J+1)) |
| Sorted traversal/count-slot initialization | O(JB), with an O(JB) explicit sorted-key array if chosen |
| One shared stream, including residual formation and counter bookkeeping | O(j_max*B^3+JB) |
| Second query/row pass, recomputation, rank lookups, sums and outputs | O(QrB^2+QrB*log(J+1)+QB) |

The tree has J<=v-1 distinct keys, hence log(J+1)<=log v<=B;
the lookup terms are bounded by O(QrB^2). No Q*r-sized array is hidden
in the ledger. Root/certificate/setup work and every duplicate attempt
remain positive. A convenient conservative total bound is

    C_A + P_v + O((j_max+1)*B^3 + QrB^2),             (3)

plus actual separately sized provenance/certificate/output transport
costs. The r=0 or Q=0 branches are handled above rather than dividing
by r or charging an imaginary scan. If a common upstream A
construction has different bit bounds, its actual C_A must be used.

The rank-phase retained/workspace bound, including stored A and the
batch inputs/answers, is

    O((r+J+Q+1)*B) + actual certificate/provenance storage.   (4)

Working counters and a streaming Euler computation need O(B) scratch;
tree nodes have O(B)-bit keys/counts/pointers under this bound. Input A
and its cached shifts need O(rB); queries and answers O(QB); the tree
and any extracted sorted-key array O(JB). Replaying input queries can
avoid retaining their duplicate copies, but is not required for (4).
The whole-instance peak also includes S_A^construction and prime-proof
verification workspace. Omitting a second list cannot guarantee a
smaller whole-instance peak when a shared upstream cost dominates.
The u=1 virtual singleton may be represented implicitly, with positive
loop arithmetic but no fabricated allocated list entry.

## 5. Fair comparator and scope of any savings

The actual complete-list implementation constructs B_v of size
s=(v+chi(N))/2, then its distinct CRT-weighted second-side residues.
An explicit fixed-width residue representation uses Theta(v*log(v))
bits for B_v and Theta(v*log(M)) bits for the weighted list; storing
every entry in a uniform B-bit slot instead uses Theta(vB) bits.
B can be much larger than log(M) because it also includes N and the
queries, so these representation choices must not be conflated. Its
positive local-square-bitset/extraction/weight work is O(vB^2)
conservatively, plus sorting O(v*log(v)*B) and the chosen actual prime
and root setup. It can use the previously proved least of binary-row
rank or two-pointer rank; Q queries retain those charged bounds. An
optimized comparator is allowed the same mathematically valid
character stream or shared cuts as this contract. No exclusive
algorithm advantage follows from naming this batch representation.

Relative to *materializing the second complete weighted list*, a
sufficient condition for (4)'s additional batch/cut storage to be
asymptotically smaller is (J+Q+1)*B=o(v*log(M)), holding common A and
provenance costs fixed. For example this holds when B=O(log(M)), r
and Q remain bounded, and v grows. In a uniform B-bit-slot comparator
the weaker J+Q=o(v) condition suffices, but that is a declared layout,
not a lower bound on every width-aware representation. The
stream performs modular exponentiations at O(B^3) per visit whereas
the table's square-marking extraction has an O(vB^2) work bound.
Thus even a smaller retained representation can be slower, and (3)
proves no total-work improvement. When J is near v, there may be no
meaningful representation saving. This is a precise tradeoff, not a
measured memory or runtime claim.

The Q queries must be fixed *offline*. For an unannounced later cut
whose required R key is absent, its count has not been stored. An
online extension must pay a new stream/recomputation, retain a fuller
descriptor, or supply a separate update/query theorem. It may not
pretend the future cuts were known or reuse an unperformed scan.
Changing N,u,A,v or the local predicate invalidates these shared ranks;
even same-instance amortization is limited to the actual declared
batch. Rank-only does not certify integer squares or proper factors,
nor does it imply a cheaper full survivor traversal.

## 6. Preservation, finite outcomes and next boundary

This is a typed static arithmetic observer/readout over the fixed
HEARTBEAT_WORLD_NATIVE_X6 basis. Retain the native-state/provenance
object carrying (N,c0,u,v,A, exact product relation, proved local
predicate, query batch) and the exact arithmetic readout bridge above.
CRT/carry/rank labels are typed state, not extra spatial axes or full
Cell addresses. The compression removes only materialization of a
specified second list for this declared batch; exact predicate
evaluation and joint translated cuts supply an observer-preservation
certificate. It neither identifies native states by equal counts nor
deletes composite/background directions from future operations.
No explicit time is needed for these static queries; online evolution
or retained query histories would require their own separately typed
scope.

This closes the bounded existence/correctness/paid-memory question for
an offline batch on one actual saved prime extension. It does not
reopen a completed formal Task or refute the inherited complete-list
obstruction, whose required complete second-list premise is explicitly
omitted. It does not establish the same contract for a composite next
group, select with adaptive cuts, unknown online queries, coupled
payloads or Hart's nonlinear candidates.

The next discriminating mathematical question is a declared workload
under which total construction plus queries is *provably* smaller than
the best matched alternative, or an honest conclusion that only space
is saved. A candidate fails this test if it needs an unstored cut at
zero cost, stores Q*r tags while claiming (4), treats chi as an oracle,
omits large-N/root/prime/A construction, substitutes the wrong sorted
coordinate, or calls equal rank answers factor certification. No
repetition of old Hart samples is needed to decide these contracts.

Status: exact paper contract, independent review pending; no scientific
execution, Native acceptance, factoring gain or parent completion.

Researcher-ID: EM-CRTJC-5F30D8A2 / TASK_RESEARCH

````

````text
# Erratum: residue width in the offline-batch comparator

2026-10-14. Author `EM-CRTJC-5F30D8A2`, local agent
`/root/crt_joint_carry`, activity `RA-CRT-JOINT-CARRY-20261014-A1`.
Original owner `EM-DIRECT-FB83AB` and every formal Task/claim/epoch
remain unchanged. This is an exact scope correction, not new research
execution or a withdrawal of the batch algorithm.

## Published version and correction boundary

Root reports a successful Source create acknowledgement for
`awdawmip/enterprise-math` commit
`b15092db5c03132c25f3b43946ee5d8cc629a2e1`, path
`research_notes/OWNER_PARALLEL_CM24_CRT_AND_MCP_REPAIR_20261014_FBF223.json`.
Its archived original batch paper is
`ACTUAL_SHIFTED_SQUARE_OFFLINE_BATCH_RANK_PAID_CONTRACT.md`,
15603 bytes, SHA256
`85fd53dc8aadd06ce6e91afdd9c204466e23a0ff0add9e187d23e24600bb0f98`;
the original review is
`CRT_OFFLINE_BATCH_PAID_CONTRACT_NONAUTHOR_REVIEW.md`,
8229 bytes, SHA256
`720c362e65578d83aab0bd8e01c31ff2bb0c21bf1c0af7f13c2521ef910449f6`.
Root subsequently completed full cold custody verification, recorded
in `publication/SOURCE_IMMUTABLE_FULL_READBACK_ACTUAL.json` and
`publication/SOURCE_FULL_COLD_VERIFICATION.json` under
`/workspace/em-research-continuation-20261014/`. This verifies the
published bytes, not the old width comparison. The Source create and
archived versions must be preserved as history; the present paper
does not pretend that the old text was never published.

This erratum supersedes only the old paper's section 5 assertion that
the ordinary explicit second list unconditionally occupies Theta(vB)
bits, its unqualified J+Q=o(v) sufficient saving condition, and the
same assertions endorsed in section 4 of that original review.
It does not retract the actual-predicate dictionary, CRT/carry paper,
CM24 artifacts, MCP repair evidence or any other capsule member.

## Correct statement

The bit parameter B in the algorithm is deliberately at least the
largest input/query arithmetic width, including N and L. It may greatly
exceed log(M). A comparator does not have to store each residue with
all of those B bits.

For the declared *explicit fixed-width residue-list* comparator,
the complete canonical local B_v list uses Theta(v*log(v)) bits and
its complete CRT-weighted list uses Theta(v*log(M)) bits, since the
zero-inclusive survivor count is Theta(v). A comparator using uniform
B-bit slots instead has Theta(vB) storage. That is a chosen layout,
not a lower bound for every width-aware or compressed representation.

Our previously proved rank-phase upper bound remains

    O((r+J+Q+1)*B)

including common A and batch inputs/answers, plus actual certificate
and provenance storage. For the additional-storage comparison choose
the algorithm's already permitted uncached-shift configuration, so
optional r cached shifts are not silently free. Their recomputation
fits the existing QrB^2 work allowance. Holding common A/provenance
costs fixed, a
sufficient condition under this bound for the extra batch/cut storage
to be o(v*log(M)) is

    (J+Q+1)*B=o(v*log(M)).

For example B=O(log(M)), bounded r,Q and growing v satisfy this
condition, because J<=r(Q+1). The weaker J+Q=o(v) is sufficient only
against the explicitly selected uniform B-bit-slot comparator, or
with a further width relationship such as B=O(log(M)); it is not an
unconditional consequence of the old bound. No smaller whole-instance
peak is inferred when common A construction or certificate workspace
dominates. No claim about optimally compressed lists is introduced.

## What remains valid and exact replacement

The correction changes no row identity, finite cutpoint bound, endpoint
or algorithm: J<=min(v-1,r(Q+1)), the dynamic distinct-key tree,
no-Q*r-tag two-pass realization, integer half-open row wrap, one paid
predicate stream and exact answers remain as proved. The paid work
upper bound

    C_A+P_v+O((j_max+1)*B^3+QrB^2)

and the rank-phase workspace upper bound are unchanged. The method
still establishes an offline representation-versus-recomputation
tradeoff, with no measured or strict total-work advantage and no
factoring completion. There was no old-code/sample rerun for this
correction.

The corrected complete batch paper is 16070 bytes, SHA256
`4bcb16298f2e39bb4db24bd4fab3b57f342ac4b38fdeaada49cd7108015f5eb2`,
Git blob `d8903e93f01aa257c9cfb4196589518c01a6f2dd`.
Its replacement nonauthor review is separately byte-pinned in the
updated delivery manifest. That review acknowledges and corrects its
old overbroad comparator-width endorsement; no new Native acceptance
is asserted.

Root will publish only this correction, corrected paper/review and
their bounded provenance as a small incremental Source. It need not
republish the old capsule's entire collection. Both Source generations
remain necessary provenance for reading this result accurately.

Researcher-ID: EM-CRTJC-5F30D8A2 / TASK_RESEARCH

````

</details>

## NT-SUP-GAUSSIAN-WEDGE160

五port Gaussian-square transfer与160层infinite-m wedge

author-only精确transfer及有限y/无限m的computer-assisted claim，与190有限序列证据、非real-rooted falsifier和未Source公开大证书分列。

状态：`AUTHOR_SYMBOLIC_AND_COMPUTER_ASSISTED_CLAIM_UNREVIEWED_NOT_ADMITTED`。

原贡献与归属：原author-only portable contributor；本文无已认证native researcher身份，不由curator补造作者ID。

Source：[research_notes/author_support/20261014_five_port_gaussian_square_fixed_modulus_wedge.md](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/author_support/20261014_five_port_gaussian_square_fixed_modulus_wedge.md)。

- G_(x,y)(q)=[X^xY^y]∏_(w0..4)(1−Xq^w−Yq^(2w))^−1；m=x+2y+5 odd≥23,x≥0 even，Δ=H_(m−10)−H_(m−19)。
- h_j=[j+4 choose4]_q,b_(j,s)=[q^s]h_j²，K_(m,j)=Σ_k(b_(j,4j+km)−b_(j,4j−9+km))；W(N,0)=1,W(N,k)=N/k·binom(N−k−1,k−1)。
- Δ_(m−5−2y,y)=Σ_(j0..y)(−1)^jW(m−5−2j,y−j)K_(m,j)，全部odd m≥23,0≤y≤(m−5)/2。
- m>4y+9时alias-free为degree-y P_y(m),leading1/y!；κ0..5=(1,5,29,109,312,728)。y0..3为1,m−10,(m²−23m+168)/2,(m³−39m²+614m−3720)/6。
- author computer-assisted claim：1≤y≤160,odd m≥4y+11时Δ_(m−5−2y,y)>Δ_(m−3−2y,y−1)。B=4y+11,t=(m−B)/2,Q_y(t)=Σ_k C_(y,k)binom(t,k)，声明13040 C全部>0且C_(y,y)=2^y。
- SOURCE_REPORTED_AUTHOR_ONLY corollary：所有odd m≥23首六fixed-m residual y0..5严格增加；m≥31用wedge，m23/25/27/29以原positive-mass cyclic recurrence作例外处理（本次不重算，大证书gap保留）。
- odd m23..39 fixed-m D_m非real-rooted：必要Newton inequality差m²−43m+140<0。finite190序列positivity/unimodality/logconcavity不是全m/y定理。

前提：五labeled ports有限ordered words与positive integer multiplicities；cyclic histogram仅为声明observer，保留aliases及来源。

边界：wedge只finite y≤160且m≥4y+11；folded region和y>160未分类，不能无限y升级。；full Newton证书1177341B SHA78432b…在原文明确not yet Source-published；本次未取得/验证，声明保留author computer-assisted证据等级。；无formal CLAIM/Driver/Task Result或native X6 transport。

来源缺口：full Newton certificate与reproducer仅原文所称分开发送conversation package，未获当前Source证据；不声称完整机器证书已读/重验。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Author-only five-port BRC: exact Gaussian-square transfer and a 160-layer infinite wedge

Date: 2026-10-14 Asia/Shanghai.
Status: AUTHOR_SYMBOLIC_DERIVATION / AUTHOR_EXACT_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
This is **not** a canonical Task Result, CLAIM, Driver acceptance, P000 amendment or native X6 theorem. Native service em_status returned BACKEND_IDENTITY_CHECK_UNAVAILABLE (operation_sent=false); no active owner was authenticated by this author.

Source controls: GLOBAL_KNOWLEDGE_V1 main@91edc5638207c8851a9774206034890d54444492; Enterprise Math main@cc07006d61f879395dd247a37ed88d17d4ae8fd0.
Earlier formal five-port residual work is historically author-only, NOT assumed independently admitted.

## Exact typed model

Five labeled ports w=0,...,4 independently carry finite ordered words in X (weight q^w) and Y (weight q^(2w)), preserving positive integer multiplicities.

G_(x,y)(q)=[X^x Y^y] product_(w=0)^4 (1-X q^w-Y q^(2w))^(-1).

For x>=0 even, y>=0 and odd m=x+2y+5>=23, H_r is the exact coefficient mass in exponent class r mod m, and Delta_(x,y)=H_(m-10)-H_(m-19). The cyclic histogram is the declared observer; no identification of distinct future-sensitive provenance is asserted.

Let h_j(q)=[j+4 choose 4]_q and b_(j,s)=[q^s] h_j(q)^2 (outside degree range set to zero).
Let K_(m,j)=sum_(k in Z)(b_(j,4j+km)-b_(j,4j-9+km)).
Let W(N,0)=1 and W(N,k)= (N/k) binom(N-k-1,k-1) for N>=2k, k>=1.

For ALL odd m>=23 and 0<=y<=(m-5)/2, an exact folded/unfolded identity holds:

Delta_(m-5-2y,y)= sum_(j=0)^y (-1)^j W(m-5-2j,y-j) K_(m,j).            (T)

Proof: With n=m-5, the charge n generating product factors via formal alpha,beta solving alpha+beta=1, alpha beta=-z. Put alpha=(1+sqrt(1+4z))/2, beta=-z/alpha. Lagrange inversion gives [z^k]alpha^N=W(N,k), so coefficient extraction yields
G_(n-2y,y)=sum_(j=0)^y (-1)^j W(n-2j,y-j) h_(n-j) h_j.
For any m-th root zeta of order>=5,
h_(m-5-j)(zeta)=zeta^(-4j-10) h_j(zeta).
At roots of order 1 or 3 this equality need not hold, but the contrast filter zeta^10-zeta^19 vanishes. Since m is odd no order 2 or 4 is relevant. Apply the discrete Fourier cyclic contrast exactly, yielding (T). The K sum explicitly retains every cyclic alias. All calculations are integer/rational exact; no physical phase or classical propagation is inferred.

For m>4y+9, all K_(m,j) (j<=y) are alias-free constants kappa_j; hence Delta_(m-5-2y,y)=P_y(m) is a degree-y rational polynomial with leading coefficient 1/y!. First kappa values j=0,..,5 are (1,5,29,109,312,728).
First fixed-m edge values for ALL odd m>=23:
y=0: 1;
y=1: m-10;
y=2: (m^2-23m+168)/2;
y=3: (m^3-39m^2+614m-3720)/6.

## Infinite in m, finite in y: exact Newton certificate

**Theorem (author computer-assisted):** for every integer 1<=y<=160 and every odd m>=4y+11,
Delta_(m-5-2y,y) > Delta_(m-3-2y,y-1).
For each y set B=4y+11, t=(m-B)/2>=0, Q_y(t)=P_y(B+2t)-P_(y-1)(B+2t). This polynomial has degree y and exact Newton expansion
Q_y(t)=sum_(k=0)^y C_(y,k) binom(t,k), C_(y,k)=Delta_t^k Q_y(0).
The exact verifier computes all 13,040 C_(y,k) from the finite y+1 original polynomial values for each y, and checks strictly positive every coefficient, including the independently expected top coefficient C_(y,y)=2^y. Therefore Q_y(t)>0 for all integer t>=0, **without bounding m**. No theorem asserted for y>160 or the folded region m<4y+11.
Certificate: fixed_modulus_wedge_positive_newton_certificate.json, 1,177,341 bytes, SHA256=78432b1c4fc73d9b79735063aec0b1c2e184399197c9022fd2ea0fbfdd43d802; reproducer verify_fixed_modulus_wedge.py (kept in separately delivered author research package, **not yet Source-published**).

Corollary for all odd m>=23: the first six fixed-m residuals indexed y=0,...,5 are strictly increasing; use theorem for m>=31 and exact original positive-mass cyclic recurrence for four exceptional m=23,25,27,29.

## Independent finite evidence and falsifier

The Gaussian-square transfer was evaluated for 190 full odd modulus sequences m=23..401, all strictly positive/unimodal/log-concave; ALL 20 inherited 23..61 sequences matched entry by entry; 85 independent original ordered-port cyclic-path examples passed positive-mass checks. These finite observations are **not** universal theorems.

For each odd m=23,25,...,39, the fixed-m residual generating polynomial D_m(z)=sum_y Delta_(m-5-2y,y) z^y is NOT real-rooted: its true degree d=(m-5)/2 is certified independently by positive top-degree counts 16,20,27,35,43,53,65,77,92, while necessary Newton normalized coefficient inequality fails because
(m-10)^2(m-7)-(m-5)(m^2-23m+168)=m^2-43m+140<0.
This eliminates universal real-rootedness as the mechanism for strict unimodality.

## Provenance, exact limits, continuation

Local reproducible original proofs, script, and decimal certificates (including a full 190-sequence certificate) are bundled with this turn's research package. This GitHub note preserves a human-comprehensible author-only frontier, **not** the 1.18 MB full Newton certificate. Files and Source are not conflated. No activity record, native session, CLAIM, frozen Result or independent Driver review is implied.

Next: derive a UNIFORM in y positive Newton transfer or exact coefficient injection, especially across the folded region m<4y+11; otherwise find a first counterexample to universal strict unimodality/positive contrast. Do not repeat the already falsified real-rootedness route. Preserve BRC labeled-port mass/provenance; no native six-axis/time transport is known.

````

</details>

## NT-SUP-J1-R61-64

J1输入重数恒等式及r61–64四个有限square-witness前沿

经典finite-field input-count恒等式与四个作者报告的奇数size整数square witnesses分列；不是output-set大小、无限r结论或已完成prior-art audit。

状态：`UNCLAIMED_SUPPORTING_RESEARCH_UNREVIEWED_NOT_ADMITTED`。

原贡献与归属：原research2 supporting conversation；UNCLAIMED/UNREVIEWED，未取得formal owner身份。

Source：[research_notes/directed_recovery/20261011_J1_r61_r64_unreviewed_support.md](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/directed_recovery/20261011_J1_r61_r64_unreviewed_support.md)。

- q odd prime,s≥3 odd,k=(q−s)/2≥1，Λ_s(a)=−sa−(2a)^−1，J_s={−(s−1)/2,…,(s−1)/2}；E为输入a∈F_q*落在J_s外的重数。
- E(q,k)=2Σ_(i0..k−1)(1+χ_q((2i+1)²+16k))。
- r61/62/63/64，k2^r；报告odd witness counts913/1035/1131/1365，maxj693731/882899/921969/1180399，max divisor19483/36821/44683/80669，T digits8933/10282/11406/13971。
- 若所报告distinct I_r、proper divisor bounds<q_min=2k+3、∏N_j=T²完整见证成立，则对全部allowed q≥q_min有非零Legendre odd product+1，从而E(q,2^r)≥4。

前提：每N_j有实际整数square-product和q非整除证书；原文声明其生成并曾独立本地验证，当前正文未携带完整见证。

边界：r5..60历史重跑仅原文报告，本文不重跑/不计新证据；17≤k≤2^64的扩展还条件依赖此前non-power-of-two theorem。；完整certificate与ZIP原文明确未声称在Git repo；不把摘要计数代替正文全证书。；prior-art只bounded abstracts，不能宣告novelty或J1六行完整外审完成。

来源缺口：r61–64 full machine certificate SHA f4d79e…及portable ZIP8d2a94…仅原文引用conversation artifacts；本次未取得完整payload。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# J1 finite-field auxiliary research: r=61..64 exact square certificates

Status: UNCLAIMED_SUPPORTING_RESEARCH / UNREVIEWED / NOT_ADMITTED.
Date: 2026-10-11 Asia/Shanghai.
Task context: RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT (TP2-39ACFC69F85D8661CFBF). This independent arithmetic support DOES NOT finish the task's external prior-art audit or replace a native CLAIM/Result/Driver review.
Pinned source: global-knowledge main 7b33f8066e9993e7c941959a9d738ed405248eb8; enterprise-math main 5873e3e48b549cf7a23d310c3c0ea6926943dc6c. P000 six-dimensional native reality remains the project premise; this is a separately typed classical finite-field lemma.

## Exact definitions and proof of the branch formula

Let q be an odd prime, s>=3 odd, k=(q-s)/2>=1, and Lambda_s(a)=-s*a-(2*a)^(-1) mod q for a in F_q^*. Set J_s={-(s-1)/2,...,(s-1)/2} mod q; E(q,k) is the NUMBER OF INPUTS a with Lambda_s(a) outside J_s, counting all multiplicities.

For any output b, the equation 2s*a^2+2b*a+1=0 has 1+chi_q(b^2-2s) roots. The exterior outputs form k pairs +/-b_j, b_j=(s+1)/2+j (0<=j<k). With i=k-1-j, 4(b_j^2-2s)=(2i+1)^2+16k mod q. Thus, exactly,
E(q,k)=2*sum_{i=0}^{k-1} (1+chi_q((2i+1)^2+16k)).
This is a branch-count observer, not merely the size of the output set.

## Four new exact integer witnesses

For each r=61,62,63,64 set k=2^r, N_j=(2j+1)^2+16k, q_min=2k+3. A separate machine-readable certificate supplies odd-size distinct index lists I_r, exact proper divisor witnesses 0<d_j<N_j with 0<d_j,N_j/d_j<q_min, and exact integer T_r with product_{j in I_r} N_j=T_r^2.

r=61: count 913, max j 693731, max divisor 19483, T decimal digits 8933.
r=62: count 1035, max j 882899, max divisor 36821, T decimal digits 10282.
r=63: count 1131, max j 921969, max divisor 44683, T decimal digits 11406.
r=64: count 1365, max j 1180399, max divisor 80669, T decimal digits 13971.

For every allowed prime q>=q_min, none of the N_j is divisible by q. The Legendre product of an odd number of nonzero N_j equals +1 because their integer product is a square; hence not all individual Legendre symbols can be -1. A +1 contributes 4 to E. Therefore E(q,2^r)>=4 for all allowed q and r=61..64.

The original full certificate, standalone standard-library verifier, proof report, search code/logs, earlier verified archive and SHA256 manifest have been generated together as EM_R2_J1_r61_r64_portable_bundle.zip in the conversation holding this support contribution. Full certificate SHA256: f4d79e8cb9d480b71a6b8f111e4271d1d58c0abb74be98812355657fa16398c1. Portable ZIP SHA256: 8d2a94c2fb18e823722e688e4e4408a40c630cf064087e3e33942f5bc1cbcb15. These referenced conversation artifacts are NOT asserted to reside in this Git repository.

Local independent verification: 4/4 newly constructed exact square witnesses PASS; historical r=5..50 archive rerun 46/46 PASS and r=51..60 10/10 PASS. If the inherited separately established non-power-of-two theorem is accepted, the finite interval exclusion now extends to 17<=k<=2^64. NO infinite-r statement follows.

Bounded abstract-level prior-art sampling: O. Kucuksakalli (2014), Value sets of Lattes maps over finite fields, DOI 10.1016/j.jnt.2014.04.014; D. R. Heath-Brown (2016), Small solutions of quadratic congruences..., DOI 10.1112/S0025579315000364; T. W. Cusick (1998), Value Sets of Some Polynomials..., DOI 10.1137/S0097539794270352. No exact symmetric-consecutive-residue containment statement was established from these limited abstracts; this is NOT a novelty finding or complete full-text audit. The already Source-documented generic x+alpha/x image-cardinality antecedent remains in place.

Pending: deposit all complete machine certificates to the authorized research artifact destination and independent review; current native session_start was refused STATIC_READONLY_SCOPE_DENIED (operation not sent). Task live Source was HANDOFF_READY / NEEDS_DISPATCH, NO_LIVE_CLAIM; this document creates no formal ownership. The next mathematical unit is r=65 and/or a uniform r proof, with full J1 interval-containment source comparison still independently required.

````

</details>

## NT-SUP-J1-MOD3-PELL

J1 r≡1mod3的parity-steered Pell triple量化界

从三个squarefree kernel的odd Pell norm解给特定模3指数子族的多个disjoint triple；全文是未审support，不接管live owner或正式外审。

状态：`UNREVIEWED_NOT_ADMITTED_NO_NATIVE_CLAIM`。

原贡献与归属：原ChatGPT scheduled researcher2，support无native claim；原live owner EM-NATIVE-79EB13未被接管。

Source：[research_notes/directed_recovery/20261011_R2_J1_MOD3_PELL_1741697_UNREVIEWED_SUPPORT.md](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/directed_recovery/20261011_R2_J1_MOD3_PELL_1741697_UNREVIEWED_SUPPORT.md)。

- r≥34,r≡1mod3,k=2^r,q odd prime≥2k+3,U69698；m(r)=max({0}∪{m≥1:U^(2m)<2^r})，E(q,2^r)≥4m(r)。
- r0=10 seeds(d,x,y)=(17,83,37),(41,529,85),(697,1923,73)，norm−2^14；multipliers(5,1)/2,(7,1)/2,(27,1)/2有norm2,2,8。
- norm-one units33+8√17,2049+320√41,34849+1320√697均<u bound69698；各triple product=(697 y17 y41 y697)²，j=(x−1)/2∈[0,k)。
- even r≡4mod6从34起；r70/100/130/196给E≥8/12/16/24。不能升级至全部r。

前提：保留parity-safe正/负multiplier选择、unit normalization、odd positive x/y、不同h与不同kernel的distinctness、对所有allowed prime的nonvanishing。

边界：75 exponent decimal certificate在本repo当前可得，本文仅静态读取metadata/seed/range及引文，不执行其scientific verifier或重新检查300triples。；没有r10+3t在34以下的统一legal-j主张；其它even mod6类仍是未来研究。；Legendre signs为detector states，不作负BRC质量或nativeforce。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# J1 neutral supporting research — mod-3 parity-steered Pell triple (2026-10-11)

Status: UNREVIEWED / NOT_ADMITTED. Author: ChatGPT scheduled researcher2, separate supporting research without a native claim. This is NOT the live owner's formal Result, research activity registration, Driver review, or an original six-dimensional Cell theorem.

GLOBAL_KNOWLEDGE_V1 snapshot: awdawmip/chatgpt-global-knowledge@49017179c37e3ca29ae78fccdce206a08d004574 (P000 ACTIVE, checked).
EM Source snapshot at proof construction: awdawmip/enterprise-math@410647cefb6872123fe829748aaa5224dbb23fca.
Formal task: RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT / TP2-0B9541A191FE5231A19B. Its 2026-10-11T09:17Z continuation reported LEASED/IN_PROGRESS with another active owner, EM-NATIVE-79EB13, and a six-row prior-art checkpoint pending formal Result freeze; no ownership was requested, taken, or displaced.

## New exact theorem

For k=2^r, r>=34 with r≡1 (mod 3), and any odd prime q>=2k+3, put N_j=(2j+1)^2+16k (0<=j<k), and U=69698, m(r)=max({0} union {m>=1:U^(2m)<2^r}). There are m(r) pairwise disjoint triples of indices, each having squarefree kernels d=17,41,697=17*41, with integer square product and with no N_j divisible by q. Thus for the previously established classical original-input count identity E(q,k)=2 sum_j(1+chi_q(N_j)), one gets E(q,2^r)>=4m(r), with chi_q(0)=0. In particular the new *even* r≡4 mod6 subfamily begins at r=34 and gives r=70 E>=8, r=100 E>=12, r=130 E>=16, r=196 E>=24 for all allowed primes. No all-r upgrade to the old theorem is claimed.

## Exact proof data

At r0=10 the three odd seed pairs (d,x,y)=(17,83,37),(41,529,85),(697,1923,73) satisfy x²-d*y²=-2^14. Their norm multipliers beta=(a+b sqrt(d))/2 are (5,1) at d17 of norm 2; (7,1) at d41 of norm 2; (27,1) at d697 of norm 8. For odd x,y,a,b,d≡1 mod4, among epsilon=+1,-1 exactly one makes both (a*x+epsilon*d*b*y)/2 and (epsilon*b*x+a*y)/2 odd integers; this follows because the two x numerators differ by 2 mod4, and the x/y numerators differ by (a-epsilon*b)(x-y)≡0 mod4. Taking absolute values gives positive odd norm solutions; after 3t steps in d17/d41 and t steps in d697 the norm equals -2^(14+3t).

The positive integral norm-one units u17=33+8sqrt(17), u41=2049+320sqrt(41), u697=34849+1320sqrt(697), all have odd A/even B and satisfy u_d<2A_d<=69698. An integral unit power normalizes each solution alpha=x+y sqrt(d) into sqrt(D)<alpha0<=u_d sqrt(D), D=2^(r+4). For h=0,...,m(r)-1, alpha_h=alpha0 u_d^h yields odd positive x,y with x< U^m*2^(r/2+1)<2^(r+1), so j=(x-1)/2 lies in [0,k). Different h give increasing x, different d give distinct squarefree kernels. Each triple product is (697*y17*y41*y697)^2. As N_j< (2k+3)^2<=q² and d<q, y<q, no selected factor vanishes mod q. The three ±1 Legendre symbols have product +1, hence at least one +1 per disjoint triple, giving E>=4m.

The initial legal r=10 seed indices are j=(41,264,961). One higher even case at r=34 has (d,x,j)=(17,2750717,1375358),(41,1784591,892295),(697,7134747291,3567373645). This proof does NOT assert the fixed unit orbits give legal j at every r=10+3t below 34.

## Executed reproducibility

The full local proof/checker/evidence package (artifact names to be transported separately) has checks: 3 exact seeds/norm multipliers/units, 16/16 parity-steering mod4 configurations, all 75 exponents r=34,37,...,256 and 300 mutually disjoint integer-square triples with exact j/x/y in decimal certificate, direct original finite-field mapping equal to E character formula for k=1024,q=2053 (E=2046) and q=2063 (E=2052). Source data digest SHA256=007fcc49cf894b5ed8977bf0492ed8be7209f92954a1152de39c0330dfcc3091. Full report digest SHA256=0502f97dfd16707dcea63392b3d63d18c40a47cf2ff6583a8548a9971c189eb8. The digests identify LOCAL scientific files; they are not claims that those files are separately committed in GitHub.

BRC application: original finite-field input labels, positive counted exterior branches, j/d/x/y provenance and valuation/squarefree-kernel distinction are retained. Legendre signs are detector states, NOT cancellations of positive branch mass. No native X6 transport is inferred.

Next smallest research question: construct low-height simultaneous odd Pell norm solutions for even r≡0,2 mod6, with parity-safe signed multipliers, or reduce U; then seek a quantitative E bound uniform across all dyadic exponents. Independent mathematical audit of parity steering, normalization, and uniform q-nonvanishing is required before promotion. Formal J1 six-row prior-art comparison is distinct and should not be repeated.
````

</details>

## NT-SUP-ADAPTIVE-THIRD

adaptive primitive lattice第三congruence：保留未审checkpoint边界

这份短checkpoint只保存reported frontier与下一求和缺口；不能由条目名或七行声明补造完整证明/变量语义。

状态：`UNREVIEWED_NOT_ADMITTED_NOT_FORMAL_REVIEW_REPORTED_FRONTIER_ONLY`。

原贡献与归属：EM-DVR-A5A686，原activity RA-EMDVR-A5A686-20260929T202932；portable checkpoint非formal review。

Source：[research_notes/portable_driver/20261001_0903_adaptive_primitive_lattice_third_congruence.md](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/portable_driver/20261001_0903_adaptive_primitive_lattice_third_congruence.md)。

- reported：index-I rank-two lattice在H-box的ambient-primitive vectors O(1+H²/I)。
- reported：selected-divisor tuples D≤H²在natural volume闭合；x=161/720,y=1/3 tilt给candidate H^(2+1/240−o(1))。
- σ=79/720,D>H²且q_(3)≤H^(1/25)的contribution H^(2−17/9000+o(1))；pair-only adaptive ceiling2/49。
- remaining carrier D>H²,q_(3)>H^(1/25),q_(1)q_(2)q_(3)>H^(6/7)。
- reported third congruence after O_7(1) core stripping：fixed-leader cofactor count O_7(H²/(Q1Q2Q3)+H/Q2)。下一步仍需保留4 follower constraints求和H/Q2边界。

前提：仅原文checkpoint给出的外部integer/lattice接口；H,D,q_i,Q_i等完整定义、常数uniformity及证明未在此短稿展开。

边界：原始science Source head为月前baseline，Oct1 portable保存；属于本月文献前沿，不冒称十月新正式证明。；保留UNREVIEWED/NOT_ADMITTED/NOT_FORMAL_REVIEW；没有完整proof source时不能升级成已核验一般定理或已完成目标。

来源缺口：仅1161B portable checkpoint；完整假设与proof source在此包未恢复，本文只提取reported statements及精确remaining carrier。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Portable Driver checkpoint — adaptive primitive lattice / third congruence

Status: UNREVIEWED / NOT_ADMITTED / NOT_FORMAL_REVIEW

Source heads:
- enterprise-math: ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec
- GLOBAL_KNOWLEDGE: 8c863c7ec308cfc74dc325af21e41da24d0f10a7

Driver: EM-DVR-A5A686
Activity: RA-EMDVR-A5A686-20260929T202932

New portable frontier:
1. Primitive lattice theorem: index-I rank-two lattice has O(1+H^2/I) ambient-primitive vectors in an H-box.
2. Therefore all selected-divisor tuples with D<=H^2 are closed at natural volume.
3. Adaptive top-three/follower tilt x=161/720, y=1/3 gives candidate amplification H^(2+1/240-o(1)).
4. With sigma=79/720, D>H^2 and q_(3)<=H^(1/25) contributes H^(2-17/9000+o(1)).
5. Pair-only adaptive architecture ceiling is 2/49.
6. Remaining carrier: D>H^2, q_(3)>H^(1/25), q_(1)q_(2)q_(3)>H^(6/7).
7. Exact third congruence after O_7(1) core stripping gives fixed-leader cofactor count O_7(H^2/(Q1Q2Q3)+H/Q2).

Next:
EM_PRIME_COVER_AP_K3_THIRD_CONGRUENCE_BOUNDARY_V1 — sum the H/Q2 cofactor-box boundary while retaining all four follower divisibility constraints.

No formal review/admission is claimed.
````

</details>

## NT-SUP-RSA-DYADIC

公开collision transcript的确定性dyadic membership-or-factor与thin-subgroup反例

已有graph-of-isomorphism barrier在给定有效碰撞清单下被算法化：逐bit membership要么给nontrivial root/gcd，要么给公开cyclic graph certificate。不是从n生成collisions，也不是global factoring改进。

状态：`EXISTING_LOCAL_NONAUTHOR_PAPER_PASS_AFTER_PRECISION_CORRECTIONS_NOT_NATIVE_ACCEPTANCE`。

原贡献与归属：原helper native identity UNKNOWN、DIRECTED_NONBLIND；reviewer/subreviewer亦UNKNOWN。前驱author EM-RSACOL-C76042与historical reviewer EM-DVR-FBF223不等于本新算法全部作者。

Source：[driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/a1fe1386f89e55f14bec/RSA_TOOLS_COMPLETE_ORIGINALS_CAPSULE.json](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/a1fe1386f89e55f14bec/RSA_TOOLS_COMPLETE_ORIGINALS_CAPSULE.json)。

原capsule成员：`theorem-tool-harvest-round-20261012/RSA_DYADIC_MEMBERSHIP_DERIVATION.md`；此成员路径是归档标签，不能伪装成独立GitHub路径。

- n=pq,distinct odd primes；有效非空unit certificates(x_i,Δ_i),Δ_i>0,x_i^Δ_i=1；L=lcmΔ_i=2^s u,u odd,y_i=x_i^u生成H₂。
- 逐square找最大depth supplied g=y_j，若任何pre-1 root不是±1即split；否则g有两CRT侧共同order2^t、half-power−1。
- 对h逐bit保持z=hg^−e,0≤e<2^k,z^(2^(t−k))=1。w=z^(2^(t−k−1))；非±1给proper gcd，否则b=0/1更新e←e+b2^k,z←zg^(−b2^k)。全部通过得h=g^e。
- 输出graph iff H₂是两cyclic projection subgroups之间isomorphism的graph；否则split iff该collision-driven mechanism存在可分combination。t0需所有y_i=1。
- r条certificate，odd stripping O(r logL)，depth≤rs squarings，bit-core rt(t−1)/2 squarings+rt updates，t>0另1 inversion及t−1 cache squarings（t0均不需要）；prototype断言/复核另加O(rt²)。literal O(r(logL+s+t²)) modular operations加lcm与验证。
- m=bitlen n,b=max(1,bitlen L)，complete conservative bitcost O((rb+rs+rt²+t)M(m)+(r+1)m³+rb³)，另计noncanonical整数读取/reduction；auxiliarycertificate O(rt+r+log(t+1))bits。
- t≥2,H_t={(a,b)∈C_(2^t)²:a≡b mod2^(t−1)}，size2^(t+1)，non-graph但uniform subgroup split probability恰2^−t；独立uniform coefficient residues mod2^t同law，短/偏置系数不自动如此。
- 历史固定n1649,x105/768,Δ16：root290,gcd17；两new n221审查fixtures仅按源记录，不重跑。

前提：semiprime premise作为假设，不由membership verifier证明；有效非空碰撞由外部供应，factor和local orders不提供给算法。；public graph verifier重查collisions/L/u/base/half-power及全部memberships；proper factor必须1<d<n，gcd(n,0)=n不算success。

边界：独立review为UNKNOWN identity / DIRECTED_NONBLIND的local paper PASS，经V2 empty-domain guard及core-vs-assertion cost澄清，不是Native ACCEPTED。；pow2 discrete-log digit lifting与Pohlig–Hellman机制关系明示，未新取prior art或声称外部novelty。；uniform subgroup概率2^−t不反驳旧完整CRT unit-group的≥1/2 law；新算法不提供collision-generation。；原八个negative checks、七fixtures、五tinygroups及review两newfixtures均历史报告，不复跑旧checker/census/T6科学。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Supplied RSA collisions: deterministic dyadic membership or factor

Status: NEW BOUNDED LOCAL DERIVATION AND PROTOTYPE, awaiting Root mathematical
review and possible Source custody. This helper's native identity is UNKNOWN;
exposure is directed/nonblind. No native Task, Claim, Run, accepted Result,
Source publication or global factoring claim is created by this unit.

The antecedent RSA return already proves the exact multi-certificate
graph-of-isomorphism barrier and safe lcm aggregation. Its Source is
5591703654d7496a9ce6f3d9a8575e47158b2ae7, return
research_returns/RSA_EXPONENT_COLLISION_CRT_COLLAPSE_RETURN_20260827.md,
SHA256 8fd60e5fd5be25c7fc17a8d142ed75616a0ceec73a89f7d2088f0221aef265b8.
Author EM-RSACOL-C76042; current nonblind review by EM-DVR-FBF223 is preserved.
The new contribution below makes that already-known existential barrier
algorithmic for a supplied transcript. It is a power-of-two discrete-log
membership procedure, related to the classical Pohlig–Hellman mechanism;
there is no external novelty claim and no newly retrieved prior-art evidence.
No such procedure was stated in the exact RSA return/current review consumed
here. The existing bounded prior-art audit should determine antecedent scope.

## Precise conditional theorem

Let n=pq with distinct odd primes. Public input is n and a nonempty list of
unit collision certificates (x_i, Delta_i), with Delta_i>0 and
x_i^Delta_i=1 modulo n. Neither p,q nor any local order is given to the
algorithm. Write L=lcm_i Delta_i=2^s u with u odd and set y_i=x_i^u.
Let H_2 be the Sylow-2 subgroup of <x_i>. There is a deterministic procedure
using only modular multiplication, public exponentiation, inversion and gcd
that returns exactly one of:

1. A nontrivial square root z of 1 modulo n and 1<gcd(z-1,n)<n.
2. A public cyclic-membership certificate: a supplied y_j=g, a depth t, and
   exponents 0<=e_i<2^t such that y_i=g^e_i; when t>0,
   g^(2^(t-1))=-1 modulo n, and when t=0, every y_i=1.

It returns the second outcome if and only if H_2 is a graph of an isomorphism
between its two cyclic CRT projection subgroups. Thus the procedure splits
if and only if the existing RSA mechanism is able to split some combination.
This supplies an efficient conditional extraction procedure, not a procedure
to produce any collision certificate from n alone.

## Why the public y_i generate exactly H_2

Every generator order divides Delta_i and therefore L. On the odd-order
component of H, exponentiation by u is zero because the odd component's
exponent divides u. On H_2, exponentiation by the odd u is an automorphism.
Hence <y_i>=H_2 and all y_i have orders dividing 2^s. This stays true when
the supplied Delta_i have redundant odd or even factors.

## Stage 1: choose a maximum-order generator

Repeatedly square each y_i until the first 1, at most s steps, recording its
exact global depth t_i. If the state immediately before that first 1 is
neither 1 nor -1, return its nontrivial CRT square root and proper gcd.
Otherwise every nonidentity y_i has the pre-1 state -1. For proof-side CRT
coordinates this means both local orders of y_i are exactly 2^t_i.

If every y_i=1, certify the trivial graph. Otherwise choose g=y_j with
t=max_i t_i. Then g has order 2^t in both CRT projections and
g^(2^(t-1))=-1 globally. All other y_i have orders at most 2^t.

## Stage 2: solve membership a bit at a time

For each h=y_i, begin with z=h and e=0. At step k=0,...,t-1 maintain

    z=h g^(-e), 0<=e<2^k, z^(2^(t-k))=1.

Compute w=z^(2^(t-k-1)), which necessarily satisfies w^2=1. If w is neither
1 nor -1, return it and its proper gcd. If w=1, set bit b_k=0; if w=-1,
set b_k=1. Replace

    e <- e+b_k 2^k,
    z <- z g^(-b_k 2^k).

Since (g^(2^k))^(2^(t-k-1))=-1, the updated z has
z^(2^(t-k-1))=1, proving the next invariant. After all t steps, z=1 and
h=g^e. No CRT coordinate, hidden order or discrete-log oracle was used.

If every membership computation succeeds, H_2=<g>. Both local projections
are injective because g has full local order 2^t on each side, so H_2 is a
graph. Conversely, if H_2 is a graph, every h has equal local order; a
maximum-order supplied generator generates this cyclic group, and every
computed square root must be 1 or -1. The algorithm therefore emits the
graph certificate. A non-graph cannot finish with these valid memberships.

The graph certificate has a short public verifier: recheck every collision,
L and u, the supplied base identity and half-power -1, and every equality
x_i^u=g^e_i. Under the stated semiprime hypothesis these prove the exact
mechanism barrier. The verifier does not certify the hypothesis that n is a
product of two distinct primes and does not claim factoring is impossible.

## Cost and output typing

Let r be the number of supplied certificates. Initial odd stripping needs r
public exponentiations of bit length O(log L). Depth detection uses at most
rs squarings. One modular inversion and t-1 squarings precompute the inverse
digit powers. The core membership tests then use at most r t(t-1)/2
squarings and rt further modular multiplications.
These bounds are polynomial in r, log n and log L; t<=s<=log_2 L. The lcm
and transcript validity checks are also ordinary polynomial integer work.
The displayed counts concern the core procedure. The saved prototype also
retains every invariant exponentiation and final membership recomputation;
those add O(rt^2) modular work. Its literal implementation still uses
O(r(log L+s+t^2)) modular arithmetic operations, plus ordinary lcm work.

The gcd output is accepted only when 1<d<n. In particular gcd(n,0)=n is a
trivial result, just as in the corrected PCF fixed-probe statement. This
branch typing is explicitly present in the prototype and its verifier.
Uniform units in the entire CRT group retain the original success law;
the new procedure does not alter that law.

## New thin-subgroup counterexample to naive random mixing

For t>=2 use additive CRT exponent coordinates C_(2^t) x C_(2^t) and let

    H_t={(a,b):a=b modulo 2^(t-1)}
       =<(1,1),(1,1+2^(t-1))>.

Both displayed generators have equal local depth t and fail individually.
H_t is not a graph: their difference is (0,2^(t-1)), a transverse order-2
element. Nevertheless a uniform element of H_t splits by unequal depths
only in the two cases (0,2^(t-1)) and (2^(t-1),0). All elements with a
nonzero lower bit have the same 2-adic valuation in both coordinates;
the two diagonal high-bit pairs also fail. Since |H_t|=2^(t+1), the exact
conditional random-combination success probability is

    2/2^(t+1)=2^(-t).

Thus non-graph structure alone gives no constant random-combination success
probability. This does not contradict the old >=1/2 law, whose sample is a
uniform unit of the complete CRT group, nor its probability over independent
full-group generators. The dyadic membership algorithm locates the
transverse element without that probability loss.

One new fixed concrete fixture is n=1649=17*97, public x_1=105,x_2=768,
Delta_1=Delta_2=16. Each has equal local depth 4. They generate the t=4 thin
subgroup, so uniform combinations succeed with probability 1/16. The new
membership procedure produces z=290 and gcd(289,1649)=17 at bit 3.
For fixture construction only, the harness uses known factors; extractor
and output verifier receive only n and the public certificates.

## Actual new bounded verification and remaining work

Seven fixed public fixtures pass, including the saved n65 amplification
witness under the new algorithm, the single new n1649 thin subgroup,
redundant annihilators, odd components, positive graph certificates and a
trivial graph. Five tiny abstract H_t examples t=2,...,6 have exact
success fractions 1/4,1/8,1/16,1/32,1/64. Eight negative checks reject
trivial gcd/root results, false exponents/orders and invalid transcripts.
The public verifier explicitly rejects an empty transcript. Separate review
identified this interface precision point and the core-vs-assertion cost
distinction; pre-review V1 code/checker/receipt are preserved under versions.
Seven consumed source originals are unchanged. No old checker, semiprime
census, T6 q3/q4 science, scalar fit or Source/native operation ran.

These are local derivation and regression evidence. Root should consume the
separate mathematical review, compare with the existing RSA prior-art
material/Pohlig–Hellman antecedents, then decide Source integration. Do not
count this as an accepted Task or duplicate the completed RSA census.

````

</details>

## NT-SUP-MATCHED-COST-INTERVAL

有限预算matched调度的选择不可识别及完整总成本区间

两个抽象finite candidate模型在预算内记录相同、complete-case子集同样优势，而预定全体成本方向相反；给有效总成本区间上的稳健证书与selection identity。

状态：`EXISTING_DIRECTED_NONBLIND_LOCAL_NONAUTHOR_PAPER_PASS_NOT_NATIVE_ACCEPTANCE`。

原贡献与归属：原文未列独立署名的本地新推导，Root与drafting agents的shared context按原peer保留；不由本轮curator认领。

Source：[research_notes/ROOT_THREE_PAPER_UNITS_AND_OWNER_NEXT_PLAN_20261014_FBF223.json](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/ROOT_THREE_PAPER_UNITS_AND_OWNER_NEXT_PLAN_20261014_FBF223.json)。

原capsule成员：`/workspace/em-owner-resume-20261011/new-round-20261011/MATH_FRONTIER_LEMMA_20261014.md`；此成员路径是归档标签，不能伪装成独立GitHub路径。

- K24,C升序,P稳定四桶；paid T_P=2+rank_P,T_C=(25/24)rank_C,budget12。等权E成功k5，P3/C125/24；H的P顺序15..24,14,13,1..12。
- A世界H成功14，P13/C175/12；B世界成功12，P26/C25/2；预算可见P十失败12、C十一失败275/24完全相同。全体和差A−91/24，B271/24，sum ratios384/475<0.9与696/425>1。
- 固定正权位置有限proper-return completions及有效0≤L_Mi<∞,L≤U≤∞；D_α=Σw_i(T_Pi−αT_Ci),α>0。
- A_α=Σw_i(L_Pi−αU_Ci)≤D_α≤B_α=Σw_i(U_Pi−αL_Ci)。interval-product信息模型tight，真实coupling模型只safe外界；无限端点按inf/sup，不作∞−∞。
- B_α≤0给robust weak savings,B_α<0 strict,A_α>0相反证书；α0.9是weighted total-cost线性比较，非9round median-of-means+strict-win协议。
- S为pair complete indicator,q=Σw_iS_i∈(0,1),d_i=T_Pi−αT_Ci，则E_w[d|S1]−E_w[d]=Cov_w(d,S)/q。

前提：有限预先指定positions与w≥0,Σw1；先去掉w0项；上下界必须属于同执行/保存/缓存上下文、完整setup/production/consumer/storage/closing只收费一次。

边界：反例是抽象label/bucket模型，不证明真实Hart e_k/buckets能实现两表或同一实际input有不同futures。；record-limit instrumented diagnostic不是unmetered wall-time下界；换保存实现不能回填旧时间。；pair proper-success、有效finite totals与实际剩余工作上下界不能由本引理凭空产生；Unit20 UNKNOWN与原parent OPEN保留。；α百分比/ratio解释另需positive comparator total；底层线性比较不需取比。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# 有限预算下 matched 优先调度的不可识别反例与总成本区间引理

2026-10-14；本地独立推导，供 Owner 选择数学方向。没有生成 N、运行任何旧样本/producer/checker、解析旧 raw、操作 Native 会话或改写原 owner 文件。本文不是正式独立接纳，也不声称 Hart 算法优劣或文献首创。

**已完成的结果：**即使候选域完全相同、consumer 完全相同、优先次序是稳定四桶次序、准备费全部为正且已支付，完整返回子集上的明显优势，也不能确定预定全体输入的总成本方向。下面给出两个预算内观察完全相同、但全体成本方向相反的有限模型，并证明一般总成本差的最紧区间公式。

## 1. 已有覆盖与此次真正的新接口

实读 Unit20 报告：六方法矩阵不完整，优先两法有 record-limit CENSOR；正式 pair 条件要求完整 9×16、proper-return 且无 integrity failure，缺测保持 UNKNOWN [R1，第 3、10–18 行]。Unit21 仅保存机制改进，算法/observer/计时口径未改；八个 priority pair 仍 UNKNOWN，保存费与嵌套计时不能混加 [R2，第 3、7–13 行]。

已有数学覆盖了：固定 priority consumer 前缀不因 producer 变快而改变，以及其条件费用下界 [R3，§“Prefix invariance lemma”]；prefix bucket scan 的无固定幂增益边界 [R4]；同 K 的 120-stride-first 是一个完整排列，而 full classic480 的 120M 域不能冒充同 K [R5，§3、§5–6]。本文不重复这些证明。

对当前证据目录内 86 份去除主要镜像目录的 Markdown 作定向检索，未命中 selection bias / complete-case / partial identification / 选择偏差 / 识别区间等命题，并实读上述最接近的结论。这只是本地 coverage 检查，不是全库或文献优先权证明。

最值得推进的缺口是：**当支付全部成本会改变哪些输入能完成时，怎样从有限记录判定预先指定总体的优势？** 改善保存可能让更多调用进入预算，却不会自动把完整子集上的比较变成全体比较。此问题先于把新增完整调用称为“残差优先优势”。

## 2. 定义：分开目标、观察和模型假设

固定预先指定的有限输入位置 i=1,…,m 及权重 w_i≥0，Σw_i=1。所有求和忽略 w_i=0 的位置，避免 0×∞。位置可以是固定案例；本文不假设随机抽样、均匀 semiprime 分布或独立重复。

P 为优先方法，C 为一个明确命名的强对照。在指定、固定的执行上下文中，T_Pi、T_Ci 是得到 proper return 的完整非负有限总成本。两个方法各自的 setup、生成/筛选、失败、存储/收尾费用均只计一次；共同费用仅在真相同且真支付时抵消。若成功是否存在也未知，不得借本定义直接宣布成功；下面反例特意让所有继续执行都必定有限成功。

每个方法/位置的现有证据只能给出区间

    L_Mi ≤ T_Mi ≤ U_Mi,                 M∈{P,C}.

完整且全部费用已计入时 L=U。相同路径的未完成累计付费通常给下界；若只是 instrumented diagnostic 的记录限额，不能把它当作 unmetered wall-time 下界。跨缓存/保存实现的假想继续执行也不能自动沿用原时间下界。没有合理上界时写 U=+∞，而不是用 budget 代替完整成本。

以下反例使用一个明确的、有限的**抽象候选消费模型**。它保留同域/同 consumer/四桶顺序和全费用，但不要求任意桶与成功位能同时由真实 Hart 的 a_k=ceil√(4Nk)、e_k=a_k²−4Nk 实现。这一限制对结论至关重要：反驳的是从上述一般实验设计条件推导总体优势，不是宣称找到新的整数分解反例。

## 3. 严格反例：相同可见记录，相反总体结论

所有案例均有 K=24 个候选，编号 1,…,24；同一 consumer 只有在唯一 productive 候选处成功。C 按升序，P 按 (bucket,k) 字典序，bucket∈{0,1,2,3}。桶在执行前固定，不由执行结果选择。

用一个正价格账本：生成/保留一个候选的整包费用为 1/24，计算/保留一个桶的整包费用为 1/24；一次完整 consumer、失败/成功及其控制收尾整包费用为 1。P 生成并分类全部 24 个候选，预付 2；C 按需生成，不算无用的桶。这里每个整包已包括该模型规定的全部 bookkeeping，不存在另一个被默认为免费的生成/缓存步骤。它是声明的有限模型，绝非当前 Hart macro/bit/wall 价格标定。

因而命中位置为 rank 时：

    T_P = 2 + rank_P,
    T_C = (25/24) rank_C.

每法预算为 12；只能启动可完整支付的下一整包，未完成时保留全部既有账本。这个确定预算规则是反例的规则，不冒充实际 30 秒 cooperative guard。

预先固定两个等权案例 E、H。E 的唯一 productive 候选为 k=5，令它单独在 bucket0，其余在 bucket1。于是

    T_PE = 3,       T_CE = 125/24.

两者均在预算内完成，P/C=72/125<0.9。若把这一确定案例形式上复制成 9×16 个固定重复，全部轮次也都严格获胜；这只是代数观察，不是运行 timing，更不声称独立样本量增加。

H 的桶固定如下，两个世界完全相同：

| bucket | 候选 |
| --- | --- |
| 0 | 15,…,24 |
| 1 | 14 |
| 2 | 13 |
| 3 | 1,…,12 |

因此 P 次序为 15,…,24,14,13,1,…,12；C 仍为 1,…,24。

- 世界 A：H 的唯一 productive 候选为 14。
- 世界 B：H 的唯一 productive 候选为 12。

H 在预算内的可见记录在 A/B 完全一样：P 预付 2，消费 15,…,24 十个失败，累计 12；C 消费 1,…,11 十一个失败，累计 275/24，下一整包将超出 12。因此两法 H 均 censored；桶、已消费编号、每项收费、失败与停止状态全相同。世界间只改变尚未消费的成功标签，不能从这些可见记录区分。

如继续到 proper return，总成本为：

| 世界/案例 | P | C |
| --- | ---: | ---: |
| 两世界的 E | 3 | 125/24 |
| A 的 H：命中 14 | 13 | 175/12 |
| B 的 H：命中 12 | 26 | 25/2 |

两个案例等权时，总成本差的符号等于成本和之差的符号：

    A: ΣT_P−ΣT_C = 16−475/24 = −91/24 < 0;
    B: ΣT_P−ΣT_C = 29−425/24 = 271/24 > 0.

更强地，A 的成本和之比为 384/475<0.9，而 B 为 696/425>1。两世界都有有限 proper returns；没有借助不终止、域不匹配、免费评分或未付生成制造逆转。完整案例子集始终只有 E，子集结果始终强烈支持 P，却无法区分全体优势与全体劣势。证毕。

**精确适用结论：**同 K、固定四桶、相同成功判定、全成本计费和预先固定预算，并不足以推出“完整案例的优势可外推”。真实 Hart 若要排除该现象，还需要 e_k/桶与 proper-success 位置之间的额外算术约束或有效总体成本界；本反例没有证明真实 Hart 能实现这两张标签表。已有 Unit20 将缺测标 UNKNOWN 是正确边界，本文没有要求降低其门槛。

## 4. 引理：总成本优势的稳健判定区间

固定 α>0。对每个正权位置要求 0≤L_Mi<∞、L_Mi≤U_Mi≤+∞；兼容 completion 仅指两个方法均有 proper return 且总成本为有限实数的完成值。定义预定有限总体的线性比较目标

    D_α = Σ_i w_i (T_Pi − α T_Ci).

α=1 检查总成本方向；α=0.9 检查**加权总成本**节省至少 10%。后者不是当前 9 轮 median-of-means 与 strict-win 联合判据，不能混用。

若上述区间均有效，则必有

    A_α := Σ_i w_i (L_Pi − α U_Ci)
          ≤ D_α ≤
    B_α := Σ_i w_i (U_Pi − α L_Ci).             (1)

在这些区间是全部信息、可行集合为其直积的模型中，(1) 为最紧区间；在真实 Hart 的算术耦合可行集合中它仍是安全外界，但不保证紧。

证明：对每个 i，T_Pi 的系数非负，T_Ci 的系数非正，分别代入相反端点即可得上下界并加权求和。直积模型中同时取 T_Pi=L_Pi、T_Ci=U_Ci 达到下端点；相反选择达到上端点。其间的线性插值仍在所有区间内，故没有内部空缺。若端点无穷，仅作 inf/sup 理解，并用任意大的有限值逼近；避免使用未定义的 ∞−∞。证毕。

于是 B_α≤0 是对所有兼容完成值都成立的节省证书，B_α<0 给严格证书；A_α>0 是对所有完成值都成立的失败证书。A_α<0<B_α 时，在直积信息模型里存在相反答案，完整子集再稳定也不能填补它。等号按非严格/严格命题分别处理。

有限集合上还可写出选择偏差的精确恒等式。令 S_i 指示 pair 是否完整，q=Σw_iS_i∈(0,1)，d_i=T_Pi−αT_Ci，则

    E_w[d | S=1] − E_w[d] = Cov_w(d,S)/q.       (2)

证明只需展开 Cov_w(d,S)=E_w[dS]−qE_w[d]。固定随机种子、匹配候选域、固定调用顺序，都不蕴含右端为零；完成依赖方法耗时/保存费，正是 S 与 d 可以相关的入口。式 (2) 无须把有限案例假装成总体随机样本。

## 5. 对当前 frontier 的可执行含义与停止界限

1. **当前可合流的是理论边界。** Unit20 原始八个 UNKNOWN 不变；Unit21 的保存修复也不转写为数学/算法完成。本文未对 Unit20 真实数据计算 (1)，因为不能把 record-limit diagnostic 下界替代 timed total。
2. **下一条有判别力的数学问题**是：对一个固定 matched 同域 comparator，能否利用已支付 Hart 状态与剩余区间，证明一个包含生成、评分、必要 consumer、缓存和保存的总费用上界 U，同时把真实算术相关性加入可行集合，使 B_0.9≤0 或 A_1>0？若只能获得 root-call 数而缺价格/其余费用，这个证书尚未成立。不同域 fullclassic/Fermat 可另作端到端比较，不能套同域排列证明。
3. **最小新证书**是一次明确的有限模型推导：指定价格/执行上下文、完整费用分解、每个未知单元的有效界及其依赖，算出 (1) 的单侧符号。无需重新跑旧样本，也无需先生成更多 N。若只能保留双侧跨零区间，应明确停止于“当前证据不可识别”；这不是证明 priority 无效，更不是母问题完成。
4. 若以后采用限时成功率或 capped-cost 作为另一个目标，必须事先定义预算、failure utility 和总体权重，保留所有预定位置。其成功概率/受限成本不能替代本来的完整 proper-return 总成本。存储实现改变后的测量上下文需重新声明，不能在旧结果上反事实补时间。

## 引用（均为此次实读的既存本地文件）

- [R1：Unit20 saved actual cost report](/workspace/em-owner-resume-20261011/new-round-20261011/hart-streaming-cost-audit-20261013/unit20-far48-train-index0-plan-only/FAR48_ONE_ACTUAL_TRAIN_SCOPED_FULL_COST_REPORT.md:3)。实际记录与 pair 条件；没有读取其约 470 MB raw。
- [R2：Unit21 storage integration/preservation report](/workspace/em-owner-resume-20261011/new-round-20261011/hart-streaming-cost-audit-20261013/unit21-immutable-diagnostic-shards-nonscientific-fixtures/UNIT21_ACTUAL_STORAGE_SAVE_INTEGRATION_AND_PRESERVATION_REPORT.md:3)。另实读 FINAL_DISPATCHER_REVISION_SCOPE 与 NEW_WIRING_SCOPE_AND_FUTURE_INTEGRATION，确认 storage-only 边界。
- [R3：Generator-independent consumer-prefix fee lemma](/workspace/em-owner-resume-20261011/new-round-20261011/hart-streaming-cost-audit-20261013/consumer-prefix-generator-independent-fee-unit/GENERATOR_INDEPENDENT_PRIORITY_CONSUMER_PREFIX_FEE_LEMMA.md:46)。固定 consumer 前缀与 conditional fee region，非删失识别结果。
- [R4：Prefix-scan no-fixed-power-gain lemma](/workspace/em-owner-resume-20261011/new-round-20261011/hart-streaming-cost-audit-20261013/occupied-row-k-prefix-next-unit/ROOT_PREFIX_SCAN_NO_FIXED_POWER_GAIN_LEMMA.md:1)。无重证、无重新 root/scan。
- [R5：Hart480→same-K fair-control paper](/workspace/em-owner-resume-20261011/new-round-20261011/hart-streaming-cost-audit-20261013/strong-controls-independent-anchors-far32-next-unit/root-source-decoded/HART_480_STRIDE_TO_4N_K_DOMAIN_FAIR_CONTROL_PAPER.md:30)。same-K permutation 与 120M 不同域边界。
- [R6：Original total-cost classification minimal plan](/workspace/em-owner-resume-20261011/new-round-20261011/hart-streaming-cost-audit-20261013/total-cost-hard-target-followup-plan-unit/TOTAL_COST_CLASSIFICATION_MINIMAL_PLAN_V2_DRAFT.md:1)。原 63 位置、非共享准备/总费用与 bit/wall 分离要求；此处只作设计来源，未将其旧进度表当成当前进度。

贡献等级：本地新推导的抽象严格反例与初等区间引理；未作外部文献 novelty 检索；无新增整数实例、无实测性能结果、无正式 Driver/Steward 接纳。原任务与母目标保持 UNFINISHED / OPEN。

````

</details>

## NT-SUP-RSA-ANTECEDENT

旧RSA extraction-and-barrier的十月Source报告：单collision、uniform law与aggregate graph障碍

保留十月Driver对八月冻结return的原有限结论，并绑定真实DR/RR/report字节；既有Task-local review为ACCEPTED/terminal、指定FOLLOWUP_TASK，母目标仍OPEN，新dyadic算法状态另列。

状态：`EXISTING_TASK_REVIEW_ACCEPTED_TERMINAL_FOLLOWUP_TASK_BOUND_TO_ACTUAL_DR`。

原贡献与归属：原冻结author EM-RSACOL-C76042；十月报告 EM-DVR-FBF223及其disclosed六前身份，NONBLIND。

Source：[driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/1a75122e78c426311877/RSA_CURRENT_DRIVER_MATHEMATICAL_REVIEW_20261012.md](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/1a75122e78c426311877/RSA_CURRENT_DRIVER_MATHEMATICAL_REVIEW_20261012.md)。

- n=pq distinct odd primes，unit x及valid Δ>0,x^Δ=1；Δ=2^s u,u odd，local orders2^a m_p,2^b m_q。z_j=x^(u2^j)的nontrivial pre-1 root分解 iff a≠b。
- A=v2(p−1),B=v2(q−1),m=min(A,B)；uniform complete unit的failure F1=(4^m+2)/(3·2^(A+B))，success1−F1≥1/2，A=B=1时sharp。
- 单x指数kernel ord_n(x)Z；多x共同kernel=lcm_i ord_n(x_i)Z=exp〈x_i〉Z；全unit power maps相等 iff λ(n)|(e−e′)。exposed nonzero global Δ为known annihilator，非collision generation。
- L=lcm_i Δ_i安全annihilator；任意gcd不安全。n65,x57/47,Δ4各自fail但product14给gcd(13,65)=13，是原文strict amplification witness。
- 所有H-combinations均不能按此2-adic机制split iff H₂为两local cyclic projection之间isomorphism的graph。
- k个independent uniform full-group units的aggregate failure Fagg_k=[1+Σ_(t1..m)φ(2^t)(2^(tk)−2^((t−1)k))]/2^((A+B)k)≤F1^k≤2^−k；uniform coefficient vectors modL推前uniform H。

前提：数学是exposed-collision输入模型；独立uniform complete-unit sampling与even-order conditioning、all-residue sampling、thin-subgroup sampling分开。

边界：八月author EM-RSACOL-C76042原return及210semiprimes/274904units/18+12公式cases仅历史冻结证据，不复跑或重命名十月新研究。；实际DR-EA5EFB3177111D8A8A44已绑定RR及报告SHA/blob：disposition ACCEPTED、terminal true、destination FOLLOWUP_TASK为RS-RSA-EXPONENT-COLLISION-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT。只确认已存Task-scope review，不推断followup完成、母目标关闭或新dyadic正式接受。；Shor/HAC/Miller/Abbassi–Bayle/Goursat/Monier的具体先例区分按报告保留，不新取文献、不将bounded未命中当novelty证明。；不提供efficient collision generation或global factoring lower bound；未将source-reported graph障碍和新localdyadic算法状态合并。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Current Driver review of the frozen RSA exponent-collision Result

Driver-ID: EM-DVR-FBF223 / CONTROL_PLANE
Session: MCP-cd5eefdde49843898b2a70c1af94d8dd
Authority: DA-A1DB35C00ED2F8C2A9FA; actual server authorization comment 6115340052.
Prepared 2026-10-12. This current review does not reactivate any quarantined historical review or publication.

## Exact object and judgment

Task RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE, publication TP2-301CA54924787090237D, Result RR-2D43CCB30B906AFB6E20.
Current continuation300 reports FROZEN_RETURN/AWAITING_REVIEW, no live claim, no operational review and no legacy intake requirement. Own complete artifact302 verifies all 2037 Result bytes, SHA256 b69dd5e3107caf2e214e2e37df47e41d22d8a88d2e12a3cc165afa2bc7b6b9aa and blob48e59507afa688c544a584a84b35566f0bac362c at Source5591703654d7496a9ce6f3d9a8575e47158b2ae7. The full taskbook, return and execution record have also been read and their SHA256/blob digests independently recomputed against that packet. Return SHA2568fd60e5fd5be25c7fc17a8d142ed75616a0ceec73a89f7d2088f0221aef265b8; taskbook8f35f12e2d09e944915d28d6ffc033e913a69615e7f285832a70ab60f41c5220; ER eea6b712f9b772b248aa7d15a8c3260d18c032187e995e5bbd76819309ae5ee4. Original bytes and author's EM-RSACOL-C76042 identity are retained.

Judgment: ACCEPTED at this exact extraction-and-barrier Task scope; FOLLOWUP_TASK for the unchanged bounded external prior-art audit. The exposed-collision premise is essential. This is neither an efficient collision-generation procedure nor an improvement in factoring complexity. The larger research portfolio remains OPEN.

## Independent mathematical assessment

Let n=pq for distinct odd primes, x a unit, and a valid transcript provide Delta>0 with x^Delta=1. In proof-side CRT coordinates the orders are 2^a m_p and 2^b m_q, with odd m_p,m_q. If Delta=2^s u, then both odd parts divide u and u/m_p,u/m_q are odd. Thus the coordinates of x^u have exact orders 2^a,2^b, even if Delta contains redundant factors. The first global 1 in successive squaring occurs at t=max(a,b). When a<b its predecessor has signs (1,-1); when b<a the signs reverse; when a=b>0 the predecessor is (-1,-1), and when both are zero the initial value is already1. Hence the nontrivial-square-root mechanism succeeds iff a differs from b. Only the public transcript, modular arithmetic and gcd enter the extractor. This iff concerns the stated mechanism and grants no lower bound against other factoring methods.

For a uniform unit, independent local Sylow-2 components are uniform in C_(2^A),C_(2^B). Depth0 has probability2^-A and depth t>=1 has probability2^(t-1-A). Summing equal-depth pairs gives [1+sum_(t=1)^m 4^(t-1)]/2^(A+B)=(4^m+2)/(3*2^(A+B)). For fixed m the largest value occurs at A=B=m; it equals 1/3+2/(3*4^m), decreasing to1/3 and attaining1/2 exactly at m=1. Therefore success>=1/2 is sharp. Uniform-unit sampling is not interchangeable with conditioning on even order or sampling all residues.

The simultaneous exponent kernel is the lcm of the supplied element orders, equal to the exponent of their generated subgroup. The exponent of the complete unit group is lambda(n), proving the global power-map equality criterion. One nonzero globally annihilating Delta therefore supplies the classical randomized known-annihilator factor reduction; generating that Delta remains outside scope.

L=lcm(Delta_i) is a safe annihilator of the generated subgroup. The witness n65, x57,x47, each Delta4, has both displayed units square to-1 and their product14 square to1 with gcd(14-1,65)=13. This verifies strict amplification of the supplied transcript by combinations without repeating a semiprime census. Gcd of arbitrary local Delta_i does not generally annihilate either unit.

For the aggregate barrier, every element of H_2 has equal local depths iff both coordinate projections are injective. A nonzero projection kernel would have depth0 on one side and positive depth on the other; conversely injective projections identify H_2 with each image and preserve orders. The cyclic local factors therefore identify H_2 as the graph of an isomorphism between equal-order cyclic images. This is the exact subgroup mechanism barrier, not a claim of information-theoretic RSA security.

For t>=1 each local factor has a unique subgroup of order2^t, and there are phi(2^t) graphs. An ordered k-tuple generating a fixed graph has 2^(tk)-2^((t-1)k) choices. Distinct generated graphs do not double-count a tuple. Including the all-identity tuple yields exactly the return's aggregate failure law. All such tuples are a subset of separately failing tuples, so Fagg<=F1^k<=2^-k. Uniform exponent coefficient vectors modulo L push forward uniformly to H. This supplies an existential mechanism and finite randomized combination sampling; it does not establish a new collision-generation oracle.

## Evidence strength and no-repeat units

The author reported210 semiprimes,274904 units,18 aggregate formula cases and12 additional small aggregate parameter triples. I retain those as frozen regression evidence and do not relabel them as rerun by this Driver. The general claims above have elementary algebraic proofs; census output is corroboration. No new prime/semiprime campaign, KQB request, quota reset, or blanket Task redispatch occurred.

## Provenance judgment and necessary bounded successor

The already prepared primary-source audit is not a formal Result of the successor yet. It does materially inform interpretation:

- Miller1976 is read with its actual ERH-conditioned deterministic statements; HAC §8.2 Fact8.6 supplies the standard randomized ed-1 factor reduction.
- Shor quant-ph/9508027v2 §5 explicitly states the unequal local 2-depth criterion for order-based splitting. A supplied annihilator has the same odd-part terminal-sign chain as the exact order, so the local iff is an equivalent antecedent, not a new theorem claim.
- Abbassi–Bayle arXiv2505.00433v2 Prop4.1 together with Thm5.2 recovers the exact unconditional uniform-unit probability once the even-order conditioning is restored. Its all-residue factor phi(n)/n is a different sampling model.
- Goursat's graph-of-isomorphism core is classical. The collision packaging and exact aggregate ordered-tuple law have only a bounded partial-antecedent/no-exact-package-match judgment in the searched corpus; absence is not novelty proof.
- Monier strong-liar formulas have additional odd-part filtering and conditioning; they are adjacent and must not be substituted for the uniform-unit law.

Thus a bounded source-backed classification is worthwhile and already largely prepared. Reuse those bytes and recorded searches under the same audit Task's reviewed Gen2 publication; do not repeat literature retrieval or search merely because the previous publication was correctly isolated. Its mathematical scope, parent, five semantic sections and gates remain unchanged. The publication-scope code fix permits an independently authorized successor while preserving exact old quarantined bytes and authority isolation.

## Independence, typing and disposition boundary

This is a nonblind review of a historical author's frozen proof, not an identity-based claim of clean context. Root prior contribution IDs EM-DIRECT-E1F2B6, EM-DIRECT-FA0C27, EM-DIRECT-49ADE6, EM-DVR-C1A1D9, EM-DVR-4C90FB and current EM-DVR-FBF223 are disclosed. They do not overlap the original Result author. Delegated bounded source/probability preparations and shared Root context are disclosed; they are supporting papers rather than separately registered accepted Results.

These finite groups and probabilities are external classical arithmetic auxiliary readouts. The fixed P000 native Heartbeat X6 substrate and separately typed time remain unchanged; no full-X6 propagation or native-state collapse is claimed. Tool harvest is RESULT_ONLY at this Result's original strength; no new global tool family, L4, Working Truth, Foundation or canonical promotion is granted.

Required next step is the same bounded prior-art audit, after current Source publication/packet readback confirms its Gen2 operational state. The extraction Task may close at its satisfied hard target; that does not close the larger number-theory program.


````

````text
# RSA Exponent-Collision CRT Collapse — Research Return

Status: `PASS / EXACT_EXTRACTION_AND_BARRIER_FROZEN`

Researcher-ID: `EM-RSACOL-C76042`  
Task: `RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE`  
Publication: `TP2-301CA54924787090237D`  
Claim: `chatgpt-rsacol-20260827-2313-c76042`

Hard target:

`RSA_EXPONENT_COLLISION_2ADIC_COLLAPSE_FACTOR_EXTRACTION_OR_EXACT_BARRIER_FROZEN`

## Executive result

The task closes positively at its stated scope.

For a valid local collision
\[
x^\Delta\equiv 1\pmod n,\qquad n=pq,\qquad \Delta>0,
\]
write
\[
\Delta=2^s u,\quad u\text{ odd},
\]
and
\[
\operatorname{ord}_p(x)=2^a m_p,\qquad
\operatorname{ord}_q(x)=2^b m_q,
\]
with \(m_p,m_q\) odd. The extractor-visible chain
\[
z_j=x^{u2^j}\pmod n
\]
produces a nontrivial CRT square root of \(1\), and hence a factor of \(n\), **if and only if**
\[
\boxed{a\ne b.}
\]

For a uniformly random unit, with
\[
A=v_2(p-1),\qquad B=v_2(q-1),\qquad m=\min(A,B),
\]
the exact single-certificate failure and success probabilities are
\[
\boxed{
F_1=\frac{4^m+2}{3\cdot 2^{A+B}}
}
\]
and
\[
\boxed{
P_1=1-\frac{4^m+2}{3\cdot 2^{A+B}}\ge \frac12.
}
\]
The lower bound is sharp at \(A=B=1\), including Blum-prime pairs.

A global exponent-map collision exposes a nonzero multiple of
\[
\lambda(n)=\operatorname{lcm}(p-1,q-1),
\]
so random-base collapse becomes the classical known-annihilating-exponent/order-to-factor reduction.

Multiple local certificates can do strictly more than separate attempts: their lcm safely annihilates the generated subgroup, and combinations of individually failing units can split \(n\). The exact multi-certificate obstruction is that the generated 2-primary subgroup is the graph of an isomorphism between its two local cyclic projections.

## 1. Collision kernels

Let
\[
G=(\mathbb Z/n\mathbb Z)^\times.
\]

For one fixed unit \(x\), the map
\[
\phi_x:\mathbb Z\to \langle x\rangle,\qquad e\mapsto x^e
\]
has kernel
\[
\boxed{
\ker\phi_x=\operatorname{ord}_n(x)\mathbb Z.
}
\]
Therefore
\[
x^e\equiv x^{e'}\pmod n
\iff
\operatorname{ord}_n(x)\mid(e-e').
\]

For a finite sample \(S=\{x_1,\ldots,x_r\}\), the simultaneous exponent map
\[
e\mapsto (x_1^e,\ldots,x_r^e)
\]
has kernel
\[
\boxed{
\operatorname{lcm}_i\operatorname{ord}_n(x_i)\,\mathbb Z.
}
\]
This lcm is exactly the exponent of the subgroup
\[
H=\langle x_1,\ldots,x_r\rangle.
\]

Under CRT,
\[
\operatorname{ord}_n(x)
=
\operatorname{lcm}\!\left(
\operatorname{ord}_p(x),
\operatorname{ord}_q(x)
\right).
\]

## 2. Exact single-collision collapse theorem

Assume the transcript supplies only
\[
(n,x,\Delta)
\]
with
\[
\gcd(x,n)=1,\qquad x^\Delta\equiv1\pmod n.
\]
The extractor is not given \(p,q,\lambda(n)\), or any hidden order.

Write
\[
\Delta=2^s u,\qquad u\text{ odd},
\]
and proof-side local orders as
\[
r_p=\operatorname{ord}_p(x)=2^a m_p,\qquad
r_q=\operatorname{ord}_q(x)=2^b m_q,
\]
where \(m_p,m_q\) are odd.

Since \(r_p,r_q\mid\Delta\),
\[
m_p\mid u,\qquad m_q\mid u,\qquad a,b\le s.
\]
Hence \(x^u\) has exact order \(2^a\) modulo \(p\) and exact order \(2^b\) modulo \(q\).

Define
\[
z_j=x^{u2^j}\pmod n,\qquad 0\le j\le s.
\]
Then
\[
z_j\equiv1\pmod p\iff j\ge a,
\qquad
z_j\equiv1\pmod q\iff j\ge b.
\]
If \(a>0\),
\[
z_{a-1}\equiv-1\pmod p,
\]
and similarly at \(q\).

Thus the first global index with \(z_t=1\pmod n\) is
\[
t=\max(a,b).
\]

If \(a<b\), then
\[
z_{t-1}\equiv(1,-1)
\]
under CRT, so
\[
z_{t-1}^2\equiv1\pmod n,\qquad z_{t-1}\not\equiv\pm1\pmod n,
\]
and
\[
\gcd(z_{t-1}-1,n)=p,\qquad
\gcd(z_{t-1}+1,n)=q.
\]
The case \(b<a\) is symmetric.

If \(a=b=t>0\), then
\[
z_{t-1}\equiv(-1,-1)\equiv-1\pmod n,
\]
so the first pre-\(1\) root is trivial. If \(a=b=0\), already \(z_0=1\).

Therefore:
\[
\boxed{
\text{2-adic collapse splits }n
\iff
v_2(\operatorname{ord}_p(x))
\ne
v_2(\operatorname{ord}_q(x)).
}
\]

A valid extractor is:

1. verify \(\gcd(x,n)=1\) and \(x^\Delta\equiv1\pmod n\);
2. strip all powers of \(2\) from \(\Delta\), obtaining \(u\);
3. set \(z=x^u\bmod n\);
4. square until the next square is \(1\);
5. at the preceding state test \(\gcd(z-1,n)\) and \(\gcd(z+1,n)\).

No hidden factor or order is consumed.

## 3. Exact random-unit success probability

Let
\[
A=v_2(p-1),\qquad B=v_2(q-1).
\]

For a uniform element of the cyclic group \(\mathbb F_p^\times\), its 2-primary component is uniform in \(C_{2^A}\). Therefore, for
\[
a=v_2(\operatorname{ord}_p(x)),
\]
\[
\Pr(a=0)=2^{-A},
\]
and for \(1\le t\le A\),
\[
\Pr(a=t)=2^{t-1-A}.
\]
The \(p\)- and \(q\)-components are independent.

The collapse fails exactly when \(a=b\). With
\[
m=\min(A,B),
\]
\[
\begin{aligned}
\Pr(\mathrm{fail})
&=
2^{-A-B}
+
\sum_{t=1}^m
2^{t-1-A}2^{t-1-B}\\
&=
\boxed{
\frac{4^m+2}{3\cdot2^{A+B}}
}.
\end{aligned}
\]

Hence
\[
\boxed{
\Pr(\mathrm{split})
=
1-\frac{4^m+2}{3\cdot2^{A+B}}.
}
\]

The largest failure probability over \(A,B\ge1\) is \(1/2\), attained at \(A=B=1\). Thus
\[
\boxed{\Pr(\mathrm{split})\ge\frac12}
\]
is the best uniform lower bound.

## 4. Global fake-exponent collision

Two exponents induce the same power map on every unit exactly when their difference annihilates \(G\). Since the exponent of \(G\) is Carmichael's value
\[
\lambda(n)=\operatorname{lcm}(p-1,q-1),
\]
we have
\[
\boxed{
x^e=x^{e'}\ \forall x\in G
\iff
\lambda(n)\mid(e-e').
}
\]

Therefore one exposed nonzero global collision difference is already a known multiple of \(\lambda(n)\). For every subsequently chosen unit \(x\),
\[
x^\Delta=1\pmod n,
\]
so the same 2-adic descent gives a factor with the exact probability in Section 3, at least \(1/2\) per independent random base.

This does not generate a collision and does not beat the classical reduction from a known multiple of the group exponent/order to factoring. It identifies precisely what a global fake exponent leaks.

## 5. Independent certificates and safe aggregation

For independent random units \(x_1,\ldots,x_k\) with valid local collision differences \(\Delta_i\), separate single-certificate attempts fail independently with probability
\[
\boxed{
F_1^k
=
\left(
\frac{4^m+2}{3\cdot2^{A+B}}
\right)^k.
}
\]
Therefore separate attempts alone succeed with probability at least
\[
1-2^{-k}.
\]

There is also a safe transcript-level aggregate:
\[
L=\operatorname{lcm}(\Delta_1,\ldots,\Delta_k).
\]
Because
\[
\operatorname{ord}_n(x_i)\mid\Delta_i\mid L,
\]
\(L\) annihilates every \(x_i\), hence the whole subgroup
\[
H=\langle x_1,\ldots,x_k\rangle.
\]
Every combination
\[
y=x_1^{c_1}\cdots x_k^{c_k}
\]
therefore satisfies
\[
y^L=1\pmod n
\]
and can be fed to the same collapse.

By contrast, \(\gcd(\Delta_1,\ldots,\Delta_k)\) need not annihilate any individual \(x_i\); it has no universal safe-aggregation property.

### Strict amplification witness

Take
\[
n=65=5\cdot13,\qquad
x_1=57,\qquad x_2=47,\qquad
\Delta_1=\Delta_2=4.
\]
Each unit has local 2-depth pair \((2,2)\), so each single collapse fails at the trivial root \(-1\).

But
\[
y=x_1x_2\equiv14\pmod{65},
\qquad
y^2\equiv1\pmod{65},
\]
with nontrivial CRT signs, and
\[
\boxed{
\gcd(14-1,65)=13.
}
\]

Thus lcm-plus-subgroup combination can expose leakage that is absent from every supplied unit when treated separately.

## 6. Exact multi-certificate barrier

Let
\[
P_2\cong C_{2^A},\qquad
Q_2\cong C_{2^B}
\]
be the local Sylow-2 factors, and let \(H_2\) be the 2-primary component of \(H\).

Every combination in \(H\) fails the depth test exactly when
\[
v_2(\operatorname{ord}(\pi_p h))
=
v_2(\operatorname{ord}(\pi_q h))
\quad
\text{for every }h\in H_2.
\]

If that equality holds for every \(h\), both coordinate projections on \(H_2\) are injective: a nonidentity element in one projection kernel would have local depth \(0\) on one side and positive depth on the other. Since \(H_2\) injects into a cyclic 2-group, \(H_2\) is cyclic. Its two images have the same order, and
\[
H_2
\]
is the graph of an isomorphism between those two cyclic image subgroups.

Conversely, any graph of an isomorphism preserves element orders, so every element has equal local 2-depth.

Hence:
\[
\boxed{
\text{no }H\text{-combination can split by this 2-adic mechanism}
\iff
H_2\text{ is a graph of an isomorphism between its local projections}.
}
\]

This is the exact multi-certificate diagonal barrier.

## 7. Exact aggregate-barrier probability

For \(0\le t\le m=\min(A,B)\), each local cyclic 2-group has a unique subgroup of order \(2^t\). For \(t\ge1\), there are
\[
\varphi(2^t)=2^{t-1}
\]
isomorphisms between the two order-\(2^t\) subgroups.

A fixed graph has order \(2^t\). The number of ordered \(k\)-tuples generating that graph is
\[
2^{tk}-2^{(t-1)k},
\]
because a tuple fails to generate it exactly when all entries lie in its unique maximal subgroup.

The \(t=0\) graph contributes one all-identity tuple. Therefore the probability that the generated 2-primary subgroup remains wholly trapped is
\[
\boxed{
F_k^{\mathrm{agg}}
=
\frac{
1+\displaystyle\sum_{t=1}^m
\varphi(2^t)
\left(2^{tk}-2^{(t-1)k}\right)
}{
2^{(A+B)k}
}.
}
\]

At \(k=1\), this reduces to \(F_1\). Also
\[
F_k^{\mathrm{agg}}\le F_1^k\le2^{-k}.
\]
For \(k\ge2\) and \(m\ge2\), the first inclusion can be strict; the \(n=65\) witness exhibits the mechanism.

Because \(L\) annihilates \(H\), choosing coefficient vectors uniformly modulo \(L\) maps uniformly onto \(H\). Thus an extractor can search combinations without knowing the CRT factors.

## 8. Barrier scope

For one local certificate, the exact barrier is
\[
\boxed{a=b.}
\]

For several certificates with lcm aggregation, the exact barrier is
\[
\boxed{
H_2\text{ is a diagonal graph of a local cyclic-subgroup isomorphism}.
}
\]

The smallest useful additional collision is one whose 2-primary component enlarges the generated subgroup away from this graph. It may split directly, or only after a combination.

These are barriers for the collision-driven 2-adic CRT-square-root mechanism, not information-theoretic lower bounds against factoring the public integer \(n\) by unrelated algorithms.

## 9. Exposure-model separation

1. **Single local collision:** exposes a known multiple of \(\operatorname{ord}_n(x)\). It splits exactly when the local 2-depths differ.
2. **Finite sample:** a common collision period is the exponent of the generated subgroup; separate periods may be lcm-aggregated safely.
3. **Global fake exponent:** exposes a known nonzero multiple of \(\lambda(n)\), enough for the classical random-base factor reduction.

Collision exposure and collision generation remain separate. This task proves no efficient way to produce the collision transcript from \(n\) alone.

## 10. Regression and recovery audit

Task-local checker:

`python scripts/check_rsa_exponent_collision_crt_collapse.py`

Re-executed during state-machine recovery on 2026-08-28 with exact-integer arithmetic:

```text
SINGLE_COLLISION_THEOREM=PASS
EXHAUSTIVE_SEMIPRIMES=210
EXHAUSTIVE_UNITS=274904
GLOBAL_MULTIPLE_TESTS=PASS
STRICT_AGGREGATION_WITNESS=n65:x57,x47,delta4->product14
AGGREGATE_FORMULA_CASES=18
FINITE_REGRESSION_IS_NOT_A_GENERAL_PROOF=TRUE
```

An additional recovery audit exhaustively checked the aggregate-barrier formula for
\[
A,B\in\{1,2\},\qquad k\in\{1,2,3\},
\]
covering 12 exact parameter triples, with zero failures.

The factors are used only by the regression harness as hidden ground truth. The extractor itself consumes only public transcript data \((n,x,\Delta)\) or safe lcm-generated subgroup certificates.

Finite checks are regression/falsification evidence only; the general statements above are proved algebraically.

## Terminal disposition

`PASS / HARD_TARGET_MET / EXACT_SINGLE_COLLISION_CRITERION / EXACT_RANDOM_PROBABILITY / GLOBAL_KERNEL / STRICT_MULTI_CERTIFICATE_AMPLIFICATION / DIAGONAL_GRAPH_BARRIER`

Unresolved residue inside task scope: `NONE`.

Out-of-scope residue: efficient collision generation is a separate research question and is not implied by this result.

Control-plane recommendation: Driver-review this frozen result and close the current task generation if accepted. Open no collision-generation successor unless separately justified and immutably published.

````

</details>

## NT-SUP-HART-NEAR-CAP

near-ratio Fermat的公开offset cap A0/16覆盖证明

同一小paper在NEAR40/NEAR48预生成capsule中重复；只采一次数学证明，不把更小cap推为实测优势。

状态：`EXISTING_PAPER_ONLY_LEMMA_NO_INDEPENDENT_REVIEW_OR_NATIVE_ACCEPTANCE_ASSERTED`。

原贡献与归属：EM-SEMIPRIME-1F8B9B，historical Root EM-DVR-FBF223明确near-bound direction；UNKNOWN/directed context保留。

Source：[research_notes/ROOT_NEAR40_FINAL_CODE_SEED_RESOURCE_PREGEN_SOURCE_CAPSULE_20261013_FBF223.json](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/ROOT_NEAR40_FINAL_CODE_SEED_RESOURCE_PREGEN_SOURCE_CAPSULE_20261013_FBF223.json)。

原capsule成员：`/workspace/em-owner-resume-20261011/new-round-20261011/hart-streaming-cost-audit-20261013/unit17-near40-train-index0-plan-only/NEAR40_PUBLIC_FERMAT_OFFSET_COVERAGE_AND_PAID_SCOPE_PROOF.md`；此成员路径是归档标签，不能伪装成独立GitHub路径。

- N=pq,distinct odd primes,p<q<2p,A0=ceil√N；公开inclusive offset T=floor(A0/16)，absolute endpoint A0+T。
- r=q/p∈(1,2)有r+1/r<5/2，((p+q)/(2√N))²<9/8<289/256=(17/16)²。故A*=(p+q)/2<17√N/16。
- 整数t*=A*−A0满足0≤t*<A0/16⇒t*≤floor(A0/16)；z=(A*)²−N=((q−p)/2)²且A*−(q−p)/2=p为proper factor。
- 公开计算仅T=A0//16；denominator16 load width5与真实division按A0 operand width收费，未实际执行的multiply-by-one不造收费。

前提：明确ratio promise1<q/p<2、odd distinct prime admission以及routine实际执行完整offset前缀；resource stop/CENSOR时不能由paper替代actual coverage。

边界：原number57 NT-HART-CONTROL-DOMAINS的ratio256 cap与Hart480界作为前驱，不冒称已覆盖此ratio<2精确证明。；no N/seed/sample/timing生成；不证明一般odd N、general bitcost/walltime advantage或Task完成。；原作者EM-SEMIPRIME-1F8B9B及Root near-bound direction保留，未见独立专门peer则不制造PASS。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Public near-ratio Fermat OFFSET cap T=floor(A0/16)

This is a paper-only lemma for the selected near40 stratum, not an executed sample, timing result or Native acceptance. Let N=pq for distinct odd primes p<q<2p, A0=ceil(sqrt(N)), and let the routine visit A=A0+t for every integer offset0<=t<=T=floor(A0/16), unless a declared resource stop intervenes. All public preparation, division, roots, residuals, masks, failures and proper-factor work remain paid.

Set r=q/p, so1<r<2. Since (2r-1)(r-2)<0, 2r^2-5r+2<0 and r+1/r<5/2. Therefore

((p+q)/(2sqrt(N)))^2=(r+2+1/r)/4<9/8=288/256<289/256=(17/16)^2.

All quantities are positive; hence A*=(p+q)/2<17sqrt(N)/16. Oddness makes A* an integer, and A*>=sqrt(N) gives A*>=A0. Thus t*=A*-A0 is an integer with

0<=t*<17sqrt(N)/16-A0<=17A0/16-A0=A0/16.

For any integer t*<A0/16, t*<=floor(A0/16), including when A0 is a multiple of16 (then the stronger t*<=A0/16-1 holds). Consequently t* lies in the inclusive public offset interval0..T. At this point b*=(q-p)/2 is an integer, z=A*^2-N=b*^2, and A*-b*=p is a proper factor1<p<N. This square passes the zero-inclusive QR predicates, so an exact square/direct-proper consumer reaches a valid return no later than t*, provided the declared routine executes this prefix. Earlier proper return/precheck is also valid, but is not asserted without an actual run.

T is an OFFSET cap, not the absolute A endpoint. The absolute endpoint is A0+floor(A0/16). It is computed from production N and the predeclared public near stratum only; no hidden p/q, firsthit or successfuloffset is supplied to production. The proof requires the admitted ratio promise; it is not a bound for arbitrary odd N or an executed-coverage claim after CENSOR. Distinct prime/odd assumptions are satisfied only by the future offline exactcertificate admission. No N or seedhash has been generated in this paper step.

The optimized public calculation is exactly T=A0//16. There is no artificial multiply-by-one or charge for a product that was never executed. The denominator16 load is explicitly paid as fermat_public_offset_divisor_constant_load (one event, width5), and the actual division is fermat_public_offset_division (one event, widths A0.bit_length(),5). Relative to unit16 T=(9*A0)//8, remove the actually absent product and its width4 charge; change the actual division numerator width from(9*A0).bit_length() toA0.bit_length(), denominator width4 to5. The positive constant-load/division costs and all unchanged210B sieve/prep/ceil-root/increment/directfactor costs remain in the ledger and timed twin. No general bit-cost or walltime advantage follows from this smaller public cap.

Provenance: author EM-SEMIPRIME-1F8B9B with Root EM-DVR-FBF223's explicit near-bound direction; Root6 substantive identities and inheritedUNKNOWN/directedNONBLIND context remain disclosed. P000/HEARTBEAT_NATIVE_X6 basis; external integer/declaredfee mathematics, noveltyUNKNOWN, fullTaskUNFINISHED and motherOPEN.

````

</details>

## NT-SUP-R004-PPRIMARY-PROFILE

R004有限p-primary残差的分层profile与未解future接口

Sep30 checkpoint是本月Git新增文献中的必要早源；采收明确分层模残差法则及旧Δ优化负界，不声称其selectedTask已解决。

状态：`RESEARCH_CHECKPOINT_REPORTED_FINITE_MODULE_INTERFACE_NOT_FOUNDATION_NOT_WORKING_TRUTH`。

原贡献与归属：EM-DIRECT-B74C91，Sep30 RESEARCH_CHECKPOINT；无independent peer。

Source：[research_notes/early_bottleneck_revisit/20260930_EM_DIRECT_B74C91.md](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/early_bottleneck_revisit/20260930_EM_DIRECT_B74C91.md)。

- R=Z/p^KZ,D_H=(Row(A_H)+Row(B_H))/Row(A_H)，Δ(H)=log_p|D_H|。H⊆J的restriction给surjection D_J→D_H，故Δ单调。
- c_j(D)=dim_Fp(p^(j−1)D/p^jD),1≤j≤K；surjection使每层c_j(D_H)≤c_j(D_J)。
- (c1,…,cK)确定cyclic exponent multiplicities，Δ(H)=Σ_j c_j(D_H)。原文仅引用既有finite counterexamples说明Δ一般既不submodular也不supermodular。

前提：有限Z/p^KZ modules及实际restriction surjection；profile只记录同构型层数据，不自动保留embedding/provenance。

边界：未恢复这里所引旧sub/supermodular counterexample完整正文，不新造数值反例；只保留reported negative boundary。；monotone profile不恢复submodularity，不证明declared hiding/refinement/query language的future sufficiency/composition；selectedTask仍需决定embedding data。；RESEARCH_CHECKPOINT/NOT_FOUNDATION/NOT_WORKING_TRUTH，无independent peer或正式theorem truth；文件原日期Sep30，不伪写October新证明。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# Early bottleneck revisit — 2026-09-30

Status: `RESEARCH_CHECKPOINT / EVIDENCE_DRIVEN_REVISIT / NOT_FOUNDATION / NOT_WORKING_TRUTH`

Researcher-ID: `EM-DIRECT-B74C91`
GLOBAL_KNOWLEDGE snapshot: `awdawmip/chatgpt-global-knowledge@8c863c7ec308cfc74dc325af21e41da24d0f10a7`
Enterprise Math scientific comparison snapshot: `awdawmip/enterprise-math@ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec`

## Scope

Revisited representative 2026-08-10/11 bottlenecks: P018 result-conservation hardblock; R007 scale-collapse descent no-go; P017/P018 square-root diagonal stop; P333 compiler-capacity checkpoint; R004 p-adic structural-target defect; branch-preserving collapse; R022 residual certificate fastpaths and proof-carrying reversible BRC. Deduped against current ordered-path/CFD/first-hit residual tasks, R004 causal identifiability, R014 resource calculus, R021 branching collapse, RH carry closure, R063 path-norm roots, and later directed-recovery compiler artifacts.

## Classification

- P018 result conservation: interface/proof-obligation bottleneck, not universal counterexample. Current branch-preserving future-language and residual-faithful programs already cover the research shape. Decision: no duplicate publication.
- R007 scale-collapse descent: true no-go for naive collapse. Preserve it. Current R021/residual work already reopens the safe branch-preserving version. Decision: no duplicate publication.
- P017/P018 square-root diagonal parity stop: method barrier/open, not a general impossibility theorem. Later native path-root work is semantically different. Current scan did not find enough new theorem-level leverage to justify publication this run.
- P333 compiler capacity: early tool/representation bottleneck substantially absorbed by later direct/general/certified word compiler work and R014 resource calculus. Decision: no new task.
- R004 p-adic structural-target defect: exact old structure plus exact negative scalar-optimization result; qualifies for a materially different restart under current residual-fidelity rules.

## R004 judgment-changing evidence

Old object over `R=Z/p^KZ`: `D_H=(Row(A_H)+Row(B_H))/Row(A_H)`. Old scalar `Delta(H)=log_p|D_H|` is monotone under `H subset J` because restriction gives a surjection `D_J -> D_H`, but finite counterexamples show `Delta` is generally neither submodular nor supermodular.

Define `c_j(D)=dim_Fp(p^(j-1)D/p^jD)` for `1<=j<=K`. If `D_J -> D_H` is surjective, multiplication and quotient induce a surjection on every layer, hence `c_j(D_H)<=c_j(D_J)` coordinatewise. By the standard structure theorem for finite `Z/p^KZ` modules, `(c_1,...,c_K)` determines the cyclic exponent multiplicities, and `Delta(H)=sum_j c_j(D_H)`.

This does not restore submodularity and does not prove future-operation sufficiency. It supplies a strictly finer finite typed residual with an exact monotonic law, which is the concrete new reason to revisit the old bottleneck.

## Selected task

`RS-R004-PADIC-TARGET-DEFECT-RESIDUAL-PROFILE-20260930`

Target: decide whether the p-adic layer profile/invariant-factor residual is sufficient and compositional for declared sequential hiding/refinement/query languages, or whether additional module embedding/provenance data is necessary. Positive exact calculus and minimal collision/no-go are both acceptable closure; finite scans alone are not.

Prepared taskbook blob: `sha1:0e100305f7c4f964e205d17093e21c1c12430cdc`
Immutable publication id: `TP2-2F73D1BB1AAA29EF4FCD`
Publisher: `EM-DIRECT-B74C91`
Effective rank: `P2 / MEDIUM`.

Publication grants no theorem truth, Working Truth, or Foundation status.

## Native ordinary-control transport blocker

A fresh `EM_CHAT_CONTROL_V1` status request for this conversation was attempted twice through the prescribed bridge path. Both creation attempts were blocked by the host tool safety layer before any request was created. No old session, Driver authorization, or CLAIM was reused. Therefore this run can verify Source immutable publication records but cannot truthfully report a successful ordinary-control bridge receipt.

````

</details>

## NT-SUP-J1-INTERVAL-SCOPE

J1 surviving interval与rational-map short-interval定理的条件域分离

未审source-comparison negative：实际full-image包含问题在near-half-field区间，不能把rational-map受限input短区间估计直接套入。

状态：`UNREVIEWED_NOT_ADMITTED_NEUTRAL_SOURCE_COMPARISON_NEGATIVE`。

原贡献与归属：local conversation em-research2-20261010-743915c4a185，UNREVIEWED neutral support；未伪造native claimant身份。

Source：[research_notes/portable_supplemental/20261010_R2_J1_INTERVAL_SCOPE_AUDIT_743915c4.md](https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/portable_supplemental/20261010_R2_J1_INTERVAL_SCOPE_AUDIT_743915c4.md)。

- 继承经典J1：odd s,p∤2s,Λ_s(a)=−sa−1/(2a)，a∈F_p*；|ImΛ_s|=(p+η((2s)^−1))/2，J_s={−(s−1)/2,…,(s−1)/2}。
- 若s<p且ImΛ_s⊆J_s，则s≥(p−1)/2；s≥p则interval已wrap全field。
- Merai–Shparlinski Cor1.2的rational degree d≥2短input/output intervals I,J尺度H需H≤p^(1/(2d²+d−1/2))；d2给H≤p^(2/19)。
- p≥7时p^(2/19)<√p≤(p−1)/2；H=s与surviving J1不交；H=s−1在p7有2>7^(2/19)，p≥11则(p−3)/2>√p，仍不交。

前提：这是依赖既有accepted cardinality的source-comparison；不重证其完整image theorem，也不把restricted-domain intersection改成full-domain containment。

边界：原文只报告Merai–Shparlinski primary PDF Cor1.2全文/图页读取；Shparlinski subgroup论文intro，Ugolini abstract/intro，Bergman–Coulter–Fain publisher ABSTRACT_ONLY；本次未重新外部获取文献。；不证明literature novelty/无exact antecedent、J1六行外审完成或所有H/J/C目标；near-half-field character interval语义仍未解决。；原文UNREVIEWED/NOT_ADMITTED/NEUTRAL_SUPPLEMENTAL，dispatch/session等待不是正式claim/研究执行授权；本卷只存已成文的定量scope negative。

<details>
<summary>现有主文献原文（字面保存，不跳转原相对链接或执行命令）</summary>

````text
# J1 interval-antecedent scope audit
Date: 2026-10-10. Status: UNREVIEWED / NOT_ADMITTED / NEUTRAL_SUPPLEMENTAL.
Author local conversation: em-research2-20261010-743915c4a185. No CLAIM/run or current owner-task execution is asserted. Own session_start #3572 remains QUEUED; continuation #3574 was rejected PREREQUISITE_NOT_SUCCEEDED. Keep the original session request, not a replacement identity.

## Current route and durable frontier
Matched complete dispatch #3571 (r2-20261010-dispatch-02) SUCCEEDED selected RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT, publication TP2-39ACFC69F85D8661CFBF, NEEDS_DISPATCH / CLAIM_NEW_OWNER. Full receipt read in #3573/#3575, total 32543 characters, sha256 c2eed502361eed719cb6a9691c4d688409eb542920431fecce91cdc16d3c2b62. This route alone grants no claim.
The embedded old continuation still describes an image-cardinality search. The actual last_progress_ref checkpoint was read at enterprise-math@33e6a1ba9c299c7c20a5a9dd9a6be6edeea8d038:
research_artifacts/mcp/RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT/MCP-cd2f0d5e07b24117a4493046af3c3777/a6c13cc2576dd668c5da/_checkpoint.json
blob 888b78daf3b9b48d3a046e47e3bf40090c2bc722.
It closes the exact x+alpha/x fiber/image-cardinality antecedent and leaves the symmetric-interval layer. Its J1_EXTERNAL_PRIOR_ART_AUDIT_20260923.md, blob 13299f94ba47be9e7e1daface3180dcdf88e762a, was also read. Consume this newer persisted frontier; do not repeat the closed cardinality search. Current exact native continuation still awaits successful own registration.

Accepted source consumed: enterprise-math@56ad8c023de193aefe3b0494e04d38c31e1af6bd:driver_reviews/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260829.md, blob 80b550aa21d0695d0ca9e4853bd707319f6413e4. Preserve H1/H2/C2 narrowing and all row statuses.

## Exact remaining comparison
In the prime-field subcase, odd s and p not dividing 2s, Lambda_s(a)=-sa-1/(2a), a in F_p^*. The inherited J1 result gives |Im Lambda_s|=(p+eta((2s)^(-1)))/2. The symmetric residue set is J_s={-r,...,r}, r=(s-1)/2.
Classifying the map/fibers is already closed externally by the predecessor. This unit audits literature specifically about interval containment and explains a scope separation; it does not re-prove accepted J1 or close the entire H/J/C audit.

## Primary sources actually inspected on 2026-10-10
1. Laszlo Merai and Igor E. Shparlinski, Sparsity of curves and additive and multiplicative expansion of rational maps over finite fields, arXiv:1803.02165v1, 6 March 2018.
https://arxiv.org/pdf/1803.02165
The full primary PDF was accessible, with Corollary 1.2 and its page-3 image inspected. For a rational map of degree d>=2 and intervals I=[K,K+H], J=[L,L+H], the corollary assumes H<=p^(1/(2d^2+d-1/2)) and bounds #(psi(I) intersect J) by H^(1/d+o(1)).
For d=2 the precise cutoff is H<=p^(2/19). This is a genuine structural antecedent for rational-map interval concentration. It is a restricted-domain small-interval estimate, not an exact full-domain J1 saturation classification.

2. Igor E. Shparlinski, Polynomial values in small subgroups of finite fields, Rev. Mat. Iberoam. 32(4) (2016), 1127-1136, DOI 10.4171/rmi/909.
https://ems.press/content/serial-article-files/38607?nt=1
Primary PDF introduction inspected. It treats polynomial/rational values on an input interval and their intersection with, or generation of, a multiplicative subgroup. Target multiplicative subgroups are not the declared additive symmetric residue interval. It is adjacent context, not evidence of exact duplication of the surviving J1 layer.

3. Simone Ugolini, On the iterations of certain maps x -> k*(x+x^(-1)) over finite fields of odd characteristic, arXiv:1304.3283v2, 3 July 2013.
https://arxiv.org/pdf/1304.3283
Primary PDF abstract/introduction inspected, with document search for interval returning no match. The map-family/dynamics antecedent is already known. This bounded inspection supplies no interval theorem; keyword absence and abstract inspection do not certify absence from the entire literature or a full semantic audit of every theorem.

4. Emily Bergman, Robert S. Coulter and Bradley Fain, On consecutive residues and nonresidues under a linear map in a finite field, DOI 10.1017/S0004972724000698.
https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/abs/on-consecutive-residues-and-nonresidues-under-a-linear-map-in-a-finite-field/869EC2766EB7FC86E3BC03E9F3E64D89
Publisher abstract inspected: online 11 October 2024, issue June 2025. It describes quadratic-character combinations for x and mx+a. Full text was not available through this read. This is a possible character-method lead, not an inspected exact theorem covering Lambda_s/J_s.

Searches used both exposed search engines with finite-field Joukowski/Dickson image interval and rational-function concentration terms. Search results alone were not promoted into theorem evidence. No claim of exhaustive literature coverage is made.

## New precise scope separation
Consume the accepted full-image cardinality, not a re-derivation. If Im Lambda_s is contained in J_s and s<p, then
s >= (p+eta((2s)^(-1)))/2 >= (p-1)/2.
If s>=p then the full interval wraps over all residue classes; it is not a small-interval case either.
For prime p>=7,
p^(2/19) < sqrt(p) <= (p-1)/2,
the latter following from p^2-6p+1>=0.
Therefore the nontrivial J1 saturation-candidate range and the d=2 short-interval regime H<=p^(2/19) do not overlap when taking the target interval scale H=s (or s-1). For H=s-1 and p>=7, even H>p^(2/19): at p=7 the smallest candidate s is 3, H=2>7^(2/19), and for p>=11, (p-3)/2>sqrt(p)>p^(2/19).
Consequently Corollary 1.2 cannot be directly specialized at the scale of a surviving full-image saturation candidate. It can study restricted-domain short-window concentration but does not adjudicate the remaining near-half-field J1 cases. A derived asymptotic no-containment corollary at tiny s would already follow from the accepted cardinality bound and would add no mathematical gain; it is intentionally not reported as a new theorem.

This is a source-comparison negative result: a concrete promising literature route is filtered by its actual quantitative hypotheses. It leaves the exact symmetry/character pattern over an interval of size comparable to p unresolved.

## BRC disposition and validation
REUSE_APPLIED: use the retained full-domain image support, known fiber capacity and declared target observer. The observer distinguishes a full value-set containment statement from an input-restricted interval intersection. A source-output shape resembling the same rational map does not license changing population or scale. Positive weighted-recurrent tools are not required. No new general mechanism or native-coordinate transfer is introduced.
Validation is the displayed exact inequality and direct visual inspection of the source exponent, not a numerical scan. The predecessor's cardinality theorem and accepted replication are consumed without replay. No independent Driver review, theorem admission, Foundation/Working Truth or novelty claim is made.

## Smallest unfinished unit
Read successful own session/continuation and its exact taskbook before formal execution; preserve current publication and authentic predecessor/checkpoint. Complete a targeted audit of near-half-field quadratic-character patterns for Lambda_s and J_s, using the exact interval/field semantics of the frozen packet. Bergman et al. remains ABSTRACT_ONLY and needs accessible primary full text if selected. If no exact antecedent is found in a fully stated bounded set, record only NO_MATERIAL_MATCH_IN_AUDITED_SET for that sublayer, then move to the next H/J/C row under the task's actual authority.

````

</details>
