#!/usr/bin/env python
# vim: fileencoding=utf-8 et ts=4 sts=4 sw=4 tw=0 fdm=marker fmr=#{,#}

from distutils.core import setup

DESCRIPTION = '''
`zone53`_ is a convenient Python API to manage Amazon’s DNS web service
`route53`_. Essentially, it is a thin layer on top of `boto.route53`_
providing Zone and Record classes.

.. _zone53: https://github.com/aglyzov/zone53
.. _route53: http://aws.amazon.com/route53/
.. _boto.route53: http://boto.readthedocs.org/en/latest/ref/route53.html
'''

if __name__ == '__main__':
    setup(
        name             = 'zone53',
        version          = '0.3.2',
        description      = 'A convenient Python API to manage AWS route53 (requires boto)',
        long_description = DESCRIPTION,
        author           = 'Alexander Glyzov',
        author_email     = 'bonoba@gmail.com',
        url              = 'https://github.com/aglyzov/zone53',
        py_modules       = ['zone53'],
        requires         = ['boto (>= 2.0)']
    )

