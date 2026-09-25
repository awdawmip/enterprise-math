# B11 contiguous-Dixon closure — neutral portable evidence

Status: `UNREVIEWED / NOT_ADMITTED / NOT_A_TASK_CHECKPOINT / NOT_A_RESULT / REGISTER_PENDING`

Actual ChatGPT thread: `6ab33b2f-3230-83ee-b3e2-e6e98fd1cbad`  
Stable logical ID for this real thread: `chatgpt-thread-6ab33b2f-3230-83ee-b3e2-e6e98fd1cbad`  
Local role ID: `LOCAL-TR-6ab33b2f-3230-83ee-b3e2-e6e98fd1cbad`  
The local role ID is not a service-issued Researcher-ID and conveys no CLAIM/session/run authority.

Input evidence:
- Source archive commit: `2d1b14c4289f99e53cee3987c984f5f02ea6e108`
- Exact prior message: `control_plane_reconciliations/recovered_chat_evidence/20260925/raw/hourly_d25/043_27511aa9-1b08-432f-a0c3-ae2449b5a947.md`
- Original message ID: `27511aa9-1b08-432f-a0c3-ae2449b5a947`
- Original message SHA256: `b9a15e307648b4ed398710695f7fa8dbafa9c236e3cbc9f7214a053b984c56fd`
- Governing D25 native pointer remains `authority_granted=false`; this note does not alter it.
- Historical E267A2/MCP-70a... identity is provenance only and is not used here.

## Exact open unit

Let
[
p=6m+1
]
be prime (hence this covers the target classes (p\equiv13,19\pmod{24})). Define
[
T_p=\sum_{j=1}^{m}\frac{(-m)_j}{(3m+1)_j(3j-1)}
]
and
[
q_p(2)=\frac{2^{p-1}-1}{p}.
]

The recovered message 043 reduced the WZ boundary problem to
[
\boxed{T_p\stackrel{?}{\equiv}\frac23q_p(2)\pmod p.}
\tag{B10}
]
Equivalently, with
[
S_m:={}_3F_2\!\left[
\begin{matrix}-m,1,-1/3\\3m+1,2/3\end{matrix};1
\right],
]
one has (T_p=1-S_m), so the target is
[
\boxed{S_m\equiv1-\frac23q_p(2)\pmod p.}
\tag{B11}
]

## Step 1 — a coefficientwise mod-p contiguous-Dixon move

Because (p=6m+1),
[
(3m+1)-\left(m+\frac23\right)=\frac p3.
]
For every (0\le j\le m), all factors in
((3m+1)_j) and ((m+2/3)_j) are (p)-adic units. Hence coefficientwise
[
\frac1{(3m+1)_j}\equiv
\frac1{(m+2/3)_j}\pmod p.
]
Therefore
[
S_m\equiv S_m^*\pmod p,
]
where
[
S_m^*:=
{}_3F_2\!\left[
\begin{matrix}-1/3,1,-m\\2/3,m+2/3\end{matrix};1
\right].
\tag{1}
]

This is exactly the contiguous-Dixon pattern
[
{}_3F_2\!\left[
\begin{matrix}a,b,c\\2+a-b,1+a-c\end{matrix};1
\right]
]
with
[
a=-\frac13,qquad b=1,qquad c=-m.
]

## Step 2 — remove the b=1 singularity in contiguous Dixon

Kim–Rakha–Rathie, *Extensions of Certain Classical Summation Theorems for the Series 2F1, 3F2, and 4F3 with Applications in Ramanujan’s Summations*, IJMMS 2010, Article ID 309503, formula (4.8), gives the needed contiguous Dixon summation for generic (b).

Taking the removable limit (b\to1) in that formula gives
[
{}_3F_2\!\left[
\begin{matrix}a,1,c\\1+a,1+a-c\end{matrix};1
\right]
=
\frac a2\left[
\psi\!\left(\frac a2+\frac12\right)
-\psi\!\left(\frac a2\right)
+\psi\!\left(\frac a2-c+1\right)
-\psi\!\left(\frac a2-c+\frac12\right)
\right].
\tag{2}
]

For completeness, the limit is obtained because the two gamma-ratios inside formula (4.8) both equal (1) at (b=1); their first-order difference supplies the digamma bracket in (2), while the remaining prefactor tends to (a/2).

Substitute (a=-1/3, c=-m):
[
S_m^*
=
-\frac16\left[
\psi(1/3)-\psi(-1/6)
+\psi(m+5/6)-\psi(m+1/3)
\right].
\tag{3}
]

