# Business Case: Warehouse Management System Replacement and Robotics Pilot

## Executive Summary

Copperline Retail Group operates four regional distribution centers — Charlotte, NC; Reno, NV; Columbus, OH; and Allentown, PA — that together fulfill store replenishment for 214 stores across 31 states and a growing direct-to-consumer channel that now represents roughly 18% of the company's $1.92B in FY2025 net revenue. The distribution network runs on "Trailhead WMS," an on-premise warehouse management platform first deployed in 2011 and last materially upgraded in 2017. Trailhead has reached the end of its useful life. It cannot support wave-less order release, real-time inventory positioning, or the labor-planning granularity that modern omnichannel fulfillment demands, and its vendor has signaled that mainstream support ends in 2028.

This business case, sponsored by Devon Marsh (VP, Supply Chain & Logistics), proposes a two-part investment: (1) replacement of Trailhead WMS with Kinetic Flow WMS, a cloud-native warehouse management platform from Kinetic Flow Technologies, deployed across all four distribution centers; and (2) a co-located autonomous mobile robot (AMR) goods-to-person pilot at the Reno, NV distribution center in partnership with Orbis Robotics. The pilot is scoped deliberately narrowly — a single facility, a bounded pick zone — so that Copperline can validate throughput, labor, and accuracy economics before committing to a network-wide robotics rollout.

The three-year total cost of ownership is estimated at $12.8M. Projected three-year benefits total $17.3M, driven principally by pick-labor productivity, accuracy-driven reduction in returns and re-picks, and reclaimed throughput capacity at Reno. At Copperline's standard 8% discount rate, the investment produces a net present value of $3.2M, an internal rate of return of 22%, and a payback period of 25 months.

The proposal is best understood as two investments of very different character bundled into a single case. The WMS replacement is a near-mandatory modernization: Trailhead is running out of vendor runway and is already constraining the network's ability to serve the order profile the business is generating. The robotics pilot is a discretionary, higher-variance bet on the future shape of Copperline's fulfillment labor model. Combining them in one case reflects operational reality — the AMR pilot at Reno depends on the new WMS as its control layer and cannot be delivered on Trailhead — but the governance framing throughout this document keeps the two components distinguishable so that the Committee can weigh the confident modernization against the exploratory pilot on their own merits.

The financial model for this case was prepared by Omar Delgado (Director, FP&A). The case was presented to the Tech Investment Steering Committee at its Q3 2026 quarterly session on September 15, 2026. Because the aggregate FY2027 capital envelope was oversubscribed and the robotics benefit case carries execution uncertainty that the Committee wished to see de-risked, the initiative was **deferred to FY2027 Q2** pending confirmation of FY2027 capital availability and refinement of the Reno pilot's benefit-realization assumptions. This document is the case as submitted, annotated with the Committee's disposition.

## Problem and Strategic Context

### An aging WMS at the center of fulfillment

Trailhead WMS was architected for an era when Copperline's distribution centers served stores and little else. The platform's order model assumes batch-oriented, wave-based release tuned to store-replenishment cadences: pallets and full cases moving to 214 predictable destinations on fixed schedules. That model has aged badly against the reality of the business. E-commerce order density at the distribution centers has grown at a compound annual rate above 20% since FY2021, and the mix has shifted decisively toward small-line, high-frequency each-picking. A typical direct-to-consumer order at Copperline is now 2.3 lines and 3.1 units — a profile Trailhead was never designed to handle efficiently.

The operational symptoms are concrete. At the Reno DC, which serves the fastest-growing e-commerce demand in the western region, pickers walk an estimated 8 to 11 miles per shift under Trailhead's static slotting and paper-assisted pick paths. Pick density during peak (October through December) routinely exceeds the platform's practical wave-planning ceiling, forcing supervisors into manual wave splitting and ad hoc labor reallocation. Trailhead offers no real-time labor standards, no dynamic slotting, and no meaningful exception-management workflow; inventory accuracy is maintained through periodic cycle counts rather than continuous reconciliation.

### Labor cost pressure

Warehouse labor is Copperline's largest controllable distribution cost and its most volatile. Fully loaded hourly labor rates across the four DCs have risen approximately 19% cumulatively over the past three years, and the Reno and Allentown markets in particular have experienced persistent seasonal staffing shortfalls, with peak-season agency premiums running 35% to 50% above base. Because Trailhead cannot optimize pick paths or balance work dynamically, Copperline absorbs this rising rate against a productivity baseline that has been essentially flat. Every point of labor productivity the company fails to capture compounds directly against the fastest-inflating line in the distribution P&L.

