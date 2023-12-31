"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class DrinkType(str, Enum):
    r"""The type of drink."""
    COCKTAIL = 'cocktail'
    NON_ALCOHOLIC = 'non-alcoholic'
    BEER = 'beer'
    WINE = 'wine'
    SPIRIT = 'spirit'
    OTHER = 'other'
