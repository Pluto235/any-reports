# Fermi-LAT γ-ray QPO 检测调研 (2020–2025)

> **范围**：2020–2025 年发表在 arXiv 上、利用 Fermi-LAT γ 射线光变曲线搜寻
> blazar / AGN 准周期振荡 (quasi-periodic oscillation, QPO) 的 **8 篇论文**。
> 不包含 TESS 光学和方法学性质论文。
>
> **数据生成日期**：2026-05-13。数据来源于论文摘要、Tables 与 Section 4–5 正文。

## TL;DR

- **论文数**：8（其中 3 篇大样本：Chen+24 扫 134 blazars、Ren+22 扫 35 brightest、Sharma+25 扫 7）。其余 5 篇为单源研究。
- **覆盖源**：去重约 30+ 个独立 AGN（含 FSRQ、BL Lac、RDG/non-blazar）。
- **周期跨度**：~35 d (PKS 2247-131 短周期) 至 ~3 yr (S5 1044+71 ~1127 d)，主体集中在 50 d–1 yr。
- **方法演化**：LSP + REDFIT + WWZ（最常见组合）→ 加 CWT post-trial + Emmanoulopoulos PSD/PDF Monte Carlo（Ren+22 引入）→ 再加 Gaussian Process (DRW / SHO) + MCMC 物理参数拟合（Sharma+25 集成）。
- **物理图像**：短周期 (< 1 yr) 偏好 helical jet / plasma blob helical motion；长周期 (> 1 yr) 偏好 SMBBH 轨道进动 / Lense-Thirring；mildly beamed 与 non-blazar 系统讨论 accretion + lighthouse 效应。
- **发生率**：Chen+24 在 134 blazars 严格筛选下给出 transient QPO 发生率 **~3%**。

## 主表 — 每篇论文一览

| # | 论文 | 样本 | 周期范围 / 数量 | 最高 σ | 主要方法 | Fermi 数据 | 物理解释 |
|---|---|---|---|---|---|---|---|
| 1 | Kushwaha+ 2020 | OJ 287 | ~314 d × 1 | ~3σ | LSP, REDFIT, WWZ | 2008-08 → 2018-02 | quasi-stationary radio knots / SMBBH |
| 2 | Zhang+ 2021 | PKS 0521-36 | ~1.1 yr × 1 | ~5σ | LSP, WWZ, REDFIT, GP | 2008-08 → 2021-03 | γ-ray outburst-driven (mildly beamed) |
| 3 | Ren+ 2022 | 35 brightest 4LAC (19 FSRQ + 15 BL Lac + 1 RDG) | 30 d – 1127 d，**36 QPO 候选 in 24 源** | >5σ post-trial | CWT (Morlet) + global wavelet + Emmanoulopoulos MC | 2008-08 → 2021-04 | SMBBH / jet precession / helical |
| 4 | Gong+ 2023 | S4 0954+658 | 66 d & 210 d | >5σ (66d) | LSP, WWZ, REDFIT, epoch fold | 2008 → 2022 | plasma blob helical motion |
| 5 | Zhang+ 2023 | S2 0109+22 | ~600 d | 3.5σ | LSP, WWZ, REDFIT, phase fold | 2008-08 → 2023-01 | binary BH + lighthouse |
| 6 | Sharma+ 2023 | PKS 0521-36 | 268 d, 295 d, 806 d | >3σ | LSP, WWZ, GP (SHO + DRW) | 2008-08 → 2023 (15 yr) | first long-term QPO in non-blazar AGN |
| 7 | Chen+ 2024 | 134 blazars (flux-limited) → 6 源 8 QPO | 54 d – 341 d | ~4.3σ (PKS 1510-089) | WWZ + LSP + Emmanoulopoulos MC, 严格 5+ cycles | 2008-08 → ~2021-04 | helical jet (favored) |
| 8 | Sharma+ 2025 | 7 blazars | ~225 d – ~1449 d | 4σ (PKS 0736+01) | LSP + REDFIT + DRW MC (30k LC) + MCMC SMBBH 拟合 | 2008-08 → 2025-04 (15+ yr) | SMBBH 主导 + jet precession |

## 完整 QPO 候选列表（每行 = 一个源 × 一个 QPO 信号）

按发表年份-论文-显著性排序。同一源出现在不同论文里时多次列出，便于对比。

