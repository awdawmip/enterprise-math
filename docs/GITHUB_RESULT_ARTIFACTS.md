# Result inputs from selected GitHub content

A Result can refer to material already committed to `awdawmip/enterprise-math`, including a historical commit whose content differs from current main or whose path no longer exists there. The calling researcher chooses the material for its research meaning. Commit and path describe the chosen input; they are not current-branch membership or version-equality gates.

The optional native freeze input `artifact_sources` is a list of `{repository, source_commit, path, git_blob_sha1}` references. The CLI accepts it as `--artifact-sources-json`. The native writer reads those actual committed bytes, calculates their SHA-256, and stores the sources and manifest in the Result. This reads material; it does not write into a task output directory. No upload or duplicate material commit is needed.

Result audit and continuation consume these sources rather than substituting files from the current checkout. A normal Git checkout can read its object database; an archive-based worker reads the fixed public GitHub raw-content URL without credentials. Reads verify the selected blob and content hashes. The reader has a 32 MiB per-file capacity and a bounded process-local cache, and retains no historical checkout tree. GitHub availability and existence of the selected content remain real dependencies.

The native Result record still belongs to its actual authorized researcher/session/run and task. Existing role, contribution, CLAIM, ownership and write-CAS rules protect the record write; they do not choose mathematical conclusions or require an artifact to match main. The actual publishing destination and repository scope are unchanged. Reference code is read as data, never executed as the control program. Publication does not imply mathematical acceptance.

The legacy filesystem/checkpoint freeze interface remains available. Existing immutable Results, receipts and unresolved transactions are not rewritten or replayed. New reference Results use the added `artifact_sources` field; records without that field retain their legacy audit semantics.

For the existing console, use `em_private_session_control` with `operation=use`, your own custody reference, and `payload.tool=em_execution_freeze_github`. Its arguments remain `run_id`, `generation`, `return_path`, `metadata`, optional `output_paths` and `source_commit`. GitHub Chat uses `freeze_github` with the existing own `run_request_id`. Read the original request receipt; reconcile an unknown outcome by that same ID.

This change was prepared without adding or running tests, as requested. Static parsing, package construction and read-only deployment checks are not end-to-end Result validation.
