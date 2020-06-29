
import os
import re
from string import Template


class AngleBracketTemplate(Template):
    """ Template for substituting tokens in angle brackets.

    Tokens may have mixed case letters and underscores.
    E.g. <foo>, <foo_bar> or <Scene>
    """
    delimiter = '<'
    pattern = r"""
        \<(?:
        (?P<escaped>\<)|
        (?P<named>  )\>|
        (?P<braced>[A-Za-z][A-Za-z_]+)\>|
        (?P<invalid>)
        )
        """


class Expander(object):
    """Class to expand angle bracket tokens."""

    def __init__(self, **context):
        self._context = context

    def evaluate(self, target):
        """Evaluate target, whether its a value, list, or dict."""
        if type(target) == dict:
            result = {}
            for k in target:
                result[k] = self.evaluate_item(target[k])
            return result
        elif type(target) == list:
            return [self.evaluate_item(value) for value in target]
        return self.evaluate_item(target)

    def evaluate_item(self, item):
        """Evaluate an expression string

        Replace <token>s with values provided by the _context dict
        """
        item = os.path.expandvars(item.strip())
        try:
            return AngleBracketTemplate(item).substitute(self._context)
        except KeyError:
            raise KeyError("Invalid token. Valid tokens are: {}".format(
                self._context.keys()))