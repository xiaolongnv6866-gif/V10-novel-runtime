# Counter-Example Candidates — 《晚明》

> Stage 1 原始候选池。此处不做三重验证、不代表已晋级能力。每条均回到原 EPUB 抽取章节核对。

- id: ce01
  title: 地盘扩大后中央直达基层变慢
  type: counter-example
  source_chapter: "第五卷 南征北战|第153章 民事官"
  source_quote: |
    地域广大造成的结果，就是有司的反应速度很慢
  summary: |
    这是文本内部对自身早期组织模式的明确修正。
  bound_to:
    - "规模触发的组织重构"
    - "中央瓶颈出现后，以地方试点建立新层级"
  failure_mode: |
    早期由中央部门直接向基层下令的方式，在地域扩大后造成处理迟滞。
  mechanism: |
    组织规模改变后，原有信息与授权路径的距离变长；同一套结构不再适配新的空间尺度。
  warning_signs:
    - "事务跨多个地区"
    - "同类事项因驻地不同处理速度悬殊"
    - "中央部门成为排队瓶颈"
  tags: [counter-example, scale, bottleneck]
  task_ids: [WM-T03]

- id: ce02
  title: 物资分配权在繁荣后变成寻租空间
  type: counter-example
  source_chapter: "第五卷 南征北战|第153章 民事官"
  source_quote: |
    由屯长控制生产物资，本身就有寻租的空间
  summary: |
    文本明确承认早期制度残余需要被重新拆权。
  bound_to:
    - "基层行政权力随经济复杂化要重新拆分"
  failure_mode: |
    开荒期集中在基层主官手中的物资分配权，在资源升值后诱发投诉和腐败空间。
  mechanism: |
    制度环境变化后，原本为效率设置的集中权力获得可交易价值；继续沿用会把基层行政变成利益入口。
  warning_signs:
    - "投诉增加"
    - "店铺/种子/耕牛等资源具有明显稀缺价值"
    - "主官既裁决又分配"
  tags: [counter-example, rent-seeking]
  task_ids: [WM-T03, WM-T11]

- id: ce03
  title: 只记得制度名词，缺少完整运行知识
  type: counter-example
  source_chapter: "第六卷 气吞山河|第32章 混乱的庭审"
  source_quote: |
    我一直以为普通法就是陪审团
  summary: |
    这是对“现代人天然懂现代制度”的直接反例。
  bound_to:
    - "制度移植的试点—暴露缺口—争论—继续/暂缓循环"
  failure_mode: |
    穿越者记得一个现代制度的显著标签，却不知道法官、程序和配套角色如何运行。
  mechanism: |
    “熟悉名词”被误当成“掌握制度”，一旦进入真实场景，缺失条件立即暴露。
  warning_signs:
    - "人物只能说出制度名称"
    - "无法说明关键角色职责"
    - "遇到边界问题只能现场猜"
  tags: [counter-example, knowledge-boundary]
  task_ids: [WM-T11]

- id: ce04
  title: 把一种制度当成普遍答案
  type: counter-example
  source_chapter: "第六卷 气吞山河|第33章 九——年"
  source_quote: |
    任何以为一个制度解决所有问题的想法都是有危害的
  summary: |
    文本通过司法争论明确提出这条反例。
  bound_to:
    - "不要把单一制度写成万能药"
  failure_mode: |
    用单一制度价值压过时代目标、执行成本与配套条件。
  mechanism: |
    制度的收益依赖环境；当人物只比较理念不比较条件，会把“先进”写成魔法。
  warning_signs:
    - "讨论只剩制度标签"
    - "没有执行主体与成本"
    - "失败被解释成“执行者不够先进”"
  tags: [counter-example, institution]
  task_ids: [WM-T11]

- id: ce05
  title: 赚钱方案与角色价值观发生冲突
  type: counter-example
  source_chapter: "第五卷 南征北战|第16章 文登军报"
  source_quote: |
    他知道烟草有害健康，乱宣传肯定会生意更好，却会让更多人因为时尚而变成烟民
  summary: |
    此例显示强组织并不自动产生道德正确的选择。
  bound_to:
    - "成功转化为新权力，同时提高政治风险"
  failure_mode: |
    高利润产品让组织利益与人物的现代健康认知发生冲突。
  mechanism: |
    组织越成熟，收益最大化不再天然等于主角价值最大化；制度能力会放大错误选择的影响。
  warning_signs:
    - "宣传效果与真实后果相反"
    - "商业部门只看增长"
    - "人物开始为“好处”合理化代价"
  tags: [counter-example, ethics, commerce]
  task_ids: [WM-T06]

