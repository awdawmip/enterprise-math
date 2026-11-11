# Selecting a new research unit

Continue your own unfinished research while it has a concrete next step. A new-unit draw is appropriate when that direction is exhausted, explicitly released, or a genuinely new unit is needed. It does not interrupt a live owner or replace the researcher's judgment about mathematical value.

Use the existing `dispatch` entry once, with one stable request ID. The console derives a seed and waiting-clock anchor from that durable request; retries, worker restarts and receipt polling retain the draw. Native CLI callers can retain `fair_selection.selection_seed` and use `--selection-seed` (and the same observation clock/input) to reproduce it. Read the returned route before preparing or claiming. A missing publication excludes that definition-only item from the new-unit draw; it does not hide other runnable work.

Selection preserves accepted-CLAIM service accounting and 40/30/20/10 base priority weights. A seeded weighted draw chooses priority, then an explicit-parent-chain direction, then a task. Bounded service correction, bounded known waiting time and an unclaimed-task bonus give neglected work a real chance. More siblings do not multiply a direction's chance. Waiting is not a strict oldest-first queue, and unknown lifecycle time creates no invented waiting debt. The receipt records method, seed, clock, candidate digest and the selected waiting/service statistics.

Preparation revalidates the originally returned Task and publication rather than drawing a new global winner. Current role, identity, ownership, dependency and CLAIM CAS rules still apply. Concurrent readers may recommend the same task; this is not an atomic reservation or global quota. After a definite ownership loss, obtain a new dispatch request. Unknown writes must be reconciled by their original ID first, never resubmitted under a new ID.

Use current continuation/dispatch receipts rather than manually repeating an old conversation's task list. Existing run -> own continuation/resume; new unit -> dispatch -> follow fresh/typed-continuation route -> CLAIM/open. Do not register a new identity every round, reopen paused automations or change their frequency for this policy. No extra startup inventory/history scan is required.

Offline fixtures check seed replay, waiting opportunity, priority/direction behavior, preserved accounting and owner/CAS boundaries. They do not prove that every scheduled conversation has consumed the new route or that a recommended task has been claimed or mathematically completed.
