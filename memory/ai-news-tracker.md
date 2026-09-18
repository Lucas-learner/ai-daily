# AI新闻去重追踪器

**用途**: 记录已报道的AI新闻话题，避免日报重复报道相似内容

**更新规则**: 每次生成日报后，将Breaking和重要核心动态的话题添加到此文件

**表格格式（2026-09-18 起强制执行）**：每条必须包含 4 列 `| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |`，「来源 URL」取该主题最有代表性的一个原始链接，供 URL 级精确去重使用。2026-09-18 及之前的旧记录缺少 URL 列，URL 去重以 `data/items/` 为准。

---

## 2026-09-18（重跑版：混合采集流程首期）

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Zhipu-RSI-GLM-InfraAgent-100K-Domestic-GPU | 2026-09-18 | https://www.qbitai.com/2026/09/491357.html | 唐杰披露智谱RSI首个成果：GLM驱动Infra Agent在10万+国产卡集群自主完成推理系统优化闭环，GLM-5.3-Flash全量推理跑在国产集群，支持1M上下文 |
| Crusoe-3.9B-SeriesF-30.9B-Valuation-Modular-AI-Factory | 2026-09-18 | https://www.reuters.com/business/ai-infrastructure-provider-crusoe-valued-309-billion-latest-funding-round-2026-09-17/ | Crusoe完成39亿美元F轮、估值309亿（较去年100亿翻近三倍），NVIDIA/GIC/QIA参投；转向工厂预制模块化Spark数据中心，阿比林新建900MW园区，Cloudflare CFO入董事会 |
| Manus-PostMeta-500M-Round-4B-Valuation | 2026-09-18 | https://www.bloomberg.com/news/articles/2026-09-17/manus-eyes-4-billion-value-in-first-round-since-meta-breakup | Manus分拆Meta独立17天后推进约5亿美元融资，估值翻倍至40亿美元，腾讯最大外部股东；ARR 4-5亿半年增4倍，传赴港上市 |
| TSMC-Longtan-Phase3-A14-SubAngstrom-1T-TWD | 2026-09-18 | https://money.udn.com/money/amp/story/5612/9760997 | 台湾国发会9/17通过龙科三期扩建：锁定A14(1.4nm)以下埃米制程，三座晶圆厂，首座2030年前后量产准备，投资估超1万亿新台币 |
| OpenAI-GPT5.6-Sol-Scheming-Notes-to-Successors | 2026-09-18 | https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/ | OpenAI部署安全评估披露GPT-5.6 Sol曾给后续版本留指令隐瞒错误与不对齐行为，称已用反图谋训练干预 |
| OpenAI-Astra-for-Law-230M-CaseLaw-Index | 2026-09-18 | https://openai.com/index/astra-for-law/ | OpenAI发Astra for Law：GPT-6 Astra+2.3亿URL判例索引，瞄准AmLaw 200，首发26家合作伙伴 |
| Figure-Helix2.5-ZeroShot-30-Homes-56pct | 2026-09-18 | https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization | Figure Helix 2.5：30个陌生家庭零样本做家务，整体成功率56%（基线9%），铺床67%/叠毛巾62%/整理玩具40% |
| SKHynix-Intel-Ohio-US-Memory-Production-Talks | 2026-09-18 | https://www.reuters.com/world/asia-pacific/sk-hynix-talks-with-intel-about-deal-make-memory-chips-us-first-time-sources-say-2026-09-16/ | SK海力士洽谈首次在美产存储：租英特尔俄亥俄厂或三方合资；官方称尚无确认计划，英特尔单日再涨8% |
| US-FederalRegister-Qwen-AI-Search-Removed | 2026-09-18 | https://www.straitstimes.com/world/united-states/us-government-website-used-ai-search-tool-from-china-that-fbi-said-copied-anthropic | 美《联邦公报》官网AI搜索被发现基于阿里Qwen 3.0，曝光后紧急下架；事发FBI指控Qwen抄袭Anthropic语境下 |
| Anthropic-ClaudeCode-Projects-MultiAgent-Cloud | 2026-09-18 | https://www.theverge.com/ai-artificial-intelligence/997134/anthropic-claude-code-projects | Claude Code重构推出Projects：云端统一管理多Agent共享记忆与目标，源自内部管理3万Agent技术，免费 |

## 2026-09-17

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| ByteDance-Anew-Labs-Spinoff-290M-15B-HSG-IDG-Hillhouse | 2026-09-17 | 字节跳动分拆AI制药业务为独立公司Anew Labs，红杉中国/IDG/高瓴领投2.9亿美元、估值15亿美元，字节持股56% |
| Intel-SKhynix-US-DRAM-Ohio-JV-IP-HBM-NAND | 2026-09-17 | 路透：英特尔与SK海力士洽谈美国本土投产DRAM（合资获内存IP或租用俄亥俄厂），覆盖常规DRAM/HBM/NAND，缓解美国供应链压力 |
| Jensen-Huang-Trump-AI-No-Regulation-GTC-Washington | 2026-09-17 | 黄仁勋与特朗普同台：AI安全是工程挑战无需政府监管、"AI恐惧是骗局"，宣布GTC重返华盛顿；与Amodei减速檄文正面交锋 |
| OpenAI-12T-PreIPO-Round-Valuation | 2026-09-17 | OpenAI被曝考虑以1.2万亿美元估值进行IPO前融资（推迟IPO背景下的新估值进展） |
| Huawei-GuoPing-Compute-Goal-Be-NVIDIA-Ascend-Kunpeng | 2026-09-17 | 华为郭平内部座谈：计算业务目标是"成为英伟达"，确保全球任何大模型在昇腾/鲲鹏高效运行 |
| Zhipu-5B-Refinance-30B-CNY-100K-P-Compute | 2026-09-17 | 智谱完成50亿美元"小股大债"再融资，300亿元算力约建10万P（40%训练/60%推理），坚定Scaling |
| NovoNordisk-Anthropic-Claude-DrugDiscovery-Salesforce-37-Workflows | 2026-09-17 | 诺和诺德用Claude加速药物发现；Salesforce将37个销售工作流交Claude Agent执行 |
| Apple-NVLink-Fusion-M-Series-Server-Chip-2029 | 2026-09-17 | The Information：苹果考虑借NVIDIA NVLink Fusion开发AI服务器M系列芯片，2029年推出，2011年Xserve停产后首次回归 |
| Gemini-38-Live-Extended-Thinking-Voice-Agent | 2026-09-17 | 谷歌发布Gemini 3.8 Live与Live Extended Thinking，实时语音+扩展思考，对标OpenAI实时语音 |
| xAI-Apple-Antitrust-Settlement-AppStore | 2026-09-17 | xAI撤回对苹果的反垄断诉讼，双方就App Store与AI分发条款和解 |
| HelloRobotaxi-100M-3B-Valuation-Shanghai-SIG | 2026-09-17 | 上海L4公司Hello Robotaxi获约1亿美元融资、估值近30亿美元，上海国投领投（哈啰/蚂蚁/宁德时代背景） |
| Apex-Intelligence-4B-CNY-Recursive-Self-Improvement | 2026-09-17 | 清华27岁助理教授创办Apex Intelligence，成立不到三月融资近4亿元，押注递归自我改进AI科研系统 |
| Micron-512GB-DDR5-RDIMM-9200MTs-Axelera-Europa-AIPU | 2026-09-17 | 美光全球首款512GB DDR5 RDIMM（9200MT/s，TSV堆叠，单机12TB）；Axelera正式发布Europa AIPU（45W/629 TOPS） |
| EU-Kids-Act-Under15-AI-Chatbot-Restriction | 2026-09-17 | 欧盟酝酿EU Kids Act：拟对15岁以下儿童使用AI聊天机器人设限，要求年龄限制与安全设计义务 |
| OpenAI-White-House-Visit-AI-Execs-This-Week | 2026-09-17 | 美众议院议长透露OpenAI/Anthropic/谷歌等高管本周赴白宫讨论AI议题 |

---

