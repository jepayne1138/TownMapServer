"""Calls the launch server function."""
import os
import sys
from townmapserver import server


required_configs = [
    ('address', 'HOST'),
    ('port', 'PORT'),
]


if __name__ == '__main__':
    try:
        server_args = {
            arg: os.environ[config_name]
            for arg, config_name in required_configs
        }
    except KeyError:
        print(
            'The following config setting are required: {}'.format(
                [config_name for _, config_name in required_configs]
            )
        )
        print('Set config values with the following command:')
        print('"heroku config:set {config1}={value1} {config2}={value2}"')
        sys.exit(-1)

    server.launch_server(**server_args)
