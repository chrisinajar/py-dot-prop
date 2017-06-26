
from setuptools import setup
from pypandoc import convert_file

#: Converts the Markdown README in the RST format that PyPi expects.
long_description = convert_file('README.md', 'rst')

setup(name='dot_props',
      description='Get values from nested dict objects using dot notation',
      long_description=long_description,
      version='0.1.0',
      url='https://github.com/chrisinajar/py-dot-props',
      author='Chris Vickery',
      author_email='chrisinajar@gmail.com',
      license='MIT',
      # classifiers=[
      #     'Development Status :: 4 - Beta',
      #     'Intended Audience :: System Administrators',
      #     'License :: OSI Approved :: Apache Software License',
      #     'Programming Language :: Python :: 3'
      # ],
      packages=['dot_props'],
      install_requires=[
          'six>=1.10'
      ]
    )
