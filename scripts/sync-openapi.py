#!/usr/bin/env python3
import json
import os
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError as exc:
    raise SystemExit("Missing dependency: pyyaml. Install with `python3 -m pip install pyyaml` or run on the SendyKit server where it is already available.") from exc

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DEFAULT_CANONICAL = Path('/home/thedream/mail.thedream.rocks/sendykit/docs/openapi/sendykit-v2.yaml')
CANONICAL = Path(os.environ.get('CANONICAL_OPENAPI', str(DEFAULT_CANONICAL)))
OUTPUT = Path(os.environ.get('PUBLIC_OPENAPI_OUTPUT', str(REPO / 'api-reference/openapi.json')))

if not CANONICAL.exists():
    raise SystemExit(f'Canonical OpenAPI file not found: {CANONICAL}')

spec = yaml.safe_load(CANONICAL.read_text())
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(spec, indent=2) + '\n')
print(f'Synced {CANONICAL} -> {OUTPUT}')
