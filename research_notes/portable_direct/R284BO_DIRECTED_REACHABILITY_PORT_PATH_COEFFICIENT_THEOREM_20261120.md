# R284BO — Directed-path coefficient theorem and semiconnected editable-Port sufficiency

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Independent portable research, not a native CLAIM/Result/Review.

## Frozen lineage and objective

Continue R284BM at `a2537fde3598cef07a8a31eca0b0a676d143f29e` and R284BN at `6448f2061ecf5154d5999d2b014747f6c724410b`. These proved a sharp n−1 editable-edge lower bound and the complete n=3 connectedness criterion. The open question for n≥4 is which connected graph orientations suffice for full matrix identification.

Let E be a set of directed editable off-diagonal positions on vertices V={0,...,n−1}, n≥2. The exact formal observer is

```text
F_C^E(d,z) = det(diag(d_0,...,d_{n-1}) - C - sum_{(i,j) in E} z_ij E_ij).
```

All variables are algebraically independent; C has strictly positive rational entries unless stated otherwise. The observer is auxiliary and does not assert a native P000/X6 readout.

## Theorem BO1 — Every directed simple path exposes its reverse endpoint coefficient

Take any directed simple path `P=(v_0→v_1→...→v_l)`, length l≥1, whose arrows belong to E. Let W={v_0,...,v_l}, and set

```text
m_P = (product_{r=0}^{l-1} z_{v_r,v_{r+1}})
      (product_{u not in W} d_u).
```

Then the exact coefficient identity over Z[C] is

```text
[m_P] F_C^E = -C_{v_l,v_0}.
```

**Proof.** Each of the l specified z factors forces the corresponding row v_r to use column v_{r+1}. Each specified d_u for u outside W forces row u to use column u. The only unassigned row is v_l and the only unassigned column is v_0. Hence precisely one Leibniz determinant term contributes: the length-(l+1) cycle v_0→v_1→...→v_l→v_0, whose last entry is `-C_{v_l,v_0}`. Its permutation sign is `(-1)^l`, and its l+1 selected matrix entries each have sign −. Their product is therefore `(-1)^l (-1)^{l+1} C_{v_l,v_0}=-C_{v_l,v_0}`. All other editable z variables have exponent zero in m_P. QED.

The identity holds before any positivity assumption; it also holds as a formal integer polynomial and after reduction in any field.

## Theorem BO2 — Pairwise directed reachability suffices for identifiability

Suppose the directed graph (V,E) is **semiconnected**: for each unordered pair {i,j}, at least one of i→*j or j→*i is reachable by a directed path. Then the map `C↦F_C^E` is injective on strictly positive rational n×n matrices.

**Proof.** The diagonal entries are obtained from `[product_{k!=i} d_k]F_C=-C_ii`. The two-vertex principal coefficients give `[product_{k notin {i,j}} d_k]F_C=C_ii C_jj-C_ij C_ji`, so every product `C_ij C_ji` is known. For any pair {i,j}, choose a directed path from one to the other, available by semiconnectedness. BO1 gives the reverse entry `C_{target,source}` exactly. Strict positivity makes it nonzero, so divide the already known product to recover the other entry. Thus every entry of C is reconstructed. QED.

A directed Hamiltonian path `0→1→...→n−1` is semiconnected and has exactly n−1 arrows. Combining R284BM's disconnected-graph lower bound with BO2, a directed Hamiltonian path is a **second family of edge-count-optimal observers**, besides the outgoing directed star. An arbitrary outward star need not be semiconnected but remains sufficient via the distinct R284BM coefficient reconstruction; semiconnectedness is a sufficient, not claimed necessary, condition.

## Corollary BO3 — One noiseless finite-field scalar

For fixed n≥2, H≥2 and a semiconnected E, there exists a prime p and a fixed single setting (d,z) over F_p for which one noiseless residue F_C^E(d,z) mod p uniquely identifies every C∈{1,...,H}^{n×n}.

Proof: BO2 makes all integer difference polynomials Q=F_C−F_C' nonzero. The degree-n homogeneous part of F_C is `det(diag(d)-sum zE)`, independent of C, so deg Q≤n−1. Every coefficient of F_C has absolute value at most M=n!(H+2)^n, by Leibniz ℓ¹ norm, so p>2M preserves a nonzero coefficient of each Q. There are J=binom(H^(n²),2) candidate pairs. For independent uniform controls in F_p, Schwartz–Zippel and a union bound give total collision probability at most J(n−1)/p, which is strictly below one for any prime p>max{2M,J(n−1)}. One fixed setting exists. Candidate-table decoding may remain exponential; the corollary is noiseless and does not assert a sharp modulus.

## Exact checks

The Python standard-library checker uses the R284BM symbolic Leibniz determinant routine. On the directed Hamiltonian path, it confirms all coefficients [m_P] for every i<j:
- n=2, H=2: 16 complete matrices, 16 exact path coefficient assertions.
- n=3, H=2: 512 complete matrices, 1,536 exact assertions.
- n=4: 72 seeded positive matrices with entries in {1,2,3,4}, 432 assertions.
- n=5: 12 seeded matrices, 120 assertions.
- Separately for all 65,536 four-by-four binary matrices, the reconstruction signature (diagonals, lower-triangular entries, reciprocal products) is distinct, by exact integer enumeration. This latter test checks the algebraic reconstruction encoding, not all 65,536 determinant polynomials.

The general proof is combinatorial/algebraic and does not depend on empirical extrapolation. See `R284BO_directed_path_coefficient_checker.py` and `R284BO_directed_path_coefficient_verification.json`.

## Next scientific obligation

Determine whether the undirected connectedness criterion is sufficient in n≥4 for editable-Port orientations with incomparable reachability (for instance mixed-in/mixed-out trees). Search for exact positive-matrix collisions and develop a full coefficient-recovery method if none are found. Keep other graph conditions, source-side modular measurement cost, and bounded-noise decoding as separate questions. No P000 or native X6 claim is revised.
