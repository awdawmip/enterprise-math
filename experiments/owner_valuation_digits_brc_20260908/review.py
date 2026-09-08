"""Bounded, quotient-free-oracle review of the captured digits-only candidate.

Run in a fresh process: python -B -X utf8 review.py
This deliberately does not import package __init__, histogram, or primality.
"""

from __future__ import annotations

import ast
import hashlib
import importlib
import inspect
import json
import sys
import time
import types
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_integers(values) -> str:
    return sha(json.dumps([hex(value) for value in values], separators=(",", ":")).encode())


def check_chain(n, p, digits, traces, trace_type) -> None:
    current = n
    assert len(traces) == (len(digits) if n else 0)
    for digit, trace in zip(digits, traces):
        assert type(trace) is trace_type
        assert (trace.numerator, trace.denominator) == (current, p)
        assert trace.evaluation_kind == "BRC_DIVISION_EVALUATION"
        assert trace.reconstruct() == current == p * trace.quotient + trace.remainder
        assert trace.collapsed_numerator == p * trace.quotient
        assert digit == trace.remainder and 0 <= digit < p
        assert 0 <= trace.quotient < current
        current = trace.quotient
    assert current == 0


def main() -> None:
    started = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()
    limit_before = sys.get_int_max_str_digits()
    metadata = json.loads(HERE.joinpath("inputs.json").read_text(encoding="utf-8"))
    for path, pin in metadata["captured"].items():
        assert sha(HERE.joinpath("frozen", path).read_bytes()) == pin["sha256"]
    candidate_path = HERE.joinpath("owner_arithmetic_20260907.candidate.py")
    candidate = candidate_path.read_bytes()
    assert sha(candidate) == metadata["candidate_sha256"]
    original = HERE.joinpath("frozen/research_notes/owner_arithmetic_20260907.py").read_bytes()
    old_ast = ast.parse(original)
    new_ast = ast.parse(candidate)

    def node(tree, name):
        return next(item for item in tree.body if getattr(item, "name", None) == name)

    def segment(data, tree, name):
        item = node(tree, name)
        return b"".join(data.splitlines(keepends=True)[item.lineno - 1:item.end_lineno])

    protected = {}
    for name in ("_integer", "ComputationBudgetExceeded", "_digit_coefficients",
                 "SignedValuationSpectrum", "signed_valuation_spectrum"):
        before = segment(original, old_ast, name)
        assert before == segment(candidate, new_ast, name)
        protected[name] = sha(before)
    suffix_marker = b"@lru_cache(maxsize=256)"
    assert original[original.index(suffix_marker):] == candidate[candidate.index(suffix_marker):]
    suffix_sha = sha(original[original.index(suffix_marker):])
    changed_ast = [item for item in ast.walk(node(new_ast, "digits_lsd"))
                   if isinstance(item, (ast.Div, ast.FloorDiv, ast.Mod))
                   or isinstance(item, ast.Name) and item.id in {"divmod", "Fraction", "Decimal"}]
    assert not changed_ast

    # Import the exact facade/dependencies through a test-only namespace package.
    # The repository's broad __init__ import chain is intentionally not executed.
    assert "enterprise_math" not in sys.modules
    package = types.ModuleType("enterprise_math")
    package.__path__ = [str(HERE.joinpath("frozen/src/enterprise_math"))]
    sys.modules["enterprise_math"] = package
    facade = importlib.import_module("enterprise_math.exact_arithmetic")
    native_division = importlib.import_module("enterprise_math.division")
    native_functions = {"division": facade.division,
                        "brc_evaluate_division": facade.brc_evaluate_division,
                        "euclidean_state": native_division.euclidean_state,
                        "multiple_collapse": native_division.multiple_collapse,
                        "integer_quotient": native_division.integer_quotient}
    code_names = {function.__code__: name for name, function in native_functions.items()}
    counts = dict.fromkeys(native_functions, 0)

    def profile(frame, event, arg):
        if event == "call" and frame.f_code in code_names:
            counts[code_names[frame.f_code]] += 1

    def no_legacy_divmod(*args):
        raise AssertionError("LEGACY_DIVMOD_BYPASS_REACHED")

    namespace = {"__name__": "bounded_candidate", "BRCDivisionTrace": facade.BRCDivisionTrace,
                 "division": facade.division, "brc_evaluate_division": facade.brc_evaluate_division,
                 "divmod": no_legacy_divmod}
    names = {"_integer", "digits_lsd", "ComputationBudgetExceeded", "signed_valuation_spectrum"}
    selected = ast.Module(body=[ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0),
                               *[item for item in new_ast.body if getattr(item, "name", None) in names]], type_ignores=[])
    exec(compile(ast.fix_missing_locations(selected), str(candidate_path), "exec"), namespace)
    digits_fn = namespace["digits_lsd"]
    # A before-only guard demonstrates the old bypass without computing its quotient.
    old_namespace = {"divmod": no_legacy_divmod}
    exec(compile(ast.Module(body=[node(old_ast, "digits_lsd")], type_ignores=[]), "frozen_digits", "exec"), old_namespace)
    try:
        old_namespace["digits_lsd"](7, 3)
    except AssertionError as exc:
        assert str(exc) == "LEGACY_DIVMOD_BYPASS_REACHED"
    else:
        raise AssertionError("before guard did not detect divmod")

    # N is built from known low-first tuples by multiplication and addition only.
    known = [
        ("zero", 2, (0,)), ("one", 2, (1,)),
        ("below_base", 3, (2,)), ("exact_base", 3, (0, 1)),
        ("below_power", 3, (2,) * 7), ("exact_power", 3, (0,) * 7 + (1,)),
        ("mixed_base31", 31, (30, 0, 7, 30, 1)),
        ("default_256_digit_cap_minus_one", 2, (1,) * 256),
        ("helper_composite_base", 4, (3, 0, 2)),
        ("helper_large_integer_outside_public_prime_budget", (1 << 17001) + 1, ((1 << 17000) + 37,)),
    ]
    cases = []
    sys.setprofile(profile)
    try:
        for label, p, expected in known:
            n = sum(digit * p**index for index, digit in enumerate(expected))
            seed = object()
            collector = [seed]
            previous = counts.copy()
            actual = digits_fn(n, p, arithmetic_trace=collector)
            assert type(actual) is tuple and actual == expected and collector[0] is seed
            traces = collector[1:]
            check_chain(n, p, actual, traces, facade.BRCDivisionTrace)
            delta = {name: counts[name] - previous[name] for name in counts}
            expected_calls = len(actual) if n else 0
            assert delta == {"division": expected_calls, "brc_evaluate_division": expected_calls,
                             "euclidean_state": expected_calls, "multiple_collapse": expected_calls,
                             "integer_quotient": expected_calls * 2}
            trace_encoded = [{key: hex(value) if isinstance(value, int) else value
                              for key, value in asdict(trace).items()} for trace in traces]
            cases.append({"id": label, "input_bit_lengths": [n.bit_length(), p.bit_length()],
                          "input_sha256": digest_integers([n, p]), "output_sha256": digest_integers(actual),
                          "digit_count": len(actual), "trace_count": len(traces), "calls": delta,
                          "full_trace_digest_hex_integer_encoding": sha(json.dumps(trace_encoded, sort_keys=True, separators=(",", ":")).encode()),
                          "status": "PASS"})

        helper_rejections = []
        for label, n, p, error in [
            ("negative_n", -1, 2, ValueError), ("bool_n", True, 2, TypeError),
            ("noninteger_n", "7", 2, TypeError), ("base_zero", 2, 0, ValueError),
            ("base_one", 2, 1, ValueError), ("negative_base", 2, -2, ValueError),
            ("bool_base", 2, True, TypeError), ("noninteger_base", 2, "3", TypeError),
        ]:
            previous = counts.copy()
            collector = []
            try:
                digits_fn(n, p, arithmetic_trace=collector)
            except error as exc:
                helper_rejections.append({"id": label, "exception": type(exc).__name__, "message": str(exc)})
            else:
                raise AssertionError(label)
            assert counts == previous and collector == []

        # Stop before the first histogram constructor. This tests caller routing,
        # not primality, histogram, carry execution, or signed spectrum results.
        class HistogramBoundaryReached(Exception):
            pass

        def histogram_stop(*args):
            raise HistogramBoundaryReached

        prime_queries = []

        def finite_prime_stub(p):
            prime_queries.append(p)
            assert p in {2, 3, 4}
            return p in {2, 3}

        namespace.update(WeightHistogram=histogram_stop, is_prime=finite_prime_stub)
        public_fn = namespace["signed_valuation_spectrum"]
        caller_cases = []
        for label, args, kwargs, expected_error, expected_calls, expected_primes in [
            ("zero_routes_to_histogram", (0, 2), {}, HistogramBoundaryReached, 0, [2]),
            ("last_allowed_small_digit_budget", (15, 2), {"max_digits": 4}, HistogramBoundaryReached, 4, [2]),
            ("negative_radius", (-1, 2), {}, ValueError, 0, []),
            ("bool_radius", (True, 2), {}, TypeError, 0, []),
            ("composite_prime", (2, 4), {}, ValueError, 0, [4]),
            ("bool_prime", (2, True), {}, TypeError, 0, []),
            ("prime_budget", (2, 37), {}, namespace["ComputationBudgetExceeded"], 0, []),
            ("small_digit_budget_boundary", (4, 2), {"max_digits": 2}, namespace["ComputationBudgetExceeded"], 0, [2]),
            ("default_digit_budget_boundary", (1 << 256, 2), {}, namespace["ComputationBudgetExceeded"], 0, [2]),
            ("invalid_max_prime", (2, 2), {"max_prime": 1}, ValueError, 0, []),
            ("invalid_max_digits", (2, 2), {"max_digits": 0}, ValueError, 0, []),
        ]:
            previous = counts.copy()
            prime_queries.clear()
            try:
                public_fn(*args, **kwargs)
            except expected_error as exc:
                observed_error = type(exc).__name__
            else:
                raise AssertionError(label)
            assert counts["brc_evaluate_division"] - previous["brc_evaluate_division"] == expected_calls
            assert prime_queries == expected_primes
            caller_cases.append({"id": label, "exception": observed_error,
                                 "facade_calls": expected_calls, "finite_stub_prime_queries": prime_queries.copy(),
                                 "status": "PASS"})
    finally:
        sys.setprofile(None)

    assert sys.get_int_max_str_digits() == limit_before
    assert "enterprise_math.brc_histogram" not in sys.modules and "enterprise_math.legendre" not in sys.modules
    protected_worktree = {}
    for path, previous in metadata["source_worktree_before"].items():
        local = Path(metadata["source_worktree"]).joinpath(path)
        current = sha(local.read_bytes()) if local.is_file() else None
        assert current == previous, path
        protected_worktree[path] = current
    native_identity = {name: {"module": function.__module__, "qualname": function.__qualname__,
                              "loaded_file": inspect.getsourcefile(function),
                              "first_line": function.__code__.co_firstlineno,
                              "loaded_file_sha256": sha(Path(inspect.getsourcefile(function)).read_bytes())}
                       for name, function in native_functions.items()}
    report = {"status": "PASS_BOUNDED_DIGITS_MIGRATION_ONLY", "started_utc": started,
              "completed_utc": datetime.now(timezone.utc).isoformat(),
              "elapsed_seconds": time.perf_counter() - start,
              "argv": [sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve())],
              "python": sys.version, "executed_script_sha256": sha(Path(__file__).read_bytes()),
              "inputs_manifest_sha256": sha(HERE.joinpath("inputs.json").read_bytes()),
              "candidate_sha256": sha(candidate), "published_source": metadata["published_source"],
              "actual_local_source": metadata["actual_local_source"], "actual_local_tree": metadata["actual_local_tree"],
              "captured_source_pins": metadata["captured"], "native_code_object_identities": native_identity,
              "actual_native_code_object_call_counts": counts,
              "valid_digit_cases": cases, "invalid_standalone_helper_rejections": helper_rejections,
              "caller_pre_histogram_cases": caller_cases,
              "unchanged_definitions_sha256": protected, "unchanged_carry_and_output_suffix_sha256": suffix_sha,
              "protected_selected_source_worktree_hashes": protected_worktree,
              "integer_decimal_limit_before_after": [limit_before, sys.get_int_max_str_digits()],
              "local_static_digits_no_divmod_or_division_operators": True,
              "before_guard": "Original divmod entry blocked before it computed; old invalid nonterminating inputs not run.",
              "trace_visibility": "Optional helper collector receives every native BRCDivisionTrace; unchanged public API supplies none and neither returns nor persists digit traces.",
              "limits": ["Not a whole valuation tool V2 compliance result or mathematical L4 admission.",
                         "No full spectrum, carry loop, signed output, primality implementation, histogram arithmetic, or Fraction chain was executed.",
                         "Caller tests use an explicit finite primality stub and stop at the first histogram constructor.",
                         "Full package __init__ was not executed; exact three-file facade dependency island loaded by a test namespace.",
                         "Valid-domain preservation follows Euclidean uniqueness plus unchanged downstream bytes; not a new complete signed-output runtime comparison.",
                         "Standalone helper invalid-input rejection is a separate tightening; helper has no new resource cap, public limits remain unchanged.",
                         "Large/composite helper cases do not relax public prime or digit budgets."]}
    HERE.joinpath("review.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "valid_digit_cases": len(cases),
                      "standalone_rejections": len(helper_rejections), "caller_boundary_cases": len(caller_cases),
                      "native_calls": counts, "elapsed_seconds": report["elapsed_seconds"],
                      "review_sha256": sha(HERE.joinpath("review.json").read_bytes())}))


if __name__ == "__main__":
    main()
