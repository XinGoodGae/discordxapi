from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 2 - Pre-Alpha',
  'Intended Audience :: Developers',
  'Natural Language :: English',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.6'
]
 
setup(
  name='discordxapi',
  version='0.0.1',
  description='A easy way to use discord tools',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  author='XinGod',
  url=''
  author_email='xingodcontact@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='discord, api, tools', 
  packages=find_packages(),
  install_requires=[
      'requests',
      'aiohttp',
      'discord',
      'unidecode',
      'numpy',
      'colorama',
      'discord_webhooks'
  ]
)