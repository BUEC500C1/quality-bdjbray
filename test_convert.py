import convert as cvt

def test_valid():								
	assert cvt.convert(1) == 'I';
	assert cvt.convert(3) == 'III';
	assert cvt.convert(10) == 'X';
	assert cvt.convert(62) == 'LXII';
	assert cvt.convert(110) == 'CX';
	assert cvt.convert(185) == 'CLXXXV';
	assert cvt.convert(2002) == 'MMII';
	assert cvt.convert(6700) == 'MMMMMMDCC';