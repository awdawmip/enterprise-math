# R4 five-tail check: the branch omitting 38737

Date: 2026-11-24. Shared-context collaborative mathematical check, by the prefix collaborator, within Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. This note is not an independent project Review or a formal acceptance claim.

## 1. Scope and conclusion

R4 is the historical 43-coordinate R3 fiber with the additional condition a=0 at all 31 free prime coordinates of the proved budget-eight observer. Under the separately established four-prefix reduction, the remaining positions are

\[
n=32+36w,\qquad
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\]

This check concerns complete supplements using at most five tail primes on B and **omitting** the fixed h=2 prime 38737, where h=ord_q(2^36).

The result is closed: every such cover consists of five h=7 channels, one on each occupied row

\[
w\equiv0,1,2,3,5\pmod7.
\]

No fixed h=3 or h=4 channel can be present in this branch of a complete five-tail dictionary. The eligible h=7 inventory in R4 is exactly the five-prime set

\[
\{92737,649657,77158673929,40388473189,118750098349\},
\]

because R4 makes the four former f=7 primes 29,43,1429,5419 inactive. Thus the surviving no-38737 family assigns these five primes bijectively to the five listed residues. This gives 5!=120 phase dictionaries and 120*2^5=3840 signed CRT progression descriptions for this particular family.

The present note verifies the infinite-period mass argument and all its finite incidence inputs. The other tail branches belong to the separate `tail_proof.md` derivation.

## 2. All-prime mass bound

Delete m distinct occupied rows of B covered by h=7 channels. Denote the remaining set by R, its size by r, and its largest column and row sizes by

\[
c_5=\max_b|\{w\in R:w=b\pmod5\}|,\qquad
c_7=\max_b|\{w\in R:w=b\pmod7\}|.
\]

Mass is measured in units of one complete residue class modulo 35; thus R has mass r. A channel of period h contributes

\[
\frac{|\{w\in R:w=b\pmod{\gcd(h,35)}\}|}
{h/\gcd(h,35)}.
\tag{1}
\]

After the h=7 channels and the selected fixed h=3/h=4 channels are accounted for, every remaining available prime has mass at most

\[
E(R)=\max\{r/9,c_5/3,c_7/2,1\}.
\tag{2}
\]

This is an all-order bound. The gcd-one column has h>=9: h<=5 is old, fixed or inactive, h=6 and h=8 are killed by the R4 observer, and h=7 is handled separately. In the gcd-five column, h=5 is inactive and h=10 is killed, so h>=15. The gcd-seven column after h=7 starts at h=14. The gcd-35 column covers at most one whole point, including its possible lift-period-one case h=35. No prime-size cutoff is used.

The only selected fixed small channels in this no-h2 branch can be

\[
246241:w=1\pmod3,\qquad487824887233:w=2\pmod4.
\]

On every R their individual proportions are exactly 1/3 and 1/4. If both occur, their union proportion is exactly

\[
\frac13+\frac14-\frac1{12}=\frac12.
\tag{3}
\]

The mod-three and mod-four restrictions are coprime to 35. Consequently (3) remains exact after any number of whole mod-seven rows are deleted. It does not assume statistical independence of unspecified prime phases.

Let a be the number of selected fixed channels and p their union proportion: (a,p) is (0,0), (1,1/3), (1,1/4), or (2,1/2). There are at most 5-a-m remaining slots. Formulae (1)-(3) give

\[
\mu(\text{all selected channels on }R)
\le p r+(5-a-m)E(R)=:U(R).
\tag{4}
\]

Duplicates or empty h=7 classes spend slots without covering any new R point. Counting m as distinct nonempty rows and using (4) is still an upper bound in those cases.

## 3. Exact exclusion table

The five occupied mod-seven rows 0,1,2,3,5 of B have sizes 3,2,2,3,3, respectively. Every permissible deleted-row subset has been checked with exact rational arithmetic. In the table, the maximum ratio and the minimum gap are taken independently over all subsets of the indicated size.

| Selected fixed primes | m | Subsets checked | Maximum U(R)/r | Minimum r-U(R) |
|---|---:|---:|---:|---:|
| None | 0 | 1 | 25/39 | 14/3 |
| None | 1 | 5 | 3/5 | 4 |
| None | 2 | 10 | 9/14 | 5/2 |
| None | 3 | 10 | 3/5 | 2 |
| None | 4 | 5 | 1/2 | 1 |
| 246241 | 0 | 1 | 11/13 | 2 |
| 246241 | 1 | 5 | 47/60 | 13/6 |
| 246241 | 2 | 10 | 16/21 | 5/3 |
| 246241 | 3 | 10 | 19/30 | 5/3 |
| 246241 | 4 | 5 | 1/3 | 4/3 |
| 487824887233 | 0 | 1 | 119/156 | 37/12 |
| 487824887233 | 1 | 5 | 7/10 | 3 |
| 487824887233 | 2 | 10 | 19/28 | 9/4 |
| 487824887233 | 3 | 10 | 11/20 | 2 |
| 487824887233 | 4 | 5 | 1/4 | 3/2 |
| Both | 0 | 1 | 23/26 | 3/2 |
| Both | 1 | 5 | 4/5 | 2 |
| Both | 2 | 10 | 5/7 | 2 |
| Both | 3 | 10 | 1/2 | 2 |

All 119 nonempty-residual cases satisfy U(R)<r. The only unexcluded case is a=0,m=5, where R is empty because the five h=7 rows cover B completely. At most five tail slots then leaves no room for any additional channel.

## 4. Executed evidence and scope

Run:

```bash
python verify_no_h2_mass.py
```

The standard-library verifier executed successfully. `no_h2_mass_certificate.json` retains all 119 individual residual sets, their exact incidence maxima, mass bounds, relative ratios and gaps. It also directly verifies each fixed-channel union proportion on the complete common period 420; this is 119 finite geometry checks, not a native BRC execution.

The all-prime inference uses the analytic column bound (2), backed by the inherited complete small-order inventories and the explicit R4 zero constraints. The finite table only evaluates those universal bounds on the finite residual geometry. This distinguishes the argument from enumerating primes below a numerical cutoff.

The native semantics remain the fixed-X6 full typed integer register with T(x)=2x+1. No residue vector replaces that state, and this note makes no exact unrestricted total-cost claim from dictionary irredundancy.
