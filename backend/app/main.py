from app.api import Api
from dynaconf import Dynaconf

settings = Dynaconf(
        envvar_prefix="DYNACONF",
        settings_files=['../config/settings.toml', '../config/.secrets.toml'],
    ) 
api = Api(settings)
app = api.app