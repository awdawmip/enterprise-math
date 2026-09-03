# Gregory–Machin continuation: blind H=7,000,000 smooth-norm support-six rediscovery

Status: `FREE_RESEARCH / EXECUTABLE_BOUNDED_SUBFAMILY_CENSUS + PRIOR_ART_REDISCOVERY / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_h7m_smooth_support6_census_20260903.py`
Depends on: the exact Gaussian valuation-lattice and valuation-circuit endpoint theorem already frozen for #1160.

## 1. Purpose

The previous support-three and support-four exact censuses showed that Gaussian split-prime valuation circuits can rediscover Gauss and Størmer without fitting numerical arctangent sums.  The next falsifiable architecture test is whether the same native search can reach a high-support, low-Lehmer formula whose denominators are millions rather than thousands.

A direct scan of all six-subsets up to several million is impossible.  This note therefore declares a finite arithmetic search box before endpoint recognition and asks whether a support-six rank-five circuit emerges from it.

No target denominator tuple, coefficient vector, five-prime palette, numerical value of pi, or floating arctangent equality is supplied to candidate generation.

## 2. Declared blind search box

The denominator universe is

\[
2\le D\le 7{,}000{,}000.
\]

Retain only denominators for which every odd split prime divisor of

\[
D^2+1
\]

is at most

\[
1300.
\]

The odd prime bound is a round smoothness cutoff; it is not a list of desired Gaussian primes.

The circuit target is:

- six distinct reciprocal denominators;
- union of free split-prime coordinates has exactly five primes;
- free valuation rank five, hence a primitive six-column circuit;
- endpoint torsion is the diagonal `C8` class;
- Lehmer measure is below the previously established support-four Størmer benchmark.

Two palette-generation classes are searched exhaustively within their declarations:

1. one denominator already carries the full five-prime palette;
2. with no full-support column, the five-prime palette is the union of two denominator support sets.

This is a bounded exact theorem only for these declared palette classes, not for all six-term Machin identities.

## 3. Smooth-norm sieve without factoring seven million integers independently

For every split prime

\[
p\equiv1\pmod4,\qquad p\le1300,
\]

compute the two roots

\[
D\equiv\pm\sqrt{-1}\pmod p.
\]

Only those arithmetic progressions can contain a factor `p` of `D^2+1`.  Divide all powers of `p` along both progressions.  Also remove the exact ramified factor `2` from odd `D`.  A denominator survives iff the residual norm is one.

Thus the smoothness filter is an exact arithmetic sieve; it does not call a floating recognizer and does not need an independent full factorization of all seven million norms.

There are exactly

\[
\boxed{104}
\]

allowed odd split primes below the cutoff.

From the raw denominator universe, only

\[
\boxed{17{,}741}
\]

smooth denominators survive.

Their exact free-support size distribution is:

| support size | count |
|---:|---:|
| 1 | 25 |
| 2 | 187 |
| 3 | 855 |
| 4 | 2817 |
| 5 | 6368 |
| 6 | 6120 |
| 7 | 1331 |
| 8 | 38 |

These counts are frozen as checker assertions.

## 4. Exact endpoint sieve below the Størmer Lehmer benchmark

For a candidate support set, endpoint feasibility is still decided only by exact native data:

1. exact Gaussian factorization orientation coordinates;
2. exact integer valuation matrix;
3. primitive circuit by cofactors;
4. exact `C8` torsion pairing.

Only after those layers is Lehmer measure used for ranking/pruning.

### 4.1 Full-support-column palettes

There are `6364` distinct five-prime support palettes represented by at least one full-support denominator.

Only

\[
\boxed{18}
\]

six-tuples in this class can even lie below the Størmer Lehmer bound.

Exact rank-five/torsion checking yields

\[
\boxed{0}
\]

endpoint circuits.

### 4.2 Pair-generated five-prime palettes

Among support sets of size at most four, pairwise unions generate exactly

\[
\boxed{311{,}403}
\]

distinct five-prime palettes.

The denominator-cost lower bound plus exact actual-union test leaves only

\[
\boxed{21}
\]

six-tuples below the Størmer benchmark.

Exact circuit and torsion checking leaves exactly

\[
\boxed{1}
\]

endpoint circuit.

It is

\[
\boxed{
D=(239,1023,5832,110443,4841182,6826318)
}
\]

with coefficient vector

\[
\boxed{(183,32,-68,12,-12,-100)}
\]

and free split-prime palette

\[
\boxed{(5,13,229,457,1201)}.
\]

Its Lehmer measure is

\[
\boxed{\mu\approx1.512439470049298}.
\]

This is the classical Hwang 1997 six-term identity.  No novelty is claimed for the formula.  The research result is the blind native rediscovery inside the declared arithmetic box.

## 5. Finite winding certificate

An endpoint circuit alone fixes the rational-turn class but must not silently choose an unwrapped analytic branch.

The checker therefore multiplies the signed reciprocal turns as primitive integer direction pairs.  Every `D>=2` step is smaller than a quarter-turn in the later classical readout, so a sign change of the horizontal coordinate records one exact tangent-chart sheet crossing.

For the rediscovered Hwang word the checker returns

\[
\boxed{\text{endpoint}=(1,1),\qquad\text{sheet}=0,\qquad\text{crossings}=0.}
\]

Hence its finite lift reaches the principal diagonal with no hidden winding.  Only after this native certificate is fixed is the classical completion read as `pi/4`.

## 6. Interpretation

The search sequence is now:

\[
\text{bounded denominator box}
\to
\text{smooth Gaussian norms}
\to
\text{five-prime palettes}
\to
\text{rank-five integer circuits}
\to
C_8\text{ endpoint}
\to
\text{finite winding lift}
\to
\text{analytic Lehmer ranking}.
\]

At no point is the target numerical value of pi used to recognize a candidate identity.

This demonstrates that high-support efficient Machin identities are discoverable as sparse arithmetic circuits in the native rational-turn carrier rather than only as floating inverse-trangent fits.

## 7. Scope boundary and next frontier

This result is exhaustive only in the declared `H=7M`, split-prime `<=1300`, five-free-prime, support-six, two-palette-generation-class box.

It does not prove global optimality of Hwang's identity.  In fact, a subsequent prior-art audit located a 2010 paper by Amrik Singh Nimbran reporting an exact six-integer-reciprocal identity of Lehmer measure about `1.48912`; the valuation/winding machinery independently certifies that identity as well.  That result lies outside the present smooth box because one free split prime is `32787077` and the largest denominator is `1737720807`.

The correct continuation is therefore not to promote Hwang as a global optimum.  It is to understand the exact local surgery that creates such large-prime residuals and determine when that surgery strictly improves fixed-compute completion cost.
