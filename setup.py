from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'SantimPay Unofficial package'
LONG_DESCRIPTION = ''
with open('README.md', 'r') as r:
    LONG_DESCRIPTION = r.read()

setup(
    name='santimPay',
    version=VERSION,
    author='Nahom Dereje',
    license='MIT',
    author_email='dev@nahom.eu.org',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/nahom-d54/SantimPay.git",
    install_requires=[
        "PyJWT==2.8.0",
        "httpx==0.27.0"
    ],
    keywords=['SantimPay', "Python", "PaymentGateway", "EthiopiaPaymentGateway"],
    classifiers= [
                "Development Status :: 3 - Alpha",
                "Intended Audience :: Education",
                "Programming Language :: Python :: 3",
                "Operating System :: MacOS :: MacOS X",
                "Operating System :: Microsoft :: Windows"
            ]
)
