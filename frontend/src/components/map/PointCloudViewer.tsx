import { useEffect, useRef } from "react";
import * as THREE from "three";

interface PointCloudViewerProps {
  pointcloudUrl: string;
}

export function PointCloudViewer({ pointcloudUrl }: PointCloudViewerProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x1a1a2e);

    const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
    camera.position.set(5, 5, 5);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(containerRef.current.clientWidth, containerRef.current.clientHeight);
    containerRef.current.appendChild(renderer.domElement);

    // Grid helper
    scene.add(new THREE.GridHelper(10, 10));

    // Placeholder: load point cloud via Potree or custom loader later
    // For now, add an axis helper
    scene.add(new THREE.AxesHelper(3));

    const animate = () => {
      requestAnimationFrame(animate);
      renderer.render(scene, camera);
    };
    animate();

    return () => {
      renderer.dispose();
      containerRef.current?.removeChild(renderer.domElement);
    };
  }, [pointcloudUrl]);

  return (
    <div
      ref={containerRef}
      style={{ width: "100%", height: "100%", minHeight: 500 }}
    />
  );
}
