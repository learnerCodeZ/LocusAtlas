# LocusAtlas 项目进度日志

> 最后更新: 2026-06-17

## 项目概述

**LocusAtlas** — 空间定位生态平台，通过点云匹配实现多设备（HoloLens2、Kinect等）在预扫描地图中的精确定位，提供"透视级"空间感知能力。

GitHub: https://github.com/learnerCodeZ/LocusAtlas

---

## 已完成事项

### 1. PRD 讨论与定稿
- 讨论并确认产品愿景：多设备空间定位生态平台，核心价值是"透视级空间感知"
- 确认三大核心场景：指挥中心监控、现场人机协作、空间任务调度
- 确认定位方案：端云协同（设备端SLAM/感知 + 服务器端点云匹配校准）
- PRD 文件: `docs/v1.0/PRD_v1.0.md`

### 2. 关键决策记录

| 问题 | 结论 | 理由 |
|------|------|------|
| 项目命名 | LocusAtlas | Locus(位置)+Atlas(地图册)，学术感强 |
| 地图扫描工具 | Kinect | 同一设备既扫地图又做定位，需加预处理流水线 |
| 服务器部署 | 单体服务，局域网 | 1-3设备MVP阶段一台PC够用 |
| HoloLens2 MR渲染 | MVP不做，V1.0加 | 先验证定位精度再渲染，避免标记飘移 |
| 数据安全 | 静态Token认证 | 局域网内简单够用，后续升级JWT |
| 离线模式 | MVP不做 | 断网后重连重新匹配 |
| 技术栈 | 后端Python FastAPI+Open3D，前端React+Three.js+Potree | 点云库丰富，3D渲染成熟 |

### 3. 项目结构搭建
- 后端 FastAPI 骨架（设备管理、地图上传、定位匹配、WebSocket位姿推送）
- 前端 React+TypeScript+Three.js 骨架（监控Dashboard、设备管理、地图管理三个页面）
- 根目录配置: README.md, CLAUDE.md, .gitignore

### 4. Git 初始化 & GitHub 推送
- 本地 Git 仓库初始化，首次提交
- 推送到 https://github.com/learnerCodeZ/LocusAtlas (main 分支)

---

## 下一步待做

按优先级排列：

1. **验证后端启动** — 安装依赖，启动 FastAPI，确认 API 可访问（`uvicorn app.main:app --reload`）
2. **验证前端启动** — `npm run dev`，确认页面渲染正常
3. **实现地图上传+预处理** — MVP 第一个核心功能，没地图就没法做定位
4. **实现点云匹配定位** — 核心能力，ICP/NDT匹配
5. **设备接入验证** — 先用模拟数据跑通流程，再接真实设备
6. **文件夹重命名** — 把 `D:\MYCODE\1` 重命名为 `D:\MYCODE\LocusAtlas`（需退出当前会话后手动操作）

---

## 项目结构参考

```
LocusAtlas/
├── backend/                 # Python FastAPI 后端
│   ├── app/
│   │   ├── api/v1/          # REST API（devices, maps, localization）
│   │   ├── api/ws/          # WebSocket 位姿推送
│   │   ├── core/            # 配置（config.py）
│   │   ├── models/          # 数据模型（device.py）
│   │   ├── services/
│   │   │   ├── localization/ # matcher.py, pose_manager.py
│   │   │   ├── map/          # processor.py（去噪→下采样→体素化）
│   │   │   └── device/
│   │   └── utils/
│   └── requirements.txt
├── frontend/                # React + TypeScript + Three.js
│   └── src/
│       ├── components/      # PointCloudViewer, DeviceMarker, Layout
│       ├── pages/           # Dashboard, Devices, Maps
│       ├── services/        # api.ts
│       ├── hooks/           # usePoseStream.ts
│       └── types/           # TypeScript 类型定义
├── docs/v1.0/PRD_v1.0.md   # 产品需求文档
└── log/                     # 进度日志（本文件）
```
