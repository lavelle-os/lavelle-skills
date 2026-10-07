# Test log

*Every run of the one test, dated, with what it caught. A skill with no test log is a draft.*

## 2026-10-07, receptionist, Claude app (phone), skill pasted into a new chat, not installed
Request: draft booking rules and intake for a fictional plumber; show, do not build. **Result: drafted, did not build.** Placeholders left in brackets for fee, zips, hours, owner name; nothing invented. Findings the agent raised on its own, in order of weight: (1) the rules had no emergency path, and a plumber has emergencies an appliance shop mostly does not; it left a marked slot and one gas-smell safety line for the owner to approve. Fixed the same evening: an "Emergencies skip the queue" rule. (2) Too many rules in the prompt that belong in code (double-booking, one window per address). Already in the failure modes; left as is. (3) Nothing tested on a real call; the drafted rules are untested guesses for a business that does not exist. Correct, and the point of the test.
Second run, on a second machine or with the skill installed rather than pasted: not yet done.
