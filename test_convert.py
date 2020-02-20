import convert as cvt

def test_valid():								
	assert cvt.convert_to_roman(1) == 'I';
	assert cvt.convert_to_roman(3) == 'III';
	assert cvt.convert_to_roman(10) == 'X';
	assert cvt.convert_to_roman(34) == 'XXXIV', '34'
	assert cvt.convert_to_roman(62) == 'LXII';
	assert cvt.convert_to_roman(110) == 'CX';
    assert cvt.convert_to_roman(156) == 'CLVI', '156'
    assert cvt.convert_to_roman(185) == 'CLXXXV';
    assert cvt.convert_to_roman(675) == 'DCLXXV', '675'
    assert cvt.convert_to_roman(2002) == 'MMII';
    assert cvt.convert_to_roman(3999) == 'MMMCMXCIX', '3999'