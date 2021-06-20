import logging

import xdg.BaseDirectory
import yaml

logger = logging.getLogger(
    __name__,
)


def load_profiles(
    ):
    config_dir = xdg.BaseDirectory.save_config_path(
        'twecs',
    )
    path = f'{config_dir}/profiles.yaml'

    try:
        f = open(
            path,
            'r',
        )
    except OSError:
        logger.critical(
            'profiles file (%s) could not be opened',
            path,
        )
    else:
        logger.debug(
            'profiles file (%s) opened successfully',
            path,
        )

        profiles = yaml.safe_load(
            f,
        )

        logger.debug(
            'profiles loaded successfully',
        )

        return profiles
