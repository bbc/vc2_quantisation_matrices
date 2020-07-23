from setuptools import setup, find_packages

with open("vc2_quantisation_matrices/version.py", "r") as f:
    exec(f.read())

setup(
    name="vc2_quantisation_matrices",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/bbc/vc2_quantisation_matrices",
    author="BBC R&D",
    description="Routines for computing quantisation matrices for the SMPTE ST 2042-2 VC-2 professional video codec.",
    license="GPLv2",
    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",

        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",

        "Programming Language :: Python :: 3",
    ],
    keywords="smpte-RP-2042-3 vc2 dirac dirac-pro quantisation-matrix bit-width",
    install_requires=["vc2_data_tables", "enum34", "sympy"],
    entry_points = {
        'console_scripts': [
            'vc2-make-quantisation-matrix=vc2_quantisation_matrices.cli_tool:main',
        ],
    },
)