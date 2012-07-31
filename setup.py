# vim: fileencoding=utf-8 et ts=4 sts=4 sw=4 tw=0 fdm=marker fmr=#{,#}

from distutils.core import setup

if __name__ == '__main__':
    setup(
        name         = 'zone53',
        version      = '0.1',
        description  = 'A convenient Python interface to AWS route53 on top of Boto',
        author       = 'Alexander Glyzov',
        author_email = 'bonoba@gmail.com',
        url          = 'https://github.com/aglyzov/zone53',
        py_modules   = ['zone53'],
        requires     = ['boto (>= 2.0)']
    )

