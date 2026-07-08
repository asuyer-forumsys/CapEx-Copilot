# Business Case: Cloud Infrastructure Migration

## Executive Summary

Copperline Retail Group's core application estate runs on an aging, self-operated data center footprint anchored by the primary facility in Charlotte, NC, with a secondary co-location site that provides only partial disaster-recovery coverage. This infrastructure — much of it refreshed last in 2018–2019 and now approaching or past its planned replacement horizon — has become a constraint on the business rather than a foundation for it. It cannot scale elastically to absorb e-commerce peak traffic, its disaster-recovery posture leaves the company exposed to unacceptable recovery objectives, and its operating cost is high and rising as hardware ages and support premiums escalate.

This business case, sponsored by Marcus Whitfield (SVP & CIO), proposes a comprehensive migration of Copperline's production and non-production workloads to public cloud infrastructure over a twelve-month program, retiring the majority of the on-premise footprint and re-platforming the company's customer-facing and core operational systems onto elastic, cloud-native infrastructure with a modern disaster-recovery architecture.

The three-year total cost of ownership is estimated at $14.2M, inclusive of migration execution, cloud run-rate, and transition-period parallel operating costs. Projected three-year benefits total $19.6M, driven by data-center operating-cost reduction, availability improvement (reduced unplanned downtime), avoided hardware-refresh capital, and the scalability and elasticity needed to serve e-commerce peaks without over-provisioning. At Copperline's standard 8% discount rate, the migration produces a net present value of $4.1M, an internal rate of return of 31%, and a payback period of 22 months.

Among the initiatives in Copperline's technology-modernization portfolio, this migration carries the strongest headline return — a 31% IRR and a 22-month payback — for a reason that is structural rather than incidental. Its benefits rest on well-understood, largely deterministic economics: eliminating a known operating-cost run-rate, avoiding a near-term hardware-refresh outlay that would otherwise be unavoidable, and closing a disaster-recovery gap that has been flagged repeatedly in internal risk reviews. Unlike initiatives whose value depends on customer behavior, adoption, or new revenue, the bulk of this case's benefit is cost the company is already incurring and can stop incurring. That is what makes it both the most financially attractive and the most defensible leadoff investment of the modernization program.

The financial model for this case was prepared by Omar Delgado (Director, FP&A). The case is submitted to the Tech Investment Steering Committee, co-chaired by Renata Alvarez (EVP & CFO) and Marcus Whitfield (SVP & CIO), for its Q4 2024 review, with a targeted approval in November 2024 and program go-live in January 2025.

## Problem and Strategic Context

### An aging on-premise data-center footprint

Copperline operates its own primary data center in Charlotte, NC, supported by a secondary co-location facility that was originally intended as a full disaster-recovery site but has, in practice, been provisioned only for a subset of critical systems. The compute, storage, and network hardware in the primary facility is largely at or beyond its planned five-year refresh cycle. Continuing on the current path means a substantial, near-term capital outlay simply to refresh in place — replacing end-of-life servers, storage arrays, and network gear — with no strategic return beyond keeping the lights on.

The estate is also operationally heavy. A significant share of the infrastructure team's capacity is consumed by undifferentiated maintenance: patching, firmware, hardware break-fix, capacity planning, and the sheer overhead of running physical facilities. This is engineering effort spent on keeping infrastructure alive rather than on advancing the application capabilities that differentiate Copperline in a competitive specialty-retail market. The opportunity cost compounds: every quarter the team spends absorbed in facility and hardware operations is a quarter it is not spending on the automation, observability, and platform work that the rest of the modernization roadmap will demand of it.

The support economics are deteriorating as well. As hardware moves past its supported life, extended-support premiums and third-party maintenance costs rise sharply, and spare-parts availability for older platforms becomes both more expensive and less reliable. Copperline is, in effect, paying an escalating tax to keep an aging estate running — a tax that buys no new capability and grows every year the refresh decision is deferred.

### Disaster-recovery gaps

