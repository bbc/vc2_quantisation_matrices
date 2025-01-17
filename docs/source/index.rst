``vc2_quantisation_matrices``
=============================

The :py:mod:`vc2_quantisation_matrices` package, provides both a standalone
software tool and Python module for computing 'default' quantisation matrices
for the SMPTE ST 2042-1 `VC-2 professional video codec
<https://www.bbc.co.uk/rd/projects/vc-2>`_. Specifically, this software
implements the procedure from section (D.3.2) for computing quantisation
matrices which achieve noise-power normalisation.

You can find the source code for :py:mod:`vc2_quantisation_matrices` `on GitHub
<https://github.com/bbc/vc2_quantisation_matrices/>`_.

.. only:: not latex

    .. note::
    
        This documentation is also `available in PDF format
        <https://bbc.github.io/vc2_quantisation_matrices/vc2_quantisation_matrices_manual.pdf>`_.

.. only:: not html

    .. note::
    
        This documentation is also `available to browse online in HTML format
        <https://bbc.github.io/vc2_quantisation_matrices/>`_.

.. toctree::
   :hidden:

   bibliography.rst


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   cli
   api
   implementation
