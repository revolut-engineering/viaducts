import os
from pathlib import Path

from omniduct import DuctRegistry

import configuration


_DEFAULT_DIRECTORY = Path.home() / ".revconnect/"
_PASSWORD_REQUIRED = (
    # Provide a meaningful message
    "Please ensure you have set the password as an environment variable"
)


class Viaducts:
    def __init__(self, **options):
        #: path, is set to a default path '.revconnect/' or passed in by
        # the variable ``config_path`` in options.
        path = Path(options.get("config_path", _DEFAULT_DIRECTORY))

        self.configurations = configuration.load(config_path=path)
        self.registry = DuctRegistry()

    def __getitem__(self, name):
        if name in self.registry:
            return self.registry[name]

        elif name in self.configurations:
            config = self.configurations[name]

            if not config.get("disabled", False):
                for k, v in config.items():
                    config[k] = parse_value(k, v)
                self.registry.register_from_config({name: config})
                return self.registry[name]

        raise KeyError("Configuration not found.")


def parse_value(key, value):
    """ Attempt to retrieve item from dict.
    Can also get the item from environment,
    and return a default if not set.
    """
    #: ensure password has been set as an environment variable
    if key == "password":
        var_split = value.split(":", 2)
        try:
            env_name = var_split[1]
            return os.environ[env_name]
        except (KeyError, IndexError):
            raise KeyError(_PASSWORD_REQUIRED)

    if isinstance(value, str) and value.startswith("_env"):
        var_split = value.split(":", 2)
        var_name = var_split[1]
        var_default = "" if len(var_split) < 3 else var_split[2]
        value = os.environ.get(var_name, var_default)
    return value
