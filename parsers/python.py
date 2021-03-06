
import re
from base_parser import BaseParser


class Parser(BaseParser):

    def setup_settings(self):
        nameToken = '[a-zA-Z_\\x7f-\\xff][a-zA-Z0-9_\\x7f-\\xff]*'
        self.settings = {
            'varIdentifier': nameToken + '(?:\.' + nameToken + ')*',
            'fnIdentifier': nameToken,
            'classIdentifier': nameToken,
            'bool': 'boolean',
            'function': 'def',
            'block_start': '"""',
            'block_middle': '',
            'block_end': '"""',
            'insert_after_def': True
        }

    def parse_class(self, line):
        res = re.search(
            'class\\s+(?P<name>' + self.settings['classIdentifier'] + ')\\s*\(?(?P<extends>[^\)]+)?\)?',
            line
        )

        if res:
            return (res.group('name'), res.group('extends'))

        return None

    def parse_function(self, line):
        # def [name] [($@%&+)] {
        res = re.search(
            'def\\s+'
            + '(?P<name>' + self.settings['fnIdentifier'] + ')'
            # sub fnName
            + '\\s*\\((?P<args>.*)\):',
            # (arg1, arg2)
            line
        )

        if not res:
            return None

        return (res.group('name'), res.group('args'))
        # return (res.group('name'), ())

    def get_arg_type(self, arg):
        #  def add($x, $y = 1)
        res = re.search(
            '(?P<name>' + self.settings['varIdentifier'] + ")\\s*=\\s*(?P<val>.*)",
            arg
        )
        if res:
            return self.guess_type_from_value(res.group('val'))

        #  function sum(Array $x)
        if re.search('\\S\\s', arg):
            return re.search("^(\\S+)", arg).group(1)
        else:
            return None

    def get_arg_name(self, arg):
        return re.search("([^=]+)", arg).group(0)

    def parse_var(self, line):
        res = re.search(
            #   var $foo = blah,
            #       $foo = blah;
            #   $baz->foo = blah;
            #   $baz = array(
            #        'foo' => blah
            #   )

            '(?P<name>' + self.settings['varIdentifier'] + ')\\s*=>?\\s*(?P<val>.*?)(?:[;,]|$)',
            line
        )
        if res:
            return (res.group('name'), res.group('val').strip())

        res = re.search(
            '\\b(?:var|public|private|protected|static)\\s+(?P<name>' + self.settings['varIdentifier'] + ')',
            line
        )
        if res:
            return (res.group('name'), None)

        return None

    def guess_type_from_value(self, val):
        if self.is_numeric(val):
            return 'float' if '.' in val else 'integer'
        if val[0] == '"' or val[0] == "'":
            return 'string'
        if val[:5] == 'array':
            return 'array'
        if val.lower() in ('true', 'false', 'filenotfound'):
            return 'boolean'
        if val[:4] == 'new ':
            res = re.search('new (' + self.settings['fnIdentifier'] + ')', val)
            return res and res.group(1) or None
        return None