The most acute risk in the current environment is disaster recovery. Because the secondary site covers only a subset of critical systems and relies on manual, infrequently tested failover procedures, Copperline's realistic recovery-time and recovery-point objectives for a primary-site loss are far worse than the business requires. A serious event at the Charlotte facility — power, cooling, network, or physical — would threaten extended outages to store systems, e-commerce, and the supporting back office. For a retailer that now transacts roughly 18% of its $1.92B in FY2025-trajectory revenue online and depends on integrated store systems across 214 locations, that exposure is not acceptable. The current DR posture has been flagged repeatedly in internal risk reviews.

### Scaling constraints for e-commerce peak traffic

Copperline's e-commerce channel has grown steadily and now contributes a meaningful and rising share of revenue, with demand concentrated in seasonal peaks — the fourth-quarter holiday period and promotional events. On-premise infrastructure forces a structural inefficiency: to serve peak, the company must provision for peak year-round, carrying idle capacity for most of the year and still risking saturation during unanticipated surges. There is no elasticity. Every peak season, the digital-commerce and infrastructure teams manage capacity headroom manually and conservatively, trading cost against risk. A cloud-native footprint replaces this with elastic scaling that provisions capacity to demand and releases it when demand recedes.

The consequences of getting this wrong are asymmetric and expensive. Under-provisioning during a holiday surge or a viral promotional event means degraded site performance or outright outages at precisely the moment the channel is generating its highest revenue — a direct hit to sales and to brand trust. Over-provisioning, the company's current defensive posture, means paying year-round for capacity used only a few weeks a year. Neither option is acceptable at the scale Copperline's digital channel has reached. Elastic infrastructure resolves the dilemma by decoupling capacity from ownership: the company pays for peak capacity only during peak and sheds it afterward, converting a large fixed provisioning decision into a variable cost that tracks actual demand.

### Strategic alignment

This migration is the foundational layer beneath Copperline's broader technology-modernization portfolio. The initiatives that follow it — unified commerce and omnichannel POS, a customer data platform, ERP replacement, and security modernization — all assume a scalable, resilient, cloud-based infrastructure substrate. Undertaking those programs on the current on-premise footprint would either be impossible or would require duplicative, throwaway investment. Sequencing the cloud migration first, in FY2025, de-risks and enables the entire multi-year roadmap. This is why the CIO sponsors it directly and why it is positioned as the leadoff initiative of the modernization program.

## Financial Modeling

The three-year total cost of ownership captures one-time migration execution, ongoing cloud run-rate, transition-period parallel running (during which both on-premise and cloud costs are carried), and internal program cost. All figures are in USD millions and use Copperline's standard 8% discount rate for NPV. The one-time implementation (migration execution plus transition-period parallel run and program cost concentrated in Year 1) is targeted at $6.8M.

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Yr Total |
|---|---|---|---|---|
| Cloud infrastructure run-rate | 2.10 | 3.30 | 3.60 | 9.00 |
| Migration execution (SI + tooling) | 3.40 | 0.50 | 0.20 | 4.10 |
| Transition-period parallel run (legacy overlap) | 1.60 | 0.30 | 0.00 | 1.90 |
| Internal program & change management | 0.55 | 0.35 | 0.30 | 1.20 |
| **Total Cost of Ownership** | **7.65** | **4.45** | **4.10** | **16.20** |
| Less: avoided legacy run-rate (offset) | (0.40) | (0.80) | (0.80) | (2.00) |
| **Net Total Cost of Ownership** | **7.25** | **3.65** | **3.30** | **14.20** |

Cost is front-loaded into Year 1, when migration execution, tooling, and the bulk of parallel-running overlap occur. Cloud run-rate rises across the three years as workloads migrate off legacy and settle into steady state, while the avoided legacy run-rate offset grows as on-premise systems are decommissioned. Net of the legacy offset, the three-year TCO is $14.2M. Discounted at 8% against the benefit stream below, the migration yields an NPV of $4.1M, an IRR of 31%, and a 22-month payback measured from program start.

Two modeling choices are worth surfacing for the Committee. First, the transition-period parallel-run line is a genuine and often-underestimated cost of any migration: for a period, Copperline pays for both the legacy environment and its cloud replacement, and the size of that overlap is directly tied to how quickly legacy systems are shut down. The model assumes a disciplined decommissioning schedule that confines the bulk of parallel running to Year 1; a slower schedule would inflate this line, which is why decommissioning pace features so prominently in the risk assessment and scenario modeling below. Second, the cloud run-rate is modeled on committed-use and reserved-capacity pricing for stable baseline workloads, with elastic on-demand capacity reserved for peak — the combination that yields the lowest total run-rate while preserving the elasticity that is a core benefit of the move. The figures do not assume aggressive future optimization; they reflect a conservative steady-state posture the infrastructure team is confident it can hold from the outset.

