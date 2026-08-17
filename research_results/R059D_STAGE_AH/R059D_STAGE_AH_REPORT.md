# R059D Stage AH — N Motzkin Boundary-Word Autonomous Growth Law

Researcher-ID: `EM-R059D-AH-7B1EFD`

Task-ID: `RS-R059D-STAGE-AH-N-MOTZKIN-WORD-AUTONOMOUS-GROWTH-LAW`

Taskbook source: `134eec2e1482c8edeb2fbe03a4ab6e012d1f9fd1`

Frozen source main: `adc59649c9c8d9544037ec8972b4c80b71e9b14a`

Accepted AG owner head: `5063495ff0df643890cd1f4c72ffd2077161c13d`

## Primary disposition

`FULL_N_MOTZKIN_WORD_FORWARD_GENERATOR_PROVED`

Stage AH closes the first complete integer-only N-circle generation chain.

## 1. Exact autonomous word generator

The successful route is a constant-size boundary residual state, not a 2D occupancy scan and not a stored word table.

For `r>0`, initialize

`a=r, b=0, rho=-4`.

While `a-b>1`:

- `rho>=0`: emit `1`; update `rho<-rho-3(a+2b+3)`, `b<-b+1`;
- `rho<0`: emit `2`; update `rho<-rho+3(a-b-3)`, `a<-a-1`, `b<-b+1`.

If termination has `a-b=1`, insert a central `2`. Complete the right half by reversing the emitted half and mapping `1<->3`, `2->2`.

This produces the exact canonical `W_N(r)` for every integer `r>=0`.

Runtime contains no occupancy query, source `Q`, floating point, sqrt, pi, trigonometry, word table, jump table or radius-specific tuning.

## 2. Proof mechanism

AG gives, on the left half `a>=b`,

`L(a,b)=3(a^2+ab+b^2)-3a+1`,

with selection iff `L(a,b)<=3r^2`.

The column predicate is strictly increasing:

`L(a,b+1)-L(a,b)=3(a+2b+1)>0`.

And for `a-b>=2`,

`L(a-1,b+1)-L(a,b)=3(b-a+2)<=0`.

Hence from a selected left boundary point the diagonal successor is always selected, while the vertical successor decides whether the next outer-boundary symbol is `1` or `2`.

Define

`rho=3r^2-L(a,b+1)`.

Initially `rho=-4`. The two exact finite-difference identities are

`rho_1'=rho-3(a+2b+3)`,

`rho_2'=rho+3(a-b-3)`.

Therefore the runtime never has to evaluate `L` or query the AG support predicate. The residual carries exactly the necessary decision state.

Reflection `(a,b)<->(b,a)` proves that the right half is the reverse/symbol-swapped image of the left half.

## 3. Structural results

Discovery audit `r=1..512` confirms and the proof explains:

- all `1` events precede all `3` events;
- the word is determined by one left half plus a parity center rule;
- center is `2` exactly in the odd-length case;
- left-half alphabet is `{1,2}`, right-half alphabet is `{2,3}`;
- simple insertion-only growth is false: first counterexample is `W_11` not being a subsequence of `W_12`;
- insertion/deletion distance between consecutive words reaches 45 at `r=412` in discovery.

Thus a nonlocal-looking word reorganization is nevertheless controlled by a constant-size integer residual state.

## 4. AG/AF closure

Because the generated word equals the canonical N word, AG immediately gives

`#1=#3=J_N(r)=floor(alpha*r+1/3)`,

`#2=r-J_N(r)`,

`|W_N(r)|=r+J_N(r)`.

Using the frozen AF height convention, `B` is obtained by summing current Motzkin height immediately before each `a`-decreasing symbol `2` or `3`.

Then exactly

`D=2r+1`,

`C=6r+6J=6|W|`,

`V=1+3r(r+1)+6B`.

So the autonomous chain is now

`r -> W_N(r) -> (B_N,J_N) -> (D_N,C_N,V_N)`.

## 5. Full D6 circle generator

From `(r,0)`, execute the generated word to obtain the first-sector vertex path ending at `(0,r)`.

Using

`R(a,b)=(-b,a+b)`,

concatenate the six rotated sector paths. Adjacent sectors share only their axis endpoint and `R^6=id`, producing one locally adjacent closed D6 boundary with exactly `C` edges.

Canonical API:

`generate_enterprise_circle_N(r) -> {W,B,J,D,C,V,sector_vertices,full_boundary}`.

The API is integer-only at runtime.

## 6. State sufficiency

The auxiliary state `(a,b,rho)` is a constant number of integers, plus the word prefix being emitted.

True minimality is not claimed. AF's lower bound remains binding: scalar `J` alone is insufficient to determine the word or `B`.

Freeze:

`CONSTANT_SIZE_SUFFICIENT_AUXILIARY_STATE_PROVED__MINIMALITY_OPEN`.

## 7. Holdout and extended replay

The generator definition and source were frozen before holdout.

Untouched `r=513..4096`:

- complete word mismatches: `0`;
- AG count mismatches: `0`;
- Motzkin failures: `0`.

Additional exact checkpoints:

- `r=8192`: word equality PASS; `J=1267`, `B=7019457`;
- `r=16384`: word equality PASS; `J=2534`, `B=28078005`.

Finite replay validates implementation only; theorem status comes from the residual-invariant proof.

## 8. Checker

Deterministic mathematical/implementation replay before external Git-history gate:

`146779/146779 PASS`

Digest:

`a63fa7ac7bf014ef1c91a0c27613ecef9bab8d360c7379224637a2b11c981c48`.

## 9. Remaining boundaries

AH closes the N-side complete integer circle generator for the frozen N resolver.

It does **not** prove:

- N/C resolver-independence or unique Enterprise circle selection;
- a C word-growth theorem;
- information-theoretic minimality of `(a,b,rho)`;
- any classical-pi theorem.

No AI or later stage is consumed.

`STOP_FOR_DRIVER_REVIEW`
