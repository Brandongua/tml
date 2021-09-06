from setuptools import setup

setup(
    name='tml',
    version="1.0.0",
    url='https://www.github.com/brandongua/tml',
    description='The interpreter for the terminal markup language',
    author='Brandon',
    packages=['tml'],
    entry_points="""
        [console_scripts]
        tml=tml.tml:main
    """
)

