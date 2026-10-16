# C114 — GF(2) deleted-face positive-port estimate; 68D BRC unique transverse zero tube enlarged 7.5×

**Status:** AUTHOR_EXACT_RATIONAL_VERIFIED; PORTABLE_CLEAN_REPLAY; NO_NATIVE_CLAIM; NOT_DRIVER_ADMITTED. **Date:** 2026-10-17 (Asia/Shanghai).

## Frozen references and scope

- GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge main@eef913c51d2da30ff9d09907b43dd0a07fd7c4f9`. Read universal bootstrap/manual, project P000, ACTIVE worldview, research activity and BRC protocols.
- EM frozen research input: `awdawmip/enterprise-math main@2e9e9763b66e0e07282378d90696dafec1c85609`; current portable research/control protocols read there.
- Parent C113 **zip SHA256**: `22e919f621f523c7516517add2ea01de99e936137e10971859012a91e5d8e888`; 11 exact arcs, 365 exact rational rectangles. 48-bit core: only c_2=c_24=1; 156 integer edges, 142 face characters; six strong anchors, 68 independently perturbed weak faces.
- **Restricted mathematics:** classical positive-weight finite auxiliary BRC with all GF(2) face correlations preserved. NOT a P000 native X6 Cell, three-dimensional slice or physical theorem.

## New exact bound, with no independence assumption

Let a,b,c,d be the four nonnegative joint-port masses, with F=AD−BC=4(ad−bc) and Q0=4(ad+bc). Perturb each weak face independently by
`r_f^z=epsilon+(1-epsilon)r_f^0+z_f`, `|z_f|<=delta`.

For each active u-face i in the original stage, let `m_{p,-i}` be **the actual conditional port p mass after deleting the factor (1+chi_i*r_i)** and leaving all other baseline factors unchanged; let `lambda_i=partial_u r_i^0 >= 0`. On an exact rational rectangle R, set
`alpha_f=epsilon+delta/(1-R_f)`, where R_f bounds the original r_f^0, `1+rho=prod_f(1+alpha_f)`, and `1+rho_minus_i=(1+rho)/(1+alpha_i)`.
Define the explicit nonnegative polynomial
`T_i=4*lambda_i*(m_{a,-i}*d+a*m_{d,-i}+m_{b,-i}*c+b*m_{c,-i})`.
The original positive-state product rule proves, on the entire rectangle,
```
abs(partial_u F_z-partial_u F_0)
 <= sum_i ( (1+rho)*(epsilon+(1-epsilon)*rho_minus_i)+rho )*T_i.
abs(F_z-F_0) <= Q0*(2*rho+rho^2).
```
Differentiating the original factor first and then deleting it avoids the preceding C113 log-response singular denominators; all 68 original correlated face characters remain intact.

## C114 exact 7.5-fold result

At `delta=3/200000=1.5e-5`, `epsilon=1501/100000000=1.501e-5`, all 68 weak couplings lie strictly between zero and one. For all 11 joined stages, all t in [0,1], all independent perturbations |z_f|<=delta and all u in [2/5,99/100], the exact 365-rectangle Bernstein evidence gives
```
F_z(t,2/5)>76;
F_z(t,99/100)<-5;
partial_u F_z(t,u)<-295.
```
Thus each arc has **exactly one simple internal root**, depending continuously/smoothly on its parameters. Original joints preserve all four Fourier ports, so the five C102 anomalous mechanisms remain linked by a common zero structure in a strictly interior 68D corridor; the union contains a relatively open connected smooth 67D zero patch. No assertion about global connectivity of the whole zero set or different discrete cores.

New exact rational Bernstein coefficient upper bounds checked: **53,066** across **365** rectangles and **11** arcs; minimum strict negative-derivative margin is above **295.0926**, maximum F perturbation below **23.935**. An independent **direct GF(2) factor-convolution** algorithm rechecks all four baseline moments for 11 arcs and **1,572** Bernstein coefficients in 32 deleted-factor spot checks. Clean temporary extraction and SHA256 verification passed:
`C114_CLEAN_SHA256_PARENT_INPUT_GF2_53066_RATIONAL_COEFFICIENTS_AND_1572_INDEPENDENT_SPOTS_PASS`.

**Portable evidence bundle SHA256:** `b70c155f19023cea597d711eeb56d7cbb0b5082e92dd8019a06bf816b53359c9`; parent C113 bundle nested with hashes, primary proof, independent verifier, complete 3 MB exact per-rectangle certificate, and manifest. Available as ChatGPT C114 portable attachment; GitHub this file records the author theorem summary and evidence hash, not the full executable bytes.

## Open C115: endpoint robustness rather than derivative

Strengthen the port-specific bound on `F_z(t,99/100)` without globally using `Q0(2rho+rho^2)`, targeting `delta>=2e-5` with a genuinely sharp **endpoint** sign margin. Separate still unresolved: a proven native X6 three-coordinate, relation/provenance-preserving bridge; independent Driver mathematical review and formal Source admission.

## Control and provenance

Authenticated GitHub account: `awdawmip`, this is an **author-only research note**. The control tasks/dispatch returned `CONTROL_QUOTA`; the native session start returned `STATIC_READONLY_SCOPE_DENIED` / `operation_sent=false`. Therefore active native Owner was not verified, and no valid native CLAIM, Result, Driver review, or canonical taskbook admission is claimed. Branch publication is durable only if separately read back, and is not main admission.
