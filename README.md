# 心动员工敬业度调研数据仪表板

一个现代化的员工敬业度和满意度数据可视化仪表板，采用Power BI风格设计，提供交互式数据分析和智能问答功能。

## 🌐 在线访问

**GitHub Pages部署版本**：https://shelly-kora.github.io/employee-engagement-dashboard/

> 💡 推荐使用GitHub Pages版本，加载速度更快，功能更稳定

## 🌟 功能特性

### 📊 数据可视化
- **KPI仪表板**：总体人数、填写人数、敬业度、满意度、高效员工比例
- **四象限分析**：员工敬业-满意度交叉分析气泡图
- **年度对比**：2023年与2024年趋势对比
- **部门分析**：全部部门、二级部门、管理层对比、职级分析

### 🎯 核心指标
- **敬业度**：68%（较2023年提升8%）
- **满意度**：68%（较2023年提升8%）
- **填写率**：64.5%（828/1284人）
- **高效员工比例**：62.8%（敬业且满意）

### 🏢 部门覆盖
- **26个一级部门**：从财务部到TapTap等各个业务单元
- **60+二级部门**：详细的项目组和专业组数据
- **管理层分析**：管理岗位vs非管理岗位对比
- **职级分析**：不同职级员工表现对比

### 💬 智能问答
- **AI助手**：基于数据的智能问答系统
- **专业分析**：提供部门表现、改进建议、趋势分析
- **实时交互**：支持自然语言查询

### 📱 技术特性
- **响应式设计**：适配桌面和移动设备
- **Power BI风格**：现代化的商业智能界面
- **Excel支持**：支持上传Excel文件更新数据
- **实时图表**：基于Chart.js的交互式图表

## 🚀 快速开始

### 在线访问
- **GitHub Pages**：[https://shelly-kora.github.io/employee-engagement-dashboard/](https://shelly-kora.github.io/employee-engagement-dashboard/)
- **备用链接**：[https://mcp.edgeone.site/share/Q8F-fzMCe43aJLVACn8si](https://mcp.edgeone.site/share/Q8F-fzMCe43aJLVACn8si)

### 本地运行
1. 克隆项目
```bash
git clone https://github.com/shelly-kora/employee-engagement-dashboard.git
cd employee-engagement-dashboard
```

2. 打开仪表板
```bash
# 使用任意HTTP服务器
python -m http.server 8000
# 或者直接在浏览器中打开 index.html
```

3. 访问 `http://localhost:8000`

## 📁 项目结构

```
employee-engagement-dashboard/
├── index.html                    # 主入口页面（仪表板导航）
├── dashboard_premium.html        # 🌟 高级版仪表板（推荐）
├── dashboard_final.html          # 📈 完整版仪表板
├── dashboard_optimized.html      # ⚡ 优化版仪表板
├── dashboard_clean.html          # 🎯 简洁版仪表板
├── dashboard_fixed.html          # 🔧 修复版仪表板
├── dashboard_updated.html        # 🆕 更新版仪表板
├── dashboard.html                # 📊 基础版仪表板
├── process_employee_survey.py    # 🐍 数据处理脚本
├── 初始数据.xlsx                 # 📋 原始调研数据
├── 员工敬满度分析/               # 📈 详细分析数据
├── README.md                     # 📖 项目说明
├── LICENSE                       # ⚖️ 开源协议
├── CHANGELOG.md                  # 📝 版本更新日志
├── requirements.txt              # 🐍 Python依赖
├── .github/workflows/deploy.yml  # 🚀 自动部署配置
└── .gitignore                    # 🚫 Git忽略文件
```

## 🎨 界面预览

### 主仪表板
![主仪表板](docs/screenshots/dashboard-main.png)

### 四象限分析
![四象限分析](docs/screenshots/quadrant-analysis.png)

### 部门对比
![部门对比](docs/screenshots/department-comparison.png)

## 📈 数据说明

### 数据来源
- 基于2024年员工敬业度调研真实数据
- 涵盖1284名员工，828人参与填写
- 包含26个一级部门和60+二级部门数据

### 指标定义
- **敬业度**：员工对工作的投入程度和热情
- **满意度**：员工对工作环境和条件的满意程度
- **高效员工**：同时具备高敬业度和高满意度的员工
- **填写率**：实际参与调研人数占总员工数的比例

## 🛠️ 技术栈

- **前端框架**：原生HTML5 + CSS3 + JavaScript
- **图表库**：Chart.js
- **样式框架**：自定义CSS（Power BI风格）
- **数据处理**：XLSX.js（Excel文件解析）
- **部署平台**：GitHub Pages + EdgeOne Pages
- **自动部署**：GitHub Actions

## 🚀 部署说明

### GitHub Pages自动部署
本项目配置了GitHub Actions自动部署：
- 每次推送到`main`分支时自动触发部署
- 部署到GitHub Pages：https://shelly-kora.github.io/employee-engagement-dashboard/
- 支持自定义域名配置

### 手动部署到其他平台
```bash
# 部署到Vercel
npx vercel --prod

# 部署到Netlify
npm install -g netlify-cli
netlify deploy --prod --dir .

# 部署到GitHub Pages（手动）
git checkout -b gh-pages
git push origin gh-pages
```

## 📊 数据更新

### 上传新数据
1. 点击"上传数据"按钮
2. 选择Excel文件（.xlsx或.xls格式）
3. 系统自动解析并更新图表

### 数据格式要求
Excel文件应包含以下列：
- 部门名称
- 二级部门
- 员工数量
- 敬业度分数
- 满意度分数

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 开发环境设置
1. Fork本项目
2. 创建功能分支：`git checkout -b feature/new-feature`
3. 提交更改：`git commit -am 'Add new feature'`
4. 推送分支：`git push origin feature/new-feature`
5. 提交Pull Request

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 📞 联系方式

- 项目维护者：心动网络
- 邮箱：support@xindong.com
- 项目地址：https://github.com/shelly-kora/employee-engagement-dashboard

## 🔄 版本历史

### v1.1.0 (2024-12-19)
- 🚀 添加GitHub Pages自动部署
- 🎯 创建仪表板导航入口页面
- ⚡ 优化项目结构和文档

### v1.0.0 (2024-12-19)
- ✨ 初始版本发布
- 📊 完整的KPI仪表板
- 🎯 四象限员工分析
- 🏢 全部门和二级部门数据
- 💬 智能问答功能
- 📱 响应式设计

---

**⭐ 如果这个项目对您有帮助，请给我们一个Star！** # Updated 2025年 5月27日 星期二 10时43分07秒 CST
