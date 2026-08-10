/-
R007 validation manifest.

This module intentionally does not register R007 in the canonical `EnterpriseMath.lean`
root.  Its only purpose is to make the complete owner-local R007 Lean surface reachable
from one explicit validation target.

When a Lean/Mathlib environment is available, compile this module directly before any
promotion/root-registration step.  A successful root `EnterpriseMath` build alone is
not evidence that these owner-local modules were checked.
-/

import EnterpriseMath.Scale.AllowedCellInterval
import EnterpriseMath.Scale.CellBridgeDescent
import EnterpriseMath.Scale.CellGapBridge
import EnterpriseMath.Scale.FareyBridge
import EnterpriseMath.Scale.FareyGap
import EnterpriseMath.Scale.FareyGridBridge
import EnterpriseMath.Scale.FiniteIntervalHelly
import EnterpriseMath.Scale.FinitePrefixExtension
import EnterpriseMath.Scale.GlobalScaleExtension
import EnterpriseMath.Scale.GridBridgeDescent
import EnterpriseMath.Scale.NaturalLift
import EnterpriseMath.Scale.OverlapBlockConnectivity
import EnterpriseMath.Scale.OverlapBoundary
import EnterpriseMath.Scale.OverlapCells
import EnterpriseMath.Scale.OverlapComponentCount
import EnterpriseMath.Scale.OverlapComponents
import EnterpriseMath.Scale.OverlapConnectivity
import EnterpriseMath.Scale.OverlapDivisibility
import EnterpriseMath.Scale.OverlapGraph
import EnterpriseMath.Scale.OverlapReachability
import EnterpriseMath.Scale.PerfectPowerNoDescent
import EnterpriseMath.Scale.PrefixCompatibility
import EnterpriseMath.Scale.PrefixExtensionStep
import EnterpriseMath.Scale.PrimeSplit
import EnterpriseMath.Scale.ScaleExtensionHelly
