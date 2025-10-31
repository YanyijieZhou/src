"""Convenience exports for the getmy package.

Expose commonly used helpers from `getmy.getmy` at package level so callers
can do either `import getmy.getmy as gm` or `import getmy as gm` and access
the same functions.
"""
from .getmy import (
	dict_key_list,
	get_yaml_section,
)

__all__ = [
	'dict_key_list',
	'get_yaml_section',
]
