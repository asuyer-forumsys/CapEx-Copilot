# ERP Replacement Change Request Addendum: Revised Scope, Budget, and Timeline

## Purpose of This Addendum

This addendum formally amends the ERP Replacement business case — "ERP Replacement Business Case: Legacy 'Summit' to Ledgerline Cloud ERP," authored by the Enterprise PMO in October 2024, approved by the Tech Investment Steering Committee in December 2024, and ratified by the Board Finance & Audit Committee as a capital ask exceeding the $5M board threshold. It is issued at the direction of the Q3 2026 Steering Committee, whose September 15, 2026 minutes recorded confirmation of material scope creep in the ERP integration workstream and instructed the Enterprise PMO to prepare a formal change request quantifying the cost, timeline, and financial-model impact.

The purpose of this document is to establish the current, authoritative scope, budget, timeline, and financial metrics for the ERP Replacement program, superseding the corresponding figures in the original October 2024 case. The revised program carries a three-year total cost of ownership of $27.8M, a go-live target of Q2 2027, a net present value of $2.1M at the company's standard 8% discount rate, an internal rate of return of 12%, and a payback period of 34 months. Because the revised ask remains well above the $5M board threshold, this addendum requires supplemental ratification by the Board Finance & Audit Committee.

The program remains sponsored by Renata Alvarez, EVP & CFO, with the revised financial model prepared by Omar Delgado, Director of FP&A. This addendum is authored by Elena Popescu, Director of the Enterprise PMO, who owns the Business Case Review Policy under which the change is governed.

## Root Cause of Scope Change

The change originates in a single, well-defined discovery made during program execution: the true integration surface between the legacy Summit ERP and Copperline's surrounding systems is more than twice as large as the original case assumed.

The original business case was scoped, costed, and planned on the basis of six custom integrations between Summit and the surrounding application landscape — the interfaces to point-of-sale, warehouse management, e-commerce, payroll, tax, and vendor EDI that the IT organization could positively identify and document at the time. The implementation and integration budget, the data-migration plan, the timeline, and the contingency reserve were all sized against that count of six.

During the integration-mapping workstream conducted in the first half of 2026 — a systematic trace of every inbound and outbound data flow touching the Summit environment, undertaken as the team prepared to build the consolidated Ledgerline integration tier — the implementation team discovered fourteen custom integrations to Summit, not six. Eight of the fourteen were undocumented: interfaces built over the platform's seventeen-year life by staff who have since left the company, running quietly in production with no runbook, no owning team, and in several cases no record in the IT asset inventory. Among them were a nightly feed to a regional tax-jurisdiction service, a bespoke bank-reconciliation bridge, a store-level cash-management interface, and a hand-built connector to a third-party freight-audit system — each of them load-bearing for a live business process, and each of them absent from the original scope.

The mapping exercise itself illustrates why the interfaces stayed hidden for so long. The team reconstructed the integration landscape not from documentation — which was incomplete — but from the ground up: by instrumenting the Summit environment and tracing every scheduled job, database trigger, file drop, and network connection that moved data in or out over a full monthly cycle, then reconciling each observed flow against a system of record. Several of the eight undocumented interfaces surfaced only because a downstream system received a file that no one in IT could account for, prompting a backward trace to a batch job buried in a scheduler with a cryptic name and no owner. The freight-audit connector, for instance, was discovered because a weekly outbound file to a third-party auditor had simply always been there; the person who built it left the company more than five years ago. None of these interfaces could have been enumerated from Summit's documentation because, in a real sense, they were never documented in the first place.

