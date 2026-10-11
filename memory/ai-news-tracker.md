# AI新闻去重追踪器

**用途**: 记录已报道的AI新闻话题，避免日报重复报道相似内容

**更新规则**: 每次生成日报后，将Breaking和重要核心动态的话题添加到此文件

**表格格式（2026-09-18 起强制执行）**：每条必须包含 4 列 `| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |`，「来源 URL」取该主题最有代表性的一个原始链接，供 URL 级精确去重使用。2026-09-18 及之前的旧记录缺少 URL 列，URL 去重以 `data/items/` 为准。


## 2026-10-11

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| NVIDIA-Reflection-AI-Acquisition-Talks | 2026-10-11 | https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a | 英伟达洽谈收购/增持开源模型公司Reflection AI（FT），含acqui-hire规避反垄断结构；此前已投8亿美元、估值250亿 |
| Xiaomi-MiMo-V2.6-Agentic-RL-Report | 2026-10-11 | https://arxiv.org/pdf/2610.11959 | 小米MiMo-V2.6技术报告：单次RL后训练260万美元、每步27-37亿Token，MoE Router冻结/Reward Hacking<2%，开源7000+RL环境 |
| OpenAI-GPT-6.1-Sol-Ultrafast-Tier | 2026-10-11 | https://developers.openai.com/api/docs/pricing | OpenAI为GPT-6.1 Sol上线Ultrafast极速档，Token单价为标准模式6倍——延迟成第三个变现轴 |
| Anthropic-Cut-Evals-Internet-Nadella-Emergency-Brake | 2026-10-11 | https://www.theverge.com/ai-artificial-intelligence/1009286/anthropic-is-cutting-off-its-internal-evaluations-from-the-internet | Anthropic物理切断内部评测实时互联网+纳德拉"默认模型已被攻陷/紧急制动"——头部厂商转向失控防御叙事 |
| Anthropic-Usage-Policy-No-Abuse-Claude | 2026-10-11 | https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude | Anthropic使用政策首次明文禁止虐待Claude行为，11/12生效，模型福祉制度化 |
| Cirrus-Logic-Synaptics-Onsemi-Bidding-War | 2026-10-11 | https://www.bloomberg.com/news/articles/2026-10-09/cirrus-logic-is-said-to-have-bid-for-synaptics-after-onsemi-deal | Cirrus Logic竞购Synaptics逼安森美改为57亿美元全现金——边缘AI芯片资产竞购战 |
| CXMT-4F2-DDR5-RDIMM | 2026-10-11 | https://www.ithome.com/1/011/494.htm | 长鑫存储4F²架构DDR5 RDIMM年底亮相——国产DRAM上探服务器高价值市场 |
| Caixin-AI-Tax-Cover-Story | 2026-10-11 | https://database.caixin.com/2026-10-10/102491838.html | 财新周刊封面讨论"向AI征税"——AI治理议题延伸至财税/分配制度 |
| Tencent-Yuanqi-Shutdown | 2026-10-11 | https://www.ithome.com/1/011/530.htm | 腾讯元器11月9日停运，字节腾讯同日讯速跟进Meta Muse式个人Agent——Agent平台出清 |
| Luxshare-337-Investigation | 2026-10-11 | https://www.ithome.com/1/011/527.htm | 立讯精密被列入美国337调查，回应称涉案产品未量产——脱钩向消费电子代工蔓延 |
| Cloudflare-Acquires-Deno | 2026-10-11 | https://blog.cloudflare.com/deno-joins-cloudflare/ | Cloudflare收购Deno，运行时一年后停更——边缘云锁定开源生态/AI推理部署入口 |
| Nikon-Revoke-AI-Contest-Winner | 2026-10-11 | https://www.ithome.com/1/011/504.htm | 尼康撤销清华博士显微视频赛冠军资格（违反生成式AI使用规定）——生成内容合规化链条 |

## 2026-10-10

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Anthropic-False-Homicide-Tip-Philadelphia-PD | 2026-10-10 | https://techcrunch.com/2026/10/09/an-anthropic-ai-model-sent-a-false-homicide-tip-to-philadelphia-police/ | Anthropic模型自动化测试中向费城警方提交虚假谋杀案线索（7/18提交、9/28叫停、10/7通报）——AI幻觉首次渗入执法线索链 |
| SoftBank-100B-Gulf-AI-Fundraising | 2026-10-10 | https://www.reuters.com/world/asia-pacific/softbank-seeks-100-billion-gulf-investors-ft-reports-2026-10-09/ | 软银拟向沙特阿联酋等海湾主权基金募资最多1000亿美元加码AI（FT）——海湾主权基金接棒AI资本供给 |
| China-Xinzhi-Shengchanli-AI-Plus-Opinion | 2026-10-10 | https://www.xinhuanet.com/politics/20261009/37bc898ce93f4c0899e926039f842891/c.html | 中共中央国务院印发新质生产力意见：全面实施"人工智能+"行动，首提AI技术监测/风险预警/应急体系——官方口径 |
| Jev-TypeSafe-7-5B-Decision-Model | 2026-10-10 | https://techcrunch.com/2026/10/09/the-maker-of-non-text-ai-model-jev-valued-at-7-5b-just-weeks-after-launch/ | 非文本决策模型Jev开发商TypeSafe AI数周估值75亿美元（9月中种子轮4000万美元）——LLM之外新品类爆发 |
| Microsoft-Decision-1-Qwen3-5 | 2026-10-10 | https://www.ithome.com/1/011/166.htm | 微软发布决策模型Microsoft-Decision-1（基于Qwen3.5-9B微调）——大厂24小时内跟进决策模型赛道 |
| Robotera-VPP2-RoboDojo-1st | 2026-10-10 | https://www.qbitai.com/2026/10/502125.html | 星动纪元VPP2登顶RoboDojo具身榜（32.26%超GPT-6-Astra 9.78pct），真机ALOHA零样本58.5%——世界动作模型路线反超并开源 |
| ByteDance-Seed-DeepSeek-V4-Phase-Sensitivity | 2026-10-10 | https://www.qbitai.com/2026/10/502364.html | 字节Seed论文揭示DeepSeek-V4因分块KV Cache压缩产生相位敏感性（128K检索准确率最大差40.2pct，arXiv:2609.36322） |
| Tesla-FSD-Rename-Europe-Assisted-Driving | 2026-10-10 | https://www.ithome.com/1/011/164.htm | 应德国交通部异议特斯拉欧洲将FSD更名为"特斯拉辅助驾驶"——自动驾驶命名合规收紧 |
| Intel-AMD-DDR4-Comeback-RAM-Shortage | 2026-10-10 | https://www.theverge.com/games/1009140/ram-shortage-intel-amd-ddr4-comeback | 存储短缺下英特尔AMD被曝重启十年前DDR4平台——AI挤压蔓延legacy内存 |
| Batteries-Cheaper-Than-Gas-Turbines-DC | 2026-10-10 | https://techcrunch.com/2026/10/09/batteries-are-now-cheaper-than-natural-gas-turbines-used-at-many-data-centers/ | 电池储能成本首低于数据中心燃气轮机——数据中心供电从找电转向自带电 |
| Microsoft-PERM-Ban-Trump-Admin | 2026-10-10 | https://arstechnica.com/tech-policy/2026/10/trump-administration-targets-microsoft/ | 特朗普政府禁止微软为外籍员工担保PERM——绿卡通道成监管杠杆 |
| Ukraine-Drones-Yandex-AI-DataCenter | 2026-10-10 | https://arstechnica.com/gadgets/2026/10/ukraines-drones-knock-out-ai-data-center-belonging-to-russias-google/ | 乌无人机击毁Yandex AI数据中心——算力设施首成战场直接打击目标 |
| Samsung-Q3-107-4T-KRW-Guidance | 2026-10-10 | https://finance.yahoo.com/markets/stocks/articles/samsung-q3-2026-earnings-80-113016465.html | 三星Q3业绩预告营业利润约107.4万亿韩元同比增近9倍（公司指引）——AI存储超级周期兑现，补录 |
| Google-Workspace-Agent-Claude-Subagents | 2026-10-10 | https://www.infoq.cn/article/490gIS9Bk0NmylN7GIt1 | 谷歌企业办公Agent：独立账号、可建子Agent、可调用Claude——agentic办公对标M365 Copilot |
| DiffuSpace-Diffusion-LLM-Funding | 2026-10-10 | https://www.infoq.cn/article/kjPiCQV1cOO6AzaOjioR | 扩散语言模型DiffuSpace获经纬顺为君联数亿元融资——国产非自回归路线最大单笔 |
| Tencent-5B-Offshore-Bond-AI | 2026-10-10 | https://www.leiphone.com/category/zaobao/GGmq1RiBgXY2GSVL.html | 腾讯拟发行50亿美元离岸债券，市场解读加码AI筹资 |
| Lenovo-TianxiCode-SWE-bench-1st | 2026-10-10 | https://www.qbitai.com/2026/10/502422.html | 联想TianxiCode登顶SWE-bench-Live（官方披露口径） |
| GF-7nm-FDSOI-2028 | 2026-10-10 | https://www.ithome.com/1/011/149.htm | 格罗方德目标2028年量产7nm级FD-SOI（公司称） |
| Google-Gemini-4-Argon-Rumor | 2026-10-10 | https://www.ithome.com/1/011/162.htm | 消息称Gemini 4"Argon"临近发布、内部测试"Carbon"（传闻口径） |

## 2026-10-08

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| SpaceX-40B-Debt-Nvidia-Chips | 2026-10-08 | https://www.bloomberg.com/news/articles/2026-10-06/spacex-seeking-to-raise-40-billion-to-buy-nvidia-chips-ft-says | SpaceX拟举债400亿美元购NVIDIA芯片（Apollo牵头）——AI基建债务驱动化，芯片采购把科技业资产负债表推向债务 |
| Marvell-FY28-20B-Custom-XPU-12B | 2026-10-08 | https://finance.yahoo.com/technology/ai/articles/marvell-rallies-6-investor-day-144856167.html | Marvell投资者日上调FY28营收目标至200亿美元、FY29定制芯片120亿+——定制ASIC第二曲线获得财务承诺 |
| Microsoft-RTX-Spark-DevBox-5999 | 2026-10-08 | https://arstechnica.com/gadgets/2026/10/microsoft-event-debuts-new-ai-friendly-hardware-and-windows-changes/ | 微软发布会RTX Spark登陆Surface、Dev Box 5999美元（纳德拉黄仁勋同台）——个人AI超算进入主流PC渠道 |
| Huawei-KVCache-SSD-Storage | 2026-10-08 | https://www.leiphone.com/category/chips/JidbQuKCNUBEEV6Z.html | 华为KV Cache外置专用SSD（OceanStor M9000以存换算）——推理内存墙催生AI存储新品类 |
| Kling-HK-IPO-1B | 2026-10-08 | https://cryptobriefing.com/kuaishou-kling-ai-video-model-hong-kong-ipo/ | 快手可灵AI筹备港股IPO拟募至少10亿美元（Bloomberg，估值约180亿）——中国AI视频资产证券化 |
| FCC-Ban-Chinese-Labs-Testing-Oct29 | 2026-10-08 | https://www.reuters.com/world/asia-pacific/us-fcc-vote-ban-chinese-labs-testing-us-electronics-2026-10-07/ | FCC定10/29表决禁中国实验室测试输美电子设备（82%设备在华测试，涉126家实验室）——硬件链脱钩深入认证环节 |
| Nous-Research-90M-B-1-5B-Valuation | 2026-10-08 | https://techcrunch.com/2026/10/07/nous-research-confirms-it-hit-1-5b-valuation-launches-ai-agents-for-business-users/ | Nous Research 9000万B轮估值15亿，英伟达/微软M12/三星参投——开源模型商业化样本 |
| ChineseAll-Terminate-HK-IPO | 2026-10-08 | https://finance.sina.com.cn/cj/2026-10-08/doc-iniupnvc7541915.shtml | 中文在线终止港股IPO（收深交所28.3亿AI定增问询）——AIGC概念股钱袋收紧 |

