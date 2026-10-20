# R046 — Prior Art and Engineering Sources

Researcher-ID: `EM-R046-5C8A21`  
Task source: `2b9f282c1990de916f472a4764823729eff05203`  
Status: `SOURCE_AUDIT / NOT CANONICAL`

## Source typing rule

Sources are typed as `EMPIRICAL_ENGINEERING_EVIDENCE`, `STANDARD_CLASSICAL_MATHEMATICAL_DERIVATION`, `CONVENTION_NORMALIZATION`, or `PRIOR_ART_INTERPRETATION`. The R046 decomposition/quotient itself is new project analysis and is not attributed to the external sources.

External sources establish protocols, effective formulas/conventions, scale regimes or error envelopes. They do **not** establish any Enterprise Math native ontology.

## Registry

| Source ID | Type | Source | Used for |
|---|---|---|---|
| `SRC-NIST-INDEXING-1975` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NBSIR 75-750: Indexing Table Calibration](https://emtoolbox.nist.gov/Publications/NBSIR75-750.asp) | angular indexing calibration; whole-turn subdivision; closure/error propagation |
| `SRC-NIST-ROUNDNESS` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST/SEMATECH e-Handbook: Multiple-trace roundness designs](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc3442.htm) | 360-degree traces; least-squares circle effective readout; multi-trace separation of spindle/workpiece effects |
| `SRC-NIST-SIZE-2013` | `STANDARD_CLASSICAL_MATHEMATICAL_DERIVATION` | [NIST: Size tolerancing revisited — calculated diameters](https://www.nist.gov/publications/size-tolerancing-revisited-basic-notion-and-its-evolution-standards) | calculated diameters from circumference/area/volume under ISO GPS; definition dependency |
| `SRC-NIST-PI-TAPE-SOPS` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST OWM Laboratory Metrology SOPs - SOP 23 PI Tape Bench Method](https://www.nist.gov/pml/owm/laboratory-metrology/standard-operating-procedures-sops) | pi-tape calibration protocol existence |
| `SRC-NIST-CIRC-AREA-VOL` | `STANDARD_CLASSICAL_MATHEMATICAL_DERIVATION` | [NIST OWM: Circumference, Area and Volume relationships](https://www.nist.gov/pml/owm/circumference-area-and-volume) | classical circumference/area/cylinder-volume formulas; shared geometric definition descendants |
| `SRC-NIST-APERTURE` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST Optical Aperture Area and Coordinate Measurement Facility](https://www.nist.gov/laboratories/tools-instruments/optical-aperture-area-and-coordinate-measurement-facility) | absolute aperture area from calibrated edge-coordinate imaging; nominally circular apertures |
| `SRC-NIST-APERTURE-2000` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST Summary of High Accuracy Aperture Measurement Capabilities](https://www.nist.gov/publications/summary-high-accuracy-aperture-measurement-capabilities-national-institute-standards) | 3.5 mm to 25 mm aperture calibration; relative uncertainty at 10^-4 to 10^-5 scale depending system |
| `SRC-NIST-FLOW-2014` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST: Liquid Flow Meter Calibrations with the 0.1 L/s and 2.5 L/s Piston Provers](https://www.nist.gov/publications/liquid-flow-meter-calibrations-01-ls-and-25-ls-piston-provers) | known cross-sectional area times piston displacement over time; 0.003 to 2 L/s combined ranges; expanded uncertainty about 0.044% and 0.064% for two provers |
| `SRC-NIST-VOLUME` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST Fluid Metrology Calibration Services - Volume](https://www.nist.gov/pml/sensor-science/fluid-metrology/fluid-metrology-calibration-services-volume) | gravimetric water volume calibration; litre-scale capacity standards; reported expanded uncertainties |
| `SRC-NIST-TF-P` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST Time and Frequency from A to Z: Period/Phase](https://www.nist.gov/pml/time-and-frequency-division/popular-links/time-frequency-z/time-and-frequency-z-p) | T=1/f; phase may be expressed as time or angular units; one cycle closure |
| `SRC-NIST-PHASE-1992` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST phase angle calibration generator](https://www.nist.gov/publications/phase-angle-calibration-generator) | phase calibration over 1 Hz to 100 kHz |
| `SRC-NIST-PHASE-CAL` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST Low Frequency Primary Phase Angle Calibration](https://www.nist.gov/laboratories/tools-instruments/low-frequency-primary-phase-angle-calibration) | two-channel sinusoidal phase calibration; 0 to 360 degree service representation; frequency-dependent uncertainty |
| `SRC-BIPM-SI-2026` | `CONVENTION_NORMALIZATION` | [BIPM SI Brochure, 9th edition v4.01](https://www.bipm.org/en/publications/si-brochure) | current SI unit conventions |
| `SRC-BIPM-RADIAN-1980` | `CONVENTION_NORMALIZATION` | [CIPM 1980 Resolution 1 on SI supplementary units](https://www.bipm.org/en/committees/ci/cipm/69-1980/resolution-1) | plane angle as ratio of lengths; radian treated as dimensionless derived SI unit; freedom in expression conventions |
| `SRC-FFTW-CONVENTION` | `CONVENTION_NORMALIZATION` | [FFTW Reference - What FFTW Really Computes](https://fftw.org/fftw3_doc/What-FFTW-Really-Computes.html) | DFT sign and normalization conventions vary; unnormalized transform convention |
| `SRC-NUMPY-FFT` | `CONVENTION_NORMALIZATION` | [NumPy FFT documentation](https://numpy.org/doc/stable/reference/routines.fft.html) | DFT with 2pi exponential under cycle index parameterization; normalization options backward/ortho/forward |
| `SRC-NIST-DLMF-FOURIER` | `STANDARD_CLASSICAL_MATHEMATICAL_DERIVATION` | [NIST DLMF §1.14 Fourier Transforms](https://dlmf.nist.gov/1.14) | continuous Fourier convention with symmetric normalization; alternative sign conventions; Parseval under convention |
| `SRC-NIST-JNT` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST Johnson Noise Thermometry](https://www.nist.gov/programs-projects/johnson-noise-thermometry) | spectral cross-correlation and QVNS comparison; wide-band noise thermometry; reported microkelvin-per-kelvin uncertainty program |
| `SRC-NIST-JNT-2009` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST Johnson noise thermometry system analysis](https://www.nist.gov/publications/johnson-noise-thermometry-system) | spectral response, aliasing, nonlinearities and variance scaling |
| `SRC-NIST-THERMAL-2017` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST: Thermal Property Measurement Methods and Analysis for AM Solids and Powders](https://www.nist.gov/publications/thermal-property-measurement-methods-and-analysis-am-solids-and-powders) | localized thermal excitation and measured diffusivity/relaxation |
| `SRC-NIST-DLMF-HEAT` | `STANDARD_CLASSICAL_MATHEMATICAL_DERIVATION` | [NIST DLMF heat/diffusion equation representations](https://dlmf.nist.gov/1.18) | Gaussian heat-kernel representations; normalization/boundary-condition dependence |
| `SRC-NIST-TN1297` | `PRIOR_ART_INTERPRETATION` | [NIST TN 1297: Guidelines for Evaluating and Expressing Uncertainty](https://www.nist.gov/pml/nist-technical-note-1297) | normal, rectangular and triangular probability models depending information; uncertainty distributions are modeling choices |
| `SRC-NIST-DLMF-GAUSSIAN` | `STANDARD_CLASSICAL_MATHEMATICAL_DERIVATION` | [NIST DLMF normal distribution](https://dlmf.nist.gov/26.2) | normal distribution normalization includes sqrt(2pi) in a standard representation |
| `SRC-NIST-CAVITY-1986` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST acoustic and microwave resonances of a cavity](https://www.nist.gov/publications/acoustic-and-microwave-resonances-same-cavity) | independent acoustic/microwave resonances in same bounded cavity; high-precision ratio inference |
| `SRC-NIST-CYLACOUSTIC-2010` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST cylindrical acoustic resonance metrology](https://www.nist.gov/publications/cylindrical-acoustic-resonator-primary-thermometry) | longitudinal acoustic resonance frequencies; laser-interferometric cavity length; sub-ppm relative frequency uncertainty |
| `SRC-NIST-ACOUSTIC-MICROWAVE-2016` | `EMPIRICAL_ENGINEERING_EVIDENCE` | [NIST: Acoustic and microwave tests in a cylindrical cavity for acoustic gas thermometry at high temperature](https://www.nist.gov/publications/acoustic-and-microwave-tests-cylindrical-cavity-acoustic-gas-thermometry-high) | acoustic frequencies with ppm-scale uncertainty; microwave modes tracking cavity dimensions across temperature |

## Dependency interpretations introduced by R046

- **Classical geometry:** circumference/diameter, area/diameter and ideal cylindrical volume relationships are treated as one effective definition family for pi-origin counting. Independent wrap, edge-area, flow and gravimetric protocols remain empirical channels inside that family.
- **Radian/phase:** BIPM/NIST sources allow the operational phase relation to be expressed through cycle fraction or time displacement; the `2pi` multiplier appears when the same cycle is coordinatized in radians.
- **Fourier:** FFTW, NumPy and DLMF expose alternative sign/normalization choices. R046 therefore treats factor placement as convention debt and retains only convention-invariant reconstruction/physical spectral comparison.
- **Gaussian/integral:** DLMF gives standard normalized Gaussian/heat representations, while NIST uncertainty guidance permits alternative distribution models depending available information. R046 strips the normalization factor and retains empirical relaxation/transport behavior.
- **Bounded modes:** NIST resonance metrology supplies independent acoustic/microwave evidence for discrete bounded spectra and state tracking. R046 strips angular-frequency/wavenumber conventions and does not import the continuum eigenproblem into N0.

## Source limitations

- The atlas is deliberately representative, not exhaustive.
- Where a NIST page describes a capability but no universal uncertainty, the artifact records the tolerance as protocol-specific rather than inventing a number.
- Formula pages are used to type classical dependencies; they are not counted as independent engineering successes.
- The cited sources are not used to select any native mechanism or to calibrate against the classical decimal expansion of pi.