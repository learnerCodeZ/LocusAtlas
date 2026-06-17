import { useEffect, useState } from "react";
import { listDevices, registerDevice, deleteDevice } from "../services/api";
import type { Device } from "../types";

export function Devices() {
  const [devices, setDevices] = useState<Device[]>([]);

  const refresh = () => listDevices().then((r) => setDevices(r.data));
  useEffect(() => { refresh(); }, []);

  const handleAdd = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = new FormData(e.currentTarget);
    await registerDevice({
      id: form.get("id") as string,
      name: form.get("name") as string,
      type: form.get("type") as Device["type"],
    });
    refresh();
  };

  return (
    <div style={{ padding: 20 }}>
      <h1 style={{ color: "#fff" }}>设备管理</h1>

      <form onSubmit={handleAdd} style={{ marginBottom: 20, display: "flex", gap: 8 }}>
        <input name="id" placeholder="设备ID" required />
        <input name="name" placeholder="设备名称" required />
        <select name="type">
          <option value="hololens2">HoloLens2</option>
          <option value="kinect">Kinect</option>
        </select>
        <button type="submit">注册</button>
      </form>

      <table style={{ width: "100%", color: "#fff", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>ID</th><th>名称</th><th>类型</th><th>在线</th><th>操作</th>
          </tr>
        </thead>
        <tbody>
          {devices.map((d) => (
            <tr key={d.id}>
              <td>{d.id}</td>
              <td>{d.name}</td>
              <td>{d.type}</td>
              <td>{d.online ? "在线" : "离线"}</td>
              <td><button onClick={() => deleteDevice(d.id).then(refresh)}>删除</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
