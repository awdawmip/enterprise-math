# R503 research continuation

Date 2026-11-03. Scientific pin R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Predecessor R502 `3273d034df3b007beeb9a30c64dcf80ade0373d4`.
Confirmed author-side theorem: D_26(k)>0 for 1<=k<=6; D_26(k)<0 for k>=7, k positive integer, r=2k+1, s=3.
Proof: inherited EOR p_t polynomial degree bound 2t, Hessenberg gives degree <=156. G_26 degree105, 52-point Newton interpolant S degree <=51. 157 verified integer identities imply a polynomial identity; six positive S values and 52 strictly negative shifted Newton coefficients at origin k=7 certify signs to infinity.
Reproduce: `node R503_VERIFY.js > R503_EVIDENCE.json`, `python R503_INDEPENDENT.py`. Outputs R503_EXACT_JS_PASS and R503_INDEPENDENT_PASS. 20 direct Toeplitz determinants, 540 independent branch-kernel comparisons, six independent SymPy matrix samples.
Native gateway: session start STATIC_READONLY_SCOPE_DENIED (operation_sent=false); owner list CONTROL_QUOTA; no native CLAIM, Result, Driver acceptance or platform-issued Researcher-ID. Project GitHub credential awdawmip has write rights, author-side material in Draft PR #1708.
Next exact unit: m=27,s=3; 54-point Newton coefficients, 163-point polynomial identity (deg<=162), sign-shift classification, original signed branch checks. Alternative exact problem: fixed k=6,7,10 rational rank generating function poles. P000/ACTIVE worldview and R462 science input are unchanged.