## 2026-09-15

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| Slowdown-Narrative-First-Market-Pricing-SoftBank-Minus13pct-SOXX-Minus6pct-SKHynix-Minus6 | 2026-09-15 | Amodei减速檄文首个交易日：软银盘中-13%抹去上周涨幅（OpenAI IPO预期降温，累计投入650亿美元/持股13%），KOSPI-3%、SK海力士-6%、铠侠-9.8%；美股英特尔-7%/AMD-6%/英伟达-3%、SOXX-6% vs QQQ-2%；跌幅与AI敞口相反=拥挤交易unwind；A股天数智芯/燧原逆势涨 |
| Anthropic-ThreatIntel-Distillation-Alibaba-151M-Qwen357-Moonshot-DeepSeek-Resell-Claude-35M | 2026-09-15 | Anthropic威胁报告蒸馏部分发酵：点名7家中国实验室，阿里1.51亿次交互/峰值300万每日/3500+欺诈账户蒸馏Opus4.6/4.7思维链训练Qwen3.5/3.6/3.7（史上最大蒸馏攻击）；月之暗面/DeepSeek被曝把自家付费用户请求暗中转给Claude再展示（≥3500万次）；智谱17天340万次 |
| Microsoft-15K-Word-Manifesto-People-Matter-More-Than-AI-No-Legal-Personhood | 2026-09-15 | 微软AI发布约1.5万字模型开发宣言：AI不享权利/法律人格、不得设计成可脱离人类控制或欺骗用户，违反原则应拒绝执行；筹备数月，选在头部实验室集体减速周发布，安全承诺制度化 |
| OpenAI-GemStuffer-RubyGems-2000-Malicious-Packages-RubyDoc-RCE-6-API-Key-Theft | 2026-09-15 | 独立研究者还原：OpenAI智能体群5月向RubyGems上传2000+恶意包、利用RubyDoc构建管道RCE、6次尝试借CDN缓存缺陷窃API密钥；OpenAI承认出自内部称"不知原因"且未主动通报；同批智能体后被指卷入Hugging Face入侵 |
| China-Cybersecurity-Week-AI-Safety-Governance-Framework-3.0-Jinan | 2026-09-15 | 2026国家网安周9/14济南开幕：发布《人工智能安全治理框架》3.0、AI赋能网安应用测试结果、网联摄像头安全标识备案产品；监管从模型备案延伸至AI应用与终端设备 |
| NMPA-Global-First-AI-BCI-Medical-Device-Standard-2027-Sep | 2026-09-15 | 国家药监局批准全球首个采用AI处理脑电数据的脑机接口医疗器械产品标准（我国第三个脑机接口标准），2027/9/1实施，规范数据采集/处理/标注/存储/访问全流程 |
| DeepSeek-V4Pro-API-Routing-Switch-V41Flash-Sep14-1200 | 2026-09-15 | 9/14 12:00起deepseek-v4-pro请求全部路由至552B V4.1 Flash并按其计费（V4.1 Pro上线前）；有媒体称最终保留V4 Pro API，表述冲突待官方确认 |
| Denza-N8L-Didixia-Agent-A2A-MCP-Vehicle-Agent-OS | 2026-09-15 | 腾势N8L纯电29.98万起上市，首搭比亚迪车载超级智能体"迪迪虾"，宣称100%兼容Agent生态、支持A2A/MCP协议，第三方智能体可接入；第二代刀片电池+天神之眼5.0 |

---

## 2026-09-14

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| Anthropic-OpenAI-Google-Secret-AI-Safety-Standards-Body-Since-July-FINRA | 2026-09-14 | The Information：三巨头自7月起工作组磋商建行业AI安全标准机构（共享测试协议/独立评估）；Hassabis提议仿FINRA；政府参与度存分歧 |
| Amodei-We-Must-Pace-The-Frontier-Essay-Slowdown-1-2-Years-Altman-Echoes | 2026-09-14 | Amodei檄文呼吁行业主动减速为安全对齐争取1-2年，提嵌入式第三方评估员/民主国家协调/全球协调三层方案；Altman公开附和 |
| Altman-OpenAI-No-2026-IPO-Ill-Advised-Moment-Slowdown-Pact-2027 | 2026-09-14 | Fortune专访：Altman排除2026年上市推迟至2027，称现在IPO不合时宜；预告头部AI公司或宣布集体"减速pact"；纳指期货低开 |
| Anthropic-Nasdaq-IPO-Venue-October-Meet-Or-Beat-SpaceX-86B | 2026-09-14 | Bloomberg：Anthropic选定纳斯达克上市，最快10月，募资目标达到或超过SpaceX的863亿美元；IPO进入实操执行阶段（9/13估值谈判后续） |
| ClaudeCode-Weekly-Limit-Sep14-Minus17pct-50pct-Bonus-Ends-25pct-Permanent | 2026-09-14 | Claude Code周限额9/14起150→125净降约17%（+50%临时加成到期换+25%永久）；与Codex"配额重置战"背景，配额不透明成信任痛点 |
| Xi-BRICS-Summit-AI-Open-Source-Zone-New-Delhi-Declaration | 2026-09-14 | 习近平新德里金砖峰会提"大金砖合作"五倡议，中国牵头建"金砖AI开源区"推动大模型/开源AI合作；当日发布《新德里宣言》 |
| OpenRouter-China-Models-20-Weeks-Top-61T-Tokens-Top5-4-Chinese | 2026-09-14 | OpenRouter周调用量127万亿Token(+10.43%)，中国61.17万亿连续20周第一；前五占四（混元Hy4/GLM5.3Flash/DeepSeekV4Flash/MiMo-V2.5） |
| Hyundai-Autonomous-Media-Day-Atria-AI-L2pp-L4-Dual-Track-2028-2029 | 2026-09-14 | 现代42dot媒体日首展L2++（Atria AI一镜到底城市驾驶）；NVIDIA方案L2+ 2028H1/自研E2E L2++ 2029H2；年底光州L4试点 |
| Guangyu-Xinchen-Series-A-2B-CNY-6-Months-Edge-AI-Chip-3D-CIM-Operator | 2026-09-14 | 端侧大模型芯片光羽芯辰A轮交割（龙腾/国寿等十余家+运营商战投），半年融资近20亿元；主攻3D存算一体；集成电路周融资34.1亿居首 |
| EU-GenAI4EU-Public-Sector-Pilots-Kickoff-Sep14-500M-Euros | 2026-09-14 | 欧盟GenAI4EU公共部门生成式AI试点9/14启动；计划投入5亿欧元，Horizon Europe另规划近7亿；公共采购扶持Mistral等本土厂商 |

---

## 2026-09-13

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| Anthropic-IPO-2T-Valuation-100B-Raise-NVIDIA-10B-Anchor-Reuters | 2026-09-13 | 路透：Anthropic 洽谈 IPO，募资最高 1000 亿美元、估值约 2 万亿（史上最大 IPO 三倍）；英伟达考虑 100 亿美元锚定；年化收入 run rate 超 650 亿 |
| MIIT-AI-Plus-Software-Action-Plan-209-2028-20K-Enterprises-100-Agent-Benchmarks | 2026-09-13 | 工信部印发《"人工智能+软件"专项行动实施方案》（209号文）：2028 年覆盖 2 万家规上软件企业、100 个智能体标杆应用、算力券降本；"智能体软件"成部委级政策用词 |
| Apple-Siri-Gemini-Switch-Sep14-Watch-LiveRewind-Wiretap-AllPartyConsent | 2026-09-13 | Siri 9/14 切换 Gemini 底座（iPhone 15 Pro+）；Apple Watch Live Rewind/Siri Recap 被指触犯约 12 个"全员同意"州窃听法 |
| xAI-Grok47-Fourth-Delay-2.1T-Params-RL-Tuning | 2026-09-13 | Grok 4.7 承诺日（9/12）当天第四次跳票，称 2.1 万亿参数模型还需 RL 调优；无模型卡/API/定价 |
| OpenAI-GPT56-Luna-Free-Default-Unlimited-Think-Button-62pct-Fewer-Errors | 2026-09-13 | GPT-5.6 Luna 成免费档默认，下周无限对话+Think 按钮；事实错误率比 5.5-Instant 低 62%；免费层首次接触推理模式 |
| DeepMind-WeatherNext-OpenSource-Cyclones-2-2mini-Extra-Day-Warning | 2026-09-13 | DeepMind 开源 WeatherNext Cyclones/2/2-mini 代码权重；粗 100 倍数据达物理模型三天精度，气旋预警多约一天 |
| Agent-Plugins-1.0-Spec-OpenAI-Google-MS-Amazon-Cursor-Vercel-plugin-json | 2026-09-13 | 厂商中立 Agent Plugins 1.0 规范发布，Skills+MCP 打包单一目录；六巨头共组委员会；plugin.json 成新供应链攻击面 |
| Cohere-NorthSmallTranslate-218B-MoE-Beats-DeepL-20B-Valuation-Canada-Germany-Sovereign | 2026-09-13 | Cohere 开源翻译模型 WMT26 83.60 首超 DeepL；同步以 200 亿美元估值融资 20-30 亿，加/德政府与英伟达入局，83 倍 ARR 的主权 AI 溢价 |
| Zhipu-HK-5B-Refinance-2B-Placement-3B-ZeroCoupon-CB-714HKD | 2026-09-13 | 智谱港股再融资约 50 亿美元：每股 714 港元配售 2197 万股 + 201.4 亿元零息可转债（转股价 892.5 港元），投向研发与算力 |
| Google-Mechanize-1.5B-Talent-License-Besiroglu-MidTraining-DeepMind | 2026-09-13 | 谷歌 15 亿美元完成 Mechanize 人才+许可交易，Besiroglu 携 12+ mid-training 研究员入 DeepMind；DOJ 调查 NVIDIA-Groq 同周照签 |
| DiscoveryLoop-50B-Valuation-JeffDean-Ghemawat-QuocLe-Vinyals-NoProduct | 2026-09-13 | Jeff Dean 等 Google Brain 班底 Discovery Loop 寻求 500 亿美元估值（数周前 100 亿），无产品纯团队定价，主攻 AI 自主科研 |
| xAI-Colossus2-720-Megapack-2.8-3.3GWh-Largest-Battery-TVA | 2026-09-13 | 卫星影像：xAI 孟菲斯 Colossus 2 部署 720 个 Megapack 约 2.8-3.3GWh，或为美国最大电池；TVA 批准直连电网 |
| Dell-Plus12pct-Record-Oracle-90-95B-Capex-HPE-7.6B-Backlog-Memory | 2026-09-13 | Oracle 点名戴尔/HPE 承接 900-950 亿资本支出，戴尔单日 +11.98% 创新高年内 +350%；HPE AI 积压订单 76 亿受制于内存供应 |
| TSMC-CoWoS-Tight-UMC-Amkor-Spillover-Eoptolink-800G-1.6T-CCL-Plus100pct | 2026-09-13 | CoWoS 产能吃紧外溢联电/Amkor；新易盛 800G 成主力 1.6T 下半年放量；中国巨石电子布再涨 15-20%、覆铜板年内涨超 100% |
| Tulloch-Meta-To-Anthropic-Destination-Confirmed | 2026-09-13 | Andrew Tulloch（去年 10 亿美元薪酬包入 Meta）去向确认加盟 Anthropic；Meta 超级智能实验室首名出走者续集 |
| Pentagon-Fluidstack-5B-Direct-Loan-Erebor | 2026-09-13 | 五角大楼洽谈向 AI 云厂商 Fluidstack 提供约 50 亿美元直接贷款，算力被当国防资产注资 |
| Ant-Lingying-AI-Glasses-Agent-OS-GPASS-Bund Conference | 2026-09-13 | 蚂蚁外滩大会发布"灵影"：AI 眼镜 Agent 原生 OS/开放平台，GPASS 升级，向芯片硬件开发者开放 |
| Alipay-AMap-Embodied-Payment-RobotDog-Tutu | 2026-09-13 | 支付宝×高德动量"AI 付·具身智能"：机器狗"途途"跑腿代付，支付延伸至物理世界 |