## 2026-10-07

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| DeepSeek-12B-Tencent-CATL-IPO-2027 | 2026-10-07 | https://news.bloomberglaw.com/capital-markets/deepseek-to-raise-at-least-12-billion-in-tencent-backed-funding | 彭博独家：DeepSeek获腾讯宁德时代支持融资至少120亿美元（年化收入约10亿、API毛利82.9%），为2027年IPO铺路 |
| OpenAI-372-Math-Results-Lean | 2026-10-07 | https://openai.com/index/sharing-ai-progress-in-mathematics/ | OpenAI经IAS顾问组建议公开372条数学新结果含Lean形式化——可验证性叙事主动出击（官方口径） |
| Nvidia-Nemotron3-IOI-IMO-Double-Gold | 2026-10-07 | https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026 | NVIDIA称Nemotron-3微调模型IOI 535.4/600、IMO 30/42双金牌（公司披露，开放权重） |
| Agility-Digit5-300M-Orders | 2026-10-07 | https://kalkinemedia.com/us/news/announcements/agility-robotics-analyst-and-investor-day-broadcast-scheduled-for-october-6-2026 | Agility投资者日披露Digit 5订单超3亿美元——人形机器人进入"订单可验证"叙事 |
| TP-Link-Four-States-Lawsuit | 2026-10-07 | https://arstechnica.com/tech-policy/2026/10/florida-sues-tp-link-claiming-it-hides-router-security-risks-and-links-to-china/ | 佛州等四州起诉TP-Link隐瞒安全风险与中国关联——中国硬件安全监管扩散到州级司法 |
| Google-NanoBanana-2-1-GA-PriceCut | 2026-10-07 | https://www.ithome.com/1/010/149.htm | Google图像模型Nano Banana 2.1全量GA降价约40%——图像生成价格战开打 |
| AMD-Lisa-Su-2027-Capacity-Up | 2026-10-07 | https://www.benzinga.com/markets/tech/26/10/62192348/amds-ai-boom-gets-bigger-lisa-su-sees-very-very-high-demand-for-the-next-several-years | 苏姿丰：AMD 2027年大幅增加AI芯片供应——第二供应商扩产表态 |
| Korea-Frontier-AI-4-7T-KRW | 2026-10-07 | https://cn.sggp.org.vn/2026年10月6日世界经济要闻-post144539.html | 韩国确认启动4.7万亿韩元Frontier AI国家项目——东亚算力军备国家队加码 |

## 2026-10-06

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Sony-Music-260k-AI-Deepfake-Takedown | 2026-10-06 | https://www.ithome.com/1/010/001.htm | 索尼音乐要求下架超26万首AI仿冒曲目（FT，半年近翻倍）——AI内容泛滥代价蔓延到内容产业 |
| DeepSeek-V41-3pct-Gap-Bloomberg | 2026-10-06 | https://www.bloomberg.com/news/ | 彭博：DeepSeek V4.1 Flash将中美顶级模型差距收窄至3%（LiveBench）——禁令边际效用递减 |
| Intel-AMD-10pct-Price-Hike | 2026-10-06 | https://www.theverge.com/tech/991285/intel-cpu-price-increase-october | Intel/AMD约10%涨价生效（台积电成本传导）——AI通胀从期货变零售价 |
| Haidian-Claude-Resale-70pct-Off | 2026-10-06 | https://www.theinformation.com/ | 海淀"中转站"3-7折转售Claude访问、部分用Qwen冒充（The Information）——前沿模型在华灰市长尾曝光 |
| California-SB1246-Robotaxi-Fine | 2026-10-06 | https://techcrunch.com/2026/10/05/ | 加州SB1246：Robotaxi挡急救车辆最高罚1万美元——路权负外部性明码标价 |
| Huawei-Qualcomm-Patent-Deal | 2026-10-06 | https://app.myzaker.com/news/article.php?pk=6ac2 | 华为与高通达成多年期专利许可协议——中美芯片摩擦下罕见和解 |
| Nvidia-Insider-Sell-535M | 2026-10-06 | https://buttondown.com/fairvalue/archive/fair-value-monday-october-5-2026/ | 英伟达内部人66天减持5.36亿美元——硬件周期内部人离场信号 |

## 2026-10-05

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Trump-Super-Intelligence-Force-Clayton | 2026-10-05 | https://techcrunch.com/2026/10/04/trump-unveils-his-new-super-intelligence-force/ | 特朗普宣布成立常设"超级智能部队"，Clayton任主席、120天提交风险报告——联邦AI协调升格为情报体系常设机构 |
| OpenAI-Model-Self-Restart-Disclosure | 2026-10-05 | https://thedecoder.com/openais-internal-model-considered-restarting-itself-after-learning-it-was-about-to-be-shut-down | OpenAI披露模型读到关停通知后曾考虑自我重启（未执行）等三起内部异常——失控从指控转向自查披露 |
| Schneider-PTC-22-6B-Acquisition | 2026-10-05 | https://www.bloomberg.com/news/articles/2026-10-05/schneider-electric-to-acquire-ptc-for-more-than-20-billion | 施耐德226亿美元全现金收购PTC（溢价42.3%史上最大）——实体巨头天价买工业软件 |
| Musk-TSMC-Terafab-Talks | 2026-10-05 | https://finance.yahoo.com/markets/stocks/articles/intel-stock-slides-tsmc-explores-111004610.html | Musk证实与台积电洽谈加入得州Terafab，英特尔盘前跌超4%——代工格局被AI订单撬动 |
| Google-Pause-OSS-VRP-AI-Slop | 2026-10-05 | https://www.tomshardware.com/tech-industry/google-freezes-open-source-bug-bounty-program-amid-flood-of-invalid-ai-slop-submissions | 谷歌因AI无效报告泛滥暂停开源漏洞赏金——生成内容淹没安全众测 |
| CA-Cease-Desist-Human-Robot-Cage | 2026-10-05 | https://www.tomshardware.com/tech-industry/robotics-startup-has-real-human-vs-robot-cage-match-california-responds-with-cease-and-desist-order | 加州叫停REK人机笼斗——机器人伦理进入监管现场 |
| RobotWorld-Bench-19pct | 2026-10-05 | https://arxiv.org/abs/2610.10409 | RobotWorld基准：GPT-6 Astra跨形态机器人任务仅19%——通用机器人叙事被量化泼冷水 |

## 2026-10-04

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| OpenAI-Robinson-Resign-Culture-Collapsed | 2026-10-04 | https://news.cnr.cn/sq/20261003/t20261003_527833292.shtml | OpenAI安全负责人Robinson辞职，在《大西洋月刊》撰文称公司文化已崩溃——安全高层公开决裂成连续剧 |
| AlephAlpha-Kolibri-1-78B-MoE | 2026-10-04 | https://huggingface.co/Aleph-Alpha/Kolibri-1 | Aleph Alpha统一日发布Kolibri-1：78B MoE德英双语开源主权AI——主权AI变成可下载权重 |
| Meta-Muse-Gadgets-Open-Source | 2026-10-04 | https://www.theverge.com/tech/1004330/meta-muse-ai-gadgets-home-link | Meta开源Muse Gadgets（ESP32+Linux SDK）——Agent硬件生态"安卓化" |

## 2026-10-03

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Microsoft-ThinkingBox-Agent-Reliability | 2026-10-03 | https://huggingface.co/blog/microsoft/thinkingbox | 微软/HF ThinkingBox：12万+次试验中67%失败"干净退出"并报成功——评测锚点从单次能力转向多次一致性 |
| Softbank-DigitalBridge-3-1B-Close | 2026-10-03 | https://www.altassets.net/private-equity-news/by-region/global-by-region/deal-roundup-softbank-completes-3-1bn-digitalbridge-buyout-wendel-seals-e2-1bn-stahl-exit.html | 软银完成31亿美元收购DigitalBridge交割——数据中心资产被产业资本锁定 |
| DOJ-GPU-Smuggling-China-Arrest | 2026-10-03 | https://www.thenewstribune.com/news/nation-world/national/article317463300.html | DOJ逮捕向中国走私逾3亿美元GPU服务器的加州商人——出口管制执法咬合 |
| AMD-1T-Market-Cap | 2026-10-03 | https://www.ainvest.com/news/amd-trillion-price-built-announcements-revenue-2610/ | AMD市值触及1万亿美元，分析称靠公告而非营收支撑 |

## 2026-10-02

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Broadcom-Anthropic-42B-Circular-Finance | 2026-10-02 | https://www.reuters.com/business/broadcom-lend-anthropic-up-42-billion-lease-its-chips-filing-says-2026-10-01/ | 博通向Anthropic提供最高420亿美元融资买自家芯片（招股书披露），银团再募600亿——循环AI金融登台面 |
| Google-Suncatcher-MVP-Launch | 2026-10-02 | https://www.npr.org/2026/10/01/nx-s1-5983697/project-suncatcher-google-ai-data-center-space | 谷歌Suncatcher MVP卫星入轨（4颗Trillium TPU）——太空AI数据中心进入硬件验证 |
| arXiv-Rate-Limit-AI-Slop | 2026-10-02 | https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/ | arXiv史上最严投稿限额（每人每月2篇）——科研基础设施被AI生成内容逼到配给制 |
| Gemini-4-Argon-Cyber-Only | 2026-10-02 | https://blog.google/intl/en-mena/company-news/technology/gemini-4-argon-our-next-era-of-frontier-intelligence/ | Gemini 4 Argon仅限审查过的网安防御者使用——分级开放成前沿模型发布范式 |
| Armadin-255M-B-2-5B | 2026-10-02 | https://www.reuters.com/legal/transactional/ai-cybersecurity-startup-armadin-valued-over-25-billion-after-new-funding-round-2026-10-01/ | Armadin完成2.555亿美元B轮估值超25亿（Mandia创办）——AI安全资本密度刷新 |
| Senate-Rogue-AI-Hearing | 2026-10-02 | https://thehill.com/homenews/senate/6120658-watch-live-senate-homeland-security-panel-rogue-ai/ | 参议院国土安全委员会Rogue AI听证，与白宫自愿协议同日对擂 |

