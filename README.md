<h1 align='center'>
    Viaducts
</h1>
<h4 align='center'>
    Database connections via ducts.
</h4>

See [omniduct documentation](http://omniduct.readthedocs.io) for more information.

## Install

**Please note:** This is still in development.

Installing dependency branch

```
pip install git+git://github.com/foxyblue/omniduct.git@56d64e4dc2ce3cf098e47fa88cbec73931e6a38a
pip install viaducts
```

## Usage

```python
from viaducts import Viaducts

viaducts = Viaducts()

exasol = viaducts['exasol']
exasol.query("SELECT 43;", format='pandas')
```

### Example Config

```yaml
databases:
  black:
    protocol: postgresql
    host: localhost
    port: 5432
    username: postgres
    password: _env:BLACK_DB_PW
  exasol:
    protocol: exasol
    host:
      - 'localhost:8563'
    username: _env:EXASOL_USER
    password: _env:EXASOL_PASSWORD
    schema: _env:EXASOL_SCHEMA

filesystems:
  local:
    protocol: localfs
    global_writes: True
  s3_company_bucket:
    protocol: s3
    bucket: company-bucket
```

## Supported extensions:

- [X] Support for environment variable extraction, this includes requiring password to be set in env.
- [X] Configuration can be set in multiple `yaml` files.
- [X] Added support for exasol ([Open in PR](https://github.com/airbnb/omniduct/pull/99))
- [ ] Connecting to multiple hosts.

## Omniducts supports

- [X] Failover.
