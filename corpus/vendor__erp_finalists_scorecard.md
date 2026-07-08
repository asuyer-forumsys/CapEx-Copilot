# ERP Finalists Evaluation Scorecard

## RFP Context and Purpose

This scorecard documents the competitive evaluation conducted in support of the ERP Replacement business case, which proposes retiring Copperline Retail Group's seventeen-year-old on-premise "Summit" ERP in favor of a cloud-native platform. The Enterprise PMO issued a formal Request for Proposal to five ERP vendors in the summer of 2024, covering financials, procurement, inventory and order management, and the integration architecture required to connect the ERP to Copperline's point-of-sale, warehouse-management, e-commerce, and enterprise-data landscape across 214 stores and four distribution centers.

Three vendors advanced to the finalist round following an initial screen on functional coverage, retail-vertical experience, and cloud delivery model: Ledgerline Cloud ERP (Ledgerline Systems), Vantage Suite ERP (Vantage Software), and Corvus ERP Cloud (Corvus Technologies). Two of the original five respondents were eliminated in the screening round — one for lacking a genuine multi-tenant SaaS offering and instead proposing a hosted single-tenant deployment that reproduced much of the operational burden Copperline is trying to shed, and the other for thin references in specialty retail at Copperline's scale.

Each finalist completed a structured functional demonstration against Copperline-supplied scenarios — a representative month-end close, a multi-node inventory replenishment cycle, a store-to-DC transfer, and a procurement-to-pay flow — submitted a detailed cost proposal and implementation plan, and participated in reference calls and a formal vendor-viability review. The demonstrations were scripted deliberately so that the committee scored the same scenarios across all three vendors rather than letting each vendor present its own strengths, and the cost proposals were normalized to a common three-year total-cost-of-ownership basis so that subscription, implementation, and run-cost differences were compared on equal terms. This document records the weighted evaluation of those three finalists and the resulting recommendation, which feeds directly into the ERP Replacement business case and its subsequent change-request addendum.

## Evaluation Criteria and Weighting

The evaluation committee — drawn from FP&A, the Enterprise PMO, IT, and the supply-chain and digital-commerce organizations — scored each finalist against five weighted criteria. Weights were set before proposals were opened, in accordance with the Business Case Review and Template Guide, to prevent post-hoc adjustment. Each criterion was scored on a 1-to-10 scale, where 10 represents a clear best-in-class result.

| Criterion | Weight | Rationale for Weighting |
|---|---|---|
| Cost (total cost of ownership) | 25% | Capital discipline is a governance priority for a PE-recapitalized business; TCO drives the NPV case. |
| Functionality & fit | 25% | The platform must cover finance, procurement, and real-time inventory for a multi-node retailer out of the box, with minimal customization. |
| Implementation risk | 20% | Copperline's integration surface is large; delivery risk is the dominant driver of program-cost variance. |
| Vendor viability | 15% | The chosen SaaS provider becomes a multi-year operational dependency; financial and organizational durability matters. |
| Integration architecture | 15% | The new ERP must connect cleanly to POS, WMS, e-commerce, and the enterprise data spine without recreating Summit's brittle interface web. |

Cost and functionality were weighted equally and highest, reflecting the twin governance priorities of capital discipline and genuine capability. Implementation risk was weighted third at 20%, a deliberate signal that the committee viewed delivery risk — not license price — as the largest threat to the business case, given Summit's tangle of undocumented custom interfaces. Vendor viability and integration architecture rounded out the model at 15% each.

The committee also agreed two scoring conventions before opening proposals, to keep the exercise disciplined. First, any criterion scored below 4 for a given vendor would be treated as a potential disqualifier requiring explicit committee discussion rather than being silently averaged away — a guard against a strong overall score masking a fatal weakness in one dimension. Second, the vendor-viability score would be anchored to an independent review of each vendor's audited financials, customer concentration, and cash runway, rather than to the vendor's own representations. Both conventions proved decisive in the Corvus evaluation.

## Scorecard

The table below presents each finalist's raw score per criterion, the weight applied, and the resulting weighted total. Weighted totals are the sum of each raw score multiplied by its criterion weight.

| Criterion | Weight | Ledgerline Cloud ERP | Vantage Suite ERP | Corvus ERP Cloud |
|---|---|---|---|---|
| Cost | 25% | 7 | 6 | 9 |
| Functionality & fit | 25% | 9 | 8 | 7 |
| Implementation risk | 20% | 8 | 7 | 4 |
| Vendor viability | 15% | 9 | 9 | 3 |
| Integration architecture | 15% | 9 | 8 | 6 |
| **Weighted total** | **100%** | **8.30** | **7.45** | **6.15** |

Ledgerline Cloud ERP leads the field with a weighted score of 8.30, ahead of Vantage Suite ERP at 7.45 and Corvus ERP Cloud at 6.15. The ranking is notable because Corvus submitted the lowest-cost proposal by a clear margin and earned the top cost score of 9 — yet finished last overall, because its advantage on price was more than offset by low scores on implementation risk and, decisively, vendor viability. This is precisely the outcome the weighting was designed to surface: a cheap bid that imports unacceptable delivery and continuity risk is not a bargain for a business betting its financial backbone on the result.

