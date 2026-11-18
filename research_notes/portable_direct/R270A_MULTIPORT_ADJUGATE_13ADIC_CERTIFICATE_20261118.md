# R270A — Labeled multi-port 13-adic adjugate certificate and coupled-port witness

2026-11-18 | AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED.
Continuation R270 in this branch; frozen scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Reuses genuine positive-rational recurrent BRC WBRC-T30..T32. This is a finite labeled port calculus theorem, not native X6 dynamics.

## Theorem A: exact modular matrix-star reconstruction

Fix an odd prime p (including 13) and a d-by-d stable nonnegative rational recurrent BRC effective port matrix W_eff, with a permitted rational nonnegative port context C that connects only visible ports. Suppose each entry of A=I-W_eff-C belongs to the local ring Z_(p), and Delta=det(A) != 0 has known valuation t=v_p(Delta)>=0. The stable visible star is S=A^(-1). Then every entry of p^t S is p-integral and

rho_p(p^t S) = rho_p(adj(A)) * rho_p(Delta/p^t)^(-1).

In particular, A modulo p^(t+1) is a sufficient exact input certificate for this normalized star matrix at the declared context and determinant depth. If Delta is a p-unit (t=0), this reduces to the ordinary field inverse of A modulo p. The port labels are retained by matrix row/column indices.

Proof: the adjugate identity A^(-1)=adj(A)/Delta holds over the rational field. Write Delta=p^t u with u a p-unit. The entrywise numerator adj(A) is p-integral, so p^t A^(-1)=adj(A)/u is p-integral, and its residue is the displayed product. Matrix entries modulo p^(t+1) determine Delta modulo p^(t+1) because determinant is a polynomial in the entries, and adj(A) modulo p is determined by A modulo p. Delta mod p^(t+1) together with the known valuation determines u mod p. QED.

**Exact scope:** The statement covers the normalized full star p^t S; selected entries can sometimes need less precision if their cofactors have extra divisibility. It assumes an exact known finite context and determinant valuation, not a uniform fixed bound over all contexts.

## Theorem B: sharpness even with two genuinely coupled labeled ports

Use two ports with positive coupling x=1/10:

W_eff(w) = [[w, 1/10], [1/10, 0]],
C(r) = [[r,0],[0,0]].

These are nonnegative rational matrices with labeled ports 1 and 2. Write a=w+r and Delta=det(I-W_eff-C)=1-a-1/100. If a<1 and Delta>0, the symmetric nonnegative transition matrix is strictly stable: I-W_eff-C has positive leading principal minor and positive determinant, hence its eigenvalues are positive; with W_eff+C nonnegative its spectral radius is <1.

Concrete pair: w0=1/5, w1=33/100, r=53/100. Initial w_i residues equal 8 modulo 13; all other entries agree. The determinants are Delta0=13/50, Delta1=13/100, hence both exact stars have
S11^0=50/13, S11^1=100/13; S12^0=5/13, S12^1=10/13.
Therefore the normalized 13*S11 residues are 11 versus 9; normalized 13*S12 residues are 5 versus 10. The port interaction is genuinely nonzero (x>0).

For every N>=1, put P=13^N, M=100P+1 and
w0=1/5, w1=1/5+P/M, r=79/100-2P/M.
Then Delta0=2P/M, Delta1=P/M, the two full port matrices agree entrywise modulo P, and the same permitted context is strictly stable for both. Nevertheless normalized P*S11 residues modulo 13 are 7 versus 1, and normalized P*S12 residues are 2 versus 4. This supplies an exact coupled-port universal-depth obstruction for every N and proves that the t+1 precision bound in Theorem A cannot be replaced by t uniformly even when port count is 2 and the ports interact.

Proof: substitution yields determinant expressions and A^(-1)=Delta^(-1)[[1,1/10],[1/10,1-a]]. Positivity: 0<P/M<1/100 makes r>0 and 1-a=1/100+2P/M (resp. 1/100+P/M), so both leading minors and determinants are positive. For p=13, M≡1, inverse 2 is 7 and inverse 10 is 4, giving (7,1) and (2,4). All-N follows symbolically. QED.

## Interpretation, validation, next problem

The R269 6474-type auxiliary value-profile quotient could be combined with a port cache, but this example proves why modulo 13^N of W_eff cannot replace the complete rational signature for arbitrary future port contexts with unbounded resonance valuation. The exact BRC-T32 W_eff remains the safe port-only signature. This is not an asserted mapping of R269's source labels to actual native BRC states.

A Python Fraction checker verifies both genuinely coupled ports, the sample, and N=1..8; local exact result PASS on 2026-11-18. The all-N and d-port assertions follow from the algebraic arguments above. No independent scientific review has been performed.

Next: classify entry-specific optimal precision via v_p(cofactor_ij) and determinant valuation under permitted contexts; test multi-port compression carrying a determinant-depth certificate and origin/port/source provenance, including whether any actual R269 source-generated map exists.