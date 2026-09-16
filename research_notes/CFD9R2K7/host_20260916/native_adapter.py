"""Pressure-safe serial spectralDNS Vortex callback for a pinned native host.

This extends the restricted adapter, reusing the original rotational pair kernel
unchanged. The native 3/2-rule plus host Nyquist mask is the declared Galerkin
space; no old n//3-1 cutoff, small-coefficient threshold, or velocity projection
is inserted. This is floating arithmetic, not an interval/PDE certificate.
"""
from __future__ import annotations
import time
from collections.abc import Callable
import numpy as np


class NativeVortexAdapter:
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
        if not callable(dense_callback) or not callable(pair_kernel):
            raise TypeError("host callback and original pair kernel are required")
        self.n = int(ns[0]); self.cutoff = self.n//2 - 1
        self.shape = (3, self.n, self.n, self.n//2+1)
        if context.U_hat.shape != self.shape or context.U_hat.dtype != np.complex128:
            raise ValueError("requires complex128, last-axis rFFT host storage")
        # The host supplies sparse/broadcast wavevectors; never coerce a ragged
        # list with np.asarray or quotient modes by their squared lengths.
        self.K = context.K; self.Tp = context.Tp; self.VTp = context.VTp
        k = np.stack(np.broadcast_arrays(*context.K))
        f = np.rint(np.fft.fftfreq(self.n)*self.n).astype(int)
        expected = np.array(np.meshgrid(f, f, np.arange(self.n//2+1), indexing='ij'))
        if not np.array_equal(k, expected):
            raise ValueError("unsupported host wavevector ordering or scaling")
        self.keep = np.all(np.abs(expected) <= self.cutoff, axis=0)
        self.original = dense_callback; self.pairs = pair_kernel
        self.extract = extract_support; self.sparse_limit = sparse_limit
        self.dense = False
        self.stats = {'sparse_calls': 0, 'fft_calls': 0, 'scan_calls': 0,
                      'support_counts': [], 'scan_seconds': 0.0}
        # Calibrate through the REAL host transform, without changing the input
        # context or guessing FFT normalization.
        real = context.U.copy(); spec = context.U_hat.copy()
        real.fill(0); real[0].fill(1)
        spec = context.VT.forward(real, spec)
        constant = complex(spec[0,0,0,0])
        if abs(constant.imag) > 1e-13 or constant.real <= 0:
            raise ValueError("host normalization is not a positive real scale")
        residual = np.asarray(spec).copy(); residual[0,0,0,0] = 0
        if np.max(np.abs(residual)) > abs(constant)*1e-12:
            raise ValueError("constant-transform normalization witness failed")
        self.scale = 1.0/constant.real
        self.normalization_constant = constant.real

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

    def __call__(self, rhs, u_hat, work, Tp, VTp, K, u_dealias):
        if K is not self.K or Tp is not self.Tp or VTp is not self.VTp:
            raise ValueError("adapter used with another host context")
        if u_hat.shape != self.shape or u_hat.dtype != np.complex128:
            raise ValueError("host spectral layout changed")
        if self.dense:
            self.stats['fft_calls'] += 1
            return self.original(rhs, u_hat, work, Tp, VTp, K, u_dealias)
        t = time.perf_counter()
        mask = np.any(np.asarray(u_hat) != 0, axis=0)
        count = int(np.count_nonzero(mask[:,:,0])+2*np.count_nonzero(mask[:,:,1:]))
        # A nonzero Nyquist input is outside this direct kernel's domain. Fall
        # back rather than remove it; the unmodified host decides its treatment.
        supported = not np.any(mask & ~self.keep)
        self.stats['scan_calls'] += 1
        self.stats['scan_seconds'] += time.perf_counter()-t
        if len(self.stats['support_counts']) < 12:
            self.stats['support_counts'].append(count)
        if not supported or count > self.sparse_limit:
            self.dense = True; self.stats['fft_calls'] += 1
            return self.original(rhs, u_hat, work, Tp, VTp, K, u_dealias)
        p, a = self.extract(np.asarray(u_hat)*self.scale, self.n)
        # Preserve g itself: the host computes pressure and projects AFTER this
        # callback. Newly generated non-Nyquist modes all enter the output.
        rhs[:] = self.pairs(p, a, self.n, self.cutoff)/self.scale
        self.stats['sparse_calls'] += 1
        return rhs