## Benefits Analysis

Benefits derive from four sources: reduced unplanned downtime, data-center operating-cost savings, scalability and elasticity for peak, and an improved disaster-recovery posture. The table states each driver's baseline (current on-premise state) and the target end-state at steady operation post-migration.

| Benefit Driver | Baseline (On-Premise) | Target (Cloud) | Basis of Value |
|---|---|---|---|
| Unplanned downtime | 14 hrs/quarter | 6.3 hrs/quarter (−55%) | Availability of revenue-generating & store systems |
| Data-center opex run-rate | $9.4M/yr | $7.1M/yr (−$2.3M/yr savings) | Facilities, hardware maintenance, support premiums |
| Peak scalability / elasticity | Provision-for-peak, idle capacity | Elastic scale-to-demand | Avoided over-provisioning; peak headroom without capex |
| Disaster-recovery posture | Partial DR, manual failover | Multi-AZ, automated failover | Materially improved RTO/RPO; reduced tail risk |
| Hardware-refresh capital | Near-term refresh required | Avoided | Deferred/avoided on-premise capital outlay |

The two most heavily monetized drivers are downtime reduction and operating-cost savings. Reducing unplanned downtime from a baseline of 14 hours per quarter to a target of 6.3 hours per quarter — a 55% improvement — protects revenue and productivity across e-commerce and store systems; the model values this using an internal per-hour cost of downtime blended across affected systems. Operating-cost savings come from reducing the legacy data-center run-rate of $9.4M/yr toward a target future-state cloud-plus-residual run-rate of $7.1M/yr, a targeted steady-state saving of $2.3M/yr, realized progressively as legacy facilities and hardware are decommissioned. Avoided hardware-refresh capital is a genuine benefit — the migration eliminates the near-term in-place refresh the company would otherwise have to fund — and scalability/elasticity is valued as the avoided cost of provisioning for peak year-round.

The disaster-recovery improvement is treated as a partially monetized, largely qualitative benefit. While the reduction in tail risk is real and important, the model credits it conservatively rather than attempting to fully price a low-probability, high-impact event; the strategic value of a defensible RTO/RPO is presented to the Committee as a risk-reduction argument in its own right. Put plainly, the company is today one serious Charlotte-facility event away from a multi-day outage across store systems and e-commerce, and the migration removes that single point of failure. The Committee is asked to weigh that protection as a benefit in itself, independent of the modest figure the model attaches to it.

Benefits phase in as workloads migrate. Operating-cost savings ramp with legacy decommissioning; availability and DR benefits accrue as systems land on the resilient cloud architecture. The model assumes the benefit stream builds through Year 1 and reaches full run-rate in Years 2 and 3. Because the operating-cost saving is realized only when legacy systems are actually shut down — not merely when their replacements go live in the cloud — the case treats decommissioning as a first-class deliverable with its own schedule and gates, rather than as a clean-up activity to be handled after migration. The integrity of the opex benefit depends entirely on that discipline, a point the risk assessment returns to below.

## Risk Assessment

The following assessment uses Copperline's five standard business-case risk categories.

| Risk Category | Rating | Description | Primary Mitigation |
|---|---|---|---|
| Implementation overrun | Medium-High | Large-scale migration with many interdependent workloads; unplanned integration or networking work could extend timeline and cost. | Wave-based migration plan, experienced SI partner, contingency in Year 1 budget, executive-sponsored program governance. |
| Benefit-realization shortfall | Medium | Operating-cost savings depend on timely legacy decommissioning; delayed shutdown erodes the opex benefit. | Explicit decommissioning schedule tied to each migration wave, benefits tracking against Delgado's model, decommission gates in program plan. |
| Data-quality degradation | Low-Medium | Data migration and re-platforming risk integrity issues during cutover. | Staged cutovers with reconciliation, parallel-run validation, rollback procedures per wave. |
| Adoption failure | Low-Medium | Infrastructure and application teams must adopt cloud operating models and tooling; skills gaps could slow realization. | Cloud enablement and training program, managed-service support during transition, phased handover to internal teams. |
| Vendor viability | Low | Reliance on a major public-cloud provider and an established SI; concentration risk is real but provider viability is not a material concern. | Use of a tier-one cloud provider, portability-conscious architecture, contractual commitments and enterprise support. |

