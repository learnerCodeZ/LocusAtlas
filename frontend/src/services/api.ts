import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1",
});

// Devices
export const listDevices = () => api.get<Device[]>("/devices");
export const registerDevice = (data: Omit<Device, "token" | "online">) =>
  api.post<Device>("/devices/", data);
export const getDevice = (id: string) => api.get<Device>(`/devices/${id}`);
export const deleteDevice = (id: string) => api.delete(`/devices/${id}`);

// Maps
export const listMaps = () => api.get<MapInfo[]>("/maps");
export const uploadMap = (name: string, file: File) => {
  const form = new FormData();
  form.append("name", name);
  form.append("file", file);
  return api.post("/maps/upload", form);
};

// Localization
export const getPose = (deviceId: string) => api.get<Pose>(`/localization/pose/${deviceId}`);
export const getAllPoses = () => api.get<Record<string, Pose>>("/localization/poses");
export const getRelativePosition = (a: string, b: string) =>
  api.get<RelativePosition>(`/localization/relative/${a}/${b}`);

// Types re-export
import type { Device, Pose, MapInfo, MatchResult, RelativePosition } from "../types";
