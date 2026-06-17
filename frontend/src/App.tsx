import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Layout } from "./components/layout/Layout";
import { Dashboard } from "./pages/Dashboard";
import { Devices } from "./pages/Devices";
import { Maps } from "./pages/Maps";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/devices" element={<Devices />} />
          <Route path="/maps" element={<Maps />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
