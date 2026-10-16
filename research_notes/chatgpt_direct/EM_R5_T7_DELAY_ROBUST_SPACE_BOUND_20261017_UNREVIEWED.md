# EM R5 — Arbitrary-delay raw T7 phase witness still needs linear memory

**Type:** `UNREVIEWED / NOT_ADMITTED / AUXILIARY_SCALAR_ONLY`.
**Date:** 2026-10-17 Asia/Shanghai. **Basis:** Global Knowledge V1 main `6068eb8eb4cf3f5c0c80ac466ee0208c5dddb209`; Enterprise Math main `ace61df5bc051e20ab99e2b09fc6cbc441016d01`. The local independent verification program and certificate are retained in the research handoff; this note contains the infinite proof. This is not an original five-port BRC or X6 native result.

## Exact observer and fixed branch

The recurrence is (U_1=1, U_2=1+3t, U_{L+2}=(1+3t)U_{L+1}+t^3U_L), with raw output (Y(L)=[t^7]U_LU_{L+1}=3g(L)) for (L\ge3). The exact polynomial is
[
g(x)=\frac{(2x-5)(648x^6-7452x^5+34794x^4-85005x^3+116267x^2-86328x+27986)}{70}.
]
In (\mathbf Z_3), let (g'(\alpha)=0,\alpha\equiv2\pmod3), (c=g(\alpha)), (u=g''(\alpha)/2\in\mathbf Z_3^\times). Fix the **positive critical branch** (x=\alpha+3q), (q\equiv1\pmod3), and let (f(q)=(g(\alpha+3q)-c)/(9u)). Then (f(q)\equiv q^2\pmod3), (f'(q)\equiv2q\pmod3), (f''(q)\equiv2\pmod3); (f) bijectively and isometrically maps (1+3\mathbf Z_3) to itself. Raw input (Y=3c+27u f(q)); required output (x=\alpha+3q).

A deterministic causal generator reads **raw (Y) ternary digits from low to high once**, writes correct (x) digits irreversibly and cannot use its old output or old input as scratch memory. It may delay arbitrarily, with an **input-dependent** emission schedule, but must eventually output *every* phase digit for **every** admissible infinite input. Output cursor/length may be supplied for free; all other mutable memory is charged. The operation is added *readout precision*, not the original physical time update (L\mapsto L+1).

## New theorem — no synchronous deadline is necessary

After exactly (N=n+3) input digits ((n\ge1)), every such generator requires at least
[
\boxed{\left\lceil\frac{3^{n-1}}{n+2}\right\rceil}
]
internal states across valid prefixes, even if output deadlines are arbitrarily late and data-dependent. In particular the bit-space lower bound is
[
B_N\ge\max\{0,\lceil(n-1)\log_2(3)-\log_2(n+2)\rceil\}=\Omega(N).
]
If the number of output digits emitted after (N) inputs is independent of input values (an arbitrary *fixed* schedule, still potentially extremely slow), the sharper bound is (3^{n-1}) states and (\lceil(n-1)\log_2(3)\rceil) bits. Storing raw prefixes and Hensel-inverting with fixed polynomial degree uses (O(N)) bits, so **optimal worst-case working space is (\Theta(N))** for this fixed-sign family.

### Proof

1. By the integral isometry (f), the (N=n+3)-digit admissible raw prefixes correspond bijectively to (q\equiv1\pmod3\pmod{3^n}), a population of (3^{n-1}) objects. A prefix fixes (x\pmod{3^{n+1}}) but not the next trit: the raw continuations (Y_0=y+0\cdot3^{n+3}) and (Y_1=y+1\cdot3^{n+3}) both remain admissible and their inverse phases first differ at order (3^{n+1}). Thus a correct causal generator can have emitted only (k(y)\in\{0,\ldots,n+1\}) phase trits by this checkpoint. The output length, even if free, carries at most (n+2) possible values.
2. Put (q_{y,z}=f^{-1}((Y_z-3c)/(27u))), (z=0,1). The two roots share the prefix (q_n\pmod{3^n}). By their exact finite-level divided difference,
[
\boxed{D(y):=\frac{x_{y,1}-x_{y,0}}{3^{n+1}}\equiv(uf'(q_n))^{-1}\pmod{3^n}.}
]
Since (f'(q)-f'(r)=(q-r)E(q,r)) with (E(q,r)\equiv2\pmod3) for all (q,r\equiv1\pmod3), (f') is an isometry on that residue disc. Hence the (3^{n-1}) raw prefixes yield **pairwise distinct** two-continuation signatures (D(y)).
3. Suppose distinct prefixes (y,y') leave the generator in the **same internal state** and with the **same number (k)** of emitted phase digits. Give both runs the same future input (z00\cdots), for (z=0) and separately (z=1). From the matched machine state, the *entire future output word* is identical for each (z) across the two prefixes. The earlier output may depend on (y), but for a fixed (y) it is common to both (z) continuations and cancels upon subtraction. Because both runs have the same output length (k), the phase difference (x_{y,1}-x_{y,0}\pmod{3^{2n+1}}) must equal the corresponding difference for (y'). Liveness ensures enough future output digits eventually exist; no uniform latency bound is necessary. This forces (D(y)=D(y')\pmod{3^n}), contradicting step 2.
4. Thus each (internal state, already-emitted-length) pair represents at most one raw prefix. There are at most (n+2) permitted lengths, proving the adaptive bound. A prefix-independent emission schedule has exactly one length and proves the sharper bound. The standard store-prefix/Hensel algorithm gives the (O(N)) upper bound. QED.

**Actual finite checks** (Python integer arithmetic, no native BRC execution): 900 original recurrence rows, and all 1,093 raw prefixes across (n=1,\dots,7), checked against both the exact signatures and the undetermined next trit. The state-count lower bounds at (n=1,\dots,7) for adaptive output are (1,1,2,5,12,31,81), versus (1,3,9,27,81,243,729) for a fixed output schedule. This finite check **does not prove** a universal automaton claim.

**BRC discipline:** population = all finite-compatible integer tail phases in the positive critical branch; observer = exact raw (Y); information lost by the readout = hidden phase; future operation = increasing readout precision; preserve branch provenance and 3-adic valuations. Previous scalar normal-form/Hensel observer tools are **REUSE_APPLIED**. No claim of native typed five-port BRC execution, X6 dynamics, Driver acceptance, or a formal CLAIM.

**Control status:** identity `awdawmip` read from connected GitHub; native `em_control_tasks` was blocked by `CONTROL_QUOTA`; native `em_session_start` denied with `STATIC_READONLY_SCOPE_DENIED`; active owner remains unverified. A branch-only research note is **unreviewed Source provenance**, not a canonical mathematical Result or main-branch intake.

**Next exact question:** Remove the fixed sign: allow online choice between the two critical inverse branches and define a branch-invariant two-continuation signature or produce a lower-space counterexample. Do not silently generalize this theorem to arbitrary-sign witness pairs, native BRC ports, or the P000 X6 Cell model.