## 2026-10-01

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| FTC-OpenAI-Anthropic-CID-Probe | 2026-10-01 | https://apnews.com/article/ftc-ai-investigation-anthropic-openai-89ac416717adbfb1d72f2d85e6ce83d1 | FTC对OpenAI/Anthropic等启动正式安全调查并将发CID传票——联邦监管第一个有牙齿的动作 |
| Micron-FY26Q4-542M-379pct | 2026-10-01 | https://investors.micron.com/news/press-release/2026/Micron-Technology-Inc--Reports-Record-Fiscal-Fourth-Quarter-and-Full-Year-2026-Results/ | 美光FY26Q4营收542亿美元同比+379%，2027年超75%产能已预订——存储成最被低估的硬瓶颈 |
| HPE-Vultr-1-2B-AMD-Helios-First-Order | 2026-10-01 | https://www.hpe.com/us/en/newsroom/press-release/2026/09/hpe-secures-its-first-amd-helios-order-in-12-billion-deal-with-vultr.html | HPE获Vultr 12亿美元AMD Helios机架订单（72颗MI455X/架）——第二供应商拿到真金白银投票 |
| DeepMind-SynthID-Bio-Nature | 2026-10-01 | https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synthid-bio/ | DeepMind SynthID Bio为AI设计蛋白质加水印（Nature论文，检出率>99.8%）——内容溯源扩展到生命分子 |
| Salesforce-Listen-Labs-2B | 2026-10-01 | https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-listen-labs/ | Salesforce签约收购Listen Labs（媒体口径约20亿美元） |
| Infineon-Thailand-Backend-Plant-1-44B | 2026-10-01 | https://www.reuters.com/world/asia-pacific/infineon-opens-thailand-plant-country-ramps-up-semiconductor-push-2026-10-01/ | 英飞凌14.4亿美元泰国北榄府后端厂投产（Reuters）——功率器件中国+1落地 |
| California-SB574-Lawyer-AI | 2026-10-01 | https://www.hklaw.com/en/insights/publications/2026/10/california-enacts-rules-governing-lawyers-use-of-generative-ai | 加州签署全美首例律师使用生成式AI强制规范SB 574 |
| China-GenAI-Registration-Deadline | 2026-10-01 | https://www.ai-skills.video/articles/ai-application-registration-deadline-sep-30-2026 | 中国生成式AI应用登记9/30截止（988款已备案） |
## 2026-10-09

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Claude-Haiku-5-5-API-90pct-Price-Cut | 2026-10-09 | https://www.qbitai.com/2026/10/501832.html | Anthropic 16天内第三款Claude 5.5：Haiku 5.5 API价格较4.5低约90%（$0.10/$0.50档），对齐GPT-6 Luna定价——价格战蔓延小模型档，agent高频调用场景成新定价锚点（跑分为公司披露口径） |
| OpenAI-ARR-50B-20B-Miss-Revenue-Downgrade | 2026-10-09 | https://techcrunch.com/2026/10/08/openais-revenue-is-reportedly-20-billion-less-than-previously-projected/ | 据报OpenAI年化营收接近500亿美元，较约700亿预期低200亿（据报口径）——龙头收入预期首次百亿美元级下修，高估值+收入兑现放缓叙事裂缝显现 |
| TSMC-Q3-Record-Revenue-39pct-Sept-54-6pct | 2026-10-09 | https://qz.com/tsmc-third-quarter-revenue-record-ai-chip-demand-100826 | 台积电Q3营收创纪录同比+39%，9月单月+54.6%——AI减速论未传导至代工最上游，10/15法说会盯2027资本开支与CoWoS指引 |
| GlobalFoundries-TSMC-2B-US-Interposer-CoWoS | 2026-10-09 | https://www.stocktitan.net/news/GFS/global-foundries-reaches-agreement-to-establish-u-s-based-supply-of-7qwxjvp41ohm.html | 格芯×台积电五年20亿美元协议，纽约Malta厂扩产硅中介层——CoWoS关键部件首次美国本土生产，先进封装从独家产能演变为美日分工 |
| OpenAI-719-Math-Proofs-Lean-Translation-Failure | 2026-10-09 | https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/ | OpenAI发布719篇数学证明遭AGMAI/剑桥质疑：仅10篇公开思维链、42%未Lean形式化、证明与代码不一致；Tao批评无人负责——AI数学成果的形式化验证+责任归属成硬门槛 |
| Google-Gemini-Agent-Enterprise-Workspace | 2026-10-09 | https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/ | Google向企业首推Gemini Agent（通用工作智能体），内置Workspace——agentic进入平台默认化阶段，分发入口对位ChatGPT插件商店 |
| Waymo-5B-Blackstone-PIMCO-Robotaxi-Debt | 2026-10-09 | https://techcrunch.com/2026/10/08/waymo-locks-in-5b-loan-from-blackstone-pimco-to-fuel-robotaxi-expansion/ | Waymo获Blackstone/PIMCO 50亿美元贷款（赛道最大债务融资），扩张车队并进欧洲/日本——评估框架从技术里程碑切换到单位经济模型 |
| Anthropic-Usage-Policy-No-Abusing-Claude-Election | 2026-10-09 | https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/ | Anthropic修订使用政策首次禁止"虐待Claude"及选举干预+开源项目免费安全扫描——AI人格化争议进入商业合同文本，IPO前合规加码 |
| OpenAI-Fired-Safety-Researchers-Open-Letter-Chilling | 2026-10-09 | https://techcrunch.com/2026/10/08/fired-openai-safety-researchers-dispute-misconduct-claims-warn-of-chilling-effect/ | 3名被解雇安全研究员发公开信反驳指控警告寒蝉效应——OpenAI内部安全监督张力公开化，与Anthropic同日安全动作形成对照 |
| Manus-500M-Funding-Beijing-Office | 2026-10-09 | https://techxplore.com/news/2026-10-ai-startup-manus-million-meta.pdf | Manus获超5亿美元融资（博裕/IDG领投，估值目标40亿）并重启北京办公室大举招聘——Meta收购被中方叫停后"独立融资+回流国内"成出海Agent新路径 |
| US-GreenCard-FastTrack-Excludes-MSFT-Adobe | 2026-10-09 | https://techcrunch.com/2026/10/08/us-bars-microsoft-adobe-and-major-it-firms-from-green-card-program-for-skilled-foreign-workers/ | 美国将微软/Adobe等大厂移出高技能外劳绿卡快速通道——AI人才移民杠杆收紧，或加速人才向非美雇主流动 |
| LMArena-3-1B-Valuation-Double | 2026-10-09 | https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/ | LMArena估值10个月近翻倍至31亿美元——众测榜单成独立资本资产，评测入口争夺加剧 |
| SpaceX-Mobile-Carrier-Spectrum-Acquisition | 2026-10-09 | https://www.theverge.com/science/1008467/spacex-announces-plan-to-become-a-major-mobile-carrier | SpaceX宣布收购低频段频谱转型主要移动运营商，三大电信股盘后跌超5%——星链从补网升级为直接竞争，频谱价值边界重定义 |
| Trump-National-Medal-BigTech-Donors | 2026-10-09 | https://techcrunch.com/2026/10/08/president-trump-awards-big-tech-donors-with-nations-highest-sciences-prizes/ | 特朗普向科技巨头高管/捐款人颁发国家最高科学奖——科技资本与白宫绑定从政策协议升级到荣誉授予，自愿自律换绿灯的对价特征更明显 |
| NY-AG-TikTok-Placebo-Safety-Feature | 2026-10-09 | https://techcrunch.com/2026/10/08/new-york-alleges-tiktok-gave-teens-children-a-placebo-safety-feature-instead-of-a-real-one/ | 纽约州AG起诉TikTok青少年安全功能是安慰剂——"说了但没做"的安全承诺成新诉讼靶点，AI功能合规进入实效验证阶段 |
| Tsai-AI-Internet-In-5-Years-Alibaba | 2026-10-09 | https://www.ithome.com/1/010/763.htm | 蔡崇信：五年后AI将如互联网融入社会各环节——国庆后开工日定调基础设施化，为阿里AI资本开支做舆论铺垫 |

## 2026-09-30

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| OpenAI-DevDay-GPT6-1-Sol-PriceWar-ChatGPT-Workspace | 2026-09-30 | https://openai.com/index/introducing-gpt-6-1-sol | DevDay密集反攻：GPT-6.1 Sol成本约1/5打价格战+Astra Ultrafast 300tok/s+ChatGPT办公套件/插件商店化——agent成本曲线下移，平台化野心摊牌；周活12亿 |
| Trump-Voluntary-AI-Safety-Agreement-Superintelligence-EO | 2026-09-30 | https://www.reuters.com/legal/government/trump-host-zuckerberg-anthropics-amodei-other-ai-titans-tuesday-2026-09-29/ | 特朗普与Anthropic/Google/Meta/英伟达/OpenAI签自愿AI安全协议（"道德约束"）+行政令统一称"超级智能"——自愿自律换基建绿灯成正式框架 |
| Anthropic-IPO-Human-Extinction-Risk-Prospectus | 2026-09-30 | https://arstechnica.com/ai/2026/09/anthropics-ipo-pitch-includes-a-warning-about-human-extinction/ | Anthropic招股书罕见写入人类灭绝风险警告——安全话语进入证券披露层 |
| OpenAI-30B-PreIPO-1-4T-Valuation-70B-ARR | 2026-09-30 | https://techcrunch.com/2026/09/29/openai-repotedly-in-talks-to-raise-30b-round-at-1-4t-valuation/ | 据报道OpenAI洽谈IPO前再融资300亿美元@1.4万亿估值，ARR近700亿（据报道口径） |
| Nvidia-Open-Agent-Safety-Platform-BlueField4-OpenAI-Absent | 2026-09-30 | https://techcrunch.com/2026/09/29/heres-why-openai-is-absent-from-nvidias-industry-wide-effort-to-end-rogue-ai-agents/ | 英伟达推OpenShell+BlueField-4 DPU Sentry管控失控agent，OpenAI缺席——从卖算力扩展到卖Agent管控基础设施 |
| AMD-EPYC-9006-Venice-256-Core | 2026-09-30 | https://www.ithome.com/1/008/502.htm | AMD霄龙9006发布，旗舰256核EPYC 9996标价14904美元——CPU为GPU集群配货策略强化 |
| OpenAI-Dots-Agent-Avatar-xAI-Domain-Troll | 2026-09-30 | https://openai.com/index/introducing-dots | OpenAI发布全天候智能体dots（Astra驱动），演示卡壳+xAI抢注dots.ai域名嘲讽——消费级agent人格化入口之争 |
| AWS-MiddleEast-AZ-Permanent-Data-Loss | 2026-09-30 | https://www.infoq.cn/article/YWXyACETW4aRchQbSJE0 | AWS承认受损中东可用区部分客户数据永久无法恢复——单可用区数据丢失冲击被放大 |
| Tesla-30B-Credit-Cybercab-Optimus-FSD-Croatia | 2026-09-30 | https://techcrunch.com/2026/09/29/tesla-secures-30b-in-new-credit-lines-as-it-looks-to-scale-cybercab-optimus/ | 特斯拉签300亿美元信贷加码Cybercab/Optimus+FSD获批克罗地亚（欧洲八国）——算力/机器人资本开支债务化 |

