from setuptools import setup, find_packages

setup(
    name="cip",
    version="0.1.0",
    description="Cifra de Integridade Primal (CIP) — segurança vetorial baseada em estrutura espectral",
    author="Alvaro Costa",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["numpy", "sympy"],
    python_requires=">=3.7",
        url="https://github.com/costaalv/projeto-delta",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
