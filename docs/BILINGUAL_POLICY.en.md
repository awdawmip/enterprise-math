# Bilingual Synchronization Policy

## 1. Canonical language model

Enterprise Math is maintained in two parallel prose versions:

- pure English;
- pure Chinese.

Neither version is the translation-of-record and neither is secondary. The semantic pair is canonical.

If the two versions materially disagree, the repository state is considered inconsistent until they are reconciled.

## 2. File pairing

Formal prose documents must be registered in `bilingual_pairs.json`.

Naming convention:

- English: `NAME.en.md`;
- Chinese: `NAME.zh-CN.md`.

The root README is the deliberate exception:

- English: `README.md`;
- Chinese: `README.zh-CN.md`.

## 3. Same-change requirement

Whenever one member of a registered pair is added, deleted, or materially changed, the other member must be updated in the same pushed change set.

A documentation change that modifies only one language is incomplete.

Code, machine-readable data, mathematical proof files, workflow configuration, and language-neutral metadata do not require translated duplicates unless they contain substantial explanatory prose intended for readers.

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

`tools/check_bilingual_pairs.py` verifies:

1. every registered pair exists;
2. English prose contains no Chinese characters;
3. if one member of a pair changed in the current change set, the other member changed too.

The GitHub Actions workflow `.github/workflows/bilingual-sync.yml` runs this check on pushes and pull requests.

## 7. Review rule

A documentation pull request is not ready to merge until both language versions have been reviewed for semantic parity.

A later correction must fix both sides together; do not repair one language and leave the other knowingly stale.
