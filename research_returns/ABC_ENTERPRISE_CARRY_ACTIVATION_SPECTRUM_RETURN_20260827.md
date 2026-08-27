# ABC Enterprise Carry-Activation Spectrum - Research Return

Status: `FROZEN RESEARCH RETURN / EXACT_OBSTRUCTION`
Task-ID: `RS-ABC-ENTERPRISE-CARRY-ACTIVATION-SPECTRUM`
Publication: `TP2-216D433F311CA5D7AFAC`
Researcher-ID: `EM-ABC2-1C96B2`
Claim: `chatgpt-abc2-20260827-1659`
Execution branch: `research/abc-enterprise-carry-activation-spectrum-em-abc2-1c96b2`
Execution base: `d8687690624bcf1870a28b28b6e4541770852b38`

## Verdict

`EXACT_OBSTRUCTION`

Hard target:

`ABC_CARRY_ACTIVATION_ENERGY_THEOREM_OR_OBSTRUCTION_FROZEN / MET`

For every prime `p` and every integer `k>=1`, set `P=p^k` and take the primitive triple

`(a,b,c)=(1,P-1,P)`.

For the task-frozen carry statistic

`h_p(n)=v_p(binomial(nc,na))-v_p(c)`

and first activation

`tau_p=min{n>=1 : h_p(n)>0}`,

the following exact formulas hold:

`h_p(n)=0` for every `1<=n<=P`;

`h_p(P+1)=k`;

therefore

`tau_p=P+1=p^k+1=c+1`.

Consequently the controlled-window energy

`E_p(W)=sum_{n=1}^W h_p(n)`

satisfies

`E_p(W)=0` for every `W<=p^k`.

This is an infinite theorem-level obstruction, not finite evidence.

## Proof

For the family above,

`h_p(n)=v_p(binomial(nP,n))-k`.

The exact identity

`binomial(nP,n)=P*binomial(nP-1,n-1)`

and `v_p(P)=k` give

`h_p(n)=v_p(binomial(nP-1,n-1))`.

Now assume `1<=n<=P`. Since

`nP-1=(n-1)P+(P-1)`

and `0<=n-1<P`, the lower `k` base-`p` digits of `nP-1` are all `p-1`, while the bottom index `n-1` has no digits above position `k-1`. Every bottom digit is therefore at most the corresponding top digit. By Lucas' theorem,

`binomial(nP-1,n-1) != 0 (mod p)`,

so `h_p(n)=0`.

At `n=P+1` the reduced binomial is

`binomial(P^2+P-1,P)`.

By Kummer's theorem its `p`-adic valuation is the number of carries when adding `P` and `P^2-1`. In base `p`, `P` has one digit `1` at position `k`, while `P^2-1=p^(2k)-1` has digit `p-1` in positions `0,...,2k-1`. A carry starts at position `k`, propagates through positions `k+1,...,2k-1`, and stops at position `2k`. There are exactly `k` carries. Hence

`h_p(P+1)=k>0`.

Together with the zero prefix this proves `tau_p=P+1`.

## No-go scope

The prime `p` is in `rad(abc)` and appears in `c` with exponent `k`, yet its normalized carry channel is silent throughout the full natural window `n<=c`.

Therefore all of the following unqualified claims are false:

1. every radical-support prime must make a positive carry payment by `n<=c`;
2. every support prime must activate in a window `W(p)` independent of `v_p(c)`;
3. every support prime must activate in a fixed-exponent window `W<=p^A` independent of `k`.

For (3), choose `k>A`; then `W<=p^A<p^k=P`, while `E_p(W)=0`.

This obstruction does not refute aggregate energy from other prime channels, a genuinely interior/balance-conditioned theorem excluding this family, or windows explicitly allowed to cross `p^{v_p(c)}+1`.

## Regression

Checker:

`scripts/check_abc_enterprise_carry_activation_spectrum.py`

Machine certificate:

`research_artifacts/ABC_ENTERPRISE_CARRY_ACTIVATION_SPECTRUM/carry_obstruction_certificate.json`

The checker uses exact Legendre valuations and replays 20 cases:

`p in {2,3,5,7,11}`, `1<=k<=4`.

All 20 cases verify the zero prefix, `h_p(p^k+1)=k`, and `tau_p=p^k+1`. These runs are regression only; the infinite result is proved above.

## Driver recommendation

Accept at `EXACT_OBSTRUCTION` strength. Freeze the family theorem above; reject unqualified per-support-prime early-activation claims; allow successors only if they are explicitly aggregate, interior-conditioned, or use a window with explicit dependence on `v_p(c)`.

Do not promote this task alone to Foundation/native-plane status.

Hard block: `NONE`.
