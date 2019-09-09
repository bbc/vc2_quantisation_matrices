``vc2-make-quantisation-matrix`` standalone line tool
=====================================================

The ``vc2-make-quantisation-matrix`` command line application computes noise
power normalised quantisation matrices for arbitrary VC-2 filter
configurations. This utility is installed alongside the
:py:mod:`vc2_quantisation_matrices` module.

The utility expects the following arguments:

* ``--wavelet-index``: The index of the wavelet transform used for vertical
  filtering (as enumerated by (Table 12.1) in the VC-2 specification).
* ``--wavelet-index-ho``: The index of the wavelet transform used for
  horizontal filtering. (If not given, the same wavelet specified by
  ``--wavelet-index`` is assumed).
* ``--dwt-depth``: The number of 2D transform levels applied.
* ``--dwt-depth-ho``: The number of horizontal-only transform levels to apply.
  (If not given, defaults to 0.)

For example, the following invocation computes the quantisation matrix for a
4-level 2D LeGall transform::

    $ vc2-make-quantisation-matrix --wavelet-index 1 --dwt-depth 4
    Level 0: LL:  4
    Level 1: HL:  2, LH:  2, HH:  0
    Level 2: HL:  4, LH:  4, HH:  2
    Level 3: HL:  5, LH:  5, HH:  3
    Level 4: HL:  7, LH:  7, HH:  5
