# User input integrity: a separate native computation

Status before execution: DECLARED_SINGLE_RUN_INPUT_CHECK / NOT_A_FACTORING_EXPERIMENT.

The user supplied the decimal integer 505246541734676269885345827299505246541734676269885345827299 and labels p=670915268711887, q=753070566876077. The decimal string appears to repeat the block 505246541734676269885345827299. This check determines consistency through actual native typed operations while the user clarifies the intended target. It neither assumes p and q are prime nor uses them to select a factoring parameter.

Exactly four scientific arithmetic operations are declared: multiply the supplied p and q, compare that product with the complete integer, compare it with the displayed block, and divide the complete integer by the product. All use the frozen lazy_modular Arithmetic full-adder implementation. No host multiplication, remainder, gcd, modular power or numerical answer oracle is used. Decimal parsing, source hashes, JSON/gzip, classifications of saved outputs and administrative counts are wiring/evidence work.

The source first verifies the current activity guard, the frozen adjacent helper and all of its dependency pins. It records exclusive STARTED before importing the scientific wrappers. The actual old.source_check supplies the source-bound native full-adder catalog. Every typed operation and actual native call is retained in the result, with all arithmetic costs and source bindings. This small input check does not call a previous main routine or replay any prior fixture. It preserves a failure artifact instead of blindly rerunning.

The p/q input file and result belong only to this separate integrity/answer-key unit. A later factor-blind runner receives its chosen N, public parameter policy and source bindings; it must not receive p/q, a local order, or parameters chosen from those factors. The complete versus product target question is still pending during this independent check.

Run once after a static source review with the actual guard and root's actual knowledge SHA. Evidence checks may read the saved records without rerunning this computation. This plan adds no primality certificate, factoring success rate or Shor completion claim.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1.
