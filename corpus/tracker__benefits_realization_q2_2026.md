# Portfolio Benefits Realization Tracker — Q2 2026

## Purpose and Reporting Cadence

This tracker reports the realized benefits of Copperline Retail Group's approved technology investments against the targets committed in their business cases. It is prepared by Omar Delgado, Director-level FP&A model preparer, for the Tech Investment Steering Committee co-chaired by Renata Alvarez (EVP & CFO) and Marcus Whitfield (SVP & CIO). The figures in this edition are stated **as of July 10, 2026**, covering the second quarter of fiscal year 2026.

Benefits tracking is a standing obligation under the Business Case Review and Template Guide. Every initiative that has gone live and carries measurable benefits is tracked quarterly against baseline and target, using a Red/Amber/Green (RAG) status. The tracker is not a project-status report — delivery milestones are managed elsewhere — but a financial accountability record that answers a single question for each committed benefit: are we realizing what the approved case promised, and if not, why, and what is being done about it?

As of this reporting date, two initiatives have crossed go-live and carry active benefit-tracking obligations: the Cloud Infrastructure Migration and the Omnichannel POS / Unified Commerce program. The remaining five initiatives in the portfolio are not yet in active benefit tracking, for the reasons noted in the summary table below. This edition therefore reports hard tracked data on the two live initiatives and carries the other five as informational placeholders so the Committee sees the full portfolio in one view.

RAG status is assigned per metric, not per initiative, and reflects both level and trajectory. Green means the metric is at or ahead of target. Amber means it is short of target but the gap is understood and closing, with a credible path to Green. Red means the metric is materially short with an unresolved or slow-moving cause, and it carries an expectation of a documented remediation plan. Because status weighs trajectory as well as level, an initiative can hold an Amber that is improving quarter over quarter distinct from a Red that has stalled, and the Committee should read the trend commentary alongside the color rather than the color alone.

## Portfolio Benefits Summary

The table below reports each tracked metric against its baseline and committed target. For growth metrics (opex savings, revenue lift), "% of target" is realized value divided by target. For reduction metrics (downtime, checkout time), where a lower actual is favorable, "% of target" is target divided by actual, so a figure above 100% denotes performance better than target. Baselines shown as "pre-initiative" are the measured conditions before go-live.

| Initiative | Metric | Baseline | Original target | Actual (as of Jul 10, 2026) | % of target | RAG |
|---|---|---|---|---|---|---|
| Cloud Infrastructure Migration | Opex run-rate savings | $9.4M/yr run-rate | $7.1M/yr savings | ~$6.7M/yr savings (95% of target) | 95% | Amber |
| Cloud Infrastructure Migration | Downtime | ~11.2 hrs/qtr (pre-migration) | ≤ 6.3 hrs/qtr | 5.46 hrs/qtr | 115% | Green |
| Omnichannel POS / Unified Commerce | Omnichannel revenue lift | $0 incremental | $13.4M over 3 yrs | ~63% of ramp pace ($3.9M at Feb 2026 PIR) | 63% of pace | Red |
| Omnichannel POS / Unified Commerce | Checkout time | ~98 sec (pre-initiative) | ≤ 75 sec | 62 sec | 121% | Green |
| Customer Data Platform & AI Personalization | — | — | — | Not yet tracking — approved Q1 2026, targeting live Q1 2027 (pre-go-live) | — | — |
| Cybersecurity Modernization (Zero Trust) | — | — | — | Not yet tracking — approved Q1 2026, Phase 1 live; risk-adjusted benefits, full-rollout tracking pending | — | — |
| ERP Replacement | — | — | — | Not yet tracking — approved Dec 2024, in flight (pre-go-live) | — | — |
| WMS + Robotics Pilot | — | — | — | Not yet tracking — deferred to FY2027 Q2, not yet approved to proceed | — | — |
| AI Customer Service Chatbot | — | — | — | Not tracking — rejected Q3 2026, will not proceed | — | — |

## Narrative — Cloud Infrastructure Migration

The Cloud Infrastructure Migration (sponsor: Marcus Whitfield) was approved in November 2024, went live in January 2025, and completed its 12-month post-implementation review in January 2026. It is Copperline's most mature tracked initiative and, on balance, its healthiest, though one of its two committed benefits remains short of target.

