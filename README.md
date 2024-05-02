# SantimPay Python API Package.
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/licenses/mit)
Unofficial Python SDK for [SantimPay](https://santimpay.com/)

## Introduction

This document provides a comprehensive guide to integrating and using the SantimPay Payment Gateway SDK in your application. Santimpay is a powerful payment gateway that supports various payment methods, facilitating seamless transactions for businesses. This SDK simplifies interaction with SantimPay’s API, enabling operations such as initiating payments, verifying transactions, and managing subaccounts.

## Installation

To use the SantimPay SDK in your project, you need to install it using pip, as it is a dependency for making HTTP requests it will also install `httpx` as a dependency.

```bash
pip install santimPay
```
## Usage
To begin using the SDK, import the `SantimPay` class from the module and instantiate it with your secret key.
``` python
from santimPay import SantimPay
# Replace Your_merchant_id with your mechant_id from santimpay api

# Replace your private key with your own private key by generating it

# Replace test wit boolian value - default = False
santim_pay = SantimPay('Your_merchant_id', 'Your_private_key', test=False)

```
### Making Payments
``` python

response = santim_pay.checkout.create(

)
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. After that free to contribute to this project. Please read the [CONTRIBUTING.md](https://github.com/nahom-d54/SantimPay/blob/main/CONTRIBUTING.md) file for more information.


## Run Locally

Clone the project

```bash
git clone https://github.com/nahom-d54/SantimPay.git
```

Go to the project directory

```bash
cd santimPay
```

Install dependencies

```bash
pip install -r requirements.txt
```

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
