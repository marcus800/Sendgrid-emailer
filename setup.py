#from distutils.core import setup
from setuptools import setup
setup(
    name='Emalier_Sendgrid',
    version='1.0',
    packages=[
              'lib.python2.7.site-packages.pip.req', 'lib.python2.7.site-packages.pip.vcs',
              'lib.python2.7.site-packages.pip.utils', 'lib.python2.7.site-packages.pip.compat',
              'lib.python2.7.site-packages.pip.models', 'lib.python2.7.site-packages.pip._vendor',
              'lib.python2.7.site-packages.pip._vendor.distlib',
              'lib.python2.7.site-packages.pip._vendor.distlib._backport',
              'lib.python2.7.site-packages.pip._vendor.colorama', 'lib.python2.7.site-packages.pip._vendor.html5lib',
              'lib.python2.7.site-packages.pip._vendor.html5lib._trie',
              'lib.python2.7.site-packages.pip._vendor.html5lib.filters',
              'lib.python2.7.site-packages.pip._vendor.html5lib.treewalkers',
              'lib.python2.7.site-packages.pip._vendor.html5lib.treeadapters',
              'lib.python2.7.site-packages.pip._vendor.html5lib.treebuilders',
              'lib.python2.7.site-packages.pip._vendor.lockfile', 'lib.python2.7.site-packages.pip._vendor.progress',
              'lib.python2.7.site-packages.pip._vendor.requests',
              'lib.python2.7.site-packages.pip._vendor.requests.packages',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.chardet',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.util',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'lib.python2.7.site-packages.pip._vendor.packaging',
              'lib.python2.7.site-packages.pip._vendor.cachecontrol',
              'lib.python2.7.site-packages.pip._vendor.cachecontrol.caches',
              'lib.python2.7.site-packages.pip._vendor.webencodings',
              'lib.python2.7.site-packages.pip._vendor.pkg_resources', 'lib.python2.7.site-packages.pip.commands',
              'lib.python2.7.site-packages.pip.operations', 'lib.python2.7.site-packages.attr',
              'lib.python2.7.site-packages.cffi', 'lib.python2.7.site-packages.enum',
              'lib.python2.7.site-packages.idna', 'lib.python2.7.site-packages.test',
              'lib.python2.7.site-packages.zope.interface', 'lib.python2.7.site-packages.zope.interface.tests',
              'lib.python2.7.site-packages.zope.interface.common',
              'lib.python2.7.site-packages.zope.interface.common.tests', 'lib.python2.7.site-packages.wheel',
              'lib.python2.7.site-packages.wheel.test', 'lib.python2.7.site-packages.wheel.test.simple.dist.simpledist',
              'lib.python2.7.site-packages.wheel.test.complex-dist.complexdist',
              'lib.python2.7.site-packages.wheel.tool', 'lib.python2.7.site-packages.wheel.signatures',
              'lib.python2.7.site-packages.pyasn1', 'lib.python2.7.site-packages.pyasn1.type',
              'lib.python2.7.site-packages.pyasn1.codec', 'lib.python2.7.site-packages.pyasn1.codec.ber',
              'lib.python2.7.site-packages.pyasn1.codec.cer', 'lib.python2.7.site-packages.pyasn1.codec.der',
              'lib.python2.7.site-packages.pyasn1.codec.native', 'lib.python2.7.site-packages.pyasn1.compat',
              'lib.python2.7.site-packages.automat', 'lib.python2.7.site-packages.automat._test',
              'lib.python2.7.site-packages.OpenSSL', 'lib.python2.7.site-packages.twisted',
              'lib.python2.7.site-packages.twisted.tap', 'lib.python2.7.site-packages.twisted.web',
              'lib.python2.7.site-packages.twisted.web.test', 'lib.python2.7.site-packages.twisted.web._auth',
              'lib.python2.7.site-packages.twisted.cred', 'lib.python2.7.site-packages.twisted.cred.test',
              'lib.python2.7.site-packages.twisted.mail', 'lib.python2.7.site-packages.twisted.mail.test',
              'lib.python2.7.site-packages.twisted.mail.scripts', 'lib.python2.7.site-packages.twisted.news',
              'lib.python2.7.site-packages.twisted.news.test', 'lib.python2.7.site-packages.twisted.pair',
              'lib.python2.7.site-packages.twisted.pair.test', 'lib.python2.7.site-packages.twisted.test',
              'lib.python2.7.site-packages.twisted.conch', 'lib.python2.7.site-packages.twisted.conch.ui',
              'lib.python2.7.site-packages.twisted.conch.ssh', 'lib.python2.7.site-packages.twisted.conch.test',
              'lib.python2.7.site-packages.twisted.conch.client', 'lib.python2.7.site-packages.twisted.conch.insults',
              'lib.python2.7.site-packages.twisted.conch.scripts',
              'lib.python2.7.site-packages.twisted.conch.openssh_compat', 'lib.python2.7.site-packages.twisted.names',
              'lib.python2.7.site-packages.twisted.names.test', 'lib.python2.7.site-packages.twisted.trial',
              'lib.python2.7.site-packages.twisted.trial.test', 'lib.python2.7.site-packages.twisted.trial._dist',
              'lib.python2.7.site-packages.twisted.trial._dist.test', 'lib.python2.7.site-packages.twisted.words',
              'lib.python2.7.site-packages.twisted.words.im', 'lib.python2.7.site-packages.twisted.words.test',
              'lib.python2.7.site-packages.twisted.words.xish', 'lib.python2.7.site-packages.twisted.words.protocols',
              'lib.python2.7.site-packages.twisted.words.protocols.jabber',
              'lib.python2.7.site-packages.twisted.logger', 'lib.python2.7.site-packages.twisted.logger.test',
              'lib.python2.7.site-packages.twisted.python', 'lib.python2.7.site-packages.twisted.python.test',
              'lib.python2.7.site-packages.twisted.runner', 'lib.python2.7.site-packages.twisted.runner.test',
              'lib.python2.7.site-packages.twisted.spread', 'lib.python2.7.site-packages.twisted.spread.test',
              'lib.python2.7.site-packages.twisted.plugins', 'lib.python2.7.site-packages.twisted.scripts',
              'lib.python2.7.site-packages.twisted.scripts.test', 'lib.python2.7.site-packages.twisted._threads',
              'lib.python2.7.site-packages.twisted._threads.test', 'lib.python2.7.site-packages.twisted.internet',
              'lib.python2.7.site-packages.twisted.internet.test',
              'lib.python2.7.site-packages.twisted.internet.iocpreactor',
              'lib.python2.7.site-packages.twisted.persisted', 'lib.python2.7.site-packages.twisted.persisted.test',
              'lib.python2.7.site-packages.twisted.protocols', 'lib.python2.7.site-packages.twisted.protocols.mice',
              'lib.python2.7.site-packages.twisted.protocols.test',
              'lib.python2.7.site-packages.twisted.protocols.haproxy',
              'lib.python2.7.site-packages.twisted.protocols.haproxy.test',
              'lib.python2.7.site-packages.twisted.enterprise', 'lib.python2.7.site-packages.twisted.application',
              'lib.python2.7.site-packages.twisted.application.test',
              'lib.python2.7.site-packages.twisted.application.twist',
              'lib.python2.7.site-packages.twisted.application.twist.test',
              'lib.python2.7.site-packages.twisted.application.runner',
              'lib.python2.7.site-packages.twisted.application.runner.test',
              'lib.python2.7.site-packages.twisted.positioning', 'lib.python2.7.site-packages.twisted.positioning.test',
              'lib.python2.7.site-packages.sendgrid', 'lib.python2.7.site-packages.sendgrid.helpers',
              'lib.python2.7.site-packages.sendgrid.helpers.mail',
              'lib.python2.7.site-packages.sendgrid.helpers.inbound', 'lib.python2.7.site-packages.hyperlink',
              'lib.python2.7.site-packages.hyperlink.test', 'lib.python2.7.site-packages.pycparser',
              'lib.python2.7.site-packages.pycparser.ply', 'lib.python2.7.site-packages.asn1crypto',
              'lib.python2.7.site-packages.asn1crypto._perf', 'lib.python2.7.site-packages.constantly',
              'lib.python2.7.site-packages.pysendgrid', 'lib.python2.7.site-packages.setuptools',
              'lib.python2.7.site-packages.setuptools.extern', 'lib.python2.7.site-packages.setuptools.command',
              'lib.python2.7.site-packages.exampleproj', 'lib.python2.7.site-packages.incremental',
              'lib.python2.7.site-packages.incremental.tests', 'lib.python2.7.site-packages.cryptography',
              'lib.python2.7.site-packages.cryptography.x509', 'lib.python2.7.site-packages.cryptography.hazmat',
              'lib.python2.7.site-packages.cryptography.hazmat.backends',
              'lib.python2.7.site-packages.cryptography.hazmat.backends.openssl',
              'lib.python2.7.site-packages.cryptography.hazmat.bindings',
              'lib.python2.7.site-packages.cryptography.hazmat.bindings.openssl',
              'lib.python2.7.site-packages.cryptography.hazmat.primitives',
              'lib.python2.7.site-packages.cryptography.hazmat.primitives.kdf',
              'lib.python2.7.site-packages.cryptography.hazmat.primitives.ciphers',
              'lib.python2.7.site-packages.cryptography.hazmat.primitives.twofactor',
              'lib.python2.7.site-packages.cryptography.hazmat.primitives.asymmetric',
              'lib.python2.7.site-packages.pkg_resources', 'lib.python2.7.site-packages.pkg_resources.extern',
              'lib.python2.7.site-packages.pkg_resources._vendor',
              'lib.python2.7.site-packages.pkg_resources._vendor.packaging',
              'lib.python2.7.site-packages.pyasn1_modules', 'lib.python2.7.site-packages.service_identity',
              'lib.python2.7.site-packages.python_http_client'],
    url='https://github.com/marcus800/Sendgrid-emailer/',
    license='MIT',
    author='marcus',
    author_email='lewis@pinnaclevl.com',
    description='Sendgrid emalier'
)
