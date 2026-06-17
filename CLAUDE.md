# LocusAtlas - Claude Code 项目指南

## 项目概述
空间定位生态平台（LocusAtlas），通过点云匹配实现多设备（HoloLens2、Kinect等）在预扫描地图中的精确定位。

## 核心架构
- **端云协同**：HoloLens2自带SLAM+服务器校准（近实时），Kinect周期性上传匹配（5-30s）
- **单体服务**：MVP阶段一台PC跑全部服务，局域网部署
- **点云匹配**：Open3D ICP/NDT，服务器端计算

## 关键路径
- 后端入口: `backend/app/main.py`
- 定位匹配: `backend/app/services/localization/matcher.py`
- 位姿管理: `backend/app/services/localization/pose_manager.py`
- 地图预处理: `backend/app/services/map/processor.py`
- 前端入口: `frontend/src/App.tsx`
- 3D渲染: `frontend/src/components/map/PointCloudViewer.tsx`

## 开发规范
- 后端用 Python，FastAPI，异步优先
- 前端用 TypeScript，组件式开发
- MVP 阶段数据存储用内存/SQLite，不做过度设计
- API 路由统一在 `/api/v1/` 下
