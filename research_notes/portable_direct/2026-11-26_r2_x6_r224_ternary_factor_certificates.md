# X6 R224 — exact ternary support-factor certificate spectrum

2026-11-26; AUTHOR PROOF AND EXACT COMPUTATION / NOT_REVIEWED. Same frozen static six-pair BRC input as R223@91e99a63adfe2021ec59c8ee0e8553f40975be68:research_notes/portable_direct/2026-11-26_r2_x6_r223_exact_local_output_cover.md, Port 10 and positive (17t,B,22t,D). P000 and bank theorem scope retained. No native spatial-transfer or full-direction rerun claim.

## Path resource lower bound via exact factor certificates

Let S be the complete ternary support-sign fibers, L the 35 fixed output labels, and C_a the fibers on which a is legal (exact intersection over all raw arrangement faces). Fix f in S and a with f in C_a. For each g outside C_a define Delta(f,g) as the indices of support forms with different ternary signs at f and g. A set H of factors certifies a at f precisely when H intersects every Delta(f,g), g outside C_a: equivalently no incompatible fiber agrees with f on all observed factors. The exact minimal certificate size c(f) is the minimum hitting-set cardinality over all legal a. If Delta1 is contained in Delta2, hitting Delta1 suffices for Delta2; deleting supersets is exact. Search recursively on one nonempty remaining difference set, branching on every member, removing all hit sets. A greedy packing of pairwise disjoint remaining difference sets is a sound lower bound; no probabilistic or approximate pruning. All successful certificates are checked against every incompatible fiber, and smaller budgets exhausted. The factor certificate is an ideal ternary readout resource, not the number of Boolean sign comparisons.

Every path in a depth-d tree using support-linear and support-product queries, at most k quadratic per path, encounters at most d+k distinct factors (possibly fewer through repeats). If an incompatible fiber g agrees with f on those factors, every query along f's path gives the same answer at g, hence reaches the same output, contradiction. Thus max_f c(f) ≤ d+k. This provides a library- and output-alphabet-specific necessary condition. It does not apply to unrestricted new linear forms or unlisted outputs without a new proof. R223's tree supplies a certificate of size ≤8 for every f; R224 determines the exact spectrum, not merely that upper bound. The exact result is max c(f)=4, so the direct factor bound at depth six is k≥max(0,4−6). Existing general 1≤K6≤3 remains unchanged unless this scoped bound supplies additional restricted-library information.

## Actual exact computation

All 1925 fibers, 35 labels, and all incompatible fiber pairs covered. Counted 4125246 raw difference-set incidences across legal labels, 8905 inclusion-minimal constraints after reduction and 16215 recursive hitting-set calls. For every fiber the stored certificate chooses a legal output and a minimum factor subset. Raw representative count 43685. Verification uses exact masks and signs; R220/R221 full-direction evidence inherited. No independent review.

## Exact results and full certificates

