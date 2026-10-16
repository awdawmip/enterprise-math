# Enterprise Math C108 — positive-port score bound (AUTHOR DRAFT)

Date: 2026-10-16. Fixed source snapshots: GLOBAL_KNOWLEDGE_V1 main@a7316c6ee0b9dc21f6b672009235c496ec73095a; enterprise-math main@1080faa03db98bbcfc3feb9785f39fa1b061ebd1.

Scope: C105 classical positive BRC finite model, 11 glued phases, fixed core c2=c24=1; 68 weak couplings, no independence premise. Baseline: A0<=12609529/131072=M, F0(2/5)>100, F0(99/100)<-29, dF0/du<-281 (846 inherited exact Bernstein coefficients rechecked).

For epsilon>delta>0 set r_f=epsilon+(1-epsilon)r0_f+z_f, |z_f|<=delta, eta=epsilon+delta, rho=(1+100eta)^68-1. Four nonnegative joint port masses p_i obey |p_i(z)-p_i(0)|<=rho*p_i(0), and |p_i'(z)-p_i'(0)|<=kappa*p_i(0) where kappa=300rho+120000eta(1+rho), from the original positive spin-state weights and u-log-scores. Since F=4(p++p---p+-p-+) and p++p--+p+-p-+ <= M^2/4,

|dFz/du-dF0/du| <= 2 M^2 [300rho(2+rho)+120000eta(1+rho)^2].

Case A epsilon=18/10^10, delta=17/10^10: exact bound <273, hence dFz/du<-8.
Case B epsilon=181/10^11, delta=18/10^10: exact bound <842/3, hence dFz/du<-1/3.
In both cases determinant endpoints stay >199/2 and <-57/2. All 68 couplings remain strictly (0,1). Every stage has one unique transverse interior root, stages glue continuously and define a connected relatively open 67D zero region. Case B has 6x C106 unique-root independent perturbation radius; NOT the larger C107 existence-only radius.

Locally reproduced C108 ZIP SHA256: 1d581160887395f6b7178d32ee0087daeff8f79d907ffc2fbef174df6ab8bcdd; C108 theorem Markdown SHA256 ea96adb32c48cd433430e462a91cd7915a7c96ebc26625b0f79d4dd0feba82cf. Parent C107 SHA256 0b4744f3a54e266468a8d3036676f518a31d3da7f98a73816d88c40e020a0069. Clean unzip: rational checker, SHA manifest, 846 Bernstein rechecks and independent C105 integer graph/Walsh agree. No native CLAIM or independent Driver admission. Next: exact GF2 mixed derivative supports to test uniqueness on C107's larger box. BRC finite auxiliary only; no native X6/3D-slice bridge yet.