The risk profile is more favorable than a robotics- or ERP-class program: the dominant risk is implementation overrun on a large but well-understood migration, and the benefit-realization risk is specifically tied to the discipline of decommissioning legacy on schedule. Both are addressable through program governance and are reflected in the scenario modeling below.

## Scenario Modeling

The model was run under three scenarios. The base case reflects the assumptions above. The optimistic case assumes faster-than-planned legacy decommissioning (accelerating opex savings), smooth migration with minimal rework, and slightly better availability outcomes. The pessimistic case assumes migration overrun, slower legacy shutdown that delays the opex benefit, and extended parallel-running cost.

| Scenario | 3-Yr Benefit | 3-Yr TCO | NPV @ 8% | IRR | Payback |
|---|---|---|---|---|---|
| Optimistic | $22.8M | $13.6M | $6.9M | 42% | 18 mo |
| Base | $19.6M | $14.2M | $4.1M | 31% | 22 mo |
| Pessimistic | $16.1M | $16.0M | $0.4M | 11% | 31 mo |

Notably, even the pessimistic case remains marginally NPV-positive. The downside is driven principally by the twin effects of a migration overrun and slower legacy decommissioning: the former raises cost while the latter delays the opex savings and extends parallel-running expense. That the investment holds a positive (if thin) NPV under those combined stresses reflects the underlying strength of the operating-cost and availability benefits, and distinguishes this migration from higher-variance initiatives in the portfolio.

The sensitivity analysis identifies the pace of legacy decommissioning as the single most important controllable variable. It sits on both sides of the ledger: faster shutdown accelerates the opex savings and truncates costly parallel running, while slower shutdown does the reverse and is the dominant driver of the pessimistic case. This is a favorable property from a governance standpoint, because decommissioning pace is largely within Copperline's own control rather than dependent on external market or customer behavior. The program governance is therefore structured to treat decommissioning milestones as hard gates, giving the Steering Committee a direct lever over the initiative's realized return.

## Recommendation and Governance

The Enterprise IT organization recommends approval of the cloud infrastructure migration at a three-year net TCO of $14.2M, supported by an NPV of $4.1M, an IRR of 31%, and a 22-month payback at the 8% discount rate. The migration resolves an acute disaster-recovery exposure, eliminates a looming in-place hardware-refresh outlay, delivers a durable operating-cost reduction, and — most importantly for the multi-year roadmap — establishes the scalable, resilient infrastructure substrate on which every subsequent modernization initiative depends. It is recommended as the leadoff program of the FY2025 technology portfolio.

The recommendation carries one explicit condition that the sponsor endorses rather than resists: that benefit realization be measured and reported, not assumed. Because the opex savings are gated on legacy decommissioning and the availability benefit must prove out in production, the case commits to a formal post-implementation review twelve months after go-live, benchmarking actual downtime, operating-cost savings, and implementation cost against the specific figures in this document. This is not a formality; it is the mechanism by which the Committee holds the initiative accountable to the numbers on which its approval rests, and it sets the standard the sponsor expects to be held to.

Because the single-year capital ask exceeds $5M, approval requires ratification by the Board Finance & Audit Committee in addition to Steering Committee approval.

**Disposition: Approved (November 2024).** The Tech Investment Steering Committee approved the cloud infrastructure migration at its Q4 2024 session, and the Board Finance & Audit Committee ratified the single-year capital ask. Marcus Whitfield (SVP & CIO) is the accountable sponsor; Omar Delgado (Director, FP&A) owns the financial model and benefits baseline. The program is authorized to proceed with a January 2025 go-live, on the condition that a formal post-implementation review be conducted twelve months after go-live to validate outcomes against the projections in this case. Elena Popescu (Director, Enterprise PMO) will facilitate program governance and record the approval in the committee minutes.