This is a materialization of exactly the risk the original case named as its largest: implementation overrun concentrated in the integration workstream, driven by the count and complexity of legacy Summit interfaces. The discovery does not reflect a vendor failure or an estimation error in pricing; it reflects the reality that a seventeen-year-old, heavily customized on-premise platform accumulates undocumented connective tissue that cannot be fully enumerated until an exhaustive mapping exercise is performed. Rebuilding, testing, and cutting over fourteen integrations rather than six increases the implementation-and-integration effort, extends the data-migration and testing timeline, and enlarges the contingency the program prudently carries. The Q3 2026 Steering Committee reviewed this finding on September 15, 2026, accepted it as a genuine and unavoidable scope expansion rather than a controllable overrun, and directed this change request. The committee's discussion, recorded in the Q3 2026 minutes, was notably unanimous on one point: that the discovery vindicated rather than undermined the decision to retire Summit, since a platform whose own operators cannot fully account for what connects to it is by definition a control and continuity liability.

## Revised Financial Model

The table below presents the original October 2024 program metrics alongside the revised figures established by this addendum. The revised figures are current and authoritative; the original figures are shown for comparison only. All figures are in millions of U.S. dollars except ratios and periods, and all discounting uses the company's standard 8% rate.

| Metric | Original (Oct 2024) | Revised (This Addendum) | Change |
|---|---|---|---|
| 3-year total cost of ownership | $22.5M | $27.8M | +$5.3M (+23.6%) |
| Net present value (8%) | $4.9M | $2.1M | -$2.8M |
| Internal rate of return | 19% | 12% | -7 pts |
| Payback period | 28 months | 34 months | +6 months |
| Go-live target | Q4 2026 | Q2 2027 | +6 months |

The $5.3M increase in total cost of ownership — a 23.6% rise over the original budget — is driven almost entirely by the integration workstream. The additional eight integrations require incremental systems-integration effort to reverse-engineer, rebuild, and test; an expanded data-migration and validation scope, since several of the newly discovered interfaces move master and transactional data that must be reconciled during cutover; a longer stabilization and hypercare tail; and a proportionate increase in the contingency reserve to reflect the enlarged and partially still-uncertain integration surface. Subscription and licensing costs are essentially unchanged, since the platform footprint and user counts are the same; the increase is concentrated in the implementation, data-migration, and contingency categories, exactly where the additional integration work lands.

The projected benefit stream is unchanged in composition — the capabilities Ledgerline delivers are the same, and the finance-close, inventory, markdown, IT, and audit value streams identified in the original case all remain valid — but the six-month schedule slip pushes benefit realization further into the future, which, combined with the higher cost base, compresses the net present value to $2.1M and the internal rate of return to 12%. Both remain positive and above the 8% hurdle rate: the program still creates value, but with a materially thinner margin than the original case projected. The revised 34-month payback reflects both the larger outlay and the delayed onset of the benefit stream. It is worth stating plainly for the board's benefit that this revised case is genuinely tighter than the original: a program that once carried a comfortable cushion now sits closer to the hurdle, and the margin for any further benefit shortfall has narrowed considerably. That reality is reflected in the heightened risk ratings below and is the principal reason the Enterprise PMO has re-instrumented the benefits baselines ahead of the revised go-live.

## Revised Timeline

The go-live target moves from Q4 2026 to Q2 2027, a six-month extension. The additional time is absorbed almost entirely by the expanded integration build-and-test cycle and the corresponding lengthening of the cutover and data-validation windows. The revised milestone schedule is as follows.

| Milestone | Original Target | Revised Target |
|---|---|---|
| Integration mapping complete | Q1 2026 | Completed H1 2026 (revealed 14 integrations) |
| Configuration & build complete | Q2 2026 | Q4 2026 |
| Integration rebuild & unit test complete | Q2 2026 | Q1 2027 |
| End-to-end & user acceptance testing | Q3 2026 | Q1 2027 |
| Data migration dress rehearsals | Q3 2026 | Q1 2027 |
| Go-live / cutover | Q4 2026 | Q2 2027 |
| Post-go-live hypercare complete | Q1 2027 | Q3 2027 |

The critical path now runs squarely through the integration rebuild-and-test milestone: with fourteen interfaces to reconstruct and validate rather than six, this phase both starts later and runs longer, and every downstream milestone shifts with it. The program retains its phased, stage-gated structure, so the Steering Committee will continue to review progress at each quarterly meeting and can pause or re-baseline at any gate.

