import { useEffect, useState } from "react";
import { listMaps, uploadMap } from "../services/api";
import type { MapInfo } from "../types";

export function Maps() {
  const [maps, setMaps] = useState<MapInfo[]>([]);

  const refresh = () => listMaps().then((r) => setMaps(r.data));
  useEffect(() => { refresh(); }, []);

  const handleUpload = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = e.currentTarget;
    const fileInput = form.file as HTMLInputElement;
    const name = (form.name as HTMLInputElement).value;
    if (!fileInput.files?.[0]) return;
    await uploadMap(name, fileInput.files[0]);
    refresh();
  };

  return (
    <div style={{ padding: 20 }}>
      <h1 style={{ color: "#fff" }}>地图管理</h1>

      <form onSubmit={handleUpload} style={{ marginBottom: 20, display: "flex", gap: 8 }}>
        <input name="name" placeholder="地图名称" required />
        <input name="file" type="file" accept=".pcd,.ply,.las" required />
        <button type="submit">上传</button>
      </form>

      <ul style={{ color: "#fff" }}>
        {maps.map((m) => (
          <li key={m.name}>{m.name}</li>
        ))}
      </ul>
    </div>
  );
}
