import unittest
import app

def test_hello_world():
	assert app.hello_world() == "cho tam!!!!!!!!", "Test Failed!"
	try:
		assert app.hello_world() == "mar nayan!!!!!!!!", "Test Failed Forward!"
	except AssertionError:
		print("OK: Failed intentionally!")
if __name__ == "__main__":
	test_hello_world()
	print("tests completed!")