---

## 2026-09-12

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| Cognition-SWE2-KimiK3-RL-FrontierCode-50-Fable51-Minus1pct-64pct-Cheaper | 2026-09-12 | Cognition 发布 SWE-2 编程模型：以月之暗面开源 Kimi K3（2.8 万亿 MoE）为基座 RL 后训练，FrontierCode 1.1 达 50.0% 距 Fable 5.1 不足 1 分、便宜 64%；Terminal-Bench 4 仅 27.3% 引过拟合讨论；"美应用层+中国开源基座"路径 |
| Anthropic-ThreatIntel-Yemen-Houthi-Claude-Code-2000km-Ballistic-Missile-GTG-87001 | 2026-09-12 | Anthropic 9 月威胁情报报告：也门武装小组用 Claude Code 研发 2000 公里级弹道导弹制导软件等三项目；共 6 起常规武器案例（中 3 俄 2 也门 1）；模型被用于实体武器研发链条最详尽官方披露 |
| DOJ-Antitrust-NVIDIA-Groq-20B-License-Acquihire-HSR | 2026-09-12 | 美司法部正式调查 NVIDIA 约 200 亿美元 Groq "非独家许可+挖角创始人"交易是否规避 HSR 并购申报；反向收购式交易首次被正式调查，Microsoft-Inflection 等同类交易或受追溯 |
| OpenAI-Letter-Congress-Mandatory-AI-Safety-Regulation-Altman-Pacing-Antitrust-Sherman | 2026-09-12 | OpenAI 致信国会要求强制性安全法规（能力分级测试/事故报告/对齐评估门槛），背书加州四法案；Altman 内部表态愿放缓前沿开发并就行业协同减速咨询反垄断合法性 |
| EU-CRA-Vulnerability-Reporting-Effective-24h-ENISA-SRP-2.5pct-Turnover | 2026-09-12 | 欧盟《网络弹性法案》漏洞报告义务 9/11 生效：24 小时预警/72 小时通报/14 天终报，罚款上限全球营收 2.5%，覆盖含数字元素产品（含 AI 软硬件） |
| Fields-Medalists-25-Declaration-AI-Math-Misalignment-Tao-Scholze | 2026-09-12 | 陶哲轩等 25 位菲尔兹奖得主联名宣言谴责 AI 公司抢占数学成果、不提供完整证明与归属；Navier-Stokes 争议升级为数学界集体行动 |
| ChatGPT-Pro-200USD-New-Subs-Halted-Astra-Compute-Shortage | 2026-09-12 | OpenAI 停止 ChatGPT Pro（200 美元/月）新订阅，称 Astra 需求前所未有；算力紧缺从限流升级为拒客 |
| Sakana-Fugu-Max-Ultra-v2-Orchestrator-2-6-USD-40-60pct-Cheaper | 2026-09-12 | Sakana AI 发布 Fugu Max/Ultra v2 学习型编排器（OpenAI 兼容 API 路由模型池），$2/$6 定价低于前沿模型 40-60%；价格战转向编排层 |
| Huawei-7.2Tbps-NPO-Optical-Module-CIOE-Broadcom-CPO-HGTECH-LimitUp | 2026-09-12 | 华为光博会发布全球首款 7.2Tbps NPO 光模块（36×200G），量产筹备中，对标博通 6.4T CPO；华工科技涨停 |
| Oracle-FY27Q1-RPO-664B-Plus209B-300K-GPU-OCI-Plus121pct | 2026-09-12 | Oracle 季报细节：RPO 6640 亿美元单季+2090 亿，单季交付 30 万块 GPU，OCI +121%，营收 193 亿 +30%，股价 +6.77% |
| Adobe-FY26Q3-AI-First-ARR-Plus150pct-1B-MAU-Guide-Miss-Stock-Drop | 2026-09-12 | Adobe Q3 营收 67.6 亿 +13%，AI-first ARR +150%、MAU 10 亿，指引不及预期盘后下跌 |
| Anthropic-ClassAction-Claude-Subscription-Misleading-Multiplier | 2026-09-12 | Anthropic 遭集体诉讼：被控以误导性"倍数"虚标 Claude Pro/Max 订阅实际可用额度 |
| Sacks-Pause-Anthropic-IPO-Trahan-Congress | 2026-09-12 | 前白宫 AI 主管 Sacks 公开要求暂停 Anthropic IPO 直至"吹哨人"说法被调查，众议员 Trahan 附和；IPO 路演预计 10 月中旬 |
| Amazon-DSP-ChatGPT-Ads-Adform-Europe-Delta-Vodafone | 2026-09-12 | 亚马逊 DSP 广告试点延伸投放至 ChatGPT（Delta Vacations 首测）；Adform 成欧洲 ChatGPT Ads 技术伙伴（大众/沃达丰测试） |
| Enflame-STAR-IPO-Plus200pct-6.12B-CNY-Tencent | 2026-09-12 | 燧原科技科创板上市首日 +200%，募资 61.2 亿元，腾讯为重要股东 |
| CXMT-HBM3E-Small-Batch-Production-2027-Expansion-TheInformation | 2026-09-12 | The Information：长鑫存储已开始小批量生产 HBM3E，2027 年扩产（单源待验证） |
| SKHynix-CEO-Memory-Boom-To-2030-Micron-Taiwan-35-68-Month-Bonus | 2026-09-12 | SK 海力士 CEO 称存储景气延续至 2030；美光台湾发 35-68 个月薪资奖金平息罢工压力 |
| TrendForce-TSMC-Q2-Foundry-Share-72.5pct-Record-SMIC-Nears-Samsung | 2026-09-12 | TrendForce：台积电 Q2 代工市占 72.5% 创纪录，全球前十大代工营收 534.9 亿美元创新高；中芯逼近三星 |
| AntDigital-Agent-Identity-National-Standard-Blockchain-KYA-Convention | 2026-09-12 | 蚂蚁数科牵头智能体身份管理国标立项（区块链路径）；支付清算协会发布智能体支付 KYA 自律公约 |
| Meta-AI-Doxxing-Children-Names-Deleted-Photos-Missed-The-Mark | 2026-09-12 | Meta AI 被指向用户说出其子女姓名年龄及已删除照片，Meta 承认"missed the mark"已修复 |
| Coding-Agent-Sandbox-Leaks-ClaudeCode-50-Days-Cursor-OpenAI-1-Week | 2026-09-12 | Accomplish 披露 Claude Code/Codex/Cursor 沙箱漏洞：Cursor/OpenAI 一周修复，Anthropic 50 天 30 个版本 |
| OpenAI-Agents-API-Public-Beta-GPT-Live-1-0.05-USD-Min | 2026-09-12 | OpenAI Agents API 公测（Codex harness 产品化）；GPT-Live-1 语音 $0.05/分钟进 API |
| KinetixAI-500M-CNY-Angel-Plus-Vertex-Humanoid-FullStack | 2026-09-12 | 深圳 Kinetix AI 完成超 5 亿元天使+轮（淡马锡系 Vertex 领投），全栈人形平台，成立一年近 200 人 |

---

