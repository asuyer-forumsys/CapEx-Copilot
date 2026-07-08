# WMS and Robotics Finalists Vendor Scorecard

## RFP Context and Process

This scorecard documents the evaluation of finalist vendors for Copperline Retail Group's warehouse management system replacement and distribution-center robotics pilot, conducted in support of the business case sponsored by Devon Marsh (VP, Supply Chain & Logistics). The procurement replaces the end-of-life "Trailhead WMS" platform across all four distribution centers (Charlotte, NC; Reno, NV; Columbus, OH; Allentown, PA) and selects a robotics partner for a bounded autonomous mobile robot (AMR) goods-to-person pilot at the Reno DC.

The formal RFP was issued in April 2026 to seven qualified vendors identified through market scan and analyst input. Four responses advanced past the initial completeness and mandatory-requirements screen. Following scripted demonstrations, reference calls, a total-cost workshop, and a Reno site walk for the robotics-capable respondents, the evaluation committee narrowed the field to three finalists:

- **Kinetic Flow WMS** (Kinetic Flow Technologies), paired with **Orbis Robotics** for the AMR goods-to-person pilot at Reno.
- **Atlas WMS** — a strong, mature WMS with no robotics roadmap of its own.
- **Palletworks WMS + Robotics** — a single-vendor bundle offering WMS and robotics from one provider.