| # | Source | 4FGL / 类型 | 周期 (d) | Cycles | σ | 方法 | 论文 |
|---|---|---|---|---|---|---|---|
| 1 | OJ 287 | J0854.8+2006 / BL Lac | 314 | — | ~3σ | LSP+REDFIT+WWZ | Kushwaha+ 2020 |
| 2 | PKS 0521-36 | J0522.9-3628 / non-blazar AGN | ~400 (~1.1 yr) | — | ~5σ | LSP+WWZ+REDFIT+GP | Zhang+ 2021 |
| 3 | 4C +01.02 | J0108.6+0134 / FSRQ | 268±55 | 4 | >5σ | CWT 30d | Ren+ 2022 |
| 4 | 4C +01.02 | FSRQ | 123±26 (∼122±26 7d) | 5 | 4.7σ / >5σ | CWT | Ren+ 2022 |
| 5 | PKS 0537-441 | J0538.8-4405 / BL Lac | 285±67 (∼286±73 7d) | 4 | >5σ | CWT | Ren+ 2022 |
| 6 | **S5 1044+71** | J1048.4+7143 / FSRQ | **1127±226** (~3 yr) | 3 | 4.6σ post-trial（首报） | CWT | Ren+ 2022 |
| 7 | S5 1044+71 | FSRQ | 117±38 | 4 | >5σ | CWT | Ren+ 2022 |
| 8 | B2 1520+31 | J1522.1+3144 / FSRQ | 179±42 | 6 | >5σ | CWT | Ren+ 2022 |
| 9 | B2 1520+31 | FSRQ | 71±15 | 14 | >5σ | CWT 7d | Ren+ 2022 |
| 10 | B2 1520+31 | FSRQ | 39±11 | 17 | >5σ | CWT 7d | Ren+ 2022 |
| 11 | PKS 2247-131 | J2250.0-1250 / BL Lac | 214±43 | 6 | >5σ | CWT | Ren+ 2022 |
| 12 | PKS 2247-131 | BL Lac | **34±13** (~1 month) | 10 | >5σ | CWT 7d | Ren+ 2022 |
| 13 | NGC 1275 | J0319.8+4130 / RDG | 92±33 (7d) | 4 | >5σ | CWT | Ren+ 2022 |
| 14 | … | 其余 18 源、~20 个候选 | 见 paper Table 2 | | | | Ren+ 2022 |
| 15 | S4 0954+658 | / BL Lac | 66 ± 4.8 | 9 | >5σ | LSP+WWZ+REDFIT+epoch fold | Gong+ 2023 |
| 16 | S4 0954+658 | BL Lac | 210 ± 43 | 4 | ~3.5σ | 同上 | Gong+ 2023 |
| 17 | S2 0109+22 | J0112.1+2245 / BL Lac | ~600 | 5.6 | ~3.5σ | LSP+WWZ+REDFIT+phase fold | Zhang+ 2023 |
| 18 | PKS 0521-36 | non-blazar AGN | 268 | — | >3σ | LSP+WWZ+GP(SHO+DRW) | Sharma+ 2023 |
| 19 | PKS 0521-36 | non-blazar AGN | 295 / 283 (PSD) | — | >3σ | 同上 | Sharma+ 2023 |
| 20 | PKS 0521-36 | non-blazar AGN | **806 / 886 (PSD)** — 268 d 的第三谐波 | — | >3σ | 同上 | Sharma+ 2023 |
| 21 | 4C +01.02 | FSRQ | 253.2 ± 20.0 | 6 | ~2.7σ | WWZ+LSP | Chen+ 2024 |
| 22 | **PKS 0336-01** | / FSRQ | **94.6 ± 6.8** ★新发现 | 6 | ~3.4σ | WWZ+LSP | Chen+ 2024 |
| 23 | PKS 0402-362 | FSRQ | 103.9 ± 6.7 | 5 | ~2.6σ | WWZ+LSP | Chen+ 2024 |
| 24 | **PKS 0537-441** | BL Lac | **55.0 ± 3.3 (QPO I)** ★新 | 7 | ~4.1σ | WWZ+LSP | Chen+ 2024 |
| 25 | **PKS 0537-441** | BL Lac | **54.7 ± 3.3 (QPO II)** ★新（重复 transient） | 7 | ~4.0σ | WWZ+LSP | Chen+ 2024 |
| 26 | **PKS 1424-41** | FSRQ | **57.1 ± 4.5 (QPO I)** ★新（嵌套） | 6 | ~3.2σ | WWZ+LSP | Chen+ 2024 |
| 27 | PKS 1424-41 | FSRQ | 341 ± 25.8 (QPO II) | 6 | ~3.7σ | WWZ+LSP | Chen+ 2024 |
| 28 | PKS 1510-089 | J1512.8-0906 / FSRQ | 92.3 ± 5.2 | 8 | ~4.3σ | WWZ+LSP | Chen+ 2024 |
| 29 | PKS 0736+01 | J0739.2+0137 / FSRQ | ~1449 (~4 yr) | — | 4σ | LSP+REDFIT+DRW | Sharma+ 2025 |
| 30 | PKS 1424-41 | FSRQ | ~357 | — | 3σ | LSP+REDFIT+DRW | Sharma+ 2025 |
| 31 | S2 0109+22 | BL Lac | ~667 | — | 3σ | LSP+REDFIT+DRW | Sharma+ 2025 |
| 32 | PKS 0244-470 | FSRQ | ~227 | — | 3σ | LSP+REDFIT+DRW | Sharma+ 2025 |
| 33 | PKS 0405-385 | FSRQ | ~1000 | — | 2.9σ | LSP+REDFIT+DRW | Sharma+ 2025 |
| 34 | PKS 0208-512 | FSRQ | ~909 | — | 2.85σ | LSP+REDFIT+DRW | Sharma+ 2025 |
| 35 | PKS 0035-252 | FSRQ | ~357 | — | 2.8σ | LSP+REDFIT+DRW | Sharma+ 2025 |

