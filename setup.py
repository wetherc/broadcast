from setuptools import setup, find_packages
	
setup(
    name='Broadcast',
    version='0.0.0',
    packages=find_packages(),
    include_package_data=True,
    description='Add background effects to your webcam',
    author='Chris Wetherill',
    author_email='chris@tbmh.org',
    data_files=[('', ['LICENSE.txt'])],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=True)
