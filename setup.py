from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'SantimPay Unofficial package'
LONG_DESCRIPTION = 'Santim pay python package which is directly made from the php laravel package https://github.com/ba5liel/santimpay-laravel/tree/main'

setup(
    name='santimPay',
    version=VERSION,
    author='Nahom Dereje',
    author_email='dev@nahom.eu.org',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
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
