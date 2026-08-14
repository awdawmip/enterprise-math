# Enterprise Math GitHub Transport Pre-Resolution

Status: `ACTIVE / TRANSPORT-ROUTING SOFT-LIVENESS RULE`
Effective: 2026-08-14
Scope: GitHub access-path classification when local shell networking and managed GitHub connector availability differ.

## Purpose

A local `git`, `gh`, or `curl` DNS failure is a failure of one transport path. It is not evidence that GitHub as a service, the repository, or an independently exposed managed GitHub connector is unavailable.

This rule prevents a local networking limitation from being misclassified as a research or task failure.

## Pre-resolved repository identities

- Enterprise Math source: `awdawmip/enterprise-math`
- Global Knowledge: `awdawmip/chatgpt-global-knowledge`

These identities are routing hints only. Current permissions and connector availability are runtime facts and must not be invented.

## Independent transport classes

Treat these as distinct capabilities:

1. `LOCAL_GIT_TRANSPORT`
   - local `git`, `gh`, `curl`, shell HTTPS/SSH, and the current worker's DNS/egress;
2. `MANAGED_GITHUB_CONNECTOR`
   - a platform-exposed authorized GitHub connector/API path, when present in the runtime.

Failure of one class does not imply failure of the other.

## Capability pre-resolution

At startup or first GitHub-relevant action, resolve capability from the runtime rather than probing the network repeatedly:

- if an authorized managed GitHub connector is exposed, record it as an available fallback path unless an actual connector call later fails;
- do not run `nslookup`, `ping`, repeated `curl`, repeated `git fetch`, or repeated `gh api` merely to prove that local DNS is working;
- use the smallest path required by the task.

This is capability pre-resolution, not DNS prefetching.

## First local DNS failure

On the first concrete local remote-access error such as:

- `Could not resolve host: github.com`;
- `Could not resolve host: api.github.com`;
- `Temporary failure in name resolution`;
- equivalent DNS/egress resolution failure;

classify:

`LOCAL_GIT_NETWORK_UNAVAILABLE / DNS_EGRESS_DEGRADED`

Then:

1. stop retrying that unchanged local transport;
2. preserve all local research, files, tests, commits, and artifacts already completed;
3. if `MANAGED_GITHUB_CONNECTOR` is exposed, continue supported reads/writes through it;
4. do not say `GitHub unavailable` unless the required managed path has also actually failed or is absent;
5. do not convert the transport failure into a mathematical/research `HARD_BLOCK`.

Canonical user-facing summary when the connector remains usable:

> 本地 Git 网络在当前运行环境不可用（DNS/egress 阻断），这是工具层软限制，不影响研究。按仓库规则不把它当 `HARD_BLOCK`；继续使用当前运行环境已暴露并授权的 GitHub connector 完成其支持的远端操作。

## If the connector cannot perform the exact operation

Some operations may require local Git semantics that the managed connector does not expose.

In that case:

- continue all independent mathematical/research work;
- keep the completed payload intact;
- mark only the unavailable remote operation as:

`REMOTE_PUBLICATION_DEFERRED`

or, when appropriate,

`LOCAL_GIT_TRANSPORT_REQUIRED_FOR_THIS_OPERATION`.

This is not `TASK_CANNOT_COMPLETE` unless the user's requested end state literally consists of that unavailable remote mutation and there is no alternative supported path.

## If the managed connector also fails

A connector failure must be independently observed. Do not infer it from local DNS.

Only after an actual connector failure may the runtime record:

`MANAGED_GITHUB_CONNECTOR_FAILED`

If both remote paths are unavailable, preserve the research result and classify the publication/integration slice as deferred. Research remains nonblocked unless a genuine four-field mathematical/research `HARD_BLOCK` exists.

## No retry loops

For one unchanged local DNS failure, do not enter:

`git fetch -> gh api -> curl -> nslookup -> git fetch -> ...`

One observed transport failure is sufficient to route around that transport for the current execution phase. Re-test only after materially new runtime/network information or an explicit user request.

## Relationship to existing liveness rules

This document specializes the existing principles in `docs/GITHUB_INTERACTION_BUDGET.md` and `docs/ARTIFACT_PUBLICATION_LIVENESS.md`:

- research is the hot path;
- remote tooling is a persistence/integration boundary;
- tool/network/publication failure is not a mathematical `HARD_BLOCK`;
- publication should use the simplest available bounded path.

It does not create GitHub connectivity, permissions, or a connector. It only prevents a known transport-layer failure from being misinterpreted and pre-resolves the correct fallback behavior.
