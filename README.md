# TTS_designer
Based on django, a tool for tabletop simulater mod designer.

# 简介

本项目主要用于TableTop Simulator的图包设计，提供以下功能：

- 卡牌的原画、卡面描述、数值等信息的管理。
- 将上述信息填入html模板, 渲染成单卡图片或者卡组导入图片。
- 发布资源，减少传递图包的难度。

一个方便自己近期工作的小项目，随缘维护。设计卡牌模板需要一定的html与css知识，如果更改卡面字段请直接修改model。

# 当前状态

仅构建模型与框架，下一步准备用imgkit或者html2canvas做卡牌生成。~~虽然非web端已经实现过一次了~~