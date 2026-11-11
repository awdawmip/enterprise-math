"""Offline new-unit selection; no network, Source publication or research writes."""
import copy
from collections import Counter
from datetime import datetime, timedelta, timezone
import socket
import unittest
from unittest.mock import patch

from control_plane import research_control_bootstrap
with patch.object(research_control_bootstrap, 'install'):
    import research_control_dispatch as router
from tools import research_fair_selection as fair
from tools import research_runtime_reducer as reducer

NOW = datetime(2026, 11, 11, tzinfo=timezone.utc)
POLICY = copy.deepcopy(reducer.load_policy())
POLICY['selection_policy']['random_rotation'] = {
    'enabled': True, 'wait_scale_days': 7, 'max_wait_bonus': 3, 'unclaimed_bonus': 1.5}


def task(name, priority='P0', days=30, parent=None):
    value = reducer.reduce_task(dict(task_id=name, priority=priority, kind='RESEARCH',
        base_state='READY', last_progress_at=(NOW-timedelta(days=days)).isoformat(),
        parent_task_id=parent, publication_id='TP2-FIXTURE-'+name, next_action='derive'),
        [], default_lease_minutes=120, now=NOW)
    value["publication_id"] = "TP2-FIXTURE-" + name
    return value


def choose(states, seed):
    with fair.selection_scope(seed, NOW):
        return reducer.select_state(states, POLICY)


class RotationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.network = patch.object(socket, 'socket', side_effect=AssertionError('network forbidden'))
        cls.network.start()

    @classmethod
    def tearDownClass(cls):
        cls.network.stop()

    def test_same_seed_clock_and_pool_replay_and_input_order(self):
        states=[task('old-a'),task('old-b','P1'),task('new','P2',0)]
        before=copy.deepcopy(states)
        a=choose(states,'original-request');b=choose(list(reversed(states)),'original-request')
        self.assertEqual(a['task_id'],b['task_id'])
        self.assertEqual(a['fair_selection'],b['fair_selection'])
        self.assertEqual(states,before)

    def test_old_unclaimed_directions_and_all_priorities_get_real_opportunity(self):
        states=[task('old-'+p+'-'+str(n),p,45+n*7) for p in ('P0','P1','P2','P3') for n in range(6)]
        counts=Counter();priorities=Counter()
        for n in range(512):
            chosen=choose(states,'new-unit-'+str(n));counts[chosen['task_id']]+=1;priorities[chosen['priority']]+=1
        self.assertEqual(set(counts),{s['task_id'] for s in states})
        self.assertTrue(all(priorities[p]>10 for p in ('P0','P1','P2','P3')))
        self.assertLess(priorities['P0'],300)
        print('ROTATION_OPPORTUNITY',dict(priorities),'unique_waiting_tasks',len(counts))

    def test_waiting_bonus_is_bounded_and_not_oldest_first(self):
        states=[task('old',days=70,parent='shared'),task('new',days=0,parent='shared')]
        count=Counter(choose(states,'unit-'+str(n))['task_id'] for n in range(256))
        self.assertGreater(count['old'],count['new']);self.assertGreater(count['new'],20)
        capped=[task('old',days=70,parent='shared'),task('new',days=7000,parent='shared')]
        # Both have reached the same bounded waiting bonus. Century-old metadata
        # cannot create an unbounded advantage or exclude the other candidate.
        counts=Counter(choose(capped,'unit-'+str(n))['task_id'] for n in range(256))
        self.assertGreater(min(counts.values()),70)

    def test_direction_selection_is_not_multiplied_by_task_count(self):
        states=[task('a-'+str(n),parent='direction-a') for n in range(20)]+[task('b',parent='direction-b')]
        counts=Counter(choose(states,'scope-'+str(n))['fair_selection']['direction'] for n in range(256))
        self.assertGreater(counts['direction-b'],70);self.assertGreater(counts['direction-a'],70)

    def test_live_owner_and_blocked_task_do_not_enter_draw(self):
        states=[task('live'),task('blocked'),task('available')]
        states[0].update(dispatch_state='LEASED',claim_id='existing-owner')
        states[1]['dispatch_state']='BLOCKED'
        for n in range(32):self.assertEqual(choose(states,str(n))['task_id'],'available')
        self.assertEqual(states[0]['claim_id'],'existing-owner')

    def test_missing_publication_does_not_hide_other_runnable_work(self):
        broken=task('definition-only');broken.pop('publication_id',None)
        valid=task('published')
        with fair.selection_scope('unit',NOW):
            route=router.route_from_candidates([],observations={},now=NOW,fresh_task=None,
                fresh_lane=None,policy=POLICY,states=[broken,valid])
        self.assertEqual(route['target']['task_id'],'published')
        self.assertEqual(route['fair_selection']['skipped_missing_publication'],1)

    def test_unknown_lifecycle_does_not_fabricate_old_waiting(self):
        state=task('unknown',days=1000);state['scheduling_history_degraded']='UNKNOWN_OVERLAY_START'
        selected=choose([state],'same')
        self.assertEqual(selected['fair_selection']['selected_waiting_days'],0)

    def test_failed_attempts_and_duplicate_claim_ids_do_not_buy_draw_credit(self):
        states=[task('a'),task('b')]
        sample={'event':'CLAIM','at':(NOW-timedelta(days=1)).isoformat(),'phase':1,'comment_id':2,'claim_id':'same-accepted-claim'}
        states[0]['scheduling_trace'].append(sample)
        first=choose(states,'same-seed')
        states[0]['scheduling_trace'].append(dict(sample))
        second=choose(states,'same-seed')
        self.assertEqual(first,second)
        self.assertEqual(second['fair_selection']['successful_claims'],1)

    def test_selection_context_cleans_up_after_failure(self):
        with self.assertRaises(ValueError):
            with fair.selection_scope('failed-unit',NOW):raise ValueError('synthetic failure')
        result=choose([task('a')],'next-unit')
        self.assertEqual(result['fair_selection']['selection_seed'],'next-unit')


    def test_priority_service_stays_weighted_across_successful_new_units(self):
        from tests.test_research_fair_selection import reduce, task as old_task, service
        states=[reduce(old_task('service-'+priority,priority)) for priority in ('P0','P1','P2','P3')]
        counts=Counter()
        for step in range(400):
            chosen=choose(states,'accepted-unit-'+str(step));counts[chosen['priority']]+=1
            service(next(state for state in states if state['task_id']==chosen['task_id']),3*step+1)
        for priority,wanted in {'P0':160,'P1':120,'P2':80,'P3':40}.items():
            self.assertLessEqual(abs(counts[priority]-wanted),6)
        print('ROTATION_ACCEPTED_SERVICE',dict(counts))

    def test_native_route_passes_stable_request_context_to_selector(self):
        from tests.test_priority_scoped_dispatch import PriorityScopeTests
        fixture=PriorityScopeTests();fixture.setUp()
        fixture.ns['research_runtime_reducer'].load_policy.return_value=POLICY
        fixture.states=[task('route-a'),task('route-b','P1')]
        first=fixture.route(selection_seed='original-route',selection_at=NOW.isoformat())
        second=fixture.route(selection_seed='original-route',selection_at=NOW.isoformat())
        self.assertEqual(first['target']['task_id'],second['target']['task_id'])
        self.assertEqual(first['fair_selection']['selection_seed'],'original-route')
        self.assertEqual(first['fair_selection']['selection_at'],NOW.isoformat())

    def test_malformed_waiting_clock_is_not_epoch_age(self):
        state=task('no-clock');state['scheduling_trace'][-1]['at']='unknown'
        result=choose([state],'same-unit')
        self.assertEqual(result['task_id'],'no-clock')
        self.assertEqual(result['fair_selection']['selected_waiting_days'],0)


if __name__=='__main__':unittest.main()
