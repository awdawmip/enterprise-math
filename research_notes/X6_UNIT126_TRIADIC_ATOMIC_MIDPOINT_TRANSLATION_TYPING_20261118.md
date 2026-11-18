# X6 Unit126 — exact type domain and translation defect of the original triadic midpoint helper

**Date:** 2026-11-18. **Parent objective:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`; **publication:** `TP2-B4A441B23DA3159232C2`. **Author Research lane:** `chatgpt-research-onhour-enterprise-math-20260923`, Researcher `EM-X6-FB6990`. **Status:** AUTHOR-PROVED / EXACT FINITE PYTHON EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Previously uninspected actual original caller

At the 2026-11-18 current Source, `experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py`, **Git blob `d5f6dfcfd0dedbe46feae3bc1b227185af417c2f`**, defines `midpoint_options` at **lines 54–57**. It checks the two native quantities

```python
brc.shortest_event_count(sub(b,a)) == 2
brc.shortest_path_multiplicity(sub(b,a)) == 2
```

and returns `(ZERO, add(a,b))`. Those BRC kernels are imported at lines 9–15 from the actual six-axis `signed_brc.py` (Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176` at frozen input `59538f585d037d09ef687b28715c4bc1a3f9fe03`). Call sites at **lines 67–70** supply signed unit vectors `a=s_i e_i`, `b=s_j e_j` for distinct axes in a triad. These source calls satisfy the extra condition below. Lines 71–78 test their common ZERO intermediate. Thus **all 480 three-pair cases for 160 signed triad types are correct** on their actually supplied inputs.

## Sharp all-input typing theorem

Let `a,b` be **raw six-component signed integer Cell coordinates relative to the same chosen anchor**, `d=b-a`, and suppose that the native shortest length and BRC satisfy `L(d)=2`, `B_min(d)=2`. This hypothesis holds exactly when `d=s_i e_i+s_j e_j` for two *distinct* named native axes `i != j`, each sign in `{-1,+1}`. The two shortest one-step intermediate Cells are precisely

```text
M_native(a,b) = {a+s_i e_i, a+s_j e_j}.
```

Let the existing helper's purported midpoint set be `M_old(a,b)={ZERO,a+b}`. Then under the displayed hypotheses,

```text
M_old(a,b) = M_native(a,b)  <=>  ||a||_1 = ||b||_1 = 1.
```

**Proof:** Every native geodesic from `a` to `b` must consist of the two distinct signed native steps, yielding exactly the displayed intermediates, and the pinned native kernel's multinomial returns `2!/(1!1!)=2`. If the helper is correct, it contains `ZERO` as a genuine intermediate. Necessarily the native displacement from `a` to ZERO and from ZERO to `b` each has length one, hence `||a||_1=||b||_1=1`. Conversely, when `a` and `b` are signed unit neighbors of the same anchor and `B_min(b-a)=2`, they lie on distinct axes. Their genuine intermediates are ZERO and `a+b`, exactly the helper's output. This is an equality of actual named primitive paths, not an assumed Euclidean plane or a new global distinguished origin.

**Translation-covariance counterexample:** `a=(1,0,1,0,0,0)`, `b=(0,1,1,0,0,0)`. The displacement is `(-1,1,0,0,0,0)`, so the original native preconditions `L=2`, `B_min=2` both pass. The old helper incorrectly returns `{(0,0,0,0,0,0),(1,1,2,0,0,0)}`, while the exact shortest intermediate Cells are `{(0,0,1,0,0,0),(1,1,1,0,0,0)}`. Neither originally returned point is a geodesic midpoint. The counterexample is the translation by `+e_2` (zero-based index 2) of the legitimate anchored pair `(e_0,e_1)`.

A domain-correct general implementation must compute intermediates from the two nonzero components of `b-a`, rather than presume both endpoints are unit neighbors of ZERO. Alternatively, the existing helper is correct as a **restricted anchored signed-triad helper** provided the anchor/endpoint precondition is explicitly enforced. No original producer code was changed.

## Actual executable finite certificate and strength

The new independent checker preserves the exact algebra of source lines 54–57 and the pinned native BRC formulas, and additionally computes the true primitive-step intermediate set directly. It was executed in CPython **normal, `-O`, `-OO`**; all three exit codes were zero, and the output bytes agreed (SHA256 `fb1c14f4752be309b43ff3a93c97efbb4b3c571f7acc31cea7013b2dceec40c8`).

It exhausts all `3^6=729` signed source anchors `a in {-1,0,1}^6` and all `15*4=60` two-distinct-axis signed displacements, giving **43,740 legal (a,b) ordered test pairs**. Among them **120** old-helper outputs are correct and **43,620** are wrong; the above iff criterion has **zero violations**. The same checker separately examines all **160 × 3 = 480 actually sourced signed-triad caller pairs**, with **zero errors**. The universal statement is proved symbolically; the finite census validates the exact tested domain.

This is a **source-line-faithful independent executable reproduction**, not a complete import/execution of the original 172-line script; `full_source_import_executed=false` is recorded in the machine certificate. This unit did not execute or alter the original R063/Helly C3/C4 six-file 512-case benchmark, nor claim independent admission. It adds a precise reusable caller contract to the 28-LP typed-consumer audit, relevant to LP-019/020/023/026. It does not locate the still-unverified historical LP011 wrong argmax or LP019 subtraction alleged callsites.

## Source, artifacts, continuation

Original source location: `experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py:54-57,67-78` @ blob `d5f6dfcfd0dedbe46feae3bc1b227185af417c2f`. Exact pinned kernel: `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` @ blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.

Executable certificate: `research_checks/X6_UNIT126_TRANSLATED_TRIAD_MIDPOINT_CHECK_20261118.py` and `research_checks/X6_UNIT126_TRANSLATED_TRIAD_MIDPOINT_RESULTS_20261118.json`. Parent frozen science remains on `59538f585d037d09ef687b28715c4bc1a3f9fe03` (historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`).

User's own claim/run historical references: SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-3e221a50dc8818f914e228f6`, RUN `RUN-95866d78d35721116c362956`. Native Units123–125 original request `onhour-20261118-1540-x6-own-units123-125-native-progress-v1` was conclusively SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED at Source `279d1f889449404257c497da9ae861664d97a75b`. Current exact continuation was requested under original ID `onhour-20261118-1604-x6-exact-own-cont-v1` and returned SUCCEEDED / OWN_RECORDED_RUN_AVAILABLE. New Unit126 proof/certificate persistence and researcher activity must be separately distinguished from native semantic PROGRESS and independent Driver review. The next smallest scientific unit is to inspect another *actual* downstream consumer of this midpoint helper or a named LP-011/019/R061/R062 caller with source:line, and produce a typed disposition based on its real inputs. Original R063 author benchmark has separate independent review Issue #2416.