The headline financial benefit is opex run-rate savings. Against a pre-migration infrastructure run-rate of $9.4M per year, the approved case committed to $7.1M per year in savings once the estate was fully migrated and legacy contracts retired. At the January 2026 PIR, realization stood at 92% of that target. As of this July 10, 2026 tracker, realization has improved to **95% of target**, roughly $6.7M per year in annualized savings. The status remains **Amber**, but the trend is clearly improving and the trajectory is credible: the remaining gap is concentrated in a small number of legacy workloads whose decommissioning has run behind the reserved-instance and right-sizing schedule. FP&A projects this metric will reach **Green by Q4 2026** as those workloads retire and the associated dual-running costs fall away. The Amber-not-Red rating reflects that the shortfall is modest, well understood, and narrowing quarter over quarter rather than stalled.

The second committed benefit, resilience, is performing strongly. The case targeted downtime of no more than 6.3 hours per quarter, a substantial improvement on the pre-migration baseline of roughly 11.2 hours per quarter. Actual downtime is holding at **5.46 hours per quarter**, comfortably inside the target ceiling — about 13% better — and the metric is rated **Green, exceeding target**. This result validates the resilience thesis in the original business case and has translated into fewer customer-facing incidents during peak trading windows. Taken together, the Cloud Migration is delivering its risk-reduction benefit fully and its cost benefit nearly fully, with a clear path to closing the remaining opex gap.

## Narrative — Omnichannel POS / Unified Commerce

The Omnichannel POS / Unified Commerce program (sponsor: Sasha Kim) was approved in February 2025, went live in August 2025, and completed its 6-month post-implementation review in February 2026. It is the portfolio's principal area of concern this quarter.

The program's central financial benefit is omnichannel revenue lift, targeted at $13.4M over three years. Realization has lagged the committed ramp from the outset. At the February 2026 PIR, only $3.9M had been realized — approximately 58% of the pace the ramp curve called for at that point. As of this July 10, 2026 tracker, the program is running at roughly **63% of expected ramp pace**. The status is **Red**. The improvement from 58% to 63% is real but insufficient; at this trajectory the three-year target is at risk.

The root cause is well identified and is not a technology failure. The "endless aisle" capability — which lets store associates sell the full assortment, including items not stocked in that location, and is the primary engine of the modeled revenue lift — depends on associates being trained to use it at the point of sale. As of this reporting date, only **64% of stores have completed endless-aisle associate training, against a plan of 90%**. Where training is complete, attach rates and basket sizes are tracking closer to model; where it is not, the capability is effectively dormant on the floor. The revenue shortfall is therefore an adoption shortfall driven by training completion, not a defect in the platform.

The remediation plan is an **accelerated training push**: prioritizing the untrained stores by revenue potential, adding scheduled training blocks, and holding district leadership accountable for completion against the 90% plan. FP&A will track training-completion percentage as a leading indicator alongside the revenue metric in the Q3 cycle, since closing the training gap is the single most direct lever on the lagging benefit.

The program's operational benefit, by contrast, is exceeding expectations. Average checkout time has fallen to **62 seconds against a target of 75 seconds** (from a pre-initiative baseline of roughly 98 seconds), a **Green** result that confirms the new POS is delivering the faster, more unified transaction experience the case promised. The paradox of this initiative — strong operational performance, weak financial realization — is precisely why benefit tracking is separated from delivery tracking: the system works, but the revenue benefit will not materialize until the workforce is enabled to use its differentiating capability.

## Portfolio-Level Themes

A consistent theme runs through this quarter's data: **adoption, and specifically training completion, is the dominant driver of benefit realization**, more so than delivery quality. Both live initiatives have shipped working technology. Where a benefit is falling short — the POS revenue lift most acutely — the cause traces to people not yet using the capability at the intended rate, not to the capability failing to work. Even the Cloud Migration's one soft metric is a completion problem, in that case decommissioning legacy workloads rather than training staff.

This pattern has a direct implication for how future business cases should be scrutinized. Benefit models that assume rapid, near-universal adoption without a funded, scheduled, and accountable enablement plan are the ones most likely to disappoint. Reviewers should treat training completion as a first-class assumption to stress in the Scenario Modeling section, and sponsors should consider committing to leading-indicator tracking (such as training-completion percentage) from go-live rather than waiting for the lagging financial metric to turn Red. The POS experience this quarter is the concrete evidence for that guidance.

## Next Reporting Cycle

The next edition of this tracker will be prepared for **Q3 2026**, timed to align with the mid-September meeting of the Tech Investment Steering Committee. That cycle will report continued progress on the Cloud Migration opex metric — which FP&A expects to move from Amber toward Green — and, most importantly, the effect of the accelerated training push on POS endless-aisle training completion and the omnichannel revenue ramp. No new initiatives are expected to enter active benefit tracking before then, as the next go-lives (Customer Data Platform, targeting Q1 2027) remain ahead of us. The Committee will be asked to note the POS remediation plan and its leading-indicator tracking at the September sitting.
