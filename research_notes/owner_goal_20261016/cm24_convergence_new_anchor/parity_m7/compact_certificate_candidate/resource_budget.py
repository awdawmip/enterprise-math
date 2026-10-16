"""Shared resource accounting only; no mathematics runs at import time.

This module grants no execution authority. A real admitted launcher must supply
ONE instance to producer and independent checker, then enforce output_bytes.
Primitive exact-rational operations and constant constructions each cost one;
their internal integer gcd cost is controlled by bit/wall/memory limits.
"""
from __future__ import annotations

from fractions import Fraction
import math
import resource
import signal
import time


class BudgetStop(RuntimeError):
    pass


class Budget:
    OPS = 20_000_000
    SECONDS = 300
    MEMORY = 512 * 1024 * 1024
    OUTPUT = 8 * 1024 * 1024
    BITS = 16_384

    def __init__(self, job_started_monotonic):
        # The admitted external launcher records this BEFORE interpreter,
        # import, hashing, parsing or construction work. It is a clock, not an
        # authorization token. Its genuine binding is the launcher's duty.
        if not isinstance(job_started_monotonic, (int, float)):
            raise BudgetStop("missing whole-job clock")
        if not 0 <= time.monotonic() - job_started_monotonic < self.SECONDS:
            raise BudgetStop("invalid/expired whole-job clock")
        self.started = job_started_monotonic
        self.operations = 0
        self.output_emitted = 0
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        ceiling = self.MEMORY if hard == resource.RLIM_INFINITY else min(hard, self.MEMORY)
        target = ceiling if soft == resource.RLIM_INFINITY else min(soft, ceiling)
        resource.setrlimit(resource.RLIMIT_AS, (target, target))
        self.effective_memory_ceiling = target
        def timed_out(_number, _frame):
            raise BudgetStop("shared wall-time cap")
        signal.signal(signal.SIGALRM, timed_out)
        signal.setitimer(signal.ITIMER_REAL, self.SECONDS - (time.monotonic() - self.started))

    def charge(self, amount=1):
        if not isinstance(amount, int) or amount < 0:
            raise BudgetStop("invalid operation charge")
        self.operations += amount
        if self.operations > self.OPS:
            raise BudgetStop("exact operation cap")
        self.check_time()

    def check_time(self):
        if time.monotonic() - self.started > self.SECONDS:
            raise BudgetStop("shared wall-time cap")

    def checked(self, value):
        if value.numerator.bit_length() > self.BITS or value.denominator.bit_length() > self.BITS:
            raise BudgetStop("rational bit-length cap")
        return value

    def integer(self, value):
        self.charge()
        if not isinstance(value, int) or value.bit_length() > self.BITS:
            raise BudgetStop("integer bit-length cap")
        return value

    def q(self, numerator=0, denominator=1):
        self.charge()
        self.integer(numerator)
        self.integer(denominator)
        if denominator == 0:
            raise BudgetStop("zero rational denominator")
        return self.checked(Fraction(numerator, denominator))

    def integer_product(self, a, b):
        self.charge()
        return self.integer(a * b)

    def exact_integer_quotient(self, a, b):
        self.charge()
        if not b or a % b:
            raise BudgetStop("nonexact integer quotient")
        return self.integer(a // b)

    def add(self, a, b):
        self.charge()
        return self.checked(a + b)

    def sub(self, a, b):
        self.charge()
        return self.checked(a - b)

    def mul(self, a, b):
        self.charge()
        return self.checked(a * b)

    def div(self, a, b):
        self.charge()
        if not b:
            raise BudgetStop("zero exact divisor")
        return self.checked(a / b)

    def power(self, a, n):
        if not isinstance(n, int) or not 0 <= n <= 56:
            raise BudgetStop("power outside fixed carrier")
        result = self.q(1)
        for _ in range(n):
            result = self.mul(result, a)
        return result

    def comb(self, n, k):
        self.charge()
        if not 0 <= k <= n <= 56:
            raise BudgetStop("binomial outside fixed carrier")
        return self.integer(math.comb(n, k))

    def factorial(self, n):
        self.charge()
        if not 0 <= n <= 6:
            raise BudgetStop("factorial outside residue carrier")
        return self.integer(math.factorial(n))

    def lcm(self, a, b):
        self.charge()
        return self.integer(math.lcm(a, b))

    def encoded(self, value):
        self.charge()
        self.checked(value)
        return [hex(value.numerator), hex(value.denominator)]

    def decoded(self, pair):
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("rational pair shape")
        values = []
        for s in pair:
            if not isinstance(s, str) or len(s) > self.BITS // 4 + 4:
                raise ValueError("rational hex bound")
            v = self.integer(int(s, 16))
            if hex(v) != s:
                raise ValueError("noncanonical rational hex")
            values.append(v)
        q = self.q(*values)
        if values[1] <= 0 or q.numerator != values[0] or q.denominator != values[1]:
            raise ValueError("non-reduced rational pair")
        return q

    def output_bytes(self, data):
        self.check_time()
        self.output_emitted += len(data)
        self.check_output_bound(self.output_emitted)

    def check_output_bound(self, byte_count):
        self.check_time()
        if byte_count > self.OUTPUT:
            raise BudgetStop("combined output cap")

    def snapshot(self):
        self.check_time()
        return {"primitive_exact_operations": self.operations,
                "elapsed_seconds": time.monotonic() - self.started,
                "limits": {"operations": self.OPS, "seconds": self.SECONDS,
                           "memory_bytes": self.MEMORY, "output_bytes": self.OUTPUT,
                           "integer_bits": self.BITS},
                "effective_address_space_ceiling_bytes": self.effective_memory_ceiling,
                "output_bytes_already_emitted": self.output_emitted}
