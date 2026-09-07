# Router path portability maintenance — 2026-09-07

Status: LOCAL_FIX_VERIFIED / CONTROL_PLANE_MAINTENANCE / AUXILIARY_ONLY.
Auxiliary work package: `/root/stability_research`; no research-role registration or mathematical claim.
Worktree: `D:/em/owner-control-20260907`.
Source HEAD: `57cc1add4160049cb89dae3fcb788c2a54423dd2`.
Reused Global Knowledge read lease: `main@4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`.

## Change

`tools/enterprise_toolbox.py` used platform-dependent `str(path.relative_to(ROOT))` for two externally returned repository-relative paths. On Windows this returned backslashes, so the current source discovery test could not find `src/enterprise_math/precision.py`.

Exactly two source lines now call `path.relative_to(ROOT).as_posix()`:

- Line 66: each `loaded_addenda` entry.
- Line 164: each executable module's `source_ref`.

Loading paths, directory enumeration, method concatenation, ranking, and source scanning are unchanged. No tests, registry entries, mathematical sources, or central policy were changed by this work package. The concurrently modified runtime-lane test belongs to another auxiliary work package.

## Verification

On Windows, `python -m unittest tests.test_enterprise_toolbox_router -v` first reproduced one failure in six tests: `test_current_source_scan_finds_precision_module`, with five passing. After the fix, all six existing tests passed.

A separate live inventory check passed:

- All 50 actual `loaded_addenda` paths use forward slashes, are relative, and resolve to existing files.
- Their order matches the existing sorted JSON enumeration.
- The complete 86-method list equals the base inventory followed by the same ordered addenda, including record content and order.
- All 12 returned module `source_ref` values for `precision carry borrow projection` use forward slashes and include `src/enterprise_math/precision.py`.

`git diff --check` passed. The final source diff contains only the two intended replacements; the original absence of an end-of-file newline was preserved. The source scan emits an existing invalid-escape `SyntaxWarning` while parsing another module; it does not fail the tests and is outside this patch.

Final source SHA256: `d0f0383a344194133a303f6758142bfd4ecd56deb35a3008f4bf6009ccf6892b`.

This is a local verified patch awaiting the parent's serial publication/integration. This work package performed no commit or remote action.
