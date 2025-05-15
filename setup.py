from setuptools import setup, find_packages

setup(
    name='delta-cip',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='Alvaro Costa',
    author_email='costaalv@alumni.usp.br',
    description='Cifra de Integridade Primal (CIP) — verificação vetorial baseada na estrutura dos primos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/costaalv/projeto-delta',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'numpy',
        'sympy'
    ],
    python_requires='>=3.8',
)