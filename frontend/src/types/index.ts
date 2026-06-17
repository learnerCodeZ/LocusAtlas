export interface Device {
  id: string;
  name: string;
  type: "hololens2" | "kinect" | "other";
  token: string;
  online: boolean;
}

export interface Pose {
  device_id: string;
  position: [number, number, number];
  orientation: [number, number, number, number];
  timestamp: number;
}

export interface MapInfo {
  name: string;
}

export interface MatchResult {
  device_id: string;
  position: [number, number, number];
  orientation: [number, number, number, number];
  fitness: number;
  rmse: number;
}

export interface RelativePosition {
  from: string;
  to: string;
  offset: [number, number, number];
  distance: number;
}
