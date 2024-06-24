![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# LUSID<sup>®</sup> Configuration Python SDK
This is the Python SDK for the Configuration API for [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology), a bi-temporal investment management data platform with portfolio accounting capabilities. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)


| branch | status |
| --- | --- |
| `main` |  ![PyPI](https://img.shields.io/pypi/v/lusid-configuration-sdk?color=blue)

## Installation

The PyPi package for the LUSID Configuration SDK can be installed using the following:

```
pip install lusid-configuration-sdk finbourne-sdk-utilities
```

## Usage

```
import lusid_configuration
from fbnsdkutilities import ApiClientFactory

scheduler_factory = ApiClientFactory(lusid_configuration, api_secrets_filename="/path/to/secrets.json")
sets_api = scheduler_factory.build(lusid_configuration.api.ConfigurationSetsApi)

sets_api.list_configuration_sets()
```
