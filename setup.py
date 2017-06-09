from setuptools import setup, find_packages

setup(name='cbsyst',
      version='0.1-dev',
      description='Tools calculating ocean C and B chemistry.',
      url='https://github.com/oscarbranson/cbsyst',
      author='Oscar Branson',
      author_email='oscarbranson@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Scientists',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   ],
      install_requires=['numpy',
                        'tqdm'],
      packages=['cbsyst'],
      zip_safe=False)