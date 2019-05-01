from pathlib import Path

from revlibs.dicts import DictLoader


def load(config_path):
    return parse(load_connection_settings(config_path))


def load_connection_settings(directory):
    """ Retrieve connections from specified yaml."""
    loader = DictLoader.from_path(directory)
    return list(loader.directory())


def parse(config):
    configs = {}
    for section in config:
        for protocol in section.values():
            if not isinstance(protocol, str):
                for name, kwargs in protocol.items():
                    configs[name] = kwargs
    return configs
