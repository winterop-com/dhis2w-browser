"""The plugin object dhis2w-core loads from the `dhis2w.plugins.v1` entry-point group."""

from __future__ import annotations

from dhis2w_core.plugin import Contribution, extension

#: The plugin trees this pack ships, one per supported DHIS2 major.
SUPPORTED_VERSION_KEYS: frozenset[str] = frozenset({"v41", "v42", "v43", "v44"})
#: The tree an unrecognised version key binds to; v43 is the canonical baseline.
DEFAULT_VERSION_KEY = "v43"


class BrowserPlugin:
    """Plugin descriptor for Playwright-driven DHIS2 UI automation."""

    @extension
    def contribute(self, version_key: str) -> Contribution:
        """Contribute `d2w browser` for `version_key`; the Playwright flows are CLI-only."""
        tree = version_key if version_key in SUPPORTED_VERSION_KEYS else DEFAULT_VERSION_KEY
        return Contribution(
            name="browser",
            description=(
                "Playwright-driven DHIS2 UI automation: dashboard, map and visualization screenshots, and PAT "
                "minting through the DHIS2 web UI."
            ),
            cli_module=f"dhis2w_browser.{tree}.cli",
            mcp_module=None,
        )


plugin = BrowserPlugin()
