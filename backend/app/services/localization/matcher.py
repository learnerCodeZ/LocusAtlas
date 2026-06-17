import open3d as o3d
import numpy as np
from app.core.config import settings
from app.services.localization.pose_manager import update_pose


def match_pointcloud(map_name: str, fragment_path: str) -> dict | None:
    """ICP matching: align fragment to global map, return pose."""
    from pathlib import Path

    map_dir = Path(settings.map_storage_path) / map_name
    map_files = list(map_dir.glob("*_processed.pcd"))
    if not map_files:
        return None

    map_pcd = o3d.io.read_point_cloud(str(map_files[0]))
    fragment_pcd = o3d.io.read_point_cloud(fragment_path)

    # Downsample fragment
    fragment_pcd = fragment_pcd.voxel_down_sample(0.05)
    fragment_pcd.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)
    )

    # ICP registration
    result = o3d.pipelines.registration.registration_icp(
        source=fragment_pcd,
        target=map_pcd,
        max_correspondence_distance=settings.localization.icp_max_distance,
        init=np.eye(4),
        estimation_method=o3d.pipelines.registration.TransformationEstimationPointToPlane(),
        criteria=o3d.pipelines.registration.ICPConvergenceCriteria(
            max_iteration=settings.localization.icp_max_iteration
        ),
    )

    if not result.fitness > 0.3:
        return None

    T = result.transformation
    position = T[:3, 3].tolist()
    # Extract rotation as quaternion
    from scipy.spatial.transform import Rotation
    orientation = Rotation.from_matrix(T[:3, :3]).as_quat().tolist()  # [qx, qy, qz, qw]

    return {
        "position": position,
        "orientation": orientation,
        "fitness": result.fitness,
        "rmse": result.inlier_rmse,
        "transformation": T.tolist(),
    }
