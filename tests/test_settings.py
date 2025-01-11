import sys
from pathlib import Path
from zoneinfo import ZoneInfo

from edc_test_settings.default_test_settings import DefaultTestSettings

utc = ZoneInfo("UTC")

app_name = "edc_analytics"
base_dir = Path(__file__).absolute().parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    DEBUG=True,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=base_dir / "etc",
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "edc_analytics.apps.AppConfig",
    ],
).settings


for k, v in project_settings.items():
    setattr(sys.modules[__name__], k, v)