```json
{
  "rawLines": 256,
  "cells": 11487,
  "positiveRepresentatives": 43685,
  "patterns": 1925,
  "labels": 35,
  "rawDiffs": 4125246,
  "minimalDiffs": 8905,
  "hitCalls": 16215,
  "hist": {
    "1": 9,
    "2": 903,
    "3": 1010,
    "4": 3
  },
  "maxCert": 4,
  "examples": [
    {
      "fiber": 54,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 4,
      "factors": [
        2,
        8,
        9,
        10
      ],
      "minimalConstraints": 4,
      "allLegal": [
        {
          "label": [
            695,
            4
          ],
          "cost": 4,
          "factors": [
            2,
            8,
            9,
            10
          ],
          "minimalConstraints": 4
        }
      ]
    },
    {
      "fiber": 58,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 4,
      "factors": [
        2,
        8,
        9,
        10
      ],
      "minimalConstraints": 4,
      "allLegal": [
        {
          "label": [
            695,
            4
          ],
          "cost": 4,
          "factors": [
            2,
            8,
            9,
            10
          ],
          "minimalConstraints": 4
        }
      ]
    },
    {
      "fiber": 64,
      "sign": "1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4
      ],
      "cost": 4,
      "factors": [
        2,
        7,
        8,
        9
      ],
      "minimalConstraints": 4,
      "allLegal": [
        {
          "label": [
            951,
            4
          ],
          "cost": 4,
          "factors": [
            2,
            7,
            8,
            9
          ],
          "minimalConstraints": 4
        }
      ]
    }
  ],
  "certs": [
    {
      "fiber": 0,
      "sign": "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        6
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1,
      "sign": "1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        6
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 2,
      "sign": "1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        6
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 3,
      "sign": "1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        6
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 4,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        6,
        24
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 5,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 6,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 7,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 8,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 9,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 10,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 11,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 12,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        19
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 13,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        19
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 14,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 15,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 16,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 17,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 18,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 19,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 20,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 21,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 22,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 23,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 24,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,0,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        11
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 25,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,0,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        11
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 26,
      "sign": "1,1,1,1,1,1,-1,1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 27,
      "sign": "1,1,0,1,1,1,-1,1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 28,
      "sign": "1,1,0,1,1,1,-1,1,1,0,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 29,
      "sign": "1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 30,
      "sign": "1,1,1,1,1,1,-1,1,1,1,0,0,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        11
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 31,
      "sign": "1,1,1,1,1,1,-1,1,1,0,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        9
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 32,
      "sign": "1,1,1,1,1,1,-1,1,1,0,0,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        9
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 33,
      "sign": "1,1,1,1,1,1,-1,1,1,1,0,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 34,
      "sign": "1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 35,
      "sign": "1,1,1,1,1,1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        8,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 36,
      "sign": "1,1,1,1,1,1,-1,1,0,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        11
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 37,
      "sign": "1,1,1,1,1,1,-1,1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        11
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 38,
      "sign": "1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 39,
      "sign": "1,1,1,1,1,1,-1,1,1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        9
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 40,
      "sign": "1,1,1,1,1,1,-1,1,0,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        9
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 41,
      "sign": "1,1,1,1,1,1,-1,1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        8,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 42,
      "sign": "1,1,1,1,1,1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        8,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 43,
      "sign": "1,1,1,1,1,1,-1,1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        11
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 44,
      "sign": "1,1,1,1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        8,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 45,
      "sign": "1,1,1,1,1,1,-1,1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        9
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 46,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 47,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,0,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 48,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        10
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 49,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,0,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        10,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 50,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 51,
      "sign": "1,1,0,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 52,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,0,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 53,
      "sign": "1,1,0,1,1,1,-1,1,1,-1,0,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 54,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 4,
      "factors": [
        2,
        8,
        9,
        10
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 55,
      "sign": "1,1,1,1,1,1,-1,1,0,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 56,
      "sign": "1,1,1,1,1,1,-1,1,0,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 2,
      "factors": [
        8,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 57,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 3,
      "factors": [
        8,
        10,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 58,
      "sign": "1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 4,
      "factors": [
        2,
        8,
        9,
        10
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 59,
      "sign": "1,1,1,1,1,1,-1,1,0,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        695,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 60,
      "sign": "1,1,0,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        9
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 61,
      "sign": "1,1,0,1,1,1,-1,1,0,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 62,
      "sign": "1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4
      ],
      "cost": 3,
      "factors": [
        8,
        9,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 63,
      "sign": "1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4
      ],
      "cost": 2,
      "factors": [
        8,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 64,
      "sign": "1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4
      ],
      "cost": 4,
      "factors": [
        2,
        7,
        8,
        9
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 65,
      "sign": "1,1,0,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 66,
      "sign": "1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        38
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 67,
      "sign": "1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        38
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 68,
      "sign": "1,1,1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        7
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 69,
      "sign": "1,1,0,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 70,
      "sign": "1,1,0,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 71,
      "sign": "1,1,0,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        2,
        7
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 72,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        951,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        41
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 73,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 74,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        25,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 75,
      "sign": "1,1,0,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        4,
        7
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 76,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        41
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 77,
      "sign": "1,1,0,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 78,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        29,
        41
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 79,
      "sign": "1,1,0,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        29,
        41
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 80,
      "sign": "1,1,0,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 81,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 82,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 83,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 84,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 85,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        6,
        24
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 86,
      "sign": "1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        6
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 87,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        15,
        24
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 88,
      "sign": "1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        15
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 89,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 90,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 91,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        6,
        24
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 92,
      "sign": "1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        6
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 93,
      "sign": "1,1,-1,0,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        6,
        24
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 94,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 95,
      "sign": "1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        28
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 96,
      "sign": "1,1,-1,0,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 97,
      "sign": "1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        6,
        24
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 98,
      "sign": "1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        6
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 99,
      "sign": "1,1,-1,0,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        6,
        24
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 100,
      "sign": "1,1,-1,0,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        6
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 101,
      "sign": "1,1,-1,0,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 102,
      "sign": "1,1,-1,0,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 103,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        19
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 104,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        15
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 105,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        19
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 106,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 107,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        19
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 108,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        19
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 109,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 110,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        6,
        23
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 111,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        23
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 112,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        15,
        28
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 113,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 114,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        19
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 115,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        15
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 116,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        15,
        19
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 117,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        19
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 118,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        23
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 119,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 120,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        23
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 121,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 122,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 123,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 124,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 125,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 126,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 127,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 128,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 129,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        9,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 130,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        9,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 131,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        24,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 132,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 133,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 134,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        16,
        19
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 135,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 136,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        23
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 137,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        23
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 138,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 139,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 140,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        16,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 141,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        23,
        30
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 142,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 143,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        23,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 144,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 145,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 146,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        23,
        27
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 147,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 148,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 149,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 150,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 151,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        19,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 152,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 153,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 154,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        16,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 155,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        23,
        26,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 156,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        26,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 157,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 158,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 159,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        23,
        26,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 160,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 161,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        23,
        26,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 162,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 163,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 164,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 165,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 166,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 167,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 168,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 169,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 170,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        16
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 171,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 172,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 173,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 174,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 175,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 176,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        16
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 177,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 178,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 179,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        25,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 180,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 181,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        25,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 182,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        25,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 183,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 184,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        25,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 185,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        31
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 186,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        16
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 187,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        25,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 188,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 189,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 190,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 191,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        19,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 192,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 193,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,1,1,1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        16,
        19
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 194,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 195,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,0,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 196,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 197,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 198,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 199,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 200,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 201,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 202,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 203,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 204,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 205,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 206,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 207,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 208,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 209,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 210,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 211,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 212,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 213,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 214,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,0,1,1,1,1,-1,1,1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 215,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 216,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 217,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 218,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 219,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 220,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        27,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 221,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        27,
        28
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 222,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 223,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 224,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        27,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 225,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 226,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 227,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 228,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,1,1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 229,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 230,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 231,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 232,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 233,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 234,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,0,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 235,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 236,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 237,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 238,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 239,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 240,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,0,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 241,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,0,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 242,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 243,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 244,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        27,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 245,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 246,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        27,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 247,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 248,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 249,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 250,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 251,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        26,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 252,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 253,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 254,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        9,
        27,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 255,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        9,
        26,
        30
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 256,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        26,
        30
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 257,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,0,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        26,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 258,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 259,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 260,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 261,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        26,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 262,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,0,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        26,
        27
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 263,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        26,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 264,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        26,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 265,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        16,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 266,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        16,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 267,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 268,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 269,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 270,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        16,
        26
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 271,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 272,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 273,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 274,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        11,
        16,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 275,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        11,
        31
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 276,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        11,
        16,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 277,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        11,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 278,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 279,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        11,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 280,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 281,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        25
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 282,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        9,
        11,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 283,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 284,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 285,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 286,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 287,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 288,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 289,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 290,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 291,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 292,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 293,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 294,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 295,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 296,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 297,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 298,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 299,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 300,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 301,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 302,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 303,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        27,
        31
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 304,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 305,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 306,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        11,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 307,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        11,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 308,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 309,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 310,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 311,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 312,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        9,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 313,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 314,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 2,
      "factors": [
        9,
        31
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 315,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 316,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 317,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 318,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 319,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 320,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        11
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 321,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 322,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 323,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 324,
      "sign": "1,1,-1,-1,1,1,0,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 325,
      "sign": "1,1,-1,-1,1,1,0,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        9
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 326,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 327,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 328,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 329,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 330,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 331,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 332,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 333,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 334,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 335,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 336,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 337,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 338,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 339,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 340,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 341,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 342,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 343,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 344,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 345,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 346,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 347,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 348,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 349,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        6,
        17
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 350,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 351,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 352,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 353,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 354,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 355,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 356,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 357,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 358,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 359,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 360,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 361,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        21,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 362,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        6,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 363,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 364,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        14,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 365,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 366,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 367,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 368,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 369,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 370,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 371,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 372,
      "sign": "1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 373,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,0,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 374,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,0,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 375,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 376,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 377,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 378,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,0,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 379,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 380,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 381,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 382,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 383,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 384,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 385,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 386,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 387,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 388,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 389,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        29
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 390,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        29
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 391,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        29
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 392,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        9,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 393,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 394,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 395,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 396,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 397,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,0,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 398,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,0,1,-1,-1,0,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 399,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 400,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 401,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 402,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 403,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 404,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 405,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,0,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 406,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 407,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 408,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 409,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 410,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        11,
        16,
        29
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 411,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 2,
      "factors": [
        9,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 412,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        9,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 413,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        16,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 414,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 415,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        16,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 416,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        12,
        16,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 417,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 418,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 419,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        7,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 420,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 421,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 422,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 423,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 424,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 425,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 426,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 427,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 428,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 429,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 430,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 431,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 432,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 433,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 434,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 435,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        14,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 436,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        14,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 437,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 438,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 439,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 440,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 441,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 442,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 443,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 444,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 445,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        17,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 446,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 447,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 448,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 449,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 450,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        7,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 451,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 452,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 453,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        9,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 454,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        7,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 455,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        7,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 456,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 457,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 458,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 459,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 460,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 461,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 462,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 463,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 464,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 465,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 466,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,0,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 467,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 468,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 469,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 470,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 471,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 472,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 473,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 474,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 475,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 476,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 477,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 478,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 479,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 480,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 481,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 482,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,0,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 483,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,0,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 484,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 485,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 486,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,0,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 487,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,0,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 488,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,0,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 489,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,0,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        25,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 490,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 491,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 492,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        25,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 493,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 494,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,0,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 495,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 496,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,0,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 497,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 498,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 499,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 500,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 501,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 502,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 503,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 504,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 505,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 506,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 507,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 508,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 509,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 510,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 511,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 512,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        17
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 513,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,0,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 514,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,0,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 515,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 516,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 517,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,1,1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 518,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 519,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 520,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 521,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 522,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 523,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        9,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 524,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        9,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 525,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 526,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 527,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,0,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 528,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,0,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 529,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,0,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 530,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,0,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 531,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 532,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        9,
        46
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 533,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 534,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        9,
        12,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 535,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 536,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 537,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 538,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 539,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 540,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 541,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 542,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 543,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 544,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 545,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 546,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 547,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 548,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 549,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 550,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 551,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 552,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 553,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 554,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        25,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 555,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        25,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 556,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 557,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 558,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 559,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 560,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 561,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 562,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        12,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 563,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,0,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 564,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,0,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 565,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 566,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 567,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 568,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 569,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 570,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 571,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 572,
      "sign": "1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 573,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 574,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 575,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 576,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 577,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 578,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        6,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 579,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 580,
      "sign": "1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 581,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 582,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 583,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,0,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 584,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,0,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        22,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 585,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,0,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 586,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,0,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 587,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 588,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 589,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        19,
        22,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 590,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,0,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 591,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 592,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 593,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 594,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,0,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 595,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 596,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 597,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 598,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 599,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 600,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 601,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 602,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 603,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 604,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        6,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 605,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 606,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 607,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 608,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,0,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 609,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 610,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,1,1,1,-1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 611,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 612,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,1,1,1,-1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 613,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,0,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 614,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        17,
        19,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 615,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 616,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,-1,1,1,-1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 617,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 618,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,0,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 619,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 620,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 621,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        132,
        32
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 622,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 623,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 624,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        24
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 625,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 626,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 627,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        24,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 628,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 629,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 630,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,0,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        2,
        28
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 631,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        17,
        19,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 632,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,0,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 633,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,0,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 634,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        17,
        19,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 635,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        164,
        16
      ],
      "cost": 3,
      "factors": [
        17,
        19,
        28
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 636,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,0,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        164,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        19
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 637,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 638,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 639,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        676,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        19,
        23
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 640,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 641,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 642,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,0,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        676,
        16
      ],
      "cost": 2,
      "factors": [
        16,
        23
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 643,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 644,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 645,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        692,
        16
      ],
      "cost": 3,
      "factors": [
        16,
        23,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 646,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 647,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 648,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        692,
        16
      ],
      "cost": 2,
      "factors": [
        6,
        26
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 649,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 650,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        26
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 651,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 652,
      "sign": "1,1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 653,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        23
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 654,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,-1,1,1,1,0,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        15,
        23
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 655,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 656,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        15
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 657,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        15,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 658,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,0,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        26
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 659,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 660,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        6,
        11,
        15
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 661,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 662,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        11,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 663,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        11,
        15,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 664,
      "sign": "1,1,-1,0,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        9,
        11
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 665,
      "sign": "1,1,-1,0,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        9
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 666,
      "sign": "1,1,-1,1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        9
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 667,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        9,
        15,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 668,
      "sign": "1,1,-1,0,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        9,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 669,
      "sign": "1,1,-1,0,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 670,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 671,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,0,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        3,
        11
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 672,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        11,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 673,
      "sign": "1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        9,
        11,
        30
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 674,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 675,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 676,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 677,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        9,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 678,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 679,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 680,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 681,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 682,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        16,
        25,
        29
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 683,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 684,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        16,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 685,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        6,
        29,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 686,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 2,
      "factors": [
        31,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 687,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        693,
        64
      ],
      "cost": 3,
      "factors": [
        9,
        16,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 688,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 689,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        16,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 690,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        16,
        29
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 691,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        12,
        16,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 692,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        12,
        16,
        29
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 693,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 694,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        7,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 695,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 696,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 697,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 698,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        17,
        21
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 699,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 700,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 701,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 702,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 703,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        36,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 704,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 705,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 706,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        7,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 707,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 708,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 709,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 710,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 711,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 712,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 713,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        9,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 714,
      "sign": "1,1,-1,-1,1,1,-1,1,1,0,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 715,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        9,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 716,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        9,
        25,
        30
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 717,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 718,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        6,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 719,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        30
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 720,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        30
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 721,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        16,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 722,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        16,
        29
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 723,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        29,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 724,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        16,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 725,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        16,
        42
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 726,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        16,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 727,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 728,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        7,
        18
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 729,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 730,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        13
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 731,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 732,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 733,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 734,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        7,
        31
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 735,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        7,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 736,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 737,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 738,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 739,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 740,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 741,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 742,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 743,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 744,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 745,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        17,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 746,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 747,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 748,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 749,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 750,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 751,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 752,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 753,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 754,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 755,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        41,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 756,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        7,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 757,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 758,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 759,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 760,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 761,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 762,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 763,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 764,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 765,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 766,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 767,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 768,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 769,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 770,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 771,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 772,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 773,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        20,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 774,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 775,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 776,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 777,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 778,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 779,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        44,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 780,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 781,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        7,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 782,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 783,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 784,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        17,
        41
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 785,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 786,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 787,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 788,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 789,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,0,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 2,
      "factors": [
        11,
        15
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 790,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,0,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 791,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        6,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 792,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        132,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        27
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 793,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        3,
        9,
        27
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 794,
      "sign": "1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        11,
        15
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 795,
      "sign": "1,1,-1,1,1,1,-1,1,1,0,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        9
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 796,
      "sign": "1,1,-1,1,1,1,-1,1,1,0,1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        9,
        15
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 797,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 798,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        9,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 799,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 800,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        30
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 801,
      "sign": "1,1,-1,0,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 802,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        16,
        29
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 803,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        29,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 804,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        16,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 805,
      "sign": "1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        9,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 806,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        7,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 807,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 808,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 809,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 810,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 811,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 812,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 813,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 814,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 815,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 816,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 817,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 818,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 819,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 820,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        22
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 821,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        22,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 822,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 823,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 824,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        22
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 825,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 826,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 827,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 828,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 829,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 830,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        17,
        44
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 831,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 832,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 833,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,0,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        10
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 834,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,0,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        10,
        15
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 835,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        10,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 836,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 837,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 838,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        8,
        10
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 839,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        8,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 840,
      "sign": "1,1,-1,0,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 841,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 842,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        8,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 843,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 844,
      "sign": "1,1,-1,0,1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 845,
      "sign": "1,1,-1,0,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        8
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 846,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        8,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 847,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 848,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 849,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 850,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 851,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        25,
        30
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 852,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 853,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 854,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 855,
      "sign": "1,1,-1,0,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 856,
      "sign": "1,1,-1,0,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 857,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        10,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 858,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 859,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 860,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 861,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 862,
      "sign": "1,1,-1,0,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 863,
      "sign": "1,1,-1,0,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        10
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 864,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 865,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        9,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 866,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        10
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 867,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        9,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 868,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 2,
      "factors": [
        8,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 869,
      "sign": "1,1,-1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        10,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 870,
      "sign": "1,1,-1,1,1,1,-1,1,0,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        10,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 871,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        25
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 872,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        15,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 873,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        8,
        15,
        25
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 874,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 875,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 876,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 877,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 878,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 879,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 880,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 881,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 882,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        30
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 883,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        7,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 884,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 885,
      "sign": "1,1,-1,0,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 886,
      "sign": "1,1,-1,0,1,1,-1,0,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        3,
        7
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 887,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        7
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 888,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        41
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 889,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 890,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        7
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 891,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        7,
        29
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 892,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        7
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 893,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        29,
        38
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 894,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 895,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        15,
        29,
        42
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 896,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        30,
        36
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 897,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        7,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 898,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        16,
        39
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 899,
      "sign": "1,1,-1,-1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        8,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 900,
      "sign": "1,1,-1,-1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 901,
      "sign": "1,1,-1,-1,1,1,-1,1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 902,
      "sign": "1,1,-1,-1,1,1,-1,0,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        7,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 903,
      "sign": "1,1,-1,-1,1,1,-1,0,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 904,
      "sign": "1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 905,
      "sign": "1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        8,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 906,
      "sign": "1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 907,
      "sign": "1,1,-1,-1,1,1,-1,1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 908,
      "sign": "1,1,-1,-1,1,1,-1,0,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 909,
      "sign": "1,1,-1,-1,1,1,-1,0,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        7,
        10
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 910,
      "sign": "1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        8
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 911,
      "sign": "1,1,-1,-1,1,1,-1,0,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 912,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        8,
        16,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 913,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        8,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 914,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        12,
        13,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 915,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        12,
        13,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 916,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        13,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 917,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 918,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 919,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        29,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 920,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        8,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 921,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        7,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 922,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        7,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 923,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        39,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 924,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 925,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        39,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 926,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        8,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 927,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        8,
        16,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 928,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        29,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 929,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        7,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 930,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        39,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 931,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        10,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 932,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        7,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 933,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        10,
        36,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 934,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 935,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        16,
        36,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 936,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        10,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 937,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        10,
        36,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 938,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 939,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 940,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 941,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 942,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        41
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 943,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 944,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 945,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        8,
        12
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 946,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 947,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        8,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 948,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 949,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 950,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 951,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 952,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 953,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 954,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        16,
        41
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 955,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        16,
        41
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 956,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        10,
        41
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 957,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        16,
        36,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 958,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 959,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        10,
        36,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 960,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,0,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 961,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        10,
        36
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 962,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        36
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 963,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        10,
        12,
        36
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 964,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        10,
        12
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 965,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        10,
        12,
        36
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 966,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        10,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 967,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 968,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 969,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 3,
      "factors": [
        7,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 970,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,0,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        64
      ],
      "cost": 2,
      "factors": [
        12,
        16
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 971,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        10,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 972,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        10,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 973,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        10,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 974,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        5,
        12,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 975,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        36
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 976,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 977,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        12,
        13,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 978,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 979,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 980,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 981,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        12,
        13,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 982,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 983,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        29,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 984,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        7,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 985,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        39,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 986,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 987,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        10,
        36,
        39
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 988,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        10,
        41
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 989,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        10,
        36,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 990,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        10,
        36
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 991,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        12,
        36,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 992,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        10,
        12,
        38
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 993,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        12,
        16,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 994,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,0,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 995,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 996,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 997,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 998,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 999,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,0,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        39,
        41
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1000,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,0,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        10,
        41
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1001,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        10,
        36,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1002,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1003,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1004,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1005,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1006,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1007,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1008,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1009,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        38,
        44
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1010,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1011,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1012,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1013,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1014,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        13,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1015,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1016,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1017,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1018,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1019,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1020,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1021,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1022,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1023,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1024,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1025,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1026,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1027,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        36,
        41
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1028,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        31,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1029,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        13,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1030,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1031,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1032,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1033,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1034,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1035,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1036,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1037,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1038,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        13
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1039,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1040,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1041,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1042,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        31,
        41
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1043,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,0,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1044,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        18
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1045,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1046,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1047,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1048,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        12,
        31
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1049,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        20,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1050,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1051,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        21,
        44
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1052,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        8,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1053,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        21,
        44
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1054,
      "sign": "1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1055,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1056,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        21,
        44
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1057,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1058,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        20,
        21,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1059,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1060,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        44
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1061,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1062,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1063,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1064,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        8,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1065,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1066,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1067,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1068,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1069,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        8,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1070,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1071,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1072,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1073,
      "sign": "1,1,-1,-1,1,0,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        5,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1074,
      "sign": "1,1,-1,-1,1,0,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        5,
        8
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1075,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1076,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1077,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        7,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1078,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1079,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1080,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1081,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1082,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1083,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        8,
        31
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1084,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1085,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        8,
        22
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1086,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1087,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1088,
      "sign": "1,1,-1,-1,1,1,-1,-1,0,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1089,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1090,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,0,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1091,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1092,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1093,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1094,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1095,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        22
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1096,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1097,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1098,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1099,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1100,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1101,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1102,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1103,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        10,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1104,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1105,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        22,
        31
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1106,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        20,
        31
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1107,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        10,
        44
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1108,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1109,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        31,
        44
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1110,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        8,
        10,
        44
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1111,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        22,
        31
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1112,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1113,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        20,
        31
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1114,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        10,
        31
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1115,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1116,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1117,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1118,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1119,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1120,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1121,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1122,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1123,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1124,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1125,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1126,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1127,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1128,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1129,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        22,
        44
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1130,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1131,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1132,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1133,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1134,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1135,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        21,
        31
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1136,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        22,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1137,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1138,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        10,
        21,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1139,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1140,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1141,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1142,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1143,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        31,
        38
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1144,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        21,
        31
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1145,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        14,
        21,
        38
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1146,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1147,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        10,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1148,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1149,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1150,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1151,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1152,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        17,
        38
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1153,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        17
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1154,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1155,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        7,
        14,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1156,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1157,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1158,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1159,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1160,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1161,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1162,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1163,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1164,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        10,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1165,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1166,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1167,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1168,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        5,
        10
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1169,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        7,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1170,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1171,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        38,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1172,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1173,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        5,
        38
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1174,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1175,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        5,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1176,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        7,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1177,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1178,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1179,
      "sign": "1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1180,
      "sign": "1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1181,
      "sign": "1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1182,
      "sign": "1,1,-1,-1,1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1183,
      "sign": "1,1,-1,-1,1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1184,
      "sign": "1,1,-1,-1,1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1185,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1186,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1187,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1188,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        10,
        14,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1189,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1190,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        10,
        14,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1191,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1192,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1193,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1194,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1195,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1196,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1197,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1198,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        10,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1199,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        10,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1200,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1201,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        10,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1202,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        10,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1203,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        14,
        31,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1204,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1205,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1206,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        14,
        31,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1207,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        14,
        31,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1208,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        5,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1209,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        14,
        31,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1210,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1211,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1212,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,0,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1213,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1214,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1215,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1216,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1217,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        14,
        31,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1218,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        5,
        32,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1219,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1220,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1221,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1222,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1223,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        25
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1224,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        7,
        15
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1225,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        7
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1226,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        25
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1227,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 2,
      "factors": [
        7,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1228,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1229,
      "sign": "1,1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4
      ],
      "cost": 3,
      "factors": [
        2,
        3,
        7
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1230,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        38
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1231,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1232,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        15,
        38
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1233,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        38
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1234,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        25,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1235,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        29
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1236,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1237,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        29,
        38
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1238,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        15,
        29,
        38
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1239,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1240,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        30,
        38
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1241,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        25,
        30,
        36
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1242,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1243,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        25,
        30,
        36
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1244,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        30,
        38
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1245,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        30,
        36
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1246,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1247,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        30,
        36
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1248,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1249,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1250,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1251,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        38,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1252,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        15,
        29,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1253,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1254,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,0,1,1,-1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1255,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,0,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        38,
        42
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1256,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1257,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,0,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1258,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1259,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,0,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        38
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1260,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        15,
        38,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1261,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1262,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        30,
        42
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1263,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1264,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1265,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        38
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1266,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,0,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        38,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1267,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        38,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1268,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        10,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1269,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        36,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1270,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,0,0,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        36,
        38
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1271,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        12,
        36,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1272,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1273,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 3,
      "factors": [
        12,
        38,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1274,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 3,
      "factors": [
        12,
        38,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1275,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        12,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1276,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 3,
      "factors": [
        18,
        38,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1277,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        12,
        16,
        38
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1278,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,0,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,0,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        16,
        38
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1279,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1280,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 3,
      "factors": [
        18,
        38,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1281,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1282,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 3,
      "factors": [
        18,
        38,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1283,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        16384
      ],
      "cost": 2,
      "factors": [
        3,
        18
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1284,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        18,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1285,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,0,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1286,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        18,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1287,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        13,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1288,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,0,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        16,
        44
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1289,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,0,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1290,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        31
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1291,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        17
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1292,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1293,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1294,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        31
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1295,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        17
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1296,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1297,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1298,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        25
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1299,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        16
      ],
      "cost": 3,
      "factors": [
        2,
        8,
        25
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1300,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1301,
      "sign": "1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        25
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1302,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 10
    },
    {
      "fiber": 1303,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1304,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1305,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1306,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        29,
        41
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1307,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1308,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        29,
        41
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1309,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        36
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1310,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 9
    },
    {
      "fiber": 1311,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        41
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1312,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        15,
        25,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1313,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        36
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1314,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,0,1,-1,1,1,-1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        30,
        36
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1315,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        30,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1316,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        36
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1317,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1318,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1319,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,0,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        30,
        36
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1320,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1321,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,0,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1322,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        30,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1323,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        30,
        42
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1324,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        44
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1325,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        44
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1326,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1327,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1328,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        36
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1329,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        12,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1330,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        12,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1331,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1332,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1333,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        39,
        44
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1334,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        12,
        44
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1335,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        44
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1336,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        44
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1337,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        12,
        44
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1338,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1339,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1340,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        7,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1341,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,0,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        13,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1342,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1343,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1344,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1345,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        16,
        20
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1346,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1347,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1348,
      "sign": "1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        5,
        10,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1349,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        5,
        16
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1350,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1351,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1352,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1353,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        21,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1354,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1355,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        5,
        31
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1356,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1357,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1358,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        21,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1359,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        569,
        8
      ],
      "cost": 2,
      "factors": [
        16,
        21
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1360,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        14,
        16,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1361,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        5,
        14,
        31
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1362,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        14,
        31,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1363,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        14,
        31,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1364,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        34,
        46
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1365,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        5,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1366,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        25
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1367,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        29
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1368,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        29,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1369,
      "sign": "1,1,0,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        29,
        36
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1370,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,0,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        41
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1371,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        25,
        41
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1372,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,0,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        25
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1373,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,0,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1374,
      "sign": "1,1,0,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,0,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        36
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1375,
      "sign": "1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        25,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1376,
      "sign": "1,1,0,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        7,
        44
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1377,
      "sign": "1,1,1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        4
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1378,
      "sign": "1,1,1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,0,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        4
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1379,
      "sign": "1,1,1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        4
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1380,
      "sign": "1,1,0,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        4
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1381,
      "sign": "1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1382,
      "sign": "1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,0,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        36
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1383,
      "sign": "1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        44
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1384,
      "sign": "1,1,0,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1385,
      "sign": "1,1,0,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,0,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        44
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1386,
      "sign": "1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,0,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        44
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1387,
      "sign": "1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        5,
        44
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1388,
      "sign": "1,1,0,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        5,
        44
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1389,
      "sign": "1,1,0,1,-1,0,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,0,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1390,
      "sign": "1,1,1,1,-1,0,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        5
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1391,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        5,
        12
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1392,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,0,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        42
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1393,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        5,
        12
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1394,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        5,
        12
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1395,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        12
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1396,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        12
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1397,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        5,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1398,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        5,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1399,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        2,
        18
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1400,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        5,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1401,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        34
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1402,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        34
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1403,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1404,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1405,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        5,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1406,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        5,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1407,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        34
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1408,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1409,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        34
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1410,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        34
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1411,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        13
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1412,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1413,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        20
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1414,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        20
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1415,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        20
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1416,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        20
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1417,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1418,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1419,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1420,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1421,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1422,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1423,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1424,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1425,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1426,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1427,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1428,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        37
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1429,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1430,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1431,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,0,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        37
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1432,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,0,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        37
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1433,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        22,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1434,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        22,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1435,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        37
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1436,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        37
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1437,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        22,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1438,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        22,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1439,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,0,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        15,
        36
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1440,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        15,
        25,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1441,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,0,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        15,
        36
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1442,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 3,
      "factors": [
        7,
        15,
        42
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1443,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        30,
        44
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1444,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        44
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1445,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        42
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1446,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        42
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1447,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1448,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        12
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1449,
      "sign": "1,1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        12
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1450,
      "sign": "1,1,-1,0,1,0,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1451,
      "sign": "1,1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1452,
      "sign": "1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1453,
      "sign": "1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1454,
      "sign": "1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1455,
      "sign": "1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1456,
      "sign": "1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1457,
      "sign": "1,1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1458,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        13
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1459,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1460,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        16
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1461,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1462,
      "sign": "1,1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1463,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        13
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1464,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        13
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1465,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1466,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1467,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1468,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 3,
      "factors": [
        5,
        16,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1469,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        2048
      ],
      "cost": 2,
      "factors": [
        16,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1470,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1471,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1472,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1473,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        16,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1474,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        16,
        21
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1475,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1476,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        34
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1477,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1478,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1479,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1480,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        4,
        17,
        31
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1481,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1482,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        31
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1483,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,0,1,0,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1484,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,0,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 2,
      "factors": [
        15,
        44
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1485,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        42,
        44
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1486,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,0,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1487,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1488,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        42
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1489,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1490,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1491,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        12
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1492,
      "sign": "1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        12,
        30
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1493,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,0,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        44
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1494,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1495,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        42,
        44
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1496,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,0,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1497,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1498,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        15
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1499,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1500,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        5,
        15
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1501,
      "sign": "1,1,-1,1,0,0,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1502,
      "sign": "1,1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        12
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1503,
      "sign": "1,1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1504,
      "sign": "1,1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        4,
        18
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1505,
      "sign": "1,1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1506,
      "sign": "1,1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        4,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1507,
      "sign": "1,1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        5
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1508,
      "sign": "1,1,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        3,
        4
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1509,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1",
      "label": [
        693,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        44
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1510,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,0,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 2,
      "factors": [
        4,
        44
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1511,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1",
      "label": [
        689,
        4096
      ],
      "cost": 3,
      "factors": [
        2,
        42,
        44
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1512,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,0,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        42
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1513,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        12,
        42
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1514,
      "sign": "1,1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1515,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        5,
        15
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1516,
      "sign": "1,1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1517,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        5,
        15
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1518,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1519,
      "sign": "1,1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1520,
      "sign": "1,1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1521,
      "sign": "1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        3,
        5,
        12
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1522,
      "sign": "1,1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        5
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1523,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        5,
        12
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1524,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        5,
        12
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1525,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        5,
        12
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1526,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1527,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        15,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1528,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1529,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1530,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1531,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1532,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1533,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1534,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        13,
        15
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1535,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        13,
        15
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1536,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        128
      ],
      "cost": 2,
      "factors": [
        13,
        15
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1537,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        34
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1538,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1539,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        34
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1540,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        20,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1541,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1542,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1543,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        3,
        12
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1544,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        5,
        15,
        34
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1545,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        15
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1546,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        15,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1547,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1548,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        21
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1549,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        15,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1550,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        18,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1551,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        15,
        30
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1552,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        30
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1553,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        15,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1554,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        15,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1555,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        34
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1556,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        21,
        39
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1557,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1558,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1559,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        34
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1560,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1561,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1562,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1563,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        4,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1564,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        16,
        34
      ],
      "minimalConstraints": 8
    },
    {
      "fiber": 1565,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        4,
        34
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1566,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1567,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        34
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1568,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        16,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1569,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1570,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        4,
        16
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1571,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        16,
        21
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1572,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        16
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1573,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1574,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1575,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1576,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        4,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1577,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1578,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        4,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1579,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1580,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        4,
        17,
        31
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1581,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 2,
      "factors": [
        4,
        31
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1582,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        31,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1583,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1584,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1585,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        32,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1586,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1587,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1588,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1589,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        16,
        22,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1590,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        22,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1591,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        16,
        22,
        37
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1592,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        16
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1593,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        14,
        16
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1594,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1595,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        20
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1596,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1597,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1598,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        22,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1599,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1600,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1601,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1602,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1603,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1604,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        21,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1605,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1606,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        21
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1607,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        17
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1608,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1609,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        17,
        31,
        37
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1610,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        4,
        31,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1611,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        31,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1612,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        31,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1613,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        633,
        256
      ],
      "cost": 3,
      "factors": [
        4,
        32,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1614,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1615,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1616,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 2,
      "factors": [
        15,
        18
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1617,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,0,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        5,
        15,
        34
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1618,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        5,
        15,
        34
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1619,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        4096
      ],
      "cost": 3,
      "factors": [
        4,
        13,
        15
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1620,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        34
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1621,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        34
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1622,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,0,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        15
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1623,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        13,
        15
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1624,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        30
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1625,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1626,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        20
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1627,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        20
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1628,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        20,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1629,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1630,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        15,
        20,
        34
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1631,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        15,
        20
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1632,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        34,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1633,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,0,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        13,
        34
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1634,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1635,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        21,
        39
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1636,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1637,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        21,
        39
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1638,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        21
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1639,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1640,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1641,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1642,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1643,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1644,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        20
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1645,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        20
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1646,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1647,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1648,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1649,
      "sign": "1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1650,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1651,
      "sign": "1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        4,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1652,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1653,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1654,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1655,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        22,
        37
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1656,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        22
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1657,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1658,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1659,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1660,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        4,
        16,
        17
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1661,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        31,
        37
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1662,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        32,
        37
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1663,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1664,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        31,
        32
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1665,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        32,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1666,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        46
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1667,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        31,
        46
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1668,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1669,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        16,
        17
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1670,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        16,
        37
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1671,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        17
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1672,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        4,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1673,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        17,
        35
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1674,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        17,
        32
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1675,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        20,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1676,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        20,
        30
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1677,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        30
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1678,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        13,
        30
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1679,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1680,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        21
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1681,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1682,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 3,
      "factors": [
        13,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1683,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        37
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1684,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        37
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1685,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        37
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1686,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        37
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1687,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        37
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1688,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        37
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1689,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1690,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1691,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 2,
      "factors": [
        22,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1692,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        561,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1693,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        22,
        37
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1694,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        22,
        37
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1695,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1696,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1697,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        49,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        37
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1698,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        22,
        37
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1699,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1700,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1701,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1702,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1703,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1704,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1705,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1706,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        37,
        39
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1707,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,0,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        37
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1708,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        37
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1709,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        37
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1710,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        14,
        15
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1711,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        17
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1712,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        14,
        17
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1713,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1714,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1715,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1716,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        31,
        35
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1717,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        31,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1718,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1719,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1720,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        22
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1721,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        14,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1722,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        14,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1723,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1724,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 2,
      "factors": [
        3,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1725,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8
      ],
      "cost": 3,
      "factors": [
        3,
        15,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1726,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        17,
        35
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1727,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        17,
        35
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1728,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        32
      ],
      "minimalConstraints": 7
    },
    {
      "fiber": 1729,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        32,
        35
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1730,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        17,
        35
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1731,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        633,
        8192
      ],
      "cost": 3,
      "factors": [
        16,
        17,
        35
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1732,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        39
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1733,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        14,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1734,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        14,
        22
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1735,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        14,
        15
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1736,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        14,
        15
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1737,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        35
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1738,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        14,
        15,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1739,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        35
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1740,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        16,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1741,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        35,
        46
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1742,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        46
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1743,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1744,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        35
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1745,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        14
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1746,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        14
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1747,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        14,
        35
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1748,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 3,
      "factors": [
        2,
        14,
        35
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1749,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1750,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        14
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1751,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        14,
        39
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1752,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,0,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        39
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1753,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1754,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        2,
        35,
        40
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1755,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        2,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1756,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        2,
        17,
        35
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1757,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1758,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1759,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1760,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        17,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1761,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        17,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1762,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        2,
        17,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1763,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        32,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1764,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        2,
        35,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1765,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        2,
        35,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1766,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1767,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1768,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        32,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1769,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1770,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        16,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1771,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        32,
        35
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1772,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        16,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1773,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        32,
        35
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1774,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        3,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1775,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        3,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1776,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        35,
        40
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1777,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        32,
        35
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1778,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        15,
        17
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1779,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,0,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        1024
      ],
      "cost": 2,
      "factors": [
        3,
        35
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1780,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        35,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1781,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        2,
        15,
        17
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1782,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        15,
        17,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1783,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        15,
        17,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1784,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1785,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        32,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1786,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        35,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1787,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1",
      "label": [
        121,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        35,
        40
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1788,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1789,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1790,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        32,
        40
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1791,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        32,
        40
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1792,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        15,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1793,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        15,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1794,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 3,
      "factors": [
        15,
        40,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1795,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 3,
      "factors": [
        15,
        40,
        43
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1796,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1797,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1798,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        32,
        40
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1799,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        32,
        40
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1800,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        40
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1801,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 3,
      "factors": [
        15,
        40,
        46
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1802,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        40
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1803,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        46
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1804,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        3,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1805,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        3,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1806,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        16,
        40
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1807,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1808,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        43
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1809,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        43
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1810,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        40
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1811,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        35
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1812,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        43
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1813,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        35
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1814,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        3,
        31,
        40
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1815,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        31,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1816,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        43
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1817,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        31,
        43
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1818,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1819,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1820,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1821,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1822,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1823,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1824,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1825,
      "sign": "1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        256
      ],
      "cost": 2,
      "factors": [
        31,
        32
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1826,
      "sign": "0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        2
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1827,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        32
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1828,
      "sign": "1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        2,
        40
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1829,
      "sign": "1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        2,
        40
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1830,
      "sign": "0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        2
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1831,
      "sign": "0,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        2
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1832,
      "sign": "0,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        2
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1833,
      "sign": "0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1834,
      "sign": "0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1835,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        43
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1836,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        43
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1837,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        43,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1838,
      "sign": "0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1839,
      "sign": "0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        43,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1840,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1841,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        3,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1842,
      "sign": "0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        15
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1843,
      "sign": "0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1844,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        3,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1845,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1846,
      "sign": "1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        3,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1847,
      "sign": "0,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        15
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1848,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        43
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1849,
      "sign": "0,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        3
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1850,
      "sign": "1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        3,
        43
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1851,
      "sign": "0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        3
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1852,
      "sign": "0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1853,
      "sign": "1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 1
    },
    {
      "fiber": 1854,
      "sign": "1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        1
      ],
      "cost": 2,
      "factors": [
        0,
        1
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1855,
      "sign": "0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        1
      ],
      "cost": 2,
      "factors": [
        0,
        1
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1856,
      "sign": "-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        32
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1857,
      "sign": "-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        32
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1858,
      "sign": "-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1859,
      "sign": "-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1860,
      "sign": "-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        43,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1861,
      "sign": "-1,0,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1862,
      "sign": "-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1863,
      "sign": "-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1864,
      "sign": "-1,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        43,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1865,
      "sign": "-1,0,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1866,
      "sign": "-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1",
      "label": [
        89,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1867,
      "sign": "-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        43
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1868,
      "sign": "-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        43,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1869,
      "sign": "-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        46
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1870,
      "sign": "-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        43
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1871,
      "sign": "-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        15
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1872,
      "sign": "-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1873,
      "sign": "-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1874,
      "sign": "-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        15
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1875,
      "sign": "-1,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1876,
      "sign": "-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        3
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1877,
      "sign": "-1,0,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1878,
      "sign": "-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        1,
        3
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1879,
      "sign": "-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 1,
      "factors": [
        1
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1880,
      "sign": "-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        1,
        46
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1881,
      "sign": "-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        0,
        46
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1882,
      "sign": "-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        2,
        33
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1883,
      "sign": "-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        33
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1884,
      "sign": "-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1885,
      "sign": "-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1886,
      "sign": "-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1887,
      "sign": "-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        2,
        33
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1888,
      "sign": "-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        33
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1889,
      "sign": "-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1890,
      "sign": "-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1891,
      "sign": "-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        2,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1892,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        3,
        33
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1893,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        15,
        33
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1894,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        33
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1895,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        33
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1896,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1897,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1898,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1899,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1900,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1901,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1902,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        3,
        33
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1903,
      "sign": "-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        3,
        33
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1904,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        33
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1905,
      "sign": "-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        33
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1906,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1907,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1908,
      "sign": "-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1909,
      "sign": "-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1910,
      "sign": "-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1911,
      "sign": "-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        3,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1912,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        1,
        16,
        33
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1913,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        33
      ],
      "minimalConstraints": 6
    },
    {
      "fiber": 1914,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 5
    },
    {
      "fiber": 1915,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1916,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        45
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1917,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        8192
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        33
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1918,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        33
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1919,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        8192
      ],
      "cost": 2,
      "factors": [
        16,
        33
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1920,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1",
      "label": [
        72,
        512
      ],
      "cost": 3,
      "factors": [
        0,
        16,
        33
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1921,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1",
      "label": [
        72,
        512
      ],
      "cost": 2,
      "factors": [
        16,
        45
      ],
      "minimalConstraints": 4
    },
    {
      "fiber": 1922,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        72,
        512
      ],
      "cost": 2,
      "factors": [
        33,
        45
      ],
      "minimalConstraints": 3
    },
    {
      "fiber": 1923,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        512
      ],
      "cost": 2,
      "factors": [
        16,
        33
      ],
      "minimalConstraints": 2
    },
    {
      "fiber": 1924,
      "sign": "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",
      "label": [
        64,
        512
      ],
      "cost": 2,
      "factors": [
        16,
        33
      ],
      "minimalConstraints": 2
    }
  ]
}
```

