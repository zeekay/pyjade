from pyjade import Environment

class DjangoEnvironment(Environment):

    auto_close_tags = {
        'for': 'endfor',
        'if': 'endif',
        'ifchanged': 'endifchanged',
        'ifequal': 'endifequal',
        'ifnotequal':'endifnotequal',
        'block':'endblock',
        'filter':'endfilter',
        'autoescape':'endautoescape',
        'with':'endwith',
        'blocktrans': 'endblocktrans',
        'spaceless': 'endspaceless',
        'comment': 'endcomment',
        'cache': 'endcache',
        'localize': 'endlocalize',
        'compress': 'endcompress',
    }

    may_contain_tags = {
        'if': ['else','elif'],
        'ifchanged': ['else'],
        'ifequal': ['else'],
        'ifnotequal': ['else'],
        'for': ['empty'],
        'with': ['with'],
    }

    code_tags = ('include','extends','for','block','if','elif','ifchanged','ifequal','ifnotequal','else','filter','with','while')

    def tag_begin(self,node):
        return '{%%%s%%}'%node.statement

    def tag_end(self,node):
        return '{%%%s%%}'%node.closetag if node.closetag else ''

    def var(self,node):
        return '{{%s}}'%node.raw
