from setuptools import setup
setup(
    name='mailDropper',
    version='1.0.1',
	author='katkamrachana',
	author_email='katkam.rachana@gmail.com',
	license='AGPL',
	include_package_data=True,
	packages=["mailDropper"],
	scripts=["mailDropper/sendmail.py"],
	keywords=["email", "bulk", "custom"],
	url='https://github.com/katkamrachana/mailDropper'
)
