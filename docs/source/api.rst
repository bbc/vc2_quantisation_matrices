:py:mod:`vc2_quantisation_matrices` Python module usage
=======================================================

The :py:mod:`vc2_quantisation_matrices` may be used to create quantisation
matrices which normalise noise power between transform bands. This may be done
using the following function:

.. autofunction:: vc2_quantisation_matrices.derive_quantisation_matrix

As an example, the quantisation matrix for a 4-level 2D LeGall transform may be
found as follows:

.. doctest::

    >>> from vc2_data_tables import WaveletFilters
    >>> from vc2_quantisation_matrices import derive_quantisation_matrix
    
    >>> matrix = derive_quantisation_matrix(
    ...     wavelet_index=WaveletFilters.le_gall_5_3,     # 1
    ...     wavelet_index_ho=WaveletFilters.le_gall_5_3,  # 1
    ...     dwt_depth=4,
    ...     dwt_depth_ho=0,
    ... )
    
    >>> from pprint import pprint
    >>> pprint(matrix)
    {0: {'LL': 4},
     1: {'HH': 0, 'HL': 2, 'LH': 2},
     2: {'HH': 2, 'HL': 4, 'LH': 4},
     3: {'HH': 3, 'HL': 5, 'LH': 5},
     4: {'HH': 5, 'HL': 7, 'LH': 7}}

.. tip::
    
    The :py:mod:`vc2_data_tables` module, used here, provides named constants
    for all of the VC-2 filter types.

The returned nested dictionary structure matches the layout used by the
``quant_matrix()`` VC-2 pseudocode function (12.4.5.3). For each transform
level, the outer dictionary contains an entry with an inner dictionary giving
the quantisation index offset for each orientation. Orientations are labelled
using the strings 'L', 'H', 'LL' 'LH', 'HL', and 'HH'.