★ = 该源在该周期/方法下的首次报告。
注：Ren+ 2022 给出 36 个候选，本表只列摘要里 5 个最显著源；完整列表见原文 Table 2。

## 逐篇细读

### 1. Kushwaha+ 2020 — OJ 287 [arXiv:2009.13754]

- **源**：OJ 287 (BL Lac，z=0.306)，最经典的 SMBBH 候选体（光学 12-yr QPO）。
- **检测**：γ-ray 月度 binned 光变曲线中识别 ~314 d 周期 (~3σ)。
- **方法**：LSP、REDFIT、WWZ 三件套，无 GP。
- **解释**：与 quasi-stationary radio knot 位置漂移和 γ-ray–mm radio 强相关一致 — 信号可能与喷流内静止结节相关，而非 SMBBH 12-yr 主周期。
- **数据**：Fermi-LAT 2008-08 → ~2018-02 (约 9.5 yr)。

### 2. Zhang+ 2021 — PKS 0521-36 [arXiv:2106.10040]

- **源**：PKS 0521-36 — 4LAC 中分类为 BL Lac / 中间态非典型 blazar，**mildly beamed jet**。
- **检测**：在两次 outburst（2012-10 和 2019-05）之间的 ~5.8 yr 窗口（MJD 56317–58447）内识别 **~1.1 yr 周期 (~5σ)**。
- **方法**：LSP + WWZ + REDFIT 三种 + Gaussian Process 模型四种独立验证。
- **解释**：首例 γ-ray QPO in mildly beamed jet；推测 γ-ray outburst 在 QPO 形成中起关键作用。
- **数据**：~12.6 yr LAT 全数据，但 QPO 仅在 5.8 yr 窗口内。

### 3. Ren, Cerruti & Sahakyan 2022 — 35 brightest AGN [arXiv:2204.13051]

- **样本**：4LAC 中最亮 34 个 + 手工加入 PKS 2247-131，共 35 个（19 FSRQ + 15 BL Lac + 1 radio galaxy NGC 1275）。
- **方法**：Continuous Wavelet Transform (Morlet, via `PyCWT`) + global wavelet spectrum + **post-trial look-elsewhere correction** (Auchère 2016) + Emmanoulopoulos PSD/PDF Monte Carlo（10⁴ artificial LC × 每源 × 每 binning）。
- **时间 binning**：30 d 与 7 d 两套，独立比对。
- **能段**：100 MeV – 500 GeV。**数据跨度** Aug 2008 → Apr 2021 (MJD 54686-59308)。
- **结果**：**36 QPO 候选 in 24/35 源**（post-trial σ > 3，至少 3 cycles）。
  - 长周期 (>1 yr) 出现在 5 源：**S5 0716+714, S5 1044+71, Mrk 421, PKS 2155-304, CTA 102**。
  - 月周期 (<300 d) 出现在 20 源。
  - 摘要 5 个最显著：4C +01.02, PKS 0537-441, **S5 1044+71** (1127 d 首报), B2 1520+31, PKS 2247-131。
