# Prime Coordinate Hidden-Factor Separation Spectrum — Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-HIDDEN-FACTOR-SEPARATION-SPECTRUM`  
Publication-ID: `TP2-FC3E7A11955B41A7F002`  
Researcher-ID: `EM-PCF3-C321DA`  
Claim-ID: `chatgpt-pcf3-20260828-0742-c321da`  
Execution record: `ER-839F541F4A98FB33D8A7`

## Primary verdict

`SEPARATOR_FOUND_WITH_EXACT_SCOPE`

Hard target `HIDDEN_FACTOR_SEPARATION_SPECTRUM_CLASSIFIED` is met at task-local research-return strength.

The strongest exact result is an N-only three-level valuation-wall separator for every distinct odd semiprime, supplemented by a complete five-state cyclotomic collision spectrum for the frozen public polynomial probes. The wall result is **not** a factorization-speedup theorem: direct construction still reaches kernel index `Theta(p)` on balanced `N=pq`, so `COMPLEXITY_COMPRESSION_OF_VALUATION_WALL` remains open.

## Source-exposure and control boundary

The canonical control-plane owner of this return is the pure-JSON Issue #240 claim `chatgpt-pcf3-20260828-0742-c321da`.

After this owner had independently derived and checked the cyclotomic sub-spectrum, a concurrent source-exposed Draft PR #761 (`EM-PCF3-DCEC44`, head `48231a8ddd8852bbef09d538c754ef42118e9f46`) appeared with a stronger valuation-wall result. Its scheduler CLAIM/HANDOFF bodies append `AGENT_STATE` after the JSON object and therefore are not parsed by the current strict `json.loads(body)` runtime reducer. That control-plane defect does not make its mathematics false. I therefore disclose it as `PARALLEL METHOD-HARVEST`, re-derive the wall theorem below, and do not inherit any authority from its scheduler events.

## PCF1-admitted typed response

PCF1's binding constructor rule is preserved: algorithm-side inputs are only `N`, independent/public parameters and fixed public constants; hidden factors, CRT idempotents and factor-labelled channels remain proof-side.

The executable wall component uses the public integer kernel

\[
A_s=\binom{2s}{s}^2\binom{3s}{s}
   =\frac{(2s)!(3s)!}{(s!)^5}.
\]

For `k=1,2,3`, define

\[
D_0=1,\qquad D_k(N,s)=\gcd(A_s,N^k),\qquad
H_k(N,s)=D_k/D_{k-1}.
\]

Every object is computed from `(N,s)` alone.

The polynomial component remains

\[
P_N(s)=\bigl(s^2+1,\ s^2+s+1,\ s^6-1,\ s^6+1\bigr)\pmod N.
\]

For any integer scalar `a(N,s)`, direct GCD separation is exactly local divisibility asymmetry:

\[
\gcd(N,a)\text{ is proper}\iff[p\mid a]\oplus[q\mid a]
\]

when `N=pq`. For an N-only square integer matrix, a full-rank/singular asymmetry is integerized by `det(M)`; general rank needs determinantal minors. A single global boolean response is synchronized for odd factors and is not a direct splitter.

## Exact valuation-wall theorem

Let `r>3` be prime and `0\le s<r`. Legendre's formula gives

\[
\boxed{v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+
\left\lfloor\frac{3s}{r}\right\rfloor.}
\]

The denominator contributes no `r`; and because `3s<3r<r^2`, there are no higher `r^j` terms. Therefore the local valuation is exactly

\[
0,1,2,3
\]

according as

\[
r>3s,\quad 2s<r<3s,\quad \frac32s<r<2s,\quad s<r<\frac32s.
\]

For squarefree `N=pq`, the nested quotient satisfies

\[
\boxed{H_k(N,s)=\prod_{r\in\{p,q\}:v_r(A_s)\ge k}r.}
\]

Hence `H1,H2,H3` are exactly the hidden-factor walls at `3s,2s,3s/2`.

## Complete first-dyadic spectrum