## Updated Risk Assessment

The risk profile is reassessed against the same five standard categories used in the original case, with explicit note of which risks have materialized.

| Risk Category | Revised Rating | Status & Commentary |
|---|---|---|
| Implementation overrun | High (materialized) | This is the risk that has come to pass. The integration surface proved more than twice the scoped size. The change request re-baselines cost and schedule to the discovered reality; residual risk now centers on whether any further undocumented interfaces remain, mitigated by the completed exhaustive mapping. |
| Benefit-realization shortfall | Medium-High | Unchanged in nature but heightened in consequence: with NPV compressed to $2.1M, the program has far less margin to absorb any benefit shortfall. Benefit owners and the benefits tracker remain in place, and baselines are being re-confirmed ahead of the revised go-live. |
| Data-quality degradation | Medium-High | Elevated. Several newly discovered integrations move master and transactional data, enlarging the migration and reconciliation scope and the surface for data defects. Mitigation: additional dress-rehearsal cycles and expanded validation gates built into the revised timeline. |
| Adoption failure | Medium | Broadly unchanged. The six-month slip modestly extends the period of legacy/parallel operation, but the training and change-management approach is unaffected. Hypercare is extended to Q3 2027. |
| Vendor viability | Low | Unchanged. Ledgerline Systems remains financially sound; the scope change is internal to Copperline's legacy estate and does not alter the vendor risk assessed in the finalist scorecard. |

The headline of the reassessment is that implementation overrun has moved from a managed forward-looking risk to a materialized event that this change request addresses head-on. The compression of NPV to $2.1M also raises the stakes on benefit realization and data quality, both of which are reflected in tighter instrumentation and additional validation cycles in the revised plan.

## Governance & Ratification

The revised three-year total cost of ownership of $27.8M remains substantially above the $5M single-year capital threshold that, under the Business Case Review and Template Guide, requires Board Finance & Audit Committee ratification. A change of this magnitude — a $5.3M, 23.6% increase over a previously board-ratified figure — cannot be authorized at the Steering Committee level alone. This addendum therefore requires supplemental ratification by the Board Finance & Audit Committee.

Harold Whitcombe, Independent Director and Chair of the Board Finance & Audit Committee, is the ratifying authority, consistent with his role in ratifying the original December 2024 case. Following Steering Committee endorsement of this change request, the addendum will be advanced to the Finance & Audit Committee for supplemental ratification of the revised $27.8M program budget and Q2 2027 go-live. The sponsor reaffirms the commitment to bring any further material change in scope, cost, or timeline back through the same governance path.

## Recommendation

The Enterprise PMO and FP&A recommend that the Tech Investment Steering Committee endorse this change request and advance it to the Board Finance & Audit Committee for supplemental ratification. The recommendation is to proceed with the ERP Replacement program under the revised scope and budget: a three-year total cost of ownership of $27.8M, a Q2 2027 go-live, a net present value of $2.1M, an internal rate of return of 12%, and a 34-month payback.

The rationale for continuing rather than pausing is clear. The scope increase reflects work that must be done regardless of platform — the fourteen integrations are real, load-bearing, and cannot be abandoned without breaking live business processes. The strategic case that justified the program in October 2024 is unchanged and, if anything, reinforced: the discovery of eight additional undocumented interfaces is itself the strongest possible illustration of why the fragile, opaque Summit estate must be retired. The revised financial case, though thinner, remains value-creating, with NPV positive and IRR above the 8% hurdle. Stopping now would strand the cost already sunk and leave Copperline dependent on precisely the legacy platform this program exists to replace.

**Sponsor:** Renata Alvarez, EVP & Chief Financial Officer
**Revised financial model prepared by:** Omar Delgado, Director, FP&A
**Addendum author:** Elena Popescu, Director, Enterprise PMO
**Date:** September 25, 2026
**Disposition:** Submitted for Steering Committee endorsement and supplemental Board Finance & Audit Committee ratification
