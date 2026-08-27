# P022 Observation-History Composite Franel Escape — Research Checkpoint

Status: `ACTIVE / NONTERMINAL / EXACT_DOUBLE_HORIZON_REDUCTION_FROZEN`

Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-2346F5D3E731ED56DB0A`  
Claim: `chatgpt-p022obs-20260827-1645`  
Researcher: `EM-P022OBS-D5D438`

## Current durable advance

The Driver-routed `q=3r-1` boundary result has been consumed rather than replayed.
Writing

\[
M=3m,\qquad r=2M=6m,\qquad q=6M-1=18m-1,
\]

the accepted residue `q|F_(6m)` is now equivalent to two additional exact
integer forms.

For general prime `p=6M-1`, the existing Bailey tail

\[
T_M={}_3F_2(-M,-M,-M;-3M,3M;1)
\]

satisfies

\[
T_M=E_M K_M,
\]

with the p-adic unit

\[
E_M=\frac23\frac{M!(2M)!(2M-1)!(3M-1)!}{(4M-1)!^2}
\]

and the denominator-free double-horizon kernel

\[
K_M=\sum_{j=0}^{2M}(-1)^j
\binom{2M}{j}\binom{M+j}{j}\binom{4M+j-1}{j}.
\]

Moreover, modulo `p=6M-1`, binomial complementation removes the alternating
sign and the terminal `j=2M` term vanishes, giving

\[
K_M\equiv W_M\pmod p,
\]

\[
W_M=\sum_{j=0}^{2M-1}
\binom{2M}{j}\binom{M+j}{j}\binom{2M-1}{j}.
\]

Therefore the live boundary obstruction is exactly

\[
\boxed{
q\mid F_{6m}
\iff
K_{3m}\equiv0\pmod q
\iff
W_{3m}\equiv0\pmod q.
}
\]

The new integer kernel is also exactly unit-equivalent to the older owner
integerization `U_M`:

\[
K_M=
\frac{\binom{4M-1}{M}}
{2\binom{2M-1}{M}}U_M.
\]

Thus no new zero locus is invented; the gain is a second combinatorial geometry
and, crucially, a sign-free `2M`-horizon form.

## Current unfinished unit

The hard target is still open.  The smallest unfinished unit is

\[
W_{3m}\not\equiv0\pmod{18m-1}
\]

under the admissible P022 twin-boundary prime conditions.

The active next attack is the exact three-section

\[
W_{3m}=W_m^{(0)}+W_m^{(1)}+W_m^{(2)},
\]

obtained by splitting the sign-free horizon by `j mod 3`.  Over `F_(q^2)` this
is a root-of-unity filter at a primitive cube root.  Because `q=5 (mod 6)`,
Frobenius exchanges the two nontrivial cube roots, matching the already-frozen
period-two Dwork/Galois orbit of the P022 cyclotomic hypergeometric datum.

No all-m nonvanishing theorem is claimed yet, and no finite census is promoted
to proof.