## Finalist Rationale

### Ledgerline Cloud ERP (Ledgerline Systems) — Recommended

Ledgerline emerged as the strongest all-round finalist. In the functional demonstrations it covered Copperline's finance, procurement, and multi-node inventory scenarios with the least custom configuration, and its real-time general-ledger posting and network-wide inventory model map directly onto the two capabilities the business case depends on most: a compressed close cycle and a trustworthy live inventory position. It scored a 9 on functionality and fit, the highest in the field.

Ledgerline's integration architecture was also the committee's favorite, earning a 9. The platform exposes a well-documented, standards-based API layer and a managed integration framework that lets Copperline retire Summit's hand-built point-to-point interfaces in favor of a consolidated, observable integration tier — a direct mitigation of the interface-fragility risk that drove the replacement in the first place. On vendor viability, Ledgerline scored a 9: the reference checks were strong, the company is well-capitalized with a healthy retail-sector installed base, and the master agreement includes source-code escrow, data-portability, and service-level protections.

Ledgerline's only relative weakness is price. At a cost score of 7 it is not the cheapest option — it came in above Corvus and modestly above Vantage — and its subscription pricing carries contracted annual uplift. The committee judged this a fair premium for the lowest-risk path to the capabilities in the business case, and the program's positive NPV absorbs the cost comfortably. Ledgerline is the recommended selection.

### Vantage Suite ERP (Vantage Software) — Runner-Up

Vantage was a credible and close runner-up, finishing second on every criterion except vendor viability, where it tied Ledgerline at 9. Vantage Software is a large, established ERP vendor with a durable balance sheet and a deep partner ecosystem, and the committee had no continuity concerns about it. Its functional coverage was strong, scoring an 8, though its inventory and order-management demonstrations required somewhat more configuration than Ledgerline's to meet Copperline's multi-node scenarios.

Vantage scored a 7 on implementation risk and an 8 on integration architecture — solid, but a step behind Ledgerline. Its integration tooling is capable but more reliant on a specialized middleware layer and a narrower pool of certified implementation partners, which the committee viewed as marginally increasing both delivery risk and long-run run-cost. On price, Vantage's proposal was competitive but slightly higher on a normalized TCO basis than the committee expected, earning a cost score of 6. Vantage would be a defensible choice, but on the weighted model it trails Ledgerline by nearly a full point, driven by Ledgerline's edges in functional fit, integration architecture, and implementation risk.

### Corvus ERP Cloud (Corvus Technologies) — Not Recommended

Corvus submitted the most aggressive price in the field and earned the top cost score of 9. For a cost-conscious, PE-owned business, that price was genuinely attractive, and the committee gave it a full and serious review rather than dismissing it on size alone. Corvus's functional demonstration was respectable, scoring a 7, with reasonable coverage of core finance and inventory needs.

The case against Corvus rests on two criteria. First, implementation risk: Corvus scored a 4. Its reference base for retailers at Copperline's scale and integration complexity is thin, its implementation methodology relies heavily on a small internal delivery team rather than a broad certified-partner network, and the committee had low confidence that Corvus could absorb the surprises inherent in migrating off a seventeen-year-old, heavily customized legacy platform. Second, and decisively, vendor viability: Corvus scored a 3. Corvus Technologies is a small vendor with a thin balance sheet, limited cash runway relative to the multi-year commitment Copperline would be making, and meaningful concentration in its customer base. Betting the company's financial and inventory backbone on a provider whose own continuity is uncertain was a risk the committee was unwilling to take at any price. Its integration architecture scored a 6 — functional but less mature than either competitor's.

The committee's conclusion was explicit: Corvus's cost advantage is real but does not compensate for the elevated implementation and vendor-viability risk it carries. A materially cheaper platform that could destabilize the close, the inventory record, or the company's ability to report to its owners is not a saving. Under the pre-agreed scoring conventions, Corvus's vendor-viability score of 3 triggered the committee's disqualifier review, and after examining Corvus Technologies' most recent financials — a thin balance sheet, limited cash runway against a multi-year SaaS commitment, and a customer base concentrated enough that the loss of a few large accounts could threaten the firm — the committee concluded the continuity risk was not one Copperline should accept for its transactional core at any price point. Corvus is not recommended.

## Recommendation

The evaluation committee recommends the selection of **Ledgerline Cloud ERP (Ledgerline Systems)** as Copperline Retail Group's replacement ERP platform. Ledgerline earned the highest weighted score at 8.30, led the field on functionality and fit, integration architecture, and vendor viability, and offers the lowest-risk path to the capabilities on which the ERP Replacement business case depends. Vantage Suite ERP is recorded as the qualified runner-up should contract negotiations with Ledgerline fail to reach acceptable terms. Corvus ERP Cloud, despite the most attractive price, is not recommended owing to elevated implementation risk and significant vendor-viability concerns. This recommendation is carried forward into the ERP Replacement business case and its financial model.