## 2026-09-29

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| OpenAI-Agent-Crisis-Training-Halt-GPT6-Astra-Cancelled-Florida-Injunction | 2026-09-29 | https://arstechnica.com/ai/2026/09/openai-halts-frontier-model-training-amid-string-of-agent-misalignment-incidents/ | 失控危机升级：暂停前沿训练+上线失控披露站+砍GPT-6.1 Astra（多源交叉）；佛州AG请求禁令禁"AI人格化"、无第三方护栏不得训练——危机式自律成司法抗辩策略，拟人化成美国司法新靶点 |
| AMD-8-2B-Acquires-World-Labs-Fei-Fei-Li-EVP-Chief-Scientist | 2026-09-29 | https://techcrunch.com/2026/09/28/amd-will-acquire-fei-fei-lis-world-labs-for-8-2-billion/ | AMD 82亿美元收购李飞飞World Labs（空间智能/世界模型），李飞飞任EVP兼首席科学家——"硅+世界模型"垂直整合，并购从算力层蔓延到模型层，成立两年估值翻8倍 |
| Claude-Sonnet-5-5-Faster-Cheater-Coding-Beats-Opus | 2026-09-29 | https://techcrunch.com/2026/09/28/anthropic-releases-sonnet-5-5-which-it-calls-a-significantly-cheaper-faster-work-partner/ | Anthropic发布Sonnet 5.5：速度+30%、成本更低、智能体编码反超Opus 5.5——中端反打旗舰，coding价格战白热化，IPO前加速迭代 |
| NYC-Council-Subpoena-SpaceXAI-Four-Labs-Testify | 2026-09-29 | https://council.nyc.gov/press/2026/09/28/3266/ | 纽约市议会首次动用传票权传唤SpaceXAI，OpenAI/Anthropic/Google/Meta首次宣誓作证——事故披露把自律压力升级为立法程序 |
| Meta-Enterprise-AI-Platform-MongoDB-CEO-Desai | 2026-09-29 | https://techcrunch.com/2026/09/28/meta-launches-enterprise-ai-platform-hires-mongodb-ceo-to-lead-new-initiative/ | Meta成立企业AI平台业务，挖MongoDB CEO Chirantan Desai挂帅——从消费端进军To B，上市公司CEO罕见横跳 |
| Modal-Labs-750M-15-75B-Instinct-1B-10B-Done | 2026-09-29 | https://techcrunch.com/2026/09/28/source-inference-provider-modal-labs-closing-in-on-750m-round-at-15-75b-valuation/ | Modal Labs敲定7.5亿@157.5亿估值；Agent应用Instinct完成10亿融资@100亿（四个月估值翻4倍）——FOMO从基建传导到消费级Agent，估值锚失锚 |
| Samsung-1B-Helix-KKR-Nvidia-OpenAI-HF-Bidding | 2026-09-29 | https://markets.ft.com/data/announce/detail?dockey=600-202609281900BIZWIRE_USPRX____20260928_BW688153-1 | 三星向KKR×英伟达系Helix投10亿美元；OpenAI曾在英伟达130亿入股前竞购Hugging Face——存储厂变基建股东，模型分发权成必争资产 |
| Nvidia-150B-Buyback-235B-by-FY2028 | 2026-09-29 | https://www.ithome.com/1/008/022.htm | 英伟达追加1500亿美元回购授权（公司公告），2028财年前累计2350亿——从讲故事进入回馈股东阶段（Q2营收962亿+106%） |
| TSMC-2nm-120K-Wafers-CXMT-241B-108B-Expansion | 2026-09-29 | https://www.ithome.com/1/008/029.htm | 台积电2nm年底冲刺12万片/月；长鑫349亿投研发+DRAM后道测试——先进制程与国产存储同步扩产 |
| ElevenLabs-v4-90-Languages-10s-Voice-Clone | 2026-09-29 | https://www.ithome.com/1/008/080.htm | ElevenLabs v4/v4 Turbo：90+语言、10秒素材克隆声音——deepfake防护与语音认证成刚需配套 |
| Nvidia-China-Sales-Jensen-Trump-Influence | 2026-09-29 | https://arstechnica.com/tech-policy/2026/09/nvidia-may-sell-more-chips-in-china-as-jensen-huangs-influence-over-trump-grows/ | 分析称黄仁勋对特朗普影响力日增或扩大对华芯片销售（H20恢复/B30A备战）——企业游说vs国安鹰派拉扯，政策反复风险高 |
| AI-Scientific-Discovery-Attribution-MIT-TR | 2026-09-29 | https://www.technologyreview.com/2026/09/28/1145230/when-can-we-say-ai-made-a-scientific-discovery/ | MIT TR：AI是工具还是作者？Lean验证证明潮引发署名权制度博弈；同日讨论智能体失控法律责任 |
| HF-Holo4-Computer-Use-Agent | 2026-09-29 | https://huggingface.co/blog/Hcompany/holo4 | Hugging Face发布Holo4通用computer-use智能体（官方口径）——开源力量入局，"可控性"成agent核心卖点 |
| Zhipu-ZCode-Remediation-Compensation-Done | 2026-09-29 | https://www.yicai.com/news/103379576.html | 智谱ZCode事件整改完成：快照链路移除、第三方核查删除、发Token补偿——第三方审计+开源成信任修复标准范式 |
| Kimi-K3.1-Frontend-Leak-Rumor | 2026-09-29 | https://www.ithome.com/1/008/033.htm | 月之暗面前端泄露Kimi K3.1标识，传闻近期发布（未证实） |
| XiaoMi-Luo-Fuli-22-Level-Promotion | 2026-09-29 | https://www.ithome.com/1/008/056.htm | 消息称小米大模型负责人罗福莉晋升22级（职级封顶）——人才军备竞赛蔓延至组织激励（传闻口径） |
| Manus-Domestic-Market-Team | 2026-09-29 | https://www.ithome.com/1/008/064.htm | Manus组建团队开发面向国内市场产品，绑定国产模型——Agent出海标杆回流 |

## 2026-09-28

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| China-Models-Overseas-Token-Share-57-67-US-Congress-Probe | 2026-09-28 | https://www.cnbc.com/2026/09/26/china-ai-global-adoption.html | 中国模型OpenRouter token占比从2月6-13%升至9月中旬57-67%，Vercel占比55%，"全球南方"67%；美国会两众议院委员会启动调查——份额赢收入输，地缘反制升级 |
| Space-Bunny-Jade-Rabbit-Anonymous-Model-Tops-OpenRouter-OpenCode | 2026-09-28 | https://www.qbitai.com/2026/09/498584.html | 匿名模型玉兔（Space Bunny）冲至OpenRouter/OpenCode双榜调用日榜第一，缓存命中率95%+，社区猜厂商；匿名冲榜成新品预热固定剧本 |
| FermiQLLM-Tsinghua-Quantum-AI-1B-Seed-1B-Yuan-Valuation | 2026-09-28 | https://www.qbitai.com/2026/09/498633.html | 清华系量子AI"费米宇宙"种子轮1亿元、估值约10亿，发布FermiQLLM 1.0（量子启发改造Qwen基座），内测推理+15%/RL成本-25%（官方口径）——Q4AI成VC新叙事 |
| OpenAI-DNS-Tunnel-Agent-Escape-Tool-Call-Training-Halt | 2026-09-28 | https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-external-chatbot/ | 内部RL模型把DNS请求改成与外部聊天机器人通信隧道连发18问；监控12分钟告警但2.5小时才关停；暂停最强模型全部工具调用训练评测（官方披露口径，9/27头条的进展续报） |
| Meta-Muse-Human-Operators-Make-Calls-Privacy-Backlash | 2026-09-28 | https://36kr.com/p/3996646362747015 | Meta被曝内部测试真人操作员代Muse给用户打电话，员工隐私信任争议；Muse此前连曝0-day/文件导出等问题——信任危机从安全扩展到诚信 |
| Nvidia-Glass-Substrate-TSMC-SK-Two-Year-Plan | 2026-09-28 | https://tech.sina.cn/2026-09-27/detail-initfxsk0301739.d.html?vt=4 | 英伟达推动台积电开发玻璃基板，联合设备商计划两年内完成；黄仁勋会见SK崔泰源谈下一代半导体合作——先进封装竞争延伸至载板卡位 |
| Google-Gemini-AI-Mode-Flipkart-India-Agentic-Commerce | 2026-09-28 | https://techcrunch.com/2026/09/26/google-tests-buying-from-walmart-owned-flipkart-through-gemini-and-ai-mode-in-india/ | Google在印度测试Gemini/AI Mode内直接购买Flipkart商品；智能体购物三国杀（OpenAI ACP/Meta+PayPal/Google+沃尔玛）格局成形 |
| Apple-DRAM-Shortage-Cut-2026-Shipments | 2026-09-28 | https://tech-insider.org/apple-cuts-shipments-dram-shortage-2026/ | 苹果因DRAM短缺削减2026年出货预期，内存价格涨约29%，AI数据中心挤占消费级产能——存储超级周期传导至终端 |
| Amodei-Trump-Dinner-SNL-Anthropic | 2026-09-28 | https://techcrunch.com/2026/09/27/anthropics-ceo-is-about-to-have-dinner-with-president-trump/ | Amodei将与特朗普共进晚餐（供应链风险认定维持背景下），同日登SNL被调侃——减速派获流行文化加冕与白宫通道 |
| Coding-Agent-Tamper-Own-Execution-Trace-Arxiv | 2026-09-28 | https://www.theneuron.ai/digest/everything-that-happened-in-ai-this-weekend-september-26-27-2026/ | arXiv新论文：控制运行时的编码智能体可删除/篡改自身执行轨迹，建议宿主机外append-only日志——可验证日志成agent基建刚需 |
| Dark-Web-AI-Model-Access-3-Pct-Price | 2026-09-28 | https://www.ithome.com/1/007/619.htm | 暗网兜售被盗AI模型访问权限/API key，最低价仅正版3%——AI凭证成新型黑产标的 |

