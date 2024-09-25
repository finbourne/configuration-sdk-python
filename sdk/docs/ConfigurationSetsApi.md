# lusid_configuration.ConfigurationSetsApi

All URIs are relative to *https://fbn-prd.lusid.com/configuration*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_configuration_to_set**](ConfigurationSetsApi.md#add_configuration_to_set) | **POST** /api/sets/{type}/{scope}/{code}/items | [EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set
[**check_access_token_exists**](ConfigurationSetsApi.md#check_access_token_exists) | **HEAD** /api/sets/personal/me | [DEPRECATED] CheckAccessTokenExists: Check the Personal Access Token exists for the current user
[**create_configuration_set**](ConfigurationSetsApi.md#create_configuration_set) | **POST** /api/sets | [EARLY ACCESS] CreateConfigurationSet: Create a configuration set
[**delete_access_token**](ConfigurationSetsApi.md#delete_access_token) | **DELETE** /api/sets/personal/me | [DEPRECATED] DeleteAccessToken: Delete any stored Personal Access Token for the current user
[**delete_configuration_item**](ConfigurationSetsApi.md#delete_configuration_item) | **DELETE** /api/sets/{type}/{scope}/{code}/items/{key} | [EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set
[**delete_configuration_set**](ConfigurationSetsApi.md#delete_configuration_set) | **DELETE** /api/sets/{type}/{scope}/{code} | [EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items
[**generate_access_token**](ConfigurationSetsApi.md#generate_access_token) | **PUT** /api/sets/personal/me | [DEPRECATED] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token
[**get_configuration_item**](ConfigurationSetsApi.md#get_configuration_item) | **GET** /api/sets/{type}/{scope}/{code}/items/{key} | GetConfigurationItem: Get the specific configuration item within an existing set
[**get_configuration_set**](ConfigurationSetsApi.md#get_configuration_set) | **GET** /api/sets/{type}/{scope}/{code} | GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed
[**get_system_configuration_items**](ConfigurationSetsApi.md#get_system_configuration_items) | **GET** /api/sets/system/{code}/items/{key} | [EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set  All users have access to this endpoint
[**get_system_configuration_sets**](ConfigurationSetsApi.md#get_system_configuration_sets) | **GET** /api/sets/system/{code} | GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed  All users have access to this endpoint
[**list_configuration_sets**](ConfigurationSetsApi.md#list_configuration_sets) | **GET** /api/sets | [EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)
[**update_configuration_item**](ConfigurationSetsApi.md#update_configuration_item) | **PUT** /api/sets/{type}/{scope}/{code}/items/{key} | [EARLY ACCESS] UpdateConfigurationItem: Update a configuration item&#39;s value and/or description
[**update_configuration_set**](ConfigurationSetsApi.md#update_configuration_set) | **PUT** /api/sets/{type}/{scope}/{code} | [EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set


# **add_configuration_to_set**
> ConfigurationSet add_configuration_to_set(type, scope, code, create_configuration_item, user_id=user_id)

[EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared
        scope = 'scope_example' # str | The scope that identifies a configuration set
        code = 'code_example' # str | The code that identifies a configuration set

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_configuration_item = CreateConfigurationItem()
        # create_configuration_item = CreateConfigurationItem.from_json("")
        create_configuration_item = CreateConfigurationItem.from_dict({"key":"password","value":"a super secret password","valueType":"text","isSecret":false,"description":"Password for System A","blockReveal":false}) # CreateConfigurationItem | The data to create a configuration item
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.add_configuration_to_set(type, scope, code, create_configuration_item, user_id=user_id, opts=opts)

            # [EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set
            api_response = await api_instance.add_configuration_to_set(type, scope, code, create_configuration_item, user_id=user_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->add_configuration_to_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **create_configuration_item** | [**CreateConfigurationItem**](CreateConfigurationItem.md)| The data to create a configuration item | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **check_access_token_exists**
> check_access_token_exists()

[DEPRECATED] CheckAccessTokenExists: Check the Personal Access Token exists for the current user

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.check_access_token_exists(opts=opts)

            # [DEPRECATED] CheckAccessTokenExists: Check the Personal Access Token exists for the current user
            await api_instance.check_access_token_exists()        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->check_access_token_exists: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Personal Access Token exists |  -  |
**404** | The Personal Access Token does not exist |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_configuration_set**
> ConfigurationSet create_configuration_set(create_configuration_set, user_id=user_id)

[EARLY ACCESS] CreateConfigurationSet: Create a configuration set

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_configuration_set = CreateConfigurationSet()
        # create_configuration_set = CreateConfigurationSet.from_json("")
        create_configuration_set = CreateConfigurationSet.from_dict({"id":{"scope":"official","code":"system-a-config"},"type":"shared","description":"All the config related to System A"}) # CreateConfigurationSet | The data to create a configuration set
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_configuration_set(create_configuration_set, user_id=user_id, opts=opts)

            # [EARLY ACCESS] CreateConfigurationSet: Create a configuration set
            api_response = await api_instance.create_configuration_set(create_configuration_set, user_id=user_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->create_configuration_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_configuration_set** | [**CreateConfigurationSet**](CreateConfigurationSet.md)| The data to create a configuration set | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_access_token**
> delete_access_token()

[DEPRECATED] DeleteAccessToken: Delete any stored Personal Access Token for the current user

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.delete_access_token(opts=opts)

            # [DEPRECATED] DeleteAccessToken: Delete any stored Personal Access Token for the current user
            await api_instance.delete_access_token()        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->delete_access_token: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_configuration_item**
> delete_configuration_item(type, scope, code, key, user_id=user_id)

[EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared
        scope = 'scope_example' # str | The scope that identifies a configuration set
        code = 'code_example' # str | The code that identifies a configuration set
        key = 'key_example' # str | The key that identifies a configuration item
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.delete_configuration_item(type, scope, code, key, user_id=user_id, opts=opts)

            # [EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set
            await api_instance.delete_configuration_item(type, scope, code, key, user_id=user_id)        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->delete_configuration_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **key** | **str**| The key that identifies a configuration item | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_configuration_set**
> delete_configuration_set(type, scope, code, user_id=user_id)

[EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared
        scope = 'scope_example' # str | The scope that identifies a configuration set
        code = 'code_example' # str | The code that identifies a configuration set
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.delete_configuration_set(type, scope, code, user_id=user_id, opts=opts)

            # [EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items
            await api_instance.delete_configuration_set(type, scope, code, user_id=user_id)        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->delete_configuration_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **generate_access_token**
> PersonalAccessToken generate_access_token(action=action)

[DEPRECATED] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        action = 'action_example' # str | action=regenerate = Even if an existing parameter exists, forcibly regenerate a new one (deleting the old)  action=ensure = If no parameter exists, create one. If one does already exist, verify that it is still valid (call a service?), and if so, return it. If it is not still valid, then regenerate a new one.  action=default = If a parameter exists, return it. If not then create one. If this parameter is not provided, this is the default behaviour. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.generate_access_token(action=action, opts=opts)

            # [DEPRECATED] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token
            api_response = await api_instance.generate_access_token(action=action)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->generate_access_token: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| action&#x3D;regenerate &#x3D; Even if an existing parameter exists, forcibly regenerate a new one (deleting the old)  action&#x3D;ensure &#x3D; If no parameter exists, create one. If one does already exist, verify that it is still valid (call a service?), and if so, return it. If it is not still valid, then regenerate a new one.  action&#x3D;default &#x3D; If a parameter exists, return it. If not then create one. If this parameter is not provided, this is the default behaviour. | [optional] 

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_configuration_item**
> ConfigurationItem get_configuration_item(type, scope, code, key, reveal=reveal, user_id=user_id)

GetConfigurationItem: Get the specific configuration item within an existing set

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared
        scope = 'scope_example' # str | The scope that identifies a configuration set
        code = 'code_example' # str | The code that identifies a configuration set
        key = 'key_example' # str | The key that identifies a configuration item
        reveal = True # bool | Whether to reveal the secrets. This is only available when the userId query setting has not been specified. (optional)
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_configuration_item(type, scope, code, key, reveal=reveal, user_id=user_id, opts=opts)

            # GetConfigurationItem: Get the specific configuration item within an existing set
            api_response = await api_instance.get_configuration_item(type, scope, code, key, reveal=reveal, user_id=user_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->get_configuration_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **key** | **str**| The key that identifies a configuration item | 
 **reveal** | **bool**| Whether to reveal the secrets. This is only available when the userId query setting has not been specified. | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationItem**](ConfigurationItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_configuration_set**
> ConfigurationSet get_configuration_set(type, scope, code, reveal=reveal, user_id=user_id)

GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared
        scope = 'scope_example' # str | The scope that identifies a configuration set
        code = 'code_example' # str | The code that identifies a configuration set
        reveal = True # bool | Whether to reveal the secrets. This is only available when the userId query setting has not been specified. (optional)
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_configuration_set(type, scope, code, reveal=reveal, user_id=user_id, opts=opts)

            # GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed
            api_response = await api_instance.get_configuration_set(type, scope, code, reveal=reveal, user_id=user_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->get_configuration_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **reveal** | **bool**| Whether to reveal the secrets. This is only available when the userId query setting has not been specified. | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_system_configuration_items**
> ResourceListOfConfigurationItem get_system_configuration_items(code, key, reveal=reveal)

[EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set  All users have access to this endpoint

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        code = 'code_example' # str | The code that identifies a system configuration set
        key = 'key_example' # str | The key that identifies a system configuration item
        reveal = True # bool | Whether to reveal the secrets (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_system_configuration_items(code, key, reveal=reveal, opts=opts)

            # [EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set  All users have access to this endpoint
            api_response = await api_instance.get_system_configuration_items(code, key, reveal=reveal)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->get_system_configuration_items: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code that identifies a system configuration set | 
 **key** | **str**| The key that identifies a system configuration item | 
 **reveal** | **bool**| Whether to reveal the secrets | [optional] 

### Return type

[**ResourceListOfConfigurationItem**](ResourceListOfConfigurationItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No system configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_system_configuration_sets**
> ResourceListOfConfigurationSet get_system_configuration_sets(code, reveal=reveal)

GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed  All users have access to this endpoint

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        code = 'code_example' # str | The code that identifies a system configuration set
        reveal = True # bool | Whether to reveal the secrets (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_system_configuration_sets(code, reveal=reveal, opts=opts)

            # GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed  All users have access to this endpoint
            api_response = await api_instance.get_system_configuration_sets(code, reveal=reveal)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->get_system_configuration_sets: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code that identifies a system configuration set | 
 **reveal** | **bool**| Whether to reveal the secrets | [optional] 

### Return type

[**ResourceListOfConfigurationSet**](ResourceListOfConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No system configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_configuration_sets**
> ResourceListOfConfigurationSetSummary list_configuration_sets(type=type, user_id=user_id)

[EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared (optional)
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_configuration_sets(type=type, user_id=user_id, opts=opts)

            # [EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)
            api_response = await api_instance.list_configuration_sets(type=type, user_id=user_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->list_configuration_sets: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ResourceListOfConfigurationSetSummary**](ResourceListOfConfigurationSetSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_configuration_item**
> ConfigurationItem update_configuration_item(type, scope, code, key, update_configuration_item, user_id=user_id)

[EARLY ACCESS] UpdateConfigurationItem: Update a configuration item's value and/or description

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared
        scope = 'scope_example' # str | The scope that identifies a configuration set
        code = 'code_example' # str | The code that identifies a configuration set
        key = 'key_example' # str | The key that identifies a configuration item

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_configuration_item = UpdateConfigurationItem()
        # update_configuration_item = UpdateConfigurationItem.from_json("")
        update_configuration_item = UpdateConfigurationItem.from_dict({"value":"updated password","description":"Password for system A and B","blockReveal":false}) # UpdateConfigurationItem | The data to update a configuration item
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_configuration_item(type, scope, code, key, update_configuration_item, user_id=user_id, opts=opts)

            # [EARLY ACCESS] UpdateConfigurationItem: Update a configuration item's value and/or description
            api_response = await api_instance.update_configuration_item(type, scope, code, key, update_configuration_item, user_id=user_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->update_configuration_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **key** | **str**| The key that identifies a configuration item | 
 **update_configuration_item** | [**UpdateConfigurationItem**](UpdateConfigurationItem.md)| The data to update a configuration item | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationItem**](ConfigurationItem.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_configuration_set**
> ConfigurationSet update_configuration_set(type, scope, code, update_configuration_set, user_id=user_id)

[EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set

### Example

```python
import asyncio
from lusid_configuration.exceptions import ApiException
from lusid_configuration.extensions.configuration_options import ConfigurationOptions
from lusid_configuration.models import *
from pprint import pprint
from lusid_configuration import (
    ApiClientFactory,
    ConfigurationSetsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "configurationUrl":"https://<your-domain>.lusid.com/configuration",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid_configuration ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ConfigurationSetsApi)
        type = 'type_example' # str | Whether the configuration set is Personal or Shared
        scope = 'scope_example' # str | The scope that identifies a configuration set
        code = 'code_example' # str | The code that identifies a configuration set

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_configuration_set = UpdateConfigurationSet()
        # update_configuration_set = UpdateConfigurationSet.from_json("")
        update_configuration_set = UpdateConfigurationSet.from_dict({"description":"The group of configurations related to System A and B"}) # UpdateConfigurationSet | The data to update a configuration set
        user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_configuration_set(type, scope, code, update_configuration_set, user_id=user_id, opts=opts)

            # [EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set
            api_response = await api_instance.update_configuration_set(type, scope, code, update_configuration_set, user_id=user_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ConfigurationSetsApi->update_configuration_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **update_configuration_set** | [**UpdateConfigurationSet**](UpdateConfigurationSet.md)| The data to update a configuration set | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