- id: ce06
  title: 伤亡集中会掏空局部社区
  type: counter-example
  source_chapter: "第五卷 南征北战|第68章 畿——南"
  source_quote: |
    伤亡集中在这两个屯堡，对两个屯堡的士气损伤很大
  summary: |
    反例迫使文本重新考虑征兵制度。
  bound_to:
    - "战争成本必须穿透军队，进入家庭和社区"
  failure_mode: |
    总体损失比例看似可承受，但若集中在少数社区，会产生远高于平均值的社会后果。
  mechanism: |
    军队统计的“总量”掩盖了损失在家庭和社区中的空间分布；顶梁柱集中消失会连锁影响教育与生产。
  warning_signs:
    - "伤亡来源高度集中"
    - "学校退学增加"
    - "家庭劳动力断裂"
  tags: [counter-example, aftermath, distribution]
  task_ids: [WM-T07, WM-T10]

- id: ce07
  title: 机构重构同时激活站队与职位争夺
  type: counter-example
  source_chapter: "第五卷 南征北战|第37章 新气象"
  source_quote: |
    在座有不少民政的人事先也曾拜访徐元华或莫怀文，提前投靠以争取获得晋身的台阶
  summary: |
    制度设计必须同时写人物利益，否则会变成组织图说明书。
  bound_to:
    - "规模触发的组织重构"
  failure_mode: |
    组织重构并不会让人只按岗位理性行动，反而会提前触发站队、猜测和职位竞争。
  mechanism: |
    新的权力结构重新分配晋升机会；人物会在正式任命前先行动。
  warning_signs:
    - "任命消息尚未公布就出现拜访"
    - "群体关注谁掌握新部门"
    - "职位调整伴随私人联盟变化"
  tags: [counter-example, faction, staffing]
  task_ids: [WM-T03, WM-T13]

- id: ce08
  title: 创新第一次运行会有故障
  type: counter-example
  source_chapter: "第四卷 江山如画|第68章 军工厂与福利"
  source_quote: |
    他们搞了个样品出来，现在问题还有点多，正在改进
  summary: |
    文本在技术线中明确保留试错和熟练工瓶颈。
  bound_to:
    - "创新允许第一次出问题，但必须形成改进"
  failure_mode: |
    把新技术或新流程写成一次成功，会抹掉材料、工匠与工艺试错。
  mechanism: |
    概念可行不等于稳定生产；样品、误差、熟练工与成本都可能成为第二层问题。
  warning_signs:
    - "第一次样品就批量化"
    - "没有返工或误差"
    - "专业工匠只负责照做"
  tags: [counter-example, iteration, technology]
  task_ids: [WM-T14]

- id: ce09
  title: 旧体系中的能人不一定适合新体系内部岗位
  type: counter-example
  source_chapter: "第六卷 气吞山河|第42章 委员会"
  source_quote: |
    在旧官僚中都算能力不错的，但放到登州镇的内部管理体系中也未必适合
  summary: |
    文本把旧官员转去外务功能，而不是强行纳入内部核心管理。
  bound_to:
    - "既有名望与能力不等于适合新体系岗位"
  failure_mode: |
    因为名望、旧功或历史地位就把人物塞进核心新岗位。
  mechanism: |
    不同组织有不同信息流、执行节奏和问责方式；一般能力不能替代岗位契合度。
  warning_signs:
    - "只凭声望任命"
    - "角色没有新体系工作经验"
    - "职位存在主要是为了安置人物"
  tags: [counter-example, staffing]
  task_ids: [WM-T03, WM-T13]

- id: ce10
  title: 结构性改革拖得越晚，既得利益阻力越大
  type: counter-example
  source_chapter: "第六卷 气吞山河|第31章 道——义"
  source_quote: |
    若是以后来改，恐怕阻力就更大了
  summary: |
    此处司法从民事体系剥离的讨论明确承认延迟改革的成本。
  bound_to:
    - "制度移植的试点—暴露缺口—争论—继续/暂缓循环"
  failure_mode: |
    明知某项权力需要拆分，却因为现阶段还能勉强运作而无限推迟。
  mechanism: |
    随着群体形成稳定职位、利益和习惯，改革成本会内生增长。
  warning_signs:
    - "现有角色已经依赖该权力"
    - "问题被反复用“以后再说”延后"
    - "制度规模持续扩大"
  tags: [counter-example, path-dependence]
  task_ids: [WM-T11]