### E-commerce order-density growth and the capacity ceiling

The strategic context is not merely cost — it is capacity. The Reno DC is approaching its effective throughput ceiling under the current WMS and manual pick-pack process. Internal industrial-engineering estimates put Reno's sustainable peak-day unit throughput at roughly 92% of the volume forecast for the FY2027 holiday peak, meaning that without intervention Copperline will be routing western-region overflow to Columbus at materially higher outbound freight cost, or degrading service levels. The company's Unified Commerce initiative (the Omnichannel POS program that went live in August 2025) has made ship-from-DC and buy-online-pickup-in-store commitments that assume a fulfillment network able to scale with demand. A WMS that caps out at peak undermines those commitments.

### Network context and the case for Reno as the pilot site

Reno is the right site for the robotics pilot for reasons that go beyond its being the most constrained. Of the four distribution centers, Reno has the highest e-commerce mix in its outbound volume, the most acute peak-season labor scarcity, and the pick-zone geometry best suited to a bounded goods-to-person deployment. Charlotte, the largest and most complex facility, carries too much store-replenishment and cross-dock activity to make a clean pilot; Columbus and Allentown are healthier on capacity and less pressured on labor. Reno concentrates the exact conditions — high each-pick density, expensive and scarce labor, a throughput ceiling in sight — under which AMR goods-to-person economics are most likely to prove out. A pilot that succeeds at Reno is a pilot that has been tested against Copperline's hardest fulfillment problem, which makes any subsequent network rollout decision far better informed.

### Why now, and why a pilot

Trailhead's support horizon (mainstream support ending 2028), the throughput ceiling at Reno, and the labor-rate trajectory together create a clear window for action. Deferring the WMS replacement much beyond FY2027 would compress the migration timeline dangerously against the 2028 support cliff and would force Copperline to run its fastest-growing channel on a platform its own operators no longer trust at peak. The robotics component, by contrast, is deliberately structured as a pilot rather than a network commitment. AMR goods-to-person economics are attractive in theory but sensitive in practice to slotting discipline, order profile, and change-management execution. By confining robotics to Reno's e-commerce pick zone, Copperline can measure real throughput and labor outcomes against this business case before extending the model to Columbus, Charlotte, or Allentown — and can walk away from the robotics thesis, at limited cost, if the pilot fails to validate, while still retaining the full value of the WMS modernization.

## Financial Modeling

The three-year total cost of ownership reflects WMS subscription and implementation across all four distribution centers plus the Reno robotics pilot (AMR fleet lease, integration, and facility modification). All figures are in USD millions and use Copperline's standard 8% discount rate for NPV.

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Yr Total |
|---|---|---|---|---|
| Kinetic Flow WMS subscription (4 DCs) | 1.80 | 1.85 | 1.90 | 5.55 |
| WMS implementation & integration (SI) | 2.40 | 0.40 | 0.20 | 3.00 |
| Orbis AMR pilot — fleet lease (Reno) | 0.95 | 0.98 | 1.00 | 2.93 |
| Robotics integration & facility mods (Reno) | 0.70 | 0.10 | 0.05 | 0.85 |
| Internal program & change management | 0.22 | 0.13 | 0.12 | 0.47 |
| **Total Cost of Ownership** | **6.07** | **3.46** | **3.27** | **12.80** |

Implementation is front-loaded, as expected for a systems integration and physical robotics deployment: Year 1 carries the WMS cutover across four sites plus the one-time Reno facility modifications and AMR commissioning. Subscription and lease costs settle into a stable run-rate in Years 2 and 3. The WMS subscription is priced on a per-site, throughput-tiered basis and steps up modestly year over year with contracted escalators; the Orbis AMR fleet is leased rather than purchased, a deliberate choice that keeps the robotics commitment operating-lease in character and limits stranded-asset exposure should the pilot not be extended. The internal program and change-management line funds a dedicated Copperline delivery team, the super-user program at each DC, and the floor-leadership engagement at Reno that the benefit case depends on.

