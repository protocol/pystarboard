# PyStarboard

Python interface for querying starboard for Filecoin statistics, via Spacescope.


## Prerequisites
Check the `setup.py` script for dependencies.

## Installing

This package can be installed from source by cloning this repository and installing it manually with the command:

```
python setup.py install
```

## Setup for Data Access
`pystarboard` is a convenient interface for pulling data from Spacescope. Spacescope requires users to register for a unique token in order to request the historical data. Thus, each user of `pystarboard` needs to register for a unique token to enable data access - this is a prerequisite to use `pystarboard`.  

### Steps:
1. Follow the instructions [here](https://spacescope.io/sign/up/email) to get your own unique bearer token for data access.
2. Store your token in a json configuration file with the key `auth_key`.  An example is:
```json
{
    "auth_key": "Bearer ghp_xJtTSVcNRJINLWMmfDangcIFCjqPUNZenoVe"
}
```

## Usage
You will need to ensure that you setup your data access properly by running the following code
```python
import pystarboard.data as data
path_to_auth_cfg="<UPDATE ME>"
data.setup_spacecope(path_to_auth_cfg)
```

## See also

* [mechaFIL](https://github.com/protocol/filecoin-mecha-twin)
* [mechafil-jax](https://github.com/protocol/mechafil-jax)
