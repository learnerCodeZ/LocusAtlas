import { Outlet, NavLink } from "react-router-dom";

const navItems = [
  { to: "/", label: "监控" },
  { to: "/devices", label: "设备" },
  { to: "/maps", label: "地图" },
];

export function Layout() {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <nav
        style={{
          width: 200,
          background: "#16213e",
          padding: "20px 0",
          display: "flex",
          flexDirection: "column",
          gap: 8,
        }}
      >
        <h2 style={{ color: "#e94560", textAlign: "center", margin: "0 0 20px" }}>
          LocusAtlas
        </h2>
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            style={({ isActive }) => ({
              display: "block",
              padding: "10px 20px",
              color: isActive ? "#e94560" : "#ccc",
              textDecoration: "none",
              background: isActive ? "#0f3460" : "transparent",
            })}
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
      <main style={{ flex: 1, overflow: "auto", background: "#1a1a2e" }}>
        <Outlet />
      </main>
    </div>
  );
}