The model excludes any benefit from network-wide robotics expansion beyond the Reno pilot; the TCO likewise excludes any expansion capital. This keeps the case honest to what is actually being proposed — a four-site WMS replacement plus a single-site robotics pilot — and avoids crediting speculative future rollout economics that the pilot is specifically designed to test. The benefit stream builds as the WMS rolls out (Charlotte first, then Columbus, Allentown, and Reno) and as the Reno robotics pilot ramps past its stabilization period. Discounted at 8%, the cumulative benefit against cost yields an NPV of $3.2M, an IRR of 22%, and a 25-month payback measured from program start.

## Benefits Analysis

Benefits fall into three quantified categories — labor productivity, accuracy-driven cost avoidance, and reclaimed throughput capacity — plus qualitative benefits in resilience and analytics that the model does not monetize. The table below states the operational metric, the Trailhead baseline, and the target end-state at full deployment.

| Benefit Driver | Baseline (Trailhead) | Target (Kinetic Flow + Orbis) | Basis of Value |
|---|---|---|---|
| Pick accuracy | 98.4% order accuracy | 99.6% order accuracy | Fewer re-picks, mis-ships, returns |
| Labor cost per order (DTC) | $4.85 | $3.55 | ~27% reduction via path optimization + goods-to-person at Reno |
| Peak throughput capacity (Reno) | ~1.00x current ceiling | ~1.45x current ceiling | Deferred overflow-freight & service protection |
| Picker travel (Reno pilot zone) | 8–11 mi/shift | 2–3 mi/shift | Goods-to-person eliminates most travel |
| Inventory accuracy | ~97.2% (cycle-count) | ~99.3% (continuous) | Reduced shrink, fewer stockout events |
| Peak agency-labor premium | 35–50% over base | 15–25% over base | Higher throughput per FTE reduces peak headcount |

The single largest monetized driver is labor cost per order. Path optimization and dynamic slotting under Kinetic Flow account for the majority of the network-wide labor benefit; the goods-to-person robotics layer at Reno delivers a step-change on top of that within the pilot zone, which is where the most acute travel penalty exists today. Accuracy improvement is the second driver: at Copperline's DTC volumes, moving order accuracy from 98.4% to 99.6% materially reduces the returns-processing, re-pick, and customer-service cost associated with mis-shipped orders. The third driver — reclaimed peak capacity at Reno — is valued conservatively as avoided overflow freight and protected service levels rather than as incremental revenue, since the company does not want to credit demand it would have served regardless.

Benefits are phased. The WMS-driven productivity and accuracy gains begin accruing as each DC cuts over, so the network captures most of the WMS benefit by the end of Year 1. The robotics benefit ramps more slowly: the model assumes a stabilization period at Reno before the pilot reaches target throughput, with the pilot contributing meaningfully only from the second half of Year 1 onward.

Beyond the monetized drivers, the case carries qualitative benefits the model does not attempt to price. Continuous inventory reconciliation under Kinetic Flow replaces Trailhead's periodic cycle-count regime, giving merchandising and digital-commerce far more reliable real-time availability data — a direct enabler of the ship-from-DC and buy-online-pickup-in-store commitments made under the Unified Commerce program. Modern labor-management analytics give DC leadership visibility into productivity and staffing that Trailhead simply cannot produce, improving peak planning across all four sites. And the robotics pilot, whatever its financial outcome, generates operational learning about goods-to-person deployment — slotting, associate workflow, integration — that materially de-risks any future network decision. These benefits are real and strategically significant; they are excluded from the financial model out of conservatism, not because they lack value.

## Risk Assessment

The following assessment uses Copperline's five standard business-case risk categories. Each risk is rated for likelihood and impact and paired with the primary mitigation.

| Risk Category | Rating | Description | Primary Mitigation |
|---|---|---|---|
| Implementation overrun | High | Concurrent four-site WMS cutover plus first-time robotics commissioning at Reno; go-live during any peak window would be catastrophic. | Phased rollout (Charlotte pilot site first), mandatory peak blackout on cutovers, fixed-fee SI statement of work with milestone holdbacks. |
| Benefit-realization shortfall | High | Labor-per-order and throughput targets depend on slotting discipline and change adoption; robotics ROI is the least certain component. | Confine robotics to a single Reno zone, tie AMR lease to staged expansion gates, monthly benefits tracking against Delgado's model. |
| Data-quality degradation | Medium | Item master, slotting, and inventory data migrating from a 2011-era platform is likely to carry latent errors that degrade WMS optimization. | Pre-migration data-cleansing sprint, parallel-run reconciliation, cycle-count intensification pre-cutover. |
| Adoption failure | Medium | Goods-to-person and directed-work change floor-associate behavior significantly; supervisor and associate resistance is a real threat to the benefit case. | Dedicated change-management workstream, super-user program, phased incentive alignment, Reno floor-leadership engagement from design phase. |
| Vendor viability | Medium | Kinetic Flow Technologies is an established WMS vendor, but Orbis Robotics is a younger AMR provider; multi-vendor coordination adds fragility. | Financial-health diligence on both vendors, AMR lease (not purchase) to limit stranded-asset exposure, contractual source-code/data escrow for WMS, single accountable SI as integration owner. |

