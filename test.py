from .tasty import istasty

def test_tasty():
	for i in ['sweetapple', 'Sweetsugar', 'SWEETMANGO']:
		assert istasty(i) == 'Yes'
