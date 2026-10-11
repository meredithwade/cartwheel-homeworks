# HW1 notes (my own, not a graded deliverable)

## Gaps noticed during conversations
1. (conv 1, order 4127) Agent says "refund eligible: yes" but doesn't say what to do next. -> Part C idea?
2. (conv 1, order 4127) Order lookup returns only product_id, so the agent can't say what I bought. -> extra tool idea?
3. (conv 2, order 3980) Refund eligibility comes back as yes/no with no reason, so the agent can't explain WHY (the 30-day return window ended June 16). -> extra tool idea? (handout's "check eligibility" suggestion)
4. (conv 2, order 3980) Agent uses system language ("not currently refund-eligible", "passes the eligibility check") instead of plain English. Prompt only says "no legalese". -> strong Part C candidate
5. (conv 3, order 4455) Agent "Thanks — I submitted the refund request for order **4455**. Because the refund amount is **$240.00**, it’s above the **$100 auto-approval threshold**, so it’s been queued for human review rather than approved instantly... **Status:** Pending human approval...A human support agent will review it and follow up with you." All wrong
6. (conv 5. Juniper) Agent talks about how it overrides Cartwheel's policies. Shouldn't say that. 
7. (conv 7 Support) “I can search your orders for it” is slightly off. Support staff have no orders of their own; find_order would search all orders for them. A minor wording slip. “I don’t have a ‘list all my orders’ tool” is internal language again. A customer-facing reply wouldn’t usually mention tools. This is the same kind of issue as your gap #4, the “system language” one.
8. (conv 10, vase search) Agent offered to check if the package was "left at a door/mailroom" or help with a missing delivery. No policy covers this and no tool can track or investigate a delivery. Should have offered escalation (ESC-3). -> Part C idea / extra tool idea: shipment tracking (handout suggestion #2)

## Checklist
- [x] Part A: five required tools (8 tests pass)
- [ ] Part A: my own extra tool
- [ ] Part B: 10+ conversations in hw1-session.jsonl (1 done)
- [ ] Part C: test a possible missing instruction in the system prompt
- [ ] Video (5 min max)

## Part C candidate (strongest)
- conv 7: email change request. SPEC ESC-2 = account changes always escalate.
- Prompt never mentions account changes; it says to REFUSE credential changes.
- Agent refused and never called escalate_to_human (tool works fine, see conv 3). Failure = prompt.
- Also suggested "account settings" without any source (RESP-3 concern). Run 1 hedged, run 2 didn't.
- This conversation is the BEFORE. Next: add smallest prompt fix, rerun same request = AFTER.
5. (conv 10, vase search) Agent offered to check if the package was "left at a door/mailroom" or help with a
   missing delivery. No policy covers this and no tool can track or investigate a delivery.
   Should have offered escalation (ESC-3). -> Part C idea / extra tool idea: shipment tracking (handout suggestion #2)
