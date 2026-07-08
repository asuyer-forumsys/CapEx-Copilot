# Financial Methodology Reference

## Purpose

This reference defines the financial methodology Copperline Retail Group, Inc. uses across all business cases, post-implementation reviews, and the portfolio benefits tracker. It exists so that every sponsor, FP&A analyst, and reviewer applies the same definitions, formulas, and conventions when they compute or interpret a return metric. Where the Business Case Review and Template Guide states *that* a convention is mandated — the 8% discount rate, the three-year horizon, the five risk categories — this document explains *how* the underlying metrics are constructed and where analysts most often go wrong.

The methodology here is company-wide. It is maintained alongside the PMO's template guide and is the authority FP&A cites when a case is returned for a modeling defect. Sponsors are not expected to be financial specialists, but they are expected to understand what each headline number in their Executive Summary means and how it was derived, because they will be asked to defend it before the Tech Investment Steering Committee. Illustrative examples in this document use deliberately simple invented figures; they are not drawn from any of Copperline's active business cases and should not be read as a recalculation of any live initiative.

## Net Present Value (NPV)

Net Present Value expresses the value an initiative creates after accounting for the time value of money. Money received in the future is worth less than money in hand today, because today's money can be put to work. NPV discounts each future net cash flow back to today's dollars and sums them, netting against the initial and ongoing investment. A positive NPV means the initiative is expected to create value above Copperline's cost of capital; a negative NPV means it destroys value on the assumptions modeled.

The formula is:

```
NPV = Σ [ CFt / (1 + r)^t ]  for t = 0 .. N
```

where `CFt` is the net cash flow in period `t` (benefit minus cost), `r` is the discount rate, and `N` is the final period of the horizon. Costs are negative cash flows and benefits are positive; the initial outlay typically sits at `t = 0` and is not discounted.

Copperline mandates a discount rate of **8%** for every NPV calculation, without exception. Analysts may not substitute a project-specific hurdle rate, because a single, uniform rate is what makes NPVs comparable when the Steering Committee ranks competing asks. The 8% rate is Copperline's approved corporate figure and is reviewed only at the corporate level, not case by case.

A worked illustration using simple invented numbers shows the mechanics. Suppose an initiative requires a $100 outlay today and returns net cash of $40, $50, and $60 at the end of years one, two, and three.

| Period (t) | Net cash flow | Discount factor at 8% | Present value |
|---|---|---|---|
| 0 | -100.00 | 1.0000 | -100.00 |
| 1 | 40.00 | 0.9259 | 37.04 |
| 2 | 50.00 | 0.8573 | 42.87 |
| 3 | 60.00 | 0.7938 | 47.63 |
| **NPV** | | | **27.53** |

The discount factor for each year is `1 / (1.08)^t`. Multiplying each net cash flow by its factor and summing gives an NPV of about $27.53, so on these assumptions the initiative creates roughly $27.53 of value in today's dollars above the 8% cost of capital. The example is intentionally abstract; real Copperline cases model monthly or quarterly ramps and a fuller cost stack.

Two practical conventions apply to how analysts lay out the cash flows before discounting. First, the sign convention must be consistent: costs are entered as negative and benefits as positive within the same net-cash-flow line for each period, rather than tracking two separate undiscounted series and netting them at the end, which invites arithmetic error. Second, the timing convention must be stated: Copperline models place the initial outlay at `t = 0` (undiscounted) and treat subsequent flows as occurring at period-end. Analysts sometimes shift this to mid-period discounting to reflect benefits accruing evenly through the year; either is acceptable provided the convention is disclosed in the model and applied uniformly, because an undisclosed timing shift can move NPV by several percent and is a frequent source of reconciliation gaps between a sponsor's spreadsheet and the FP&A model.

## Internal Rate of Return (IRR)

The Internal Rate of Return is the discount rate at which an initiative's NPV equals zero. Conceptually it is the initiative's own effective annualized return: if the IRR exceeds Copperline's 8% discount rate, the NPV at 8% is positive, and the two metrics agree that the initiative creates value. IRR is useful because it expresses return as a single percentage that is intuitive to compare against the cost of capital, but it should always be read alongside NPV, not in place of it. NPV measures the *magnitude* of value created; IRR measures the *rate*. A high-IRR, small-dollar initiative can create less total value than a lower-IRR, large-dollar one.

IRR has known limitations that Copperline reviewers watch for. It can be mathematically unstable or multi-valued when a cash-flow stream changes sign more than once, and it implicitly assumes interim cash flows are reinvested at the IRR itself, which can flatter a very high-return case. For these reasons NPV remains Copperline's primary decision metric and IRR its supporting one.

IRR is **not computed** when an initiative's value is expressed primarily as risk reduction rather than as a conventional benefit cash-flow stream. Security investments are the standing example: the Cybersecurity Modernization (Zero Trust) case is evaluated on NPV and a risk-adjusted benefit figure, and its IRR is reported as not applicable, because the "benefit" is largely avoided loss and reduced exposure rather than a directly bankable cash inflow that an IRR would meaningfully summarize.

## Payback Period

The payback period is the time required for cumulative benefits to recover the initial investment. It answers a different question from NPV — not "how much value?" but "how long until we are made whole?" — and is valued at Copperline as a plain-language read on risk exposure: a shorter payback means capital is at risk for less time.