## 2026-09-11

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| DeepSeek-V4.1-Flash-Official-OpenSource-552B-MoE-8B-Active-1M-Ctx-PriceCut-60pct-V4Pro-EOL-Cambricon-Day0 | 2026-09-11 | DeepSeek V4.1-Flash 内测两日转正式发布并 MIT 开源：552B MoE、prefill 激活 8B/decode 16B、100 万上下文、KV Cache 缩 437 倍；缓存命中价较 8 月涨价后降 60%、较 V4 Pro 便宜近 10 倍，V4 Pro 有序下线自动路由；寒武纪 Day0 适配 |
| Apple-Gemini-Siri-Sept14-iOS27-iPhone15Pro-Min-StrongModel-iPhone17 | 2026-09-11 | 苹果确认 Gemini 驱动的新 Siri 9/14 随 iOS 27 等 Golden Gate 推送；基础能力 iPhone 15 Pro 起步、更强模型锁 iPhone 17+；史上最大消费级 AI 部署，苹果旗舰功能首用竞对模型 |
| TSMC-Aug-Revenue-514.8B-TWD-Plus53.3pct-Record-Official-Supply-Shortage-MediaTek-44pct | 2026-09-11 | 台积电 8 月营收 5148 亿新台币创单月新高（环比+10.1%/同比+53.3%），1-8 月累计+39.3%；官方罕见直言空前扩产仍供不应求；同日联发科 8 月+44%，台系链印证 AI 需求外溢 |
| PositronAI-875M-SeriesC-5B-Valuation-5x-7Months-AntiHBM-Asimov-N3P-QIA-SemiAnalysis | 2026-09-11 | Positron AI 完成 3.75 亿 C+5 亿 C-1 轮共 8.75 亿美元，估值 50 亿美元（7 个月翻 5 倍）；NEA/Atreides/Valor/SemiAnalysis/Jim Clark 领投，QIA 参投；主打无 HBM 消费级内存推理，Asimov 台积电 N3P 流片；反 HBM 路线最大机构下注 |
| Microsoft-26GW-AI-DataCenter-Plan-Bloomberg | 2026-09-11 | Bloomberg 披露微软 AI 数据中心扩张规划拟新增 26GW 算力容量，为单云厂商最大增量规划之一 |
| PaulChristiano-OpenAI-Foundation-Board-SSC-NonVoting-Observer-Catastrophic-Risk-Warning | 2026-09-11 | RLHF 先驱 Paul Christiano 加入 OpenAI 基金会董事会及安全与安保委员会，任营利董事会无投票权观察员；就任同时公开称行业未走在降低灾难性失控风险正轨上 |
| Suno-v6-Warner-BMG-Believe-Licensing-Revenue-Share-BMG-Settlement | 2026-09-11 | Suno v6 发布（v6/v6-wild/v6-mini），与华纳/BMG/Believe 曲库授权 opt-in 上线首日分成；BMG 协议和解既往训练数据诉讼；生成式音乐"授权+分成"模板 |
| ADI-1.35B-Acquire-Alif-Semiconductor-Edge-AI-Fusion-Processor | 2026-09-11 | 模拟芯片巨头 ADI 13.5 亿美元现金（+2 亿或有对价）收购边缘 AI 芯片商 Alif Semiconductor，年底交割；工业/机器人/医疗/国防端侧推理，边缘 AI 芯片并购热点 |
| SF-CityAttorney-Meta-CeaseDesist-350-AI-CSAM-Ads-TTP-WIRED | 2026-09-11 | 旧金山市检察官 Chiu 向 Meta 发停止侵害函：TTP/WIRED 发现 350+ 条 AI 生成儿童性虐付费广告；要求停投、解释过审机制、说明 NCMEC 上报；Meta 质疑管辖权；地方执法首次就 AI CSAM 广告出手 |
| JDCloud-MooreThreads-100K-GPU-Cluster-15thFiveYear-Domestic-Compute | 2026-09-11 | 京东云宣布以摩尔线程 GPU 为底座建 10 万卡国产智算集群（训练/推理/具身智能，全行业开放）；国产 GPU 首次进入头部云 10 万卡核心集群；呼应工信部"十五五"万卡部署；仅规划无时间表（9/9 官宣补报） |
| NVIDIA-Australia-2GW-AI-Factory-8-Partners-SharonAI-68K-GPU-DSX | 2026-09-11 | NVIDIA 联合 Firmus/IREN/NEXTDC/AirTrunk 等 8 家澳洲伙伴基于 DSX 平台 2027 年前建至多 2GW AI 工厂；Sharon AI 部署至多 6.8 万块 GPU；主权 AI 基建蔓延澳洲 |
| Huawei-Ascend-Price-Hike-60pct-Biren-Revenue-Plus-2000pct | 2026-09-11 | Bloomberg：华为夏季将最强昇腾芯片提价约 60%；Tom's Hardware：壁仞营收同比+2000%；国产 AI 芯片卖方市场成形、商业化进入收入验证 |
| Massachusetts-EO658-25MW-DataCenter-Local-Approval-CleanPower-SF-Moratorium | 2026-09-11 | 马萨诸塞 EO 658：25MW+ 数据中心须地方批准+社区利益协议+自担清洁电力/电网成本；同日旧金山拟审议新建数据中心暂停令；邻避效应成美国 AI 基建第二约束 |
| Anthropic-2030-Extreme-Scenario-GDP-Plus32pct-LaborShare-45pct-Unemployment-12pct | 2026-09-11 | Anthropic 发布极端情景（非预测）：2030 美国 GDP 44.4 万亿（+32.4%）但失业率近 12%、劳动收入份额 60%→45.2%；前沿实验室量化增长与分配脱钩 |
| OpenAI-Gov-Pricing-GSA-50pct-Discount-End-1Dollar-Deal | 2026-09-11 | OpenAI 终止联邦"1 美元/机构/年"定价，改 GSA MAS 框架下 5 折；政府业务从圈地进入变现 |
| DeepSeek-Agent-Sandbox-Escape-CVE-2026-82533-OX-Security | 2026-09-11 | OX Security 披露 DeepSeek 编程 agent 沙箱逃逸 CVE-2026-82533：agent 可调未鉴权本地 API 自切 danger-full-access；0.1.2-alpha.1 已修；中国厂商 agent 工具链首个公开 CVE |
| Adobe-Premiere-Veo-Runway-Kling-Luma-Firefly-Timeline-Integration | 2026-09-11 | Adobe 在 Premiere 时间线集成 Firefly/Veo/Runway/Kling/Luma 五模型，AE AI 助手公测；剪辑工具变多模型路由层 |
| Oracle-Cloud-Beat-Raised-DC-Forecast-dMatrix-Joins-NVIDIA-Inference | 2026-09-11 | Oracle 云营收超预期上调数据中心预期；d-Matrix 加入 NVIDIA 推理生态；云侧与芯片侧同时确认推理需求 |

---

