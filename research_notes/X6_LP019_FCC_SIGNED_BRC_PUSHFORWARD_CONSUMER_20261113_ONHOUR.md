# LP019 — exact signed-X6 N-BRC pushforward to the current FCC carrier consumer

Date: 2026-11-13, on-hour TASK_RESEARCH. Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. Status: **AUTHOR-PROVED / EXACT LOCAL CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Verified consumer and evidence boundary

Current consumer: `experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py`, actual Git blob `2a8c8c804c6d4b0a4e0919f62235e58ccb583e4e`, especially lines 8–16 and 72–85. It defines a three-component **FCC carrier readout**, not a P000 three-axis native identity. At lines 81–85 two distinct signed X6 lifts of a common FCC point have squared native component norms 1 and 2; the checker already preserves that distinction. This pass **does not patch this correct consumer** or claim to have found the original historical LP019 erroneous cancellation caller.

Immutable task science remains P000 V5 / signed X6 centered Cell at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; the above consumer is a separately verified current-main downstream observation. Source 28-LP matrix: `research_notes/X6_LP28_SOURCE_CONSUMER_ACTION_CROSSWALK_20261112_ONHOUR_1400.md` (LP019).

## New complete formula for the scoped carrier N-BRC observer

Let `z∈Z^6` be the raw signed endpoint, `N≥0` the **exact path length**, and use the fixed carrier vectors

```
v1=(1,1,0), v2=(1,-1,0), v3=(1,0,1),
v4=(1,0,-1), v5=(0,1,1), v6=(0,1,-1).
```

The projection is `F(z)=Σ z_i v_i`. Every signed X6 primitive step `±e_i` becomes `±v_i`. Define `C_N(p,q,r)` to count all ordered signed primitive words of length exactly N whose **carrier endpoint** equals `(p,q,r)`. This is the pushforward of native exact-length N-BRC mass, not native endpoint multiplicity or a shortest-to-carrier geodesic claim.

Put `B(k,t)=binom(k,(k+t)/2)` if `|t|≤k` and `k+t` is even; otherwise `B(k,t)=0`. Then for all integer `p,q,r` and `N≥0`,

```
C_N(p,q,r)
 = Σ_{a+b+c=N} N!/(a! b! c!)
     B(a+b,p) B(a+c,q) B(b+c,r).
```

**Proof:** The 12 signed step monomials are exactly

```
S(X,Y,Z) = (X+X^-1)(Y+Y^-1)
          + (X+X^-1)(Z+Z^-1)
          + (Y+Y^-1)(Z+Z^-1).
```

`C_N(p,q,r)=[X^p Y^q Z^r]S^N`. Partition the N ordered steps into the XY, XZ and YZ families with sizes a,b,c (multinomial factor). Inside each family all four sign pairs occur once; the X sign choices involve a+b factors, the Y choices a+c, the Z choices b+c, independently. Their coefficients are the three B terms. Summing these disjoint partitions proves the formula exactly, without finite-to-infinite extrapolation.

This supplies a direct carrier-aggregated count and a typed comparison to native signed BRC. It does **not** authorize erasing the native endpoint, path order, branch, signed interactions or provenance for any future operation that distinguishes them.

## Concrete separating witness and local execution

For carrier point `y=(0,1,1)`, length 1 has one native endpoint `(0,0,0,0,1,0)` and carrier N-BRC mass 1. At length 2 there are two different native endpoints

```
zA=(0,-1,1,0,0,0); zB=(1,0,0,-1,0,0),
F(zA)=F(zB)=y,
native N-BRC(zA)=native N-BRC(zB)=2.
```

Thus `C_2(y)=4`, whereas the carrier does not choose a single native endpoint; also `C_3(y)=45`. The exact series for N=0…8 is `0,1,4,45,360,3520,33600,336525,3413200`.

The standalone Python checker `research_checks/X6_LP019_FCC_SIGNED_BRC_PUSHFORWARD_20261113_ONHOUR.py` was **actually executed locally**, output `PASS FCC_SIGNED_X6_N_BRC_EXACT`. It independently compares (i) native Z6 signed-path DP pushed through F, (ii) carrier Z3 DP with 12 images, and (iii) the exact multinomial coefficient formula. Coverage N=0…8: **50,445 native endpoint terms**, **5,480 carrier coefficient states**, with `Σ native mass=12^N` each N. The exact executed script Git blob SHA-1 is `a82b8cfb6039531aec2266e283a5277ab20f7c4c`, identical to the GitHub readback at commit `b408775b7cf6031646031aec64a07301f59d8d3c`.

This is a completed **typed current-consumer certificate**, not a substitute for the original benchmark, LP019 historical-error source attribution, 28-LP full dependency closure, independent Driver revision, native semantic checkpoint or Result acceptance.

## Continuation

- Preserve prior exact proofs/50,771 regression and already repaired V12, LP028, native-cover consumers without repetition.
- Locate original LP019 purported **wrong** signed-cancellation native caller at frozen historical source, if it exists; do not treat this correct FCC consumer as that caller. Seek actual current imports/call sites that interpret carrier N-BRC as a single native-Cell N-BRC and patch only a confirmed misuse.
- Maintain original Research lane ID and request journal. Original claim request `onhour-20261113-0118-own-x6-same-session-claim-v1` returned `SUCCEEDED` with new claim `MCP-9ce362c91287345702dd387d`; native open request `onhour-20261113-0204-own-x6-open-after-claim` was `QUEUED` at this certificate's last observation. Reconcile the **same** open request; do not reissue.
- Actual session `MCP-082892eb480e45dea6d4b9fcc0491034`, Researcher `EM-X6-FB6990`, original completed RUN `RUN-0881a7a2c2f958314cc0b5f5` remains historical and is **not** the new RUN.


## First non-native FCC carrier return: exact three-step cycle theorem

This is a direct LP019/current-consumer discriminator rather than another unrestricted auxiliary model. At length 1 the carrier return mass is zero. At length 2, every carrier-zero signed two-step word is a step immediately followed (in vector sum) by its opposite, because the six FCC images `v_i` are pairwise distinct up to sign. These are also 12 native signed-X6 two-step returns. **Length 3 is the first divergence:** the carrier endpoint zero has exactly **48 ordered signed primitive words**, while the raw native signed-X6 endpoint zero has **zero** words of odd length.

To prove 48 universally within length 3 without extrapolating, each `±v_i` belongs to exactly one of the XY, XZ and YZ carrier support families, having two nonzero coordinates. A sum of three such steps can vanish only by selecting exactly one from each family: every carrier coordinate must appear an even number of times, and with three total steps that forces all three families. Choose one sign for each of the three coordinate-pair cancellation constraints (8 solutions). For each solution permute the three distinct signed native steps in 3!=6 orders: **8·6=48**. The three steps involve three distinct native axes, so their raw six-dimensional endpoint cannot be zero. Therefore `C_3(0,0,0)=48` but `B_3^{native}(0)=0`. This establishes a minimal witness for a **carrier-only closed path** that must not be promoted to native return or positive-mass cancellation.

Independent exhaustive enumeration of all `12^3=1728` ordered length-3 primitive words using the actual frozen six carrier vectors found exactly 48 carrier-zero words, all with one step from each of the three support families; the count agrees with the already published native-vs-carrier DP certificate. Status: **AUTHOR-PROVED / EXACT FINITE ENUMERATION / UNREVIEWED / NOT_ADMITTED**.
