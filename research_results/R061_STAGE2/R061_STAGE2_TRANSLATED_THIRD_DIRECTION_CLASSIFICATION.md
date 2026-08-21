# R061 Stage 2 — Translated Third-Direction Classification

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Status

`TRANSLATED_THIRD_DIRECTION_CLASSIFICATION_PASS = true`

## 1. Translation covariance of the Stage 1 distinction

Fix translated sector `S_ij(P)` and let `k` be the third carrier direction family.

The native line identity remains

`T_{P;a,b}^{(ij)} = (P,[X_i^a X_j^b])`.

A translated carrier endpoint path containing a third-family transition is not a linearization of that trace, even when carrier relations make the terminal center coincide.

Therefore the Stage 1 classification transports exactly:

`SAME_CARRIER_ENDPOINT / DIFFERENT_NATIVE_COMPONENT_TRACE`.

## 2. Smallest translated witness

For every translated `(1,1)` trace:

- native trace representatives: `X_i X_j`, `X_j X_i`;
- the carrier reverse-third one-edge route reaches the same terminal center;
- that one-edge route contains the wrong component family and is classified

`CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`.

The classification is made by trace labels, not by one jump versus two jumps.

## 3. General same-endpoint carrier shortcut

For arbitrary `a,b>0`, let `m=min(a,b)`.

At the carrier level, `m` reverse-third edges plus the residual `|a-b|` edges in the larger active component family reach the same center endpoint as the positive `(a,b)` trace.

This gives a valid endpoint path using `max(a,b)` carrier jumps. It remains outside the native line fiber because it contains third-family carrier transitions.

Thus the translated theorem is stronger than the `(1,1)` example:

`THIRD_FAMILY_ENDPOINT_PATHS_MAY_EXIST = true`;

`THIRD_FAMILY_PATH_IN_SAME_TRANSLATED_IJ_TRACE = false`.

## 4. Deterministic replay

The checker replayed all nondegenerate translated branches with `a+b<=12` over seven starts and all three sectors:

- tested translated branches: `1,386`;
- endpoint mismatches: `0`;
- classification mismatches: `0`.
