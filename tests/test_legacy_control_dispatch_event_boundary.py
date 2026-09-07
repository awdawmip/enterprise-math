import unittest
from unittest import mock

from control_plane import check_legacy_control_isolation as isolation


class LegacyControlDispatchEventBoundaryTests(unittest.TestCase):
    def test_current_public_wrapper_enforces_event_boundary(self):
        self.assertEqual([], isolation._check_dispatch_event_boundary())

    def test_checker_rejects_each_fail_open_input_class(self):
        loader = isolation.research_dispatch.load_events
        invalid_labels = (
            "bare runtime events",
            "caller-supplied normalized envelopes",
            "mixed raw comments and bare events",
        )
        for index, label in enumerate(invalid_labels):
            with self.subTest(label=label):
                calls = 0

                def accept_one_invalid_input(path):
                    nonlocal calls
                    current = calls
                    calls += 1
                    return [] if current == index else loader(path)

                with mock.patch.object(
                    isolation.research_dispatch,
                    "load_events",
                    side_effect=accept_one_invalid_input,
                ):
                    self.assertEqual(
                        [f"live dispatch does not fail closed on {label}"],
                        isolation._check_dispatch_event_boundary(),
                    )

    def test_reject_everything_is_not_a_passing_boundary(self):
        with mock.patch.object(
            isolation.research_dispatch,
            "load_events",
            side_effect=isolation.research_dispatch.DispatchError("reject all"),
        ):
            errors = isolation._check_dispatch_event_boundary()
        self.assertEqual(1, len(errors))
        self.assertIn("rejects a valid raw-comment fixture", errors[0])

    def test_raw_comment_does_not_gain_control_authority(self):
        loader = isolation.research_dispatch.load_events

        def grant_authority(path):
            result = loader(path)
            if result:
                result[0]["_github"]["control_authorized"] = True
            return result

        with mock.patch.object(
            isolation.research_dispatch, "load_events", side_effect=grant_authority
        ):
            self.assertEqual(
                ["live dispatch fails raw-comment provenance/authority preservation"],
                isolation._check_dispatch_event_boundary(),
            )


if __name__ == "__main__":
    unittest.main()