- **结论**：**所有候选均为 transient**（在分析窗口内出现/消失）。S5 1044+71 ~3 yr 周期作为最长多年 QPO 首次报告。
- **解释**：与 SMBBH 在 SMBH 演化中的存在关联，但保持开放，认为 jet 内/外多种几何机制都可解释。

### 4. Gong+ 2023 — S4 0954+658 [arXiv:2304.03085]

- **源**：S4 0954+658 (BL Lac, z=0.367)。
- **检测**：两个分段 transient QPO：
  - **66 ± 4.8 d (>5σ)**，MJD 57145–57745（2015–2016），**9 cycles** — blazar γ-ray QPO 中观测到的最多 cycle 之一。
  - **210 ± 43 d (~3.5σ)**，MJD 59035–59915（2020–2022），4 cycles。
- **方法**：LSP + WWZ + REDFIT + epoch folding。
- **解释**：plasma blob 沿 helical 路径运动 + jet 几何模型 — 与短周期一致。

### 5. Zhang+ 2023 — S2 0109+22 [arXiv:2306.11579]

- **源**：S2 0109+22 (BL Lac, z~0.36)。射电、毫米波已知 ~657 d 周期。
- **检测**：**~600 d (3.5σ)**，2013-11 至 2023-01，~9 yr / **5.6 cycles**。
- **方法**：WWZ + LSP + REDFIT + phase-folded LC。Baluev 假警报修正 + Emmanoulopoulos MC (10⁵ LCs)。
- **数据**：Fermi-LAT 2008-08-04 → 2023-01-16，7-day binned, TS>9。
- **解释**：与已知 radio 周期一致 → binary BH 系统的 accretion + lighthouse 效应。

### 6. Sharma, Prince & Bose 2023 — PKS 0521-36 [arXiv:2312.12623]

- **源**：PKS 0521-36（与 Zhang+ 2021 同源）。**non-blazar AGN**，弱 beamed jet。
- **检测**：3 个周期：**268 d, 295 d, 806 d (>3σ)**；其中 806 d 是 268 d 的 **第三谐波**。GP（SHO + DRW）模型 PSD 显示 ~283 d 和 ~886 d 两个峰。
- **方法**：LSP + WWZ + GP（SHO/DRW）。
- **数据**：Fermi-LAT 15 yr 全数据。
- **意义**：首例长周期 (>800 d) γ-ray QPO in non-blazar AGN。
- **与 Zhang+ 2021 对比**：Zhang+ 2021 在更短窗口给出 ~1.1 yr (~400 d)；Sharma+ 2023 在 15 yr 全数据给出多个周期且都更短/更长。说明在 5.8 yr vs 15 yr 窗口内，主导信号不同。

### 7. Chen+ 2024 — 134 blazars systematic search [arXiv:2401.10658]

- **样本**：134 blazars（Monitored Source List 中 peak flux > 1×10⁻⁶ ph cm⁻²s⁻¹，7 BCU + 31 BL Lac + 95 FSRQ）。
- **方法**：WWZ 全光变曲线扫描 → LSP 独立验证 → Emmanoulopoulos PSD/PDF MC 给出 σ。
- **筛选标准**（比 Ren+ 2022 严格）：
  1. cycles ≥ 5
  2. 缺数据 < 60%
  3. 肉眼可识 QPO
- **结果**：8 个 transient QPOs in 6 sources，全为 FSRQ 或 BL Lac：
  - PKS 0537-441 (2 个 QPO，重复 transient)
  - PKS 1424-41 (2 个 QPO，嵌套 — 短周期叠在长周期上)
  - 4C +01.02, PKS 0336-01, PKS 0402-362, PKS 1510-089 各 1 个
- **新发现 4 个**（首报）：PKS 0336-01 94 d、PKS 0537-441 55 d & 54 d、PKS 1424-41 57 d。
- **发生率估算**：~3%。
- **解释**：helical jet motion 模型 best fit；同时讨论磁岛 / 磁重联，但 helical jet 仍最优。

### 8. Sharma+ 2025 — 7 blazars + SMBBH 拟合 [arXiv:2505.23697]

