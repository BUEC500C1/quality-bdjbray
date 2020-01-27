import convert as cvt

def test_valid():								
	assert cvt.arabic2roman(1) == 'I';
	assert cvt.arabic2roman(3) == 'III';
	assert cvt.arabic2roman(10) == 'X';
	assert cvt.arabic2roman(62) == 'LXII';
	assert cvt.arabic2roman(110) == 'CX';
	assert cvt.arabic2roman(185) == 'CLXXXV';
	assert cvt.arabic2roman(2002) == 'MMII';
	assert cvt.arabic2roman(6700) == 'MMMMMMDCC';