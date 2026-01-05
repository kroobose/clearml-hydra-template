"""
Configuration module for ClearML + Hydra template.

This module exports the root Config class for use with Hydra's ConfigStore.
"""

from .config import Config

__all__ = ["Config"]