The evaluation committee was chaired by Supply Chain & Logistics and included representatives from Enterprise IT, FP&A (Omar Delgado, as financial-model owner), Information Security (delegated from Farrukh Rahimi's organization), and DC operations leadership from Reno and Charlotte. The scoring was completed in June 2026, ahead of the business case's presentation to the Tech Investment Steering Committee at the Q3 2026 session.

The evaluation was structured to test each finalist against Copperline's actual operating conditions rather than against a generic feature checklist. Scripted demonstrations used Copperline's own order profiles — small-line, high-frequency each-picking representative of the direct-to-consumer volume that is growing fastest at the Reno DC — so that functional scores reflected fit to the problem the investment is meant to solve. Reference calls were weighted toward retailers of comparable scale and channel mix, and the total-cost workshop normalized each vendor's pricing to a common three-year, four-site basis to make the TCO scores directly comparable. For the two robotics-capable respondents, a Reno site walk grounded the throughput and layout assumptions in the physical reality of the pilot facility. The intent throughout was to keep the scorecard defensible under the scrutiny of a business case that would ultimately go before the Steering Committee and, given its size, the Board Finance & Audit Committee.

## Evaluation Criteria and Weighting

The committee scored each finalist against seven weighted criteria on a 1–5 scale, where 5 represents best-in-class fit to Copperline's requirements. Weights were set by the committee before demonstrations to prevent anchoring. The weighting deliberately privileges functional fit and total cost — the two dimensions most tied to the business case's benefit realization — while giving meaningful weight to the robotics roadmap because the pilot's expandability is central to the long-term thesis.

| Criterion | Weight |
|---|---|
| Functional fit (each-pick, slotting, labor mgmt, omnichannel) | 22% |
| Robotics capability & goods-to-person maturity | 18% |
| Total cost of ownership (3-yr) | 18% |
| Implementation risk & SI ecosystem | 14% |
| Integration & platform openness (APIs, ERP/POS) | 12% |
| Configurability & extensibility | 10% |
| Vendor viability & financial health | 6% |

## Scorecard

Raw scores are on the 1–5 scale; the weighted total is the sum of each raw score multiplied by its criterion weight, expressed on the same 5-point scale.

| Criterion (weight) | Kinetic Flow + Orbis | Atlas WMS | Palletworks WMS+Robotics |
|---|---|---|---|
| Functional fit (22%) | 5 | 5 | 3 |
| Robotics capability (18%) | 5 | 1 | 3 |
| 3-yr TCO (18%) | 4 | 4 | 4 |
| Implementation risk & SI (14%) | 3 | 4 | 4 |
| Integration & openness (12%) | 4 | 4 | 3 |
| Configurability (10%) | 5 | 4 | 2 |
| Vendor viability (6%) | 3 | 5 | 4 |
| **Weighted total (of 5.0)** | **4.30** | **3.76** | **3.24** |

## Narrative Rationale by Finalist

### Kinetic Flow WMS + Orbis Robotics — recommended

Kinetic Flow posted the strongest functional demonstration of the three, handling Copperline's small-line, high-frequency DTC order profile natively and showing mature dynamic slotting, real-time labor standards, and exception-management workflows — exactly the capabilities Trailhead lacks. Its scripted each-pick and wave-less release demonstration mapped cleanly to the Reno operating problem. On configurability it was the clear leader: the platform's rules engine let Copperline model its own pick-path and slotting logic without custom code, which matters for a four-site rollout with differing facility layouts.

The Orbis Robotics pairing is the differentiator. Orbis brings a proven AMR goods-to-person solution that integrates with Kinetic Flow through a supported interface, and its solution engineering during the Reno site walk was credible and specific about throughput assumptions and floor layout. Combining a best-of-breed WMS with a best-of-breed robotics partner gives Copperline a genuine goods-to-person capability at Reno with a roadmap to extend to other DCs if the pilot validates.

The committee did not score Kinetic Flow + Orbis highest on every axis, and the scorecard reflects that honestly. Implementation risk scored lowest of the three finalists (3): a multi-vendor arrangement — WMS from Kinetic Flow, robotics from Orbis, integrated by a systems integrator — carries more coordination fragility than a single-vendor bundle, and the concurrent four-site cutover plus first-time robotics commissioning is genuinely demanding. Vendor viability also scored a 3, driven not by Kinetic Flow (an established WMS provider) but by Orbis Robotics, which is a younger company; the committee's mitigation is to lease rather than purchase the AMR fleet and to gate expansion. Even carrying these two soft scores, the combination's functional and robotics strength produced the top weighted total at 4.30.

### Atlas WMS — runner-up

Atlas WMS was the closest competitor and, on the pure WMS dimension, an excellent product. It matched Kinetic Flow on functional fit (5) and scored highest of all finalists on vendor viability (5) and among the best on implementation risk (4), reflecting a large, mature systems-integrator ecosystem and a long track record of stable multi-site deployments. For a WMS-only procurement, Atlas would have been a defensible selection.

The decisive gap is robotics. Atlas offers no robotics roadmap of its own and scored a 1 on the robotics-capability criterion. Under Copperline's weighting — where robotics carries 18% because the pilot's expandability is core to the long-term supply-chain thesis — that single weakness is what separates Atlas from the recommended combination. Selecting Atlas would have required standing up a separate robotics procurement and integration entirely outside the WMS vendor relationship, adding exactly the coordination complexity that a bundled or well-paired approach avoids, while forgoing a demonstrated goods-to-person path. Atlas remains the committee's recommended fallback should the Kinetic Flow + Orbis arrangement fail contracting or diligence.

### Palletworks WMS + Robotics — not recommended

Palletworks was the only true single-vendor bundle, providing both WMS and robotics from one provider. That structure is its principal appeal: it scored well on implementation risk (4) and integration-of-the-two-components is inherently simpler when one vendor owns both, reducing the multi-party coordination burden that weighs on the Kinetic Flow + Orbis approach. On paper, lower coordination risk is a real advantage for a first robotics deployment.

The bundle's weaknesses, however, are where the business case is most sensitive. Palletworks scored lowest on functional fit (3) and configurability (2): its WMS is competent for case- and pallet-oriented distribution but noticeably weaker on the small-line each-pick and dynamic-slotting workflows that dominate Copperline's DTC growth, and its rules engine is more rigid, implying custom development to model Copperline's pick logic. Its robotics offering scored a middling 3 — functional, but less mature in goods-to-person throughput than Orbis. The committee concluded that the lower coordination risk did not compensate for weaker configurability and a poorer fit to the exact order profile driving the investment. Palletworks produced the lowest weighted total at 3.24.

## Recommendation

The evaluation committee recommends **Kinetic Flow WMS (Kinetic Flow Technologies) paired with Orbis Robotics** for the goods-to-person AMR pilot at the Reno, NV distribution center. The combination scored highest on the weighted criteria (4.30 of 5.0), led decisively on functional fit, configurability, and robotics capability, and offers the clearest path from a bounded Reno pilot to a network-wide capability if the pilot validates.

The recommendation is made with explicit acknowledgment of its two soft spots — multi-vendor implementation coordination and Orbis's relative youth as a vendor — and pairs them with concrete mitigations already reflected in the business case: a phased, peak-blackout cutover with a single accountable systems integrator as integration owner; an AMR lease structure rather than purchase to limit stranded-asset exposure; staged expansion gates tied to measured pilot outcomes; and financial-health diligence on both vendors before contract execution. Atlas WMS is designated the fallback selection in the event contracting or diligence on the recommended combination does not close.

The committee also considered, and rejected, a hybrid path of selecting Atlas for the WMS and Orbis separately for robotics. While this would have paired the highest-viability WMS with the strongest robotics partner, it would have created two independent vendor relationships and an integration seam between a WMS and a robotics platform that were never designed or tested together — reintroducing the coordination risk that weighs against the recommended approach, without the benefit of Kinetic Flow and Orbis's existing supported interface and joint solution engineering. The committee judged that a validated Kinetic Flow–Orbis integration was materially lower-risk than a bespoke Atlas–Orbis pairing assembled for the first time on Copperline's pilot. Contracting is expected to proceed on the recommended combination subject to Steering Committee funding, with the fallback held in reserve.
