# X6 LP028 / R063 — full signed six-axis N=2500 free-shortest BRC census

Date: 2026-11-15 18:00 Asia/Hong_Kong. Parent: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Status: AUTHOR-EXECUTED / EXACT FINITE / NONBLIND / UNREVIEWED / NOT_ADMITTED. This 18:00 full-X6 scientific result is distinct from the earlier separately safety-denied 17:00 prose write, which remains untouched.

## Model and frozen source

Freeze P000 V5 at awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json. Select a genuine Cell and the six named signed native primitive spatial axes. This computation covers free shortest signed coordinate words for integer displacement \(z\in\mathbb Z^6\) with \(G(z)=\sum_{i=1}^6 z_i^2=2500\), \(L(z)=\sum_i |z_i|\), \(s(z)=\#\{i:z_i\neq0\}\), and positive natural BRC weight \(B(z)=L(z)!/\prod_i |z_i|!\). This defines the exact calculation; it does not count unspecified extra event/history states. Any selected three-axis chart is a proper restriction of this X6 signed coordinate population.

## Exact certificate: full six-axis population

| Nonzero axes | Signed endpoints | Total free shortest paths |
|---:|---:|---:|
| 1 | 12 | 12 |
| 2 | 240 | 6641732296455342852360 |
| 3 | 1,920 | 537215990205201455725508268665412948864000 |
| 4 | 273,840 | 630810905295749032837454653024105990097472710091386723095680 |
| 5 | 7,610,880 | 185236584658961377307180343457047096110221674854349189331422682431803176151040 |
| 6 | 94,652,160 | 46263931428930653405667681196839678797450251064953349516132813155149823035315096473061301985280 |
| **Total** | **102,539,052** | **46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372** |

Maximum signed free shortest-word length at this norm is 122.

The existing all-pair radius-50 X6 result is independently recovered at supports 1+2: 252 endpoints and 6641732296455342852372 shortest paths. The prior signed selected-three-axis N=2500 result is independently recovered as 150 endpoints and 26860799510260072787603759892561716013678 paths. The new information includes the exact 94,652,160 endpoints using all six axes, absent from those earlier restricted observers.

## Constructive proof and two independent verifications

Define \(A_d(q,\ell,s)\) as the total positive shortest-word mass among signed \(d\)-axis endpoints of squared norm \(q\), length \(\ell\), and support size \(s\). Start \(A_0(0,0,0)=1\). For an adjoined axis with absolute integer displacement \(k\ge0\),

\[
 A_{d+1}(q+k^2,\ell+k,s+[k>0])
 \mathrel{+}= (2-\mathbf1_{k=0})\binom{\ell+k}{k}A_d(q,\ell,s).
\]

Restrict \(k\le\lfloor\sqrt{2500-q}\rfloor\), iterate six axes, then select \(q=2500\). Induction proves coverage and exactness: every integer coordinate is uniquely represented by its absolute value and sign (two choices for nonzero values); any new shortest primitive-axis word is uniquely a shuffle of the old \(\ell\) words with \(k\) identical new-axis steps. The number of these shuffles is the stated binomial coefficient. Omitting length and binomial gives an exact signed endpoint-count recurrence.

An independent \(3+3\) reconstruction enumerated all nonnegative absolute triples \((a,b,c)\) with \(a^2+b^2+c^2\le2500\). Accounting for \(2^s\) sign choices and \(L!/(a!b!c!)\) yields a signed three-axis histogram \(H_3(q,L)\). Then exactly

\[
 B_6(2500)=\sum_{q=0}^{2500}\sum_{L,M}
 H_3(q,L)\,H_3(2500-q,M)\binom{L+M}{L}.
\]

It equals the entire first computation bit-for-bit in Python arbitrary-precision integers. Further direct signed three-axis enumeration agrees at N=25 (30 endpoints / 846 paths) and N=2500 (150 endpoints / full signed three-axis path mass).

A third endpoint-only independent check is Jacobi's six-square theorem:
\(r_6(n)=16\sum_{d\mid n}\chi_{-4}(n/d)d^2-4\sum_{d\mid n}\chi_{-4}(d)d^2\).
For \(2500=4\cdot5^4\), the two sums are 6,510,416 and 406,901; hence
\(r_6(2500)=16(6510416)-4(406901)=102539052\).
External published proof: Alaca, Alaca & Williams, *The Simplest Proof of Jacobi's Six Squares Theorem* (2007), with the classical formula also at https://handwiki.org/wiki/Sum_of_squares_function.

## Reproducible implementation and status

The executed dual-certificate program is permanently saved at:
https://github.com/awdawmip/enterprise-math/blob/6efa3efee1a625cd2532f0bc6f4be6dfa6eb178f/research_checks/X6_R063_N2500_FULL_SIGNED_SIX_AXIS_BRC_DUAL_CERTIFICATE_20261115_1800.py

The executable at this immutable commit has Git blob 81de14241508a0a74a9501672399b93acd2627af and SHA256 24603ebf65531dd9e96defea2ed914484ff3b0e4a19c72df7df212753af5cb87; its exact locally executed bytes exited 0 and printed PASS_X6_FULL_SIGNED_N2500_SIX_AXIS. Additional separate local exhaustive-by-support checker and independent 3+3 checker returned PASS_EXACT_INTEGER. Machine-readable full support-by-length output canonical digest: 27606f039106b4c9b67e5a3329fa39cd3a782656bed4f5aead905a37b3442fd4.

**Native experiment boundary:** Original R063 Stage0 C3/C4 frozen executable with its 17 gates and original 1..512 replay has not been run here; source support https://github.com/awdawmip/enterprise-math/issues/2416 remains the actual same-object execution route. The old LP011 signed-dominant historical wrong-caller provenance, LP019 alleged positive-count cancellation wrong-caller provenance, complete 28-LP active consumer census and independent Driver REQUEST_REVISION remain unresolved. Do not republish Source units #1–#36, replay the 17:00 rejected write, or treat this exact six-axis free-word calculation as a formal Result, external physical claim, mathematical admission or original R063 replay.
