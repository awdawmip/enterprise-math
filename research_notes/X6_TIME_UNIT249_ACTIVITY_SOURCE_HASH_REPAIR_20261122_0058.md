# X6 Unit249 — Activity source digest correction (metadata-only)

Date: 2026-11-22. Source-only correction under existing Research Activity RA-5E3FE1E761E4963EC461A892. The author-scoped Unit249 science, V8 2,145 exact assertions, 36 immutable original Unit245 BRC paths, all GitHub source files, source commits, and Git blob SHA1 values are unchanged.

The Activity event `onhour-20261122-0058-x6-original-brc-36case-precision-discriminator-unit249-v1` accidentally recorded malformed SHA256 digests beginning with 32 zero hex characters, due to a defect in the activity-side hash computation. That event's Git commits and blob SHA1 pins remain valid. The following replacement SHA256 values were computed from immutable full-file GitHub readbacks using an independently checked SHA256 implementation (standard `sha256("abc")` test verified). Preserve the original event and append a new `repairs_event_id` event; do not count this correction as Unit250 or as new mathematical research.

| File | Immutable Git commit | Correct SHA256 |
|---|---|---|
| `research_notes/X6_TIME_UNIT249_ORIGINAL_BRC_PRECISION_LAW_DISCRIMINATOR_20261122.md` | `4bdbcb463093b3eed9528f447c91d94dbbbfd5c9` | `9a3386b2b9259e99fc97c4ab83c3ecc4bb7a83107c6683459fe73efef8b079c0` |
| `research_checks/X6_TIME_UNIT249_ORIGINAL_BRC_PRECISION_LAW_REPLAY_CHECK_20261122.js` | `4ee6d7a4156dfdf349a8ee2fa15d1f2fb476f409` | `dcfc4ffa0bd066250722e9e5f647f3347e413555e84e1fd93228749f1e42f29c` |
| `research_checks/X6_TIME_UNIT249_ORIGINAL_BRC_PRECISION_LAW_REPLAY_RESULTS_20261122.json` | `c0116bf2ee4970493fcb6e7c55da4692202c4547` | `6610abb5690faa6dc8201c0b0f98d9de0aa453057a36db5958d898995d812ed0` |

This is only a metadata correction. Native task execution authorization, formal semantic PROGRESS, physical Source-admitted signed Port/sensor, reviewer acceptance and other tasks remain in their existing states.
