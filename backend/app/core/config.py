from pydantic_settings import BaseSettings
from pathlib import Path


class LocalizationSettings(BaseSettings):
    icp_max_distance: float = 0.5
    icp_max_iteration: int = 30
    kinect_match_interval_min: float = 5.0
    kinect_match_interval_max: float = 30.0
    hololens_calibration_interval: float = 10.0


class Settings(BaseSettings):
    app_name: str = "LocusAtlas"
    version: str = "0.1.0"
    debug: bool = True

    host: str = "0.0.0.0"
    port: int = 8000

    database_url: str = "sqlite+aiosqlite:///./data/locusatlas.db"

    map_storage_path: Path = Path("./data/maps")
    pointcloud_upload_path: Path = Path("./data/uploads")

    auth_secret: str = "locusatlas-dev-secret"
    auth_token_expire_hours: int = 0  # 0 = never expire (static token for MVP)

    localization: LocalizationSettings = LocalizationSettings()

    model_config = {"env_prefix": "LOCUS_", "env_file": ".env"}