- **样本**：7 blazars (PKS 1424-41, PKS 0736+01, S2 0109+22, PKS 0244-470, PKS 0405-385, PKS 0208-512, PKS 0035-252)。
- **数据**：Fermi-LAT 2008-08-05 → 2025-04-01 (MJD 54683–60766)，weekly binned，TS ≥ 9。
- **方法链条**：
  1. LSP + REDFIT 找候选峰
  2. DRW (Damped Random Walk) 模型 + **30,000 个 synthetic LC** 评估显著性
  3. MCMC 拟合 SMBBH 物理参数（Lorentz factor Γ、视角 ψ）
- **检测**（7 源全部检出，σ 不同）：
  - PKS 0736+01 ~1449 d / 4σ（**首次报告**该源 QPO）
  - PKS 1424-41 ~357 d / 3σ
  - S2 0109+22 ~667 d / 3σ
  - PKS 0244-470 ~227 d / 3σ
  - PKS 0405-385 ~1000 d / 2.9σ
  - PKS 0208-512 ~909 d / 2.85σ
  - PKS 0035-252 ~357 d / 2.8σ
- **物理解释**：长周期 (>1 yr) 在 SMBBH 框架下 — 约束 Γ ~ 10–20，ψ 几度量级；助攻 SMBBH + 喷流方向相关性研究。

## 跨论文交叉

### 同一源在多篇里出现

| 源 | 论文 | 周期 / σ |
|---|---|---|
| PKS 0521-36 (non-blazar AGN) | Zhang+ 2021 | ~1.1 yr / ~5σ |
|  | Sharma+ 2023 | 268 / 295 / 806 d / >3σ |
| PKS 1424-41 (FSRQ) | Ren+ 2022 | 90±22, 92±25 d, >5σ |
|  | Chen+ 2024 | 57 / 341 d / 3.2σ / 3.7σ |
|  | Sharma+ 2025 | ~357 d / 3σ |
| S2 0109+22 (BL Lac) | Zhang+ 2023 | ~600 d / 3.5σ |
|  | Sharma+ 2025 | ~667 d / 3σ |
| PKS 0537-441 (BL Lac) | Ren+ 2022 | 285 d (~5σ) |
|  | Chen+ 2024 | 55 / 54 d (~4σ) — 双 transient |
| PKS 0402-362 (FSRQ) | Ren+ 2022 | 221±56 d, 122±42 d |
|  | Chen+ 2024 | 103.9 d / 2.6σ |
| 4C +01.02 (FSRQ, z=2.099) | Ren+ 2022 | 268, 123 d / >5σ |
|  | Chen+ 2024 | 253 d / 2.7σ |
| PKS 1510-089 (FSRQ) | Ren+ 2022 | 119±31, 120±36 d |
|  | Chen+ 2024 | 92.3 d / 4.3σ |
| OJ 287 (BL Lac) | Kushwaha+ 2020 | 314 d / ~3σ |
|  | Ren+ 2022 | ∼300 d 量级（未在最显著 5 名内）|

观察：
- **方法越严格、周期估计往往越短**：Chen+ 2024 用严格 ≥5 cycles 筛选，发现的周期 (54–341 d) 比 Ren+ 2022 (含 long-period) 更窄。
- **数据窗口决定主导信号**：PKS 0521-36 在 5.8 yr vs 15 yr 给出不同周期组（说明 transient QPO 在不同时段切换）。

### 方法使用频率

| 方法 | 使用论文数 / 8 |
|---|---|
| LSP (Lomb-Scargle) | 8 |
| WWZ (Weighted Wavelet Z-transform) | 7 |
| REDFIT | 6 |
| Emmanoulopoulos PSD/PDF MC | 4 |
| Gaussian Process (DRW / SHO) | 3 |
| Phase fold / epoch fold | 3 |
| CWT (Morlet, post-trial corrected) | 1 (Ren+ 2022) |
| MCMC 物理参数拟合 | 1 (Sharma+ 2025) |

### 物理解释优先级

| 解释模型 | 用于哪类周期 | 出现频次 |
|---|---|---|
| Helical jet / plasma blob helical motion | 短周期 (< 1 yr) | 5 篇 |
| SMBBH orbital / precession | 长周期 (> 1 yr) | 4 篇 |
| Lense-Thirring precession | 长周期 | 2 篇 |
| Accretion disk instability + lighthouse | non-blazar / mildly beamed | 3 篇 |
| Magnetic islands / reconnection | 短周期 alternative | 1 篇 (Chen+ 2024 讨论) |

