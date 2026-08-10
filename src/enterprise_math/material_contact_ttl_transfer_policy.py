"""Exact boundary between TTL loss/transfer and same-quantizer reconstitution.

Finite-TTL expiry removes already-quantized whole-contact quanta from the causal
queue.  Exact accounting then requires those quanta to enter some declared sink
or transformed state.  A tempting alternative is to "return" the expired whole
quanta to the same contact's raw retained-detail quantizer.

If nothing else changes, that operation is algebraically null.

For amplitude ``A>0``, canonical pending remainder ``0<=delta<A`` and ``x``
expired whole quanta, the returned raw numerator is

    A*x + delta.

Euclidean re-quantization by the same amplitude gives exactly

    quotient = x,
    remainder = delta.

So every expired whole quantum is recreated immediately.  No queue relaxation,
loss or new precision effect has occurred.

Therefore a genuine nonzero TTL expiry must do at least one of the following:

* route expiry into an external/accounted sink;
* transfer it to a different material state/quantizer;
* change eligibility/timing so returned content is not immediately the same
  causal whole-queue state;
* apply an explicit lossy/transforming operator.

This module deliberately does not choose among those physical policies.  It only
prevents the mathematically empty policy "expire then reinsert unchanged into
the same quantizer" from being mistaken for dissipation or relaxation.
"""

from __future__ import annotations

from dataclasses import dataclass


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


@dataclass(frozen=True)
class SameQuantizerTTLReturnReport:
    amplitude: int
    expired_whole_quanta: int
    pending_remainder_before: int
    returned_raw_numerator: int
    requantized_whole_quanta: int
    pending_remainder_after: int

    @property
    def exactly_reconstitutes_expired_queue(self) -> bool:
        return (
            self.requantized_whole_quanta == self.expired_whole_quanta
            and self.pending_remainder_after == self.pending_remainder_before
        )


def same_quantizer_ttl_return(
    amplitude: int,
    expired_whole_quanta: int,
    pending_remainder: int,
) -> SameQuantizerTTLReturnReport:
    """Return/requantize expired whole numerator in the unchanged amplitude fiber."""
    _require_int("amplitude", amplitude)
    _require_int("expired_whole_quanta", expired_whole_quanta)
    _require_int("pending_remainder", pending_remainder)
    if amplitude <= 0:
        raise ValueError("amplitude must be positive")
    if expired_whole_quanta < 0:
        raise ValueError("expired_whole_quanta must be nonnegative")
    if not 0 <= pending_remainder < amplitude:
        raise ValueError("pending_remainder must lie in 0..amplitude-1")

    returned = amplitude * expired_whole_quanta + pending_remainder
    whole, remainder = divmod(returned, amplitude)
    report = SameQuantizerTTLReturnReport(
        amplitude=amplitude,
        expired_whole_quanta=expired_whole_quanta,
        pending_remainder_before=pending_remainder,
        returned_raw_numerator=returned,
        requantized_whole_quanta=whole,
        pending_remainder_after=remainder,
    )
    if not report.exactly_reconstitutes_expired_queue:
        raise AssertionError("same-quantizer TTL return unexpectedly changed the state")
    return report


def same_quantizer_return_blocks_genuine_expiry(
    amplitude: int,
    expired_whole_quanta: int,
    pending_remainder: int,
) -> bool:
    """True exactly when a nonzero expiry would be undone by unchanged reinsertion."""
    report = same_quantizer_ttl_return(
        amplitude,
        expired_whole_quanta,
        pending_remainder,
    )
    return (
        expired_whole_quanta > 0
        and report.exactly_reconstitutes_expired_queue
    )
