# LocusAtlas

空间定位生态平台 — 多设备点云匹配定位，3D可视化，人机空间协同。

## 项目结构

```
LocusAtlas/
├── backend/                 # Python FastAPI 后端
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/          # REST API v1
│   │   │   │   ├── devices.py
│   │   │   │   ├── maps.py
│   │   │   │   └── localization.py
│   │   │   └── ws/          # WebSocket
│   │   ├── core/            # 配置
│   │   ├── models/          # 数据模型
│   │   ├── services/
│   │   │   ├── localization/ # 点云匹配、位姿管理
│   │   │   ├── map/          # 地图预处理
│   │   │   └── device/       # 设备管理
│   │   └── utils/
│   ├── tests/
│   └── requirements.txt
├── frontend/                # React + TypeScript + Three.js
│   ├── src/
│   │   ├── components/      # UI组件
│   │   ├── pages/           # 页面
│   │   ├── services/        # API调用
│   │   ├── hooks/           # 自定义hooks
│   │   └── types/           # TypeScript类型
│   └── package.json
└── docs/
    └── v1.0/
        └── PRD_v1.0.md
```

## 快速启动

### 后端
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 前端
```bash
cd frontend
npm install
npm run dev
```

## 技术栈

- 后端: Python FastAPI + Open3D + SQLite
- 前端: React + TypeScript + Three.js + Potree
- 通信: REST + WebSocket
- 认证: 静态Token (MVP)
