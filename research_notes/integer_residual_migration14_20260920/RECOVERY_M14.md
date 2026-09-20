# Recovery M14

Parent objective: progressively migrate actual Enterprise Math/Nollm research code from floating-point decision semantics to integer plus typed residuals.

Verified remote baseline: M13 candidate `b380f5dc0136480815ae89e1976e4fac20faf102`.
M14 local change: declare optional `exact` dependency on `enterprise-math==0.1.0`; make `core.read_data` fail as a normal ValueError when BRC is absent; add installed-console gate.
Validation: 148 retained tests + 17 installed-console checks, zero retained failures/errors/skips.

Important boundary: source-slice render/site used an explicit minimal workbench fixture; exact runtime used a test-only minimal package composed from byte-identical BRC implementation files. Neither is production package acceptance.

Next executable unit: run installed console/render/site against the real production workbench package-data and complete Enterprise Math root package; then browser smoke the generated machine-report page. Do not replay M01-M13 arithmetic and do not substitute another tie rule or infer display pixels/scale from exact sources.