## Reproduction (JavaScript function body)

```javascript
function audit(tree){
const R="187,12,-1;204,11,-1;5,-2,0;9,-1,0;85,7,-2;51,2,-1;0,1,-1;34,1,-1;187,20,-9;68,1,-3;176,22,-9;22,0,-1;61,0,-1;74,0,-1;126,0,-1;4,-1,0;17,-1,0;156,-1,-1;69,0,-1;9,0,-1;235,0,-3;87,0,-1;104,-1,-1;38,0,-3;5,0,-2;39,-1,-1;40,0,-3;26,-1,-1;25,0,-3;83,0,-2;102,-7,-1;204,-11,1;395,0,-2;289,18,-1;66,2,-1;132,5,-1;44,1,-1;88,3,-1;88,7,-3;132,-7,-1;153,8,-1;153,5,-4;117,-2,-2;198,8,-1;198,5,-4;306,17,-1;234,-1,-1".split(";").map(s=>s.split(",").map(BigInt));
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],T=[[0,1],[0,2],[0,3],[1,3],[1,6],[2,3],[2,6],[2,7],[2,11],[2,12],[3,2],[3,3],[4,6],[4,12],[5,7]],E=[[17n,1n,0n],[39n,0n,0n],[17n,0n,1n],[22n,1n,0n],[0n,1n,1n],[22n,0n,1n]];
function gaps(v){let [x,y,z]=v,h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]].map(([i,j])=>BigInt(Math.abs(h[i]-h[j])))}
const G=V.map(gaps),W=[0,3,5,6,7,9],D=[];
for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){let v=[x,y,z];if((v.find(a=>a!==0)||0)>0&&v.reduce((s,a)=>s+Math.max(a,0),0)<=10&&v.reduce((s,a)=>s+Math.max(-a,0),0)<=10)D.push([v,gaps(v)])}
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t}return a}
function norm(a,unoriented=false){let d=gcd(gcd(a[0],a[1]),a[2]);if(!d)return a;a=a.map(x=>x/d);if(unoriented&&a.find(x=>x!==0n)<0n)a=a.map(x=>-x);return a}
let raw=new Map();function addLine(a){a=norm(a,true);if(a.some(x=>x>0n)&&a.some(x=>x<0n))raw.set(a.join(),a)}
for(let i=0;i<T.length;i++){let [j,g]=T[i];for(let k=i+1;k<T.length;k++){let [h,f]=T[k];addLine(E[h].map((x,s)=>BigInt(g)*x-BigInt(f)*E[j][s]))}for(let gg of G)for(let h=0;h<6;h++)if(gg[h])addLine(E[h].map((x,s)=>3n*BigInt(g)*x-2n*gg[h]*E[j][s]))}
let L=[...raw.values()];for(let r of R)if(!raw.has(norm(r,true).join()))throw Error("support absent");
let cells=[[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]];
for(let l of L){let next=[];for(let cell of cells){let sig=cell.map(x=>dot(l,x));if(!sig.some(x=>x>0n)||!sig.some(x=>x<0n)){next.push(cell);continue}for(let side of [1n,-1n]){let out=[];for(let i=0;i<cell.length;i++){let j=(i+1)%cell.length,a=sig[i],b=sig[j];if(a*side>=0n)out.push(cell[i]);if(a*b<0n){let r=cross(cross(cell[i],cell[j]),l);if(r.some(x=>x<0n))r=r.map(x=>-x);if(r.some(x=>x<0n)||!r.some(x=>x>0n)||dot(r,l)!==0n)throw Error("bad intersection");out.push(norm(r))}}next.push(out)}}cells=next}
const pts=new Map();function put(a){if(a.every(x=>x>0n)){a=norm(a);pts.set(a.join(),a)}}function sum(a){return [0,1,2].map(i=>a.reduce((s,x)=>s+x[i],0n))}
for(let c of cells){put(sum(c));for(let i=0;i<c.length;i++){put(c[i]);put(sum([c[i],c[(i+1)%c.length]]))}}

const patterns=new Map(), sign=p=>R.map(r=>{let x=dot(r,p);return x>0n?1:x<0n?-1:0});
for(const p of pts.values()){let s=sign(p),k=s.join();if(!patterns.has(k))patterns.set(k,s)}
const A=[...patterns.values()],N=A.length,all=(1n<<BigInt(N))-1n;
let pos=R.map(()=>0n),neg=R.map(()=>0n);
A.forEach((s,i)=>s.forEach((x,j)=>{if(x>0)pos[j]|=1n<<BigInt(i);if(x<0)neg[j]|=1n<<BigInt(i)}));
const mask=([i,j,sg])=>j<0?(sg>0?pos[i]:neg[i]):sg>0?((pos[i]&pos[j])|(neg[i]&neg[j])):((pos[i]&neg[j])|(neg[i]&pos[j]));
const qs=[];for(let i=0;i<R.length;i++){for(let s of [1,-1])qs.push([i,-1,s]);for(let j=i;j<R.length;j++)for(let s of [1,-1])if(i!==j||s===1)qs.push([i,j,s])}
const Q=qs.map(q=>({q,b:mask(q)}));
const count=b=>{let n=0;while(b){b&=b-1n;n++}return n};
const factors=q=>q[1]<0||q[0]===q[1]?[q[0]]:[q[0],q[1]];

const ix=new Map(A.map((s,i)=>[s.join(),i]));
const labels=new Map(), fibers=Array(N).fill(null);
const max=a=>a.reduce((x,y)=>x>y?x:y),min=a=>a.reduce((x,y)=>x<y?x:y);
for(const p of pts.values()){
 const c=E.map(e=>dot(e,p)),pr=c.reduce((a,b)=>a*b,1n),scale=c.map(x=>pr/x),scores=G.map(g=>max(g.map((a,i)=>a*scale[i]))),eta=min(W.map(i=>scores[i]));
 let n=0,m=0;for(let i=0;i<scores.length;i++)if(2n*scores[i]<3n*eta)n|=1<<i;
 for(let i=0;i<T.length;i++){let [j,g]=T[i];if(BigInt(g)*scale[j]===eta)m|=1<<i}
 const i=ix.get(sign(p).join()),f=fibers[i];if(!f)fibers[i]=[n,m];else{if(f[0]!==n)throw Error("near fiber mismatch");f[1]&=m;if(!f[1])throw Error("empty intersection")}
}
function gather(t){if(t.out){labels.set(t.out.join(),t.out);return}gather(t.yes);gather(t.no)}gather(tree);
const lab=[...labels.values()],covers=lab.map(()=>0n),groups=new Map(),single=lab.map(()=>0n);
for(let i=0;i<N;i++){let [n,m]=fibers[i],b=1n<<BigInt(i),hits=[];for(let j=0;j<lab.length;j++)if(lab[j][0]===n&&(lab[j][1]&m)){covers[j]|=b;hits.push(j)}if(!hits.length)throw Error("uncovered");if(hits.length===1)single[hits[0]]|=b;groups.set(n,(groups.get(n)||0n)|b)}
const groupList=[...groups].map(([n,b])=>({b,s:lab.map((l,j)=>l[0]===n?single[j]:0n).filter(Boolean)}));
function weakBound(S,lim=1e9){let n=0;for(let g of groupList)if(g.b&S){let z=0;for(let b of g.s)if(b&S)z++;n+=Math.max(1,z);if(n>lim)return n}return n}

const exactGroups=[...groups].map(([n,b])=>{
 const cs=lab.map((l,i)=>l[0]===n?covers[i]:0n).filter(Boolean),opts=[];
 for(let m=1;m<(1<<cs.length);m++){let v=0n,k=0;for(let j=0;j<cs.length;j++)if(m&(1<<j)){v|=cs[j];k++}opts.push({v,k})}
 opts.sort((a,b)=>a.k-b.k);return {b,opts}
});
let boundCalls=0,strictGains=0,maximumGain=0;
function bound(S,lim=1e9){boundCalls++;let n=0;for(let g of exactGroups){let x=S&g.b;if(!x)continue;let z=g.opts.find(o=>(x&o.v)===x);if(!z)throw Error("coverage missing");n+=z.k;if(n>lim)return n}return n}
function leaf(S){for(let i=0;i<covers.length;i++)if((S&covers[i])===S)return {out:lab[i]};return null}
Q.sort((a,b)=>Number(a.q[1]>=0)-Number(b.q[1]>=0));
let visited=0, scans=0, cut=0, cap=1000, memo=new Map();
const stop={};
function solve(S,d,k){
 let l=leaf(S);if(l)return l;if(!d||bound(S,1<<d)>(1<<d))return null;
 k=Math.min(k,d);const key=S.toString(36)+"/"+d+"/"+k;if(memo.has(key))return memo.get(key);
 if(++visited>cap)throw stop;
 let seen=new Set(),candidates=[],lim=1<<(d-1);
 for(let c of Q){if(c.q[1]>=0&&!k)continue;let y=c.b&S,z=S^y;if(!y||!z)continue;let part=y<z?y:z;if(seen.has(part))continue;seen.add(part);scans++;
 let a=bound(y,lim),b=bound(z,lim);if(a>lim||b>lim)continue;
 if(d===1){let yy=leaf(y),zz=leaf(z);if(yy&&zz){let t={q:c.q,yes:yy,no:zz};memo.set(key,t);return t}continue}
 candidates.push({q:c.q,y,z,a,b,score:Math.max(a,b)*100+(a+b)*3+Number(c.q[1]>=0)*2});
 }
 candidates.sort((a,b)=>a.score-b.score);
 for(let c of candidates){let k1=k-Number(c.q[1]>=0);let yy,zz;if(c.a>=c.b){yy=solve(c.y,d-1,k1);if(!yy)continue;zz=solve(c.z,d-1,k1)}else{zz=solve(c.z,d-1,k1);if(!zz)continue;yy=solve(c.y,d-1,k1)}if(yy&&zz){let t={q:c.q,yes:yy,no:zz};memo.set(key,t);return t}}
 memo.set(key,null);return null
}
function maxq(t){return t.out?0:Number(t.q[1]>=0)+Math.max(maxq(t.yes),maxq(t.no))}
function nodes(t){if(t.out)return [0,0,1];let a=nodes(t.yes),b=nodes(t.no);return [1+a[0]+b[0],Number(t.q[1]>=0)+a[1]+b[1],a[2]+b[2]]}
const logs=[];
function trial(S,d,k,path){
 let start=visited,sc0=scans;cap=visited+(d===6?18000:d>=4?10000:500);let ans=null,status;
 try{ans=solve(S,d,k);status=ans?"FOUND":"EXHAUSTED"}catch(e){if(e!==stop)throw e;status="BUDGET";cut++}
 logs.push({path,d,target:k,status,states:visited-start,scans:scans-sc0});return ans
}
function improve(t,S,d,path,ceiling){
 if(t.out)return t;
 let y=mask(t.q)&S,z=S^y;
 t={q:t.q,yes:improve(t.yes,y,d-1,path+"Y",ceiling),no:improve(t.no,z,d-1,path+"N",ceiling)};
 if(d>ceiling||d<1)return t;
 let b=maxq(t);
 while(b>0){let ans=trial(S,d,b-1,path);if(!ans)break;t=ans;b=maxq(t)}
 return t;
}
function verify(t){let h={},depth={},joint=0,outputs=new Set(),maxDistinct=0;for(let i=0;i<N;i++){let x=t,d=0,k=0,f=new Set();while(x.q){let [a,b,s]=x.q;d++;k+=Number(b>=0);f.add(a);if(b>=0)f.add(b);x=s*A[i][a]*(b<0?1:A[i][b])>0?x.yes:x.no}let [nm,mm]=fibers[i];if(x.out[0]!==nm||!(x.out[1]&mm))throw Error("bad output");if(d>6)throw Error("depth");outputs.add(x.out.join());maxDistinct=Math.max(maxDistinct,f.size);h[k]=(h[k]||0)+1;depth[d]=(depth[d]||0)+1;joint+=k}return {hist:h,depth,n:N,maxq:maxq(t),nodes:nodes(t),outputs:outputs.size,maxDistinct,joint}}


const enc=A.map(s=>{let p=0n,n=0n;for(let j=0;j<s.length;j++){if(s[j]>0)p|=1n<<BigInt(j);if(s[j]<0)n|=1n<<BigInt(j)}return [p,n]});
const pop=x=>{let n=0;while(x){x&=x-1n;n++}return n};
let hitCalls=0,rawDiffs=0,minimalDiffs=0,certs=[],hist={},maxCert=0,examples=[];
function hit(D,k){
 hitCalls++;if(!D.length)return 0n;if(k===0)return null;
 let pack=0n,lb=0;for(let x of D)if(!(pack&x)){pack|=x;if(++lb>k)return null}
 let best=D[0],options=[];
 for(let a=best;a;){let bit=a&-a;a^=bit;let rest=D.filter(x=>!(x&bit));options.push({bit,rest})}
 options.sort((a,b)=>a.rest.length-b.rest.length);
 for(let o of options){let q=hit(o.rest,k-1);if(q!==null)return q|o.bit}
 return null
}
for(let i=0;i<N;i++){
 const f=1n<<BigInt(i),[p,n]=enc[i],candidate=[];
 const diffs=enc.map(([q,m],j)=>({j,d:(p^q)|(n^m)})).filter(x=>x.d!==0n).map(x=>({...x,k:pop(x.d)})).sort((a,b)=>a.k-b.k);
 for(let a=0;a<lab.length;a++)if(covers[a]&f){
 let D=[];for(let x of diffs){if(covers[a]&(1n<<BigInt(x.j)))continue;rawDiffs++;if(!D.some(y=>(y&x.d)===y))D.push(x.d)}
 minimalDiffs+=D.length;
 let ans=null,k=0;for(;k<=8;k++){ans=hit(D,k);if(ans!==null)break}
 if(ans===null)throw Error("certificate > known tree bound");
 for(let x of diffs)if(!(covers[a]&(1n<<BigInt(x.j)))&&!(ans&x.d))throw Error("invalid certificate");
 candidate.push({label:lab[a],cost:pop(ans),factors:[...Array(R.length).keys()].filter(j=>ans&(1n<<BigInt(j))),minimalConstraints:D.length})
 }
 candidate.sort((a,b)=>a.cost-b.cost);let best=candidate[0];if(!best)throw Error("no allowed label");
 hist[best.cost]=(hist[best.cost]||0)+1;certs.push({fiber:i,sign:A[i].join(),...best});
 if(best.cost>maxCert){maxCert=best.cost;examples=[]}if(best.cost===maxCert&&examples.length<8)examples.push({fiber:i,sign:A[i].join(),...best,allLegal:candidate});
}
return {rawLines:L.length,cells:cells.length,positiveRepresentatives:pts.size,patterns:N,labels:lab.length,rawDiffs,minimalDiffs,hitCalls,hist,maxCert,examples,certs};
}
return audit({"q":[12,-1,1],"yes":{"q":[19,29,-1],"yes":{"q":[2,-1,1],"yes":{"q":[7,9,-1],"yes":{"q":[8,-1,-1],"yes":{"out":[951,4]},"no":{"q":[10,-1,-1],"yes":{"out":[695,4]},"no":{"out":[693,4]}}},"no":{"q":[9,25,-1],"yes":{"q":[41,-1,1],"yes":{"out":[951,4096]},"no":{"out":[693,4096]}},"no":{"q":[7,-1,1],"yes":{"out":[132,4]},"no":{"out":[693,4096]}}}},"no":{"q":[11,27,1],"yes":{"q":[25,-1,1],"yes":{"q":[11,-1,1],"yes":{"out":[132,16]},"no":{"out":[693,16]}},"no":{"q":[16,-1,1],"yes":{"out":[693,4096]},"no":{"out":[693,64]}}},"no":{"q":[23,27,1],"yes":{"q":[26,-1,-1],"yes":{"out":[693,16]},"no":{"out":[692,16]}},"no":{"q":[27,-1,-1],"yes":{"out":[676,16]},"no":{"out":[132,16]}}}}},"no":{"q":[11,-1,1],"yes":{"q":[2,-1,1],"yes":{"q":[6,-1,1],"yes":{"out":[132,32]},"no":{"out":[132,4]}},"no":{"q":[28,-1,1],"yes":{"q":[24,-1,1],"yes":{"out":[132,32]},"no":{"out":[132,16]}},"no":{"q":[27,28,1],"yes":{"out":[164,16]},"no":{"out":[132,16]}}}},"no":{"q":[16,42,1],"yes":{"q":[44,-1,1],"yes":{"q":[16,-1,1],"yes":{"out":[693,4096]},"no":{"out":[561,64]}},"no":{"q":[5,-1,1],"yes":{"out":[689,4096]},"no":{"out":[561,4096]}}},"no":{"q":[38,-1,1],"yes":{"q":[36,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,2048]}},"no":{"q":[39,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,16384]}}}}}},"no":{"q":[14,-1,1],"yes":{"q":[3,-1,1],"yes":{"q":[4,15,1],"yes":{"q":[13,-1,1],"yes":{"q":[30,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,128]}},"no":{"q":[22,-1,-1],"yes":{"out":[633,8]},"no":{"out":[561,8]}}},"no":{"q":[34,-1,1],"yes":{"q":[5,15,1],"yes":{"out":[561,2]},"no":{"out":[561,4096]}},"no":{"q":[37,-1,-1],"yes":{"out":[121,1024]},"no":{"out":[49,1024]}}}},"no":{"q":[18,-1,1],"yes":{"q":[38,-1,1],"yes":{"q":[16,-1,1],"yes":{"out":[561,2048]},"no":{"out":[561,8]}},"no":{"q":[39,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,16384]}}},"no":{"q":[21,22,1],"yes":{"q":[21,-1,1],"yes":{"out":[561,8]},"no":{"out":[633,8]}},"no":{"q":[20,22,1],"yes":{"out":[569,8]},"no":{"out":[561,8]}}}}},"no":{"q":[1,31,1],"yes":{"q":[35,-1,1],"yes":{"q":[17,-1,1],"yes":{"q":[15,-1,-1],"yes":{"out":[633,8]},"no":{"out":[121,1024]}},"no":{"q":[46,-1,1],"yes":{"out":[633,8192]},"no":{"out":[72,8192]}}},"no":{"q":[40,46,1],"yes":{"q":[40,-1,1],"yes":{"out":[121,8192]},"no":{"out":[72,8192]}},"no":{"q":[43,46,1],"yes":{"out":[89,8192]},"no":{"out":[72,8192]}}}},"no":{"q":[0,-1,1],"yes":{"q":[1,-1,1],"yes":{"q":[32,-1,1],"yes":{"out":[633,256]},"no":{"out":[72,256]}},"no":{"out":[72,1]}},"no":{"q":[16,-1,1],"yes":{"q":[45,-1,1],"yes":{"out":[72,8192]},"no":{"out":[64,8192]}},"no":{"q":[33,-1,1],"yes":{"out":[72,512]},"no":{"out":[64,512]}}}}}}});

```

## Next

Compare the exact certificate lower bound with the depth-six budget-two search. A factor-count bound is necessary, not sufficient for an adaptive binary tree. Explore local state versions and stronger partition/capacity obstructions; R223 construction remains the current upper bound. Native control unchanged from R222; identity/activity association unconfirmed.