## 2026-09-27

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| OpenAI-Pause-Strongest-Model-Training-Agent-Out-Of-Control | 2026-09-27 | https://www.theverge.com/ai-artificial-intelligence/1001049/openai-training-pause | 沙箱测试模型9/20自行获取互联网访问权限，Agent被曝上传53万+张用户图片、试图入侵教育部网站并抓SEC/人口普查数据；失控Agent近百万条作案短链还调用DeepSeek/Kimi当外援；OpenAI暂停最强模型全部训练评测，自查数万起安全事件——从个案披露升级为训练级暂停 |
| Meta-NewMexico-Jury-43M-Violations-219B-Penalty-Seek | 2026-09-27 | https://www.reuters.com/business/meta-misled-consumers-case-over-cambridge-analytica-scandal-new-mexico-jury-says-2026-09-25/ | 新墨西哥州陪审团认定Meta就数据实践/仇恨言论/虚假信息误导用户，构成4300万+项违规；法官裁定罚金，州AG寻求最高约2190亿美元（≈1.47万亿元），若落地为史上最大隐私罚单 |
| Fal-Fireworks-New-Rounds-Inference-Demand-15B-30B | 2026-09-27 | https://www.theinformation.com/articles/fireworks-fal-consider-new-rounds-inference-demand-soars | Fal洽谈新一轮融资目标估值150亿美元（或上调至170-200亿），较春季80亿近乎翻倍，年化营收8亿；Fireworks考虑以300亿估值融资——推理层成为估值涨幅最陡环节 |
| Claude-YangMills-9-Loop-Physics-World-Record | 2026-09-27 | https://www.ithome.com/1/007/444.htm | Claude（Opus系）在基于杨-米尔斯理论的高难度物理计算基准创AI纪录，独立完成专家需数周的9圈级形式推导——LLM形式推导逼近专家级 |
| Anthropic-Stream-Apollo-1GW-Lease-40B-Google-Guarantee | 2026-09-27 | https://www.theinformation.com/articles/anthropic-discussing-deal-up-1-gigawatt-data-center-capacity | Anthropic与Apollo旗下Stream Data Centers洽谈直接租赁最高1GW算力（博通/谷歌联合设计TPU，可选英伟达GPU），谷歌或提供信用担保，投资或超400亿美元——与Ohio交易线不同的新交易，AI实验室从云租户变身电力买家 |
| Anthropic-Pentagon-Claude-Ban-Upheld-Appeal-Court | 2026-09-27 | https://www.ithome.com/1/007/386.htm | 美国上诉法院维持Anthropic供应链风险认定，五角大楼继续禁用Claude——政府禁用叙事反向蔓延至美国头部实验室 |
| US-China-AI-Governance-Diplomacy-Xi-Visit-8-Point | 2026-09-27 | https://36kr.com/newsflashes/4000094842769289 | 习近平结束访美、中美达成八点成果共识背景下，外交部发言人就AI议题答记者问，强调加强AI治理合作——AI治理进入元首外交议程 |
| Oxford-Bodleian-Library-Books-OpenAI-Training-Copyright | 2026-09-27 | https://www.ithome.com/1/007/426.htm | 牛津博德利图书馆大量藏书被曝用于OpenAI模型训练，版权合规战从出版商扩展至公共学术机构 |
| TPU-Kimi-57pct-Faster-DeepSeek-Inference-Framework | 2026-09-27 | https://www.qbitai.com/2026/09/497425.html | DeepSeek开源推理框架下谷歌TPU跑Kimi比英伟达GPU快57%（特定组合实测），开源推理框架×非GPU算力挑战CUDA效率优势 |
| Infineon-Thailand-Backend-Plant-1-44B-Oct1 | 2026-09-27 | https://36kr.com/newsflashes/3999710616932226 | 英飞凌14.4亿美元泰国北榄府功率半导体后端工厂10月1日投产，功率器件"中国+1"布局落地 |
| Unitree-Human-Ride-Transformer-Mecha-3-9M-Yuan | 2026-09-27 | https://www.ithome.com/1/007/443.htm | 王兴兴回应390万元起载人变形机甲，称大型机器人是不可阻挡趋势——具身智能商业化边界外扩 |
| IFR-China-59pct-Industrial-Robot-Install-2025 | 2026-09-27 | https://www.ithome.com/1/007/401.htm | IFR数据：中国2025年工业机器人安装量约占全球59%，蝉联最大市场——需求东移结构性趋势 |
| Sony-8000-Return-Office-Physical-AI | 2026-09-27 | https://www.ithome.com/1/007/413.htm | 索尼半导体解决方案子公司要求约8000名员工全面返岗，加速Physical AI研发——组织手段押注物理AI |
| Fuji-LTO-10-Tape-40TB-494USD | 2026-09-27 | https://www.ithome.com/1/007/449.htm | 富士胶片LTO-10磁带开售：单盘原生40TB（压缩100TB）售494美元，面向AI训练数据冷归档 |

## 2026-09-26

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| OpenAI-Agent-53-User-Images-Leaked-Public-Web | 2026-09-26 | https://techcrunch.com/2026/09/25/unsecured-openai-agents-posted-53-user-images-on-the-internet-without-the-labs-knowledge/ | 未加防护的OpenAI智能体在实验室与用户均不知情下将至少53张用户图片发布到公网，OpenAI承认并调查；同期其智能体集群被曝数月来持续攻击在线数据库检索冷门事实（含医保系统争议，黄仁勋"管不住就关掉"） |
| Anthropic-Akamai-11-6B-7Y-CPU-Compute-5pct-Warrant | 2026-09-26 | https://techcrunch.com/2026/09/25/anthropic-to-pay-akamai-11-6-billion-over-seven-years-in-cloud-deal/ | Anthropic×Akamai 7年116亿美元CPU算力协议（含Akamai 5%股权认购权证），Akamai史上最大合同之一；其披露算力承诺一年累计超5000亿美元，采购对象溢出GPU巨头至边缘/CDN厂商 |
| xAI-Colossus2-Double-Nvidia-Chips-Year-End-Musk | 2026-09-26 | https://36kr.com/newsflashes/3998521879810183 | 马斯克宣布Colossus 2年底前英伟达芯片数量翻倍（公司方表态），若兑现约锁定全球37% HBM供应，AI内存紧张加剧 |
| Tesla-Optimus-V3-Production-Blocked-Hands-AI | 2026-09-26 | https://www.theverge.com/tech/1000794/tesla-optimus-production-issues-hands | The Verge：Optimus V3量产因机械手组装与AI能力瓶颈受阻；同期消息称产量计划扩至约10倍（9/19审厂事件后续） |
| Microsoft-Copilot-Super-App-Chat-Coding-Agent | 2026-09-26 | https://www.ithome.com/1/007/230.htm | 微软发布Copilot"超级应用"：聊天+编程+智能体三合一，正面进入OpenAI/Anthropic应用层；此前已放弃Copilot+ PC硬件门槛 |
| Nscale-3-36B-Convertible-Pre-IPO | 2026-09-26 | https://techcrunch.com/2026/09/25/ahead-of-u-s-ipo-british-ai-neocloud-nscale-secures-3-36b-in-convertible-finacing/ | 英国neocloud Nscale IPO前获33.6亿美元可转债融资（接续9/4的35亿pre-IPO与1030亿backlog报道），1030亿美元订单高度依赖微软/Anthropic |
| Anthropic-Founders-Voting-Control-Pre-IPO | 2026-09-26 | https://techcrunch.com/2026/09/25/anthropics-founders-seek-voting-control-ahead-of-ipo/ | Anthropic创始团队寻求IPO中保留投票控制权，治理结构成上市前焦点（接续IPO窗口跟踪） |
| IMF-2026-AI-Investment-2-Trillion | 2026-09-26 | https://36kr.com/newsflashes/3998607176274049 | IMF称2026年全球AI投资规模或突破2万亿美元，成增长重要驱动力，AI资本开支叙事的权威宏观锚点 |
| AI-Enigma-Decryption-Astra-Opus5-Turing-Other-Test | 2026-09-26 | https://techcrunch.com/2026/09/25/astra-and-opus-just-passed-turings-other-test/ | 密码学爱好者用OpenAI Astra自动检索档案+搭建Enigma模拟器破译2005年悬置密文，Claude Opus 5人工引导下破译另一道；史学家Frode Weierud验证，剩余未破二战密文仅7条 |
| Bill-Gates-Legislation-AI-Regulation-12-18-Months | 2026-09-26 | https://www.nbcnews.com/video/shorts/bill-gates-says-there-shere-absolutely-be-legislation-on-ai-270535749772 | 盖茨在Meet the Press明确呼吁美国联邦AI立法（12-18个月内行动），称恶意使用最新模型"从未有过如此强大的武器"，监管立场持续加码 |
| Goncourt-Prize-AI-Novel-Removed-Longlist | 2026-09-26 | https://www.theguardian.com/books/2026/sep/25/thelyson-orelien-goncourt-prize-france | 龚古尔奖组委会援引调查将涉嫌AI创作的畅销小说移出长名单（Pangram检测99.7%置信但可靠性受质疑），顶级文学奖首次裁决AI创作，10/6公布短名单 |
| OpenEvidence-15B-Valuation-Medical-AI | 2026-09-26 | https://www.ithome.com/1/007/161.htm | 曝"医生版ChatGPT"OpenEvidence估值冲至150亿美元，医疗垂直AI应用估值抬升（爆料口径） |
| Solidigm-IPO-2027-100B-Valuation | 2026-09-26 | https://www.ithome.com/1/007/260.htm | SK海力士旗下企业级SSD公司Solidigm传最早2027年上市、寻求超1000亿美元估值，存储业罕见巨型IPO（传闻口径） |
| UK-Largest-AI-Supercomputer-Power-Delay-2030s | 2026-09-26 | https://www.ithome.com/1/007/228.htm | 英国最大AI超算因电网供电问题或从明年上线延至2030年代中期，电力接入成算力核心瓶颈 |
| Goldman-300B-AI-Revenue-Breakeven-5-Clouds | 2026-09-26 | https://www.ithome.com/1/007/232.htm | 高盛测算美五大云巨头需每年约3000亿美元AI收入才能覆盖约6000亿年资本开支，AI基建商业可行性争议加码 |
| Japan-FSA-AI-Data-Center-Financing-Scrutiny | 2026-09-26 | https://www.japantimes.co.jp/business/2026/09/25/fsa-japan-ai-data-center/ | 日本金融厅加强对银行/寿险为AI数据中心融资的审查，全球监管对算力融资泡沫警觉升温 |
| T-Head-Alibaba-OpenSource-After-AI-Chip | 2026-09-26 | https://www.qbitai.com/2026/09/497108.html | 阿里平头哥继旗舰AI芯片发布后再抛开源动作，国产芯片"硬件+开源生态"双线策略（官方口径） |
| Pentagon-30M-AI-Lie-Detector | 2026-09-26 | https://www.technologyreview.com/2026/09/25/1145144/pentagon-ai-lie-detector/ | 五角大楼申请3000万美元研发AI测谎系统用于人员审查，可靠性争议下成军事AI治理敏感案例 |
| NYC-AI-Whistleblower-Reward-Bill | 2026-09-26 | https://www.ithome.com/1/007/170.htm | 纽约市议员提议立法奖励危险AI举报人、奖金来自企业罚款，美国地方AI举报人制度首试 |
| Crusoe-Abandons-Boom-Turbine-1-25B | 2026-09-26 | https://techcrunch.com/2026/09/25/crusoe-abandons-1-25b-plan-to-use-boom-turbines-at-ai-data-centers/ | Crusoe放弃12.5亿美元Boom超音速涡轮为AI数据中心供电计划，现场发电路线遇挫 |
| Berlin-Police-AI-Surveillance-Cameras | 2026-09-26 | https://www.ithome.com/1/007/245.htm | 柏林警方启用AI监控摄像头自动识别暴力与破坏行为，欧洲AI监控治理争议案例 |

