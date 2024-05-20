# Class that manages how configuration is loaded.
from kedro.config import OmegaConfigLoader  # noqa: E402
from kedro_viz.integrations.kedro.sqlite_store import SQLiteStore
from pathlib import Path

CONFIG_LOADER_CLASS = OmegaConfigLoader
CONFIG_LOADER_ARGS = {
    "base_env": "base",
    "default_run_env": "local",
}
INSTALLED_PLUGINS = ["kedro_mlflow"]

SESSION_STORE_CLASS = SQLiteStore
SESSION_STORE_ARGS = {"path": str(Path(__file__).parents[2] / "data")}
