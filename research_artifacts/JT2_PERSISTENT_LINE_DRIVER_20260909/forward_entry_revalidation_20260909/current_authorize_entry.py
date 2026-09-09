import sys
from pathlib import Path
ROOT = Path('D:/em/control-assigned-gov-driver-entry-20260909')
sys.path.insert(0, str(ROOT))
from control_plane import research_control_bootstrap
research_control_bootstrap.install(ROOT)
from tools import research_runtime_guard
raise SystemExit(research_runtime_guard.main())
