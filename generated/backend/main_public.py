from __future__ import annotations

import importlib
import json
from pathlib import Path

from fastapi import FastAPI

from generated.backend.core.database import ping_database

app = FastAPI(title="Generated Public API")


@app.get("/health", tags=["system"])
def health():
    db_ok = ping_database()
    return {
        "status": "ok" if db_ok else "degraded",
        "database": "connected" if db_ok else "unreachable",
        "mode": "public",
    }


def _should_include(module_dir: Path) -> bool:
    metadata_path = module_dir / "metadata.json"
    if not metadata_path.exists():
        return False

    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except Exception:
        return False

    access_modes = metadata.get("access_modes", [])

    if "public" == "all":
        return (module_dir / "router_public.py").exists()

    if "public" == "public":
        return "public" in access_modes and (module_dir / "router_public.py").exists()

    if "public" == "secure":
        return any(x in access_modes for x in ("auth", "rbac")) and (module_dir / "router_public.py").exists()

    return False


def load_routers():
    base = Path(__file__).parent
    for module_dir in base.iterdir():
        if not module_dir.is_dir():
            continue
        if module_dir.name in {"core", "__pycache__"}:
            continue
        if not _should_include(module_dir):
            continue

        module_base = f"generated.backend.{module_dir.name}"
        router_module = "router_public.py".replace(".py", "")

        try:
            mod = importlib.import_module(f"{module_base}.{router_module}")
            app.include_router(mod.router)
        except Exception as exc:
            print(f"[WARN] Failed to load {module_dir.name}: {exc}")


load_routers()
