export function usePoseStream() {
  const wsUrl =
    (import.meta.env.VITE_WS_URL || "ws://localhost:8000") + "/ws/poses";
  let ws: WebSocket | null = null;
  const listeners = new Set<(pose: any) => void>();

  function connect() {
    ws = new WebSocket(wsUrl);
    ws.onmessage = (e) => {
      const pose = JSON.parse(e.data);
      listeners.forEach((fn) => fn(pose));
    };
    ws.onclose = () => {
      setTimeout(connect, 3000);
    };
  }

  function subscribe(fn: (pose: any) => void) {
    listeners.add(fn);
    if (!ws || ws.readyState === WebSocket.CLOSED) connect();
    return () => {
      listeners.delete(fn);
      if (listeners.size === 0 && ws) {
        ws.close();
        ws = null;
      }
    };
  }

  return { subscribe };
}
