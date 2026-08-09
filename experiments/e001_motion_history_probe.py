"""E001.5 deterministic multi-tick response-history merge probe."""

from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_history import run_open_loop_motion_program


def main() -> None:
    initial = [Body2D(0, -2, 0, 0), Body2D(1, 0, 0, 0)]
    schedule = [
        {0: (1, 0), 1: (-1, 0)},
        {0: (-1, 0), 1: (0, 0)},
        {0: (1, 0), 1: (-1, 0)},
    ]
    report = run_open_loop_motion_program(initial, schedule)
    print(f"ticks={report.ticks}")
    print(f"response_histories={report.history_count}")
    print(f"terminal_states={report.terminal_state_count}")
    print(f"history_collision_spectrum={report.history_collision_spectrum}")
    for state, histories in report.terminal_histories:
        print(f"state={state}")
        print(f"fiber_size={len(histories)}")
        print(f"histories={histories}")

    merged = [
        (state, histories)
        for state, histories in report.terminal_histories
        if len(histories) > 1
    ]
    if not merged:
        raise SystemExit("E001.5 expected at least one response-history merge")


if __name__ == "__main__":
    main()
