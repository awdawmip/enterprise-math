# Bilingual Synchronization Policy

## 1. Canonical language model

Registered canonical prose in Enterprise Math is maintained in two parallel versions:

- pure English;
- pure Chinese.

Neither version is the translation-of-record and neither is secondary. The semantic pair is canonical.

If the two versions materially disagree, the repository state is considered inconsistent until they are reconciled.

## 2. File pairing

Documents adopted as shared bilingual canonical prose must be registered in
`bilingual_pairs.json`. Research notes, drafts and task-local handoffs may use one
language and need no translated duplicate merely to be saved or continued.
Existing registered pairs remain governed by this policy.
The `docs/NAME.en.md` and `docs/NAME.zh-CN.md` naming convention denotes registered
pairs; use ordinary note paths for unpaired research material.

Naming convention:

- English: `NAME.en.md`;
- Chinese: `NAME.zh-CN.md`.

The root README is the deliberate exception:

- English: `README.md`;
- Chinese: `README.zh-CN.md`.

## 3. Same-change requirement

When a registered pair is added, deleted, or materially changed, complete its
paired update before adopting that change as the shared canonical version. The
translation may be batched with the coherent integration; saving an interim
single-language draft or owner-branch checkpoint does not require it.

A canonical bilingual update with an outstanding translation remains incomplete;
this does not block independent research or preservation of the scientific file.

Code, machine-readable data, mathematical proof files, workflow configuration, and
language-neutral metadata do not require translated duplicates. Their explanatory
prose follows this policy only when it is explicitly maintained as a registered
canonical language pair.

## 4. Purity rule

English prose files must contain English prose only. Chinese prose files must contain Chinese prose only.

Allowed exceptions include:

- mathematical notation;
- code and identifiers;
- file paths;
- URLs;
- bibliographic names and titles when exact citation is required;
- project or software proper names that should not be translated.

Do not write bilingual explanatory paragraphs in a single canonical prose file.

## 5. Semantic parity

The two versions should preserve the same:

- claim status;
- definitions;
- formulas;
- examples;
- caveats;
- proof status;
- research questions;
- references;
- roadmap decisions.

Wording may be idiomatic rather than literal, but neither language may add or remove a material scientific claim without the same change being reflected in the paired version.

## 6. Automated enforcement

`tools/check_bilingual_pairs.py` verifies pair existence, English-file character
rules and matching heading structure. With `--base <commit>`, it also checks that
both members changed within the compared change set. These structural checks do
not establish semantic parity.

For a narrow change, `--paths <registered-path> [...]` checks the named pairs and
their counterparts. An explicitly requested unregistered path is an error; it is
not silently omitted. Without `--paths`, the command retains the complete registry
and document-registration audit. Use a valid comparison base when requesting the
same-change check.

The GitHub Actions workflow `.github/workflows/bilingual-sync.yml` is manual
(`workflow_dispatch`). Neither it nor a full registry audit is a prerequisite for
ordinary research or saving a scientific checkpoint.

## 7. Review rule

Before a registered canonical update is integrated, check the pair for semantic
parity; a maintainer may supply the translation. This is not a separate
mathematical-acceptance review or a requirement to translate ordinary research
notes. A later canonical correction must reconcile both sides; intermediate
single-language work must not be presented as an already synchronized pair.