Assume `3<p<q` and let

\[
s_*=2^{j_*},\qquad j_*:=\min\{j\ge0:3\cdot2^j>p\}.
\]

Minimality gives

\[
\frac32s_*<p<3s_*<2p,\qquad s_*<p.
\]

At `s_*` exactly four mutually exclusive cases exist:

1. `q>3s_*`: `H1=p`, a direct separator.
2. `p<2s_*<q<3s_*`: `(H1,H2,H3)=(N,p,1)`, so `H2` separates at the same kernel index.
3. `2s_*<p<q<3s_*`: `(H1,H2,H3)=(N,1,1)` and `q/p<3/2`.
4. `3s_*/2<p<q<2s_*`: `(H1,H2,H3)=(N,N,1)` and `q/p<4/3`.

There is no fifth case. In particular `H3=1` in every synchronized first-wall case, so the third wall is redundant at this collision time.

## One public seed breaks all remaining synchronization

In either fully synchronized case, `q<2p`. Define

\[
\boxed{u=\left\lfloor\frac{\operatorname{isqrt}(N)}3\right\rfloor+1.}
\]

Because distinct-prime `N=pq` is nonsquare, `3u` is the least multiple of `3` strictly above `\sqrt N`; hence

\[
p<\sqrt{pq}<3u.
\]

Also `q<2p` implies

\[
u<\frac{\sqrt2}{3}p+1<p
\]

for `p\ge5`.

It remains to place `3u` below `q`. Since `q>3`, either `q\equiv1` or `2\pmod3`.

- If `q\equiv1\pmod3`, then `q-1` is a multiple of 3. Distinct odd primes give `p\le q-2`, so `\sqrt{pq}<q-1`.
- If `q\equiv2\pmod3`, then `q-2` is a multiple of 3. The possibility `p=q-2` would force `p>3` to be divisible by 3, impossible; hence `p\le q-4` and `\sqrt{pq}<q-2`.

Thus the least multiple of 3 above `\sqrt N` satisfies

\[
\boxed{p<3u<q,\qquad u<p.}
\]

Applying the valuation formula gives

\[
\boxed{\gcd(A_u,N)=p.}
\]

Therefore the following factor-blind procedure is exact on every distinct odd semiprime:

1. precheck `gcd(N,6)` to extract factor `3` when present;
2. otherwise test dyadic `s=1,2,4,...` until `H1!=1`;
3. return proper `H1` if obtained;
4. if `H1=N`, inspect `H2` at the same `s` and return it when proper;
5. if still synchronized, use the single public `u=floor(isqrt(N)/3)+1` and `gcd(A_u,N)`.

This closes the separation question but not the complexity question. The largest required kernel index remains `Theta(p)` in balanced cases under direct evaluation.

## Cyclotomic five-state sub-spectrum

For the PCF1-admitted fixed probes

\[
f_4=X^2+1=\Phi_4,\quad f_3=X^2+X+1=\Phi_3,
\]
\[
f_{6-}=X^6-1=\Phi_1\Phi_2\Phi_3\Phi_6,\quad
f_{6+}=X^6+1=\Phi_4\Phi_{12},
\]

the local zero vector at every prime `ell>3` has only five states:

- `Z=(0,0,0,0)`;
- `C=(0,0,1,0)` from orders `1,2,6`;
- `B3=(0,1,1,0)` from order `3`;
- `A4=(1,0,0,1)` from order `4`;
- `D12=(0,0,0,1)` from order `12`.

Cyclicity of `F_ell^*` gives exact counts:

| `ell mod 12` | Z | C | B3 | A4 | D12 |
|---:|---:|---:|---:|---:|---:|
| 1 | `ell-12` | 4 | 2 | 2 | 4 |
| 5 | `ell-4` | 2 | 0 | 2 | 0 |
| 7 | `ell-6` | 4 | 2 | 0 | 0 |
| 11 | `ell-2` | 2 | 0 | 0 | 0 |

For `ell=3`, the counts are `(1,1,1,0,0)`.