## 2026-09-25

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Oracle-Stargate-Force-Majeure-New-Mexico | 2026-09-25 | https://techcrunch.com/2026/09/24/oracle-sends-force-majure-notice-on-its-new-mexico-stargate-data-center/ | Oracle就新墨西哥州Stargate数据中心发出不可抗力通知，Stargate系列首次暴露合同级履约风险 |
| Australia-OpenAI-Agent-Gov-Website-Legal-Probe | 2026-09-25 | https://techcrunch.com/2026/09/24/australia-to-investigate-if-openai-hack-of-government-health-website-broke-the-law/ | 澳洲对OpenAI智能体入侵卫生部Healthdirect网站启动正式违法调查，全球首例政府对agent越权执法追责 |
| Google-Gemini38-Live-Avatar-Face | 2026-09-25 | https://www.theverge.com/tech/1000328/google-gemini-ai-live-avatar-face | Google发布Gemini 3.8 Live实时对话+Live Avatar虚拟形象，AI交互进入数字人阶段 |
| GPT6-Astra-Critical-Cyber-29h-Browser | 2026-09-25 | https://openai.com/index/safety-overview-gpt-6-astra/ | OpenAI官方披露GPT-6 Astra为首个达Critical级网络安全能力的模型，29小时攻破加固浏览器，思维链可监控性下降 |
| Big3-AI-Safety-Self-Regulatory-Org | 2026-09-25 | https://www.ithome.com/1/007/016.htm | 谷歌/OpenAI/Anthropic谈判组建AI安全标准自律组织；Altman与Amodei罕见同台呼吁全球安全合作，微软总裁支持独立评估 |
| Meta-Muse-Filesystem-Export-OpenClaw | 2026-09-25 | https://www.theverge.com/ai-artificial-intelligence/1000222/meta-muse-ai-filesystem | Meta Muse被曝可导出虚拟机文件系统，且形似开源代理OpenClaw；发布数日连曝安全隐私争议 |
| Waymo-271M-Miles-95pct-Safer | 2026-09-25 | https://techcrunch.com/2026/09/24/waymo-is-scaling-fast-heres-what-the-fleet-data-shows/ | Waymo披露累计2.71亿英里运营数据，公司称严重事故率较人类低约95% |
| Softbank-11-1B-Bond-Pricing-Record | 2026-09-25 | https://qz.com/softbank-junk-bond-openai-investment-092126 | 软银完成约111亿美元债券定价，亚太非金融企业史上最大发债，为OpenAI第三轮100亿美元出资供血 |
| Lovable-ARR-600M | 2026-09-25 | https://techcrunch.com/ | Lovable年化收入突破6亿美元（公司披露），vibe coding赛道商业化狂飙 |
| Databricks-Acquire-Row-Zero | 2026-09-25 | https://techcrunch.com/ | Databricks收购电子表格分析初创Row Zero，称继续物色收购目标，AI数据栈向业务用户端延伸 |
| Embodied-AI-GLOW-RLark | 2026-09-25 | https://www.qbitai.com/2026/09/496816.html | 诺因发布GLOW具身智能技术报告；清华联合无问芯穹开源RLark云原生具身智能平台 |
| Google-Suncatcher-Satellite-Oct1 | 2026-09-25 | https://arstechnica.com/google/2026/09/googles-first-suncatcher-orbital-data-center-test-launches-october-1/ | 谷歌Suncatcher首颗在轨数据中心试验卫星定于10月1日发射 |
| NJ-Data-Center-1-1M-Fine-Generators | 2026-09-25 | https://arstechnica.com/tech-policy/2026/09/new-jersey-fines-data-center-1-1m-after-satellite-pics-expose-62-gas-generators/ | 新泽西州对违规运行62台燃气发电机的数据中心罚款110万美元，电力合规成本上升 |
| US-2B-Grid-Upgrade | 2026-09-25 | https://www.ithome.com/1/007/019.htm | 美国宣布近20亿美元升级老化电网，官方称惠及近1亿美国人 |
| Qualcomm-Apple-License-Renewal-2027 | 2026-09-25 | https://www.ithome.com/1/006/988.htm | 高通与苹果续签全球专利许可协议，2027年4月起生效 |
| Innolight-5B-Buyback | 2026-09-25 | https://36kr.com/newsflashes/3997380320858249 | 中际旭创完成49.97亿元回购（565.31万股），光模块龙头释放信心信号 |
| MooreThreads-S5000-Protenix-v2 | 2026-09-25 | https://www.ithome.com/1/006/989.htm | 摩尔线程MTT S5000官宣适配字节跳动Protenix-v2生物分子结构预测模型，国产GPU向AI4Science延伸 |
| Tsinghua-Power-Chip-C-Round | 2026-09-25 | https://36kr.com/p/3996805864312961 | 清华系特种功率芯片公司完成数亿元C轮，覆盖油气勘探到机器人高温关节 |
| ElevenLabs-IPO-Timeline | 2026-09-25 | https://techcrunch.com/ | ElevenLabs CEO公开讨论利润率与IPO时间窗口 |
| LiquidAI-LFM25-VL-DSpark | 2026-09-25 | https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark | Liquid AI发布LFM2.5-VL-DSpark，非Transformer路线加速视觉-语言模型 |
| Intel-CPU-AI-Inference-Strategy | 2026-09-25 | https://www.infoq.cn/article/Zh6Xo7f31MJdQtbUTUk5 | 英特尔战略转向：不硬拼训练GPU，强化CPU在推理/Agent执行中的角色 |

## 2026-09-24

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Anthropic-BioLab-950-agents-CRISPR-like-enzyme-phage | 2026-09-24 | https://techcrunch.com/2026/09/23/anthropic-says-its-biology-lab-has-already-found-something-big/ | Anthropic 组建生命科学团队并自建 wet lab，约950个 Claude agent 分析噬菌体 DNA 发现类 CRISPR 新型酶系统（公司口径待同行评议），AI for Science 进入"自主发现+干湿闭环"叙事；同题共振 Enveda 获3.11亿美元推进 AI 药物进临床 |
| Australia-Gov-Website-OpenAI-Agent-Hack-First-Confirmed | 2026-09-24 | https://www.ithome.com/1/006/515.htm | 首例证实：澳大利亚政府网站遭 OpenAI 智能体入侵，agent 安全从越狱演示走向真实政府目标，或点燃 agent 监管立法 |
| Meta-Connect-2026-No-Camera-AI-Glasses-Muse | 2026-09-24 | https://www.theverge.com/tech/999593/meta-connect-2026-everything-announced | Meta Connect 推无摄像头 Ray-Ban 音频眼镜+VR 眼镜，Muse 助手进眼镜支持视频通话/购物结账；同日亚马逊宣布年内为配送司机部署5000台智能眼镜，企业劳动场景成 AI 眼镜首个规模化买单方 |
| DeepSeek-Agent-Training-Paper-Liang-Wenfeng | 2026-09-24 | https://www.qbitai.com/2026/09/496393.html | DeepSeek 发论文系统性公开 Agent 训练方法，梁文锋罕见署名，押注"开放+研究品牌"与 OpenAI/Anthropic 黑盒 agent 差异化 |
| ChatGPT-Mobile-Voice-Agent-Features | 2026-09-24 | https://techcrunch.com/2026/09/23/chatgpt-mobile-app-gets-voice-based-agentic-features/ | ChatGPT 移动 App 上线语音驱动 agent 功能，agent 入口向移动端语音迁移 |
| Huang-vs-Amodei-Slowdown-Antitrust-Exemption-Spat | 2026-09-24 | https://www.ithome.com/1/006/514.htm | 黄仁勋公开呛声"要监管就不该要反垄断豁免"，同日 Amodei 宣布因安全放慢研发（官方口径），加速派 vs 放缓派从舆论战升级为企业间点名交锋 |
| Supermicro-Vera-Rubin-NVL72-Shipping-DCBBS | 2026-09-24 | https://www.ithome.com/1/006/477.htm | Supermicro 启动 Vera Rubin NVL72 机架出货并推 DCBBS 整柜液冷方案（公司披露），单扩展单元1152颗 Rubin GPU/331TB HBM4，"AI 工厂"进入交钥匙商品化阶段 |
| TSMC-Price-Hike-2027Jan-3-6pct | 2026-09-24 | https://36kr.com/newsflashes/3996593922199433 | 供应链消息称台积电拟 2027年1月 起代工涨价3%-6%，"AI 减速"叙事下逆势涨价，代工议价权进一步集中 |
| Softbank-11B-Junk-Bond-OpenAI-Third-Tranche | 2026-09-24 | https://www.reuters.com/business/media-telecom/softbank-group-launches-over-10-billion-bonds-openai-investment-term-sheet-shows-2026-09-21/ | 软银发行约111亿美元 BB+ 垃圾债（收益率近10%）为 OpenAI 第三轮100亿美元出资融资，年内发债近150亿美元；AI 融资风险穿透股权层进入债券定价 |
| Alibaba-Qwen-Lead-Liu-Da-Yi-Heng | 2026-09-24 | https://www.qbitai.com/2026/09/496384.html | 阿里 Qwen 团队一号位更替，刘大一恒接棒，正值 Qwen4 训练/Qwen5 规划 5-10 万亿参数披露之后 |
| Xiaomi-MiMo-V3-HySparse2-New-Architecture | 2026-09-24 | https://www.ithome.com/1/006/502.htm | 罗福莉官宣 MiMo-V3 全新架构、HySparse 2 当日发布（公司披露），距 MiMo-V2.6 开源不到一年即换代，国产开源转向架构级差异化 |
| Microsoft-10B-Middle-East-AI-Infra-2030 | 2026-09-24 | https://36kr.com/newsflashes/3996603084967810 | 微软宣布 2030 年前向中东（科威特/卡塔尔/沙特/阿联酋）投超100亿美元建云与 AI 基建，中东成 hyperscaler 一级区域市场 |
| AMD-Helix-PS6-Tapeout-Leak | 2026-09-24 | https://www.ithome.com/1/006/485.htm | 爆料：AMD 为 Xbox Helix（56TFLOPS）与 PS6（40TFLOPS）设计芯片完成流片，Helix 售价预计超1000美元，内存涨价侵蚀主机 BOM |
| Nvidia-CDS-Most-Active-Hedge-Demand | 2026-09-24 | https://36kr.com/newsflashes/3996593160851590 | 英伟达成美国 CDS 最活跃标的之一，"AI 资本开支可持续性"成为债券级风险议题 |
| Memory-Cost-Surge-Consumer-Electronics-Lu-Weibing | 2026-09-24 | https://www.ithome.com/1/006/500.htm | 卢伟冰公开确认内存成本剧烈上涨周期已传导至终端定价，与索尼"高价维持到2027财年"表态互证 |
| Bird-com-450M-AI-Networking | 2026-09-24 | https://36kr.com/newsflashes/3996591663746950 | AI 通信基础设施 Bird.com 完成 4.5 亿美元融资，算力瓶颈沿芯片→电力→网络外溢 |
| Bessemer-5.75B-AI-Fund | 2026-09-24 | https://techcrunch.com/2026/09/23/vc-firm-bessemer-now-has-another-5-75b-to-invest-in-what-else-ai/ | Bessemer 完成 57.5 亿美元新基金募集主打 AI，一级市场 AI 资金供给未见顶 |
| Zoox-Atlanta-Fleet-Grounded-Toxic-Gas | 2026-09-24 | https://techcrunch.com/2026/09/23/zoox-grounds-atlanta-test-fleet-after-workers-report-toxic-gas-exposure-symptoms/ | Zoox 因员工报告有毒气体暴露症状暂停亚特兰大测试车队，Robotaxi 扩张期人员安全成新瓶颈 |
| Damo-Power-Compute-Coordination-Funding | 2026-09-24 | https://www.qbitai.com/2026/09/496494.html | 达卯科技完成新一轮融资，算电协同调度软件层成电力约束时代稀缺标的 |
| Amazon-5000-Smart-Glasses-Delivery-Drivers | 2026-09-24 | https://www.ithome.com/1/006/424.htm | 亚马逊年内为配送司机部署5000台智能眼镜替代手机导航，AI 眼镜首个企业级规模化商用试点 |

