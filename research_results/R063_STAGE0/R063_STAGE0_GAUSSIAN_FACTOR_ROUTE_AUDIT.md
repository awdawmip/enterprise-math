# R063 Stage 0 — Gaussian factor route audit

C4 does not scan the target Diophantine equation. It factors the norm integer and uses the UFD structure of `Z[J]`.

For a norm integer `M`, the construction is:

1. `2` ramifies through the Gaussian prime `1+J`; its Gaussian exponent is fixed by `v_2(M)`.
2. Every prime `q == 3 (mod 4)` remains inert; `v_q(M)` must be even and contributes the fixed integer Gaussian factor `q^(v_q(M)/2)`.
3. Every prime `p == 1 (mod 4)` splits as `pi_p * conjugate(pi_p)`. If `v_p(M)=e`, choose `t=0..e` and allocate exponents `(t,e-t)` between the conjugate pair.
4. Multiply by the four units and keep the ordered nonnegative sector representatives.

This enumerates every Gaussian integer of norm `M` and nothing else by unique factorization.

## Central factorization metadata

```json
{
  "gaussian_prime_rows": [
    {
      "exponent_in_norm": 2,
      "gaussian_exponent_fixed": 2,
      "gaussian_prime": [
        1,
        1
      ],
      "gaussian_type": "RAMIFIED",
      "prime": 2
    },
    {
      "allocation_range": [
        0,
        4
      ],
      "exponent_in_norm": 4,
      "gaussian_type": "SPLIT",
      "pi": [
        2,
        1
      ],
      "pi_conjugate": [
        2,
        -1
      ],
      "prime": 5
    }
  ],
  "integer": 2500,
  "integer_factorization": [
    {
      "exponent": 2,
      "prime": 2
    },
    {
      "exponent": 4,
      "prime": 5
    }
  ],
  "representable_as_gaussian_norm": true
}
```

## Discovered first-quadrant factor-allocation channels

- `(0, 50)` <- `[{"channel_id": "C4-0000", "pre_unit_value": [0, 50], "split_prime_allocations": [{"conjugate_exponent": 2, "pi_exponent": 2, "prime": 5}], "unit": "1", "value": [0, 50]}]`
- `(14, 48)` <- `[{"channel_id": "C4-0001", "pre_unit_value": [48, -14], "split_prime_allocations": [{"conjugate_exponent": 4, "pi_exponent": 0, "prime": 5}], "unit": "J", "value": [14, 48]}]`
- `(30, 40)` <- `[{"channel_id": "C4-0002", "pre_unit_value": [-40, 30], "split_prime_allocations": [{"conjugate_exponent": 1, "pi_exponent": 3, "prime": 5}], "unit": "-J", "value": [30, 40]}]`
- `(40, 30)` <- `[{"channel_id": "C4-0003", "pre_unit_value": [40, 30], "split_prime_allocations": [{"conjugate_exponent": 3, "pi_exponent": 1, "prime": 5}], "unit": "1", "value": [40, 30]}]`
- `(48, 14)` <- `[{"channel_id": "C4-0004", "pre_unit_value": [-48, -14], "split_prime_allocations": [{"conjugate_exponent": 0, "pi_exponent": 4, "prime": 5}], "unit": "-1", "value": [48, 14]}]`
- `(50, 0)` <- `[{"channel_id": "C4-0005", "pre_unit_value": [0, 50], "split_prime_allocations": [{"conjugate_exponent": 2, "pi_exponent": 2, "prime": 5}], "unit": "-J", "value": [50, 0]}]`

C4 root equality with the post-freeze N=2500 brute fiber: `True`. C4 and canonical C3 agree **before** brute verification.

C4 is stronger as a factorization provenance description: it exposes Gaussian prime-exponent allocation directly. C3 instead exposes the scalar-root-to-Euclid scaled-square channel. They quotient to the same component-root set for square native norms.