## 显著性 σ 分布

|  σ 范围 | 候选数（含重复源） |
|---|---|
| > 5σ (post-trial) | ~20+（主要来自 Ren+ 2022） |
| 4–5σ | ~5 |
| 3–4σ | ~10 |
| < 3σ | ~3 (Chen+ 2024 中 4C +01.02 253-d 等) |

## 数据 binning 约定

| 论文 | binning |
|---|---|
| Kushwaha+ 2020 | monthly (~30 d) |
| Zhang+ 2021 | 30 d |
| Ren+ 2022 | 7 d + 30 d 并行 |
| Gong+ 2023 | 7 d |
| Zhang+ 2023 | 7 d (+ 10/30 d 验证) |
| Sharma+ 2023 | weekly |
| Chen+ 2024 | weekly |
| Sharma+ 2025 | weekly |

7-day binned 已成 2022 年后的实际标准（短周期 < 1 yr 几乎必须）。

## 参考文献

1. **Kushwaha P., Sarkar A., Gupta A. C., Tripathi A., Wiita P. J.**, 2020, *MNRAS*, 499, 653. *A Possible γ-ray Quasi-periodic Oscillation of ~314 days in the Blazar OJ 287.* [arXiv:2009.13754](https://arxiv.org/abs/2009.13754) · [DOI 10.1093/mnras/staa2899](https://doi.org/10.1093/mnras/staa2899)
2. **Zhang H., Yan D., Zhang P., Yang S., Zhang L.**, 2021, *ApJ*, 919, 58. *A Quasi-periodic Oscillation in the γ-ray Emission from the Non-blazar Active Galactic Nucleus PKS 0521-36.* [arXiv:2106.10040](https://arxiv.org/abs/2106.10040) · [DOI 10.3847/1538-4357/ac0cf0](https://doi.org/10.3847/1538-4357/ac0cf0)
3. **Ren H. X., Cerruti M., Sahakyan N.**, 2023, *A&A* (submitted Feb 2023). *Quasi-periodic oscillations in the γ-ray light curves of bright active galactic nuclei.* [arXiv:2204.13051](https://arxiv.org/abs/2204.13051)
4. **Gong Y., Tian S., Zhou L., Yi T., Fang J.**, 2023, *ApJ*, 949, 39. *Two Transient Quasi-periodic Oscillations in γ-Ray Emission from the Blazar S4 0954+658.* [arXiv:2304.03085](https://arxiv.org/abs/2304.03085) · [DOI 10.3847/1538-4357/acca7b](https://doi.org/10.3847/1538-4357/acca7b)
5. **Zhang H., Wu F., Dai B.**, 2023, *PASP*, 135, 074101. *The detection of possible γ-ray quasi-periodic modulation with ~600 days from the blazar S2 0109+22.* [arXiv:2306.11579](https://arxiv.org/abs/2306.11579) · [DOI 10.1088/1538-3873/acdf1f](https://doi.org/10.1088/1538-3873/acdf1f)
6. **Sharma A., Prince R., Bose D.**, 2023, *MNRAS* (submitted). *Detection of gamma-ray quasi-periodic oscillations in non-blazar AGN PKS 0521-36.* [arXiv:2312.12623](https://arxiv.org/abs/2312.12623)
7. **Chen J., Yu J., Huang W., Ding N.**, 2024, *MNRAS*, 528, 6807. *Transient quasi-periodic oscillations in the gamma-ray light curves of bright blazars.* [arXiv:2401.10658](https://arxiv.org/abs/2401.10658) · [DOI 10.1093/mnras/stae416](https://doi.org/10.1093/mnras/stae416)
8. **Sharma A., Chaudhary S., Sarath A., Bose D.**, 2025, preprint. *Exploring Year-timescale Gamma-ray Quasi-Periodic Oscillations in Blazars: Evidence for Supermassive Binary Black Holes Scenario.* [arXiv:2505.23697](https://arxiv.org/abs/2505.23697)

---

*报告生成：2026-05-13 · 数据来源：上述 8 篇 arXiv PDF（保存在 `/home/server/projects/QPO/docus/`）· 数字与论文原表/正文对应；同一源在不同论文给出不一致周期时，原值保留 — 不在本报告中合并。*
