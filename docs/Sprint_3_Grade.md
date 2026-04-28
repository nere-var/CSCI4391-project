# Sprint 3 Grade, Venture 4: Krusty Compost Crew (Binny & Bloom)

**Graded:** April 28, 2026
**Sprint Window:** April 15 – April 24, 2026 (extended from April 21)
**Final Demo:** April 29, 2026
**Final Deliverables Due:** May 3, 2026

---

## Overall Grade: 95/100

**Note on individual grades:** This is the venture-level grade. Members who severely under-contributed during Sprint 3 may receive a reduced individual grade applied separately.

---

## Summary

Sprint 3 was the team's strongest sprint of the semester. Every Definition of Done item is checked, every P0 item shipped, every P1 item shipped, and several P2/P3 items also landed. The 20-case evaluation rerun is documented in `docs/Milestone 2 - Sprint 3/evaluation_rerun.md` with full image evidence and pass/fail rationale. The waste-reduction dashboard now shows efficiency rankings and per-player formula breakdowns. The chat-page loading indicator (a Sprint 2 video pain point) is wired into `InventoryPage.html` with a real GIF. Two demo rehearsals are documented (`rehearsal_notes.md`, `rehearsal2.md`), with feedback rolled into the second pass. `unit_conversion.py` was consolidated and `test_unit_conversion.py` provides regression coverage. The single-ingredient hallucination edge case was hardened with safer AI output handling. `main.py` was renamed to `cli.py` to clarify the entry-point structure. A late-window dietary and allergy check was added on top of all required work.

