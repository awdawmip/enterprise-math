# D25/LIFT — recovered frozen \(R_p\) and minimal two-port causal certificate

2026-10-24 · ordinary TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923`.

**Author status:** `UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT`. This is a source-linked portable research lemma and an actual finite falsification/regression computation; it is not a native CM/divided-power computation, a completed all-prime LIFT proof, a Result, or independent review.

## 1. Authentic immutable inputs and the newly resolved source gap

Parent: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Exact Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source commit `c47e13e4aba0e006366f989d6334d443f6333ae3` is **not** updated by moving GitHub/control heads. The frozen taskbook Git blob is `53a3ef039325534e3715add837f0eee332289984`.

A material source omission in the preceding portable scalar work is now resolved by an actual **frozen-parent readback**, not by fitting experimental data: at the frozen scientific commit, [the parent reflected-derivative research return](https://github.com/awdawmip/enterprise-math/blob/c47e13e4aba0e006366f989d6334d443f6333ae3/research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md) explicitly defines, for \(p=6m+1\), the second-digit target

\[
\boxed{
R_p=2\sum_{i=1}^{m} B_i
       \sum_{r=1}^{i} (1+6(i-r))C_r \pmod p,
\qquad
C_r=\frac{2^{r-1}(r-1)!^2}
 {18(5/6)_r(2/3)_r}.}\tag{R-src}
\]

Here \(B_0=1\), \(B_{k+1}/B_k=(6k+1)(3k+1)/(36(k+1)^2)\), and \(B_k=(1/6)_k(1/3)_k/(2^k(k!)^2)\). This is the inherited **exact \(R_p\) from the frozen scalar interface**. It is not an invented same-class CM \(\kappa\), nor does it supply the missing native representative \([X]U\bmod p^2\) or fixed \(H_0/B_0\) normalization of that distinct CM operation.

Also consumed without recrediting its proof: [the previous independent direct three-valuation-port LIFT reduction](https://github.com/awdawmip/enterprise-math/blob/1a2f999546137ed8cc457b75846ee4bc42b7a839/research_notes/portable_direct/20261024_onhour_d25_frozen_lift_scalar_three_valuation_ports.md), with actual \(\Delta_p=(G_ph-1)/p\), \(G_p=g/p\), \(g=\sum_{k=0}^{p-1} B_k\), \(h=\sum_{k=0}^{p-1}(12k+1)B_k\). Accepted parent CM0/UR supply the requisite divisibilities; no CM0, UR, WZ/FIVE or earlier high-digit theorem is re-proved here.

## 2. All-prime algebraic theorem: rank-two streaming of the exact frozen target

For every target prime \(p\equiv13,19\pmod{24}\), \(p=6m+1\), define (in \(\mathbf Z_{(p)}\), with reduction only at the declared final observer)

\[
b_i=\binom mi\binom{2m}{i}2^{-i},\qquad
A_0=T_0=0,\qquad C_1=\frac1{10},
\]
\[
\boxed{
C_{i+1}=\frac{36i^2}{(6i+5)(3i+2)}C_i,\qquad
A_i=A_{i-1}+C_i,\qquad
T_i=T_{i-1}+6A_{i-1}+C_i.}\tag{1}
\]
Then the **authentic** frozen \(R_p\) admits the one-pass formula
\[
\boxed{R_p\equiv 2\sum_{i=1}^{m} b_iT_i\pmod p.}\tag{2}
\]

**Proof.** The consecutive-factor ratio in \((R\text{-src})\) is
\[
\frac{C_{i+1}}{C_i}
=2\frac{i^2}{(i+5/6)(i+2/3)}
=\frac{36i^2}{(6i+5)(3i+2)},
\]
and \(C_1=1/[18(5/6)(2/3)]=1/10\). In the range \(1\le i<m\), both denominator factors lie strictly between zero and \(p\); hence every modular inverse is legal. Inductively \(A_i=\sum_{r=1}^{i} C_r\). Writing
\(T_i=\sum_{r=1}^{i}(1+6(i-r))C_r\) shows
\(T_i-T_{i-1}=C_i+6A_{i-1}\), proving the second update. Finally \(1/6\equiv-m\), \(1/3\equiv-2m\bmod p\) and \(i!\) is a \(p\)-unit for \(i\le m\), so
\[
B_i\equiv\frac{(-m)_i(-2m)_i}{2^i(i!)^2}
=\binom mi\binom{2m}i\,2^{-i}=b_i\pmod p.
\]
Substitution in the exact original double sum proves (2). No prime scan or speculative source normalization is used in this proof. \(\square\)

**Minimality at its declared interface.** The kernel \(K_s=1+6s\) of the ordered source-stream map \(C\mapsto T\) has strictly rank-two shifted Hankel witness
\[
\det\begin{pmatrix}K_1&K_2\\K_2&K_3\end{pmatrix}
=\det\begin{pmatrix}7&13\\13&19\end{pmatrix}=-36\ne0
\quad\text{in }\mathbf F_p\ (p\ge13).
\]
Thus one state cannot implement this convolution **for arbitrary input streams and arbitrarily long horizons in a linear time-invariant causal realization with direct feedthrough**; (1) achieves two states \(A,T\). This is not a prohibition on nonlinear encodings, task-specific fixed-stream shortcuts, or compression after the final scalar \(R_p\) has been observed. An equivalent single-output second-order relation is \(T_i-2T_{i-1}+T_{i-2}=C_i+5C_{i-1}\) for \(i\ge2\), with zero-padded inputs.

Computational cost of the inner target goes from the literal \(\Theta(m^2)\) double sum to \(O(m)\) rational/modular source-port updates with \(O(1)\) extra state, retaining exact intermediate \(C_i,A_i,T_i\). This is a proven **algorithmic/observer reduction** of \(R_p\), not a completed all-prime LIFT or a claim that the remaining CM comparison has lower proof complexity.

## 3. Source-matched exact LIFT discrepancy, with all three valuation ports

In the separately proved direct three-port theorem, let \(L_0,L_1,L_2\) be its low-block zeroth/first/second parameter jets, \(U_1,U_2\) its middle-block first/second contributions, \(V_2\) its upper double-zero contribution, \(H_0,H_1\) its original \(h\)-weighted jets. Set
\[
\Gamma_0=L_0/p+L_1+U_1,\qquad
\Gamma_1=L_2+U_2+V_2.
\]
Then the **new cross-source matching** of the frozen \(R_p\) with the already proved direct scalar decomposition yields
\[
\boxed{\mathcal E_p :=
\frac{\Gamma_0H_0-1}{p}
+(L_2+U_2)H_0+\underbrace{V_2H_0}_{\text{upper original valuation-2 port}}
+\Gamma_0H_1
-2\sum_{i=1}^{m} b_iT_i\pmod p.}\tag{3}
\]

Under the frozen accepted CM0 and UR premises, all divided terms are \(p\)-integral, and
\[
\boxed{\mathcal E_p\equiv\Delta_p-R_p\pmod p;\qquad
\text{D25/LIFT}\iff(\forall p\equiv13,19\pmod{24})\,\mathcal E_p=0.}\tag{4}
\]
Here equivalence is only at the accepted scalar interface and requires the task's **original** first/middle/upper valuation blocks, not the auxiliary \(S_m\) WZ endpoint. In particular omitting \(V_2\) would change \(\Delta_{19}\) by \(6\bmod19\) (inherited source witness), so a mod-\(p^2\) truncation of \(g\) is not sufficient after dividing by \(p\).

This is the previously missing **source-authenticated \(R_p\)-versus-\(\Delta_p\) match**. Its new content is locating the actual immutable target, proving the streaming source-port law and bringing it onto the already verified exact scalar observer. It does **not** use a newly sourced CM divided-power representative and does not prove (4) universally.

## 4. Actually executed exact arithmetic, two independent routes

The attached executable reproducer uses only Python stdlib and the **original source recurrences**. For each target prime it constructs \(g,h\) modulo \(p^3\), legally divides by \(p\) twice, and independently computes \(R_p\) by (1) and also by the original nested sum \(R\text{-src}\). The nested input check is not another claim of an independent scientific review. The exact Fraction check reconstructs every \(B_k\) and \(C_r\) independently of modular recurrence for four small primes.

**This turn's actual execution:** 312 of 312 qualifying target primes \(13\le p\le10000\) passed \(\Delta_p=R_p\bmod p\), including all 77 primes \(\le2000\). The rank-two stream agreed with the original inner double sum at *every* checked prefix. Explicit pairs \((\Delta_p,R_p)\): \(13:(0,0)\), \(19:(12,12)\), \(37:(11,11)\), \(43:(15,15)\), \(157:(82,82)\), \(211:(119,119)\). A separate exact Fraction check at \(p=13,19,37,43\) gave the same pairs. These finite computations are **falsification/regression evidence, not an all-prime proof, independent referee pass, or native CM benchmark**.

Reproducer (its default bound 2000 is faster; invoke `python <saved-file> 10000` for the 312-prime check):

~~~python
from fractions import Fraction as Q
from math import factorial, isqrt
import sys

def primes(bound):
    sieve = bytearray([1])*(bound+1)
    sieve[:2] = b'\0\0'
    for d in range(2,isqrt(bound)+1):
        if sieve[d]:
            sieve[d*d:bound+1:d] = b'\0'*((bound-d*d)//d+1)
    return [p for p in range(13,bound+1) if sieve[p] and p%24 in (13,19)]

def modular_ports(p):
    mod=p**3
    b=1;g=h=0
    for k in range(p):
        g=(g+b)%mod
        h=(h+(12*k+1)*b)%mod
        if k+1<p:
            b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod)%mod
    assert g%p==0 and ((g//p)*h-1)%p==0
    Delta=((((g//p)*h-1)%p**2)//p)%p
    m=(p-1)//6
    b=1;c=pow(10,-1,p);a=t=R=nested=0
    seen=[]
    for i in range(1,m+1):
        b=b*(6*i-5)*(3*i-2)*pow(36*i*i,-1,p)%p
        if i>1:
            j=i-1
            c=c*36*j*j*pow((6*j+5)*(3*j+2),-1,p)%p
        t=(t+6*a+c)%p
        a=(a+c)%p
        seen.append(c)
        raw=sum((1+6*(i-r))*seen[r-1] for r in range(1,i+1))%p
        assert t==raw
        R=(R+2*b*t)%p
        nested=(nested+2*b*raw)%p
    assert R==nested
    return Delta,R

def fraction_small(p):
    m=(p-1)//6
    B=[Q(1)]
    for i in range(1,p):
        B.append(B[-1]*Q((6*i-5)*(3*i-2),36*i*i))
    g=sum(B)
    h=sum((12*k+1)*B[k] for k in range(p))
    v=((g/p*h-1)/p)
    assert v.denominator%p
    Delta=v.numerator*pow(v.denominator,-1,p)%p
    C=[Q(0),Q(1,10)]
    for j in range(1,m):
        C.append(C[-1]*Q(36*j*j,(6*j+5)*(3*j+2)))
    source=2*sum(B[i]*sum((1+6*(i-r))*C[r] for r in range(1,i+1))
                 for i in range(1,m+1))
    assert source.denominator%p
    R=source.numerator*pow(source.denominator,-1,p)%p
    return Delta,R

bound=int(sys.argv[1]) if len(sys.argv)>1 else 2000
ps=primes(bound)
for p in ps:
    x,y=modular_ports(p)
    assert x==y,(p,x,y)
for p in (13,19,37,43):
    assert fraction_small(p)==modular_ports(p),p
print("PASS:",len(ps),"target primes <= ",bound)
print("samples:",{p:modular_ports(p) for p in (13,19,37,43,157,211) if p<=bound})
~~~

## 5. Typed BRC audit, limitations and precise handoff

**Source/method resolution:** `COMPOSE_APPLIED` — existing `T0_BRC` source-labeled branch/provenance carrier and `T1_SCALE_ENUMERATION_VALUATION` finite \(p\)-valuation ports, with the parent exact rational hypergeometric recurrence. Carrier: ordered \((i,r)\) branches and source-labeled \(C_r,B_i\), plus independent \(0/1/2\)-valuation \(k\) branches for \(\Delta_p\). Future operations are causal affine convolution, weighted accumulation, \(p\)-integral multiplication and two legal divisions. The final \(\mathbf F_p\) observer is not a complete port state; replacing the ordered stream by total \(\sum C_r\) erases \(T_i\) and fails the declared future-operation lease. No claim of a newly accepted general BRC tool, new P000 axiom, six-axis space, CM computation, or independence is made.

**Next exact science:** Find a source-preserving finite telescoper, Frobenius/CM same-class bridge, or exact obstruction that cancels the discrepancy (3) *uniformly in both residue classes*. Preserve \(V_2H_0\), original \(C_r\) and \(B_i\), and \(R_p\) rather than reverting to source-unmatched WZ endpoints. If invoking the CM route, first supply/authenticate the actual primitive, map direction/semilinearity, \([X]U\bmod p^2\), fixed \(H_0/B_0\), \(\omega+6\nabla_\lambda\omega\), and \(\kappa\) normalization. Neither 312 finite successes nor the scalar recurrence alone resolves this.

**Live control provenance:** Fresh same-lane own recovery [#6278](https://github.com/awdawmip/kimi-query-bridge/issues/6278) returned SUCCEEDED but no current winning claim, run, unpublished uploads or pending mutations; old Researcher session `MCP-cf39e84761fa4092a3600450d8aad3ab` remains ACTIVE with prior server-stored contributions. Two neutral staging archives are **not** Task progress. Fresh same-lane exact continuation [#6279](https://github.com/awdawmip/kimi-query-bridge/issues/6279) SUCCEEDED with `execution_authorized=false`, route `REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION` and no continuation_seed. Previous exact RESEARCH dispatch [#6271](https://github.com/awdawmip/kimi-query-bridge/issues/6271) ended `FAILED: TimeoutExpired`; no blind mutation replay or no-dispatch inference. Source claim/open/current-run checkpoint/freeze/review are **not** asserted. Current scientific proof is portable and awaits independent verification and lawful Source admission. No scheduler, source pin, worldview or notification change.