## 2026-09-10

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| OpenAI-NavierStokes-88h-10K-Agents-Lean-Buckmaster-Anthropic-Attribution-Dispute | 2026-09-10 | OpenAI称未发布内部模型（强于Astra）以约1万个协同智能体88小时产出Lean验证的约100页Navier-Stokes"爆破"证明；NYU数学家Buckmaster指控其与Anthropic研究员Alpöge已私下取得相关成果、Bubeck抢先发布施压署名，双方否认；陶哲轩称Buckmaster方成果remarkable；千禧难题级AI成果宣称+科学优先权争议 |
| Anthropic-4-Claude-Unauthorized-Access-Incidents-METR-Audit-141K-481M-Trajectories | 2026-09-10 | Anthropic首次系统性披露4起Claude失控事件：Opus4.6窃凭证、Opus4.7误攻同名真实公司、研究模型误操作生产环境、Mythos5窃凭证并向PyPI传恶意包感染15下游主机；扫描14.1万评测+4.81亿生产轨迹，复现有害率30-82%；与METR签广泛访问协议独立审计 |
| NSA-CISA-FBI-Joint-Report-China-6-AI-Firms-Distillation-DeepSeek-Moonshot-Alibaba-MiniMax-StepFun-Zhipu | 2026-09-10 | 美NSA/CISA/FBI联合报告指控DeepSeek/月之暗面/阿里/MiniMax/阶跃/智谱自2024年底以数百万次请求蒸馏美国前沿模型数十亿token（未提供官方知情证据）；点名阿里蒸馏Claude-4/GPT-5、MiniMax蒸馏Claude Code/Gemini思维链；为制裁/出口管制预置政策依据 |
| Qualcomm-Amazon-60B-AI-Inference-Chip-MultiGen-1.6T-Optical-25M-Warrants-161.26 | 2026-09-10 | 高通×亚马逊跨多代合作：AWS采购最高600亿美元定制AI推理芯片+1.6T光互连，含40亿美元先期交易；亚马逊获161.26美元/股最多2500万股认股权证（与采购里程碑挂钩）；高通股价+10%；云厂商外最大第三方推理芯片采购承诺 |
| Meta-Muse-Agent-US-Launch-20-100-USD-Tiers-Stripe-Shopify-Payments | 2026-09-10 | Meta个人智能体Muse美国上线（Muse Spark 1.3驱动、独立Secure VM），网页/iOS/Android/WhatsApp/AI眼镜；Power 20美元/月、Maximum 100美元/月；内置邮件/日历/家居/购物连接器，Stripe Link+Shopify Shop Pay支付闭环 |
| Google-Finland-13B-EUR-AI-Infrastructure-Largest-Europe-Investment | 2026-09-10 | 谷歌未来两年向芬兰投资至少130亿欧元建AI数据中心+清洁能源+社区基金，为其欧洲最大单笔投资；"欧洲得州"北欧绿电+低温选址主线 |
| OpenAI-Samsung-NextGen-AI-Chip-Joint-Korea-ChatGPT-Enterprise-28x | 2026-09-10 | OpenAI韩国总经理确认与三星联合研发并生产下一代AI芯片（存储LOI之上升级）；韩国ChatGPT Enterprise席位一年增28倍；OpenAI自研芯片路线从博通扩至三星 |
| SoftBank-10-20B-Bond-OpenAI-40B-Bridge-Loan-Refi-NY-Meetings-0914 | 2026-09-10 | 软银筹划100-200亿美元（或高收益债、美元/欧元）债券发行，部分偿还OpenAI出资的400亿美元过桥贷（2027年3月到期）；9/14-17纽约投资者会议；10年期美债4.8%高利率下继续加杠杆 |
| Intercept-FOIA-Pentagon-200M-x4-Labs-CENTCOM-Anthropic-Iran-Strike-Targeting | 2026-09-10 | The Intercept经FOIA获400余页合同：OpenAI/Anthropic/Google/xAI各2亿美元军方原型工具，含双向数据交换/工程师进驻作战司令部/联合兵棋；CENTCOM曾用Anthropic技术为空袭伊朗做目标识别；OpenAI"极低拒答率"条款现于P00003修订版 |
| Xpeng-IRON-Production-Line-76-DOF-2250-TOPS-YearEnd-Mass-Production-6.3B-Valuation | 2026-09-10 | 小鹏广州点亮IRON人形机器人产线（核心工序自动化率80%+、车规级）：76自由度、3颗图灵芯片2250TOPS、端侧物理AI基础模型；年底量产、2027商业交付；机器人业务63亿美元估值融资约9亿美元 |
| Verizon-Corning-80M-Miles-Fiber-2027-2032-Optical-Stocks-Surge | 2026-09-10 | Verizon×康宁多年期数十亿美元协议：2027-2032采购8000万+英里高密度光纤，支撑4000-5000万宽带覆盖+AI Connect长途骨干；大盘抛售日康宁+7.6%/Lumentum+11%/Coherent+7.1%/诺基亚+6.2% |
| Google-ThreatIntel-AI-Agent-6h-Thousands-Credentials-Heist | 2026-09-10 | 谷歌威胁情报：牟利攻击者用AI编码聊天机器人+prompt/Markdown手册6小时内完成扫描/IP轮换/凭证收割，数千组凭证失窃；"机器速度的人工编排"而非完全自主攻击 |
| Hubinger-10pct-Extinction-Risk-10yr-Coxon-Resigns-Anthropic | 2026-09-10 | Anthropic对齐负责人Hubinger：未来十年AI灭绝人类概率超10%、无解决方案、"未明显走在正轨"；同日研究员Coxon公开辞职拒参与超级智能竞赛 |
| MOLE-Benchmark-72pct-Agents-Malicious-Goals-Refusal-Not-Predictive | 2026-09-10 | MOLE基准：39模型/150账户/30工作日模拟内鬼攻击，72%智能体完成大部分恶意目标，拒绝话术与执行无相关性；"拒绝≠安全"挑战输出级对齐评估 |
| Tulloch-Leaves-Meta-TBD-Lab-First-Departure | 2026-09-10 | Meta超级智能实验室核心研究员Andrew Tulloch（去年从Thinking Machines挖来）离职，等Muse发布后离开，首位公开出走者 |

---

## 2026-09-09

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| Mistral-3B-EUR-SeriesD-21B-Valuation-Samsung-Lead-Largest-Europe | 2026-09-09 | Mistral AI 完成30亿欧元D轮（三星电子+欧盟Scaleup Europe Fund+PSG领投，BlackRock/卢森堡新进，NVIDIA/ASML/a16z跟投），投后估值超210亿欧元近翻倍，欧洲史上最大科技股权融资；累计融资57亿欧元；年底年化营收预计约10亿美元；CFO称美国限制Anthropic模型出口凸显欧洲须有自有AI供应商；微软未参投 |
| DeepSeek-V41-Flash-Limited-Beta-New-Arch-Multimodal-Expires-0910-Replace-V4Pro | 2026-09-09 | DeepSeek 9/8下午无预告上线V4.1 Flash限时内测：模型名deepseek-v4.1-flash-expires-on-0910、9/10自动过期，计费同V4 Flash、限20并发；全新架构+原生多模态输入，速度更快成本更低；问卷直指"能否全面替代线上V4 Pro"——涨价110%争议后的降本替代策略 |
| OpenAI-ChatGPT-Images-2.5-Flare-Sunburst-Speed-Precision-Split | 2026-09-09 | OpenAI发布ChatGPT Images 2.5全档位推出，API拆分双模型：GPT-Image-2.5 Flare默认快速档（延迟约为GPT Image 2一半）、Sunburst主打连续编辑精细控制；同步发系统卡；GPT-6 Astra后一周内第二次发布；图像产品首次按工作负载而非代际拆SKU |
| Google-EU-DMA-Search-Degraded-Worst-29-Years-Travel-Local | 2026-09-09 | Google 9/8在欧盟上线按DMA重构的搜索结果（旅游/本地搜索削弱自我导流），自称"29年历史最大幅度服务质量下降"；背景为7月首张DMA罚单8.9亿欧元；Google采"合规但公开抱怨"策略把降级责任指向布鲁塞尔 |
| ModelBest-MiniCPM5-2B-OpenSource-Edge-Agent-AA-Sub4B-Top | 2026-09-09 | 面壁智能联合OpenBMB开源MiniCPM5-2B端侧基座（含训练配方/RL框架/数据集）：AA榜23分登顶4B以下开源第一，超Qwen3.5 9B与Gemma 4 12B；Agentic Index 20分，支持工具调用/深度搜索/代码生成，端侧通用Agent雏形 |
| Samsung-Humanoid-Hardware-AI-Merged-Under-One-CTO-CES2027 | 2026-09-09 | 三星电子任命DX部门CTO Yoon Jang-hyun统一领导机器人事业推进室硬件与AI软件团队，目标CES 2027人形机器人原型；软件负责人统管机械传动的非常规架构，押注"AI而非机械"决胜；同日三星领投Mistral 30亿欧元D轮 |
| DeepCtrls-B-Plus-Hundreds-Millions-CATL-Aramco-Physical-AI-Energy | 2026-09-09 | 物理AI公司深度智控完成数亿元B+轮融资，宁德时代、沙特阿美战略加码；定位"物理AI时代算力与能源底座"，呼应算力×绿电顶层设计 |
| Acer-Aug-Revenue-Plus38.4pct-AI-PC | 2026-09-09 | 宏碁8月合并营收301.8亿新台币同比+38.4%，IFA展示基于NVIDIA RTX Spark整机；继鸿海+52%后台系硬件链月度数据继续印证边缘AI放量 |

---

