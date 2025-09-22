import logging
import os


def raise_if_default(key, value, default):
    """
    Raise a warning or an error if the config value is the default.
    """
    if value != default:
        return value

    env = os.environ.get("ENVIRONMENT", "PRODUCTION")
    match env:
        case "PRODUCTION":
            raise Exception(
                f"Using the default value for '{key}' is not allowed on production."
            )
        case "DEVELOPMENT":
            logging.warning(
                f"You are using the default value for '{key}'."
                " This is only allowed on development environments"
                " and should be changed for production."
            )
    return value
