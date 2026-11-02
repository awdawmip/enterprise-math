# D25 — Exact original W216 B2 tail and its 428-prime nonzero contrast with S2304 (2026-11-02)

**AUTHOR-DERIVED EXACT ALL-PRIME OBSERVER REDUCTION / FINITE EXACT NONZERO CHECK / UNREVIEWED / NOT_ADMITTED / NOT_SOURCE_CHECKPOINT.** Original TASK `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; science input frozen `c47e13e4aba0e006366f989d6334d443f6333ae3`; research conversation `chatgpt-research-onhour-enterprise-math-20260923`.

## Source-faithful exact identity, all primes p>3

Let `w_k=(6k+1)(2k)!(3k)!/[216^k(k!)^5]`, `s_k=(8k+1)(4k)!/[2304^k(k!)^4]`, `H=(p-1)/2`, `E_W=floor((2p-1)/3)`, `E_S=floor((3p-1)/4)`. Define p-adic unit `U_{W,p}(k)=p^{-v_p(alpha_W(k))}alpha_W(k)`, where alpha is the unweighted coefficient, and the original source-tagged observer

```
B2_W(p) = sum_(k=H+1)^E_W (6k+1) U_W,p(k)  mod p,
B2_S(p) = sum_(k=H+1)^E_S (8k+1) U_S,p(k)  mod p.
```

The original factorial valuations for `0<=k<p` are
`v_p(alpha_W(k))=floor(2k/p)+floor(3k/p)` and
`v_p(alpha_S(k))=floor(4k/p)`.
Hence, on the interval `H<k<p`, each coefficient has exact valuation two through the relevant `E`, and valuation at least three thereafter.

Consequently, with `W(n)=sum_(k=0)^n w_k`, `S(n)=sum_(k=0)^n s_k`, there are exact p-adic integer congruences

```text
[W(p-1)-W(H)] / p² ≡ B2_W(p)  (mod p),
[S(p-1)-S(H)] / p² ≡ B2_S(p) = 0  (mod p),
[(W(p-1)-W(H))-2(S(p-1)-S(H))] / p² ≡ B2_W(p)  (mod p).
```

The second line is a **rigorous all-prime prior-art consequence** of Guo–Zudilin (2019), Thm 1.1, as proved in the companion source note `5ad12b69bc348227d7ea3165056aabbf886a738a`; this W-versus-S distinction is exact for the declared signed cutoff observer, independent of CM hypotheses. The W nonzero assertion below is only finite.

## Actually executed independent exact enumeration

Original factorial unit recurrence, retaining original 216 denominator and signed weight, was executed for **all 428 primes 5<=p<=3000**, covering all 8 nonzero classes modulo24. For every one, `B2_W(p) != 0 (mod p)`; in particular all **107 target primes** in classes 13/19 mod24 have a nonzero W-port while the corresponding S-port is universally zero.

Fixed examples `p -> B2_W(p)`: 13->10; 19->9; 37->20; 43->35; 61->17; 67->58; 109->16; 139->13; **373->266**; 1171->1048. The previously established original p373 W-tail/T_W=266 independently cross-checks this calculation. Exact sign/source information means the visible nonzero port cannot simply be dropped by replacing the pair with the S-model alone.

The 428-prime checker is in this commit at `research_notes/portable_direct/d25_W216_B2_428prime_exact_20261102.py`; full local executed JSON `d25_w216_B2_exploration_20261102.check.json`. Exact scope is finite enumeration; no all-prime W nonvanishing proof is claimed.

## Next direct target

The signed original double-model boundary port is now precisely `B2_W(p)` modulo p. Pursue a source-aligned formula relating that nonzero W port to the other four signed carry sources and to frozen original `Delta_p-R_p`. Use both p≡13 and 19 mod24 and retain original (model,a,b,valuation,unit,weight,carry) provenance. The native fixed p373 H0/B0 divided-power [X]U, rank, semilinear Frobenius and odd Green/Hesse remain `PENDING_OWNER/NOT_EXECUTED` at https://github.com/awdawmip/enterprise-math/issues/1559.
