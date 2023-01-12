[![PyPI current version](https://img.shields.io/pypi/v/hikvision-isapi-cli.svg)](https://pypi.python.org/pypi/hikvision-isapi-cli)
[![Python Support](https://img.shields.io/pypi/pyversions/hikvision-isapi-cli.svg)](https://pypi.python.org/pypi/hikvision-isapi-cli)


# hikvision-isapi-cli
A client library for accessing Hikvision ISAPI

### OpenAPI Generator

```bash
rm -fr .history/;cd ..;openapi-python-client update --path hikvision-isapi-cli/openapi.json --custom-template-path=hikvision-isapi-cli/templates/ --config=hikvision-isapi-cli/.config.yaml;cd hikvision-isapi-cli
```

## Usage
First, create a client:

```python
from hikvision_isapi_cli import Client

client = Client(base_url="https://api.example.com", username="username", password="SuperSecretPassword")
```

Now call your endpoint and use your models:

```python
from hikvision_isapi_cli.models import MyDataModel
from hikvision_isapi_cli.api.my_tag import get_my_data_model
from hikvision_isapi_cli.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from hikvision_isapi_cli.models import MyDataModel
from hikvision_isapi_cli.api.my_tag import get_my_data_model
from hikvision_isapi_cli.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = Client(
    base_url="https://internal_api.example.com", 
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = Client(
    base_url="https://internal_api.example.com",  
    verify_ssl=False
)
```

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info.

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `hikvision_isapi_cli.api.default`

## Building / publishing this Client
This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
