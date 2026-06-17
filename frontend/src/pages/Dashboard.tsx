import { useEffect, useState } from "react";
import { PointCloudViewer } from "../components/map/PointCloudViewer";
import { DeviceMarker } from "../components/devices/DeviceMarker";
import { usePoseStream } from "../hooks/usePoseStream";
import { getAllPoses } from "../services/api";
import type { Pose } from "../types";

export function Dashboard() {
  const [poses, setPoses] = useState<Record<string, Pose>>({});
  const { subscribe } = usePoseStream();

  useEffect(() => {
    getAllPoses().then((res) => setPoses(res.data));
    const unsub = subscribe((pose: Pose) =>
      setPoses((prev) => ({ ...prev, [pose.device_id]: pose }))
    );
    return unsub;
  }, []);

  return (
    <div style={{ padding: 20, height: "100%", display: "flex", flexDirection: "column" }}>
      <h1 style={{ color: "#fff" }}>实时监控</h1>
      <div style={{ flex: 1, position: "relative" }}>
        <PointCloudViewer pointcloudUrl="" />
        <div
          style={{
            position: "absolute",
            top: 10,
            right: 10,
            background: "rgba(0,0,0,0.7)",
            padding: 10,
            borderRadius: 8,
          }}
        >
          {Object.values(poses).map((p) => (
            <DeviceMarker key={p.device_id} pose={p} />
          ))}
        </div>
      </div>
    </div>
  );
}
