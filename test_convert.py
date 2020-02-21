import convert as cvt

def test_valid():								
	assert cvt.convert_to_roman(1) == 'I';
	assert cvt.convert_to_roman(3) == 'III';
	assert cvt.convert_to_roman(10) == 'X';
	assert cvt.convert_to_roman(34) == 'XXXIV';
	assert cvt.convert_to_roman(62) == 'LXII';
	assert cvt.convert_to_roman(110) == 'CX';
	assert cvt.convert_to_roman(156) == 'CLVI';
	assert cvt.convert_to_roman(185) == 'CLXXXV';
	assert cvt.convert_to_roman(675) == 'DCLXXV';
	assert cvt.convert_to_roman(2002) == 'MMII';
	assert cvt.convert_to_roman(3999) == 'MMMCMXCIX';
	assert cvt.convert_to_roman(5000) =='out of range';
	assert cvt.convert_to_roman('!!!')=='please enter a number';
	assert cvt.convert_to_roman('abc')=='please enter a number';