Use
[
\psi(-1/6)=\psi(5/6)+6,
]
[
\psi(m+5/6)-\psi(5/6)
=
6\sum_{r=0}^{m-1}\frac1{6r+5},
]
and
[
\psi(m+1/3)-\psi(1/3)
=
3\sum_{r=0}^{m-1}\frac1{3r+1}.
]
All non-rational digamma constants cancel. Thus the exact finite identity is
[
\boxed{
S_m^*
=
1-
\sum_{r=0}^{m-1}\frac1{6r+5}
+
\frac12\sum_{r=0}^{m-1}\frac1{3r+1}.
}
\tag{4}
]

No asymptotic or numerical step occurs here.

## Step 3 — reflect the two residue-class harmonic blocks

Set
[
A_m:=\sum_{r=0}^{m-1}\frac1{6r+5},
\qquad
B_m:=\sum_{r=0}^{m-1}\frac1{3r+1}.
]

For (0\le r<m),
[
p-(6r+5)=2\bigl(3(m-r-1)+1\bigr).
]
Hence modulo (p),
[
A_m\equiv-\frac12B_m.
]
Equation (4) becomes
[
\boxed{S_m^*\equiv1+B_m\pmod p.}
\tag{5}
]

## Step 4 — identify B_m with the base-2 Fermat quotient

Let
[
I_m:=\sum_{k=m+1}^{2m}\frac1k.
]
Since
[
p-3k
]
runs, in reverse order, through
[
1,4,7,\ldots,3m-2,
]
we have
[
\frac13 I_m
=
\sum_{k=m+1}^{2m}\frac1{3k}
\equiv
-B_m\pmod p.
]
Therefore
[
\boxed{B_m\equiv-\frac13I_m\pmod p.}
\tag{6}
]

It remains to evaluate (I_m). Use the standard Skula–Dobson–Ichimura generalization of Eisenstein’s Fermat-quotient congruence. In the notation
[
s_p(j,N)=\sum_{jp/N<r<(j+1)p/N}\frac1r,
]
their theorem gives, for (N=3),
[
4q_p(2)\equiv-[s_p(0,6)+s_p(2,6)]\pmod p.
]
For (p=6m+1),
[
s_p(0,6)=H_m,
\qquad
s_p(2,6)=H_{3m}-H_{2m}.
]
Eisenstein’s half-range congruence is
[
2q_p(2)\equiv-H_{3m}\pmod p.
]
Substitution yields
[
4q_p(2)
\equiv
-H_m-H_{3m}+H_{2m}
=
I_m+2q_p(2),
]
hence
[
\boxed{I_m\equiv2q_p(2)\pmod p.}
\tag{7}
]

Combining (6) and (7),
[
\boxed{B_m\equiv-\frac23q_p(2)\pmod p.}
\tag{8}
]

## Step 5 — B11 and T_p

From (5) and (8),
[
S_m^*
\equiv
1-\frac23q_p(2)
\pmod p.
]
Step 1 gives (S_m\equiv S_m^*\pmod p). Therefore
[
\boxed{
{}_3F_2\!\left[
\begin{matrix}-m,1,-1/3\\3m+1,2/3\end{matrix};1
\right]
\equiv
1-\frac23q_p(2)
\pmod p.
}
\tag{B11-PROVED}
]

Since (T_p=1-S_m),
[
\boxed{
T_p
\equiv
\frac23q_p(2)
\pmod p.
}
\tag{B10-PROVED}
]

Thus the exact OPEN unit in recovered message 043 is closed, in fact for every prime (p\equiv1\pmod6), which strictly contains the target residue classes (13,19\pmod{24}).

## Evidence and proof-strength boundary

- The contiguous-Dixon input is an external published identity: Kim–Rakha–Rathie (2010), formula (4.8), specialized through the removable (b\to1) limit.
- The Fermat-quotient input uses Eisenstein plus the Skula–Dobson–Ichimura finite-interval generalization.
- The remainder is finite algebra in \(\mathbf F_p\).
- No enlarged prime scan is used as proof.
- No claim is made here that the entire D25 LIFT/JT2 is formally admitted. Recovered message 043 shows B11 is one WZ-boundary sublemma; other endpoint material outside B11 must still be consumed according to the preserved chain.
- Status remains `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.
- Do not repeat B1–B10, the WZ shift, finite-Clausen audit, or this B11 derivation unless integrity review finds a specific defect.

## Immediate next mathematical action after lawful registration

Consume B11 as proved portable evidence, return to the preserved WZ second-digit normal form, and determine whether the remaining endpoint lemma (the recovered (E_p\) / (S_{4m}(2m)) side) is already closed by another preserved message or remains the sole LIFT residue. Do not infer JT2 closure solely from this note.