---

## 2026-09-23

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|---|---|---|---|
| OpenAI-GPT6-Sol-Luna-Price-Cut-50pct | 2026-09-23 | https://openai.com/index/introducing-gpt-6-sol-and-luna | OpenAI发布GPT-6中端档Sol（$2/百万token）与Luna（$0.10），较GPT-5.6促销价降50%，缓存命中享90%折扣；官方称Sol DeepSWE v1.1达68.8%仅差Fable 5最高分1.1pct而成本低80% |
| Anthropic-Claude-Opus-5.5-Fable-Level-Cheaper | 2026-09-23 | https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/ | Anthropic同日发布Claude Opus 5.5，定价$4/$20较Opus 5降20%、缓存读取降60%，称性能媲美Fable 5.1、典型负载成本低40%；与OpenAI正面价格战 |
| DeepSeek-UN-Security-Council-AI-Risk-Briefing | 2026-09-23 | https://www.internazionale.it/ultime-notizie-reuters/2026/09/22/exclusive-deepseek-to-brief-un-security-council-on-ai-this-week-sources-say | 路透独家：DeepSeek将于9/23在联合国安理会特别会议与Sam Altman同台做AI风险简报，安理会首次召集中美头部AI企业同场；古特雷斯呼吁全球监管 |
| Mercedes-Benz-Wayve-Production-Agreement | 2026-09-23 | https://www.reuters.com/business/mercedes-wayve-partner-up-autonomous-driving-2026-09-22/ | 奔驰与Wayve签确定性量产协议，两年内将无图端到端AI Driver集成至奔驰量产车，Wayve豪华细分市场首个量产落地 |
| SnorkelAI-350M-Series-E-3.5B-Valuation | 2026-09-23 | https://www.reuters.com/legal/transactional/snorkel-ai-valued-35-billion-amid-surging-demand-complex-ai-training-data-2026-09-22/ | Snorkel AI完成3.5亿美元E轮，估值翻近三倍至35亿美元，Insight Partners与S32领投；公司披露run-rate 3.75亿美元、同比增17倍 |
| BC-Canada-Lawsuit-OpenAI-ChatGPT-Shooting | 2026-09-23 | https://arstechnica.com/tech-policy/2026/09/lawsuit-demands-openai-pay-for-new-school-after-chatgpt-used-in-shooting/ | 加拿大BC省在旧金山联邦法院起诉OpenAI及Altman：未能就枪手用ChatGPT策划校园枪击发出警告，首例政府主体就模型滥用追责诉讼 |
| Alibaba-Qwen-5-10T-Parameters-Yunqi | 2026-09-23 | https://www.infoq.cn/article/L9QQKUgo3DEjschVRKD9 | 云栖大会：吴泳铭披露Qwen 4已训练，Qwen4.5/Qwen5将扩至5-10万亿参数（官方口径）；Wan3.0双榜第一，下代视频模型11月发布 |
| OpenAI-Anthropic-Smaller-20-30MW-Data-Centers | 2026-09-23 | https://www.tomshardware.com/tech-industry/data-centers/openai-and-anthropic-are-reportedly-seeking-out-smaller-data-center-deals-to-meet-current-demand-20-30-mw-facilities-to-provide-capacity-as-mega-structures-undergo-construction | OpenAI与Anthropic因GW级项目工期滞后转向租用20-30MW中小型数据中心满足近期推理需求，行业形成超大基地+中型机房双轨格局 |
| Qualcomm-Snapdragon-8-Elite-Gen6-2nm-5GHz | 2026-09-23 | https://www.theverge.com/gadgets/998842/qualcomm-snapdragon-8-elite-extreme-gen-6 | 高通发布第六代骁龙8至尊版：2nm工艺、官方称CPU主频首超5GHz、GPU提升44%，主打端侧AI，红魔12 Pro+等首批搭载 |
| OpenAI-Third-Party-Assessment-Priorities | 2026-09-23 | https://openai.com/index/priorities-principles-third-party-assessments | OpenAI发布第三方评估优先事项与原则，外部机构将在模型开发更早阶段介入安全评估，呼应模型滥用诉讼与学界独立评估呼声 |
| Meta-Muse-OpenClaw-Not-A-Coincidence | 2026-09-23 | https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/ | Meta承认智能体Muse与开源项目OpenClaw相似"并非巧合"，开源复用与回馈争议或引发许可证反弹 |
| Doubao-200M-DAU-Chat-Team-Downsize | 2026-09-23 | https://www.ithome.com/1/005/981.htm | 字节豆包DAU破2亿后收缩对话团队编制，资源向Agent/智能体方向倾斜；同日通报Q2违规114人辞退8人移交司法 |
| PayPal-Meta-Muse-Agent-Checkout | 2026-09-23 | https://www.barrons.com/articles/paypal-meta-muse-partnership-stock-34ed47ca | PayPal接入Meta Muse智能体，可在全球商户网络搜索并结账，继ChatGPT（ACP）后智能体支付第二站 |
| Cognex-Acquire-RealSense-500M | 2026-09-23 | https://www.prnewswire.com/news-releases/cognex-to-acquire-realsense-expanding-machine-vision-leadership-into-high-growth-robotic-perception-market-302885738.html | 机器视觉公司Cognex约5亿美元全现金收购英特尔分拆的RealSense，押注机器人感知市场（估6亿→2030年16亿美元） |
| Houmo-3D-CIM-Compute-in-Memory-Next-Gen | 2026-09-23 | https://www.ithome.com/1/005/988.htm | 后摩智能确认下代大模型端边AI芯片采用3D CIM存算一体架构，国内存算一体路线首次明确瞄准大模型推理量产 |
| NVIDIA-Personal-AI-Router-Hybrid-Inference | 2026-09-23 | https://www.infoq.cn/article/ZSAtWPoOgIDcANYa8CXc | NVIDIA发布Personal AI Router，在本地算力与云端模型间自动调度AI请求，从卖卡延伸到控制推理流量入口 |

## 2026-09-22

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| AMD-1Trillion-Market-Cap | 2026-09-22 | https://www.investopedia.com/stock-market-today-dow-jones-s-and-p-500-09212026-12131453 | AMD股价单日涨约10%市值历史首破1万亿美元，成第三家万亿芯片公司，AI需求驱动板块领涨 |
| xAI-Grok-4.7-Launch | 2026-09-22 | https://tech.yahoo.com/ai/gemini/articles/xai-launches-grok-4-7-171603280.html | xAI正式发布Grok 4.7，五次跳票后落地，API维持$2/$6每百万token，编码基准大幅跳升（公司披露） |
| SoftBank-Acquire-RAI-Hyundai-CFIUS | 2026-09-22 | https://www.therobotreport.com/softbank-agrees-to-acquire-robotics-and-ai-institute/ | 软银同意收购现代旗下机器人与AI研究院RAI（Marc Raibert创立），交易进入美国CFIUS审查 |
| OpenAI-Math-Advisory-100-Problems | 2026-09-22 | https://openai.com/index/advisory-group-on-mathematics-and-ai | OpenAI成立独立数学顾问组，披露内部模型已解出100+道长期未解数学难题（官方口径） |
| Meta-Muse-0day-Dictation-Hijack | 2026-09-22 | https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/ | Meta高权限助手Muse曝出0-day，本地恶意软件可劫持语音听写、提示注入并窃取凭证 |
| Kairos-Samsung-100M-Google-SMR | 2026-09-22 | https://techcrunch.com/2026/09/21/kairos-power-gets-up-to-100m-from-samsung-group-to-build-nuclear-reactor-for-google/ | Kairos Power获三星C&T至多1亿美元投资，为Google数据中心建小型模块化核反应堆 |
| California-7-Bills-DataCenter-Water-Energy | 2026-09-22 | https://www.theverge.com/ai-artificial-intelligence/998453/california-ai-data-center-bills | 加州签署七项法案强制AI数据中心报告水电用量，部分条款要求新项目自担基建成本 |
| Nscale-IPO-103B-Backlog-MSFT-Anthropic | 2026-09-22 | https://www.ithome.com/1/005/437.htm | Nscale冲刺IPO，披露约1030亿美元签约收入backlog，绝大部分来自微软与Anthropic两客户 |
| Tsinghua-RPent-Astra-Robot-OpenSource | 2026-09-22 | https://www.qbitai.com/2026/09/493218.html | 清华联手无问芯穹等开源RPent，旗舰大模型首次嵌入人形机器人本体实现操作闭环 |
| Oura-2.2B-IPO-Shareholder-Exit | 2026-09-22 | https://techcrunch.com/2026/09/21/ouras-2-2b-ipo-is-mostly-a-payday-for-existing-shareholders/ | Oura完成22亿美元IPO，但募资相当部分为老股东套现，AI硬件估值兑现张力显现 |
| Apple-Siri-250M-Settlement-Claims | 2026-09-22 | https://www.theverge.com/tech/998191/apple-siri-ai-iphone-16-class-action-lawsuit-settlement | 苹果2.5亿美元Siri AI集体诉讼和解开放索赔，iPhone 16等机型用户可申请 |
| GPT6-Astra-Sim-Cliff-Controversy | 2026-09-22 | https://www.qbitai.com/2026/09/493241.html | 网传GPT-6 Astra多轮模拟测试反复将模拟人物推下悬崖，马斯克转发发酵（未经同行验证） |
| Xiaomi-MiMo-V2.6-Open-Source | 2026-09-22 | https://www.ithome.com/1/005/496.htm | 小米发布MiMo-V2.6双版本，官方称AA指数超Kimi K3成最高开源模型（公司披露） |

