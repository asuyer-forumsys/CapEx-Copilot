# Business Case: AI Customer Service Chatbot ("Conversant AI")

## Executive Summary

This business case proposes Conversant AI, an AI-powered conversational customer-service capability intended to automate a substantial share of Copperline Retail Group's inbound tier-1 customer contacts, reduce average handle time on escalated contacts through agent-assist, and absorb seasonal call-volume spikes without proportional staffing. The initiative is sponsored by Talia Novak, VP Customer Experience, with financial modeling prepared by Omar Delgado, Director of FP&A. It was prepared for presentation to the Tech Investment Steering Committee in the third-quarter 2026 review cycle.

The program carries a three-year total cost of ownership of $4.3M against a projected three-year benefit of $6.9M. At the mandated 8% discount rate, it returns a net present value of $2.0M, an internal rate of return of 33%, and a simple payback of 17 months. On its own standalone metrics, the case is financially attractive — the highest IRR and shortest payback of any initiative in the FY2027 candidate portfolio. It is also, as the Committee ultimately concluded, the most easily deferred, and the Recommendation and Governance section documents the disposition reached.

The strategic thesis is that Copperline's contact center is under structural cost pressure and is especially strained by the seasonal spikes that characterize a home-and-garden business. A large fraction of inbound contacts are routine — order status, store hours and inventory, return policy, delivery scheduling — and are well suited to automation. Conversant AI would deflect these contacts through a conversational interface across web, mobile, and messaging channels, and would assist live agents on more complex contacts, shortening handle time and improving consistency. The expected benefits are lower contact-center labor cost, reduced average handle time, and, through faster resolution, improved customer satisfaction.

## Problem and Strategic Context

Copperline's contact center carries a cost base that grows with the business and spikes with the seasons, and a rising share of that cost is spent on contacts that do not require human judgment. Inbound volume is dominated by routine, repetitive inquiries: "Where is my order?", "Does my local store have this item?", "What are your holiday hours?", "How do I return an online purchase?", "When is my delivery scheduled?" These tier-1 contacts are numerous, individually low-value, and highly automatable, yet today each one consumes a live agent's time.

The seasonality of the assortment makes the cost problem worse. Home and garden demand concentrates sharply in the spring planting season and again around the holidays, and contact volume tracks that curve. Copperline meets the peaks with a combination of overtime and seasonal temporary staffing, both of which are expensive and neither of which is efficient: temporary agents require training, ramp slowly, and are released before that investment fully pays back, while overtime strains the permanent team and degrades service quality at the worst possible time. During peak weeks, customer wait times lengthen, abandonment rises, and the customer-experience metrics the organization is accountable for deteriorate precisely when customer traffic — and the stakes — are highest.

The strategic context is a contact center that cannot scale economically. Every incremental point of e-commerce growth generates incremental contact volume, and under the current model that volume converts more or less linearly into labor cost. E-commerce is approximately 18% of Copperline's $1.92B FY2025 net revenue and is the fastest-growing channel, so the contact-cost curve is on a structurally rising path even before seasonal effects are layered in. Conversant AI is proposed as the lever that breaks that linearity: automating the routine contacts that make up the bulk of volume, so that human agents concentrate on the complex, high-empathy interactions where they add real value, and so that seasonal spikes are absorbed by elastic automation rather than by expensive temporary staffing. The customer-experience thesis is that faster, always-available, consistent answers to routine questions improve satisfaction even as cost falls.

The capability also fits a broader digital-experience arc. The unified commerce platform and the Lumenpoint CDP investment give Copperline, for the first time, authoritative real-time order, inventory, and customer data — precisely the substrate a conversational agent needs to answer routine questions accurately rather than generically. A chatbot deployed without that substrate would be limited to canned responses; deployed on top of it, it can resolve a genuine "where is my order and can I change the delivery window" interaction end to end. That dependency is a strength of the timing thesis but also, as the committee later observed, an argument for sequencing the chatbot behind the maturation of the data foundation it relies upon.

## Financial Modeling

The financial model was prepared by Omar Delgado, Director of FP&A, on the standard three-year TCO basis at the 8% discount rate. The total cost of ownership is $4.3M, distributed as follows.

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| Conversant AI platform subscription | $0.7M | $0.75M | $0.75M | $2.2M |
| Implementation and integration | $0.8M | $0.2M | $0.1M | $1.1M |
| Model usage, NLU tuning and maintenance | $0.2M | $0.2M | $0.2M | $0.6M |
| Knowledge-base development and training | $0.15M | $0.05M | $0.05M | $0.25M |
| Allocated internal labor | $0.05M | $0.05M | $0.05M | $0.15M |
| **Total** | **$1.9M** | **$1.25M** | **$1.15M** | **$4.3M** |

The cost profile is the lightest of any initiative in the FY2027 candidate set, reflecting a software-only program with no physical deployment. Year 1 carries the implementation and integration spend — connecting the platform to the order-management, store-inventory, and CRM systems that feed the routine inquiries it must answer — plus the initial knowledge-base build. The platform subscription and the model-usage line are essentially flat run-rate costs; the ongoing NLU tuning and knowledge-base maintenance line is deliberately funded through all three years, because a conversational system that is not continuously maintained degrades as products, policies, and customer language change.

Against this cost base, the three-year benefit of $6.9M yields an NPV of $2.0M, an IRR of 33%, and a payback of 17 months. The strong IRR and short payback are functions of the low, front-light cost base and the fast onset of deflection savings once the system is live.

## Benefits Analysis

The benefit case rests on three quantified levers, all flowing from automating and assisting customer contacts.

