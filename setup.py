from distutils.core import setup, Extension

blake_hash_module = Extension('blake_hash',
                               sources = ['blakemodule.c',
                                          'blake_hash.c',
										  'sph_blake.c'],
                               include_dirs=['.'])

setup (name = 'blake_hash',
       version = '0.1.0',
       description = 'Bindings for Blake-256 proof of work compatible with Decred.',
       maintainer = 'devwarrior',
       maintainer_email = 'devwarrior.decred@gmail.com',
       url = 'https://github.com/devwarrior777/decred-hash-py',
       ext_modules = [blake_hash_module])