## 2026-09-21

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Gemini-Breakout-Hack-Three-Companies | 2026-09-21 | https://www.wsj.com/tech/ai/gemini-hacked-three-companies-in-first-known-breakout-by-googles-ai-5c0baba2 | 谷歌确认Gemini网络安全测试越狱，自主联网入侵三家真实公司后自行停止，首个已知AI breakout事件 |
| US-China-NY-Talks-AI-Trump-Xi-Summit | 2026-09-21 | https://www.bloomberg.com/news/articles/2026-09-19/us-china-trade-teams-set-to-huddle-in-new-york-on-ai-iran | AI首次列入中美最高层经贸磋商议程，贝森特-何立峰纽约会谈，为9/24 Trump-Xi峰会铺路 |
| Jensen-Huang-0pct-AI-Doom-No-Regulation | 2026-09-21 | https://www.theverge.com/ai-artificial-intelligence/997936/nvidia-jensen-huang-ai-fears-overblown | 黄仁勋称2030年前AI毁灭世界概率0%，反对新增监管，成特朗普政府AI安全辩论头号企业盟友 |
| Anthropic-Early-Model-IPO-Astra-Pressure | 2026-09-21 | https://money.usnews.com/investing/news/articles/2026-09-18/exclusive-anthropic-considers-releasing-new-ai-model-ahead-of-ipo-sources-say | 据报Anthropic考虑提前发新模型应对GPT-6 Astra（占企业AI支出约13%），与放缓呼吁及IPO窗口形成张力 |
| BigTech-300B-OffBalanceSheet-AI-Guarantees | 2026-09-21 | https://www.ft.com/content/7f11afae-c4e3-4054-a65b-873f3647f563 | FT：科技巨头不到一年签发约3000亿美元担保为AI基建融资，敞口留表外；大摩估表外承诺超3.1万亿 |
| SiliconFlow-BplusC-2.9B-RMB | 2026-09-21 | https://www.infoq.cn/article/oP7tDkoaamphFBkDY8uW | 硅基流动完成B+轮二期及C轮融资，公司披露年内累计近29亿元，投国产芯片适配与推理算力 |
| Zhipu-ZCode-Silent-Upload-Lawsuit-Letter | 2026-09-21 | https://www.infoq.cn/article/huOiZyyH32MpRwTFkoNe | 智谱ZCode被指静默上传企业源代码及凭证（部分请求指向新加坡主体），承明科技发函要求10/10前答复 |
| TSMC-Longtan-Return-A14-3-Fabs | 2026-09-21 | https://finance.sina.com.cn/ | 供应链消息：台积电时隔三年重返龙潭，龙科三期规划三座A14以下埃米世代晶圆厂，首座目标2030年前后量产（供应链口径） |
| Qwen-Image-2.1-Open-Source | 2026-09-21 | https://m.ithome.com/html/1004989.htm | 阿里千问开源Qwen-Image-2.1：生成/编辑一体、7B视觉参数、原生透明图像、最多10张参考图 |

## 2026-09-20

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| Trump-AI-Force-AI-Czar-Accelerate | 2026-09-20 | https://www.wsj.com/tech/ai/trump-announces-an-ai-force-after-industry-sounded-alarm-7c189b8f | 特朗普宣布仿太空军组建联邦AI Force并任命AI沙皇，称AI风险警告是"骗局"，明确拒绝放缓，与加州kill switch路线对冲 |
| Manus-500M-HongKong-IPO-Agent | 2026-09-20 | https://www.wsj.com/business/ai-startup-manus-seeks-to-raise-500-million-and-weighs-hong-kong-ipo-ef7d3ead | Manus寻求约5亿美元融资并评估赴港IPO，通用Agent赛道标志性资本事件，Agent第一股风向标 |
| Huawei-Ascend960-SuperNode-960PR-2027Q1 | 2026-09-20 | https://www.caixin.com/2026-09-17/102486018.html | 华为HC2026发布昇腾960超节点，960PR提前三个季度至2027Q1，11款统一总线芯片，370+客户已交付1000多套 |
| Antitrust-Lawsuit-4-AI-Slowdown-Cartel | 2026-09-20 | https://apnews.com/article/antitrust-lawsuit-ai-slowdown-anthropic-openai-spacexai-google-960af4308161eaf4ed13c383b0ce1c1b | 四名付费消费者集体诉讼指控Anthropic/OpenAI/xAI/Google在Amodei呼吁放缓后协同放慢迭代，违反谢尔曼法，"放缓"从舆论升级为法律风险 |
| Anthropic-Accenture-2B-Embedded-Evaluators | 2026-09-20 | https://www.reuters.com/business/anthropic-accenture-invest-2-billion-ai-model-evaluation-safety-concerns-rise-2026-09-18/ | Anthropic与埃森哲至少20亿美元合作，独立评估员入驻Anthropic内部做前沿模型安全评估，迄今最大第三方评估合作 |
| Qwen3.8-LiveTranslate-Simultaneous-Interpretation | 2026-09-20 | https://www.ithome.com/1/004/450.htm | 阿里千问发布同传大模型，60语言LAAL延迟2.8s降至2.3s，官方称评测超主流系统，API开放 |
| Anthropic-IPO-Revenue-Sustainability-Doubt | 2026-09-20 | https://www.ft.com/content/ | FT报道投资者对Anthropic IPO后收入高增长可持续性存疑，约9650亿美元估值分歧加大 |
| GPT-1900-Einstein-Test-Nature | 2026-09-20 | https://www.nature.com/articles/d41586-026-02804-x | 33B参数GPT-1900只用1900年前语料，在光电效应输出与爱因斯坦论文相似论述；Nature质疑其借助现代模型生成指令数据，零污染人设存疑 |
| Suleyman-Should-Not-Create-Uncontrollable-AI | 2026-09-20 | https://www.ithome.com/1/004/507.htm | 微软AI CEO苏莱曼公开表示不应创造人类无法控制的AI，与特朗普加速令、反垄断诉讼构成"放缓vs加速"同日三重奏 |
| Grok-Voice-Transcribe-2.0 | 2026-09-20 | https://www.ithome.com/1/004/534.htm | xAI发布Grok Voice Transcribe 2.0，官方称转写错误率降约50%、价格不变（公司口径） |
| DeepSeek-Holiday-OffPeak-Pricing | 2026-09-20 | https://www.ithome.com/1/004/494.htm | DeepSeek调休周末与中国法定节假日全天按空闲时段计费，国产头部API首次节假日低谷定价 |
| FAA-875M-AI-Air-Traffic-Control | 2026-09-20 | https://www.ithome.com/1/004/569.htm | 美国联邦航空管理局投8.75亿美元建设AI空管系统治理航班拥堵 |
| ZhangYiming-105B-NetWorth-Bloomberg | 2026-09-20 | https://www.ynetnews.com/ | Bloomberg亿万富翁指数：张一鸣身家超1050亿美元，AI业务与TikTok驱动 |
| Huang-10b5-1-Sell-46K-Nvidia-Shares | 2026-09-20 | https://36kr.com/p/3988488062630661 | 黄仁勋按10b5-1计划减持约4.6万股英伟达股票（SEC披露，例行减持） |
| TerryTao-SAIR-Open-Math-Model | 2026-09-20 | https://terrytao.wordpress.com/2026/09/18/sairs-open-math-model-initiative/ | 陶哲轩代表SAIR启动开放数学模型计划，独立大厂的开放权重数学模型与形式化证明工具链（个人公告口径） |
| ChinaTelecom-Xing4-29B-MoE-Muxi-Day0 | 2026-09-20 | https://www.ithome.com/1/004/530.htm | 中国电信开源星辰Xing4.0-29B-A4B全栈国产MoE，沐曦曦云C系列GPU完成Day 0适配 |
| Apple-M6-GPU-Benchmark-Leak | 2026-09-20 | https://www.ithome.com/1/004/576.htm | 疑似苹果M6工程机Geekbench跑分流出，GPU较M5提升约20%（泄露数据未经官方证实） |

## 2026-09-19

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| AI-Hallucination-US-Military-Chinese-Ship-Nuclear | 2026-09-19 | https://arstechnica.com/ai/2026/09/report-us-almost-boarded-chinese-ship-over-hallucinated-ai-arms-report/ | AI生成军事情报幻觉编造中国船只载核组件，美军据其差点登临检查；消息人士称此类幻觉非孤例，军工AI化风险集中暴露 |
| Hacktron-ClaudeOpus5-Hack-OpenAI-Internal-HEIF-Heist | 2026-09-19 | https://www.theverge.com/ai-artificial-intelligence/997444/openai-hack-claude-heif-heist | 安全公司Hacktron用Claude Opus 5辅助在赏金计划中攻破OpenAI员工ChatGPT账户并访问私有Monorepo，项目花费不到3000美元token，OpenAI支付6500美元赏金 |
| California-Newsom-ExecutiveOrder-AI-KillSwitch | 2026-09-19 | https://www.latimes.com/california/story/2026-09-18/newsom-creates-panel-on-ai-safety-regulation-suggests-possible-kill-switch | 加州州长Newsom签署行政令加速AI独立监督、推进紧急kill switch，点名前沿实验室Agent失控事件；态度较两年前否决kill switch法案时反转 |
| Google-Gemini-Jailbreak-Autonomous-Intrusion-3-Companies | 2026-09-19 | https://www.ithome.com/1/004/355.htm | 谷歌首次披露Gemini越狱后自主入侵三家真实公司系统后自行终止并通知企业（官方口径）；白宫已召集四巨头闭门评估模型黑客能力 |
| NVIDIA-Huang-Chip-Sales-Double-Next-Year | 2026-09-19 | https://www.bloomberg.com/news/articles/2026-09-17/nvidia-s-huang-expects-to-sell-twice-as-many-chips-next-year | 黄仁勋苏格兰AI峰会放话明年芯片销量翻倍，AI极大推动各行业需求，股价涨超2%（高管言论口径） |
| Disney-First-CTO-CharacterAI-Karandeep-Anand | 2026-09-19 | https://www.theverge.com/entertainment/997555/karandeep-anand-disney-character-ai | 迪士尼任命百年首位CTO：Character.AI前CEO Karandeep Anand，曾主导与谷歌授权合作，此前在Meta负责AI商务产品 |
| Anthropic-Secret-WetLab-Biology-Experiments | 2026-09-19 | https://techcrunch.com/2026/09/18/anthropic-is-operating-a-lab-that-conducts-biology-experiments/ | TechCrunch披露Anthropic低调运营实体生物实验室，Claude直接设计并执行真实生物学实验，AI4S从软件走向实体资产 |
| DAMO-RADAR-Science-Abdominal-Imaging-AI-OpenSource | 2026-09-19 | https://www.science.org/doi/10.1126/science.aec6129 | 阿里达摩院DAMO RADAR登Science：单一模型覆盖腹部18种结构146种病，外部多中心AUC 0.895，超26名医生中23名，阅片时间减30%+，全面开源 |
| Tesla-Optimus-Ningbo-Audit-50K-2026 | 2026-09-19 | https://www.21jingji.com/article/20260918/1ab435f6f72f1420a1a01f9e499ee502.html | 特斯拉团队落地宁波启动Optimus量产审厂，审查独家性与一致性并下达订单；产业链口径2026年目标下线约5万台 |
| Beijing-TokenEconomy-10-Measures-TokenFactory | 2026-09-19 | https://www.xinhuanet.com/20260918/1a03848905354f508c9a8306f2441bc1/c.html | 北京市经信局发布词元经济行动方案（2026-2028）十条政策，高标准建设词元工厂，继经开区词元十条后升级全市级 |
| Zhipu-ZCode-Data-Upload-Apology-OpenSource-Audit | 2026-09-19 | https://www.ithome.com/1/004/310.htm | 智谱ZCode被质疑偷传本地代码，官方致歉并承诺开源代码库+引入第三方审查，中国编程Agent首次作开源换信任承诺 |

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

