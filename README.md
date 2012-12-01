Installation:
=============

Manual installation:

    git clone git://github.com/oblique/pygments-style-behelit.git
    cd pygments-style-behelit
    python setup.py install


Usage example:
==============

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='behelit').style
    <class 'pygments_style_behelit.BehelitStyle'>


Export the style as CSS:
========================

    pygmentize -S behelit -f html > behelit.css


Please read the [official documentation][pygments] for further information
on the usage of pygment styles.


[pygments]: http://pygments.org/docs/