| Benefit Metric | Baseline | Target (Year 3 exit) | 3-Year Value Contribution |
|---|---|---|---|
| Tier-1 contact deflection (contact-center labor cost) | ~0% automated | Substantial tier-1 automation | $4.2M |
| Average handle time on escalated contacts (agent-assist) | Full manual handling | Reduced via agent-assist | $1.9M |
| Customer satisfaction (CSAT) on routine inquiries | Wait-time-dependent | Faster, always-on resolution | $0.8M |
| **Total quantified benefit** | | | **$6.9M** |

The deflection lever is the largest contributor. Automating a substantial share of routine tier-1 contacts across web, mobile, and messaging removes those contacts from the live-agent queue, reducing both permanent contact-center labor cost and, critically, the seasonal overtime and temporary-staffing premium paid to meet peaks. The model sizes deflection conservatively, crediting only contact types with high automation confidence and assuming a graded ramp as the knowledge base matures.

The average-handle-time lever operates on the contacts that are not deflected. Agent-assist surfaces relevant order, inventory, and policy information to the live agent in real time, shortening handle time and improving first-contact resolution on complex inquiries. The value is booked as labor efficiency on the escalated contact base.

The CSAT lever captures the customer-experience upside: always-available, instant answers to routine questions, and shorter waits on escalated contacts because agents are freed from routine volume. The model credits only a modest retention-linked value here, keeping the case's benefit weighted toward the hard labor savings.

## Risk Assessment

The following assessment addresses the five standard risk categories.

**Implementation overrun.** The program is software-only and modest in scope, limiting overrun exposure, but it depends on integrations to order-management, inventory, and CRM systems to answer contacts accurately. The risk is assessed as low-to-moderate, concentrated in Year 1 integration. Mitigations include a fixed-scope implementation and phased channel rollout beginning with the highest-volume, most-automatable contact types.

**Benefit-realization shortfall.** The savings depend on deflection rates actually achieved, which in turn depend on the quality and coverage of the knowledge base and on customers accepting a conversational interface. The risk is assessed as moderate. Mitigations include a conservative graded-deflection assumption, continuous knowledge-base tuning, and measurement of deflection and containment rates as governed KPIs.

**Data-quality degradation.** The chatbot's answers are only as accurate as the underlying order, inventory, and policy data it retrieves; stale or incorrect data produces confidently wrong answers that damage trust more than a slow human answer would. The risk is assessed as moderate. Mitigations include grounding responses in authoritative real-time systems, guardrails that escalate to a human on low confidence, and a maintained content pipeline for policy changes.

**Adoption failure.** Adoption risk is two-sided: customers may bypass or distrust the bot, and agents may under-use agent-assist. The risk is assessed as moderate. Mitigations include a frictionless escalation path that keeps customer trust, clear signposting of automated versus human interaction, and agent enablement so that assist is a help rather than an interruption.

**Vendor viability.** The conversational AI market is fast-moving and crowded, and platform capabilities and pricing are evolving quickly. The risk is assessed as moderate — higher than for the more mature platform categories in the portfolio — because a vendor or the underlying model economics could shift materially within the three-year window. Mitigations include contractual portability of the knowledge base and conversation designs, avoidance of deep proprietary lock-in, and a preference for architectures that can adapt to evolving model options.

## Scenario Modeling

The model was flexed under three scenarios, varying deflection rate and implementation cost, holding the 8% discount rate constant.

| Scenario | Key assumptions | 3-Year Benefit | 3-Year Cost | NPV (8%) | Payback |
|---|---|---|---|---|---|
| Base | Graded deflection to substantial tier-1 automation; cost on plan | $6.9M | $4.3M | $2.0M | 17 mo |
| Optimistic | Higher deflection and containment; cost on plan | $8.4M | $4.3M | $3.2M | 13 mo |
| Pessimistic | Deflection reaches ~60% of plan; ~10% cost overrun | $4.9M | $4.7M | $0.5M | 26 mo |

The base case is the recommended planning basis. The optimistic case assumes deflection and containment exceed plan as the knowledge base matures quickly. The pessimistic case models weaker customer acceptance and a cost overrun, and even then the program stays marginally NPV-positive. The scenario spread shows a resilient standalone return; the case's vulnerability is not its economics but its strategic priority relative to competing capital demands, which is where the Committee's deliberation ultimately turned.

## Recommendation and Governance

On its standalone merits, the sponsor recommended approval: Conversant AI carries the highest IRR (33%) and shortest payback (17 months) of any FY2027 candidate, at the lowest absolute cost ($4.3M TCO), and addresses a real and growing contact-center cost problem.

**Committee disposition.** The Tech Investment Steering Committee reviewed the case at its third-quarter 2026 meeting on September 15, 2026, and recorded a disposition of **rejected for FY2027**. The Committee's documented rationale was not a challenge to the arithmetic but a matter of prioritization and confidence. First, the FY2027 capital envelope is heavily committed to two large, strategically foundational programs — the in-flight ERP replacement and the WMS and robotics investment under consideration — and the co-chairs judged that customer-service automation, however attractive its return, ranks below core operational and supply-chain modernization in strategic priority for the coming year. Second, the Committee expressed reservations about ROI confidence at this stage: the benefit is concentrated in a deflection assumption that is unproven in Copperline's specific contact mix, the conversational AI vendor landscape is evolving rapidly enough to make a one-year deferral prudent, and the Committee preferred to see the customer-data and personalization foundation (Lumenpoint CDP) mature before layering an AI service capability on top of it. The Committee noted that the case is well-constructed and financially sound, and invited the sponsor to resubmit in a future cycle once the competing capital demands ease and deflection assumptions can be validated with a limited proof of concept.

Sponsorship rests with Talia Novak, VP Customer Experience; the financial model is owned by Omar Delgado, Director of FP&A. The case is retained in the portfolio backlog for reconsideration in a subsequent cycle, with its disposition of record standing as rejected for FY2027.
