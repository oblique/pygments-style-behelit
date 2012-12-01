# -*- coding: utf-8 -*-
"""
    behelit
    ~~~~~~~~~~

    Port of the behelit color scheme.

    :copyright: Copyright 2011 oblique
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text


class BehelitStyle(Style):
    """
    Port of the behelit color scheme.
    """

    background_color = '#101010'
    highlight_color = '#ffff5f'

    styles = {
        Text:                   '#66ff66',
        Error:                  'bold #ff005f',

        Comment:                '#5f5f5f',
        Comment.Preproc:        'bold #87ff5f',

        Keyword:                '#d7005f',
        Keyword.Type:           '#5fafff',

        Operator:               'bold #66ff66',
        Operator.Word:          'bold #ee6363',

        Punctuation:            '#ff6a6a',

        Name:                   '#66ff66',
        Name.Function:          '#af87ff',
        Name.Constant:          '#af87ff',
        Name.Label:             '#af87ff',

        Number:                 '#af87ff',

        String:                 '#ffff87',
    }