For uniform public `s mod N`, CRT makes the two local seeds independent. All four polynomial GCD probes fail exactly when the two local five-state signatures agree; hence the collision count is the dot product of the two local state-count vectors. This gives a complete exact polynomial collision registry by `(p mod 12,q mod 12)`.

The single residue `s^6-1` has `rho_ell=gcd(6,ell-1)>=2` roots at every odd prime and therefore exact proper-split probability

\[
\rho_p/p+\rho_q/q-2\rho_p\rho_q/(pq)>0.
\]

But the complete fixed probe family has at most 12 local roots, so on balanced semiprimes one iid uniform public seed has only `O(N^{-1/2})` success. Moreover any fixed finite public seed set for any fixed finite integer-polynomial family has infinitely many synchronized prime pairs: choose `p,q` larger than every nonzero absolute probe value on that finite seed set.

For seeds `0..63`, an explicit synchronized pair is

\[
p=62523502271,\quad q=62523502303,
\]
\[
N=3909188338232494230113.
\]

## Separation taxonomy and PCF4 handoff

The ranked integerizable signals are now:

1. `H1` at the first dyadic wall — direct proper factor when the first wall is asymmetric.
2. `H2` at the same kernel index — strictly new information on the mid-straddle class.
3. the single public fallback `u=floor(isqrt(N)/3)+1` — deterministic synchronization breaker.
4. `x^6-1`, then the signed pair `(x^6-1,x^6+1)` — cheap polynomial baselines with exact but square-root-scale seed support.
5. `Phi3/Phi4` refinements — useful only inside synchronized polynomial branches.
6. `H3` at first dyadic collision — exact redundancy.

Packet/path, shell, filament, relational-axis or rank coordinates that lack a frozen N-to-carrier/N-to-matrix map remain descriptive and are not silently promoted into an extractor.

## Verification and artifacts

Canonical owner artifacts:

- `research_artifacts/PRIME_COORD_FACTOR_HIDDEN_FACTOR_SEPARATION_SPECTRUM/EVIDENCE_REPORT.md`
- `scripts/check_pcf3_hidden_factor_separation_spectrum.py`
- `scripts/check_pcf3_hidden_factor_separation_spectrum_independent.py`

The owner branch's independently derived cyclotomic checkers froze:

`PCF3_SPECTRUM_CHECK_PASS primes=61 pairs=190 crt=10805 corpus=84/89 semiprime=43/48 fixed64=3909188338232494230113`

`PCF3_INDEPENDENT_CHECK_PASS primes=45 pairs=120 fixed64=3909188338232494230113 aggregate=84/89`

Disclosed parallel PR #761 additionally exposes a direct wall-spectrum checker reporting 61/61 theorem-domain PCF2 cases and an independent enumeration of 1,830 distinct odd semiprimes below prime 300 with zero failures. Those finite counts are regression only; the wall theorem is proved above and does not depend on accepting that PR's control events.

Source pins:

- task publication `TP2-FC3E7A11955B41A7F002`;
- taskbook blob `49047f8f7950bcb15c80316ebd733af2725d5a35`;
- accepted PCF1 result `RR-B8D8679EB033E990E825` / record blob `5962795e98743cf8b5dba3fcfc043f508bda34a4`;
- PCF1 Driver review blob `b1bef218c80e5979a5de8f8b0c95ac2317857bf4`;
- PCF1 downstream gate blob `7939539e249af663eebf86c38a66dfc30c807ccb`;
- finite PCF2 corpus source only: Draft PR #740 head `dce4a309f8d799030081ed82e310c26a92d8f465`;
- disclosed wall method-harvest: Draft PR #761 head `48231a8ddd8852bbef09d538c754ef42118e9f46`.

## Smallest unresolved residue

`COMPLEXITY_COMPRESSION_OF_VALUATION_WALL`.

No polynomial-time, sub-square-root, novel factoring exponent, Working Truth, Foundation authority, canonical promotion or general factoring lower bound is claimed.
