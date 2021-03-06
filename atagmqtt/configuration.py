"""Configuration module."""
from pydantic import BaseSettings, Field
import homie
import atagmqtt

class Settings(BaseSettings):
    """Application settings for the ATAG ONE MQTT bridge."""

    hostname: str = Field('atagmqtt', env='HOSTNAME')
    loglevel: str = Field('INFO', env='LOGLEVEL')

    atag_update_interval: int = Field(30, env='ATAG_UPDATE_INTERVAL')
    atag_host: str = Field(None, env='ATAG_HOST')
    atag_paired: bool = Field(False, env='ATAG_PAIRED')

    mqtt_host: str = Field(None, env='MQTT_HOST')
    mqtt_port: int = Field(1883, env='MQTT_PORT')
    mqtt_username: str = Field(None, env='MQTT_USERNAME')
    mqtt_password: str = Field(None, env='MQTT_PASSWORD')

    homie_update_interval: int = 60
    homie_topic: str = Field('homie', env='HOMIE_TOPIC')
    homie_implementation: str \
        = f"Atag One Homie {atagmqtt.__version__} Homie 3 Version {homie.__version__}"
    homie_fw_name: str = "AtagOne"
    homie_fw_version: str = "0.1.0"

    class Config:
        """Where to find the environment file containing the settings."""

        env_file = '.env'
