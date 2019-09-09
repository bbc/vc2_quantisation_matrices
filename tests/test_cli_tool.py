import pytest

import shlex

from collections import OrderedDict

from vc2_data_tables import WaveletFilters, QUANTISATION_MATRICES

from vc2_quantisation_matrices.cli_tool import (
    parse_wavelet_identifier,
    format_quantisation_matrix,
    main,
)


@pytest.mark.parametrize("ident,exp_index", [
    ("3", WaveletFilters.haar_no_shift),
    ("haar_no_shift", WaveletFilters.haar_no_shift),
])
def test_parse_wavelet_identifier(ident, exp_index):
    assert parse_wavelet_identifier(ident) is exp_index


def test_format_quantisaton_matrix():
    assert format_quantisation_matrix(OrderedDict([
        (1, OrderedDict([("H", 1)])),
        (0, OrderedDict([("L", 0)])),
        (2, OrderedDict([("LL", 2)])),
        (3, OrderedDict([("HL", 3), ("HH", 5), ("LH", 40)])),
    ])) == (
        "Level 0: L:  0\n"
        "Level 1: H:  1\n"
        "Level 2: LL:  2\n"
        "Level 3: HL:  3, LH: 40, HH:  5"
    )


@pytest.mark.parametrize("args", [
    # Missing wavelet and depth
    "",
    # Missing depth
    "-w 1",
    # Missing wavelet
    "-d 1",
    # Missing non-ho wavelet or depth
    "-W 1 -d 1",
    "-w 1 -D 1",
    # Unknown wavelet
    "-w 100 -d 1",
    "-w foobar -d 1",
    "-w 1 -W 100 -d 1",
    "-w 1 -W foobar -d 1",
    # Out-of-range depth
    "-w 1 -d -10",
    "-w 1 -d 0 -D -10",
])
def test_bad_arguments(args):
    with pytest.raises(SystemExit):
        main(shlex.split(args))


@pytest.mark.parametrize("args", [
    "-w 3 -d 4",
    "-w haar_no_shift -d 4",
])
def test_default_argument_values_work(args, capsys):
    assert main(shlex.split(args)) == 0
    
    out, err = capsys.readouterr()
    
    assert out == "{}\n".format(format_quantisation_matrix(
        QUANTISATION_MATRICES[(
            WaveletFilters.haar_no_shift,
            WaveletFilters.haar_no_shift,
            4,
            0,
        )]
    ))
    assert err == ""


def test_all_arguments_work(capsys):
    assert main(shlex.split("-w 3 -W 1 -d 2 -D 1")) == 0
    
    out, err = capsys.readouterr()
    
    assert out == "{}\n".format(format_quantisation_matrix(
        QUANTISATION_MATRICES[(
            WaveletFilters.haar_no_shift,
            WaveletFilters.le_gall_5_3,
            2,
            1,
        )]
    ))
    assert err == ""
