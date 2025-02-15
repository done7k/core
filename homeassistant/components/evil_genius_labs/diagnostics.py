"""Diagnostics support for Evil Genius Labs."""
from __future__ import annotations

from homeassistant.components.diagnostics import REDACTED
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from . import EvilGeniusUpdateCoordinator
from .const import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
) -> dict:
    """Return diagnostics for a config entry."""
    coordinator: EvilGeniusUpdateCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    return {
        "info": {
            **coordinator.info,
            "wiFiSsidDefault": REDACTED,
            "wiFiSSID": REDACTED,
        },
        "data": coordinator.data,
    }
