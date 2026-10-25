import sys
from pathlib import Path

from playwright.sync_api import Browser, BrowserContext, Playwright


def _flag_value(flag: str) -> str | None:
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return None


DEBUG = "--debug" in sys.argv
TRACING = _flag_value("--tracing") == "on"

TRACE_DIR = Path("trace")


def launch_browser(playwright: Playwright, **kwargs) -> Browser:
    return playwright.chromium.launch(
        headless=False, slow_mo=500 if DEBUG else 0, **kwargs
    )


def start_tracing(context: BrowserContext) -> None:
    if TRACING:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)


def stop_tracing(context: BrowserContext, name: str) -> None:
    if TRACING:
        TRACE_DIR.mkdir(exist_ok=True)
        context.tracing.stop(path=str(TRACE_DIR / f"{name}.zip"))