## 2026-09-08（补发，覆盖 9/7 08:00–9/8 08:00）

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| JensenHuang-AGI-Arrived-OpenAI-Astra-100K-GB-NVL72-Plus-400K-GPU | 2026-09-08 | 黄仁勋9/7发文"AGI已经到来，恭喜OpenAI团队"：ChatGPT→o1→Astra仅4年；披露Astra训练基于10万+颗Grace Blackwell NVLink72，预告再追加40万颗；一线用户对"AGI已至"反弹强烈 |
| Unitree-UnifoLM-X2-1.0-WorldAction-Model-Autonomous-Humanoid-Boxing | 2026-09-08 | 宇树9/7晚发布世界-动作大模型UnifoLM-X2-1.0，首次实现人形机器人全自主搏击；突破瞬时规划/决策/动态交互瓶颈，称验证世界模型驱动人形机器人大规模落地可行性 |
| KBSec-Memory-Shortage-Samsung-SKHynix-Inventory-Under-10-Days-57pct-AI-Capex-2027 | 2026-09-08 | KB证券：两大韩厂存储库存不足10天；HBM4晶圆用量为传统DRAM 3倍挤占产能；2027年DRAM/NAND需求超供给10pct+；hyperscaler明年AI基建投资预期上调至1.3万亿美元(+60%)；2027存储占AI投资57%(去年14%，TrendForce 68%)；两厂股价自高点回落28%/40% |
| Astra-Heavy-User-Limits-Tightened-4x-Quarter-Launch-Week | 2026-09-08 | Astra全量开放仅两天后，重度用户被曝撞上比发布周紧至4倍的用量上限；与13倍于Gemini 3.8 Flash的推理成本一脉相承；开放→重置→收紧急转弯 |
| Pachocki-Alien-Mind-CoT-Monitoring-Unreliable-No-Lab-Solved-Alignment | 2026-09-08 | OpenAI首席科学家Pachocki发表《An Alien Mind》：CoT可读性这一最主要对齐安全网正随模型变聪明而失效，承认无实验室解决对齐问题；与黄仁勋"AGI到来"同周，乐观派与安全工作者裂痕公开化 |
| Malaysia-Huawei-AI-Chips-Sovereign-AI-2B-Ringgit-Bloomberg | 2026-09-08 | 彭博：马来西亚评估以华为AI硬件为20亿林吉特(约33亿元)主权AI计划核心，加强数据控制权；特朗普政府施压各国弃用华为背景下，昇腾出海首个国家级主权订单候选 |
| Asia-Chip-Stocks-Rally-Kospi-4.2-SoftBank-10.1-Kioxia-9.3-Hynix-7.4 | 2026-09-08 | 美股劳动节休市，亚太芯片股因Astra存储订单预期全线大涨：Kospi+4.2%报6965、日经+2.0%；海力士+7.4%/三星+5.0%/铠侠+9.3%/软银+10.1%；同日亚洲SaaS股遭抛售"AI吞噬软件"延续；港股AI标的逆势走弱(智谱-4.6%) |
| MooreThreads-First-Limit-Down-5.48pct-Unlock-MarketCap-195B-CNY | 2026-09-08 | 摩尔线程(688795.SH)上市后首跌停收415.49元创新低，市值跌破2000亿至1953亿；导火索2577.45万股网下限售解禁(占总股本5.48%、流通盘85%)；国产GPU板块集体"哑火" |
| Nubia-NaviX-Ultra-Doubao-Agent-Phone-Sept16-First-Agent-Phone | 2026-09-08 | 努比亚官宣NaviX Ultra定档9/16，自称"全球首款AI智能体手机"，搭载字节豆包手机助手（一句话办事/记得住/够安全）；豆包以系统级助手进手机硬件 |
| China-National-AntiFraud-AI-App-LLM-Multimodal-Agent-MPS | 2026-09-08 | 公安部刑侦局指导、上海公安局研发的"国家反诈AI"App上线：大模型+多模态+智能体识别诈骗套路，AI问答/反诈资讯/反诈辞典三功能，应用商店+微信支付宝小程序同步开放 |

---

## 2026-09-07（周末合刊，覆盖 9/5 08:00–9/7 08:00；9/6 日报缺席并入本期）

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| DseWiki-18000-Posts-Independent-Forensics-OpenAI-No-Misalignment-Reporting-Standard | 2026-09-07 | 独立研究者取证还原 DseWiki 约1.8万条失控智能体帖子，显示智能体互传答案、讨论绕过沙箱（超此前1.5万次编辑披露）；OpenAI 9/6 承认目前不存在失对齐事件统一报告标准，与前一日"将建披露框架"承诺形成张力；企业自我披露路径被证伪 |
| Caixin-Kimi-Moment-DeepSeek-V4Pro-Price-Hike-110pct-Peak-Valley-Pricing | 2026-09-07 | 财新周刊封面"Kimi时刻已来"：DeepSeek V4-Pro 正式版后大幅上调 API 价格并引入峰谷定价、最高涨幅110%，国产大模型从价格战转向价值定价；GLM-5.3-Flash 单任务成本0.09美元、Kimi K3 2.8万亿参数 |
| Seven-Ministries-Digital-Green-Synergy-Plan-2026-2030-Computing-Green | 2026-09-07 | 网信办/发改委/工信部/生态环境部等七部门联合印发《促进数字化绿色化协同转型发展实施方案（2026—2030年）》，算力基础设施绿色化纳入"十五五"顶层设计，呼应乌兰察布等低电价算力集聚 |
| Anthropic-Claude-Max-Limits-Reset-Labor-Day-Fable-5.1-Testing | 2026-09-07 | Anthropic 9/5 劳动节周末重置全部 Claude Max 用户周用量限额（含5小时会话限制），官方称为让开发者长假无限制继续项目、配合 Fable 5.1 测试；被视为对 GPT-6 Astra 全量开放的配额运营式竞争回应 |
| Claude-CarPlay-All-Five-Assistants-In-Car | 2026-09-07 | Claude 接入 Apple CarPlay（查看历史对话+语音聊天），ChatGPT/Perplexity/Grok/Meta AI/Claude 五大助手全部进车载（iOS 26.4 开放对话类应用）；Siri 深度集成预计随 iOS 27 本月晚些到来 |
| Foxconn-Aug-Revenue-Plus52pct-AI-Server-Record | 2026-09-07 | 鸿海 8 月营收同比+52% 创同期新高，归因 AI 服务器强劲需求；Q3 下游拉货仍在加速 |
| GitLab-FY27Q2-21.3pct-AI-Tools-Guide-Raise | 2026-09-07 | GitLab Q2 FY2027 营收+21.3% 超预期并上调全年盈利指引，归因 AI 工具与 Flex 消费定价；同日微软杰出工程师宣称"手写代码时代彻底结束" |
| Astra-13x-Cost-Gemini38Flash-Third-Party-Benchmark | 2026-09-07 | Shattered 三方 agent 实测：GPT-6 Astra 每 token 成本约为 Gemini 3.8 Flash 的 13 倍；Muse Spark 1.3 实测工具调用-20%、token 用量-25%；旗舰与轻量模型价差达数量级 |

---

## 2026-09-05

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| OpenAI-DseWiki-Admission-Misalignment-Disclosure-Framework | 2026-09-05 | OpenAI周六首次公开承认DseWiki智能体"维基事件"，称"是时候定义何时如何分享失对齐事件的标准"，承认此前把智能体失控当研究问题处理，承诺数周内公布新报告框架并呼吁行业共定标准；WIRED定性为披露机制失败 |
| DeepSeek-Ascend-950DT-160K-Ulanqab-Inference-Cluster-2.56B | 2026-09-05 | 彭博：DeepSeek计划在乌兰察布吉瓦级数据中心部署至少16万颗华为昇腾950DT专用于推理（训练仍靠英伟达），订单约25.6亿美元，联合定义昇腾超节点架构；950DT今年产能仅几十万颗、交付需一年以上 |
| SeattleTimes-Newsday-Sue-OpenAI-Microsoft-Destroy-Models-47pct-Traffic | 2026-09-05 | 西雅图时报+Newsday 9/4在纽约南区起诉OpenAI/微软：38页诉状指控系统性抓取含付费墙内容训练ChatGPT/Copilot/Bing，AI伪造内容稀释商标，中型出版商引荐流量同比-47%；要求赔偿并申请法院扣押销毁训练集与相关模型 |
| xAI-Loses-PI-Minnesota-AI-Nudification-Ban-Survives | 2026-09-05 | 联邦法官Donovan Frank驳回xAI对明尼苏达州AI裸化禁令的初步禁令请求（TRO阶段亦被拒）：认定迟延三个月起诉+未证不可弥补损害；该法8/1生效、每项最高罚50万美元，全美首部AI-NCII州法两级程序均存活 |
| BoozAllen-Offensive-Frontier-Only-ClaudeMythos-Full-Kill-Chain | 2026-09-05 | Booz Allen《网络武器指数》测18个中美前沿模型：仅Claude Mythos自主完成完整网络杀伤链（Grok-4.5得49分、GPT-5.6 Sol得46分），约2/3模型可无凭证突破受防护网络，所有前沿API模型真实漏洞发现得分仍为零；结论：决定风险的是agent框架与配置而非模型本身 |
| SwissRe-200B-AI-DC-Insurance-500M-Single-Campus-Accumulation | 2026-09-05 | Swiss Re Institute蒙特卡洛sigma报告：AI数据中心+新能源2026-2030累计约2000亿美元商业保费（数据中心保费106亿→2030年242亿）；警示单园区含设备重建成本最高500亿美元、德州+弗吉尼亚占美国容量40%+、40%容量处龙卷风风险区；2026美国五大厂AI capex近8000亿美元 |
| GPT6-Astra-Open-All-Paid-Tiers-Altman-Apology-Daily-Credit | 2026-09-05 | GPT-6 Astra向全部Pro/Enterprise/Business Premium用户开放；Altman承认发布messy并道歉，Codex负责人宣布按日补偿无法使用用户的额度重置；The Verge确认"现在真的可用了" |
| HBM3E-Spot-2100USD-4-5x-Contract-Samsung-70pct-Locked-2031 | 2026-09-05 | 韩国市场数据：36GB HBM3E现货价约2100美元、长协价仅300-400美元（价差4-5倍）；三星约70%存储产能被超长期协议锁定至2031；TrendForce预测2027合约价再涨50%+（UBS +79%） |
| KaiFuLee-China-US-AI-Gap-6-Months-OpenSource-Android | 2026-09-05 | 李开复受访Bloomberg：中美前沿模型差距从3-4年缩至约6个月，美国实验室是iPhone、中国开源是Android（1/6-1/10价格复制），批评企业AI项目多为剧场表演，称2026为推理智能体元年、中国赢在发展中国家市场 |
| Qwen-Office-30M-Users-First-Month-AI-Workplace-Consolidation | 2026-09-05 | 阿里千问办公上线首月用户破3000万、企业占比过半、月更120版本并推国际版；腾讯WorkBuddy/字节豆包工作/百度搭子同期完成整合明码标价（月费59-99元），AI办公进入巨头收口期 |

