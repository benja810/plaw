from setuptools import setup, find_packages

setup(
    name='plaw',
    version='0.1',
    packages=['plaw'],
    description='A python wrapper for the lemmy HTTP API',
    author='Benjamin Jablonski',
    author_email='thebigjablonski@gmail.com',
    install_requires=["requests >=2.6.0, <3.0"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='lemmy plaw api',
)
