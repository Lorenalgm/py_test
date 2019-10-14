from google_driver import GoogleDriver

def test_requests():
	result = GoogleDriver().search('test')
	assert 200 == result.status_code
	assert "test" in str(result.content)
	
