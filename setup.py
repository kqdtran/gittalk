from distutils.core import setup

setup(
    name='gittalk',
    version='0.1.0',
    url='https://github.com/kqdtran/gittalk',
    author='Khoa Tran',
    author_email='khoatran@berkeley.edu',
    description=('talk with git'),
    license='MIT',
    packages=['gittalk'],
    scripts=[
        'bin/gittalk'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
    ],
)