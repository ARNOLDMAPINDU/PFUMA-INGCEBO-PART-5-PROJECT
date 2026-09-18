// The single source of truth this app displays — the PFUMA web app.
// This is the whole point of app-webview: one UI, not two codebases.
//
// Academic build: points at the Vite dev server running locally on this
// machine (`npm run dev`, default port 5173), not a hosted deployment —
// there is no VPS dependency. A physical phone needs the dev machine's
// LAN IP, not localhost (find it with `ipconfig`, "IPv4 Address");
// override with EXPO_PUBLIC_WEB_URL if that IP changes. An
// emulator/simulator can usually use localhost directly.
export const WEB_URL = process.env.EXPO_PUBLIC_WEB_URL || 'http://10.11.246.53:5173';
