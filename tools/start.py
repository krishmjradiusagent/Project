#!/usr/bin/env python3
import json
import os
import shutil
import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

ROOT = Path.cwd()
APP = ROOT / "app"
DEFAULT_PORT = 5173
STATIC_PORT = 8000

def find_free_port(preferred: int) -> int:
    for port in [preferred] + list(range(preferred + 1, preferred + 20)):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return preferred

def has_command(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def detect_package_manager(app: Path) -> str:
    if (app / "pnpm-lock.yaml").exists() and has_command("pnpm"):
        return "pnpm"
    if (app / "yarn.lock").exists() and has_command("yarn"):
        return "yarn"
    if (app / "bun.lockb").exists() and has_command("bun"):
        return "bun"
    return "npm"

def run(command, cwd: Path):
    print(f"$ {' '.join(command)}")
    return subprocess.run(command, cwd=cwd)

def popen(command, cwd: Path):
    print(f"$ {' '.join(command)}")
    return subprocess.Popen(command, cwd=cwd)

def get_scripts(package_json: Path) -> dict:
    try:
        data = json.loads(package_json.read_text())
        return data.get("scripts", {})
    except Exception:
        return {}

def install_deps(pm: str):
    if pm == "pnpm":
        return ["pnpm", "install"]
    if pm == "yarn":
        return ["yarn", "install"]
    if pm == "bun":
        return ["bun", "install"]
    return ["npm", "install"]

def dev_command(pm: str, port: int, scripts: dict):
    script = "dev" if "dev" in scripts else "start" if "start" in scripts else None
    if not script:
        return None

    # Most Vite/Next apps accept this; if not, user can run package command manually.
    if pm == "pnpm":
        return ["pnpm", script, "--", "--host", "0.0.0.0", "--port", str(port)]
    if pm == "yarn":
        return ["yarn", script, "--host", "0.0.0.0", "--port", str(port)]
    if pm == "bun":
        return ["bun", "run", script, "--host", "0.0.0.0", "--port", str(port)]
    return ["npm", "run", script, "--", "--host", "0.0.0.0", "--port", str(port)]

def static_server():
    port = find_free_port(STATIC_PORT)
    url = f"http://localhost:{port}"
    print("No package.json found in app/.")
    print("Starting static server.")
    print(url)
    webbrowser.open(url)
    subprocess.run([sys.executable, "-m", "http.server", str(port)], cwd=APP)

def main():
    if not APP.exists():
        raise SystemExit("app/ folder not found. Put app/prototype code inside app/.")

    package_json = APP / "package.json"
    if not package_json.exists():
        static_server()
        return

    pm = detect_package_manager(APP)
    scripts = get_scripts(package_json)

    if not (APP / "node_modules").exists():
        print("node_modules missing. Installing dependencies...")
        result = run(install_deps(pm), APP)
        if result.returncode != 0:
            raise SystemExit("Dependency install failed.")

    port = find_free_port(DEFAULT_PORT)
    cmd = dev_command(pm, port, scripts)
    if not cmd:
        raise SystemExit("No dev/start script found in app/package.json.")

    url = f"http://localhost:{port}"
    print(f"Starting local app: {url}")
    proc = popen(cmd, APP)

    time.sleep(2)
    webbrowser.open(url)

    try:
        proc.wait()
    except KeyboardInterrupt:
        print("\nStopping local server...")
        proc.terminate()

if __name__ == "__main__":
    main()