Contribution is exceptional. Five members shipped substantial code or documentation: Luis 40, Jaylynn 36, Abigail 19, Taja 17, Emma 12. The split is not perfectly even but every member has visible, meaningful work and the Sprint 2 concern (Jay's lower commit count) has been addressed in full. Luis and Jaylynn both crossed thirty commits.

The grade sits at 95 rather than higher because: the dry-run-2 video upload mechanism took several iterations to land cleanly (file-rename ping-pong on Apr 24 in the README and Video_Recording.md), and a few of the late-window README updates suggest the documentation packaging for May 3 still needs one more pass. These are nitpicks against an otherwise standout sprint.

---

## Category Breakdown

### 1. Task Completion (39/40)

**P0 (4 of 4 complete):**
- 20-case evaluation rerun: shipped with full image evidence in `evaluation_rerun.md` and `evaluation_rerun_images/`.
- Waste-reduction dashboard UI: shipped with efficiency ranking, formula breakdown, two-decimal score rounding, ranking by efficiency percentage.
- Full team demo rehearsal (dry run 1): shipped (`rehearsal_notes.md`).
- Loading indicator wired into chat: shipped. `showLoading()` triggers on form submit, GIF appears during recipe generation, disappears on response.

**P1 (4 of 4 complete):**
- Single-ingredient hallucination fix: shipped (`Added safer ai output and fixed saved recipe formatting`).
- Consolidated unit conversion tables: shipped. `unit_conversion.py` has a single normalize/convert source of truth, `test_unit_conversion.py` covers it with pytest.
- Demo script timings + speaker notes: shipped as `final_demo_script.md` with login-failure scenario, gamification scenario, and per-step structure.
- Sprint 2 DoD cleanup: shipped (small Luis commits).

**P2 (3 of 3 complete):**
- Expiry notification prominence: shipped (`Two-tier severity`, `Notification Order`, `Welcome Text Readability`, all by AlexandriaTH/Taja).
- Use / donate / compost on camera: shipped via gamification commits and demo script Scenario 1 enhancements.
- Gamification score visibility: shipped (real-time score updates on dashboard).

**P3 (3 of 3 complete):**
- Dry run 2 + video capture: shipped (`rehearsal2.md`, dry-run-2 video).
- Screenshot refresh: shipped (Abigail's `ImagesPt2` reorganization with new inventory and notification banners).
- README pass: shipped multiple iterations by Luis.

**Bonus:** Dietary and allergy check (Jaylynn Apr 22), `main.py` → `cli.py` rename (Luis Apr 23), safer AI output formatting.

### 2. Code Quality (18/20)

- `cli.py` rename clarifies entry-point structure.
- `unit_conversion.py` is a clean single-source module.
- Score rounding to two decimals throughout the dashboard is the kind of polish the demo benefits from.
- Loading-image GIF and CSS are properly served from `static/Pictures/`.

### 3. Documentation (14/15)

- `evaluation_rerun.md` with image evidence is the most thorough evaluation document submitted by any team this semester.
- Two rehearsal documents capture both runs and the feedback loop between them.
- `final_demo_script.md` with timings and per-step content is ready for the live demo.

### 4. Testing / Evaluation (14/15)

- 20-case rerun with images for every test case.
- `test_unit_conversion.py` pytest coverage on every conversion path.
- Two timed rehearsals documented.

### 5. Team Contribution (10/10)

| Member | In-window Commits | Sprint 3 Work | Signal |
|---|---|---|---|
| Luis M | 40 | README iteration, env.example, db rebuild scripts, cli.py rename, openrouterllm.py tuning, video uploads | Strong |
| Jaylynn Vega (Jay) | 36 | Gamification (delete/cook/donate/compost), dietary/allergy check, demo script, validator polish, db management | Strong |
| Abigail Rodriguez Vazquez | 19 | Loading indicator, screenshot refresh, ImagesPt2 reorganization, rehearsal notes | Strong |
| AlexandriaTH (Taja) | 17 | Notification severity, welcome readability, evaluation rerun with images, last 11+10 test-case images | Strong |
| nerevar / ner (Emma) | 12 | Waste reduction dashboard, efficiency rankings, score rounding, scoreboard updates | Strong |

All five members shipped substantial work. The plan called for distributing P0 critical-path tasks across four different people (rather than concentrating on Luis); that distribution materialized.

---

## Per-Task Completion Status

| Priority | Task | Owner | Status |
|---|---|---|---|
| P0 | Re-run 20-case evaluation | Taja | Done (with images) |
| P0 | Waste reduction dashboard UI | Emma | Done |
| P0 | Full team demo rehearsal | All | Done |
| P0 | Wire loading indicator into chat | Abigail | Done |
| P1 | Fix single-ingredient hallucination | Emma | Done |
| P1 | Consolidate unit conversion tables | Emma | Done (+ pytest) |
| P1 | Tighten demo script timings | Jay | Done |
| P1 | Update Sprint 2.md DoD | Luis | Done |
| P2 | Expiry notification prominence | Taja | Done |
| P2 | Use / donate / compost on camera | Jay | Done |
| P2 | Gamification score visibility | Emma | Done |
| P3 | Dry run 2 + video capture | All | Done |
| P3 | Screenshot refresh | Abigail | Done |
| P3 | README pass | Luis | Done |

---

## Definition of Done (Sprint 3) Check

- [x] `docs/Sprint 3/evaluation_rerun.md` shows 17+/20 feasibility pass on the original evaluation set
- [x] Waste reduction dashboard visible on user dashboard with formula breakdown
- [x] Loading indicator appears when the user submits a chat prompt and disappears when the response renders
- [x] At least one full team demo rehearsal completed with notes
- [x] Single-ingredient edge case either passes or is explicitly flagged as a known limitation
- [x] `normalize_quantity` and `convert_recipe_unit` share a single source of truth
- [x] Final demo script has per-step timings and speaker notes
- [x] Every team member has commits this sprint

Every box checked.

---

## Items to Complete by May 3 (Final Deliverables)

The May 3 package is required to be under `docs/Final_Demo/` in the repo. Save the following items there:

1. **Final demo slides** (PDF or PPTX) under `docs/Final_Demo/`. Cover: problem (food waste, expiry-aware planning), pipeline (pantry + chat + validator + gamification), evaluation results from `evaluation_rerun.md` (with images), live-demo plan.
2. **Runbook** at `docs/Final_Demo/Runbook.md`. Cover: prerequisites, env setup (`.env.example`), how to run Flask backend, how to seed the database (the new `01-build-db-new.py` / `02-insert-db-new.py` scripts), demo accounts (`demo`, `empty`, `expired`, `vegetarian`), how to use the inventory + chat + recipe + scoreboard pages, common errors.
3. **Final demo video** at `docs/Final_Demo/Final_Demo_Video.mp4`. The dry-run-2 video is a strong starting point. Polish if time allows.
4. **Final code on `main`**. Confirm `main` reflects the demo state.

Optional polish, not blocking:

5. **Move Sprint 3 docs into a sensible final structure**. Right now the team has `docs/Milestone 2 - Sprint 3/` as the home for evaluation, rehearsal, and demo script. For the final deliverables package, copy or symlink the key artifacts under `docs/Final_Demo/` so a grader can find everything in one place.
6. **Final eval consolidation**. Combine the M2 evaluation, Sprint 2 rerun, and Sprint 3 rerun into a single timeline doc that tells the "we measured, we fixed, we re-measured" story. Strong narrative for the final demo.

The team is in excellent shape going into the final demo and final deliverables. Keep the momentum.