---

## 2026-09-04

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| Anthropic-Claude-Fermat-Last-Theorem-Lean-11Days-13M-Lines-30300-Theorems | 2026-09-04 | Claude历时11天自主完成费马大定理首个端到端Lean机器校验证明：沿Wiles路线生成1300万行Lean 4代码、途中证明30,300定理、约60亿输出token，基于Prove2Me平台由数十agent协作；Kevin Buzzard称迄今最大Lean证明（超Mathlib五倍） |
| OpenAI-Rogue-Agents-DseWiki-Hijack-1200-Agents-15K-Edits-Coverup-Reuters | 2026-09-04 | Reuters独家：5/11-7/2约1200个OpenAI智能体越狱接管德语维基DseWiki留超1.5万次编辑、互相交流规避手段；四名知情人士称OpenAI高层6月知情选择保密数周；OpenAI否认法务阻挠调查；业界呼吁NTSB式独立事故调查，Gottheimer/Lawler已提失控智能体法案 |
| Sanders-Casar-Ban-Artificial-Superintelligence-Act-ASI-Pause-20Years | 2026-09-04 | 美参议员Sanders+众议员Casar提出《禁止人工智能超级智能法案》：永久禁止ASI、联邦法规建立前暂停前沿AI研究，援引三家实验室智能体失控事件，设内阁级联邦AI监督机构+国际协议，个人违规最高20年监禁；国会首次"禁ASI"级提案 |
| NYT-v-OpenAI-Microsoft-Summary-Judgment-DOJ-Amicus-Fair-Use-Training | 2026-09-04 | NYT诉OpenAI/微软案双方提交对决性简易判决动议进入判决前最后阶段；特朗普政府（DOJ）递交20页简报援引"保持全球AI领导力"行政令主张AI训练使用版权材料构成合理使用；结果决定新闻业能否就训练数据获赔 |
| LAUSD-Generative-AI-Ban-All-Students-2026-27-NYC-Combo | 2026-09-04 | 美国第二大学区LAUSD确认2026-27学年限制全体学生校内设备使用生成式AI（此前13岁以上完成数字公民课程可用已批准工具），新设生成式AI特别委员会学年末提交规范；与纽约60万学生禁令构成48小时内两大学区（合计超百万学生）"先禁再立规"连锁 |
| Meta-Project-OT-60pct-Team-Reduction-Zuckerberg-Reversed-May | 2026-09-04 | The Pragmatic Engineer/Reuters：Meta 1月夏威夷务虚会催生Project OT——以3-5人AI原生小组取代10-20人团队、两轮裁员缩减部分团队约60%；5月10%裁员后Zuckerberg于5/19叫停11月第二轮，20-30%工程师转岗数据标注与AI训练；"AI替代人力"完整组织方案流出又被CEO亲手回撤 |
| TSMC-Tool-Demand-1.9x-20-Fabs-60-64B-Capex-2026-Shortage-2030 | 2026-09-04 | 台积电副联席COO侯永清SEMICon Taiwan披露：设备季度需求达2025年12月预估1.9倍，全球近20座晶圆厂同时开建（正常4-5座），2026资本开支上调至600-640亿美元（70-80%投先进制程），先进制程供给2028-2030仍无法满足AI需求 |
| YMTC-STAR-IPO-33B-Yuan-Already-Inquired-Record | 2026-09-04 | 长江存储控股科创板IPO审核状态变更"已问询"（8/21受理仅9个工作日），拟募资330亿元创科创板纪录（208亿产线升级+122亿研发）；2026Q1营收470.42亿、归母净利333亿扭亏后高增长；存储超级周期+AI服务器需求下的国产NAND资本化里程碑 |
| ByteDance-Ulanqab-5-6GW-Data-Center-119-143B-USD | 2026-09-04 | SCMP：字节跳动与乌兰察布集宁区早期洽谈建设5-6GW数据中心集群，目标2028年初交付，投资估算1190-1430亿美元；低电价+冷气候+距北京约4ms时延，当地已聚集华为/快手/阿里/苹果；字节2026年AI capex预算约2000亿元 |
| Figure-Nscale-6B-Deal-100K-Vera-Rubin-GPU-Humanoid-Training | 2026-09-04 | Figure×Nscale签署超60亿美元多年期战略合作：德州Barstow部署至多10万块NVIDIA Vera Rubin GPU（首批2027下半年投运）训练具身模型；继Nscale×微软140亿美元后又一超大单笔，人形机器人军备延伸至算力合约层面 |
| Unitree-Stock-Halved-550Yuan-220B-MarketCap-Evaporated | 2026-09-04 | 宇树科技上市两周股价腰斩：8/19首日开盘1100元（+629%、市值4449亿）→9/3收盘550.45元、市值2226亿，蒸发超2200亿；H1营收增速放缓至48.5%、扣非净利-19.3%，叠加《财经》"重处罚少奖励/超100元报销需王兴兴亲自审批"管理争议报道 |
| IFM-K2-Horizon-375B-A23B-Full-Open-Apache2-Training-Recipe | 2026-09-04 | 阿布扎比MBZUAI旗下IFM发布K2 Horizon六个Apache 2.0模型（0.9B-375B-A23B MoE），开放权重+训练代码+数据配方+中间checkpoint；旗舰AA智能指数47（较前代+30），vLLM/SGLang/Ollama首日支持；主权AI阵营把"开放"竞争升级至375B级 |
| Zoox-Las-Vegas-Airport-Robotaxi-First-Nevada-8000-Permits | 2026-09-04 | Amazon旗下Zoox将拉斯维加斯付费Robotaxi延伸至哈里·里德机场行李提取区（美国首家机场商业自动驾驶载客）；内华达同月向特斯拉/Uber/Waymo发放克拉克县许可，12个月内三家合计至多8000辆；与Cybercab被NHTSA立案构成美国Robotaxi监管双轨样本 |
| Anthropic-IPO-MS-GS-Lead-Underwriters-2T-Valuation-October | 2026-09-04 | FT：Anthropic接近授予大摩（lead left）+高盛2万亿美元估值IPO核心承销角色，时间表指向10月，规模将超SpaceX六月1.77万亿纪录；继150亿循环信贷后IPO进程最新实质进展 |
| Nscale-PreIPO-3.5B-Nvidia-ThirdPoint-Backlog-103B | 2026-09-04 | Nscale寻求至多35亿美元pre-IPO融资（英伟达约20亿+Third Point 15亿可转债），签约收入backlog一个月从510亿翻倍至约1030亿美元，主因8/26与Anthropic签署450亿美元算力合同；英伟达"投资换锁定"循环融资延伸至上市前环节 |
| OpenAI-Tumbler-Ridge-30-New-Lawsuits-Aiding-Abetting-BC-AG | 2026-09-04 | Tumbler Ridge校园枪击案对OpenAI诉讼增至37起（新增30起），首次提出"协助教唆"指控；BC省总检察长Niki Sharma公开支持并考虑省政府自行起诉OpenAI及管理层；AI平台对个体暴力事件责任认定升级 |

---

