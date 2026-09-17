"""One-time exact static-carrier route for the pinned serial spectralDNS Vortex interface.

Research prototype for RS-CFD-SPECTRAL-HYBRID-20260910. It preserves the original
host dense callback, unprojected rotational pair kernel, complex coefficients,
pressure stage, retained labels and Nyquist policy. The only new decision is a
one-time exact Boolean-support closure before the trajectory starts.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Callable, Iterable
import time
import numpy as np

Vec = tuple[int, int, int]

@dataclass(frozen=True)
class ClosureResult:
    status: str
    carrier_size: int | None
    lower_bound: int
    rounds: int
    pair_tests: int
    carrier: tuple[Vec, ...] | None


def _neg(v: Vec) -> Vec:
    return (-v[0], -v[1], -v[2])


def _add(p: Vec, q: Vec) -> Vec:
    return (p[0] + q[0], p[1] + q[1], p[2] + q[2])


def _in_box(v: Vec, cutoff: int) -> bool:
    return all(-cutoff <= x <= cutoff for x in v)


def truncated_additive_carrier(seed: Iterable[Vec], cutoff: int, limit: int) -> ClosureResult:
    """Least negation/pair-sum carrier in [-K,K]^3, with sound early fallback."""
    C = {tuple(map(int, v)) for v in seed}
    C |= {_neg(v) for v in tuple(C)}
    if any(not _in_box(v, cutoff) for v in C):
        raise ValueError("seed outside retained cube")
    if len(C) > limit:
        return ClosureResult("FALLBACK_DENSE", None, len(C), 0, 0, None)
    rounds = 0
    pair_tests = 0
    while True:
        rounds += 1
        L = sorted(C)
        new: set[Vec] = set()
        for i, p in enumerate(L):
            for q in L[i:]:
                pair_tests += 1
                r = _add(p, q)
                if _in_box(r, cutoff) and r not in C and r not in new:
                    new.add(r)
                    rn = _neg(r)
                    if rn not in C and rn not in new:
                        new.add(rn)
                    if len(C) + len(new) > limit:
                        return ClosureResult("FALLBACK_DENSE", None, limit + 1, rounds, pair_tests, None)
        if not new:
            return ClosureResult("CERTIFIED_STATIC_CARRIER", len(C), len(C), rounds, pair_tests, tuple(sorted(C)))
        C |= new


def verify_carrier(carrier: Iterable[Vec], cutoff: int) -> bool:
    C = set(carrier)
    if any(_neg(v) not in C for v in C):
        return False
    for p in C:
        for q in C:
            r = _add(p, q)
            if _in_box(r, cutoff) and r not in C:
                return False
    return True


def build_fixed_rfft_gather(carrier: Iterable[Vec], n: int):
    """Map every full signed carrier label to last-axis rFFT storage without loss."""
    p = np.asarray(tuple(carrier), dtype=np.int64)
    ix = np.empty(len(p), dtype=np.int64)
    iy = np.empty(len(p), dtype=np.int64)
    iz = np.empty(len(p), dtype=np.int64)
    conj = np.zeros(len(p), dtype=np.bool_)
    for i, (x, y, z) in enumerate(p):
        if z >= 0:
            ix[i], iy[i], iz[i] = x % n, y % n, z
        else:
            ix[i], iy[i], iz[i], conj[i] = (-x) % n, (-y) % n, -z, True
    return p, ix, iy, iz, conj


def gather_fixed_rfft(u_hat, gather):
    p, ix, iy, iz, conj = gather
    a = np.ascontiguousarray(np.asarray(u_hat)[:, ix, iy, iz].T)
    if np.any(conj):
        a[conj] = a[conj].conjugate()
    return p, a


class StaticCarrierNativeVortexAdapter:
    """Serial spectralDNS-compatible Vortex callback with one-time exact routing.

    `validate_initial` must run once before trajectory integration. If the exact
    least retained support carrier exceeds the configured limit, every nonlinear
    call is sent to the unchanged dense host callback. Otherwise each stage is
    gathered only on the fixed carrier and evaluated with the original unprojected
    pair kernel. No coefficient thresholding or pruning is performed.
    """
    convection = "Vortex"

    def __init__(self, context, params, dense_callback: Callable,
                 pair_kernel: Callable, extract_support: Callable, *,
                 comm_size: int, sparse_limit: int = 128):
        if comm_size != 1:
            raise ValueError("only serial host contexts are supported")
        if params.dealias != "3/2-rule" or not params.mask_nyquist:
            raise ValueError("requires native 3/2-rule and host Nyquist masking")
        ns = np.asarray(params.N, dtype=int)
        if len(ns) != 3 or not np.all(ns == ns[0]) or ns[0] % 2 or ns[0] < 8:
            raise ValueError("requires an even cubic three-dimensional grid")
        if not np.allclose(params.L, 2*np.pi, rtol=0, atol=1e-13):
            raise ValueError("only the 2pi periodic cube is supported")
        if not isinstance(sparse_limit, int) or sparse_limit < 0:
            raise ValueError("nonnegative integer sparse_limit required")
        if not callable(dense_callback) or not callable(pair_kernel) or not callable(extract_support):
            raise TypeError("host callback, pair kernel and support extractor are required")
        self.n = int(ns[0]); self.cutoff = self.n//2 - 1
        self.shape = (3, self.n, self.n, self.n//2+1)
        if context.U_hat.shape != self.shape or context.U_hat.dtype != np.complex128:
            raise ValueError("requires complex128, last-axis rFFT host storage")
        self.K = context.K; self.Tp = context.Tp; self.VTp = context.VTp
        k = np.stack(np.broadcast_arrays(*context.K))
        f = np.rint(np.fft.fftfreq(self.n)*self.n).astype(int)
        expected = np.array(np.meshgrid(f, f, np.arange(self.n//2+1), indexing='ij'))
        if not np.array_equal(k, expected):
            raise ValueError("unsupported host wavevector ordering or scaling")
        self.keep = np.all(np.abs(expected) <= self.cutoff, axis=0)
        self.original = dense_callback; self.pairs = pair_kernel; self.extract = extract_support
        self.sparse_limit = sparse_limit; self.route_ready = False; self.dense = False; self.gather = None
        self.stats = {
            'decision': None, 'carrier_size': None, 'lower_bound': None,
            'detector_rounds': None, 'detector_pair_tests': None,
            'detector_seconds': 0.0, 'gather_seconds': 0.0,
            'pair_kernel_seconds': 0.0, 'sparse_calls': 0, 'fft_calls': 0,
            'fixed_carrier_labels_read_per_sparse_call': 0,
            'pruning_used': False,
        }
        real = context.U.copy(); spec = context.U_hat.copy()
        real.fill(0); real[0].fill(1)
        spec = context.VT.forward(real, spec)
        constant = complex(spec[0,0,0,0])
        if abs(constant.imag) > 1e-13 or constant.real <= 0:
            raise ValueError("host normalization is not a positive real scale")
        residual = np.asarray(spec).copy(); residual[0,0,0,0] = 0
        if np.max(np.abs(residual)) > abs(constant)*1e-12:
            raise ValueError("constant-transform normalization witness failed")
        self.scale = 1.0/constant.real; self.normalization_constant = constant.real

    def validate_initial(self, u_hat):
        h = np.asarray(u_hat)
        if h.shape != self.shape or h.dtype != np.complex128 or not np.isfinite(h).all():
            raise ValueError("invalid initial spectral field")
        if np.any(h[:, ~self.keep] != 0):
            raise ValueError("initial field must have zero Nyquist planes")
        ix = (-np.arange(self.n)) % self.n
        mirror = np.take(np.take(h[:,:,:,0], ix, axis=1), ix, axis=2).conjugate()
        if not np.allclose(h[:,:,:,0], mirror, rtol=0, atol=1e-12):
            raise ValueError("initial zero plane is not Hermitian")
        t = time.perf_counter()
        p, _ = self.extract(h*self.scale, self.n)
        res = truncated_additive_carrier((tuple(map(int, v)) for v in p), self.cutoff, self.sparse_limit)
        self.stats['detector_seconds'] += time.perf_counter() - t
        self.stats.update(decision=res.status, carrier_size=res.carrier_size,
                          lower_bound=res.lower_bound, detector_rounds=res.rounds,
                          detector_pair_tests=res.pair_tests)
        if res.status == 'CERTIFIED_STATIC_CARRIER':
            if res.carrier is None or not verify_carrier(res.carrier, self.cutoff):
                raise AssertionError("invalid static carrier certificate")
            self.gather = build_fixed_rfft_gather(res.carrier, self.n)
            self.stats['fixed_carrier_labels_read_per_sparse_call'] = len(res.carrier)
            self.dense = False
        else:
            self.gather = None; self.dense = True
        self.route_ready = True
        return res

    def __call__(self, rhs, u_hat, work, Tp, VTp, K, u_dealias):
        if not self.route_ready:
            raise RuntimeError("validate_initial must be called before trajectory integration")
        if K is not self.K or Tp is not self.Tp or VTp is not self.VTp:
            raise ValueError("adapter used with another host context")
        if u_hat.shape != self.shape or u_hat.dtype != np.complex128:
            raise ValueError("host spectral layout changed")
        if self.dense:
            self.stats['fft_calls'] += 1
            return self.original(rhs, u_hat, work, Tp, VTp, K, u_dealias)
        t = time.perf_counter()
        p, a = gather_fixed_rfft(np.asarray(u_hat)*self.scale, self.gather)
        self.stats['gather_seconds'] += time.perf_counter() - t
        t = time.perf_counter()
        # Original pair kernel returns the full retained output; no output labels
        # are pruned. Pressure/diffusion remain downstream in the unchanged host.
        rhs[:] = self.pairs(p, a, self.n, self.cutoff)/self.scale
        self.stats['pair_kernel_seconds'] += time.perf_counter() - t
        self.stats['sparse_calls'] += 1
        return rhs


def propose_pruning(u_hat, mask):
    """Separate proposal only. It is never called by the certified trajectory route."""
    h = np.asarray(u_hat)
    if mask.shape != h.shape[1:] or mask.dtype != bool:
        raise ValueError("boolean spectral mask required")
    return h*mask, h*(~mask), {
        'status': 'UNVERIFIED_PROPOSAL_DO_NOT_USE_AS_CERTIFIED_TRAJECTORY',
        'missing_bounds': ['roundoff','time_discretization','unresolved_modes','error_propagation'],
    }