There are two variants. **Simple payback** counts undiscounted cash flows until the cumulative total turns positive. **Discounted payback** counts discounted cash flows, and is therefore always at least as long as simple payback because discounting shrinks later inflows. Copperline's convention is to report payback in **months** and to compute it on the standard model so that it is consistent across cases. Payback is a screening and communication metric, not a decision rule on its own: an initiative with an attractive payback can still have a weak NPV if benefits collapse after the payback point, which is one reason payback is always presented next to NPV and IRR rather than alone.

## Total Cost of Ownership (TCO)

Total Cost of Ownership is the full cost of an initiative over its evaluation horizon, not merely its purchase price or first-year spend. Copperline models TCO over a standard **three-year** horizon and requires it to be built up from a standard set of cost categories so that nothing material is omitted or hidden inside a single line:

- **Licensing** — software subscription or license fees over the horizon.
- **Implementation** — the cost of standing the solution up, including internal labor and systems-integrator fees.
- **Integration** — connecting the solution to Copperline's existing systems (POS, ERP, WMS, CDP, and related platforms).
- **Data migration** — extracting, cleansing, and loading data into the new system.
- **Training** — enabling associates and staff to use the capability; frequently underestimated and, as the benefits tracker shows, frequently the driver of adoption shortfalls.
- **Infrastructure** — cloud or on-premise compute, storage, and network capacity.
- **Contingency** — an explicit reserve for the uncertainty inherent in delivery.

Requiring every category keeps sponsors from presenting an artificially low TCO by leaving out integration or training and then discovering those costs after approval. The three-year horizon matches the benefit horizon so that TCO and benefit are compared over the same window.

A recurring judgment in TCO modeling is the treatment of internal labor. Copperline's convention is to include the fully loaded cost of internal staff whose time is materially redirected to an initiative, even though that cost does not appear as a new invoice, because omitting it understates the true cost of ownership and flatters the return. Purely incremental external spend and redirected internal effort are both counted; only genuinely spare capacity that would otherwise be idle is excluded, and that exclusion must be justified in the model notes. A second judgment is the horizon boundary: costs that are contractually committed within the three-year window but paid just outside it are pulled into the horizon, while speculative year-four refresh costs are not, so that the horizon is applied to committed cash rather than to convenient cut-off dates.

## Benefit-Cost Ratio and Risk-Adjustment

The benefit-cost ratio is the projected three-year benefit divided by the three-year TCO, a quick read on how many dollars of benefit each dollar of cost is expected to return. It is a useful sanity check but is not a substitute for NPV, because it ignores timing.

For investments whose benefit is dominated by avoided loss rather than realized cash — chiefly security and resilience initiatives — Copperline derives a **risk-adjusted benefit** rather than booking a raw avoided-loss figure. The method is to estimate the exposure being reduced (for example, the modeled financial impact of a class of incident), weight it by a defensible probability of occurrence, and then apply the reduction in that probability or impact that the initiative delivers. The resulting expected-value figure is what enters the benefit line. This discipline keeps security cases honest: it prevents a sponsor from claiming the full gross value of a worst-case breach as a benefit, and it makes explicit the probability and impact assumptions that reviewers can then challenge. It is also why IRR is set aside for these cases, since the risk-adjusted benefit is an expected value rather than a contracted inflow.

Reviewers of risk-adjusted cases should pay particular attention to the probability estimate, which carries most of the weight and is the hardest to source. Copperline expects the estimate to be anchored to something external — industry incident base rates, the organization's own historical event frequency, or a control-maturity assessment — rather than asserted. A useful discipline is to show the benefit under a range of probability assumptions in the Scenario Modeling section, so the Committee can see how sensitive the case is to that single input. Where a security case's positive NPV depends on an aggressive probability assumption that cannot be defended, the honest conclusion is that the case rests on risk tolerance rather than on financial return, and it should be presented on that footing.

## Common Pitfalls and Reviewer Checklist

Most business cases returned by FP&A fail on a small number of recurring modeling errors. Reviewers are expected to check each case against the items below before it reaches the Steering Committee.

| Common pitfall | What it looks like | What the reviewer checks |
|---|---|---|
| Overstated adoption | Benefit ramp assumes near-universal, immediate uptake | Is the adoption curve evidenced? Does the downside scenario stress it? Training completion is the usual real-world constraint. |
| Benefit double-counting | The same savings claimed in two components, or a benefit already counted in another approved case | Are benefit components mutually exclusive and separately measurable? |
| Undocumented integration scope | A low integration line with no list of systems to be connected | Is every integration point named and costed? Integration is a mandatory TCO category. |
| Wrong or varying discount rate | NPV computed at anything other than 8% | Is 8% applied uniformly across all periods? |
| Optimistic benefit timing | Full-year benefit booked in the go-live year | Does the model reflect a realistic ramp, with partial benefit in the first period? |
| Missing contingency | TCO with no reserve against delivery uncertainty | Is an explicit contingency line present and proportionate to delivery risk? |
| Unmeasurable benefits | Headline benefit includes items with no post-go-live metric | Can each benefit be tracked in the quarterly benefits tracker? If not, it should not be in the headline. |
| Simple vs. discounted payback confusion | Payback quoted without stating which basis | Is the basis stated, in months, and consistent with the model? |

A case that clears this checklist, conforms to the seven-section template, and reconciles to the FP&A model is ready for Committee review. Questions on methodology should be raised with FP&A before submission rather than debated at the Committee table.
