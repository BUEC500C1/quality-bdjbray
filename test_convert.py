import convert as cvt


def test_valid():								
	assert cvt.convert_to_roman(1) == 'I';

def test_valid2():
	assert cvt.convert_to_roman(3) == 'III';

def test_valid3():
	assert cvt.convert_to_roman(10) == 'X';

def test_valid4():
	assert cvt.convert_to_roman(34) == 'XXXIV';

def test_valid5():
	assert cvt.convert_to_roman(62) == 'LXII';

def test_valid6():
	assert cvt.convert_to_roman(110) == 'CX';

def test_valid7():
	assert cvt.convert_to_roman(156) == 'CLVI';

def test_valid8():
	assert cvt.convert_to_roman(185) == 'CLXXXV';

def test_valid9():
	assert cvt.convert_to_roman(675) == 'DCLXXV';

def test_valid10():
	assert cvt.convert_to_roman(2002) == 'MMII';

def test_valid11():
	assert cvt.convert_to_roman(3999) == 'MMMCMXCIX';

def test_valid12():
	assert cvt.convert_to_roman(5000) == "number out of range";

def test_valid13():
	assert cvt.convert_to_roman("abc") == "Please enter a number";

def test_valid14():
	assert cvt.convert_to_roman("!!!") == "Please enter a number";


