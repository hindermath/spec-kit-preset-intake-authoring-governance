#!/usr/bin/env python3
"""Resolve an existing repository file before the PowerShell wrapper reads it."""

import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--repo", required=True)
parser.add_argument("--file", required=True)
args = parser.parse_args()
try:
    root = Path(args.repo).resolve(strict=True)
    path = Path(args.file).resolve(strict=True)
    if not path.is_file() or not path.is_relative_to(root):
        raise ValueError("outside repository")
    print(json.dumps({"path": str(path)}))
except (OSError, RuntimeError, ValueError):
    print(json.dumps({"errorClass": "RIG004", "message": "repository file containment failed"}))
    raise SystemExit(2) from None
