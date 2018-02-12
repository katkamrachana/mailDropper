from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()
setup(
    name='mailDropper',
    version='1.0.1',
    author='katkamrachana',
    author_email='katkam.rachana@gmail.com',
    license='AGPL',
    long_description=readme(),
    include_package_data=True,
    packages=["mailDropper"],
    scripts=["mailDropper/sendmail.py"],
    keywords=["email", "bulk", "custom"],
    url='https://github.com/katkamrachana/mailDropper',
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
