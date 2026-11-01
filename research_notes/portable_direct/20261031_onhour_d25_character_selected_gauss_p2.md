# D25: Character-selected Gauss zero at p² — conditional single-factor route

2026-10-31. **AUTHOR-SIDE, EXPLORATORY, EXACT FINITE CHECK, UNREVIEWED / NOT_ADMITTED**. New character-selected vanishing is an UNPROVED CONJECTURE, not Source theorem or native experiment. Consume project proof fc10280dbc1cb9ef929869cc3379f8bb31bf1d31 and published Guo–Zudilin 2019 theorem; mother RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

For primes p>3 set β_k=(1/8)_k(3/8)_k/[9^k(k!)²], G_p=Σ_{0≤k<p}β_k, H_p=Σ_{0≤k<p}(16k+1)β_k. Let ε_p=(3/p). For p≡5,7 mod8, equivalently p mod24 in {5,7,13,23}, the **new conjecture** is:

- If ε_p=+1 (p≡13,23 mod24), then G_p≡0 mod p² and H_p is a p-unit.
- If ε_p=−1 (p≡5,7 mod24), then H_p≡0 mod p² and G_p is a p-unit.

This is a source-selective assertion: not both factors zero. With the truncated Gauss polynomial F_p(z)=Σ_{k<p}(1/8)_k(3/8)_k z^k/(k!)², precisely G_p=F_p(1/9), H_p=[(1+16 z∂_z)F_p(z)]_{z=1/9}.

**PROVED CONDITIONAL CONSEQUENCE:** the exact classical Clausen identity B_p=G_pH_p−T_{β,p}, and Guo–Zudilin's proven B_p≡pχ_{−3}(p) mod p³, imply that **if** the corresponding factor vanishes mod p², then T_{β,p}≡−pχ_{−3}(p) mod p². Thus a character-selective single-variable Gauss proof could complete the previously isolated three-port beta-tail character conjecture. The new character-selective premise is NOT yet proved. This does not establish the original 216-model p³ claim or affine p⁴ bridge.

**Executed exact Python certificate:** d25_gauss_character_selected_factor_20261031.py examined all 100 primes ≤1200 with p mod8 in {5,7}: 51 with ε=+1 had G=0 modp² and H unit modp; 49 with ε=−1 had H=0 modp² and G unit. Program independently checked β via coefficient recurrence and factorial numerator-product spot cases. Selected p³ checks demonstrate sharpness: for p=13, G/p²≡1 mod13; p=23 G/p²≡12; p=29 H/p²≡22; p=31 H/p²≡16; p=373 G/p²≡12. A universal modp³ strengthening is FALSE (p=13 supplies exact counterexample). Finite tests do not prove the universal modp² conjecture.

Retain G and H as distinct signed/Gauss observers and original two-index beta-tail provenance; scalar evaluation cannot replace native H0/B0, Frobenius, or source-specific Green/Hesse. **Next mathematical action:** a class-selective finite WZ/CM or hypergeometric proof of single-factor p² vanishing in the four mod24 classes; then integrate with original 216 I0–I2 versus I3–I5 to solve D25 or find counterexample.

Native original-class #1559 remains p373 NOT_EXECUTED/PENDING_OWNER. Research lane's historical own recovery #6632 non-authorizing; original request research-onhour-20261031-0205-dispatch-r15 #6633 terminal UPSTREAM_CODE_REVIEW_REQUIRED, gateway v0.6.11 research_authority_granted=false. No new Source CLAIM/run, Research-Activity registration, formal Result or review is asserted. No maintenance conversation use, P000/ACTIVE worldview change or scheduler alteration.