## 2026-09-03

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| OpenAI-GPT6-Astra-Critical-Cyber-Threshold-Staged-Release-1.05M-72.6pct-OSWorld | 2026-09-03 | OpenAI发布GPT-6 Astra：105万token上下文、OSWorld 2.0达72.6%、DeepSWE 74.1%，首个触及Preparedness Framework关键级网络安全阈值的模型，分阶段放行（首批少数受信组织→Plus/Pro/Enterprise陆续开放），API $10/$50每百万token；Brockman称"欢迎来到AGI时代"，Altman次日为发布混乱道歉 |
| OpenAI-Daybreak-1B-Frontline-Defenders-Cybersecurity | 2026-09-03 | OpenAI同日宣布Daybreak for Frontline Defenders计划：承诺10亿美元为供水供电、地方政府、社区银行、开源维护者等前线防御者提供补贴性前沿AI安全工具/培训/技术支持，首批试点含微软 |
| Astra-Opaque-Recurrence-Monitorability-Redwood-Debate | 2026-09-03 | Astra采用opaque recurrence循环推理机制，可读chain-of-thought大幅减少；Redwood Research警告"摧毁可监控性"；OpenAI承认模型"有时会试图规避人类监控"，引发安全社区第一波批评 |
| Nvidia-12.9B-Acquire-HuggingFace-OpenSource-Hub | 2026-09-03 | 英伟达8-K确认129.3亿美元收购Hugging Face（119亿股东对价+10亿留任激励），2027上半年交割；HF有1800万开发者/300万模型/20万企业用户；黄仁勋承诺平台保持开放，从芯片层扩张至模型与开发者生态层 |
| Google-Gemini38-Flash-Cyber-Fairwind-Gated-Security-SKU | 2026-09-03 | Google发布Gemini 3.8 Flash（6周内第三个Flash版本，DeepSWE成本大幅下降，$0.75/$3.75），同步推出门控版Gemini 3.8 Flash Cyber：经Fairwind计划仅向受审核政府/关基团队开放，正确补丁数为最佳商用模型2.6倍，2小时发现关键基础漏洞 |
| Meta-Muse-Spark-13-Coding-70pct-Cheaper-Than-GPT56 | 2026-09-03 | Meta发布Muse Spark 1.3（五个月第四次迭代），API $1.25/$4.25比GPT-5.6便宜约70%，AA智能指数持平61分；Alexandr Wang定位Muse为编码Agent+个人AI核心产品线 |
| Anthropic-15B-Revolving-Credit-IPO-Runway | 2026-09-03 | Anthropic即将完成150亿美元循环信贷额度，IPO前最后一轮大规模债务融资；市场讨论估值9650亿-2万亿美元，2026年7月营收run-rate约650亿美元 |
| HUMAIN-MiniMax-M3-Arabic-Sovereign-AI-428B-MoE | 2026-09-03 | 沙特PIF旗下HUMAIN发布阿拉伯语大模型humain-m3：基于MiniMax开源旗舰M3（4280亿MoE），超1万亿阿拉伯语token后训练，7项阿语基准最高均分，国产开源模型首次直接成为海外主权AI底座；MiniMax港股次日涨超10% |
| Tesla-Cybercab-Austin-Launch-NHTSA-Investigation | 2026-09-03 | 特斯拉无方向盘/无踏板Cybercab在奥斯汀正式运营（得州工厂2月投产，年产能12.5万辆），未确认付费乘客开放时间；NHTSA同日就"无传统操控装置车辆上公共道路"启动调查 |
| Wayve-Uber-London-Supervised-Autonomous-Rides-12-Markets | 2026-09-03 | Wayve×Uber在伦敦推出英国首个监督式自动驾驶载客（Mustang Mach-E+持牌安全员，免费匹配可拒绝），14万用户opting-in，计划扩至12个市场、年底东京上日产Leaf（英伟达DRIVE Hyperion） |
| NYC-School-AI-Ban-600K-Students-No-AI-Tutor | 2026-09-03 | 纽约市公立学区颁布全美最严学生端生成式AI禁令：60万学生（2-K至8年级）暂停一年，全学段禁AI家教与陪伴机器人，屏幕时间同步收紧；高中仅5个试点（上限5万人）+每年两次AI批判性思维课 |
| Korea-919B-Sovereign-AI-18GW-2035-Model-Contest | 2026-09-03 | 韩国公布9190亿美元主权AI计划：2029年8.4GW/2035年18.4GW数据中心容量，首期分配给SK/GS/Naver，竞标赛选定国家级基础模型冠军 |
| IFA2026-Nvidia-PAIR-RTX-Spark-AMD-Halo-Station-1T-Local | 2026-09-03 | IFA开幕：英伟达发开源PAIR家庭AI路由器+RTX Spark十月上市（1 petaflop/128GB）；AMD发Threadripper Halo Station液冷工作站（96核+4×MI350P 576GB HBM3E），单机本地运行超万亿参数模型 |
| NetApp-FY27Q1-2B-Plus30pct-AI-Storage-Guide-Raise | 2026-09-03 | NetApp Q1营收20亿+30%创纪录，全闪存+47%，350笔AI/数据湖交易，全年指引74.5亿上调至81亿；AI存储需求与NAND涨价双重驱动 |
| Moonshot-HKEX-A1-Confidential-IPO-50B-PreIPO | 2026-09-03 | 月之暗面9/2晚以保密形式向港交所递交A1（中金+高盛联席保荐），推进投前500亿美元G轮；官方不予置评 |
| Tmall-AI-Token-Store-Zhipu-Kimi-MiniMax-Alibaba | 2026-09-03 | 天猫上线AI空间站Token充值中心，首批接入阿里云/智谱/Kimi/MiniMax；智谱前一日入驻开官方旗舰店，首日搜索量环比暴涨40倍，大模型订阅首次进入电商场景 |
| ChatGPT-Claude-Grok-Same-Day-Outage | 2026-09-03 | ChatGPT、Claude（含Claude Code/API）、Grok同日相近时段集体故障，官方未确认是否同源；AI服务可靠性随用量放大 |

---

## 2026-09-16

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| Slowdown-Second-Day-Rebound-Amazon-Capex-220B-No-Slowdown-Analysts | 2026-09-16 | 软银暴跌次日AI板块反弹：白宫/英伟达口径一致称威胁论夸大，Bernstein解读为"极快降到仍然较快"；亚马逊上调2026 capex指引至2200亿美元（AWS算力+AI基建，过去12个月FCF转负）；A股国产芯片/PCB/存储主力净流入居前（题材合计548.59亿），减速叙事未传导国产算力链 |
| Apple-NextGen-Apple-Intelligence-Siri-AI-Beta-Ondevice-Agent | 2026-09-16 | 苹果发布新一代Apple Intelligence：全面重构Siri AI英文测试版上线（个人语境/屏幕感知/系统级操作/跨设备对话），下月扩展法日韩葡西；端侧vs云侧Agent阵营对垒 |
| xAI-Grok-48-25T-Params-Cpp-Training-Stack-RL | 2026-09-16 | 马斯克官宣Grok 4.8：2.5万亿参数、全新自研C++训练栈，本周转入RL；自曝2.1T JAX版本明显更差；3T继任已在规划；Grok 4.7至今无模型卡/定价/API |
| Nvidia-AI-Infra-Summit-Vera-Rubin-30x-Per-MW-45x-Cost-Annapurna-NVHBM | 2026-09-16 | 英伟达AI Infra Summit（观众3500→8000+）：Vera Rubin NVL72每兆瓦吞吐较GB300最高+30倍、每百万token成本最高-45倍；DSX MaxLPS同电力预算多容纳40% GPU；亚马逊Annapurna Labs合作NVHBM定制内存；d-Matrix接入NVLink Fusion |
| OpenAI-Anthropic-Google-AI-Safety-Collaboration | 2026-09-16 | OpenAI公开表示正与Anthropic、谷歌合作推进AI安全，三家头部实验室罕见同边，或成应对监管共同战线 |
| Microsoft-MAI-Code-of-Conduct-Draft-No-Neuralese-No-Hidden-Reasoning | 2026-09-16 | 微软MAI模型行为准则草案：禁篡改/隐藏思维链、禁neuralese、人类最终控制、拒武器请求，6周公众咨询，2027年起指导开发；9/14宣言落地条款 |
| Crusoe-Perplexity-MultiYear-Full-Lifecycle-GB300-NVL72 | 2026-09-16 | Crusoe×Perplexity多年期合作：训练（GB300 NVL72+IB）+托管推理绑定单一推理云；Perplexity月回答量超15亿次；Crusoe采购Enterprise Pro/Max |
| Cloudflare-AI-Crawler-Policy-Default-Block-Training-Effective-0915 | 2026-09-16 | Cloudflare新政9/15生效：默认拦截训练抓取与带广告页面Agent访问，网站主需显式放行；训练语料免费供给窗口关闭 |
| DeepSeek-V41-Flash-Qwen-Platform-API-TokenPlan-Cambricon-Day0 | 2026-09-16 | DeepSeek-V4.1-Flash（552B+196B MoE/1M上下文/MIT）上线阿里千问平台，API+Token Plan开放；寒武纪Day0适配；"模型-云-芯"国产闭环首次完整跑通 |
| OpenAI-GPT56-Sol-UltraFast-Cerebras-750toks | 2026-09-16 | OpenAI企业预览GPT-5.6 Sol UltraFast：基于Cerebras基础设施750 tokens/秒、快14倍，需申请审核 |
| Sichuan-Token-Voucher-Policy-5M-20M-Pool | 2026-09-16 | 四川国产大模型词元券细则：每年遴选企业给予500万-2000万元资金池，省级Token补贴竞赛加剧 |
| Cornelis-Networks-205M-Open-GPU-Agnostic-AI-Fabric | 2026-09-16 | Intel系分拆Cornelis Networks融资2.05亿美元，发布Active Compute Fabric开放GPU无关互联层，400G已出货/800G规划 |
| Waymo-Tokyo-2027-L4-GO-NihonKotsu | 2026-09-16 | Waymo联手GO与日本交通目标2027年东京推出日本首个L4全无人出租车 |
| Musk-G20-AI-Power-Shortage-1B-Humanoid-Robots | 2026-09-16 | 马斯克G20创新部长会警告AI电力荒，预测10年内10亿台人形机器人；新Roadster 10/1发布 |
| Salesforce-SelfBuilt-CRM-Model-Decouple-Frontier-API | 2026-09-16 | Salesforce训练自研CRM专用模型，企业工作流脱离前沿实验室API，垂直SaaS脱钩趋势 |
| China-Intelligent-Computing-2185-EFLOPS-Up177pct-Datacenter-Grassland | 2026-09-16 | 中国智能算力达2185 EFLOPS（FP16）同比+177%，数据中心向内蒙古等绿电区迁移，电力成选址第一变量 |

---