The concentration of "High" ratings in implementation overrun and benefit-realization shortfall is the honest center of gravity for this case, and it is precisely what motivated the Committee's request to de-risk before funding.

## Scenario Modeling

To bound the range of outcomes, the model was run under three scenarios. The base case reflects the assumptions above. The optimistic case assumes faster robotics stabilization, full slotting discipline, and labor rates continuing to inflate at the recent trend (which increases the value of every productivity point). The pessimistic case assumes a delayed robotics ramp, partial adoption, and a data-migration remediation overrun.

| Scenario | 3-Yr Benefit | 3-Yr TCO | NPV @ 8% | IRR | Payback |
|---|---|---|---|---|---|
| Optimistic | $21.4M | $12.5M | $6.1M | 34% | 19 mo |
| Base | $17.3M | $12.8M | $3.2M | 22% | 25 mo |
| Pessimistic | $12.6M | $14.1M | ($0.6M) | 5% | 41 mo |

The pessimistic case is the material one for governance: under a delayed robotics ramp combined with a data-migration overrun, the investment turns marginally NPV-negative. This asymmetry — a solid base case with a genuinely negative downside — is the reason the robotics pilot is structured with staged expansion gates rather than an upfront network commitment, and it reinforces the case for validating Reno before extending robotics elsewhere.

It is worth noting where the downside sensitivity actually concentrates. A stress on the WMS component alone — slower rollout, partial adoption — moves the outcome but does not on its own push the case negative, because the WMS labor and accuracy benefits are broad-based across four sites and relatively robust. The path to a negative NPV runs almost entirely through the robotics pilot: a delayed or failed Reno ramp removes the highest-value marginal benefit while its lease and integration costs are largely already committed. This decomposition is the analytical basis for the recommendation's structure — fund the confident, broad-based WMS modernization, and gate the narrow, higher-variance robotics pilot so its downside is bounded and its upside is measured before any further capital follows.

## Recommendation and Governance

The Supply Chain & Logistics organization recommends approval of the Kinetic Flow WMS replacement across all four distribution centers together with the Orbis Robotics goods-to-person pilot at the Reno DC, at a three-year TCO of $12.8M, supported by an NPV of $3.2M, IRR of 22%, and a 25-month payback at the 8% discount rate. The WMS replacement is, on its own, a near-mandatory modernization given Trailhead's support horizon and Reno's throughput ceiling; the robotics pilot is the discretionary, higher-variance component and is deliberately bounded so that its downside is contained and its upside is measurable.

Because the combined single-year FY2027 capital ask exceeds $5M, the initiative would, if approved, require ratification by the Board Finance & Audit Committee in addition to Steering Committee approval.

**Disposition: Deferred (Q3 2026 Steering Committee, September 15, 2026).** The Tech Investment Steering Committee, co-chaired by Renata Alvarez (EVP & CFO) and Marcus Whitfield (SVP & CIO), reviewed the case against a materially oversubscribed FY2027 capital envelope. The Committee did not dispute the strategic necessity of the WMS replacement, but declined to fund the combined program in the current cycle for two reasons: first, FY2027 capital availability will not be confirmed until the CFO's portfolio prioritization is finalized; and second, the Committee asked the sponsor to return with a tightened robotics benefit-realization case for Reno, including firmer stabilization-period assumptions and staged expansion gates. The initiative is deferred to the **FY2027 Q2** cycle. Devon Marsh remains sponsor; Omar Delgado will refresh the financial model with updated labor-rate and robotics-ramp inputs ahead of resubmission. Elena Popescu (Director, Enterprise PMO) recorded the disposition in the Q3 2026 committee minutes.
