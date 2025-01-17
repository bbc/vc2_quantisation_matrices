SMPTE ST 2042-1 (VC-2) Quantisation Matrix Computation Routines
===============================================================

This Python package, `vc2_quantisation_matrices`, provides both a standalone
software tool and Python module for computing 'default' quantisation matrices
for the SMPTE ST 2042-1:2017 [VC-2 professional video
codec](https://www.bbc.co.uk/rd/projects/vc-2). Specifically, this software
implements the procedure from section (D.3.2) of the standard for computing
quantisation matrices which achieve noise-power normalisation.

This software is provided both as an informal reference and also as a tool for
computing quantisation matrices for wavelet transform and depth combinations
for which no default matrix is provided.

For further information, please conatact [Jonathan
Heathcote](mailto:jonathan.heathcote@bbc.co.uk) or [John
Fletcher](mailto:john.fletcher@bbc.co.uk).


Installation
------------

You can install the `vc2_quantisation_matrices` Python
module from [PyPI](https://pypi.org/) using:

    $ pip install vc2_quantisation_matrices

Alternatively you can install it from a copy of this repository using:

    $ python setup.py install

Documentation
-------------

You can read the [`vc2_quantisation_matrices` manual online
here](https://bbc.github.io/vc2_quantisation_matrices/) (also available in [PDF
format](https://bbc.github.io/vc2_quantisation_matrices/vc2_quantisation_matrices_manual.pdf)).
This includes both instruction on the use of this software as well as a more
thorough overview of the process it implements.


Running the Tests
-----------------

To run the test suite, first install the test suite dependencies using:

    $ pip install -r requirements-test.txt

Then run the tests:

    $ pytest tests/


Building the Documentation
--------------------------

To build the documentation, first install the build dependencies:

    $ pip install -r requirements-doc.txt

Then build the documentation:

    $ cd docs
    $ make html  # or make latexpdf 

The built documentation can then be found in `docs/build/`.


License
-------

This software is distributed under the [GNU General Public License version
3](./LICENSE.txt), &copy; BBC 2021.
