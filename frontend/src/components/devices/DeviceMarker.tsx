import { useState, useEffect } from "react";
import * as api from "../../services/api";
import type { Pose } from "../../types";
import { usePoseStream } from "../../hooks/usePoseStream";

export function DeviceMarker({ pose }: { pose: Pose }) {
  const typeIcon = pose.device_id.includes("hl2") ? "🧑" : "🤖";
  return (
    <div style={{ textAlign: "center", color: "#fff", fontSize: 12 }}>
      <div style={{ fontSize: 24 }}>{typeIcon}</div>
      <div>{pose.device_id}</div>
    </div>
  );
}
