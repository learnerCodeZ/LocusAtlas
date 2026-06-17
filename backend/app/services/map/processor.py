import open3d as o3d
import numpy as np
from app.core.config import settings


def preprocess_pointcloud(input_path: str, voxel_size: float = 0.05) -> dict:
    """去噪 → 下采样 → 体素化"""
    pcd = o3d.io.read_point_cloud(input_path)
    points_original = len(pcd.points)

    # Statistical outlier removal
    pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

    # Voxel downsampling
    pcd = pcd.voxel_down_sample(voxel_size)

    # Estimate normals (needed for ICP)
    pcd.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 2, max_nn=30)
    )

    output_path = input_path.rsplit(".", 1)[0] + "_processed.pcd"
    o3d.io.write_point_cloud(output_path, pcd)

    return {
        "output_path": output_path,
        "points_original": points_original,
        "points_processed": len(pcd.points),
    }
