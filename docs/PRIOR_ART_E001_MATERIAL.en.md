# E001 Material Benchmark — Prior Art and Engineering Boundary

Status: `RESEARCH / NOVELTY_UNVERIFIED`

## 1. Experimental benchmark

The first real-material loading benchmark uses L. R. G. Treloar's 1944 vulcanized-rubber measurements, including the classical uniaxial data set [SRC-TRELOAR-1944-RUBBER]. The machine-readable values used by the executable E001 benchmark are consumed from the public `thermalCANN` repository, which states the Steinmann transcription lineage [SRC-THERMALCANN-2023-TRELOAR-DATA].

Treloar's measurements, the physical behavior of vulcanized rubber, and the data transcription are external experimental assets. Enterprise Math makes no invention claim over them.

## 2. Continuous constitutive comparison

Classical hyperelastic constitutive modeling of rubber-like materials is established engineering mechanics. Steinmann, Hossain and Possart survey and compare a broad family of such models on Treloar data [SRC-STEINMANN-2012-HYPERELASTIC].

The E001 executable benchmark includes low-parameter Neo-Hookean, Mooney-Rivlin and Yeoh-style loading fits only as external contrast models. Their formulas, continuum-mechanics meaning, parameter-identification practice and historical development are not claimed as Enterprise Math results.

## 3. Enterprise Math test object

E001 asks a narrower engineering question: after the experimental coordinates are declared at finite integer resolution, can a small curve family built from project primitives—integer roots, integer powers, root-basin geometry and explicit projection—represent useful material response with competitive error and predictable resolution/complexity tradeoffs?

The current candidate is deliberately only a one-dimensional loading-curve benchmark. A good fit to uniaxial data does **not** establish a three-dimensional strain-energy function, objectivity, thermodynamic consistency, multiaxial predictivity, cyclic hysteresis fidelity, rate dependence, damage, plasticity or fracture.

## 4. Novelty boundary

The benchmark may support engineering usefulness only if advantages survive direct comparison with established constitutive models, real unloading/rate/history data, and implementation-cost measurements. Merely reproducing a known curve by integer arithmetic is not a novelty claim.

Historical novelty of the finite-precision synthesis remains `NOVELTY_UNVERIFIED`.
